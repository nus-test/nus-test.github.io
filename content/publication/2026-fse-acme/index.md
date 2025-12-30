---
title: "ACME: Automated Clause Mapping Engine for Testing Emerging Database Systems"
authors:
- Yuancheng Jiang
- Jianing Wang
- Chuqi Zhang
- Roland Yap
- Zhenkai Liang
- Manuel Rigger
date: "2025-12-30T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2000-12-15T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: The ACM International Conference on the Foundations of Software Engineering (FSE)
publication_short: In *FSE 2026*

abstract: "A growing number of emerging database management systems, such as time-series and streaming databases, have been developed to support specialized workloads with enhanced performance and functionality. However, these systems are often less mature than traditional relational databases, making them more prone to logic bugs and internal errors that affect correctness and reliability. To address this, we propose an enhanced differential testing framework designed for emerging SQL-like databases. Our key insight is that many of these systems are conceptually extensions of relational databases, allowing us to uncover bugs by comparing query results with those from more robust relational systems. To bridge the differences in syntax and semantics between emerging and relational databases, we leverage Large Language Models (LLMs) to automate the discovery of supported clauses and generate clause mappings that translate system-specific features into equivalent expressions in SQL. Our approach proceeds in three steps: (i) collecting and analyzing the syntax of clauses supported by both the emerging database system and a relational reference system, (ii) constructing clause mappings via LLMs, validating them through testing queries, and formalizing them into Abstract Syntax Tree (AST) transformations or mapping functions, and (iii) generating semantically equivalent but syntactically varied queries to expand the scope of differential testing. To ensure the reliability of LLM-generated clause mappings, we introduce a testing query mechanism that re-prompts incorrect mappings after runtime verification. We implemented this approach in a tool called ACME and applied it to four widely used emerging database systems, uncovering 57 previously unknown bugs, including 17 logic bugs and 40 internal errors. Of these, 50 have been fixed and 5 confirmed by vendors. Our results demonstrate the practicality and effectiveness of ACME in improving the reliability of emerging database systems through scalable, LLM-assisted differential testing."

# Summary. An optional shortened abstract.
# summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

#tags:
#- Source Themes
#featured: true

#links:
#- name: Custom Link
#  url: http://example.org
url_pdf: https://arxiv.org/pdf/2501.01236
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

