#!usr/bin/env python2.7
#-*- coding: iso-8859-1 -*-

# the first editon was very mauch based on this example: http://stackoverflow.com/a/14177040/1728652
# after some refactoring it is now very clean, commented and beautiful!

import sys
import json
from twython import Twython


def readConfig(pathToConfigFile):
  with open(pathToConfigFile, 'r') as configFile:
    return json.load(configFile)

def saveTweetData(pathToSaveFile, data):
  with open(pathToSaveFile, 'w') as saveFile:
    saveFile.write(json.dumps(data))

def main():
  # read the config
  config = readConfig('.config.json')
  # creating the search query using the our parameters
  searchQuery = 'from:%s %s' % (config['user screen name'],
                                config['hash tag'])

  # preparing authentification the Twython way
  t = Twython(app_key=config['consumer key'],
              app_secret=config['consumer secret'],
              oauth_token=config['access token'],
              oauth_token_secret=config['access token secret'])
  
  # starting the search with Twython
  search = t.search(q=searchQuery, count=config['tweet count'])
  # get the result
  tweets = search['statuses']
  # save the data according to the config
  saveTweetData(config['target path'], tweets)

if __name__ == '__main__':
  main()
