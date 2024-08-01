---
title: "Finding Logic Bugs in Spatial Database Engines via Affine Equivalent Inputs"
authors:
- Wenjing Deng
- Qiuyang Mang
- Chengyu Zhang
- Manuel Rigger
date: "2024-08-01T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2000-12-15T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: Proceeding of ACM Management of Data
publication_short: In *SIGMOD 2025*

abstract: "Spatial Database Management Systems (SDBMSs) aim to store, manipulate, and retrieve spatial data. SDBMSs are employed in various modern applications, such as geographic information systems, computer-aided design tools, and location-based services. However, the presence of logic bugs in SDBMSs can lead to incorrect results, substantially undermining the reliability of these applications. Detecting logic bugs in SDBMSs is challenging due to the lack of ground truth for identifying incorrect results. In this paper, we propose an automated geometry-aware generator to generate high-quality SQL statements for SDBMSs and a novel concept named Affine Equivalent Inputs (AEI) to validate the results of SDBMSs. We implemented them as a tool named Spatter (Spatial DBMS Tester) for finding logic bugs in four popular SDBMSs: PostGIS, DuckDB Spatial, MySQL, and SQL Server. Our testing campaign detected 34 previously unknown and unique bugs in these SDBMSs, of which 30 have been confirmed, and 18 have already been fixed. Our testing efforts have been well appreciated by the developers. Experimental results demonstrate that the geometry-aware generator significantly outperforms a naive random-shape generator in detecting unique bugs, and AEI can identify 14 logic bugs in SDBMSs that were overlooked by previous methodologies."

# Summary. An optional shortened abstract.
# summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

#tags:
#- Source Themes
#featured: true

#links:
#- name: Custom Link
#  url: http://example.org
#url_pdf: https://bajinsheng.github.io/assets/pdf/dqp_sigmod24.pdf
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

