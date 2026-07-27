-- NOTICE: This file created by an LLM coding system on 2026-07-27.

-- Pandoc Lua filter: expands an empty ```schedule code block into the course
-- schedule table, read from docs/_data/schedule.csv. Jekyll renders the same
-- CSV into the homepage table via site.data.schedule, so the file is the one
-- source for both and neither table is ever committed by hand.

local CSV = PANDOC_SCRIPT_FILE:gsub("[^/]*$", "") .. "../docs/_data/schedule.csv"
local HEADERS = { "Week", "Class Day", "Topic", "Before Class", "In Class" }
local WIDTHS = { 0.06, 0.15, 0.38, 0.22, 0.19 }

-- Splits one CSV line, honoring "quoted, fields" and "" escapes.
local function split_line(line)
  local fields, pos = {}, 1
  while pos <= #line + 1 do
    local value
    if line:sub(pos, pos) == '"' then
      value, pos = "", pos + 1
      while pos <= #line do
        local char = line:sub(pos, pos)
        if char ~= '"' then
          value, pos = value .. char, pos + 1
        elseif line:sub(pos + 1, pos + 1) == '"' then
          value, pos = value .. '"', pos + 2
        else
          pos = pos + 1
          break
        end
      end
      pos = pos + 1
    else
      local comma = line:find(",", pos, true)
      value = comma and line:sub(pos, comma - 1) or line:sub(pos)
      pos = comma and comma + 1 or #line + 2
    end
    fields[#fields + 1] = value
  end
  return fields
end

local function read_rows()
  local handle = io.open(CSV, "r")
  if not handle then
    error("schedule.lua: cannot read " .. CSV)
  end

  local rows, header = {}, nil
  for line in handle:lines() do
    line = line:gsub("^\239\187\191", ""):gsub("\r$", "")
    if line ~= "" then
      local fields = split_line(line)
      if not header then
        header = fields
        for i, name in ipairs(HEADERS) do
          if header[i] ~= name then
            error("schedule.lua: " .. CSV .. " header must be: " .. table.concat(HEADERS, ", "))
          end
        end
      else
        rows[#rows + 1] = fields
      end
    end
  end
  handle:close()

  if #rows == 0 then
    error("schedule.lua: no schedule rows in " .. CSV)
  end
  return rows
end

local function markdown_table(rows)
  local lines = {
    "| " .. table.concat(HEADERS, " | ") .. " |",
    "|:-----|:----------|:------|:-------------|:---------|",
  }
  for _, row in ipairs(rows) do
    local cells = {}
    for i = 1, #HEADERS do
      cells[i] = (row[i] or ""):gsub("|", "\\|")
    end
    lines[#lines + 1] = "| " .. table.concat(cells, " | ") .. " |"
  end
  return table.concat(lines, "\n")
end

function CodeBlock(el)
  for _, class in ipairs(el.classes) do
    if class == "schedule" then
      local blocks = pandoc.read(markdown_table(read_rows()), "markdown").blocks
      local colspecs = {}
      for i, width in ipairs(WIDTHS) do
        colspecs[i] = { pandoc.AlignLeft, width }
      end
      blocks[1].colspecs = colspecs
      return blocks
    end
  end
  return nil
end
