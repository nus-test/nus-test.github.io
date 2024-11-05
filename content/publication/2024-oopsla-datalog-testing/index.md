---
title: "Finding Cross-rule Optimization Bugs in Datalog Engines"
authors:
- Chi Zhang
- Linzhang Wang
- Manuel Rigger
date: "2023-12-23T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2023-12-15T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: In *Proc. ACM Program. Lang.*
publication_short: In *OOPSLA 2024*

# abstract: Database systems are widely used to store and query data. Test oracles have been proposed to find logic bugs in such systems, that is, bugs that cause the database system to compute an incorrect result. To realize a fully automated testing approach, such test oracles are paired with a test case generation technique; a test case refers to a database state and a query on which the test oracle can be applied. In this work, we propose the concept of Query Plan Guidance (QPG) for guiding automated testing towards "interesting" test cases. SQL and other query languages are declarative. Thus, to execute a query, the database system translates every operator in the source language to one of potentially many so-called physical operators that can be executed; the tree of physical operators is referred to as the query plan. Our intuition is that by steering testing towards exploring diverse query plans, we also explore more interesting behaviors—some of which are potentially incorrect. To this end, we propose a mutation technique that gradually applies promising mutations to the database state, causing the DBMS to create diverse query plans for subsequent queries. We applied our method to three mature, widely-used, and extensively-tested database systems—SQLite, TiDB, and CockroachDB—and found 53 unique, previously unknown bugs. Our method exercises 4.85—408.48× more unique query plans than a naive random generation method and 7.46× more than a code coverage guidance method. Since most database systems—including commercial ones—expose query plans to the user, we consider QPG a generally applicable, black-box approach and believe that the core idea could also be applied in other contexts (e.g., to measure the quality of a test suite).
# Summary. An optional shortened abstract.
# summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

#tags:
#- Source Themes
#featured: true

#links:
#- name: Custom Link
#  url: http://example.org
url_pdf: https://dl.acm.org/doi/pdf/10.1145/3649815
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

