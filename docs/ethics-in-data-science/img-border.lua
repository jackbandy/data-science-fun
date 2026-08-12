-- Hairline frame around figure images in LaTeX/PDF output.
-- The HTML side is handled by img.img-border in styles.css; CSS classes do
-- not survive into LaTeX, so the same .img-border class is translated here.

function Image(img)
  if not FORMAT:match("latex") then
    return nil
  end
  if not img.classes:includes("img-border") then
    return nil
  end
  return {
    pandoc.RawInline("latex",
      "{\\setlength{\\fboxrule}{0.4pt}\\setlength{\\fboxsep}{0pt}\\fbox{"),
    img,
    pandoc.RawInline("latex", "}}"),
  }
end
