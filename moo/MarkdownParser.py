'''
Created on Oct 11, 2015

@author: ThetNaing
'''
import mistune
from lxml import etree
from BeautifulSoup import BeautifulSoup, Comment


MARKDOWN = '''Icon|Name|Rarity|Type|Max HP|Max Atk|Max Def|Leader Skill|Passive Skill|Link Skill
-|-|:-:|:-:|:-:|:-:|:-:|:--|:--|-
[](#wc-bido) | [Bido - Vicious Power Fighter](http://i.imgur.com/XKru7hd.jpg) | R | [PHY](/phy) | hp | atk | def | HP +15% | STR & PHY type ATK +10% | [The Hera Clan](/r/DBZDokkanBattle/wiki/characters_jp "Ki+2"), [Galactic Warrior](/r/DBZDokkanBattle/wiki/characters_jp "+20% ATK"), [Tough as Nails](/r/DBZDokkanBattle/wiki/characters "+1500 DEF"), [Loyalty](/r/DBZDokkanBattle/wiki/characters "Ki+1")
[](#wc-bojack) | [Bojack - Galaxy's Most Evil](http://imgur.com/mbqP6NU) | SR | [STR](/str) | 6123 | 6172 | 3289 | +40% ATK to STR | +50% ATK when super attack is launched| [The Hera Clan](/r/DBZDokkanBattle/wiki/characters_jp "Ki+2"), [Galactic Warriors](/r/DBZDokkanBattle/wiki/characters "ATK +20%"), [Big Bad Bosses](/r/DBZDokkanBattle/wiki/characters "ATK +25% when HP is 10% or below"), [Thirst for Conquest](/r/DBZDokkanBattle/wiki/characters "ATK +15%"), [Revival](/r/DBZDokkanBattle/wiki/characters_jp "Ki+2")
[](#wc-bujin) | [Bujin - Merciless Supernatural Power](http://imgur.com/G1DJp2V) | R | [INT](/int) | 6249 |3186 | 2641 | TEQ opponent's ATK -10% | Ki+1 to INT & STR| [The Hera Clan](/r/DBZDokkanBattle/wiki/characters_jp "Ki+2"), [Galactic Warrior](/r/DBZDokkanBattle/wiki/characters_jp "+20% ATK"), [Telekinesis](/r/DBZDokkanBattle/wiki/characters_jp "Opponent DEF down 10%"), [Loyalty](/r/DBZDokkanBattle/wiki/characters_jp "Ki+1")
[](#wc-kogu) | [Kogu - Dastardly Swordsman](http://i.imgur.com/sSR4aho.jpg) | R | [TEQ](/teq) | hp | atk | def | Damage received reduced by 10% | TEQ and STR Ki +1 | [The Hera Clan](/r/DBZDokkanBattle/wiki/characters_jp "Ki+2"), [Galactic Warriors](/r/DBZDokkanBattle/wiki/characters_jp "ATK +20%"), [Infighter](/r/DBZDokkanBattle/wiki/characters_jp "Opponent DEF -5%"), [Thirst for conquest](/r/DBZDokkanBattle/wiki/characters_jp "ATK +15%"), [Loyalty](/r/DBZDokkanBattle/wiki/characters_jp "Ki +1")
[](#wc-bojack1) | [Maximum Power Bojack - Full Power](http://imgur.com/LR02Jbc) | SSR | [STR](/str) | 7250 | 7813 | 3956 | ATK+50% to STR | +75% ATK when Super Attack is launched| [The Hera Clan](/r/DBZDokkanBattle/wiki/characters_jp "Ki+2"), [Galactic Warrior](/r/DBZDokkanBattle/wiki/characters_jp "+20% ATK"), [Big Bad Bosses](/r/DBZDokkanBattle/wiki/characters_jp "+25% ATK when HP is 10% or below"), [Thirst for conquest](/r/DBZDokkanBattle/wiki/characters_jp "+15% ATK"), [Coward](/r/DBZDokkanBattle/wiki/characters_jp "Ki+1")
[](#wc-gohan7) | [Super Saiyan Gohan (Teen) - Resolute Valor](http://i.imgur.com/hVFzvW0.jpg) | SR | [PHY](/phy) | 6024 | 5883 | 3174 | +25% ATK to AGL & PHY | +30% ATK when turn begins| [Golden Warrior](/r/DBZDokkanBattle/wiki/characters_jp "Ki +1, Opponent DEF -2000"), [Saiyan Warrior Race](/r/DBZDokkanBattle/wiki/characters_jp "+700 ATK"),  [Super Saiyan](/r/DBZDokkanBattle/wiki/characters_jp "+10% ATK"), [All in the Family](/r/DBZDokkanBattle/wiki/characters_jp "+2000 DEF"), [Z-Fighters](/r/DBZDokkanBattle/wiki/characters_jp "+500 ATK")
[](#wc-gohan9) | [Super Saiyan 2 Gohan (Teen) - Entrusted Mission](http://imgur.com/f13p23k) | SSR | [AGL](/agl) | 7502 | 7191 | 3889 | +30% HP and ATK to AGL and STR | Ki+2 for AGL and STR | [Super Saiyan](/r/DBZDokkanBattle/wiki/characters_jp "+10% ATK"), [Saiyan Warrior Race](/r/DBZDokkanBattle/wiki/characters_jp "+700 ATK"), [Kamehameha](/r/DBZDokkanBattle/wiki/characters_jp "+2500 ATK when Super Attack is launched"), [Golden Warrior](/r/DBZDokkanBattle/wiki/characters_jp "Ki +1, Opponent DEF -2000")
[](#wc-zangya) | [Zangya - Brutal Battlefield Diva](http://imgur.com/1Dola8S) | SR | [AGL](/agl) | 6833 | 5433 | 3666 | Ki +2 when HP is 50% or more | +5% HP recovery when turn begins | [The Hera Clan](/r/DBZDokkanBattle/wiki/characters_jp "Ki+2"), [Galactic Warrior](/r/DBZDokkanBattle/wiki/characters_jp "+20% ATK"), [Battlefield Diva](/r/DBZDokkanBattle/wiki/characters_jp "Ki+2"), [Loyalty](/r/DBZDokkanBattle/wiki/characters_jp "Ki+1"), [Atrocities](/r/DBZDOkkanBattle/wiki/characters_jp "+500 ATK") '''
     
if __name__ == "__main__":
    markdown = mistune.Markdown()
    htmlStr = markdown(MARKDOWN)
    print htmlStr
    bs = BeautifulSoup(htmlStr)

        
    results = {}
    for row in bs.findAll('tr th'):        
        print row
    
    print results