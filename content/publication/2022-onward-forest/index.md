---
title: "Forest: Structural Code Editing with Multiple Cursors"
authors:
- Philippe Voinov
- Manuel Rigger
- Zhendong Su
date: "2022-10-03T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2017-01-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: In *Proceedings of the 2022 ACM SIGPLAN International Symposium on New Ideas, New Paradigms, and Reflections on Programming and Software*
publication_short: In *Onward! 2022*

abstract: Software developers frequently refactor code. Often, a single logical refactoring change involves changing multiple related components in a source base such as renaming each occurrence of a variable or function. While many code editors can perform such common and generic refactorings, they do not support more complex refactorings or those that are specific to a given code base. For those, as a flexible — albeit less interactive — alternative, developers can write refactoring scripts that can implement arbitrarily complex logic by manipulating the program's tree representation. In this work, we present Forest, a structural code editor that aims to bridge the gap between the interactiveness of code editors and the expressiveness of refactoring scripts. While structural editors have occupied a niche as general code editors, the key insight of this work is that they enable a novel structural multi-cursor design that allows Forest to reach a similar expressiveness as refactoring scripts; Forest allows to perform a single action simultaneously in multiple program locations and thus support complex refactorings. To support interactivity, Forest provides features typical for text code editors such as writing and displaying the program through its textual representation. Our evaluation demonstrates that Forest allows performing edits similar to those from refactoring scripts, while still being interactive. We attempted to perform edits from 48 real-world refactoring scripts using Forest and found that 11 were possible, while another 17 would be possible with added features. We believe that a multi-cursor setting plays to the strengths of structural editing, since it benefits from reliable and expressive. Our results suggest that multi-cursor structural editors could be practical for performing small-scale specialized refactorings.
# Summary. An optional shortened abstract.
# summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

#tags:
#- Source Themes
#featured: true

#links:
#- name: Custom Link
#  url: http://example.org
url_pdf: https://arxiv.org/pdf/2210.11124
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

