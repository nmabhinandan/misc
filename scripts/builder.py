#!/usr/bin/env python3

import urllib.request, json, os, subprocess
from pathlib import Path

dir_path = os.path.dirname(os.path.realpath(__file__))

file = Path( dir_path + '/data.json')
data = {}
if file.is_file():
	with open(str(file)) as f:
	    data = json.load(f)

def build_active_window_control():
	res = urllib.request.urlopen('https://api.github.com/repos/kotelnik/plasma-applet-active-window-control/tags').read()
	tags = json.loads(res.decode('utf-8'))
	latest = tags[0]['name'][1:]
	if data.get('awc_version') and latest <= data['awc_version']:
		pass
	else:
		data['awc_version'] = latest
		os.chdir('/tmp')
		subprocess.call(['git', 'clone', 'https://github.com/kotelnik/plasma-applet-active-window-control.git'])


build_active_window_control()

with open(str(file), 'w') as f:
	json.dump(data, f)


