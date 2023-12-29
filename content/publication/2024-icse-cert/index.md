---
title: "CERT: Finding Performance Issues in Database Systems Through the Lens of Cardinality Estimation"
authors:
- Jinsheng Ba
- Manuel Rigger
date: "2023-10-10T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2017-01-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["3"]

# Publication name and optional abbreviated publication name.
publication: In *Proceedings of the 46th International Conference on Software Engineering*
publication_short: In *ICSE 2024*

abstract: Database Management Systems (DBMSs) process a given query by creating an execution plan, which is subsequently executed, to compute the query's result. Deriving an efficient query plan is challenging, and both academia and industry have invested decades into researching query optimization. Despite this, DBMSs are prone to performance issues, where a DBMS produces an inefficient query plan that might lead to the slow execution of a query. Finding such issues is a longstanding problem and inherently difficult, because no ground truth information on an expected execution time exists. In this work, we propose Cardinality Estimation Restriction Testing (CERT), a novel technique that detects performance issues through the lens of cardinality estimation. Given a query on a database, CERT derives a more restrictive query (e.g., by replacing a LEFT JOIN with an INNER JOIN), whose estimated number of rows should not exceed the number of estimated rows for the original query. CERT tests cardinality estimators specifically, because they were shown to be the most important component for query optimization; thus, we expect that finding and fixing such issues might result in the highest performance gains. In addition, we found that some other kinds of query optimization issues are exposed by the unexpected cardinality estimation, which can also be detected by CERT. CERT is a black-box technique that does not require access to the source code; DBMSs expose query plans via the EXPLAIN statement. CERT eschews executing queries, which is costly and prone to performance fluctuations. We evaluated CERT on three widely used and mature DBMSs, MySQL, TiDB, and CockroachDB. CERT found 13 unique issues, of which 2 issues were fixed and 9 confirmed by the developers. We expect that this new angle on finding performance bugs will help DBMS developers in improving DMBSs' performance.
# Summary. An optional shortened abstract.
# summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

#tags:
#- Source Themes
#featured: true

#links:
#- name: Custom Link
#  url: http://example.org
url_pdf: https://arxiv.org/pdf/2306.00355.pdf
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
projects:
- sqlancer

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

