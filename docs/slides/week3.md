---
format:
  revealjs:
    theme: theme/uic-orange-reveal.scss
    width: 1280
    height: 720
    margin: 0
    slide-number: c
    controls: true
    progress: true
    include-in-header:
      text: |
        <style>
        .reveal .footer p {
          gap: 40px;
        }
        .reveal .footer .footer-text {
          font-size: 0.94em;
          font-weight: 400;
        }
        .reveal .footer .footer-text a {
          font: inherit !important;
          color: inherit !important;
        }
        .reveal .sources h1 {
          font-size: 3.5rem;
        }
        .reveal .business-card-slide p {
          margin: 0;
          text-align: center;
        }
        .reveal .business-card-slide img {
          display: block;
          max-height: 470px;
          max-width: 88%;
          margin: 16px auto 0;
          object-fit: contain;
        }
        .reveal .section-header {
          display: flex !important;
          flex-direction: column;
          justify-content: center;
          text-align: center;
        }
        .reveal .section-header h1 {
          border-bottom: 12px solid #f9461c;
          display: inline-block;
          font-size: 5.6rem;
          margin: 0 auto;
          padding: 0 0 18px;
        }
        .reveal .spreadsheet-demo table {
          table-layout: fixed;
          width: 100%;
          max-width: 100%;
          font-size: 0.48em;
          line-height: 1.2;
        }
        .reveal .spreadsheet-demo th,
        .reveal .spreadsheet-demo td {
          overflow-wrap: anywhere;
          padding: 0.32em 0.42em;
        }
        .reveal .spreadsheet-demo th:first-child,
        .reveal .spreadsheet-demo td:first-child {
          width: 8%;
          color: #777;
          font-weight: 700;
          text-align: center;
        }
        .reveal .format-summary th,
        .reveal .format-summary td {
          overflow-wrap: anywhere;
          padding: 0.28em 0.4em;
        }
        .reveal .format-summary table {
          table-layout: fixed;
          width: 100%;
          max-width: 100%;
          font-size: 0.5em;
          line-height: 1.25;
        }
        .reveal .format-summary colgroup col:nth-child(1) {
          width: 11.11% !important;
        }
        .reveal .format-summary colgroup col:nth-child(2) {
          width: 44.44% !important;
        }
        .reveal .format-summary colgroup col:nth-child(3) {
          width: 44.44% !important;
        }
        .reveal .format-summary th:nth-child(1),
        .reveal .format-summary td:nth-child(1) {
          width: 11.11%;
        }
        .reveal .format-summary th:nth-child(2),
        .reveal .format-summary td:nth-child(2) {
          width: 44.44%;
        }
        .reveal .format-summary th:nth-child(3),
        .reveal .format-summary td:nth-child(3) {
          width: 44.44%;
        }
        .reveal .format-summary code {
          white-space: normal;
          font-size: 0.86em;
        }
        .reveal .columns ul {
          font-size: 0.78em;
          line-height: 1.45;
        }
        .reveal .columns .column > div.sourceCode,
        .reveal .columns .column > .code-copy-outer-scaffold,
        .reveal .columns .column > pre {
          margin-top: 1em;
        }
        .reveal pre code {
          font-size: 0.88em;
          line-height: 1.2;
        }
        .reveal .columns pre code {
          font-size: 0.88em;
          line-height: 1.2;
        }
        .reveal .code-caption {
          margin: 0.35em 0 0;
          text-align: center;
          font-size: 0.68em;
          font-style: italic;
          color: #666;
        }
        </style>
    footer: '<img src="../images/uic-black-logo.svg" alt="UIC logo"> <img src="../images/cc-by-nc-sa-small.svg" alt="CC BY-NC-SA"> <span class="footer-text">CS 418, Intro to Data Science, Week 3</span><span class="footer-text"><a href="https://dodatascience.fun/slides/week3.html">dodatascience.fun/slides/week3</a></span>'
