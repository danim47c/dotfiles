
from libqtile import layout

from typing import List  # noqa: F401

auto_fullscreen = True

bring_front_click = True

cursor_warp = True

dgroups_app_rules = []  # type: List

dgroups_key_binder = None

follow_mouse_focus = True

focus_on_window_activation = "smart"

main = None

wmname = "LG3D"

def floating_layout_func(colors: dict): 
  return layout.Floating(
    float_rules=[
      {'wmclass': 'confirm'},
      {'wmclass': 'dialog'},
      {'wmclass': 'download'},
      {'wmclass': 'error'},
      {'wmclass': 'file_progress'},
      {'wmclass': 'notification'},
      {'wmclass': 'splash'},
      {'wmclass': 'toolbar'},
      {'wmclass': 'confirmreset'},  # gitk
      {'wmclass': 'makebranch'},  # gitk
      {'wmclass': 'maketag'},  # gitk
      {'wname': 'branchdialog'},  # gitk
      {'wname': 'pinentry'},  # GPG key password entry
      {'wmclass': 'ssh-askpass'},  # ssh-askpass
    ],
    border_focus=colors["secondary"]
  )
