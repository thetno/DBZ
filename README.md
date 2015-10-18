# DBZ
DBZ Dokkan Battle Team Generator/Analyzer

Require NetworkX Library (https://networkx.github.io/)

Filter Character types, rarity and link types in Properties.py

Generated DOT code can be used for plotting on GraphViz (Online version - http://www.webgraphviz.com/)

Credits to http://www.dbzdokk.com/, http://dbz-dokkanbattle.wikia.com/, https://www.reddit.com/r/DBZDokkanBattle/wiki/characters



Script will generate DOT code like below, which can be used with GraphViz

graph G {
"Bujin - Merciless Supernatural Power" -- "Full Power Bojack - Full Strength Tremor" [label="2", tooltip="ATK +20%,Ki +2"];
"Bujin - Merciless Supernatural Power" -- "Zangya - Brutal Battlefield Diva" [label="3", tooltip="ATK +20%,Ki +1,Ki +2"];
"Full Power Bojack - Full Strength Tremor" -- "Zangya - Brutal Battlefield Diva" [label="2", tooltip="ATK +20%,Ki +2"];
"Super Saiyan Gohan (Teen) - Resolute Valor" -- "Super Saiyan 2 Goku - The Fruits of Training" [label="3", tooltip="+700 ATK,+10% ATK,Ki +1 Opponent, DEF -2000"];
"Super Saiyan Gohan (Teen) - Resolute Valor" -- "Super Saiyan Bardock - The First Awakened" [label="2", tooltip="+700 ATK,+10% ATK"];
"Super Saiyan 2 Goku - The Fruits of Training" -- "Super Saiyan Bardock - The First Awakened" [label="3", tooltip="+700 ATK,+10% ATK,+2 Ki"];
"Raditz - Cocky Counter" -- "Mercenary Tao - Professional Tactician" [label="2", tooltip="+500 ATK,+1 Ki"];
"Raditz - Cocky Counter" -- "Chilled - Dastardly Space Pirate" [label="2", tooltip="+500 ATK,+1 Ki"];
"Mercenary Tao - Professional Tactician" -- "Chilled - Dastardly Space Pirate" [label="2", tooltip="+500 ATK,+1 Ki"];
"Goku (Angel) - Messenger from another world" -- "Gohan (Teen) - Grand Plan" [label="2", tooltip="+2500 ATK when using Super Attack,+500 ATK"];
"Goku (Angel) - Messenger from another world" -- "Goku - Determined Defender" [label="3", tooltip="+2500 ATK when using Super Attack,+10% ATK,+500 ATK"];
"Goku (Angel) - Messenger from another world" -- "Goku - The Saiyan Among Us" [label="2", tooltip="+2500 ATK when using Super Attack,+500 ATK"];
"Gohan (Teen) - Grand Plan" -- "Goku - Determined Defender" [label="2", tooltip="+2500 ATK when using Super Attack,+500 ATK"];
"Gohan (Teen) - Grand Plan" -- "Goku - The Saiyan Among Us" [label="2", tooltip="+2500 ATK when using Super Attack,+500 ATK"];
"Chilled - Dastardly Space Pirate" -- "Frieza(1st From) - Embodiment of Evil" [label="2", tooltip="+2 Ki,+15% ATK"];
"Goku - The Saiyan Among Us" -- "Krillin - Martial Stability" [label="2", tooltip="+1 Ki,+500 ATK"];
"Mercenary Tao - Professional Tactician" -- "Cyborg Tao - Mercenary's Mettle" [label="3", tooltip="+1 Ki,+500 ATK,+500 ATK"];
"Super Saiyan Bardock - The First Awakened" -- "King Vegeta - Proud Royalty" [label="2", tooltip="+700 ATK,+15% ATK"];
"Goku - Determined Defender" -- "Gohan (Kid) - Slumbering Strength" [label="2", tooltip="+1 Ki,+500 ATK"];
"Goku - Determined Defender" -- "Goku (Kid) - Innocent Challenger" [label="2", tooltip="+2500 ATK when using Super Attack,+1 Ki"];
"Android #18 (Future) - Dastardly Demoness" -- "Android #17 (Future) - A Future Forsaken" [label="3", tooltip="Ki +2,+500 ATK,Ki +1"];
"Android #18 - Alluring Assassin" -- "Android #17 - Dauntless Runner" [label="2", tooltip="+2 Ki,+10% ATK"];
"Mecha Frieza - Reborn for Revenge" -- "Cyborg Tao - Mercenary's Mettle" [label="2", tooltip="+2 Ki,ATK +15%"];
"Mecha Frieza - Reborn for Revenge" -- "Frieza(1st Form) - Emperor of Iniquity" [label="2", tooltip="+15% ATK,+700 ATK"];
"Mecha Frieza - Reborn for Revenge" -- "Vegeta - Saiyan Elite" [label="2", tooltip="ATK +15%,+700 ATK"];
"Android #18 - Beautiful but Deadly" -- "Android #17 - Dauntless Runner" [label="2", tooltip="+2 Ki,+10% ATK"];
"King Vegeta - Proud Royalty" -- "Vegeta - Saiyan Elite" [label="3", tooltip="+700 ATK,ATK +15%,+1 Ki"];
"Cell (Perfect Form) - Perfect Power" -- "Cell (2nd Form) - Strength Evolved" [label="2", tooltip="+1 Ki,+500 ATK"];
"Frieza(1st Form) - Emperor of Iniquity" -- "Frieza(1st From) - Embodiment of Evil" [label="2", tooltip="ATK +25% when HP is 10% or below,+700 ATK"];
"Cyborg Tao - Mercenary's Mettle" -- "Jackie Chun - Seasoned Sensei" [label="2", tooltip="ATK +15%,+1 Ki"];
}