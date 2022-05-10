layouts/shortcodes/bugs.html: data/bugs.json export.py
	mkdir -p layouts/shortcodes/
	python3 export.py > layouts/shortcodes/bugs.html
