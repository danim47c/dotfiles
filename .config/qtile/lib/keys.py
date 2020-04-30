
from libqtile.config import Key
from libqtile.lazy import lazy

win = 'mod4'

keys = [
  # Switch between windows in current stack pane
  Key([win], "Down", lazy.layout.down()),
  Key([win], "Up", lazy.layout.up()),
  Key([win], "Left", lazy.layout.left()),
  Key([win], "Right", lazy.layout.right()),

  # Move windows up or down in current stack
  Key([win, "control"], "Down", lazy.layout.shuffle_down()),
  Key([win, "control"], "Up", lazy.layout.shuffle_up()),

  # Toggle floating
  Key([win, "shift"], "f", lazy.window.toggle_floating()),

  # Switch window focus to other pane(s) of stack
  Key([win], "space", lazy.layout.next()),

  # Toggle between different layouts as defined below
  Key([win], "Tab", lazy.next_layout()),
  Key([win, 'shift'], "Tab", lazy.previous_layout()),
  Key([win], "w", lazy.window.kill()),

  Key([win, "control"], "r", lazy.restart()),
  Key([win, "control"], "q", lazy.shutdown()),
  Key([win], "r", lazy.spawncmd()),

  # MonadTall
  Key([win, "control"], "Left", lazy.layout.swap_left()),
  Key([win, "control"], "Right", lazy.layout.swap_right()),
  Key([win, "control"], "Down", lazy.layout.shuffle_down()),
  Key([win, "control"], "Up", lazy.layout.shuffle_up()),
  Key([win, 'shift'], "Up", lazy.layout.grow()),
  Key([win, 'shift'], "Down", lazy.layout.shrink()),

  # Volume 
  Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 5%-")),
  Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 5%+")),
  Key([], "XF86AudioMute", lazy.spawn("amixer set Master toogle")),

  # Custom
  Key([win], 'r', lazy.spawncmd()),
  Key([win], 'v', lazy.spawn('pavucontrol')),
  Key([win], 'p', lazy.spawn('rofi -show')),
  Key([win], 'o', lazy.spawn('rofi -show run')),
  Key([win], 'l', lazy.spawn('rofi -show ssh')),
  Key([win], "Return", lazy.spawn("alacritty")),
  Key([win], 'b', lazy.spawn('chrome')),
  Key([win], 'f', lazy.spawn('thunar'))
]
