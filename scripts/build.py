#!/usr/bin/env python3

from pathlib import Path

SRC_DIR = Path(__file__).parent.parent / 'src'
DIST_DIR = Path(__file__).parent.parent / 'dist'

HTML_TEMPLATE = SRC_DIR / 'template.html'
CSS_FILE = SRC_DIR / 'style.css'
JS_FILE = SRC_DIR / 'pixxely.js'
OUTPUT_FILE = DIST_DIR / 'pixxely.html'

def build():
    html = HTML_TEMPLATE.read_text(encoding='utf-8')
    css = CSS_FILE.read_text(encoding='utf-8')
    js = JS_FILE.read_text(encoding='utf-8')
    html = html.replace('<!-- INLINE_CSS -->', css)
    html = html.replace('<!-- INLINE_JS -->', js)
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(html, encoding='utf-8')
    print(f'Build complete: {OUTPUT_FILE.resolve()}')

if __name__ == '__main__':
    build()
