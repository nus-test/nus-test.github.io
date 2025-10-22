#!/usr/bin/env python3
"""
generate_event_md_precise.py

Create a markdown file matching the project's event template as closely as possible.

Behavior:
- Reads a JSON input containing fields like title, date, date_end, authors, location,
  summary, abstract, speaker_info.
- Produces a markdown file with front matter and comment blocks similar to existing files.
- Defaults: event -> "Weekly Talk", event_url -> "", address subkeys empty, country default to "Singapore"
- Filename: YYMMDD.md derived from date field (or today if absent)
- Won't overwrite an existing file unless --force is passed.

Usage:
  python3 scripts/generate_event_md_precise.py input.json output_dir/ [--force]
"""
from pathlib import Path
import sys
import json
from datetime import datetime, date


def parse_date_for_filename(date_str: str) -> str:
    if not date_str:
        dt = datetime.utcnow()
    else:
        s = date_str
        if s.endswith('Z'):
            s = s[:-1]
        try:
            dt = datetime.fromisoformat(s)
        except Exception:
            try:
                dt = datetime.strptime(s, '%Y-%m-%d')
            except Exception:
                dt = datetime.utcnow()
    return dt.strftime('%y%m%d')


def iso_midnight_of(date_obj: datetime) -> str:
    # Return YYYY-MM-DDT00:00:00Z for a given date or now
    if isinstance(date_obj, str):
        try:
            dt = datetime.fromisoformat(date_obj.rstrip('Z'))
        except Exception:
            dt = datetime.utcnow()
    elif isinstance(date_obj, datetime):
        dt = date_obj
    else:
        dt = datetime.utcnow()
    return dt.strftime('%Y-%m-%dT00:00:00Z')


