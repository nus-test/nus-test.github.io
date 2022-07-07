layouts/shortcodes/bugs.html: data/bugs.json export.py
	mkdir -p layouts/shortcodes/
	python3 export.py > layouts/shortcodes/bugs.html

update:
	python3 update.py > data/bugs2.json
	mv data/bugs2.json data/bugs.json
