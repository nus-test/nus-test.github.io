---
title: "Testing Graph Database Engines via Query Partitioning"
authors:
- Matteo Kamm
- Manuel Rigger
- Chengyu Zhang
- Zhendong Su
date: "2022-12-09T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2017-01-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: In *32nd ACM SIGSOFT International Symposium on Software Testing and Analysis*
publication_short: In *ISSTA 2023*

abstract: Graph Database Management Systems (GDBMSs) store data as graphs and allow the efficient querying of nodes and their relationships. Logic bugs are bugs that cause a GDBMS to return an incorrect result for a given query (e.g., by returning incorrect nodes or relationships). The impact of such bugs can be severe, as they often go unnoticed. The core insight of this paper is that Query Partitioning, a test oracle that has been proposed to test Relational Database Systems, is applicable to testing GDBMSs as well. The core idea of Query Partitioning is that, given a query, multiple queries are derived whose results can be combined to reconstruct the given query’s result. Any discrepancy in the result indicates a logic bug. We have implemented this approach as a practical tool named GDBMeter and evaluated GDBMeter on three popular GDBMSs and found a total of 41 unique, previously unknown bugs. We consider 14 of them to be logic bugs, the others being error or crash bugs. Overall, 27 of the bugs have been fixed, and 35 confirmed. We compared our approach to the state-of-the-art approach to testing GDBMS, which relies on differential testing; we found that it results in a high number of false alarms, while Query Partitioning reported actual logic bugs without any false alarms. Furthermore, despite the previous efforts in testing Neo4j and JanusGraph, we found 13 additional bugs. The developers appreciate our work and plan to integrate GDBMeter into their testing process. We expect that this simple, yet effective approach and the practical tool will be used to test other GDBMSs.
# Summary. An optional shortened abstract.
# summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

#tags:
#- Source Themes
#featured: true

#links:
#- name: Custom Link
#  url: http://example.org
#url_pdf: http://eprints.soton.ac.uk/352095/1/Cushen-IMV2013.pdf
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
#- internal-project

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

