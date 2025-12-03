---
# A Demo section created with the Blank widget.
# Any elements can be added in the body: https://wowchemy.com/docs/writing-markdown-latex/
# Add more sections by duplicating this file and customizing to your requirements.

widget: hero  # See https://wowchemy.com/docs/page-builder/
headless: true  # This file represents a page section.
weight: 10  # Order that this section will appear.
title: ""
subtitle: ""
hero_media: group-photos/group-2025-2.jpg  # TODO: figure out how to add an attribution caption (alt="Photo of the NUS TEST lab by Sun Changsheng")
design:
  # Choose how many columns the section has. Valid values: 1 or 2.
  columns: '1'
advanced:
  css_style:
  css_class:

---

<style>
.wg-hero .hero-media {
  flex-direction: column;
  position: relative;
}
.wg-hero .hero-media::before {
  content: '';
  background: url('/media/test.svg') no-repeat center;
  background-size: contain;
  width: 400px;
  height: 160px;
  display: block;
  margin-bottom: 20px;
}
/* Image swap on hover */
.wg-hero .hero-media img {
  transition: opacity 0.3s ease;
}
.wg-hero .hero-media::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: calc(100% - 180px); /* Exclude the logo area */
  background: url('/media/group-photos/group-2025-1.jpg') no-repeat center;
  background-size: cover;
  opacity: 0;
  transition: opacity 0.3s ease;
  pointer-events: none;
  border-radius: inherit;
}
.wg-hero .hero-media:hover img {
  opacity: 0;
}
.wg-hero .hero-media:hover::after {
  opacity: 1;
}
</style>

The *Trustworthy Engineering of Software Technologies (TEST) Lab*, part of the [PL/SE group](https://nus-plse.github.io/) at the [National University of Singapore](https://www.nus.edu.sg/) ([School of Computing](https://www.comp.nus.edu.sg/)), led by [Manuel Rigger](https://www.manuelrigger.at/), is working on practical and conceptual software solutions. We aim to have a real-world impact both by creating practical tools as well as by designing principled, fundamental techniques.


Core Areas:
* Software Engineering
* Systems
* Programming Languages
  
<!-- {{< figure src="group-photos/group-2025-1.jpg">}} -->


[{{<icon name="twitter" pack="fab" >}}](https://twitter.com/test_nus)
[{{<icon name="github" pack="fab" >}}](https://github.com/nus-test/)
[{{<icon name="envelope" pack="fas" >}}](mailto:rigger@comp.nus.edu.sg)

