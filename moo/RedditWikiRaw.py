'''
Created on Oct 10, 2015

@author: ThetNaing
'''
import json
import urllib2
import httplib
import re
import sys
import Properties

RAW_DATA = None

UNICODE_MAPPING = {
                   0x96 : '-',
                   0x93 : '"',
                   0x94 : '"' 
                   }

def getRawLinkData():
    myfile = open('linkData.txt')
    data = myfile.read()
    return json.loads(data, 'ASCII');

def getRawCharData():
    global RAW_DATA
    if RAW_DATA is None:
        RAW_DATA = getRawData()
    return parseData(RAW_DATA)    

def getRawData():
    print "Reading from file"
    myfile = open('data.txt')
    data = myfile.read()
    
    if len(data) == 0:
        print "Connecting to reddit"
        conn = httplib.HTTPSConnection("www.reddit.com")
        conn.request("GET", "/r/DBZDokkanBattle/wiki/characters")
        res = conn.getresponse()
        print "Got response"
        data = res.read().decode('utf-8').replace(u'\u2013', '-').replace(u'\u201C', '"').replace(u'\u201D', '"').replace('King Vegeta', 'Proud Royalty - King Vegeta').replace('Trunks(Teen) From Hell and Back', 'Trunks(Teen) - From Hell and Back')
    return data

def parseData(data):
    charId = 0
    chars = []
    for line in data.split('\n'):
        if line.startswith("[]"):
            c = parseCharData(line, charId)
            if c['rarity'] in set(Properties.RARITY_FILTER) and c['type'] in set(Properties.TYPE_FILTER):
                chars.append(c)
            else:
                print 'Rejected', c['name'],'-', c['title']
            charId = charId + 1
    return chars     
'''
{
    "id":1,
    "name":"Super Saiyan 2 Gohan (Teen)",
    "title":"Saiyan Spirit",
    "passive":"ATK +30% when turn begins",
    "super":"Father-Son Kamehameha - Causes catastrophic damage to opponent",
    "leader":"AGL, TEQ, STR Type HP \u0026 ATK increased by 20%",
    "gameid":"1001700",
    "type":"STR",
    "rarity":"SSR",
    "links":["Golden Warrior","Kamehameha","Saiyan Warrior Race","Super Saiyan"]
}
'''

def parseCharData(raw, charId):
    data = raw.split('|')
    
    numCols = len(data)
    nameAndTitle = data[1].strip()
    m = re.search('\[(.*?)[ ]*-[ ]*(.*?)\].*', nameAndTitle)
    name = m.group(1)
    title = m.group(2)
    rarity = data[2].strip()
    chartype = re.search('\[(.*)\].*', data[3].strip()).group(1)
    
    leader = data[7].strip() if numCols == 10 else ''
        
    passive = data[8 if numCols == 10 else 7].strip()
    links = parseLinks(data[9 if numCols == 10 else 8])
    return {"id" : charId, "name" : name, "title" : title, "passive" : passive, "super" : '', "leader" : leader, "gameid" : charId, "type" : chartype, "rarity" : rarity, "links": links}
    
''' [The Hera Clan](/r/DBZDokkanBattle/wiki/characters_jp "Ki+2"), [Galactic Warrior](/r/DBZDokkanBattle/wiki/characters_jp "+20% ATK"), [Tough as Nails](/r/DBZDokkanBattle/wiki/characters "+1500 DEF"), [Loyalty](/r/DBZDokkanBattle/wiki/characters "Ki+1")'''   
def parseLinks(data):
    links = []
    for line in data.split(','):
        l = line.strip()
        m = re.search('\[(.*)\].*', l)
        try:
            link = m.group(1)
            links.append(link)
        except Exception as e:
            #can't find link, probably link description part, ignore and continue
            continue
    return links
    
    
    
     
if __name__ == "__main__":
    print getRawCharData()
    