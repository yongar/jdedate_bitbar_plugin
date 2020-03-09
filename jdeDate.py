#!/usr/bin/env python


# <bitbar.title>JDE Today</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Yonghoon Choi</bitbar.author>
# <bitbar.author.github>yongar</bitbar.author.github>
# <bitbar.desc>The plugin shows the JDE date today </bitbar.desc>
# <bitbar.image></bitbar.image>
# <bitbar.dependencies>bash</bitbar.dependencies>
# <bitbar.abouturl></bitbar.abouturl>
from datetime import datetime

def getDaysofYear(dt):
	return dt.strftime("%j")


def getJDEYear(dt):
	return "1"+dt.strftime("%y")

def getJDEDate(dt):
	return getJDEYear(dt)+getDaysofYear(dt)

print(getJDEDate(datetime.now()))

