#!/usr/bin/env python3

import glob
import os
import re

from DistUtilsExtra.command import *
from DistUtilsExtra.auto import setup

# look/set what version we have
changelog = "debian/changelog"
if os.path.exists(changelog):
    head = open(changelog).readline()
    match = re.compile(".*\((.*)\).*").match(head)
    if match:
        version = match.group(1)
#         f = open("MsgidUrl/Version.py", "w")
#         f.write("VERSION=\"%s\"\n" % version)
#         f.close()

#GETTEXT_NAME="apturl"
#I18NFILES = []
#for filepath in glob.glob("po/mo/*/LC_MESSAGES/*.mo"):
#    lang = filepath[len("po/mo/"):]
#    targetpath = os.path.dirname(os.path.join("share/locale",lang))
#    I18NFILES.append((targetpath, [filepath]))

setup(name='message-id-url',
      version=version,
      scripts=['open-msgid'],
      data_files=[('/etc/firefox/pref/',   ["data/midurl.js"]),
                  ('share/kde4/services/', ["data/mid.protocol"]),
                 ],
      )
