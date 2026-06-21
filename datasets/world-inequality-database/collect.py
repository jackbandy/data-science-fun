"""
Download income share time series from the World Inequality Database (WID.world).

Uses the WID internal REST API (discovered from the open-source wid-r-tool package).
API base: https://rfap9nitz6.execute-api.eu-west-1.amazonaws.com/prod/

Variables collected (pre-tax national income share, sptinc):
  top1_share    = top 1%  (p99p100)
  top10_share   = top 10% (p90p100)
  bottom50_share = bottom 50% (p0p50)

Countries: US, FR, DE, GB, SE, CN, IN, BR, ZA (9 countries; no global aggregate available)

Note on methodology: WID records different population-unit conventions per country.
The 'pop_code' column in the output shows which was used (i = equal-split individuals,
j = fiscal/joint units, t = tax units). Cross-country comparisons should account for
this when the same indicator is measured differently across countries.

Output: wid-income-shares.csv
"""

import base64
import json
import urllib.request
import csv

API_KEY_HEX = "ad 81 41 c8 e0 74 8a 86 8f 01 3c 07 b6 59 4c 23 bd 73 2c e6 52 2b 42 1c e6 f7 90 a2 72 4f"
API_BASE = "https://rfap9nitz6.execute-api.eu-west-1.amazonaws.com/prod/"

key_bytes = bytes([int(x, 16) for x in API_KEY_HEX.split()])
API_KEY = base64.b64encode(key_bytes).decode()

COUNTRIES = {
    "US": "United States",
    "FR": "France",
    "DE": "Germany",
    "GB": "United Kingdom",
    "SE": "Sweden",
    "CN": "China",
    "IN": "India",
    "BR": "Brazil",
    "ZA": "South Africa",
}

PERCENTILES = {
    "top1_share":     "p99p100",
    "top10_share":    "p90p100",
    "bottom50_share": "p0p50",
}

# Population-unit conventions differ by country on WID.
# We probe in preference order and take the format with the most data.
POP_AGE_CANDIDATES = [
    ("999", "i"),  # all ages, equal-split individuals (common for US)
    ("999", "j"),  # all ages, fiscal/joint units (common for EU, Asia)
    ("992", "i"),  # adults, equal-split individuals (France)
    ("992", "t"),  # adults, tax units
    ("999", "t"),  # all ages, tax units
]


def fetch_variable(country, variable_code):
    url = (
        API_BASE
        + f"countries-variables?countries={country}&variables={variable_code}&years=all"
    )
    req = urllib.request.Request(url, headers={"x-api-key": API_KEY})
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def best_series(country, ptile_code):
    """Return (variable_code, pop_code, rows) for the pop/age format with most data."""
    best_n, best_var, best_pop, best_rows = 0, None, None, []
    for age, pop in POP_AGE_CANDIDATES:
        var = f"sptinc_{ptile_code}_{age}_{pop}"
        data = fetch_variable(country, var)
        blocks = data.get(var, [])
        rows = []
        for block in blocks:
            for values in block.values():
                rows.extend(values["values"])
        if len(rows) > best_n:
            best_n = len(rows)
            best_var, best_pop, best_rows = var, f"{age}_{pop}", rows
    return best_var, best_pop, best_rows


output_rows = []
for country_code, country_name in COUNTRIES.items():
    print(f"  {country_code} …", end="", flush=True)
    for label, ptile in PERCENTILES.items():
        var, pop_code, values = best_series(country_code, ptile)
        print(f" {label}({len(values)})", end="", flush=True)
        for entry in values:
            output_rows.append({
                "country":      country_code,
                "country_name": country_name,
                "year":         entry["y"],
                "variable":     label,
                "value":        round(entry["v"], 6),
                "pop_code":     pop_code,
            })
    print()

output_rows.sort(key=lambda r: (r["country"], r["variable"], r["year"]))

outfile = "wid-income-shares.csv"
with open(outfile, "w", newline="") as f:
    writer = csv.DictWriter(
        f, fieldnames=["country", "country_name", "year", "variable", "value", "pop_code"]
    )
    writer.writeheader()
    writer.writerows(output_rows)

print(f"\nWrote {len(output_rows)} rows to {outfile}")
