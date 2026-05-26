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
