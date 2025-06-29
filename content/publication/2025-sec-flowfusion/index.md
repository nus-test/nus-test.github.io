---
title: "Fuzzing the PHP Interpreter via Dataflow Fusion"
authors:
- Yuancheng Jiang
- Chuqi Zhang
- Bonan Ruan
- Jiahao Liu
- Manuel Rigger
- Roland Yap
- Zhenkai Liang
date: "2025-01-31T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2025-01-31T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: Proceedings of the 34th USENIX Conference on Security Symposium
publication_short: In *SEC 2025*

abstract: "PHP, a dominant scripting language in web development, powers a vast range of websites, from personal blogs to major platforms. While existing research primarily focuses on PHP application-level security issues like code injection, memory errors within the PHP interpreter have been largely overlooked. These memory errors, prevalent due to the PHP interpreter's extensive C codebase, pose significant risks to the confidentiality, integrity, and availability of PHP servers. This paper introduces FlowFusion, the first automatic fuzzing framework to detect memory errors in the PHP interpreter. FlowFusion leverages dataflow as an efficient representation of test cases maintained by PHP developers, merging two or more test cases to produce fused test cases with more complex code semantics. Moreover, FlowFusion employs strategies such as test mutation, interface fuzzing, and environment crossover to increase bug finding. In our evaluation, FlowFusion found 158 unknown bugs in the PHP interpreter, with 125 fixed and 11 confirmed. Comparing FlowFusion against the official test suite and a naive test concatenation approach, FlowFusion can detect new bugs that these methods miss, while also achieving greater code coverage. FlowFusion also outperformed state-of-the-art fuzzers AFL++ and Polyglot, covering 24% more lines of code after 24 hours of fuzzing. FlowFusion has gained wide recognition among PHP developers and is now integrated into the official PHP toolchain."

# Summary. An optional shortened abstract.
# summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

#tags:
#- Source Themes
#featured: true

#links:
#- name: Custom Link
#  url: http://example.org
url_pdf: https://www.arxiv.org/pdf/2410.12496
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

