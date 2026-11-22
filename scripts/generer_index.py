#!/usr/bin/env python3
"""Construit l'index public léger à partir des archives complètes."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
archives = json.loads((ROOT / 'archives.json').read_text(encoding='utf-8'))
categories = json.loads((ROOT / 'thematiques.json').read_text(encoding='utf-8'))
valides = {categorie['id'] for categorie in categories}
index = {}
for cle, archive in archives.items():
    theme = archive.get('thematique', '')
    if theme and theme not in valides:
        raise ValueError(f"Archive {cle}: thématique inconnue: {theme!r}")
    index[cle] = {
        'numero': archive.get('numero', int(cle)),
        'titre': archive.get('titre', ''),
        'sousTitre': archive.get('sousTitre', ''),
        'source': archive.get('source', ''),
        'miniature': archive.get('miniature', f'miniatures/{cle}.webp'),
        'thematique': theme,
    }
(ROOT / 'index-archives.json').write_text(json.dumps(index, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f"Index généré : {len(index)} archives, {sum(not a['thematique'] for a in index.values())} sans thématique")
