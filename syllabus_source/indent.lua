-- NOTICE: This file created by an LLM coding system on 2026-08-31.

-- Pandoc Lua filter: renders a fenced div with class "indented" as a block set
-- slightly in from the left margin, for details that belong to the label above
-- them. Pandoc's LaTeX writer drops generic divs, so the indent has to be
-- re-applied here as the indentblock environment from template.tex; the HTML
-- build keeps the div and gets the same indent from CSS (template.html).

function Div(el)
  if not (FORMAT:match("latex") and el.classes:includes("indented")) then
    return nil
  end

  local out = pandoc.List({ pandoc.RawBlock("latex", "\\begin{indentblock}") })
  out:extend(el.content)
  out:insert(pandoc.RawBlock("latex", "\\end{indentblock}"))
  return out
end
