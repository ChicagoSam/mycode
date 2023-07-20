#!/usr/bin/env python3

# Character01 info
char01 = {
        "nam": "Minsc",
        "anc": "Human",
        "cls": "Ranger",
        "lev": "10",
        "aln": "Chaotic Good",
        "str": "18/93", 
        "dex": "15", 
        "con": "16", 
        "int": "10", 
        "wis": "15", 
        "cha": "14"
        }

# Print Character01 info in readable format
print(f"{char01['nam']} is a {char01['aln']} {char01['anc']} {char01['cls']}\n"   
    f"He has the following stats:\n"  
    f"  Strength: {char01['str']}\n"
    f"  Dexterity: {char01['dex']}\n"
    f"  Constitution: {char01['con']}\n"  
    f"  Intelligence: {char01['int']}\n"  
    f"  Wisdom: {char01['wis']}\n"  
    f"  Charisma: {char01['cha']}"
    )
