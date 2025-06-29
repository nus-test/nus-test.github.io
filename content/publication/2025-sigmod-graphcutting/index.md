---
title: "Finding Logic Bugs in Graph-processing Systems via Graph-cutting"
authors:
- Qiuyang Mang
- Jinsheng Ba
- Pinjia He
- Manuel Rigger
date: "2025-06-18T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2025-06-18T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: Proceeding of ACM Management of Data
publication_short: In *SIGMOD 2025*

abstract: "Graph-processing systems, including Graph Database Management Systems (GDBMSes) and graph libraries, are designed to analyze and manage graph data efficiently. They are widely used in applications such as social networks, recommendation systems, and fraud detection. However, logic bugs in these systems can lead to incorrect results, compromising the reliability of applications. While recent research has explored testing techniques specialized for GDBMSes, it is unclear how to adapt them to graph-processing systems in general. This paper proposes Graph-cutting, a universal approach for detecting logic bugs in both GDBMSes and various algorithms in graph libraries. Our key idea is inspired by the observation that certain graph patterns are critical for various graph-processing tasks. Dividing graph data into subgraphs that preserve those patterns establishes a natural relationship between query results on the original graph and its subgraphs, allowing for the detection of logic bugs when this relationship is violated. We implemented Graph-cutting as a tool, GSlicer, and evaluated it on 3 popular graph-processing systems, NetworkX, Neo4j, and Kùzu. GSlicer detected 39 unique and previously unknown bugs, out of which 34 have been fixed and confirmed by developers. At least 8 logic bugs detected by GSlicer cannot be detected by baseline strategies. Additionally, by leveraging just a few concrete relationships, Graph-cutting can cover over 100 APIs in NetworkX. We expect this technique to be widely applicable and that it can be used to improve the quality of graph-processing systems broadly."

# Summary. An optional shortened abstract.
# summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

#tags:
#- Source Themes
#featured: true

#links:
#- name: Custom Link
#  url: http://example.org
#url_pdf: https://arxiv.org/pdf/2410.21731
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

