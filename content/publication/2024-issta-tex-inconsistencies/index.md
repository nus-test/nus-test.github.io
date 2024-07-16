---
title: "Inconsistencies in TeX-produced Documents"
authors:
- Jovyn Tan
- Manuel Rigger
date: "2024-07-16T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2000-12-15T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: In *Proceedings of the 33rd ACM SIGSOFT International Symposium on Software Testing and Analysis*
publication_short: In *ISSTA 2024*

abstract: 'TeX is a widely-used typesetting system adopted by most publishers and professional societies. While TeX is responsible for generating a significant number of documents, irregularities in the TeX ecosystem may produce inconsistent documents. These inconsistencies may occur across different TeX engines or different versions of TeX distributions, resulting in failures to adhere to formatting specifications, or the same document rendering differently for different authors. In this work, we investigate and quantify the robustness of the TeX ecosystem through a large-scale study of 432 documents. We developed an automated pipeline to evaluate the cross-engine and cross-version compatibility of the TeX ecosystem. We found significant inconsistencies in the outputs of different TeX engines: only 0.2% of documents compiled to identical output with XeTeX and PDFTeX due to a lack of cross-engine support in popular LaTeX packages and classes used in academic conferences. A smaller—yet significant—extent of inconsistencies was found across different TeX Live distributions, with only 42.1% of documents producing the same output from 2020 to 2023. Our automated pipeline additionally reduces the human effort in bug-finding: from a sample of 10 unique root causes of inconsistencies, we identified two new bugs in LaTeX packages and five existing bugs that were fixed independently of this study. We also observed potentially unintended inconsistencies across different TeX Live distributions beyond the updates listed in changelogs. We expect that this study will help authors of TeX documents to avoid unexpected outcomes by understanding how they may be affected by the often undocumented subtleties of the TeX ecosystem, while benefiting developers by demonstrating how different implementations result in unintended inconsistencies.'

# Summary. An optional shortened abstract.
# summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

#tags:
#- Source Themes
#featured: true

#links:
#- name: Custom Link
#  url: http://example.org
#url_pdf: ''
#url_code: '#'
#url_dataset: '#'
#url_poster: '#'
#url_project: ''
#url_slides: ''
#url_source: '#'
#url_video: '#'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
#image:
#  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/pLCdAaMFLTE)'
#  focal_point: ""
# preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
#projects:
#- sqlancer

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
#slides:

# move below
#{{% callout note %}}
#Click the *Cite* button above to demo the feature to enable visitors to import publication metadata into their reference management software.
#{{% /callout %}}

#Supplementary notes can be added here, including [code and math](https://sourcethemes.com/academic/docs/writing-markdown-latex/).

---

