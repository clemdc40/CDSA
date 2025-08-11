# HTB Cheatsheets

Projet de cheatsheets Hack The Box construit avec MkDocs Material.

## Installation

```bash
pip install -r requirements.txt
mkdocs serve
```

La navigation et les cartes sont construites automatiquement à chaque build. Pour les régénérer manuellement :

```bash
python scripts/sync.py
```

## Front matter

Chaque fiche commence par un bloc YAML :

```yaml
---
title: Kerberoasting
tags: [AD, hash, spn]
os: [Windows]
difficulty: Intermediate
---
```

- **tags** : mots-clés (AD, Web, privesc…)
- **os** : systèmes concernés
- **difficulty** : Beginner, Intermediate, Advanced

## Déploiement

Le site est publié automatiquement sur GitHub Pages via `gh-pages` :

```bash
git push origin main
```
