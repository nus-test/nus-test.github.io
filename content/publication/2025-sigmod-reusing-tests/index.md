---
title: "Understanding and Reusing Test Suites Across Database Systems"
authors:
- Suyong Zhong
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

abstract: "Database Management System (DBMS) developers have implemented extensive test suites to test their DBMSs. For example, the SQLite test suites contain over 92 million lines of code. Despite these extensive efforts, test suites are not systematically reused across DBMSs, leading to wasted effort. Integration is challenging, as test suites use various test case formats and rely on unstandardized test runner features. We present a unified test suite, SQuaLity, in which we integrated test cases from three widely-used DBMSs, SQLite, PostgreSQL, and DuckDB. In addition, we present an empirical study to determine the potential of reusing these systems’ test suites. Our results indicate that reusing test suites is challenging: First, test formats and test runner commands vary widely; for example, SQLite has 4 test runner commands, while MySQL has 112 commands with additional features, to, for example, execute file operations or interact with a shell. Second, while some test suites contain mostly standard-compliant statements (e.g., 99% in SQLite), other test suites mostly test non-standardized functionality (e.g., 31% of statements in the PostgreSQL test suite are nonstandardized). Third, test reuse is complicated by various explicit and implicit dependencies, such as the need to set variables and configurations, certain test cases requiring extensions not present by default, and query results depending on specific clients. Despite the above findings, we have identified 3 crashes, 3 hangs, and multiple compatibility issues across four different DBMSs by executing test suites across DBMSs, indicating the benefits of reuse. Overall, this work represents the first step towards test-case reuse in the context of DBMSs, and we hope that it will inspire follow-up work on this important topic."

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

