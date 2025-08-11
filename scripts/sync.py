#!/usr/bin/env python3
import json
import subprocess
from pathlib import Path

import yaml
from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options

class Plugin(BasePlugin):
    config_scheme = (
        ('cheatsheets_dir', config_options.Type(str, default='cheatsheets')),
    )

    def on_pre_build(self, config):
        sync = Sync(Path(self.config['cheatsheets_dir']))
        nav, cards = sync.build()
        config['nav'] = nav
        sync.write_nav(nav)
        sync.write_cards(cards)
        return config

class Sync:
    def __init__(self, cheatsheets_dir=Path('cheatsheets')):
        self.cheatsheets_dir = Path(cheatsheets_dir)
        self.mkdocs_file = Path('mkdocs.yml')
        self.cards_file = Path('overrides/assets/cards.json')

    def build(self):
        nav = []
        cards = []
        for section in sorted([p for p in self.cheatsheets_dir.iterdir() if p.is_dir()]):
            items = []
            for md in sorted(section.glob('*.md')):
                if md.name == 'index.md':
                    continue
                meta = self.read_meta(md)
                title = meta.get('title', md.stem.replace('_', ' ').title())
                rel_path = md.relative_to(self.cheatsheets_dir).as_posix()
                items.append({title: rel_path})
                last = self.git_date(md)
                cards.append({
                    'title': title,
                    'path': rel_path.replace('.md', '/'),
                    'tags': meta.get('tags', []),
                    'os': meta.get('os', []),
                    'difficulty': meta.get('difficulty', ''),
                    'last_updated': last
                })
            if items:
                nav.append({section.name.replace('_', ' '): items})
        return nav, cards

    def read_meta(self, path: Path):
        text = path.read_text(encoding='utf-8')
        if text.startswith('---'):
            try:
                _, fm, _ = text.split('---', 2)
                return yaml.safe_load(fm) or {}
            except ValueError:
                return {}
        return {}

    def git_date(self, path: Path) -> str:
        try:
            result = subprocess.run(
                ['git', 'log', '-1', '--format=%cs', str(path)],
                capture_output=True, text=True, check=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError:
            return ''

    def write_nav(self, nav):
        config = yaml.safe_load(self.mkdocs_file.read_text(encoding='utf-8'))
        config['nav'] = nav
        self.mkdocs_file.write_text(yaml.safe_dump(config, sort_keys=False), encoding='utf-8')

    def write_cards(self, cards):
        self.cards_file.parent.mkdir(parents=True, exist_ok=True)
        self.cards_file.write_text(json.dumps(cards, indent=2), encoding='utf-8')

if __name__ == '__main__':
    sync = Sync()
    nav, cards = sync.build()
    sync.write_nav(nav)
    sync.write_cards(cards)
