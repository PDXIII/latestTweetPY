#!usr/bin/env python2.7
#-*- coding: iso-8859-1 -*-

# coded on an example I found here: http://stackoverflow.com/a/14177040/1728652

import sys
import os
import json
from pprint import pprint
from twython import Twython


def readConfig(pathToConfigFile):
  with open(pathToConfigFile, 'r') as configFile:
    return configFile.read()


config = readConfig('.config.json')

print config