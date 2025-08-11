import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent / 'scripts'))
from sync import Sync

def define_env(env):
    sync = Sync()
    nav, cards = sync.build()
    sync.write_nav(nav)
    sync.write_cards(cards)