slide-level: 1
---

# Week 3 Slide Deck {.course-title}

## Wrangling, Filtering; Formats

Jack Bandy
2026

---



# Data Formats {.section-header}

---

# How Do We Store This Data? {.business-card-slide}

![](../images/tyler-durden-business-card.png)

---


# Spreadsheet??

:::: {.columns}

::: {.column width="42%"}
- You've probably seen this
- Grid with cells, rows, columns (and sheets/tabs)
- Excel, Google Sheets, Numbers, and LibreOffice Calc
- Convenient for manual entry, review, sharing
- But don't keep your data in a spreadsheet...
:::

::: {.column width="58%"}
::: {.spreadsheet-demo}
|  | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | name | company | street | city | phone |
| 2 | Tyler Durden | Paper Street Soap Co. | 537 Paper Street | Bradford | (288) 555-0153 |
:::
:::

::::

---

# CSV

:::: {.columns}

::: {.column width="42%"}
- Comma-separated values
- Plain-text table: one row per record, one delimiter between fields
- Often used for spreadsheets, exports, and simple datasets
- Easy to inspect
- types and hierarchy are usually implicit
:::

::: {.column width="58%"}
```csv
name,company,product,street,city,postalCode,phone
Tyler Durden,Paper Street Soap Co.,All Natural Handmade,537 Paper Street,Bradford,19808,(288) 555-0153
```
:::

::::

---

# TSV

:::: {.columns}

::: {.column width="42%"}
- Tab-separated values
- Plain-text table like CSV, but fields are separated by tabs
- Still flat: hierarchy and data types need outside context
:::

::: {.column width="58%"}
```tsv
name	company	product	street	city	postalCode	phone
Tyler Durden	Paper Street Soap Co.	All Natural Handmade	537 Paper Street	Bradford	19808	(288) 555-0153
```
:::

::::

---

# JSON

:::: {.columns}

::: {.column width="42%"}
- JavaScript Object Notation
- Text format for data interchange
- Built from objects, arrays, strings, numbers, booleans, and null
- Common for web APIs and configuration files
:::

::: {.column width="58%"}
```json
{
  "name": "Tyler Durden",
  "company": "Paper Street Soap Co.",
  "product": "All Natural Handmade",
  "address": {
    "street": "537 Paper Street",
    "city": "Bradford",
    "postalCode": "19808"
  },
  "phone": "(288) 555-0153"
}
```
:::

::::

---

# XML

:::: {.columns}

::: {.column width="42%"}
- Extensible Markup Language
- Nested tags represent elements and attributes
- Verbose, but widely used by older document systems
:::

::: {.column width="58%"}
```xml
<?xml version="1.0" encoding="UTF-8"?>
<person>
  <name>Tyler Durden</name>
  <company>Paper Street Soap Co.</company>
  <product>All Natural Handmade</product>
  <address>
    <street>537 Paper Street</street>
    <city>Bradford</city>
    <postalCode>19808</postalCode>
  </address>
  <phone>(288) 555-0153</phone>
</person>
```
:::

::::

---



# YAML

:::: {.columns}

::: {.column width="42%"}
- YAML Ain't Markup Language
- Human-readable format based on indentation
- Supports mappings, lists, scalars, and comments
- Common for configuration files and data pipelines
:::

::: {.column width="58%"}
```yaml
name: Tyler Durden
company: Paper Street Soap Co.
product: All Natural Handmade
address:
  street: 537 Paper Street
  city: Bradford
  postalCode: 19808
phone: (288) 555-0153
```
:::

::::

---


# Parquet

:::: {.columns}

::: {.column width="42%"}
- Binary columnar storage format
- Efficient for large datasets
- Stores schema and data types with the data
- Common in Spark, DuckDB, Polars, and "data lakes"
:::

