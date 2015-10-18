'''
Created on Oct 10, 2015

@author: ThetNaing
'''
import itertools
import networkx as nx
from moo import DbzDokkRaw, RedditWikiRaw
import Properties
import operator

'''
[  
   {  
      "id":1,
      "name":"All in the Family",
      "description":"+2000 DEF"
   }
]
'''
class Link:
    
    def __init__(self, data):
        try:
            self.id = data['id']
            self.name = data['name'].encode('ascii', 'ignore')
            self.description = data['description'].encode('ascii', 'ignore')
        except Exception:
            print data 
    
    def __hash__(self):
        return self.id

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name and self.description == other.description
    
    def __str__(self):
        return '' + self.id + ':' + self.name + ':' + self.description
'''
[  
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
      "links":[  
         "Golden Warrior",
         "Kamehameha",
         "Saiyan Warrior Race",
         "Super Saiyan"
      ]
   }
]
'''
class Character:
    
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name'].encode('ascii', 'ignore').strip()
        self.title = data['title'].encode('ascii', 'ignore').strip()
        self.passive = data['passive'].encode('ascii', 'ignore').strip()
        self.super = data['super'].encode('ascii', 'ignore').strip()
        self.leader = data['leader'].encode('ascii', 'ignore').strip()
        self.gameid = data['gameid']
        self.type = data['type'].encode('ascii', 'ignore').strip()
        self.rarity = data['rarity'].encode('ascii', 'ignore').strip()
        self.links = self.convertUnicodeListToStringList(data['links'])
        self.isLinkValid()

    def isLinkValid(self):
        global LINK_DATA 
        allLinks = set([l.name for l in LINK_DATA])
        for link in self.links:
            if link not in allLinks:
                print "Invalid Link:", link
                
        
    def convertUnicodeListToStringList(self, data):
        result = ()
        for i in data:
            result += (i.encode('ascii', 'ignore'), )
        return result
        
    def __hash__(self):
        return self.id

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name and self.title == other.title and self.passive == other.passive and self.super == other.super and self.leader == other.leader and self.gameid == other.gameid and self.type == other.type and self.rarity == other.rarity and self.links == other.links

    def __str__(self):
        return '"' + self.name + ':' + self.title + '"'

    


MINE = open('myCharList.txt').read()


TEST = '''Chilled - Dastardly Space Pirate
Full Power Bojack - Full Strength Tremor'''



def getLinkData(raw):
    result = ()
    for l in raw:
        c = Link(l)
        result += (c,)
    return result

def getCharData(raw):
    result = ()
    for l in raw:
        c = Character(l)
        result += (c,)
    return result

def getMyCharData(raw, charsData):
    myCharsParsed = []

    for line in raw.split('\n'):
        ls = line.split('-')
        name = ls[0].strip()
        title = ls[1].strip()
        myCharsParsed.append({'name':name,'title':title})
    
    
    myChars = {}
    
    for myCharParsed in myCharsParsed:
        found = False
        for charData in charsData:
            if myCharParsed['name'] == charData.name and myCharParsed['title'] == charData.title:
                found = True
                for currLinkSkills in charData.links:
                    chars = ()
                    if myChars.has_key(currLinkSkills):                    
                        chars = myChars[currLinkSkills]
                    chars += (charData, )
                    myChars[currLinkSkills] = chars
        if not found:
            print "Not Found - " + myCharParsed['name'] + " - " + myCharParsed['title']
    return myChars

