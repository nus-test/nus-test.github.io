---
title: "Towards Efficient Build Ordering for Incremental Builds with Multiple Configurations"
authors:
- Jun Lyu
- Shanshan Li
- He Zhang
- Lanxin Yang
- Bohan Liu
- Manuel Rigger
date: "2024-07-12T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2024-07-12T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: In *Proceedings of the ACM on Software Engineering, Volume 1, Issue FSE*
publication_short: In *FSE 2024*

abstract: Software products have many configurations to meet different environments and diverse needs. Building software with multiple software configurations typically incurs high costs in terms of build time and computing resources. Incremental builds could reuse intermediate artifacts if configuration settings affect only a portion of the build artifacts. The efficiency gains depend on the strategic ordering of the incremental builds as the order influences which build artifacts can be reused. Deriving an efficient order is challenging and an open problem, since it is infeasible to reliably determine the degree of re-use and time savings before an actual build. In this paper, we propose an approach, called BUDDI—BUild Declaration DIstance, for C-based and Make-based projects to derive an efficient order for incremental builds from the static information provided by the build scripts (i.e., Makefile). The core strategy of BUDDI is to measure the distance between the build declarations of configurations and predict the build size of a configuration from the build targets and build commands in each configuration. Since some artifacts could be reused in the subsequent builds if there is a close distance between the build scripts for different configurations. We implemented BUDDI as an automated tool called BuddiPlanner and evaluated it on 20 popular open-source projects, by comparing it to a baseline that randomly selects a build order. The experimental results show that the order created by BuddiPlanner outperforms 96.5% (193/200) of the random build orders in terms of build time and reduces the build time by an average of 305.94s (26%) compared to the random build orders, with a median saving of 64.88s (28%). BuddiPlanner demonstrates its potential to relieve practitioners of excessive build times and computational resource burdens caused by building multiple software configurations.
# Summary. An optional shortened abstract.
# summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

#tags:
#- Source Themes
#featured: true

#links:
#- name: Custom Link
#  url: http://example.org
#url_pdf: https://arxiv.org/pdf/2404.13295
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

