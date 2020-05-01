
from libqtile import widget

def bottom_widgets(colors: dict):
  base = dict(
    background=colors['dark'],
    foreground=colors['primary']
  )

  separator = widget.sep.Sep(
    height_percent=100,
    background=colors['dark'],
    foreground=colors['dark'],
    linewidth=1,
    padding=3, 
  )

  widgets = []

  # GroupBox
  widgets.extend([
    widget.groupbox.GroupBox(
      **base,
      font='Ubuntu Bold',
      fontsize=12,
      margin_y=5,
      margin_x=0,
      padding_y=12,
      padding_x=20,
      borderwidth=1,
      active=colors['primary'],
      inactive=colors['secondary'],
      rounded=False,
      highlight_method='block',
      this_current_screen_border=colors['light'],
      this_screen_border=colors['light'],
      other_current_screen_border=colors['dark'],
      other_screen_border=colors['dark']
    )
  ])

  # Prompt
  widgets.extend([
    widget.prompt.Prompt(
      **base,
      prompt= "user@arch:~$ ",
      font= "Source Code Pro"
    )
  ])
  
  # Spacer
  widgets.extend([
    widget.spacer.Spacer(
      **base
    )
  ])
  
  # Clipboard
  widgets.extend([
    widget.clipboard.Clipboard(
      **base,
      timeout=30,
      max_width=64
    )
  ])
  
  widgets.append(separator)

  # CPU
  widgets.extend([
    widget.cpu.CPU(
      **base,
      format='CPU {load_percent}% - {freq_current}GHz',
      font='Ubuntu Bold'
    )
  ])
  
  # Memory
  widgets.extend([
    widget.memory.Memory(
      **base,
      format='RAM {MemUsed}/{MemTotal}MB',
      font='Ubuntu Bold'
    )
  ])

  return widgets
  