def main():    
    LINK_DATA_RAW = RedditWikiRaw.getRawLinkData()
    CHAR_DATA_RAW = RedditWikiRaw.getRawCharData()
    
    global LINK_DATA
    LINK_DATA = getLinkData(LINK_DATA_RAW)
    global CHAR_DATA
    CHAR_DATA = getCharData(CHAR_DATA_RAW)  
    
    # Get string in this format for easy analysis
    # Android #17|Dauntless Runner
    # Android #17 (Future)|A Future Forsaken
    # Android #18|Alluring Assassin
    
    MY_CHAR_RAW = MINE
    if Properties.CHAR_FILTER == 'ALL':
        MY_CHAR_RAW = '\n'.join([ ch['name'].strip() + ' - ' + ch['title'].strip() for ch in CHAR_DATA_RAW ])
    
    # Get Link skill to characters mapping
    MY_CHAR_DATA = getMyCharData(MY_CHAR_RAW, CHAR_DATA)

    G = nx.MultiGraph()
    for linkName in MY_CHAR_DATA.keys():
        if(filterLink(linkName, LINK_DATA)):
            G.add_edges_from(itertools.combinations(MY_CHAR_DATA[linkName],2), link=getLinkObj(linkName, LINK_DATA))
        
    # G.edges() returns two edges for each connection for undirected graph.
    edges = ()
    
    H = nx.Graph()
    #print "graph G {"
    for charA, charB in G.edges():
        linksBetweenTwoChars = G[charA][charB]
        
        hashedCharIds = hashInts(charA.id, charB.id)
        
        
        
        
        #No linking between two character with same name but different title
        if len(linksBetweenTwoChars) >= Properties.MIN_LINK_COUNT and hashedCharIds not in edges and charA.name != charB.name: # 
            edgeTooltip =  ",".join([j['link'].description for j in linksBetweenTwoChars.values()])
            src = charA.name + ' - ' + charA.title
            dest = charB.name + ' - ' + charB.title
            #if len(linksBetweenTwoChars) > 1:
                #print '"' + src + '" -- "' + dest + '" [label="' + str(len(linksBetweenTwoChars)) + '"];'
            edges += (hashedCharIds,)
            H.add_weighted_edges_from([(src,dest, len(linksBetweenTwoChars))], tooltip = edgeTooltip)
    #print "}"
    
    #rank(G)
    
    clustering =  nx.clustering(H)
    print len(clustering), len(G.nodes()), len(H.nodes())
    sorted_x = sorted(clustering.items(), key=operator.itemgetter(1), reverse=True)
    
    
    isPrinted = ()
    
    print "graph G {"
    for x in sorted_x:#[0:int(len(sorted_x)*0.2)]:
        links = H[x[0]]
        if len(links) >= 1: # at least 1 other characters linked to this one
#             print len(links), "-------", x[1], "|", x[0], "----------------"
            for charA, charB in itertools.combinations([x[0]] + H[x[0]].keys(), 2):
                
                hashInt = hashInts(hash(charA), hash(charB))
                if hashInt not in isPrinted:
                    isPrinted += (hashInt,)
                    try:                        
                        print '"' + charA + '" -- "' + charB + '" [label="' + str(H[charA][charB]['weight']) + '", tooltip="' + H[charA][charB]['tooltip'] + '"];'                        
                    except Exception:
                        continue                    
    print "}" 
                 
    
    '''
    M, clusters = networkx_mcl(G, expand_factor=3)
    print clusters
    for i in M.edges():
        links = M[i[0]][i[1]]
        src = i[0].name + ':' + i[0].title
        dest = i[1].name + ':' + i[1].title
        print '"' + src + '" -- "' + dest + '" [label="' + str(len(links)) + '"];'
    '''
    
    
    
    
'''    
    pos = nx.spring_layout(H)
    nx.draw(H, pos)
    node_labels = nx.get_node_attributes(H,'state')
    nx.draw_networkx_labels(H, pos, labels = node_labels)
    edge_labels = nx.get_edge_attributes(H,'state')
    nx.draw_networkx_edge_labels(H, pos, labels = edge_labels)
    plt.savefig('C:\\Z\\this.png')
#    plt.show()
#     nx.write_dot(H, 'C:\\Z\\this.dot')
'''
          
def rank(G):
    REMEMBER = {}
    for node in G.nodes():
        currentNameSet = ()
        currentNameTitleSet = ()
        findLinkScore(G, node, 0, currentNameSet, currentNameTitleSet, REMEMBER)
    for value in REMEMBER.values():
        print value[1], value[0]
        
        
    
def findLinkScore(G, root, score, currentNameSet, currentNameTitleSet, REMEMBER):
    currentNameSet += (root.name, )
    currentNameTitleSet += (root.name + ' - ' + root.title, )
    if len(currentNameSet) == 6:
        currentSetStart = currentNameTitleSet[0]
        
        if currentSetStart in REMEMBER:        
            maxCurrentSetScore = REMEMBER[currentSetStart][0]        
            if score > maxCurrentSetScore:
                REMEMBER[currentSetStart] = (score, currentNameTitleSet)
        else:
            REMEMBER[currentSetStart] = (score, currentNameTitleSet)
            
        return
    for neighbor in G[root]:
        if neighbor.name in currentNameSet:
            continue
        findLinkScore(G, neighbor, score + len(G[root][neighbor]), currentNameSet, currentNameTitleSet, REMEMBER) 
        
def filterLink(linkName, data):
    found = False
    for link in data:
        if link.name.upper() == linkName.upper():
            found = True
            for filterLink in Properties.LINK_FILTER:
                if filterLink in link.description.upper():
                    return True
    if not found:             
        print "Link Not Found", linkName
    return False

def getLinkObj(linkName, data):
    for link in data:
        if link.name.upper() == linkName.upper():
            return link
        
    print "Link Not Found", linkName
    return None
    
#Szudzik's hash     
def hashInts(a, b):
    a1 = a if a > b else b
    b1 = b if a > b else a
    return a1*a1 + a1 + b1 

if __name__ == "__main__":
    main()

