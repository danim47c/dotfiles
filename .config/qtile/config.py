try:
  from os import path
  from json import load as json_load


  qtile_path = path.join(path.expanduser("~"), ".config", "qtile")

  # Colors
  with open(
    path.join(qtile_path, 'colors.json'),
    'r'
  ) as f: colors = json_load(f)


  from lib.keys import keys

  from lib.groups import groups, extend_keys
  extend_keys(keys)

  from lib.layouts import layouts_func
  layouts = layouts_func(colors)

  from lib.screen import screens_func, widget_defaults, extension_defaults
  screens = screens_func(colors)

  from lib.mouse import mouse

  from lib.vars import * # pylint: disable=unused-wildcard-import
  floating_layout = floating_layout_func(colors)

except Exception as e:
	import traceback
	import os
	os.system('echo "' + str(traceback.format_exc()) + '" > /home/user/logs.log')
	raise TypeError

#raise TypeError