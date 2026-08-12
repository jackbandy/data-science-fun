-- Turn raw <br> tags into real Pandoc line breaks.
-- Table cells cannot contain newlines, so multi-line cells (e.g. the ACM
-- competency table in the preface) separate entries with <br>. Raw HTML is
-- dropped in LaTeX output, which runs the entries together in the PDF; a
-- LineBreak renders correctly in both HTML and LaTeX.

function RawInline(el)
  if el.format:match("html") and el.text:match("^%s*<%s*[bB][rR]%s*/?%s*>%s*$") then
    return pandoc.LineBreak()
  end
  return nil
end