def build_markdown(data: dict) -> str:
    # Fields mapping
    title = data.get('title', '')
    event = data.get('event', 'Weekly Talk') or 'Weekly Talk'
    event_url = data.get('event_url', '') or ''
    location = data.get('location', '')

    address = data.get('address', {}) or {}
    # ensure subkeys
    addr_keys = ['street', 'city', 'region', 'postcode', 'country']
    for k in addr_keys:
        if k not in address:
            # default country to Singapore if unspecified
            address[k] = 'Singapore' if k == 'country' else ''

    summary = data.get('summary', '')
    abstract = data.get('abstract', '')
    date_field = data.get('date', '')
    date_end = data.get('date_end', '')
    all_day = data.get('all_day', False)
    publishDate = data.get('publishDate') or iso_midnight_of(datetime.utcnow())
    authors = data.get('authors', [])
    tags = data.get('tags', [])
    featured = data.get('featured', False)

    image = data.get('image', {})
    # image may be dict or empty; provide defaults that match the current repo file when missing
    if not image:
        image = {
            'caption': 'Image credit: [**Unsplash**](https://unsplash.com/photos/bzdhc5b3Bxs)',
            'focal_point': 'Right'
        }

    # urls
    url_code = data.get('url_code', '')
    url_pdf = data.get('url_pdf', '')
    url_slides = data.get('url_slides', '')
    url_video = data.get('url_video', '')

    slides = data.get('slides', '')
    projects = data.get('projects', '')

    # Build front matter following the repository's existing style
    lines = []
    lines.append('---')
    lines.append(f'title: "{title}"')
    lines.append('')
    lines.append(f'event: {event!r}' if event else 'event: ""')
    # event_url: emit empty YAML value (no quotes) when empty to match repo style
    if event_url:
        lines.append(f'event_url: {event_url!r}')
    else:
        lines.append('event_url:')
    lines.append('')
    lines.append(f'location: {location}')
    lines.append('address:')
    # For empty address subkeys, emit empty YAML values (no quotes)
    def emit_addr(key, val):
        if val is None or val == '':
            return f'  {key}:'
        # keep country quoted in existing files
        if key == 'country':
            return f"  {key}: {val!r}"
        return f'  {key}: {val!r}'

    lines.append(emit_addr('street', address.get('street', '')))
    lines.append(emit_addr('city', address.get('city', '')))
    lines.append(emit_addr('region', address.get('region', '')))
    lines.append(emit_addr('postcode', address.get('postcode', '')))
    lines.append(emit_addr('country', address.get('country', 'Singapore')))
    lines.append('')
    lines.append('summary: ' + (summary if summary else ''))
    # abstract as quoted multiline block
    if abstract:
        # keep as double-quoted string with newlines escaped to match existing file style
        # but better to use triple-quote style? repo uses quoted long string; we will use double quotes and let YAML handle it
        # For simplicity, wrap in double quotes and preserve newlines as literal newlines inside the quotes
        # Escape any existing double quotes
        abstract_escaped = abstract.replace('"', '\\"')
        lines.append('abstract: "' + abstract_escaped + '"')
    else:
        lines.append('abstract: ') 
    lines.append(f'date: "{date_field}"')
    lines.append(f'date_end: "{date_end}"' if date_end else 'date_end: ') 
    lines.append(f'all_day: {str(all_day).lower()}')
    lines.append('')
    lines.append(f'publishDate: "{publishDate}"')
    lines.append('')
    # authors as bracketed list
    if authors:
        if isinstance(authors, list):
            authors_str = '[' + ', '.join(authors) + ']'
        else:
            authors_str = f'[{authors}]'
    else:
        authors_str = '[]'
    lines.append(f'authors: {authors_str}')
    # tags
    if tags:
        tags_str = '[' + ', '.join(tags) + ']'
    else:
        tags_str = '[Weekly Talk]'
    lines.append(f'tags: {tags_str}')
    lines.append('')
    lines.append('# Is this a featured talk? (true/false)')
    lines.append(f'featured: {str(featured).lower()}')
    lines.append('')
    lines.append('image:')
    if isinstance(image, dict):
        cap = image.get('caption', '')
        fp = image.get('focal_point', '')
        lines.append(f'  caption: {cap!r}')
        lines.append(f'  focal_point: {fp}')
    else:
        lines.append('  caption: ') 
        lines.append('  focal_point: ') 
    lines.append('')
    lines.append(f'url_code: "{url_code}"')
    lines.append(f'url_pdf: "{url_pdf}"')
    lines.append(f'url_slides: "{url_slides}"')
    lines.append(f'url_video: "{url_video}"')
    lines.append('')
    lines.append('# Markdown Slides (optional).')
    lines.append('slides:')
    lines.append('')
    lines.append('# Projects (optional).')
    lines.append('projects:')
    lines.append('')
    lines.append('# Slides can be added in a few ways:')
    lines.append('# ') 
    lines.append('# - **Create** slides using Wowchemy\'s [*Slides*](https://wowchemy.com/docs/managing-content/#create-slides) feature and link using `slides` parameter in the front matter of the talk file')
    lines.append('# - **Upload** an existing slide deck to `static/` and link using `url_slides` parameter in the front matter of the talk file')
    lines.append('# - **Embed** your slides (e.g. Google Slides) or presentation video on this page using shortcodes (https://wowchemy.com/docs/writing-markdown-latex/).')
    lines.append('# ') 
    lines.append('# Further event details, including page elements such as image galleries, can be added to the body of this page.')
    lines.append('')
    lines.append('---')
    lines.append('Speaker Info:')
    lines.append('')
    speaker_info = data.get('speaker_info') or data.get('body') or ''
    if speaker_info:
        lines.append(speaker_info)
    lines.append('')

    return '\n'.join(lines)


def main(argv):
    if len(argv) < 3:
        print('Usage: generate_event_md_precise.py input.json output_dir/ [--force]')
        sys.exit(2)
    in_path = Path(argv[1])
    out_dir = Path(argv[2])
    out_dir.mkdir(parents=True, exist_ok=True)
    force = '--force' in argv

    data = json.loads(in_path.read_text(encoding='utf-8'))
    fname = parse_date_for_filename(data.get('date')) + '.md'
    out_path = out_dir / fname

    content = build_markdown(data)

    if out_path.exists():
        existing = out_path.read_text(encoding='utf-8')
        if existing == content:
            print(f'Unchanged: {out_path}')
            return
        if not force:
            print(f'Skipped (exists and differs): {out_path} — use --force to overwrite')
            return

    out_path.write_text(content, encoding='utf-8')
    print(f'Wrote {out_path}')


if __name__ == '__main__':
    main(sys.argv)
