---
title: "Towards a Unified Query Plan Representation"
authors:
- Jinsheng Ba
- Manuel Rigger
date: "2025-03-27T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2000-12-15T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: Proceeding of IEEE 40th International Conference on Data Engineering
publication_short: In *ICDE 2025*

abstract: "In database systems, a query plan is a series of concrete internal steps to execute a query. Multiple testing approaches utilize query plans for finding bugs. However, query plans are represented in a database-specific manner, so implementing these testing approaches requires a non-trivial effort, hindering their adoption. We envision that a unified query plan representation can facilitate the implementation of these approaches. In this paper, we present an exploratory case study to investigate query plan representations in nine widely-used database systems. Our study shows that query plan representations consist of three conceptual components: operations, properties, and formats, which enable us to design a unified query plan representation. Based on it, existing testing methods can be efficiently adopted, finding 17 previously unknown and unique bugs. Additionally, the unified query plan representation can facilitate other applications. Existing visualization tools can support multiple database systems based on the unified query plan representation with moderate implementation effort, and comparing unified query plans across database systems provides actionable insights to improve their performance. We expect that the unified query plan representation will enable the exploration of additional application scenarios."

# Summary. An optional shortened abstract.
# summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

#tags:
#- Source Themes
#featured: true

#links:
#- name: Custom Link
#  url: http://example.org
url_pdf: https://arxiv.org/pdf/2408.07857v2
#url_code: '#'
#url_dataset: '#'
#url_poster: '#'
url_project: https://nus-test.github.io/uplan/
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

