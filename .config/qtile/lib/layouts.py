
from libqtile import layout

def layouts_func(colors: dict):
  return [
      layout.Max(),
      layout.MonadTall(
        border_focus=colors['primary'],
        border_width=1,
        margin=16
      )
  ]