::: {.column width="58%"}
```text
message business_card {
  required binary name (STRING);
  required binary company (STRING);
  required binary product (STRING);
  required binary street (STRING);
  required binary city (STRING);
  required binary postalCode (STRING);
  required binary phone (STRING);
}

row 1:
Tyler Durden | Paper Street Soap Co. | All Natural Handmade |
537 Paper Street | Bradford | 19808 | (288) 555-0153
```
:::

::::

---


# What About More Complex Data? {.image-frame-slide}

::: {.content-visible when-format="html"}
![](../assets/three-dimensional-array/three-dimensional-array.svg)
:::

::: {.content-visible when-format="pdf"}
![](three-dimensional-array.svg)
:::

---


# NetCDF

:::: {.columns}

::: {.column width="42%"}
- Network Common Data Form
- Binary, self-describing format for array-oriented scientific data
- Stores dimensions, variables, and metadata together
- Better than CSV or JSON for gridded data with coordinates
- Common in scientific workflows (e.g. climate, ocean, weather)
- Harder to quickly inspect than plain text formats
	- (Data stored as binary)
:::

::: {.column width="58%"}
```text
dimensions:
  time = unlimited
  lat = 180
  lon = 360

variables:
  float temperature(time, lat, lon)
    temperature:units = "K"
    temperature:long_name = "air temperature"
  float lat(lat)
  float lon(lon)
```

<p class="code-caption">A simplified example of what a NetCDF file can contain.</p>
:::

::::

---

# Format Summary {.format-summary}

| Format | Best fit | Short example |
|---|---|---|
| CSV | Flat tables, spreadsheet exports, simple datasets | `name,company,phone`<br>`Tyler Durden,Paper Street Soap Co.,(288) 555-0153` |
| TSV | Flat text tables where commas may appear in fields | `name	company	phone` |
| JSON | APIs, nested records, web data | `{"name":"Tyler Durden","city":"Bradford"}` |
| XML | Document-like data with tags and attributes | `<name>Tyler Durden</name>` |
| YAML | Human-edited configuration and pipeline settings | `name: Tyler Durden`<br>`city: Bradford` |
| NetCDF | Labeled multi-dimensional scientific arrays | `temperature(time, lat, lon)` |
| Parquet | Typed, compressed analytics data | `name: STRING`<br>`city: STRING` |

---

# Sources {.sources}

1. GitHub source: <https://github.com/jackbandy/data-science-fun/blob/main/docs/slides/week3.md>.
2. NetCDF reference: Unidata netCDF documentation, <https://www.unidata.ucar.edu/software/netcdf/>.
3. LearningDS chapter 14, "Web Data," netCDF discussion: <https://learningds.org/ch/14/web_netCDF.html>.
4. Format examples adapted from Wikipedia and project documentation: [JSON](https://en.wikipedia.org/wiki/JSON), [XML](https://en.wikipedia.org/wiki/XML), [Comma-separated values](https://en.wikipedia.org/wiki/Comma-separated_values), [YAML](https://en.wikipedia.org/wiki/YAML), [Tab-separated values](https://en.wikipedia.org/wiki/Tab-separated_values), [Spreadsheet](https://en.wikipedia.org/wiki/Spreadsheet), and [Apache Parquet](https://parquet.apache.org/).
5. Tyler Durden business card image: Wikimedia Commons remake by Michaelpreid, modified, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), <https://commons.wikimedia.org/wiki/File:Tyler_Durden_Business_Card.png>.
6. Slides developed using materials from [Elena Zheleva](https://www.cs.uic.edu/~elena/) and [Gonzalo Bello Lander](https://cs.uic.edu/profiles/gonzalo-bello/), the Berkeley DS 100 team, Marine Carpuat, and Brian Ziebart.
7. Slide deck built with [Quarto](https://quarto.org/) revealjs.
8. Title font is Big Shoulders; Body font is [Libre Franklin](https://en.wikipedia.org/wiki/Franklin_Gothic#Libre_Franklin).
