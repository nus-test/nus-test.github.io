---
title: "Metamorphic Coverage"
authors:
- Jinsheng Ba
- Yuancheng Jiang
- Manuel Rigger
date: "2026-06-23T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2000-12-15T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: In *Proceedings of the 35rd ACM SIGSOFT International Symposium on Software Testing and Analysis*
publication_short: In *ISSTA 2026*

abstract: 'Metamorphic testing is a widely used methodology that examines an expected relation between pairs of executions to automatically find bugs, such as correctness bugs. We found that code coverage cannot accurately measure the extent to which code is validated and mutation testing is computationally expensive for evaluating metamorphic testing methods. In this work, we propose Metamorphic Coverage (MC), a coverage metric that examines the distinct code executed by pairs of test inputs within metamorphic testing. Our intuition is that, typically, a bug can be observed if the corresponding code is executed when executing either test input but not the other one, so covering more differential code covered by pairs of test inputs might be more likely to expose bugs. While most metamorphic testing methods have been based on this general intuition, our work defines and systematically evaluates MC on five widely used metamorphic testing methods for testing database engines, compilers, and constraint solvers. The code measured by MC overlaps with the bug-fix locations of 50 of 64 bugs found by metamorphic testing methods, and MC has a stronger positive correlation with bug numbers than line coverage. MC is 4x more sensitive than line coverage in distinguishing testing methods effectiveness, and the average value of MC is 6x smaller than line coverage while still capturing the part of the program that is being tested. MC required 359x less time than mutation testing. Based on a case study for an automated database system testing approach, we demonstrate that when used for feedback guidance, MC significantly outperforms code coverage, by finding 41% more bugs. Consequently, this work might have broad applications for assessing metamorphic testing methods and improving test-case generation.'

# Summary. An optional shortened abstract.
# summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

#tags:
#- Source Themes
#featured: true

#links:
#- name: Custom Link
#  url: http://example.org
url_pdf: https://arxiv.org/pdf/2508.16307
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

