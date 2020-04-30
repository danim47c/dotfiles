
from libqtile import widget

def top_widgets(colors: dict): 
  
  base = dict(
    background=colors['lighter'],
    foreground=colors['darker']
  )

  separator = widget.sep.Sep(
    height_percent=80,
    **base,
    linewidth=0,
    padding=3, 
  )

  widgets = []

  # TaskList
  widgets.extend([
    widget.tasklist.TaskList(
      **base,
      fontsize=12,
      icon_size=15,
      padding=6,
      borderwidth=0,
      margin_x=5,
      margin_y=2,
      highlight_method='block',
      border=colors['light'],
      font='Ubuntu Bold',
      markup_focused='<span color="' + str(colors['primary']) + '">{}</span>',
      markup_floating='<span color="' + str(colors['light']) + '">{}</span>',
      markup_minimized='<span underline="low" color="' + str(colors['light']) + '">{}</span>',
      max_title_width=300,
    )
  ])

  # SysTray
  widgets.extend([
    widget.systray.Systray(
      **base
    )
  ])

  widgets.append(separator)

  # Clock
  widgets.extend([
    widget.clock.Clock(
      **base,
      format='%d / %m / %Y - %H:%M'
    )
  ])

  """
  # CurrentLayout
  widgets.extend([
    widget.currentlayout.CurrentLayout(
      **base
    )
  ])

  widgets.append(separator)
  """

  return widgets
  