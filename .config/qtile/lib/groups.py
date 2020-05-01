
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
    spawn='code'
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
    'SOUND',
    spawn='pavucontrol'
  ),
  Group(
    'MISC',
    spawn='discord',
    layout='monadtall'
  )
]

assignable_keys = ['space', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def extend_keys(keys: list):
  for i in range(len(groups)):
    key = str(i + 1)
    key = assignable_keys[i]

    keys.extend([
      Key([win], key, lazy.group[groups[i].name].toscreen()),

      Key([win, "shift"], key, lazy.window.togroup(groups[i].name, switch_group=True))
    ])