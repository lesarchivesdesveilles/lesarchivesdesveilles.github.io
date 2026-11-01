#!/usr/bin/env python3
"""Generate sitemap.xml from the published archive IDs in archives.json."""
import json
from pathlib import Path
from xml.etree.ElementTree import Element, SubElement, indent, tostring

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://lesarchivesdesveilles.fr'

with (ROOT / 'archives.json').open(encoding='utf-8-sig') as handle:
    archives = json.load(handle)

if not isinstance(archives, dict):
    raise ValueError('archives.json doit contenir un objet associant numéros et archives')

ids = sorted((str(key) for key, value in archives.items() if isinstance(value, dict) and str(key).isdigit()), key=int, reverse=True)
if not ids:
    raise ValueError('Aucune archive trouvée : sitemap non modifié')

urlset = Element('urlset', xmlns='http://www.sitemaps.org/schemas/sitemap/0.9')
for url in [f'{BASE}/', *(f'{BASE}/archive.html?archive={num}' for num in ids)]:
    SubElement(SubElement(urlset, 'url'), 'loc').text = url
indent(urlset, space='  ')
(ROOT / 'sitemap.xml').write_bytes(b'<?xml version="1.0" encoding="UTF-8"?>\n' + tostring(urlset, encoding='utf-8') + b'\n')
print(f'Sitemap généré : {len(ids) + 1} URL ({len(ids)} archives)')
