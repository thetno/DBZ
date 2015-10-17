'''
Created on Oct 10, 2015

@author: ThetNaing
'''
import json
import urllib2

def getRawLinkData():
    return json.load(urllib2.urlopen('http://api.dbzdokk.com/links'));

def getRawCharData():
    return json.load(urllib2.urlopen('http://api.dbzdokk.com/characters'))