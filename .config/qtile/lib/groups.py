
from libqtile.config import Key, Group
from libqtile.lazy import lazy

from .keys import win # pylint: disable=relative-beyond-top-level

groups = [
  Group(
    '&'
  ),
  Group(
    'BROWSE',
    spawn='google-chrome-stable'
  ),
  Group(
    'DEV',
    spawn='code -n'
  ),
  Group(
    'TERM',
    spawn='alacritty'
  ),
  Group(
    'FS',
    spawn='thunar'
  ),
  Group(
    'DISCORD',
    spawn='discord'
  ),
  Group(
    'OBS',
    spawn='obs'
  ),
  Group(
    'SOUND',
    spawn='pavucontrol'
  )
]

def extend_keys(keys: list):
  for i in range(len(groups)):
    keys.extend([
      Key([win], str(i + 1), lazy.group[groups[i].name].toscreen()),

      Key([win, "shift"], str(i + 1), lazy.window.togroup(groups[i].name, switch_group=True))
    ])