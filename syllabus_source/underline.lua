-- NOTICE: This file modified by an LLM coding system on 2026-05-26.

-- Pandoc Lua filter:
-- - Turns spans with class "underline" into underline in LaTeX/PDF output.
-- - Preserves the class for HTML output so CSS can style it.

local function has_underline_class(el)
  local classes = el.classes
  if (not classes) and el.attr and el.attr.classes then
    classes = el.attr.classes
  end
  if not classes then return false end
  for _, c in ipairs(classes) do
    if c == "underline" then return true end
  end
  return false
end

function Span(el)
  if not has_underline_class(el) then
    return nil
  end

  if FORMAT:match("latex") then
    return pandoc.RawInline("latex", "\\underline{" .. pandoc.utils.stringify(el.content) .. "}")
  end

  -- For HTML (and other formats), keep as-is (class will come through).
  return nil
end

function Underline(el)
  if FORMAT:match("latex") then
    return pandoc.RawInline("latex", "\\underline{" .. pandoc.utils.stringify(el.content) .. "}")
  end

  if FORMAT:match("html") then
    return pandoc.Span(el.content, { class = "underline" })
  end

  return nil
end

function Table(el)
  local head_rows = el.head and el.head.rows
  if not head_rows or #head_rows == 0 then
    return nil
  end

  local header = head_rows[1]
  if not header or not header.cells or #header.cells < 5 then
    return nil
  end

  local labels = {}
  for i, cell in ipairs(header.cells) do
    labels[i] = pandoc.utils.stringify(cell)
  end

  if labels[1] == "Week"
    and labels[2] == "Class Day"
    and labels[3] == "Topic"
    and labels[4] == "Before Class"
    and labels[5] == "In Class" then
    el.colspecs = {
      { pandoc.AlignLeft, 0.06 },
      { pandoc.AlignLeft, 0.15 },
      { pandoc.AlignLeft, 0.38 },
      { pandoc.AlignLeft, 0.22 },
      { pandoc.AlignLeft, 0.19 },
    }
    return el
  end

  return nil
end
