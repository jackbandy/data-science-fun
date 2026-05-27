#!/usr/bin/env python3
# Modified by an LLM coding system.

from pathlib import Path
import datetime as dt
import struct
import numpy as np

BASE = Path(__file__).resolve().parent
LINES = BASE / "Metra_Lines" / "MetraLinesshp"
STATIONS = BASE / "Metra_Stations" / "MetraStations"
DROP_FIELDS = ("GEOMETRY_WKT",)
DROP_FIELDS_LABEL = "geometry_wkt"


def esc(v):
    """Quote a value for CSV output when needed."""
    value = "" if v is None else str(v)
    return '"' + value.replace('"', '""') + '"' if any(c in value for c in ',\"\n') else value


def parse_dbf(path):
    """Read DBF fields and rows into plain Python values."""
    dbf_bytes = path.read_bytes()
    total_rows, header_bytes, record_bytes = struct.unpack_from("<IHH", dbf_bytes, 4)
    fields, offset = [], 32
    while dbf_bytes[offset] != 0x0D:
        fields.append(
            (
                dbf_bytes[offset : offset + 11].split(b"\0", 1)[0].decode().strip(),
                chr(dbf_bytes[offset + 11]),
                dbf_bytes[offset + 16],
                dbf_bytes[offset + 17],
            )
        )
        offset += 32
    fields = [f for f in fields if f[0].upper() not in DROP_FIELDS]
    rows = []
    for row_index in range(total_rows):
        row_offset = header_bytes + row_index * record_bytes
        if dbf_bytes[row_offset] == 0x2A:
            continue
        field_offset = row_offset + 1
        row = []
        for _, field_type, field_length, decimal_count in fields:
            raw_value = dbf_bytes[field_offset : field_offset + field_length].decode("latin1").strip()
            field_offset += field_length
            row.append(parse_val(raw_value, field_type, decimal_count))
        rows.append(row)
    return [f[0] for f in fields], rows, total_rows


def parse_val(value, field_type, decimal_count):
    """Convert a DBF field value from text to a Python type."""
    if not value:
        return ""
    if field_type == "D":
        try:
            return dt.date(int(value[:4]), int(value[4:6]), int(value[6:8])).isoformat()
        except Exception:
            return value
    if field_type in {"N", "F"}:
        try:
            return int(value) if "." not in value and not decimal_count else float(value)
        except Exception:
            return value
    if field_type == "L":
        return value.upper() in {"Y", "T"}
    return value


def save_csv(base, out):
    """Write one shapefile's attributes to CSV."""
    columns, rows, total_rows = parse_dbf(base.with_suffix(".dbf"))
    data = [[esc(v) for v in row] for row in rows]
    array = np.array([list(map(esc, columns))] + data, dtype=object)
    np.savetxt(out, array, fmt="%s", delimiter=",", newline="\n")
    return total_rows, len(data)


def main():
    original_rows, output_rows = save_csv(LINES, BASE / "metra_lines.csv")
    print("metra_lines:")
    print(f"  original rows={original_rows}")
    print(f"  output rows={output_rows}")
    print(f"  dropped fields={DROP_FIELDS_LABEL}")

    original_rows, output_rows = save_csv(STATIONS, BASE / "metra_stations.csv")
    print("metra_stations:")
    print(f"  original rows={original_rows}")
    print(f"  output rows={output_rows}")
    print(f"  dropped fields={DROP_FIELDS_LABEL}")


if __name__ == "__main__":
    main()
