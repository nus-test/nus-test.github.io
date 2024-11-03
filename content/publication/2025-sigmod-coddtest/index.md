---
title: "Constant Optimization Driven Database System Testing"
authors:
- Chi Zhang
- Manuel Rigger
date: "2024-11-03T00:00:00Z"
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

abstract: "Logic bugs are bugs that can cause database management systems (DBMSs) to silently produce incorrect results for given queries. Such bugs are severe, because they can easily be overlooked by both developers and users, and can cause applications that rely on the DBMSs to malfunction. In this work, we propose Constant-Optimization-Driven Database Testing (CODDTest) as a novel approach for detecting logic bugs in DBMSs. This method draws inspiration from two well-known optimizations in compilers: constant folding and constant propagation. Our key insight is that for a certain database state and query containing a predicate, we can apply constant folding on the predicate by replacing an expression in the predicate with a constant, anticipating that the results of this predicate remain unchanged; any discrepancy indicates a bug in the DBMS. We evaluated CODDTest on five mature and extensively-tested DBMSs–SQLite, MySQL, CockroachDB, DuckDB, and TiDB–and found 45 unique, previously unknown bugs in them. Out of these, 24 are unique logic bugs. Our manual analysis of the state-of-the-art approaches indicates that 11 logic bugs are detectable only by CODDTest. We believe that CODDTest is easy to understand and implement, and can be widely adopted in practice."

# Summary. An optional shortened abstract.
# summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

#tags:
#- Source Themes
#featured: true

#links:
#- name: Custom Link
#  url: http://example.org
#url_pdf: https://arxiv.org/pdf/2410.21731
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

