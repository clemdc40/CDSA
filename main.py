from typing import Any
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent / 'scripts'))
from sync import Sync

def define_env(env: Any) -> None:
    """Expose extra variables like {{ target_ip }} to templates and build navigation."""
    env.variables.update(env.conf.get('extra', {}))
    sync = Sync()
    nav, cards = sync.build()
    sync.write_nav(nav)
    sync.write_cards(cards)
