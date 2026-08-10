# 04_BESTIARY — RAIMDELLE CODEX ASGARD
Version v1.3 | Source: Raimdelle Codex Asgard (community monster manual for the FFXIV x D&D 5e Compendium)

> **THIS FILE IS A DATA ARCHIVE, NOT AN OUTPUT TEMPLATE.** The rows below are creatures compressed to
> stay small: English labels (AC/HP/STR), fields separated by `|`, and CR followed by its XP figure.
> **None of that is ever printed.** At the table a stat block has its own shape — Italian labels
> (CA/PF/FOR), one category per line, no pipes, and the GdS line carrying the bare number with no XP.
> Take the NUMBERS and the creature's PROFILE from here, never the page layout; and those numbers are
> a starting point to be scaled to the target GdS, not a value to copy.

## SCHEMA NOTES
- PRINCIPLE: completeness over brevity. Statblocks reproduced verbatim; only reformatted for parsing.
- DATA LANGUAGE = English (single source of truth). The assistant renders flavor into Italian at OUTPUT.
- MEASUREMENTS = metric, pre-converted (decimal POINT in data; render with comma at output). Key: 5 ft=1.5 m, 10 ft=3 m, 15 ft=4.5 m, 20 ft=6 m, 25 ft=7.5 m, 30 ft=9 m, 35 ft=10.5 m, 40 ft=12 m, 45 ft=13.5 m, 50 ft=15 m, 60 ft=18 m, 100 ft=30 m, 120 ft=36 m, 150 ft=45 m, 200 ft=60 m, 300 ft=90 m, 500 ft=150 m.
- Monsters store FIXED hit points here (no HP_ref), in English. ROLE (06 §B6 scale-first): each block is a LORE/CHASSIS reference — use it for the creature's type, signature moves, behaviour and defensive profile (resistances/vulnerabilities/immunities/senses); its printed CR/HP/damage are a STARTING POINT to SCALE to the target GdS (HP within the GdS band-range), NOT a verbatim authority. So a block's own CR need not match the encounter's GdS, and known data errors here are harmless (they get scaled away). Never free-invent numbers — scale from a chassis + the band.
- ORGANIZATION: 13 creature classes (Ashkin, Beastkin, Cloudkin, Dragon, Forgekin, Primals, Scalekin, Seedkin, Soulkin, Spoken, Vilekin, Voidsent, Wavekin). Within a class, by genus then species.
- OCR FLAGS: source-extraction errors are flagged inline as [OCR: ...] rather than silently "fixed" or invented.
- This file is built in blocks (append workflow). v0.1 = Block 1 (Ashkin, Beastkin, Cloudkin).

# CLASS: ASHKIN
Ashkin are beings whose natural return to the lifestream (the cycle of death and rebirth) has been interrupted — by dark necromancy, or by deep regret/rage tethering them to the material world — warping their bodies into haunting creatures.

## Genus: Ghost
The manifested spirit of one who could not complete a life's goal; despite an ethereal look, it forms a tangible fleshy body when it manifests.

### Bogy — Small Undead (Ghost), Neutral Evil
- AC 11 | HP 22 (4d6+8) | Speed 9 m fly (hover) | CR 1/4 (50 XP)
- STR 6(-2) DEX 12(+1) CON 14(+2) INT 8(-1) WIS 10(+0) CHA 16(+3)
- Damage Resistances bludgeoning, piercing, slashing from nonmagical weapons | Damage Immunities poison, necrotic
- Condition Immunities exhaustion, frightened, poisoned, unconscious | Senses passive Perception 10 | Languages —
- Cursed Aura. Creatures within 3 m must make a DC 13 Charisma save when they attempt to cast a spell; on a failure the spell is prevented.
- Actions — Cursed Tail: melee spell attack +5, reach 1.5 m, 5 (1d4+3) necrotic. Malice (Recharge 5–6): 3 m radius sphere, DC 13 Constitution save, 5 (2d4) necrotic (half on success). (Credit: Soren of Asgard.)

### Bhoot — Medium Undead (Ghost), Neutral Evil
- AC 14 (natural) | HP 60 (8d8+24) | Speed 12 m fly (hover) | CR 4 (1,100 XP)
- STR 14(+2) DEX 12(+1) CON 18(+4) INT 8(-1) WIS 14(+2) CHA 18(+4)
- Damage Resistances b/p/s from nonmagical weapons | Damage Immunities poison, necrotic
- Condition Immunities exhaustion, frightened, poisoned, unconscious | Senses passive Perception 12 | Languages —
- Cursed Aura. Creatures within 3 m must make a DC 14 Charisma save when they attempt to cast a spell; on a failure the spell is prevented.
- Actions — Multiattack: one Cursed Claws and one Drain Essence if possible. Cursed Claws: melee weapon attack +5, reach 1.5 m, 5 (1d6+2) slashing and grappled (escape DC 14; target restrained; can't claw another). Drain Essence: melee spell attack +5, reach 1.5 m, 21 (6d6+4) necrotic, heals the bhoot half the damage (grappled target only). Terror Touch (Recharge 4–6): ranged spell attack +6, reach 18 m, 27 (6d8) necrotic; on a hit DC 14 Charisma save or speed becomes 0 and the bhoot has advantage on Cursed Claws against it until the end of its next turn. (Credit: Soren of Asgard.)

## Genus: Gravekeeper
### Gravekeeper — Large Undead, Lawful Evil
- AC 14 (2 shields) | HP 171 (18d10+72) | Speed 9 m | CR 7 (2,900 XP)
- STR 16(+3) DEX 14(+2) CON 14(+2) INT 6(-2) WIS 10(+0) CHA 16(+3)
- Damage Immunities poison, necrotic | Condition Immunities exhaustion, frightened, poisoned, unconscious | Saving Throws Constitution +7 | Senses passive Perception 10 | Languages —
- Brute. A melee weapon attack deals one extra die of its damage when the gravekeeper hits (included).
- Undead Fortitude. If damage reduces it to 0 HP, it makes a Constitution save (DC 5 + damage taken) unless the damage is radiant or from a critical hit; on a success it drops to 1 HP instead. [OCR: source text says "zombie" — a template leftover; applies to the gravekeeper.]
- Actions — Multiattack: 2 Coffin Slams. Coffin Slam: melee weapon attack +6, reach 3 m, 22 (3d12+3) bludgeoning. March of the Dead (Recharge 5–6): 9 m cone, DC 14 Constitution save, 20 (4d10) necrotic and prone on a fail (half, no prone on success). (Credit: Soren of Asgard.)

# CLASS: BEASTKIN
Warm-blooded, hair-covered creatures that bear live young. Some mild-mannered beastkin are domesticated; most see bipedal humanoids as a threat.

## Genus: Bear
### Gold Bear — Large beast, unaligned
- AC 13 (natural) | HP 57 (6d10+24) | Speed 12 m | CR 3 (700 XP)
- STR 20(+5) DEX 10(+0) CON 18(+4) INT 2(-4) WIS 14(+2) CHA 7(-2)
- Saving Throws STR +7, CON +6 | Skills Perception +4 | Senses darkvision 18 m, passive Perception 14 | Languages —
- Keen Smell. Advantage on Wisdom (Perception) checks relying on smell.
- Actions — Multiattack: one Gouge and one Claws. Gouge: +7, reach 1.5 m, 14 (2d8+5) piercing. Claws: +7, reach 1.5 m, 12 (2d6+5) slashing. (Credit: JPLDN.)

## Genus: Behemoth
First sighted after the Seventh Umbral Calamity in the mountains of Coerthas; some believe them spawn of the elder primal Bahamut.

### Behemoth — Huge beast, unaligned
- AC 17 (natural) | HP 220 (21d12+84) | Speed 12 m | CR 10 (5,900 XP)
- STR 22(+6) DEX 14(+2) CON 18(+4) INT 7(-3) WIS 14(+2) CHA 18(+4)
- Saving Throws Strength +9, Constitution +8 | Skills Athletics +10, Perception +6, Intimidation +8 | Damage Resistances b/p/s from nonmagical attacks | Senses darkvision 18 m | Languages —
- Brute. Heave: if it moves at least 6 m straight toward a target and hits with Gore that turn, +6 (1d12) piercing and DC 16 Strength save or knocked prone. Sure Footed: advantage on STR/DEX saves vs prone. Innate Spellcasting (CHA, DC 16): 1/day each Call Lightning, Fireball, Ice Storm, Storm Sphere.
- Actions — Multiattack: one bite, one claw, one gore. Bite: +10, reach 1.5 m, 15 (2d8+6) piercing. Claw: +10, reach 3 m, 17 (2d10+6) slashing. Gore: +10, reach 3 m, 19 (2d12+6) piercing. Trounce (Recharge 5–6): 9 m cone, DC 16 Strength save, 22 (5d8) bludgeoning + prone (half, no prone). Behemoth Comet (1/day): crashes at a point within 36 m, 9 m radius sphere, DC 16 Dexterity save, 16 (3d10) bludgeoning + 16 (3d10) fire (half).
- Bonus Action — Trample: +8, reach 1.5 m, 13 (2d6+6) bludgeoning (+2d6 vs a prone creature). (Credit: Soren of Asgard.)

## Genus: Coeurl
Feline predators native to the Near East/Thavnair; descended from escaped war beasts of the Pearl in the Black Shroud. They use electricity to stun prey.

### Coeurl — Large beast, unaligned
- AC 14 (natural) | HP 97 (13d10+26) | Speed 12 m | CR 5 (1,800 XP)
- STR 14(+2) DEX 18(+4) CON 14(+2) INT 10(+0) WIS 15(+2) CHA 11(+0)
- Skills Stealth +7, Survival +5 | Condition Immunities paralyzed | Senses darkvision 18 m, passive Perception 12 | Languages —
- Avoidance. On a save for half damage, takes none on success and half on failure. Pack Tactics. Predatory Pounce: long jump 9 m with or without a run; creatures in its path make a DC 15 Dexterity save or take 2d6 bludgeoning and are knocked prone (half, no prone on success).
- Actions — Multiattack: one Bite, one Charged Whisker. Bite: +7, reach 1.5 m, 13 (2d8+4) piercing. Charged Whisker: +7, reach 3 m, 11 (2d6+4) slashing + 3 (1d6) lightning; DC 15 Constitution save or paralyzed 1 minute (re-save at end of its turns). (Credit: Jotunn-Bane.)

## Genus: Goobbue
### Goobbue — Large beast, unaligned
- AC 13 (natural) | HP 114 (12d10+48) | Speed 9 m | CR 3 (700 XP) | Saving Throws Constitution +6
- STR 16(+3) DEX 8(-1) CON 19(+4) INT 5(-3) WIS 12(+1) CHA 7(-2) | Senses passive Perception 11 | Languages —
- Sure-Footed. Advantage on STR/DEX saves vs prone.
- Actions — Multiattack: 2 Slams. Slam: +5, reach 3 m, 9 (2d6+3) bludgeoning. Sneeze (Recharge 5–6): 4.5 m cone, DC 14 Strength save, 16 (4d6) thunder + knocked back 3 m (half, no knockback). (Credit: Soren of Asgard.)

### Goobbue Gourmet — Large beast, unaligned
- AC 15 (natural) | HP 147 (14d10+70) | Speed 9 m | CR 5 (1,100 XP) | Saving Throws Constitution +8
- STR 17(+3) DEX 8(-1) CON 21(+5) INT 5(-3) WIS 14(+2) CHA 7(-2) | Senses passive Perception 12 | Languages —
- Goobbue's Grief. A creature that hits it with a melee attack while within 1.5 m makes a DC 16 Constitution save or takes 1d6 poison and is poisoned 1 minute (success = immune to Grief for 1 minute; poisoned creature re-saves at end of its turns). Sure-Footed.
- Actions — Multiattack: 3 Slams. Slam: +6, reach 3 m, 12 (2d6+3) bludgeoning. Moldy Phlegm (Recharge 5–6): at a point within 9 m, 3 m radius sphere, DC 16 Dexterity save, 20 (4d8) bludgeoning and can't regain HP until the start of the Goobbue's next turn (half on success). Moldy Sneeze (Recharge 5–6): 4.5 m cone, DC 16 Strength save, 24 (6d6) thunder + prone (half, no prone). (Credit: Soren of Asgard.)

## Genus: Hoarhound
Lupine predators of the Coerthas Highlands; driven off by Ishgard, they reclaimed the region after the 7th Umbral Calamity froze Coerthas.

### Fenrir — Large monstrosity, unaligned
- AC 16 (natural) | HP 275 (22d10+154) | Speed 15 m | CR 14 (11,500 XP)
- STR 24(+7) DEX 20(+5) CON 24(+7) INT 11(+0) WIS 14(+2) CHA 14(+2)
- Saving Throws DEX +10, CON +12 | Skills Perception +7, Athletics +12 | Damage Resistances nonmagical b/p/s | Damage Immunities cold | Condition Immunities charmed, frightened, paralyzed, poisoned | Senses darkvision 36 m, passive Perception 17 | Languages —
- Divine Descendance (attacks magical). Keen Sight and Smell. Legendary Resistance (3/Day). Magic Resistance.
- Actions — Multiattack: two Claws, one Bite. Bite: +12, reach 1.5 m, 25 (4d8+7) piercing + 14 (4d6) cold. Claw: +12, reach 1.5 m, 18 (2d10+7) slashing. Hoarhound Roar (Recharge 6): 18 m cone, DC 16 Dexterity save, 12d8 cold (half). Thousand Year Storm: each creature within 18 m makes a DC 16 Strength save or is pushed 3 m, knocked prone, and speed reduced to 0 until end of its next turn (success = only pushed 3 m).
- Bonus Action — Hoarhound Dash: move up to speed toward a hostile creature without provoking opportunity attacks. (Credit: Jotunn-Bane.)

### Hoarhound — Large monstrosity, unaligned
- AC 14 (natural) | HP 161 (17d10+68) | Speed 10.5 m | CR 8 (3,900 XP)
- STR 20(+5) DEX 18(+4) CON 19(+4) INT 9(-1) WIS 12(+1) CHA 12(+1)
- Saving Throws DEX +7, CON +7 | Skills Perception +4, Athletics +8 | Damage Resistances nonmagical b/p/s, cold | Condition Immunities charmed, frightened, paralyzed, poisoned | Senses darkvision 36 m, passive Perception 14 | Languages —
- Keen Sight and Smell. Pack Tactics. Pounce: move 6 m straight + claw hit = DC 14 Strength save or prone; if prone, bonus-action bite.
- Actions — Multiattack: one Claw, one Bite. Bite: +8, reach 1.5 m, 23 (4d8+5) piercing + 14 (4d6) cold. Claw: +8, reach 1.5 m, 16 (2d10+5) slashing. Hoarhound Roar (1/Day): 18 m cone, DC 14 Dexterity save, 8d8 cold (half). Blizzard III (Recharge 5–6): 6 m radius sphere within range, DC 14 Constitution save, 8d6 cold (half); ground becomes slick ice 1 minute (moving >half speed = DC 14 Acrobatics check or fall prone).
- Bonus Action — Hoarhound Dash (as Fenrir). (Credit: Jotunn-Bane.)

# CLASS: CLOUDKIN
United by flight (wings, aether, or gases). Long tamed for war and transport; some species abandoned the skies to stay on land.

## Genus: Chocobo
Beasts of burden, intelligent and easy to tame; great allies in work and, with training, in battle.

### Chocobo (Domestic) — Large beast, unaligned
- AC 11 | HP 9 (2d10) | Speed 18 m | CR 1/4 (50 XP)
- Actions — Beak: +5, reach 1.5 m, 7 (1d8+3) slashing. Claw: +5, reach 1.5 m, 6 (1d6+3) slashing. (Credit: Soren of Asgard.)

### Abalathian Chocobo — Large beast, unaligned
- AC 10 | HP 11 (2d10+2) | Speed 12 m | CR 1/4 (50 XP)
- STR 18(+4) DEX 12(+1) CON 12(+1) INT 3(-4) WIS 11(+0) CHA 7(-2) | Senses passive Perception 10
- Actions — Beak: +5, reach 1.5 m, 8 (1d8+4) slashing. Claw: +5, reach 1.5 m, 7 (1d6+4) slashing.

### La Noscean Chocobo — Medium beast, unaligned
- AC 13 | HP 8 (2d8) | Speed 18 m | CR 1/4 (50 XP)
- STR 14(+2) DEX 16(+3) CON 10(+0) INT 3(-4) WIS 11(+0) CHA 9(-1) | Senses passive Perception 10
- Actions — Beak: +5, reach 1.5 m, 6 (1d8+2) slashing. Claw: +5, reach 1.5 m, 5 (1d6+2) slashing.

### War Chocobo (template)
A Chocobo trained for battle gains: +1 Hit Die of HP; the Multiattack action (one Beak and one Claw); optionally Barding (adjust AC). Barding AC: Leather +1, Studded Leather +2, Ring Mail 14, Scale Mail +4, Chain Mail / Splint / Plate (as the armor). Sagely Fowl (optional): WIS +2, learns Cure Wounds (WIS casting), may cast it twice per day.

### Dalmascan Red — Large beast, unaligned
- AC 15 (natural) | HP 136 (16d10+48) | Speed 18 m | CR 5 (1,800 XP)
- STR 14(+2) DEX 16(+3) CON 16(+3) INT 6(-2) WIS 16(+3) CHA 10(+0) | Senses passive Perception 11
- Brute. Innate Spellcasting (WIS, DC 14): 3/day Burning Hands; 1/day Fireball.
- Actions — Multiattack: two Beak, one Claw. Beak: +6, reach 1.5 m, 13 (2d8+2) piercing. Claw: +6, reach 1.5 m, 11 (2d6+2) slashing. (Credit: Soren of Asgard.)
### Fat Chocobo — Huge beast, unaligned
- AC 14 (natural) | HP 125 (10d12+60) | Speed 6 m | CR 4 (1,100 XP)
- STR 20(+5) DEX 8(-1) CON 22(+6) INT 3(-4) WIS 16(+3) CHA 10(+0) | Senses passive Perception 13 | Languages —
- Sure Footing (movement unaffected by difficult terrain). Roly-Poly: if it Dashes and moves at least 6 m straight toward a target, it may make a Body Slam as a bonus action (a creature target makes a DC 14 Strength save or is knocked prone). Innate Spellcasting (WIS, DC 14): At will Earth Tremor; 3/day Thunderwave.
- Actions — Multiattack: 3 Beaks. Beak: +6, reach 3 m, 10 (1d8+5) piercing. Body Slam: +6, reach 1.5 m, 12 (1d12+5) bludgeoning (+1d12 if the target is prone); the target is then crushed and restrained (escape DC 14), freed when the Fat Chocobo moves.
- Reactions — Stomping Tantrum: when a creature enters a space within 3 m of it, it may cast Earth Tremor. (Credit: Soren of Asgard.)

### Ishgardian Black — Large beast, unaligned
- AC 13 | HP 9 (2d10) | Speed 6 m, fly 18 m | CR 1/2 (100 XP)
- STR 16(+3) DEX 16(+3) CON 10(+0) INT 3(-4) WIS 11(+0) CHA 8(-1) | Senses passive Perception 10 | Languages —
- Actions — Aerial Multiattack: while flying, it may make two Finesse Claw attacks as its action. Beak: +5, reach 1.5 m, 7 (1d8+3) slashing. Claw: +5, reach 1.5 m, 6 (1d6+3) slashing. Finesse Claw: +5, reach 1.5 m, 6 (1d6+3) slashing. (Credit: Soren of Asgard.)
- Lore note: the Fat Chocobo is revered as a symbol of fertility/harvest/prosperity (flocks gather around it and treat it as a leader); the Ishgardian Black is a dark-feathered, flight-capable breed developed in Ishgard, favored by messengers.

## Genus: Deathgaze
### Deathgaze — Large monstrosity, neutral evil
- AC 15 (natural) | HP 75 (10d10+20) | Speed 9 m walk, 9 m fly | CR 8 (3,900 XP)
- STR 18(+4) DEX 17(+3) CON 14(+2) INT 16(+3) WIS 15(+2) CHA 16(+3)
- Saving Throws DEX +6, CON +5 | Skills Acrobatics +6, Athletics +7 | Damage Resistances nonmagical b/p/s, lightning | Condition Immunities paralyzed | Senses passive Perception 12 | Languages —
- Lightning Absorption (lightning damage heals it instead). Magic Weapons. Innate Spellcasting (INT, DC 14, +6): At Will Aero II (*Aerora, see 03_Spells).
- Actions — Multiattack: 3 Talons. Talon: +7, reach 1.5 m, 13 (2d8+4) slashing. Bombination (Recharge 5–6): point within 36 m, 6 m radius sphere, DC 16 Dexterity save, 4d6 lightning and Slow until end of its next turn (half, no slow). (Credit: Jotunn-Bane.)

## Genus: Yol
Large cloudkin of the Azim Steppe (Othard). Steppe warriors tame one at the end of the Bardam's Mettle trial, forming a lifelong bond.

### Yol — Large monstrosity, unaligned
- AC 14 | HP 114 (12d10+48) | Speed 9 m walk, 18 m fly | CR 6 (2,300 XP)
- STR 11(+0) DEX 19(+4) CON 19(+4) INT 3(-4) WIS 14(+2) CHA 10(+0)
- Skills Perception +8 | Senses darkvision 18 m, passive Perception 18 | Languages —
- Bonded Understanding (understands a bonded rider's language). Flyby. Keen Sight.
- Actions — Multiattack: one Beak and two Talons (may replace one with Wingbeat). Beak: +7, reach 1.5 m, 10 (1d12+4) piercing. Talon: +7, reach 1.5 m, 11 (2d6+4) slashing. Wingbeat: creatures within 4.5 m make a DC 15 Strength save or take 2d6 bludgeoning, are pushed 3 m and knocked prone (half, no push/prone). Feathercut (Recharge 5–6): 6 m cone, DC 15 Dexterity save, 7d8 magical slashing (half). (Credit: Jotunn-Bane.)

## Genus: Zu
Native to the Near East deserts; since the Calamity they stay in Eorzea year-round, favoring northern Vylbrand and the Sea of Clouds.

### Zu — Large monstrosity, unaligned
- AC 15 (natural) | HP 76 (8d10+32) | Speed 7.5 m walk, 12 m fly | CR 3 (700 XP)
- STR 17(+3) DEX 14(+2) CON 18(+4) INT 6(-2) WIS 13(+1) CHA 7(-2)
- Skills Acrobatics +6, Perception +3 | Condition Immunities sleep, petrified | Senses passive Perception 13 | Languages —
- Actions — Multiattack: one Bite and two Claws. Bite: +5, reach 1.5 m, 10 (2d6+3) slashing. Claw: +5, reach 1.5 m, 7 (1d8+3) slashing. Sonic Boom: 9 m long, 3 m wide line, DC 13 Constitution save, 2d6 thunder and stunned until end of its next turn (success = no damage, not stunned). (Credit: Jotunn-Bane.)

# CLASS: DRAGON
Highly intelligent beings between Scalekin and Spoken, with vast lineage and history; they hatch from egg clutches and value family bonds greatly. (Languages: Draconic.)

## Genus: Aevis
### Aevis — Large dragon, Neutral Evil
- AC 14 (natural) | HP 123 (13d10+52) | Speed 9 m walk, 9 m fly | CR 4 (1,100 XP)
- STR 18(+4) DEX 14(+2) CON 18(+4) INT 6(-2) WIS 6(-2) CHA 8(-1)
- Skills Athletics +6 | Damage Resistances lightning | Senses blindsight 3 m, darkvision 18 m, passive Perception 8 | Languages Draconic
- Aggressive (bonus action: move up to speed toward a hostile creature). Keen Senses. Lunge: if it moves at least 6 m straight toward a creature and hits with a claw that turn, +2d6 damage and DC 14 Strength save or prone; if prone, bonus-action bite.
- Actions — Multiattack: one Bite, one Claw. Bite: +6, reach 1.5 m, 11 (2d6+4) piercing. Claw: +6, reach 1.5 m, 8 (1d8+4) slashing. Lightning Breath (Recharge 5–6): 9 m cone, DC 14 Dexterity save, 3d6 lightning and stunned until end of its next turn (half, not stunned). Strident Scream (Recharge 6): creatures within 9 m that can hear it make a DC 14 Constitution save, 6d6 psychic (half); concentration saves vs this damage have disadvantage. (Credit: Jotunn-Bane.)

## Genus: Amphiptere
### Amphiptere — Large dragon, unaligned
- AC 15 | HP 153 (18d10+54) | Speed 12 m, 12 m fly | CR 6 (2,300 XP)
- STR 14(+2) DEX 16(+3) CON 16(+3) INT 10(+0) WIS 12(+1) CHA 15(+2) | Senses passive Perception 11 | Languages Draconic
- Actions — Multiattack: 3 Pecks. Peck: +6, reach 1.5 m, 12 (2d8+3) piercing. Calamitous Wind (Recharge 3–4): 4.5 m cone, DC 13 Strength save, 20 (4d10) thunder and knocked back 4.5 m (half, no knockback). Warped Wail (Recharge 5–6): 4.5 m radius sphere, DC 13 Wisdom save, 21 (6d6) psychic and charmed by the Amphiptere on a fail (half, no charm). While charmed: speed halved, -2 AC and Dexterity saves, no reactions, only one action OR bonus action per turn, max one attack per turn; re-save at end of each of its turns. (Credit: Soren of Asgard.)

## Genus: Brobinyak
### Brobinyak — Large dragon, unaligned
- AC 15 (natural) | HP 133 (14d10+56) | Speed 15 m | CR 5 (1,800 XP)
- STR 16(+3) DEX 16(+3) CON 18(+4) INT 10(+0) WIS 10(+0) CHA 14(+2) | Senses passive Perception 11 | Languages Draconic
- Draconic Thorns. A creature that makes a melee weapon attack against it takes 2 (1d4) piercing.
- Actions — Multiattack: 2 Gouges. Gouge: +6, reach 1.5 m, 16 (2d12+3) piercing. Body Slam (Recharge 3–4): 3 m radius circle, DC 15 Strength save, 18 (4d10) bludgeoning + prone (half, no prone). Serpent's Apple (Recharge 5–6): 4.5 m cone, DC 15 Dexterity save, 19 (3d12) piercing (half). (Credit: Soren of Asgard.)

## Genus: Dragon
### Dragonet — Small dragon, unaligned
- AC 13 (natural) | HP 9 (2d6+2) | Speed 4.5 m walk, 9 m fly | CR 1/4 (50 XP)
- STR 6(-2) DEX 15(+2) CON 13(+1) INT 10(+0) WIS 12(+1) CHA 10(+0)
- Skills Perception +3, Acrobatics +4 | Senses blindsight 3 m, darkvision 18 m, passive Perception 13 | Languages understands Draconic but can't speak it
- Keen Senses.
- Actions — Bite: +4, reach 1.5 m, 4 (1d4+2) piercing. Final Yip: upon death, each dragon of higher CR within 18 m that can hear it may immediately make an attack with advantage. (Credit: Jotunn-Bane.)

### Lesser Dragon — Large dragon, unaligned
- AC 15 (natural) | HP 95 (10d10+40) | Speed 9 m | CR 3 (700 XP)
- STR 17(+3) DEX 14(+2) CON 18(+4) INT 6(-2) WIS 13(+1) CHA 11(+0)
- Skills Perception +3, Survival +3, Athletics +5 | Senses blindsight 3 m, darkvision 18 m, passive Perception 13 | Languages Draconic
- Berserk. At the start of its turn with 25 HP or fewer, roll a d6; on a 6 it goes berserk (attacks nearest creature; attacks with advantage) until destroyed or back to full HP. Keen Senses. Rampage: when it reduces a creature to 0 HP with a melee attack, bonus action to move up to half speed and make a bite.
- Actions — Multiattack: one Bite, one Claw. Bite: +5, reach 1.5 m, 10 (2d6+3) piercing. Claw: +5, reach 1.5 m, 7 (1d8+3) slashing. Fire Breath (Recharge 6): 6 m cone, DC 13 Dexterity save, 3d6 fire and ignited (half, no ignite); an ignited creature takes 1d6 fire at the start of its turns (action to pat out). (Credit: Jotunn-Bane.)

### Verge Dragon — Huge dragon, unaligned
- AC 17 (natural) | HP 237 (19d12+114) | Speed 18 m | CR 12 (8,400 XP)
- STR 18(+4) DEX 18(+4) CON 22(+6) INT 10(+0) WIS 18(+4) CHA 10(+0)
- Damage Immunities lightning | Senses passive Perception 14 | Languages Draconic
- Avoidance. Critical Rip: crits on 19–20 and crits deal one extra damage die. Wild Charge: move 6 m straight + Rip hit = DC 18 Strength save or prone; if prone, bonus-action Vicious Rip.
- Actions — Multiattack: one Rip, one Spiked Tail. Rip: +8, reach 3 m, 20 (3d10+4) slashing. Spiked Tail: +8, reach 3 m, 23 (3d12+4) piercing. Vicious Rip: +8, reach 3 m, 36 (6d10+4) slashing. Heat Lightning (Recharge 3–4): each creature in a 9 m radius sphere becomes a lightning rod targeted by a 3 m radius burst, DC 16 Dexterity save, 36 (8d8) lightning (half); a creature hit by multiple bursts saves once but takes both. Crackle Hiss (Recharge 5–6): 18 m cone, DC 18 Constitution save, 39 (7d10) lightning and paralyzed 1 minute (re-save at end of its turns).
- Bonus Action — Erratic Blaster: target within 9 m makes a DC 16 Constitution save or is paralyzed 1 minute (re-save at end of its turns). (Credit: Soren of Asgard.)

## Genus: Vouivre
### Vouivre — Large dragon, unaligned
- AC 15 | HP 127 (15d10+45) | Speed 3 m, 18 m fly | CR 5 (1,800 XP)
- STR 12(+2) DEX 18(+4) CON 16(+3) INT 10(+0) WIS 14(+2) CHA 15(+2) | Senses passive Perception 12 | Languages Draconic [OCR: source lists STR 12 with a (+2) modifier — reproduced verbatim]
- Flyby.
- Actions — Multiattack: one Bite, one Whipcrack. Bite: +7, reach 1.5 m, 8 (1d8+4) piercing. Whipcrack: +7, reach 1.5 m, 8 (1d8+4) slashing; on a hit DC 15 Constitution save, 18 (4d8) poison (half). Lumisphere (Recharge 5–6): point within 24 m, 6 m radius, DC 15 Dexterity save, 22 (4d10) radiant (half). (Credit: Soren of Asgard.)

## Genus: Wyvern
### Wyvern — Large dragon, unaligned
- AC 16 (natural) | HP 95 (10d10+40) | Speed 6 m walk, 15 m fly | CR 3 (700 XP)
- STR 14(+2) DEX 17(+3) CON 18(+4) INT 6(-2) WIS 13(+1) CHA 11(+0)
- Skills Perception +3, Survival +3, Acrobatics +5 | Damage Immunities poison | Condition Immunities poisoned | Senses blindsight 3 m, darkvision 18 m, passive Perception 13 | Languages Draconic
- Evasion. Keen Senses. Nimble Escape (Disengage or Dash as a bonus action).
- Actions — Multiattack: one Bite, one Claw. Bite: +5, reach 1.5 m, 10 (2d6+3) piercing. Claw: +5, reach 1.5 m, 7 (1d8+3) slashing. Tail Stinger: +5, reach 3 m, 6 (1d6+3) piercing + 7d6 poison; DC 14 Constitution save or poisoned 1 minute (re-save at end of its turns). (Credit: Jotunn-Bane.)

# CLASS: FORGEKIN
Mechanical beings built for specific purposes. Magitek = machina powered by ceruleum, used most by the Garlean Empire to offset its lack of magic.

## Genus: Magitek Machina
### Magitek Deathclaw — Medium construct, neutral
- AC 13 (natural) | HP 60 (8d8+24) | Speed 9 m fly (hover) | CR 3 (700 XP)
- STR 20(+5) DEX 9(-1) CON 16(+3) INT 10(+0) WIS 10(+0) CHA 10(+0)
- Damage Vulnerabilities lightning | Damage Immunities psychic | Condition Immunities poisoned, diseased, exhaustion, sleep, charmed | Senses darkvision 18 m, passive Perception 10 | Languages Common plus a language spoken by its creator
- Actions — Multiattack: 2 Death Grips. Death Grip: +7, reach 1.5 m, 9 (1d8+5) piercing; if the target is Medium or smaller it is grappled (escape DC 15; only one target at a time). (Credit: HomemadeMovies.)

### Magitek Reaper — Large construct, neutral
- AC 16 (natural) | HP 94 (9d10+45) | Speed 12 m | CR 6 (2,300 XP)
- STR 20(+5) DEX 15(+2) CON 20(+5) INT 3(-4) WIS 10(+0) CHA 10(+0)
- Skills Athletics +8, Perception +6 | Damage Vulnerabilities lightning | Damage Immunities psychic | Condition Immunities charmed, diseased, frightened, poisoned, sleep, exhaustion | Senses darkvision 36 m, passive Perception 16 | Languages understands one language of its creator but can't speak
- Magic Resistance.
- Actions — Multiattack: [OCR: source reads "makes , and undefined" — the multiattack composition is missing/garbled; GM to choose among the actions below]. Photon Stream: 4.5 m cone, DC 15 Dexterity save, 36 (8d8) piercing (half). Magitek Cannon: a point within 36 m; creatures within 9 m make a DC 15 Dexterity save, 11 (2d10) force + 28 (8d6) fire (half).
- Bonus Action — Overclock (2/Day): Dash or Disengage. (Credit: HomemadeMovies.)

### Magitek Predator — Large construct, neutral
- AC 17 (natural) | HP 119 (14d10+42) | Speed 13.5 m | CR 9 (5,000 XP)
- STR 20(+5) DEX 13(+1) CON 16(+3) INT 10(+0) WIS 10(+0) CHA 10(+0)
- Skills Investigation +8, Perception +8 | Damage Resistances nonmagical b/p/s | Damage Immunities psychic | Damage Vulnerabilities lightning | Condition Immunities charmed, diseased, frightened, poisoned, sleep, exhaustion | Senses darkvision 36 m, passive Perception 18 | Languages Common plus one creator language
- Combat Ready (advantage on initiative). Magic Resistance. Magic Weapons.
- Actions — Multiattack: three Magitek Claw attacks; when its Magitek Ray or Magitek Missiles is available, it can use either in place of one Magitek Claw. [OCR: source names "Magitek Vanguard" here — a copy/paste leftover; the entry is the Predator.] Magitek Claw: +9, reach 1.5 m, 14 (2d8+5) slashing. Magitek Ray (Recharge 5–6): a line 30 m long, 1.5 m wide, DC 16 Dexterity save, 27 (8d6) lightning + 11 (2d10) force (half). Magitek Missiles (Recharge 5–6): up to three creatures, each DC 16 Dexterity save, 18 (4d8) fire (half). (Credit: HomemadeMovies.)

### Magitek Vanguard — Large construct, neutral
- AC 15 (natural) | HP 119 (14d10+42) | Speed 12 m | CR 6 (2,300 XP)
- STR 20(+5) DEX 15(+2) CON 17(+3) INT 3(-4) WIS 10(+0) CHA 10(+0)
- Saving Throws CON +6 | Skills Athletics +8, Intimidation +3, Perception +6 | Damage Vulnerabilities lightning | Damage Resistances nonmagical b/p/s | Damage Immunities psychic | Condition Immunities charmed, diseased, frightened, poisoned, sleep, exhaustion | Senses darkvision 36 m, passive Perception 16 | Languages Common plus one creator language
- Magic Resistance. Siege Monster (double damage to objects and structures).
- Actions — Multiattack: three Cermet Drill attacks. Cermet Drill: +8, reach 1.5 m, 10 (1d10+5) piercing. Drill Cannons (Recharge 5–6): a line 9 m long, 1.5 m wide, DC 15 Strength save, 18 (4d8) piercing and knocked prone on a fail (half, not prone on success). (Credit: HomemadeMovies.)

# CLASS: PRIMALS
Primals (eikons) are born of prayer and offerings of aetheric crystals; while they live they drain the land's aether. Summoning was spread by the Ascians. A primal mirrors its summoner's intentions (territory, protection, or — under duress — unbridled rage).

## Mythic Monsters (rules note)
From "Mythic Odysseys of Theros": optional traits for boss creatures. Mythic Trait: activates when the boss is reduced to 0 HP — it recovers HP, performs an action/gains a trait, and the battle continues. Mythic Actions: extra Legendary-Action options available for 1 hour after the Mythic Trait activates. If a statblock lists Mythic Actions, the GM is not compelled to use them.

## Genus: Garuda
Ixali legend holds the Ixal once served Garuda as divine soldiers. The Lady of the Vortex is wild, cruel, and greedy — willing to sacrifice other tribes and aim for outright destruction.

### Garuda, Lady of the Vortex — Large elemental, Chaotic Evil
- AC 18 (natural) | HP 285 (30d10+120) | Speed 9 m, 18 m fly | CR 15 (13,000 XP)
- STR 18(+4) DEX 20(+5) CON 18(+4) INT 18(+4) WIS 18(+4) CHA 20(+5)
- Saving Throws DEX +10, CON +9, CHA +10 | Skills Acrobatics +10, Perception +9 | Damage Resistance nonmagical b/p/s | Damage Immunities thunder | Condition Immunities charmed, exhaustion, frightened, poisoned | Senses passive Perception 19 | Languages — [OCR: source repeats "Languages"]
- Reckoning (Mythic Trait; Recharges after a Short or Long Rest). At 0 HP she doesn't die: regains 285 HP, summons Suparna and Chirada within 12 m, summons a Storm of Reckoning (below), and now benefits from her own Malicious Aura.
- Flyby. Legendary Resistance (3/Day) [OCR: source says "If Odin fails" — copy leftover; applies to Garuda]. Magic Weapons. Malicious Aura: Garuda's allies within 9 m deal +5 thunder damage on all attacks.
- Actions — Multiattack: 3 Talon attacks [OCR: "makes 3 and talon attacks"].
  - **Talon:** +10, reach 3 m, 10 (1d10+5) slashing.
  - **Friction:** a 4.5 m radius sphere at a point within 18 m; DC 18 Dexterity save, 22 (4d10) thunder (half) [OCR: source omits the DC — 18 = Garuda's save DC].
  - **Wicked Wheel:** 4.5 m radius around her, DC 18 Strength save, 14 (3d8) bludgeoning + 14 (3d8) thunder + knocked back 4.5 m (half, no knockback).
  - **Slipstream (Recharge 3–4):** 4.5 m cone, DC 18 Constitution save, 36 (8d8) thunder + stunned until end of its next turn (half, not stunned).
  - **Aerial Blast (Recharge 5–6):** 6 m radius, 12 m high cylinder within 18 m, DC 18 Dexterity save, 36 (8d8) thunder (half) [OCR: source's "not be stunned" is a copy error — no stun in this effect]; the area is howling winds (difficult terrain) for 1 minute: entering/starting there = DC 18 Strength save, 9 (2d8) thunder (half).
  - **Summon Egis (1/Day):** one Suparna and one Chirada within 12 m.
- Bonus Action — Feather Rain: 3 m radius circle around her, DC 18 Dexterity save, 9 (2d8) piercing (half); then move up to 9 m of fly speed.
- Legendary Actions (3): Swipe (one Talon). Soar (move 9 m fly). Feather Storm (2 Actions: use Feather Rain).
- Mythic Actions (while Reckoning active): Vengeful Talon (one Talon + 5 thunder). Feather Hell (use Feather Rain). Torturous Wheels (2 Actions: Garuda or Suparna uses Wicked Wheel). (Credit: Soren of Asgard.)

#### Storm of Reckoning (environment)
A 90 m radius, 150 m tall cylinder of raging dark winds. Center = the eye of the storm, a 12 m radius, 150 m tall cylinder of strong updraft granting all creatures without a fly speed a 9 m fly speed while inside. A creature entering the raging winds or starting its turn there: DC 18 Strength save or take 7 (2d6) thunder + 7 (2d6) slashing and be forcibly moved — if airborne, dragged 18 m toward the ground; if grounded, dragged 18 m toward the eye in a straight line (1d6 bludgeoning per 3 m moved this way if it hits the ground/an object). Difficult terrain. On a success, half damage and not moved. The winds are difficult terrain when moving away from the eye.

### Chirada — Medium elemental (egi), Chaotic Evil
- AC 15 | HP 136 (16d8+64) | Speed 9 m, 18 m fly | CR 5 (1,800 XP)
- STR 14(+2) DEX 20(+5) CON 16(+3) INT 16(+3) WIS 18(+4) CHA 16(+3)
- Damage Immunities thunder | Condition Immunities charmed, exhaustion, frightened, poisoned | Senses passive Perception 13 | Languages —
- Flyby. Soothing Winds: at the start of Chirada's turn, all of her allies within 9 m recover 13 (3d6+3) HP.
- Actions — Multiattack: 2 Talon attacks. Talon: +8, reach 1.5 m, 9 (1d8+5) slashing. (Credit: Soren of Asgard.)

### Suparna — Medium elemental (egi), Chaotic Evil
- AC 15 | HP 136 (16d8+64) | Speed 9 m, 18 m fly | CR 5 (1,800 XP)
- STR 16(+3) DEX 20(+5) CON 16(+3) INT 10(+0) WIS 16(+3) CHA 18(+4)
- Damage Immunities thunder | Condition Immunities charmed, exhaustion, frightened, poisoned | Senses passive Perception 13 | Languages —
- Flyby. Malicious Aura: Suparna's allies within 9 m deal +4 thunder damage on all attacks.
- Actions — Multiattack: 2 Talon attacks. Talon: +8, reach 1.5 m, 10 (1d10+5) slashing. Friction: a 3 m radius sphere within 18 m, DC 15 Dexterity save, 16 (3d10) thunder (half). Wicked Wheel: 3 m radius around her, DC 15 Strength save, 9 (2d8) bludgeoning + 9 (2d8) thunder + knocked back 3 m (half, no knockback). (Credit: Soren of Asgard.)

## Genus: Ifrit
### Ifrit, Lord of the Inferno — Large elemental, Chaotic Evil
- AC 18 (natural) | HP 287 (23d10+161) | Speed 12 m | CR 17 (18,000 XP, PB +6)
- STR 27(+8) DEX 18(+4) CON 25(+7) INT 10(+0) WIS 14(+2) CHA 12(+1)
- Saving Throws STR +14, DEX +10, CON +13 | Skills Athletics +14, Acrobatics +10 | Damage Resistances nonmagical b/p/s | Damage Immunities fire, poison | Condition Immunities poisoned, exhaustion, frightened, charmed, sleep | Senses blindsight 18 m, passive Perception 12 | Languages Primordial
- Fire Absorption (fire damage heals it instead). Legendary Resistance (3/Day). Magic Nature (attacks are magical; advantage on saves vs spells and magical effects). Searing Aura: at the start of each of its turns, each creature within 1.5 m makes a DC 18 Constitution save or takes 3d6 fire. Crimson Cyclone (Mythic Trait; Recharges after a Short or Long Rest): if reduced to 0 HP, resets to 287 HP and gains Mythic Actions for 1 hour; award the party +25,000 XP (50,000 total) for defeating it after this trait activates.
- Actions — Multiattack: Frightful Presence once, then two Claws and one Tail. Claw: melee +14, reach 1.5 m, 19 (2d10+8) slashing + 4 (1d8) fire. Tail: melee +14, reach 3 m, 17 (2d8+8) bludgeoning + 4 (1d8) fire. Incinerate (Recharge 5–6): 9 m cone, DC 18 Dexterity save, 8d8 fire (half). Frightful Presence: each creature of its choice within 36 m and aware of it makes a DC 18 Wisdom save or is frightened 1 minute (re-save at end of its turns; on success or when it ends, immune 24 hours).
- Bonus Actions — Eruption (3/Day): the ground under each creature within 18 m erupts; DC 18 Dexterity save, 10d8 fire (half). Infernal Surge: move up to its speed toward a hostile creature it can see, without provoking opportunity attacks.
- Mythic Actions (while Crimson Cyclone is active, used as legendary actions) — Inferno Howl (Costs 3 Actions): summons an Infernal Nail in an unoccupied space within 9 m and channels aether into it (Nail: AC 12, HP 100, immune to fire and psychic, resistant to nonmagical b/p/s). Until the Nail is destroyed or explodes on the following round, Ifrit takes no actions; on initiative count 0 the next round the Nail explodes in an 18 m radius — each creature other than Ifrit becomes vulnerable to fire damage and Ifrit's Hellfire damage increases by 5d6 fire. [OCR: source also spells this "Infernal Howl".] Hellfire (1/Day, Costs 3 Actions): an 18 m radius around Ifrit, DC 20 Constitution save, 15d6 fire (half); usable ONLY after Inferno Howl. (Credit: Jotunn-Bane.)

## Genus: Leviathan
### Leviathan, Lord of the Whorl — Gargantuan elemental, neutral evil
- AC 18 (natural) | HP 277 (15d20+120) | Speed 9 m walk, 18 m swim | CR 17 (18,000 XP)
- STR 22(+6) DEX 18(+4) CON 26(+8) INT 14(+2) WIS 18(+4) CHA 12(+1)
- Saving Throws STR +12, DEX +10, WIS +10 | Skills Intimidation +7, Perception +10, Athletics +12, Acrobatics +10 | Damage Resistances nonmagical b/p/s | Damage Immunities acid | Condition Immunities charmed, exhaustion, petrified | Senses darkvision 36 m, passive Perception 20 | Languages Common, Aquan
- Agile Swimmer (underwater movement ignores difficult terrain). Amphibious. Corrupted Water: all water within 60 m is corrupted (creatures hold breath half as long, gain double exhaustion when suffocating in it). Legendary Resistance (3/Day). Call of the Depths (Recharges after a Short or Long Rest): if reduced to 0 HP, resets to 277 HP and summons a Wavespine Sahagin and a Wavetooth Sahagin within 18 m; gains Mythic Actions for 1 hour; award the party +25,000 XP (50,000 total) for defeating it after this trait activates.
- Actions — Multiattack: two Bites and one Tail; may replace one Bite with Scale Darts, or forgo both Bites to use Water Spout.
  - **Bite:** +12, reach 3 m, 19 (3d8+6) piercing.
  - **Tail:** +12, reach 4.5 m, 22 (3d10+6) bludgeoning.
  - **Scale Darts:** ranged +10, range 9/18 m, 15 (2d10+4) piercing.
  - **Water Spout:** a corrupted-water bubble at a point within 18 m; creatures within 3 m make a DC 19 Dexterity save, 18 (4d8) acid (half).
  - **Body Slam (Recharge 5–6):** a 12 m long, 6 m wide line, DC 19 Dexterity save, 35 (7d10) bludgeoning + pushed 6 m (half, no push); Leviathan then moves without provoking opportunity attacks to a point in that line (a creature in his ending space is harmlessly moved).
  - **Tidal Wave (Mythic Trait active only, 1/Day):** a 18 m wide, 6 m tall wave at a point within 36 m; it moves 30 m in a line, DC 19 Strength save, 20 (4d10) bludgeoning + 55 (10d10) acid + pushed to the wave's end (half, no push).
  - **Call Followers (1/Day):** summon a Wavespine and a Wavetooth Sahagin within 18 m (own initiative, Leviathan's allies).
- Legendary Actions (3): Scale Darts (one attack). Water Spout (2 Actions). Summon Wave Spume (2 Actions; within 18 m, own initiative).
- Mythic Actions (while Call of the Depths active): Briny Darts (ranged +10, range 9/18 m, 15 (2d10+5) piercing; on a hit DC 18 Constitution save or wounded — 11 (2d10) acid at end of each of its turns, re-save to end). Spiral Dive (3 Actions): move up to swim speed in a straight line (usable for walk/fly here), no opportunity attacks; creatures in the path make a DC 19 Dexterity save, 42 (12d6) bludgeoning + pushed to the end (half, no push). (Credit: Yamil.)
- Note: Wavespine/Wavetooth Sahagin statblocks are in the SPOKEN — Sahagin section (04_Bestiary).

### Wave Spume — Small elemental, unaligned
- AC 13 (natural) | HP 22 (4d6+8) | Speed 6 m fly (hover), 9 m swim | CR 1 (200 XP)
- STR 12(+1) DEX 8(-1) CON 14(+2) INT 4(-3) WIS 14(+2) CHA 4(-3)
- Damage Resistances nonmagical b/p/s | Damage Immunities acid | Condition Immunities prone | Senses darkvision 18 m, passive Perception 12 | Languages —
- Amphibious. Death Burst: on death, creatures within 3 m make a DC 12 Dexterity save, 10 (3d6) acid (half). Water Form: can enter a hostile creature's space and stop there; can move through a gap as narrow as 2.5 cm.
- Actions — Acid Bubble: ranged +4, range 9/18 m, 9 (2d6+2) acid; on a hit DC 12 Constitution save or take an additional 9 (2d6+2) acid at the end of its next turn. (Credit: Yamil.)

## Genus: Odin
A fell knight in dark steel atop his steed Sleipnir, roaming the Black Shroud seeking worthy battle. His essence is kept within his blade Zantetsuken; he draws aether directly from the land rather than crystal offerings.

### Odin, the Dark Divinity — Huge elemental, lawful evil
- AC 18 (natural) | HP 262 (25d12+100) | Speed 12 m | CR 15 (20,000 XP)
- STR 27(+8) DEX 21(+5) CON 19(+4) INT 17(+3) WIS 19(+4) CHA 16(+3)
- Saving Throws STR +14, DEX +11, CON +10 | Damage Vulnerabilities lightning | Damage Immunities nonmagical b/p/s | Condition Immunities charmed, exhaustion, petrified, paralyzed, stunned | Senses darkvision 18 m, passive Perception 14 | Languages Common
- To Those Who Are Worthy (Mythic Trait; Recharges after a Short or Long Rest). If reduced to 0 HP, resets to 262 HP and gains Mythic Actions for 1 hour. [OCR: source lists this trait twice — deduplicated here.] Legendary Resistance (3/Day). Tension: the sky darkens; a 90 m radius aura of nonmagical darkness that spreads around corners.
- Actions — Multiattack: three Zantetsuken attacks OR three Gungnir Lance attacks. Zantetsuken: melee +14, reach 1.5 m, 19 (2d10+8) slashing + 9 (2d8) force. Gungnir Lance: ranged +14, range 6/18 m, 21 (3d8+8) piercing.
- Bonus Actions — Hall of Lead (Recharge 5–6): up to 3 creatures in a 6 m radius sphere centered on Odin make a DC 18 Dexterity save or have speed 0 on their next turn. Hall of Sorrow (3/Day): one creature within 9 m makes a DC 18 Constitution save or has disadvantage on all attack rolls and saves until the end of its next turn. Hall of Fear: three creatures within 12 m make a DC 18 Wisdom save or are frightened 1 minute (re-save at end of turns; success/ending = immune 24 hours).
- Legendary Actions (3): Zantetsuken (2 Actions). Gungnir Lance (2 Actions). Stride (move up to speed without provoking opportunity attacks and through creatures; each creature passed takes 1d4 bludgeoning and is knocked prone).
- Mythic Actions (while Mythic Trait active): Shin-Zantetsuken (1/Day): each creature marked by Einherjar within 36 m makes a DC 20 Dexterity save, 85 (9d10+36) force (half). Einherjar (3 Actions): each creature within 36 m makes a DC 20 Dexterity save, 13 (1d10+8) force + marked 1 minute (half, no mark). (Credit: JPLDN.)

## Genus: Ramuh
God of the Sylphs, the personification of lightning that repelled invaders of the Twelveswood. Compassionate in folktale but a ruthless arbiter in truth.

### Ramuh, Lord of Levin — Huge elemental, Lawful Neutral
- AC 19 (natural) | HP 312 (25d12+150) | Speed 6 m, 12 m fly (hover) | CR 17 (11,000 XP)
- STR 18(+4) DEX 12(+1) CON 22(+6) INT 18(+4) WIS 20(+5) CHA 18(+4)
- Saving Throws Constitution +12, Wisdom +11 | Skills Insight +11, Perception +11 | Damage Resistance nonmagical b/p/s | Damage Immunities lightning | Condition Immunities charmed, exhaustion, frightened, poisoned | Senses truesight 9 m, passive Perception 21 | Languages Common, Sylvan
- Retrial (Mythic Trait; Recharges after a Short or Long Rest). At 0 HP he regains 312 HP and summons 6 grey arbiters within 18 m; one arbiter acts on initiative counts 20, 17, 14, 10, 5, 1. Legendary Resistance (3/Day).
- Actions — Multiattack: two attacks with Adjudicator's Gavel and/or Shock Strike in any combination.
  - **Adjudicator's Gavel:** melee +10, reach 3 m, 9 (1d10+4) bludgeoning + 33 (6d10) lightning.
  - **Shock Strike:** ranged spell +11, range 18 m, 14 (2d8+5) lightning; hit or miss the bolt explodes — the target and creatures within 3 m make a DC 19 Dexterity save, 16 (3d10) lightning (half).
  - **Chaotic Thunderstorm (Recharge 5–6):** a creature within 18 m makes a DC 19 Wisdom save or is charmed 1 minute (takes no actions and can't move). If still charmed at the start of Ramuh's next turn, he may (bonus action) drop it to 0 HP (it begins death saves).
  - **All other hostiles in a 36 m radius become lightning rods:** at the end of each such creature's next turn a 3 m radius bolt strikes — DC 19 Dexterity save, 21 (6d8) lightning (half); a charmed creature hit this way is no longer charmed.
  - **Indictment (1/Day):** summon 4 grey arbiters within 18 m (Small elemental, 50 HP, AC 15, immune to lightning; act on initiative 20/15/10/5; on their turn they only send a verdict to Ramuh).
- Reactions — Judgment Bolt: upon receiving 12 verdicts within the last hour, or when all grey arbiters are destroyed, all creatures in a 36 m tall, 36 m radius cylinder make a DC 19 Constitution save, #d12 lightning (# = verdicts received) (half); this treats lightning immunity as resistance. Ramuh then expends all received verdicts.
- Legendary Actions (3): Thunderstorm (ranged spell +11, range 18 m, 9 (1d8+5) lightning). Levin Bolt (2 Actions: use Shock Strike).
- Mythic Actions (1 hour after Retrial): Furious Thunderstorm (ranged spell +11, range 18 m, 21 (2d8+10) lightning). Crippling Blow (2 Actions): ranged spell +11, range 18 m, 14 (2d8+5) lightning; on a hit DC 19 Constitution save or paralyzed 1 minute (re-save at end of turns). (Credit: Soren of Asgard.)

## Genus: Shiva
Patron of the Ishgardian harriers. Unlike most primals, Shiva requires a mortal host with the will to use her power. (Section credited to Brulen.)

#### Deep Freeze (condition)
A creature with Deep Freeze: speed reduced to half its base speed (no speed bonuses apply); disadvantage on Dexterity checks and saves; resistance to fire damage; if it would make a death save, it may instead choose not to and remove Deep Freeze from itself. Lasts until ended.

#### Akh Afah Amphitheatre — Lair Actions (optional)
At the DM's discretion, when fought in the Akh Afah Amphitheatre Shiva gains Lair Actions. On initiative count 20 (losing ties), choose one (not the same two rounds in a row):
- Wall of ice on a surface within 36 m: up to 9 m long, 9 m high, 0.3 m thick; creatures in its area are pushed 1.5 m out (either side). Each 3 m section has AC 5, 30 HP, vulnerability to fire, immunity to acid/cold/necrotic/poison/psychic. The wall lasts until she uses this lair action again or dies.
- A blistering wind: each target within 36 m makes a DC 15 Constitution save or takes 5 (1d10) cold; disperses gases/vapors, extinguishes unprotected flames (50% chance for protected).
- Until the next round, Shiva can move through walls, doors, ceilings, and floors as if they weren't there.

### Shiva, Goddess of Ice — Huge elemental, Chaotic Good
- AC 18 | HP 253 (22d12+110) | Speed 12 m, fly 18 m | CR 17 (18,000 XP)
- STR 16(+3) DEX 24(+7) CON 20(+5) INT 18(+4) WIS 24(+7) CHA 30(+10)
- Saving Throws Dexterity +13, Wisdom +13, Charisma +16 | Skills Arcana +10, Deception +16, Persuasion +16, Survival +13 | Damage Vulnerabilities fire | Damage Resistances nonmagical b/p/s | Damage Immunities cold | Condition Immunities charmed, exhausted, petrified | Senses passive Perception 21 | Languages Common
- Diamond Dust (Mythic Trait; Recharges after a Short or Long Rest). At 0 HP she regains 253 HP, becomes resistant to fire, and moves up to 30 m without provoking opportunity attacks; all creatures within 90 m suffer Deep Freeze until the end of their next turn. Legendary Resistance (3/day). Magic Armoury: she creates/destroys her weapons at will (one at a time; must dismiss one before summoning another; her weapon attacks are magical). Flyby.
- Actions — Multiattack: two Silver Filigree and one armoury-weapon attack (if wielding one). Silver Filigree: melee +13, reach 1.5 m, 17 (3d6+7) piercing + 11 (2d10) cold. Icebrand (Blade only): melee +16, reach 1.5 m, 26 (3d10+10) slashing + 11 (2d10) cold. Hailstorm (Staff only): point within 45 m, 6 m radius sphere, DC 19 Dexterity save, 7 (2d6) piercing + 14 (4d6) cold (half). Glass Dance (Bow only): ranged +16, range 12/24 m, 23 (3d8+10) piercing + 11 (2d10) cold; the target suffers Deep Freeze until the end of its next turn.
- Bonus Actions — Summon Blade (sword and shield; +2 AC while wielded). Summon Staff (advantage on saves vs spell effects while wielded). Summon Bow. Dismiss Weapon.
- Legendary Actions (3): Fly (move up to fly speed without provoking opportunity attacks). Quick Dismiss (shatter current weapon). Absolute Zero (2 Actions: inflict Deep Freeze on all creatures within 3 m until the end of their next turn).
- Mythic Actions (1 hour after Diamond Dust): Dreams of Ice (coat the ground within 6 m in ice; DMG 2014 p.110 ice rules). Shatter (2 Actions): a creature within 1.5 m suffering Deep Freeze — the condition ends immediately and it makes a DC 19 Constitution save, 27 (6d8) cold (half). (Credit: Brulen.)

## Genus: Titan
The will of the earth, born of his kobold followers' prayers. Shockingly kind — but once provoked, an unstoppable father's fury.

### Titan, Lord of Crags — Huge elemental, Neutral Good
- AC 18 (natural) | HP 294 (19d12+171) | Speed 7.5 m | CR 15 (13,000 XP)
- STR 20(+5) DEX 8(-1) CON 28(+9) INT 16(+3) WIS 16(+3) CHA 24(+7)
- Saving Throws Strength +10, Constitution +14, Wisdom +8, Charisma +12 | Skills Perception +8 | Condition Immunities charmed, exhaustion | Senses tremorsense 9 m, passive Perception 16 | Languages Common, Terran
- Crushing Steps (movement unaffected by difficult terrain; advantage on STR/DEX saves vs prone). Gemstone Heart (Mythic Trait; Recharges after a Short or Long Rest): at 0 HP he regains 294 HP and gains resistance to slashing, piercing, or bludgeoning damage. Legendary Resistance (3/Day). Magic Weapons. Siege Monster (double damage to objects and structures).
- Actions — Multiattack: up to three Fist attacks, or select two targets for Weight of the Land. Fist: melee +9, reach 3 m, 13 (2d8+5) bludgeoning. Bomb Rock Toss: ranged +9, range 18 m, 13 (2d8+5) bludgeoning + 32 (8d8) fire. Weight of the Land: a creature within 12 m makes a DC 18 Dexterity save, 15 (3d10) bludgeoning (half). Landslide (Recharge 6): a 18 m long, 3 m wide line, DC 18 Dexterity save, 40 (8d10) bludgeoning + pushed 12 m (half, no push); a creature pushed into an object/creature deals 1d6 bludgeoning per 1.5 m travelled to both.
- Bonus Action — Tumult: creatures on the ground within 6 m make a DC 18 Dexterity check (save) or take 10 (2d10) bludgeoning and prone (half, no prone).
- Reaction — Mountain Buster: when struck by a melee weapon attack, a 4.5 m cone toward the attacker, DC 18 Dexterity save, 15 (3d10) bludgeoning; the area becomes difficult terrain.
- Legendary Actions (3): Fist (one attack). Tumult (2 Actions). Mountain Buster (2 Actions; vs a creature within 1.5 m).
- Mythic Actions (1 hour after Gemstone Heart): Earthen Fist (one Fist + 8 (2d8) bonus bludgeoning). Granite Gaol (2 Actions): a creature within 9 m makes a DC 18 Strength save or is sealed in stone (restrained, blinded, full cover); the Gaol has 50 HP and AC 13. Fault Line (3 Actions): recharge Landslide and use it. (Credit: Soren of Asgard.)

# CLASS: SCALEKIN
Marked by tough scaly hides that armor them against predators. Highly adaptable, but a sudden change in climate harms them greatly.

## Genus: Adamantoise
Native to Thavnair; spread to Eorzea by an egg-shipment mix-up, joining the Twelveswood ecosystem.

### Adamantoise — Large dragon, neutral
- AC 18 (natural) | HP 102 (12d10+36) | Speed 6 m walk, 9 m swim | CR 4 (1,100 XP)
- STR 17(+3) DEX 10(+0) CON 16(+3) INT 7(-2) WIS 10(+0) CHA 10(+0)
- Damage Vulnerabilities cold | Senses darkvision 36 m, passive Perception 10 | Languages —
- Amphibious.
- Actions — Multiattack: 2 Bites. Bite: +5, reach 3 m, 9 (1d12+3) piercing. Withdraw: tucks its head into its shell; while Withdrawn it gains +5 AC and advantage on STR/CON saves, but its speed is 0 (can't increase), it has disadvantage on DEX saves, and its only actions are a bonus action to emerge and a reaction to Snap.
- Reactions — Snap: when it takes damage while Withdrawn, it can emerge and make a Bite against a nearby creature with +5 to the attack and +5 piercing damage. (Credit: JPLDN.)

## Genus: Peiste
Large scalekin with serpentine neck/tail; flatten prey and use Cold Gaze to paralyze. Depicted as incarnations of evil in the arid regions they inhabit.

### Peiste — Large beast, unaligned
- AC 13 (natural) | HP 68 (8d10+24) | Speed 9 m | CR 3 (700 XP)
- STR 15(+2) DEX 11(+0) CON 16(+3) INT 6(-3) WIS 12(+1) CHA 7(-3) | Senses darkvision 18 m, passive Perception 11 | Languages —
- Actions — Multiattack: 2 Bites. Bite: +4, reach 1.5 m, 11 (2d8+2) bludgeoning. Body Slam: 3 m radius around it, DC 13 Strength save, 13 (3d8) bludgeoning (half). Cold Gaze (Recharge 5–6): 4.5 m cone, DC 13 Wisdom save, 11 (2d10) necrotic + paralyzed 1 minute (half, no paralyze; re-save at end of turns). (Credit: Soren of Asgard.)

## Genus: Puk
Small insect-eaters that ambush from the trees; temperamental, territorial, and fearless.

### Puk — Small beast, unaligned
- AC 13 | HP 22 (4d6+8) | Speed 9 m, 3 m fly | CR 1/2 (100 XP)
- STR 13(+1) DEX 16(+3) CON 14(+2) INT 5(-4) WIS 12(+1) CHA 6(-3)
- Saving Throws Dexterity +5 | Skills Acrobatics +5 | Senses passive Perception 11 | Languages —
- Ambusher. Advantage on attack rolls in round 1 against any creature it surprised.
- Actions — Backflip: +3, reach 1.5 m, 4 (1d6+1) bludgeoning; then Disengage as a bonus action. Bite: +3, reach 1.5 m, 5 (1d8+1) piercing. Fire Spit (Recharge 5–6): point within 9 m, 3 m radius sphere, DC 12 Dexterity save, 7 (2d6) fire (half). (Credit: Soren of Asgard.)

## Genus: Raptor
Named for speedy pursuit (no avian relation); claw, fang, and fiery breath. Often hunt in pairs.

### Raptor — Medium beast, unaligned
- AC 12 | HP 52 (8d8+16) | Speed 12 m | CR 2 (450 XP)
- STR 17(+3) DEX 15(+2) CON 14(+2) INT 4(-3) WIS 12(+1) CHA 8(-1)
- Skills Perception +3, Stealth +6 | Senses darkvision 18 m, passive Perception 13 | Languages —
- Keen Smell. Pounce: move 6 m straight + claw hit = DC 13 Strength save or prone; if prone, bonus-action bite.
- Actions — Bite: +5, reach 1.5 m, 8 (1d10+3) piercing. Claw: +5, reach 1.5 m, 7 (1d8+3) slashing. Flame Breath (Recharge 5–6): 4.5 m cone, DC 13 Dexterity save, 10 (3d6) fire (half).
- Regional Adaptivity: the breath may instead be Ice Breath (cold) or Lightning Breath (lightning). (Credit: Jotunn-Bane.)

## Genus: Ziz
Solitary hunters thought related to raptors; muscular legs and a wedge-shaped beak, plus noxious poisons.

### Ziz — Large beast, unaligned
- AC 13 (natural) | HP 51 (6d10+18) | Speed 12 m | CR 2 (450 XP)
- STR 16(+3) DEX 10(+0) CON 16(+3) INT 5(-3) WIS 10(+0) CHA 4(-3) | Senses passive Perception 10 | Languages —
- Charge. Move 6 m straight + Hammer Beak hit = +6 (1d12) bludgeoning and DC 13 Strength save or prone.
- Actions — Hammer Beak: +5, reach 1.5 m, 16 (2d12+3) bludgeoning. Noxious Breath (Recharge 5–6): 4.5 m cone, DC 13 Constitution save, 10 (3d6) poison + poisoned 1 minute (half, no poison; re-save at end of turns). (Credit: Soren of Asgard.)

# CLASS: SEEDKIN
Mobile plant-animal hybrids that hunt, defend, or reproduce (via seeds/spores and a host). Far deadlier than common plants.

## Genus: Cactuar
Arid-climate seedkin storing water; they fire needle barrages from a hardened carapace. Sabotenders (a sub-group) have a needle tuft and are stronger/more aggressive.

### Cactuar — Medium Plant, neutral
- AC 13 (natural) | HP 26 (4d8+8) | Speed 6 m | CR 1/2 (100 XP)
- STR 15(+2) DEX 12(+1) CON 14(+2) INT 5(-3) WIS 10(+0) CHA 3(-4)
- Skills Stealth +3 | Damage Resistances fire | Senses — | Languages —
- False Appearance (indistinguishable from a cactus while motionless). Needly Body: at the start of its turn, deals 2 (1d4) piercing to any creature grappling it.
- Actions — Scratch: +4, reach 1.5 m, 5 (1d6+2) piercing. Single Needle: ranged +3, reach 9 m, 8 (2d6+1) piercing. 100 Needles (Recharge 6): all creatures within 3 m not behind full cover take exactly 7 piercing (regardless of vulnerabilities/resistances/immunities). (Credit: Brulen.)

### Sabotender — Medium Plant, neutral
- AC 14 (natural) | HP 37 (5d8+15) | Speed 6 m | CR 1 (200 XP)
- STR 15(+2) DEX 15(+2) CON 16(+3) INT 5(-3) WIS 10(+0) CHA 3(-4)
- Skills Stealth +4 | Damage Resistances fire | Languages —
- False Appearance. Needly Body: 3 (1d6) to a grappler at the start of its turn.
- Actions — Multiattack: a Scratch or Single Needle, plus a 100 Needles if available. Scratch: +4, reach 1.5 m, 5 (1d6+2) piercing. Single Needle: ranged +4, reach 9 m, 9 (2d6+2) piercing. 100 Needles (Recharge 6): all within 3 m not behind full cover take exactly 7 piercing. (Credit: Brulen.)
- Variant — Senor Sabotender: actually a Lalafell in a sabotender suit (Manderville Gold Saucer mascot). Raise CHA to 18 and replace 100 Needles with Gentlemanly Pose: any humanoid within 90 m that can see him must succeed on a DC 11 Wisdom save or be charmed while he poses (he must use a bonus action each turn to maintain it). A charmed target is incapacitated, must move toward him by the most direct route if more than 1.5 m away, re-saves when it takes damage or at the end of its turns; success = immune 24 hours.

### Nopalitender — Large Plant, neutral
- AC 15 (natural) | HP 45 (6d10+18) | Speed 9 m | CR 3 (700 XP)
- STR 12(+1) DEX 18(+4) CON 16(+3) INT 11(+0) WIS 10(+0) CHA 3(-4)
- Skills Stealth +6 | Damage Resistances fire | Languages —
- False Appearance. Needly Body: 4 (1d8) to a grappler. Multiple Heads (3 heads; advantage on saves vs blinded, charmed, deafened, frightened, stunned, unconscious). Wakeful (at least one head is awake while it sleeps).
- Actions — Multiattack: 2 Single Needle. Scratch: +3, reach 1.5 m, 4 (1d6+1) piercing. Single Needle: ranged +6, reach 9 m, 11 (2d6+4) piercing. 1000 Needles (Recharge 6): all within 6 m not behind full cover take exactly 16 piercing. (Credit: Brulen.)

### Gigantender — Large Plant, neutral
- AC 16 (natural) | HP 68 (8d10+24) | Speed 6 m | CR 4 (1,100 XP)
- STR 18(+4) DEX 10(+0) CON 16(+3) INT 5(-3) WIS 10(+0) CHA 3(-4)
- Skills Stealth +2 | Damage Resistances b/p/s from nonmagical attacks | Damage Immunities fire | Languages —
- False Appearance. Needly Body: 4 (1d8) to a grappler. Sure-Footed (advantage on STR/DEX saves vs prone).
- Actions — Multiattack: 2 Scratch. Scratch: +6, reach 1.5 m, 7 (1d6+4) piercing. Single Needle: ranged +2, reach 9 m, 7 (2d6) piercing. 1000 Needles (Recharge 6): all within 6 m not behind full cover take exactly 16 piercing. (Credit: Brulen.)

### Sabotender Emperatriz — Medium Plant, neutral
- AC 15 (natural) | HP 82 (11d8+33) | Speed 12 m | CR 8 (3,900 XP)
- STR 12(+1) DEX 14(+2) CON 16(+3) INT 10(+0) WIS 10(+0) CHA 16(+3)
- Skills Stealth +5 | Damage Resistances b/p/s from nonmagical attacks | Damage Immunities fire | Languages —
- False Appearance. Needly Body: 4 (1d8) to a grappler. Regal Presence: other plant-type creatures within 30 m gain advantage on all saves and +1 AC.
- Actions — Multiattack: 3 attacks with Royal Rod or Single Needle. Royal Rod: +6, reach 1.5 m, 12 (2d8+3) piercing + 7 (2d6) poison. Single Needle: ranged +5, reach 9 m, 11 (2d8+2) piercing. Royal Guard (recharges on a short or long rest): regains HP = 5 × the number of plant-type creatures within 30 m. 10,000 Needles (Recharge 6): all within 15 m not behind full cover take exactly 25 piercing. (Credit: Brulen.)

### Lunatender — Large Celestial, neutral
- AC 17 (natural) | HP 110 (13d10+39) | Speed 9 m, fly 18 m | CR 10 (5,900 XP)
- STR 14(+2) DEX 14(+2) CON 16(+3) INT 18(+4) WIS 10(+0) CHA 12(+1)
- Skills Stealth +6 | Damage Resistances b/p/s from nonmagical attacks | Damage Immunities radiant, necrotic | Senses blindsight 9 m | Languages —
- False Appearance. Radiant Body: 4 (1d8) radiant to a grappler. Slender Dodge: when it takes damage it may move up to 3 m without provoking opportunity attacks (if not grappled/restrained). Propagation: on death it explodes — creatures within 6 m make a DC 14 Dexterity save, 14 (4d6) radiant (half); 24 hours later two new Lunatenders grow where it died unless the ground is hallowed, desecrated, or burned.
- Actions — Multiattack: 3 Single Ray. Single Ray: ranged +8, reach 18 m, 19 (2d8+10) radiant. 10,000 Rays (Recharge 6): all within 15 m not behind full cover take exactly 25 radiant. (Credit: Brulen.)

## Genus: Funguar
Camouflaging fungal seedkin of damp forests/caverns; a delicacy among Eorzean gourmands.

### Funguar — Small plant, unaligned
- AC 11 | HP 11 (2d6+4) | Speed 9 m | CR 1/8 (25 XP)
- STR 12(+1) DEX 12(+1) CON 14(+2) INT 4(-3) WIS 8(-1) CHA 3(-4)
- Skills Stealth +3 | Damage Vulnerabilities fire | Senses passive Perception 9 | Languages —
- False Appearance (mushroom). Queasy Cloud: when hit by a melee weapon attack, a 1.5 m radius cloud — creatures within make a DC 12 Constitution save or are poisoned 1 minute (re-save at end of turns, not on the turn they attacked it).
- Actions — Cap Bump: +3, reach 1.5 m, 4 (1d6+1) bludgeoning. (Credit: Soren of Asgard.)

## Genus: Mandragora
Sentient seedkin first seen after the Seventh Umbral Calamity; communicate among themselves and form social hierarchies.

### Mandragora — Small plant, unaligned
- AC 13 (natural) | HP 4 (1d6+1) | Speed 9 m | CR 1/8 (25 XP)
- STR 6(-2) DEX 13(+1) CON 12(+1) INT 4(-3) WIS 8(-1) CHA 3(-4)
- Skills Stealth +3 | Damage Vulnerabilities fire | Condition Immunities blinded, deafened | Senses passive Perception 9 | Languages —
- False Appearance (a common vegetable while motionless and partially burrowed).
- Actions — Headbutt: +3, reach 1.5 m, 3 (1d4+1) bludgeoning. Shriek (1/Day): each non-mandragora within 4.5 m makes a DC 11 Wisdom save or is stunned until the end of the Mandragora's next turn (a creature with pre-muffled hearing auto-succeeds).
- Reaction — Unexpected Wallop: if pulled from the ground and the creature is surprised, make one Headbutt with advantage dealing +1d6 damage. (Credit: Jotunn-Bane.)

## Genus: Morbol
Vine-and-root beasts; aggressive, indiscriminate hunters with noxious Bad Breath and large tendrils. A Malboro is a giant, extra-deadly morbol.

### Malboro — Huge Plant, unaligned
- AC 17 (natural) | HP 200 (10d12+80) | Speed 6 m, burrow 3 m, swim 3 m | CR 10 [OCR: source lists "100 XP" — clearly wrong; CR 10 = 5,900 XP]
- STR 20(+5) DEX 6(-2) CON 26(+8) INT 5(-3) WIS 16(+3) CHA 10(+0) | Senses passive Perception 15, blindsight 18 m (blind beyond) | Languages —
- [OCR: HP "200 (10d12+80)" — 10d12+80 averages ~145; 200 is the max. Reproduced verbatim.]
- Putrid Stench: detectable within 36 m; a creature coming within 3 m makes a DC 16 Constitution save or is blinded 1d4 rounds (success = immune for 1 minute). Rampaging Charge: when it Dashes, bonus-action Bite dealing +2d8 damage on a hit.
- Actions — Multiattack: 2 Tentacles and one Bite, or 3 Bile Spew. Tentacle: +9, reach 4.5 m, 15 (2d8+5) bludgeoning. Bite: +9, reach 3 m, 33 (4d12+5) piercing. Bile Spew: ranged +9, reach 18 m, 17 (2d10+5) acid. Bad Breath (Recharge 5–6): 18 m cone, DC 16 Constitution save, [OCR: damage dice missing in source — "#d# poison"; GM must assign] poison and paralyzed on a fail. (Credit: Soren of Asgard.)

## Genus: Ochu
Carnivorous seedkin that lure insects with scents, then lash and drag them in; use poison gas against predators.

### Ochu — Medium plant, unaligned
- AC 12 (natural) | HP 45 (6d8+18) | Speed 7.5 m | CR 1 (200 XP)
- STR [OCR: score missing in source, only "(+2)"] DEX 10(+0) CON 16(+3) INT 3(-4) WIS 10(+0) CHA 5(-3)
- Damage Vulnerabilities fire | Damage Resistances acid, poison | Condition Immunities poisoned | Senses passive Perception 10 | Languages —
- Actions — Lash: +3, reach 3 m, 5 (1d6+2) slashing. Acid Mist (Recharge 5–6): 3 m radius around it, DC 13 Constitution save, 7 (2d6) poison + poisoned 1 minute (half, no poison).
- Bonus Action — Hundred Lashes: use its Lash attack.
- Reaction — Panic Mist: when attacked by a melee weapon attack, use Acid Mist if available. (Credit: Soren of Asgard.)

## Genus: Treant
Ambulatory seedkin of the Black Shroud, guardians of the forest; confront any perceived threat.

### Treant — Huge Plant, unaligned
- AC 16 (natural) | HP 115 (11d12+44) | Speed 6 m | CR 4 (1,100 XP)
- STR 16(+3) DEX 8(-1) CON 18(+4) INT 5(-3) WIS 16(+3) CHA 10(+0)
- Damage Vulnerabilities fire | Damage Resistances thunder | Senses passive Perception 13 | Languages —
- Actions — Multiattack: 2 Slams. Slam: +5, reach 3 m, 14 (2d10+3) bludgeoning. Canopy: 6 m cone, DC 13 Strength save, 16 (3d10) bludgeoning (half). Acorn Bomb (Recharge 3–4): point within 9 m, 3 m radius circle, DC 13 Constitution save or fall asleep 10 minutes (until damaged or shaken awake). Arboreal Storm (Recharge 5–6): 4.5 m radius, 6 m tall cylinder, DC 13 Strength save, 11 (2d10) bludgeoning + 7 (2d6) thunder + prone (half, no prone). (Credit: Soren of Asgard.)

# CLASS: SOULKIN
Inorganic beings gifted life by aether pooling in a suitable medium — sometimes via magic, sometimes naturally — gaining movement, thought, and occasionally speech.

## Genus: Coblyn
Fleshy ore-eating creatures that skitter on tentacle limbs; the ore they consume builds their shell (colour indicates ore type: Doblyn, Soblyn, Zoblyn, etc.).

### Coblyn — Medium aberration, unaligned
- AC 13 (natural) | HP 24 (1d8+20) | Speed 6 m, burrow 6 m, climb 6 m | CR 1/2 (100 XP) [OCR: HP formula "1d8+20" reproduced verbatim]
- STR 8(-1) DEX 17(+3) CON 14(+2) INT 5(-3) WIS 13(+1) CHA 8(-1)
- Damage Immunities poison | Condition Immunities paralyzed, petrified, poisoned, unconscious | Senses darkvision 18 m, tremorsense 18 m, passive Perception 11 | Languages —
- Earth Glide (burrows through nonmagical unworked earth/stone without disturbing it). Stone Camouflage (advantage on Stealth in rocky terrain). Stone Climb (climbs difficult stone, incl. ceilings, no check).
- Actions — Bite: +5, reach 1.5 m, 6 (1d6+3) piercing. Shatter (1/Day): creatures within 3 m make a DC 12 Dexterity save, 5 (2d4) force (none on success). (Credit: Jotunn-Bane.)

## Genus: Dullahan
Ancient golems (or ashkin-like armor possessed by old souls) that stalk fallen forts and castles; never present without a reason.

### Dullahan — Large construct, unaligned
- AC 16 (Plate) | HP 153 (18d10+54) | Speed 9 m | CR 7 (2,900 XP)
- STR 20(+5) DEX 14(+2) CON 16(+3) INT 1(-5) WIS 10(+0) CHA 1(-5)
- Saving Throws STR +11, DEX +5 [OCR: source lists STR +11] | Skills Athletics +8, Perception +3 | Damage Resistances nonmagical b/p/s | Condition Immunities charmed, frightened, paralyzed, petrified, poisoned | Senses blindsight 18 m (blind beyond 18 m), passive Perception 13 | Languages understands Common but can't speak
- Brute (one extra damage die on its weapon attacks, included).
- Actions — Multiattack: 2 Greatswords. Greatsword: +8, reach 3 m, 15 (3d6+5) slashing. Iron Justice (Recharge 5–6): 4.5 m cone, DC 15 Dexterity save, 15 (3d6+5) slashing (half). Black Nebula (1/Day): a 6 m radius void puddle within 18 m for 1 minute (difficult terrain); a creature starting its turn there or entering it the first time on a turn makes a DC 13 Constitution save, 18 (4d8) necrotic (half).
- Bonus Action — King's Will (1/Day): until the end of its turn it makes one additional melee attack, each attack deals +3d6 damage, and all that damage becomes force. (Credit: Jotunn-Bane.)

## Genus: Spriggan
Sprite/faerie-like beings of rocky regions and mines; the ore/gem they carry is their power source. Seen by miners as a sign of good fortune and valuable ore.

### Spriggan — Small aberration, Chaotic Neutral
- AC 13 | HP 16 (3d6+6) | Speed 6 m | CR 1/8 (50 XP)
- STR 14(+2) DEX 11(+1) CON 14(+2) INT 4(-3) WIS 10(+0) CHA 8(-1) [OCR: source lists DEX 11 as (+1)]
- Skills Athletics +4 | Damage Vulnerabilities necrotic | Damage Resistances bludgeoning | Senses darkvision 9 m | Languages —
- Actions — Ore Bash: +4, reach 1.5 m, 4 (1d4+2) bludgeoning. (Credit: Brulen.)

### Dull Stone Spriggan — Small fae, Chaotic Neutral
- AC 13 | HP 22 (4d6+8) | Speed 7.5 m | CR 1/4 (100 XP)
- STR 14(+2) DEX 16(+3) CON 14(+2) INT 8(-1) WIS 16(+3) CHA 10(+0)
- Skills Perception +5 | Damage Resistances b/p/s from nonmagical weapons | Senses darkvision 18 m | Languages Common, Terran
- Actions — Headbutt: +4, reach 1.5 m, 4 (1d4+2) bludgeoning. Romp: 4.5 m cone, DC 12 Dexterity save, 3 (1d6) bludgeoning. Jittering Jig: draws energy from its stone for 1 minute — gains 6 (1d4+3) temp HP and +3 bonus damage on Headbutt (which counts as magical); then may Disengage or Dash as a bonus action. (Credit: Soren of Asgard.)

# CLASS: SPOKEN
Intelligent creatures with an independent language interpretable across genera. From the Au Ra to the Kobolds — if a creature communicates meaningfully across species, it is Spoken.
[OCR NOTE: several Spoken entries list CR 2 with "(200 XP)"; CR 2 = 450 XP. XP values are reproduced verbatim as printed in the source.]

## Genus: Amalj'aa
Lizard-like people of northern Thanalan who worship Ifrit; nomadic, honorable warriors and skilled smiths.

### Amalj'aa Striker — Medium humanoid (amalj'aa), Lawful Neutral
- AC 13 (natural) | HP 25 (3d8+12) | Speed 9 m | CR 1 (200 XP)
- STR 14(+2) DEX 12(+1) CON 18(+4) INT 10(+0) WIS 12(+1) CHA 10(+0) | Senses passive Perception 12 | Languages Common
- Actions — Multiattack: 2 Knuckle. Knuckle: +4, reach 1.5 m, 4 (1d4+2) bludgeoning. Devastate (Recharge 5–6): a 3 m long, 1.5 m wide line, DC 12 Dexterity save or 5 (1d10) bludgeoning and knocked prone (Enfire bonus damage applies).
- Bonus Action — Enfire (1/Day): weapons deal +2 (1d4) fire on a hit for 1 minute. (Credit: Soren of Asgard.)

### Amalj'aa Impaler — Medium humanoid (amalj'aa), Lawful Neutral
- AC 13 (natural) | HP 34 (4d8+16) | Speed 9 m | CR 1 (200 XP)
- STR 14(+2) DEX 12(+1) CON 18(+4) INT 10(+0) WIS 12(+1) CHA 10(+0) | Senses passive Perception 12 | Languages Common
- Actions — Glaive: +4, reach 3 m, 8 (1d12+2) slashing. Devastate (Recharge 5–6): a 3 m long, 1.5 m wide line, DC 12 Dexterity save or 5 (1d10) bludgeoning and prone (Enfire applies).
- Bonus Action — Enfire (1/Day): +2 (1d4) fire for 1 minute. (Credit: Soren of Asgard.)

### Amalj'aa Archer — Medium humanoid (amalj'aa), Lawful Neutral
- AC 15 (natural) | HP 25 (3d8+12) | Speed 9 m | CR 1 (200 XP)
- STR 12(+1) DEX 14(+2) CON 18(+4) INT 10(+0) WIS 14(+2) CHA 10(+0) | Senses passive Perception 12 | Languages Common
- Actions — Multiattack: 2 attacks (Shortsword/Shortbow). Shortsword: +4, reach 3 m [OCR: source lists 10 ft reach for a shortsword], 5 (1d6+2) piercing. Shortbow: ranged +4, range 24/96 m, 5 (1d6+2) piercing. Devastate (Recharge 5–6): a 3 m long, 1.5 m wide line, DC 11 Dexterity save or 5 (1d10) bludgeoning and prone.
- Bonus Action — Enfire (1/Day): +2 (1d4) fire for 1 minute. (Credit: Soren of Asgard.)

### Amalj'aa Initiate — Medium humanoid (amalj'aa), Lawful Neutral
- AC 13 (natural) | HP 25 (3d8+12) | Speed 9 m | CR 2 (200 XP)
- STR 12(+1) DEX 12(+1) CON 18(+4) INT 10(+0) WIS 14(+2) CHA 16(+3) | Senses passive Perception 12 | Languages Common
- Innate Spellcasting (CHA, DC 13, +5): 3/day Burning Hands.
- Actions — Stave: +3, reach 3 m, 3 (1d4+1) bludgeoning. Amalj'aa Fire: ranged spell +5, range 18 m, 16 (2d12+3) fire. Devastate (Recharge 5–6): a 3 m long, 1.5 m wide line, DC 11 Dexterity save or 5 (1d10) bludgeoning and prone.
- Bonus Actions — Blaze Spikes (1/Day): for 1 minute, a creature that hits it with a weapon attack takes 2 (1d4) fire. Enfire (1/Day): weapons deal +9 (2d8) fire for 1 minute. (Credit: Soren of Asgard.)

## Genus: Ixal
Bird-like humanoids of Xelphatol, north of the Black Shroud; they raid the Twelveswood and seek their promised land where Garuda dwells.

### Ixali Swordfighter — Medium humanoid (ixal), Chaotic Neutral
- AC 16 (natural armor, shield) | HP 22 (3d8+9) | Speed 9 m | CR 1 (200 XP)
- STR 12(+1) DEX 14(+2) CON 16(+3) INT 10(+0) WIS 12(+1) CHA 10(+0) | Senses passive Perception 11 | Languages Common
- Brute (one extra damage die, included). Swift Gust (1/Day): when it Dodges, +3 AC.
- Actions — Scimitar: +4, reach 1.5 m, 9 (2d6+2) slashing.
- Bonus Actions — Barbaric Surge (1/Day): its next hit deals +3 damage. Coming Storm (1/Day): make a Scimitar attack as a bonus action. Enaero (1/Day): +2 (1d4) thunder for 1 minute. (Credit: Soren of Asgard.)

### Ixali Swiftbeak — Medium humanoid (ixal), Chaotic Neutral
- AC 13 (natural) | HP 45 (6d8+18) | Speed 9 m | CR 2 (200 XP)
- STR 14(+2) DEX 12(+1) CON 16(+3) INT 10(+0) WIS 12(+1) CHA 10(+0) | Senses passive Perception 11 | Languages Common
- Brute. Swift Gust (1/Day): when it Dodges, +3 AC.
- Actions — Battleaxe: +4, reach 1.5 m, 13 (2d10+2) slashing.
- Bonus Actions — Barbaric Surge (1/Day): next hit +3 damage. Coming Storm (1/Day): make a battleaxe attack as a bonus action [OCR: source says "greataxe"]. Enaero (1/Day): +2 (1d4) thunder for 1 minute. (Credit: Soren of Asgard.)

### Ixali Straightbeak — Medium humanoid (ixal), Chaotic Neutral
- AC 13 (natural) | HP 30 (4d8+12) | Speed 9 m | CR 1 (200 XP)
- STR 14(+2) DEX 12(+1) CON 16(+3) INT 10(+0) WIS 12(+1) CHA 10(+0) | Senses passive Perception 11 | Languages Common
- Brute. Swift Gust (1/Day): when it Dodges, +3 AC.
- Actions — Spear: +4, reach 1.5 m, 11 (2d8+2) piercing.
- Bonus Actions — Barbaric Surge (1/Day): next hit +3 damage. Coming Storm (1/Day): make a spear attack as a bonus action. Enaero (1/Day): +2 (1d4) thunder for 1 minute. (Credit: Soren of Asgard.)

### Ixali Caller — Medium humanoid (ixal), Chaotic Neutral
- AC 13 (natural) | HP 30 (4d8+12) | Speed 9 m | CR 2 (200 XP)
- STR 14(+2) DEX 12(+1) CON 16(+3) INT 10(+0) WIS 16(+3) CHA 10(+0) | Senses passive Perception 13 | Languages Common
- Swift Gust (1/Day): when it Dodges, +3 AC. Innate Spellcasting (WIS, DC 13, +5): 3/day Thunderwave.
- Actions — Staff: +3, reach 1.5 m, 3 (1d4+1) bludgeoning. Ixali Aero: ranged spell +5, range 18 m, 16 (2d12+3) thunder.
- Bonus Action — Enaero (1/Day): weapons deal +9 (2d8) thunder for 1 minute. (Credit: Soren of Asgard.)

## Genus: Kobold
Industrious, pious miners of the O'Ghomoro mountains who worship Titan; organized into strict "digs."

### Kobold Potman — Medium humanoid (kobold), Lawful Neutral
- AC 14 (ring mail) | HP 30 (4d8+12) | Speed 9 m | CR 1 (200 XP)
- STR 14(+2) DEX 12(+1) CON 16(+3) INT 12(+1) WIS 12(+1) CHA 10(+0) | Senses passive Perception 11 | Languages Common
- Actions — Multiattack: 2 Shortswords. Shortsword: +4, reach 1.5 m, 5 (1d6+2) piercing.
- Bonus Actions — Barbaric Surge (1/Day): next hit +3 damage. Fast Blade (Recharge 5–6): make a Shortsword attack. Titan's Boon (1/Day): until the end of its next turn, damage it takes is reduced by 3. (Credit: Soren of Asgard.)

### Kobold Dustman — Medium humanoid (kobold), Lawful Neutral
- AC 14 (ring mail) | HP 30 (4d8+12) | Speed 9 m | CR 1 (200 XP)
- STR 14(+2) DEX 12(+1) CON 16(+3) INT 12(+1) WIS 12(+1) CHA 10(+0) | Senses passive Perception 11 | Languages Common
- Actions — Multiattack: 2 Battleaxes. Battleaxe: +4, reach 1.5 m, 7 (1d10+2) slashing. Overpower (Recharge 5–6): 4.5 m cone, DC 12 Dexterity save, 7 (1d10+2) force (half).
- Bonus Actions — Barbaric Surge (1/Day): next hit +3 damage. Enstone (1/Day): weapons deal +2 (1d4) bludgeoning for 1 minute [OCR: source says "water aether" but the damage is bludgeoning]. Titan's Boon (1/Day): reduce incoming damage by 3 until the end of its next turn. (Credit: Soren of Asgard.)

### Kobold Supplicant — Medium humanoid (kobold), Lawful Neutral
- AC 14 (ring mail) | HP 30 (4d8+12) | Speed 9 m | CR 2 (200 XP)
- STR 14(+2) DEX 12(+1) CON 16(+3) INT 16(+3) WIS 16(+3) CHA 16(+3) | Senses passive Perception 13 | Languages Common
- Innate Spellcasting (CHA, DC 13, +5): At will Magic Stone; 3/day Earth Tremor.
- Actions — Wand: +4, reach 1.5 m, 4 (1d4+2) bludgeoning. Kobold Stone: ranged spell +5, range 9 m, 19 (3d10+3) bludgeoning. Titan's Anger (Recharge 5–6): point within 9 m, 3 m radius sphere, DC 13 Dexterity save, 10 (3d6) force (half).
- Bonus Action — Titan's Boon (1/Day): reduce incoming damage by 3 until the end of its next turn. (Credit: Soren of Asgard.)

### Kobold Sidesman — Medium humanoid (kobold), Lawful Neutral
- AC 14 (ring mail) | HP 30 (4d8+12) | Speed 9 m | CR 1 (200 XP)
- STR 14(+2) DEX 12(+1) CON 16(+3) INT 16(+3) WIS 16(+3) CHA 16(+3) | Senses passive Perception 13 | Languages Common
- Innate Spellcasting (CHA, DC 13, +5): At will Shillelagh; 3/day Healing Word.
- Actions — Wand: +4, reach 1.5 m, 4 (1d4+2) bludgeoning. Kobold Stone: ranged spell +5, range 9 m, 14 (2d10+3) bludgeoning. Titan's Anger (Recharge 5–6): point within 9 m, 3 m radius sphere, DC 13 Dexterity save, 7 (2d6) force (half).
- Bonus Action — Titan's Boon (1/Day): reduce incoming damage by 3 until the end of its next turn. (Credit: Soren of Asgard.)

## Genus: Moogle
Elusive, fluffy winged creatures with mood-colored poms; friendly to those they trust, wary of strangers.

### Twelveswood Moogle — Small fae (moogle), Chaotic Good
- AC 14 | HP 33 (6d6+12) | Speed 3 m, 9 m fly (hover) | CR 1 (200 XP)
- STR 8(-1) DEX 18(+4) CON 14(+2) INT 10(+0) WIS 16(+3) CHA 16(+3)
- Skills Stealth +6 | Senses passive Perception 13 | Languages Common
- Innate Spellcasting (CHA, DC 13, +5) [OCR: source labels it "sylvan groan's" — copy error]: At will Dancing Lights, Prestidigitation; 3/day Invisibility.
- Actions — Staff: +1, reach 1.5 m, 1 (1d4-1) bludgeoning. Pom Light: ranged magic +5, reach 1.5 m [OCR: a ranged attack listed with 5 ft reach], 10 (2d6+3) radiant. Pom Cure (3/Day): a creature within 9 m recovers 7 (1d8)+3 HP. (Credit: Soren of Asgard.)

## Genus: Sahagin
Fish-folk of the Indigo Deep; once known for high-seas banditry, now settling new spawning grounds on western Vylbrand. (Wavespine/Wavetooth serve the primal Leviathan.)

### Shoalspine Sahagin — Medium humanoid (sahagin), Lawful Neutral
- AC 15 (natural armor, shield) | HP 30 (4d8+12) | Speed 9 m, 9 m swim | CR 1 (200 XP)
- STR 12(+1) DEX 14(+2) CON 16(+3) INT 10(+0) WIS 14(+2) CHA 12(+1) | Senses passive Perception 12 | Languages Common
- Amphibious. Slippery (advantage on checks/saves to escape a grapple).
- Actions — Multiattack: 2 Tridents (may substitute one for Lacerate). Claw: +4, reach 1.5 m, 5 (1d6+2) slashing. Trident: +4, reach 1.5 m (thrown 6/18 m), 5 (1d6+2) piercing. Lacerate (Recharge 3–4): +4, reach 1.5 m, 5 (1d6+2) slashing; DC 13 Constitution save or the wound bleeds — 4 (2d4) slashing at the start of its turns (re-save at end of turns). Hydroball (Recharge 5–6): 4.5 m cone, DC 13 Dexterity save, 7 (2d6) cold (half). (Credit: Soren of Asgard.)

### Shoalscale Sahagin — Medium humanoid (sahagin), Lawful Neutral
- AC 13 (natural armor) | HP 30 (4d8+12) | Speed 9 m, 9 m swim | CR 1 (200 XP)
- STR 14(+2) DEX 14(+2) CON 16(+3) INT 10(+0) WIS 14(+2) CHA 12(+1) | Senses passive Perception 12 | Languages Common
- Amphibious. Slippery.
- Actions — Multiattack: 2 Claw or Trident attacks (any combination; may substitute one for Lacerate). Claw: +4, reach 1.5 m, 5 (1d6+2) slashing. Trident: +4, reach 1.5 m (thrown 6/18 m), 5 (1d6+2) piercing. Lacerate (Recharge 5–6): +4, reach 1.5 m, 5 (1d6+2) slashing; DC 13 Constitution save or bleeding 4 (2d4) slashing at the start of its turns (re-save).
- Bonus Action — Enwater (1/Day): weapons deal +2 (1d4) cold for 1 minute. (Credit: Soren of Asgard.)

### Shoalclaw Sahagin — Medium humanoid (sahagin), Lawful Neutral
- AC 15 (natural armor) | HP 30 (4d8+12) | Speed 9 m, 9 m swim | CR 1 (200 XP)
- STR 14(+2) DEX 14(+2) CON 16(+3) INT 10(+0) WIS 14(+2) CHA 12(+1) | Senses passive Perception 12 | Languages Common
- Amphibious. Slippery.
- Actions — Multiattack: 2 Claw (may substitute one for Lacerate). Claw: +4, reach 1.5 m, 5 (1d6+2) slashing. Lacerate (Recharge 5–6): +4, reach 1.5 m, 5 (1d6+2) slashing; DC 13 Constitution save or bleeding 4 (2d4) slashing at the start of its turns (re-save).
- Bonus Action — Enwater (1/Day): weapons deal +2 (1d4) cold for 1 minute. (Credit: Soren of Asgard.)

### Shoaltooth Sahagin — Medium humanoid (sahagin), Lawful Neutral
- AC 13 (natural armor) | HP 30 (4d8+12) | Speed 9 m, 9 m swim | CR 1 (200 XP)
- STR 10(+0) DEX 14(+2) CON 16(+3) INT 10(+0) WIS 16(+3) CHA 14(+2) | Senses passive Perception 13 | Languages Common
- Amphibious. Slippery. Innate Spellcasting (WIS, DC 13, +5): At will Acid Splash, Shape Water; 3/day Frost Fingers.
- Actions — Staff: +2, reach 1.5 m, 2 (1d4) bludgeoning. Water: ranged spell +4, range 9 m, 17 (4d6+3) cold. Lacerate (Recharge 3–4): +4, reach 1.5 m, 5 (1d6+2) slashing; DC 13 Constitution save or bleeding 4 (2d4) slashing at the start of its turns (re-save). Hydroball (Recharge 5–6): 4.5 m cone, DC 13 Dexterity save, 7 (2d6) cold (half). (Credit: Soren of Asgard.)

### Wavespine Sahagin — Medium humanoid (sahagin), neutral evil
- AC 16 (natural armor, shield) | HP 91 (14d8+28) | Speed 9 m walk, 9 m swim | CR 5 (1,800 XP)
- STR 14(+2) DEX 18(+4) CON 14(+2) INT 10(+0) WIS 14(+2) CHA 8(-1)
- Saving Throws DEX +7 | Skills Survival +5, Acrobatics +7, Athletics +5 | Damage Immunities acid | Condition Immunities charmed | Senses darkvision 18 m, passive Perception 12 | Languages Common, Aquan
- Amphibious. Slippery.
- Actions — Multiattack: 2 Blessed Trident (may replace one with Corrupted Lacerate). Blessed Trident: +7, reach 3 m, 8 (1d8+4) piercing + 3 (1d6) acid. Corrupted Lacerate (Recharge 3–4): +7, reach 1.5 m, 7 (1d6+4) slashing; on a hit DC 15 Constitution save or the wound is corrupted with Leviathan's water aether (becomes vulnerable to acid; an acid-immune creature instead treats immunity as resistance; a resistant creature loses resistance — until the effect ends); 7 (2d6) acid at the end of its turns, re-save to end. Hydroball (Recharge 5–6): 4.5 m cone, DC 15 Dexterity save, 24 (7d6) acid (half).
- Reactions — Devoted to Leviathan: if it fails an attack roll or save within 18 m of Leviathan, Lord of the Whorl, it rerolls and must use the new roll. (Credit: Yamil.)

### Wavetooth Sahagin — Medium humanoid, neutral evil
- AC 14 (natural armor, shield) | HP 65 (10d8+20) | Speed 9 m walk, 9 m swim | CR 5 (1,800 XP)
- STR 12(+1) DEX 14(+2) CON 14(+2) INT 12(+1) WIS 18(+4) CHA 8(-1)
- Saving Throws WIS +7 | Skills Arcana +4, Nature +4, Perception +7 | Damage Immunities acid | Condition Immunities charmed | Senses darkvision 18 m, passive Perception 17 | Languages Common, Aquan
- Amphibious. Slippery. Innate Spellcasting (WIS, DC 15, +7): At will Acid Splash, Shape Water; 3/day each Frost Fingers, Acid Arrow; 2/day Elemental Bane (acid only); 1/day each Tidal Wave, Control Water, Fear.
- Actions — Staff: +4, reach 1.5 m, 3 (1d4+1) bludgeoning. Watera: ranged spell +7, range 9/18 m, 28 (7d6+4) acid. Corrupted Lacerate (Recharge 3–4): +5, reach 1.5 m, 5 (1d6+2) slashing; on a hit DC 15 Constitution save or corrupted (as Wavespine); 7 (2d6) acid at the end of its turns, re-save. Hydroball (Recharge 5–6): 4.5 m cone, DC 15 Dexterity save, 24 (7d6) acid (half).
- Reactions — Devoted to Leviathan: reroll a failed attack/save within 18 m of Leviathan. (Credit: Yamil.)

## Genus: Sylph
Plant-like beastmen resembling dolls mixed with foliage; natural spellcasters and habitual tricksters.

### Sylvan Groan — Small fae (sylph), Chaotic Neutral
- AC 14 | HP 18 (4d6+4) | Speed 3 m, 9 m fly | CR 2 (200 XP)
- STR 8(-1) DEX 18(+4) CON 12(+1) INT 10(+0) WIS 16(+3) CHA 16(+3)
- Damage Resistance lightning | Damage Vulnerability fire | Senses passive Perception 13 | Languages Common
- Innate Spellcasting (CHA, DC 13, +5): At will Shocking Grasp; 3/day Witch Bolt.
- Actions — Staff: +1, reach 1.5 m, 1 (1d4-1) bludgeoning. Sylvan Thunder: ranged spell +5, range 9 m, 17 (4d6+3) lightning.
- Bonus Actions — Enthunder (1/Day): weapons deal +5 (2d4) lightning for 1 minute. Shock Spikes (1/Day): for 1 minute, a creature that hits it with a weapon attack takes 5 (2d4) lightning. (Credit: Soren of Asgard.)

### Sylvan Scream — Small fae (sylph), Chaotic Neutral
- AC 15 | HP 27 (6d6+6) | Speed 3 m, 9 m fly | CR 1 (200 XP)
- STR 8(-1) DEX 18(+4) CON 12(+1) INT 10(+0) WIS 16(+3) CHA 16(+3)
- Damage Resistance lightning | Damage Vulnerability fire | Senses passive Perception 13 | Languages Common
- Innate Spellcasting (CHA, DC 13, +5): At will Shocking Grasp.
- Actions — Dagger: +6, reach 1.5 m, 6 (1d4+4) piercing. Sylvan Thunder: ranged spell +5, range 9 m, 10 (2d6+3) lightning.
- Bonus Actions — Enthunder (1/Day): +7 (3d4) lightning for 1 minute. Shock Spikes (1/Day): attacker takes 5 (2d4) lightning for 1 minute. (Credit: Soren of Asgard.)

### Sylvan Sough — Small fae (sylph), Chaotic Neutral
- AC 14 | HP 18 (4d6+4) | Speed 3 m, 9 m fly | CR 2 (200 XP)
- STR 8(-1) DEX 18(+4) CON 12(+1) INT 10(+0) WIS 16(+3) CHA 16(+3)
- Damage Resistance lightning | Damage Vulnerability fire | Senses passive Perception 13 | Languages Common
- Innate Spellcasting (WIS, DC 13, +5): At will Shocking Grasp; 3/day Cure Wounds, Healing Word.
- Actions — Staff: +1, reach 1.5 m, 1 (1d4-1) bludgeoning. Sylvan Thunder: ranged spell +5, range 9 m, 13 (3d6+3) lightning.
- Bonus Actions — Enthunder (1/Day): +5 (2d4) lightning for 1 minute. Shock Spikes (1/Day): attacker takes 5 (2d4) lightning for 1 minute. (Credit: Soren of Asgard.)

## Genus: Tonberry
Formerly the Lalafell of the sunken city of Nym, transformed by a voidsent plague. Some retain their sanity (Nymian); others give way to hatred.

### Tonberry — Small humanoid, chaotic evil
- AC 14 (natural armor) | HP 84 (13d6+39) | Speed 6 m | CR 1 (200 XP)
- STR 18(+4) DEX 11(+0) CON 16(+3) INT 8(-1) WIS 8(-1) CHA 8(-1)
- Saving Throws STR +6, CON +5 | Senses darkvision 18 m, passive Perception 9 | Languages Abyssal
- Long Live The King (+2 AC while within 9 m of a Tonberry King). Savage Attacks (melee crit deals one extra damage die). Small Savage (one extra damage die on melee hits, included).
- Actions — Chef's Knife: +6, reach 1.5 m, 9 (2d4+4) slashing.
- Reactions — Royal Guard: when a creature within 1.5 m attacks a Tonberry King, make a melee weapon attack against the attacker. (Credit: JPLDN.)

### Tonberry King — Large humanoid, chaotic evil
- AC 15 (natural armor) | HP 170 (20d10+60) | Speed 6 m | CR 7 (2,900 XP)
- STR 12(+1) DEX 12(+1) CON 16(+3) INT 18(+4) WIS 16(+3) CHA 16(+3)
- Saving Throws CON +6, WIS +6 | Senses darkvision 18 m, passive Perception 13 | Languages Abyssal
- King's Court (+2 AC if at least 4 allied Tonberries are within 9 m). King's Glory (melee crit deals one extra die). King's Rule (one extra die on melee hits, included).
- Actions — Multiattack: 3 Chef's Knife. Chef's Knife: +4, reach 1.5 m, 15 (2d10+4) slashing. Everybody's Grudge: ranged spell +7, range 18/18 m, 14 (2d10+4) psychic + 5 (1d10) psychic for every Tonberry killed within 90 m in the last 24 hours. (Credit: JPLDN.)

### Nymian Tonberry — Small Humanoid (Tonberry), Neutral Good
- AC 13 (natural armor) | HP 26 (4d6+12) | Speed 6 m | CR 1/4 (50 XP)
- STR 14(+2) DEX 11(+0) CON 16(+3) INT 16(+3) WIS 10(+0) CHA 10(+0) | Senses darkvision 18 m, passive Perception 10 | Languages Common
- Tough Skin (weapon attacks against it deal 1 less damage). Innate Spellcasting (INT, DC 13): At will Magic Stone; 1/day each Cure Wounds, Healing Word.
- Actions — Chef's Knife: +8 [OCR: +8 is high for these stats; reproduced verbatim], reach 1.5 m, 5 (1d4+2) slashing. (Credit: Soren of Asgard.)

### Folktale Tonberry — Small Humanoid (Tonberry), Chaotic Evil
- AC 15 (natural armor) | HP 112 (19d6+36) | Speed 6 m | CR 5 (1,800 XP)
- STR 20(+5) DEX 12(+1) CON 18(+4) INT 8(-1) WIS 8(-1) CHA 8(-1)
- Saving Throws STR +8, CON +7 | Senses darkvision 18 m, passive Perception 9 | Languages Abyssal
- Savage Attacks (melee crit deals one extra die). Small Savage (one extra die on melee hits, included). Thick Skin (weapon attacks against it deal 3 less damage).
- Actions — Multiattack: 3 Chef's Knife. Chef's Knife: +8, reach 1.5 m, 11 (2d4+5) slashing. Grudge (Recharge 5–6): a victim within 9 m makes a DC 15 Wisdom save, 2d10 necrotic and paralyzed on a fail (half, not paralyzed on success; re-save at end of its turns).
- Reactions — Karma (Recharge 3–4): when targeted by a resolved ranged weapon attack, cantrip, or spell, send a wisp back at the source — DC 15 Wisdom save, 2d10 necrotic and paralyzed (half, not paralyzed; re-save at end of its turns). (Credit: Soren of Asgard.)

# CLASS: VILEKIN
Insects, worms, and pests that begin in a larval form and develop through metamorphosis.

## Genus: Diremite
Colony-dwelling mites with a banemite matriarch; nomadic, hunting an area dry before moving on.

### Diremite — Large beast, unaligned
- AC 14 | HP 90 (12d10+24) | Speed 9 m walk, 9 m climb | CR 3 (700 XP)
- STR 15(+2) DEX 14(+2) CON 14(+2) INT 1(-5) WIS 9(-1) CHA 3(-4)
- Damage Immunities poison | Senses blindsight 18 m, passive Perception 9 | Languages —
- Spider Climb. Web Sense. Web Walker.
- Actions — Multiattack: 2 Claws and one Deadly Thrust. Claw: +4, reach 1.5 m, 6 (1d8+2) bludgeoning and grappled (escape DC 12; two claws, one target each). Deadly Thrust: +4, reach 3 m, 7 (1d10+2) piercing; DC 12 Constitution save or 2d6 poison and blinded 1d3 hours (half, no blind; if it fails by 5+, also paralyzed while poisoned; re-save at end of turns). Web (Recharge 5–6): ranged +5, range 9/18 m, target restrained (Strength check DC 12 to burst; webbing AC 10, HP 5, vulnerability to fire, immunity to bludgeoning/poison/psychic). (Credit: Jotunn-Bane.)

## Genus: Tarantula Hawk
Invasive oversized bees from the New World; hives become sprawling caverns.

### Worker Hawk — Medium beast, unaligned
- AC 13 (natural) | HP 39 (6d8+12) | Speed 6 m, fly 12 m | CR 1 (200 XP)
- STR 13(+1) DEX 12(+1) CON 14(+2) INT 1(-5) WIS 12(+1) CHA 3(-4) | Senses passive Perception 11 | Languages —
- Actions — Multiattack: one Bite and one Sting. Bite: +3, reach 1.5 m, 4 (1d6+1) piercing. Sting: +3, reach 1.5 m, 4 (1d6+1) piercing + 5 (2d4) poison. Spinal Tap (Recharge 5–6): +3, reach 1.5 m, 4 (1d6+1) piercing + 10 (4d4) poison; DC 12 Constitution save or poisoned 1 minute (2 (1d4) poison at the start of its turns; re-save at end of turns). (Credit: Soren of Asgard.)

### Soldier Hawk — Medium beast, unaligned
- AC 14 (natural) | HP 60 (8d8+24) | Speed 6 m, fly 12 m | CR 3 (700 XP)
- STR 14(+2) DEX 12(+1) CON 16(+3) INT 1(-5) WIS 12(+1) CHA 3(-4) | Senses passive Perception 11 | Languages —
- Actions — Multiattack: one Bite and one Sting. Bite: +4, reach 1.5 m, 5 (1d6+2) piercing. Sting: +4, reach 1.5 m, 5 (1d6+2) piercing + 15 (4d4) poison [OCR: 4d4 averages 10, source prints 15]. Spinal Tap (Recharge 5–6): +4, reach 1.5 m, 5 (1d6+2) piercing + 20 (8d4) poison; DC 13 Constitution save or poisoned 1 minute (2 (2d4) poison at the start of its turns [OCR: 2d4 averages 5, source prints 2]; re-save at end of turns). (Credit: Soren of Asgard.)

### Knight Hawk — Medium beast, unaligned
- AC 15 (natural) | HP 85 (10d8+40) | Speed 9 m, fly 18 m | CR 4 (1,100 XP)
- STR 16(+3) DEX 16(+3) CON 18(+4) INT 1(-5) WIS 14(+2) CHA 3(-4) | Senses passive Perception 12 | Languages —
- Actions — Multiattack: one Bite and one Sting, or two Sharp Spindle. Bite: +5, reach 1.5 m, 6 (1d6+3) piercing. Sting: +5, reach 1.5 m, 6 (1d6+3) piercing + 15 (4d4) poison. Sharp Spindle: ranged +5, range 9/18 m, 6 (1d6+3) piercing + 10 (3d6) poison. Straight Spindle (Recharge 5–6): a 1.5 m wide, 18 m long line, DC 14 Dexterity save, 14 (4d6) piercing (half). (Credit: Soren of Asgard.)

### Queen Hawk — Large beast, unaligned
- AC 15 (natural) | HP 147 (14d10+70) | Speed 6 m, fly 12 m | CR 6 (2,300 XP)
- STR 16(+3) DEX 16(+3) CON 20(+5) INT 1(-5) WIS 14(+2) CHA 3(-4) | Senses passive Perception 12 | Languages —
- Pheromone Leak: when a Soldier Hawk or Knight Hawk deals damage within 18 m of the Queen, it deals +2 damage.
- Actions — Multiattack: two Sting or two Sharp Spindle. Sting: +6, reach 1.5 m, 6 (1d6+3) piercing + 16 (4d6) poison. Sharp Spindle: ranged +5, range 9/18 m, 6 (1d6+3) piercing + 16 (4d6) poison. Apitoxin (Recharge 3–4): point within 9 m, 6 m radius sphere, DC 15 Dexterity save, 17 (5d6) acid (half); surfaces become difficult terrain 1 minute and a creature starting its turn there takes 7 (2d6) poison. Stinger Cell (Recharge 5–6): a 3 m wide, 6 m long line, DC 15 Dexterity save, 21 (6d6) piercing (half).
- Bonus Action — Assail: order a Knight Hawk within 18 m to use Sharp Spindle.
- Reactions — Avail: when targeted by an attack, order a Knight Hawk to move up to half speed toward her; if it reaches an adjacent space, it takes the attack's damage in her place. (Credit: Soren of Asgard.)

## Genus: Wespe
Invasive New World bees; the Killer Wespe is a spiteful variety.

### Killer Wespe — Small beast, unaligned
- AC 13 | HP 27 (6d6+6) | Speed 3 m, fly 15 m | CR 2 (250 XP)
- STR 8(-1) DEX 16(+3) CON 12(+1) INT 1(-5) WIS 10(+0) CHA 3(-4) | Senses passive Perception 10 | Languages —
- Actions — Sharp Sting: +5, reach 1.5 m, 6 (1d6+3) piercing + 7 (2d6) poison. Final Sting: +5, reach 1.5 m, 27 (6d6+6) piercing. May only be used when the Killer Wespe is below half its HP; it is reduced to 0 HP and dies after using Final Sting. (Credit: Soren of Asgard.)

## Genus: Worm
Large vilekin that vibrate their bodies to move; burrow and ambush, swallowing prey whole.

### Worm — Huge beast, unaligned
- AC 12 (natural) | HP 136 (13d12+52) | Speed 6 m, burrow 9 m | CR 4 (1,100 XP)
- [OCR: the ability-score line (STR/DEX/CON/INT/WIS/CHA) is MISSING in the source. Attack bonuses imply roughly STR ~16 (+3 used on attacks); GM should assign full scores.]
- Skills Stealth +2 | Senses blindsight 9 m, tremorsense 18 m, passive Perception 9 | Languages —
- Tunneler (burrows through solid rock at half burrow speed, leaving a 3 m-diameter tunnel).
- Actions — Bite: +5, reach 1.5 m, 9 (1d10+3) piercing + 17 (5d6) acid and grappled (escape DC 13) if Large or smaller (target restrained; can't bite another). Swallow: +5, reach 1.5 m, 9 (1d10+3) piercing [OCR: source prints "1d0"] against a grappled Medium-or-smaller creature; it is swallowed (blinded, restrained, total cover; 17 (5d6) acid at the start of the worm's turns; one creature at a time; regurgitated within 1.5 m if the worm dies). Sand Breath (1/Day): 4.5 m cone, DC 13 Constitution save, 27 (6d8) bludgeoning + blinded (half, no blind; re-save at end of turns). Recovered after it uses Bottomless Desert. Earth Break (Recharge 5–6): emerging with 3 m+ of movement, creatures within 3 m make a DC 13 Strength save, 28 (4d12) bludgeoning + pushed 3 m (half, no push).
- Bonus Action — Bottomless Desert (Recharge 5–6): while underground, a 4.5 m radius circle around it — creatures make a DC 13 Strength save or are pulled 3 m closer (no move on success). (Credit: Soren of Asgard.)

# CLASS: VOIDSENT
Otherworldly beings from the 13th reflection (the Void), reaching this world via contracts (aether for power), rifts, or the bodies of the dead. The Void has a 12-rung hierarchy.

## Genus: Ahriman
Voidsent manifesting through animals' eyes; natural magicians that fly by clawing at aether.

### Ahriman — Medium Fiend (Voidsent), Neutral Evil
- AC 14 | HP 117 (18d8+36) | Speed 3 m, 12 m fly | CR 4 (1,100 XP)
- STR 10(+0) DEX 18(+4) CON 14(+2) INT 10(+0) WIS 14(+2) CHA 18(+4)
- Saving Throws Charisma +6 | Condition Immunities poisoned | Senses darkvision 36 m, passive Perception 12 | Languages Abyssal
- Devil's Sight. Innate Spellcasting (CHA, +6, DC 14): 1st level (4 slots) Magic Missile, Witch Bolt; 2nd level (3 slots) Darkness, Hold Person.
- Actions — Multiattack: 2 Void Stone [OCR: source says "2 void stone attacks" but also lists Void Claw]. Void Claw: melee magic +6, reach 1.5 m, 9 (1d10+4) slashing. Void Stone: ranged magic +6, range 12 m, 13 (2d8+4) bludgeoning. Dread Gaze (Recharge 5–6): 4.5 m cone, DC 14 Charisma save, 14 (4d6) necrotic + paralyzed 1 minute (half, no paralyze; re-save at end of turns).
- Bonus Action — Cheapshot: Void Claw against a paralyzed creature. (Credit: Soren of Asgard.)

## Genus: Bomb
Volatile fire voidsent bordering on elementals; grow from head-sized to massive.

### Bomb — Tiny Fiend (Voidsent), unaligned
- AC 12 | HP 63 (14d4+28) | Speed 0 m, fly 6 m (hover) | CR 4 (1,100 XP)
- STR 8(-1) DEX 14(+2) CON 14(+2) INT 3(-4) WIS 10(+0) CHA 16(+3)
- Damage Vulnerabilities cold | Damage Immunities fire, poison | Condition Immunities poisoned | Senses darkvision 18 m, passive Perception 10 | Languages —
- Death Burst: at 0 HP, creatures within 4.5 m make a DC 13 Dexterity save, 14 (4d6) fire (half); ignites unattended flammables. Devil's Sight. Illumination: bright light 4.5 m + dim 4.5 m (out when it dies).
- Actions — Bomb-butt: +1, reach 1.5 m, 2 (1d4) bludgeoning + 10 (3d6) fire. Blaze: ranged +5, range 9 m, 13 (3d8) fire. Detonator (Recharge 6): 3 m radius around it, DC 13 Dexterity save, 14 (4d6) fire (half); per size category above Tiny, +1.5 m radius and +3 (1d6) fire, then it becomes Tiny and loses remaining temp HP. Self-Destruct: reduce to 0 HP, triggering Death Burst.
- Reactions — Swell: when it takes damage, its size increases one category (max Large); per category above Tiny, -1 AC and it gains temp HP equal to twice its CON modifier. (Credit: Cruztown.)

### Progenitrix — Large Elemental, Chaotic Evil
- AC 15 (natural) | HP 114 (12d10+48) | Speed 0 m, fly 9 m (hover) | CR 8 (3,900 XP)
- STR 12(+1) DEX 14(+2) CON 18(+4) INT 8(-1) WIS 12(+1) CHA 20(+5)
- Damage Vulnerabilities cold, necrotic | Damage Immunities fire, poison | Condition Immunities exhaustion, poisoned | Senses darkvision 18 m, passive Perception 12 | Languages —
- Death Burst: at 0 HP, creatures within 9 m make a DC 16 Dexterity save, 33 (6d10) fire (half); ignites flammables. False Appearance: while above half HP it looks like a standard (Large) bomb. Illumination: bright 9 m + dim 9 m.
- Actions — Body Slam: +4, reach 1.5 m, 12 (2d10+1) bludgeoning + 16 (3d10) fire. Blaze: ranged spell +8, range 9 m, 22 (4d10) fire. Scalding Scolding (Recharge 5–6): use Body Slam; on a hit +11 (2d10) fire and each creature within 3 m of the target makes a DC 16 Dexterity save or takes 11 (2d10) fire. Big Burst: reduce itself to 0 HP (triggering Death Burst) and create 1d4 bombs, each with half the Progenitrix's remaining HP. (Credit: not named in source.)

## Genus: Deathgaze (Voidsent variant)
### Deathgaze Hollow — Huge fiend, Neutral Evil
- AC 18 | HP 172 (15d12+75) | Speed 6 m walk, 15 m fly (hover) | CR 11 (7,200 XP)
- STR 17(+3) DEX 18(+4) CON 21(+5) INT 20(+5) WIS 14(+2) CHA 8(-1)
- Saving Throws DEX +8, CON +9, INT +9 | Skills Perception +6, Arcana +9 | Damage Resistances necrotic, nonmagical b/p/s, force | Condition Immunities charmed, frightened, grappled, prone, sleep, blinded | Senses Devil's Sight 36 m, passive Perception 16 | Languages Abyssal
- Aversion of Radiant (if it takes radiant damage, disadvantage on attacks and ability checks until end of its next turn). Flyby. Legendary Resistance (no per-day count given in source). Magic Resistance. Innate Spellcasting (INT, DC 17, +9): At will Aero II (*Aerora); 3/day Aero III (*Aeroga); 2/day Aero IV (*Aeroja). (See file 03.)
- Actions — Multiattack: 2 Claws. Claw: +7, reach 3 m, 12 (2d8+3) slashing + 7 (2d6) necrotic. Death Glare (Recharge 5–6): one creature within 18 m that can see it makes a DC 18 Wisdom save or is frightened 1 minute (fail by 5+ also paralyzed; re-save at end of turns; success = immune 24 hours). Void Death: a frightened creature it can see within 18 m makes a DC 18 Wisdom save or drops to 0 HP. Void Death IV (1/Day): a creature within 18 m at 0 HP and still alive makes a DC 18 Constitution save or dies; if it dies, the Deathgaze regains 10d6 HP. Doom: a creature within 18 m makes a DC 18 Wisdom save or becomes Doomed (2d6 necrotic at the start of its turns; ends only by killing/KO'ing the caster, being on a different plane, or Remove Curse / Greater Restoration / Wish). (Credit: Jotunn-Bane.)

## Genus: Demon
Voidsent infusing the bodies of the dead; disciplined foot soldiers (9th rung).

### Demon — Medium fiend (Voidsent), chaotic evil
- AC 14 (natural) | HP 58 (9d8+18) | Speed 9 m | CR 3 (700 XP)
- STR 16(+3) DEX 12(+1) CON 14(+2) INT 6(-2) WIS 10(+0) CHA 8(-1)
- Damage Resistances necrotic | Condition Immunities charmed, frightened | Senses darkvision 18 m, passive Perception 10 | Languages —
- Devil's Sight. Soldier of the Void: once per turn, +7 (2d6) damage to a creature it hits with a weapon if within 9 m of an allied voidsent of higher CR.
- Actions — Multiattack: 2 Scythe. Scythe: +5, reach 3 m, 8 (1d10+3) slashing.
- Bonus Action — Enthunder (1/Short Rest): its Scythe deals +3 (1d6) lightning until the end of its next turn. (Credit: Yamil.)

## Genus: Flan
Residual void matter; reactive to elemental magic, can split when struck (11th rung).

### Unaspected Flan — Large Ooze, Chaotic Evil
- AC 8 (natural) | HP 45 (6d10+12) | Speed 3 m, 3 m climb | CR 2 (450 XP)
- STR [OCR: score missing in source, only "(+2)"] DEX 6(-2) CON 14(+2) INT 2(-4) WIS 6(-2) CHA 1(-5)
- Damage Resistances b/p/s from nonmagical attacks | Damage Immunities nonmagical slashing | Senses blindsight 18 m (blind beyond), passive Perception 8 | Languages —
- Amorphous. Spider Climb.
- Actions — Body Slam: +3, reach 1.5 m, 5 (1d6+1) slashing.
- Reactions — Split: when a Medium-or-larger Flan takes slashing damage and has ≥10 HP, it splits into two new Flans (each with half the original's HP, one size smaller). (Credit: Jotunn-Bane.)

### Unstable Flan — Medium Ooze, Chaotic Evil
- AC 8 (natural) | HP 85 (10d8+40) | Speed 6 m | CR 2 (450 XP)
- STR 12(+1) DEX 7(-2) CON 18(+4) INT 5(-3) WIS 10(+0) CHA 16(+3)
- Saving Throws CON +7 | Damage Resistances b/p/s from nonmagical attacks | Senses passive Perception 10 | Languages Abyssal
- Spellcasting (4th-level; CHA, DC 13, +5): 1st level (4 slots) Absorb Elements. Unsteady Composition: when it uses Absorb Elements it keeps resistance to that type (changing colour) and gains a cantrip of that element (cast via its spellcasting). The DM selects the Flan's starting element to suit its environment.
- Actions — Multiattack: 2 Pseudopod. Pseudopod: +3, reach 1.5 m, 5 (1d6+1) slashing. (Credit: Soren of Asgard.)

### Unstable Greater Flan — Large Ooze, Chaotic Evil
- AC 10 (natural) | HP 180 (19d8+80) | Speed 6 m | CR 8 [OCR: source lists "450 XP" — wrong; CR 8 = 3,900 XP. HP 19d8+80 averages ~165; 180 reproduced verbatim]
- STR [OCR: score missing, only "(+3)"] DEX 10(+0) CON 18(+4) INT 5(-3) WIS 10(+0) CHA 16(+3)
- Saving Throws CON +10 | Damage Resistances b/p/s from nonmagical attacks | Senses passive Perception 10 | Languages Abyssal
- Spellcasting (5th-level; CHA, DC 16, +8): 1st level (4 slots) Absorb Elements; 3rd level (3 slots) changes with Unsteady Composition. Unsteady Composition: keeps resistance to the absorbed type and gains a cantrip and a 3rd-level spell of that element.
- Actions — Multiattack: 3 Pseudopod. Pseudopod: +8, reach 1.5 m, 8 (1d8+3) slashing. (Credit: Soren of Asgard.)

## Genus: Gaelicat
Cat-bat creatures; mischievous and clever (beastkin or voidsent is debated).

### Gaelicat — Small fiend (voidsent), chaotic neutral
- AC 14 (natural) | HP 40 (9d6+9) | Speed 6 m walk, 12 m fly | CR 1 (200 XP)
- STR 8(-1) DEX 19(+4) CON 12(+1) INT 12(+1) WIS 16(+3) CHA 10(+0)
- Skills Perception +5, Stealth +6 | Senses darkvision 18 m, passive Perception 15 | Languages —
- Keen Sight and Smell. Nimble Escape (Disengage or Hide as a bonus action).
- Actions — Scratch: +6, reach 1.5 m, 9 (2d4+4) slashing. Fascinating Lure: a humanoid within 9 m that can hear it makes a DC 14 Wisdom save or is charmed — it must move toward the Gaelicat to pet or pick it up (re-save at end of turns; success = immune 24 hours). The Gaelicat has advantage on attacks against a creature petting/holding it. (Credit: Jotunn-Bane.)

## Genus: Gremlin
Lowest-rung voidsent; scavenge aether and curse foes with magicked words.

### Gremlin — Small fiend (Voidsent), chaotic evil
- AC 15 (natural) | HP 27 (6d6+6) | Speed 9 m | CR 1 (200 XP)
- STR 6(-2) DEX 16(+3) CON 12(+1) INT 14(+2) WIS 14(+2) CHA 16(+3)
- Saving Throws DEX +5, CHA +5 | Skills Stealth +5, Intimidation +5, Performance +5 | Damage Resistances necrotic | Senses darkvision 18 m, passive Perception 12 | Languages Common, plus two more it learned to mimic
- Devil's Sight. Innate Spellcasting (CHA, DC 13, +5): At will Vicious Mockery; 1/Long or Short Rest Bane.
- Actions — Scratch: +5, reach 1.5 m, 5 (1d4+3) slashing.
- Reactions — Salt in the Wound: when a creature it can see within 18 m fails an attack, it can cast Vicious Mockery on that creature. (Credit: Yamil.)

## Genus: Succubus
Voidsent that force their soul into a humanoid woman's body, gaining transcendent grace and some of the host's memories.

#### Echoes of the Dead (Succubus quirk, 1d8 — flavor)
A Succubus keeps some of its host's traits; the DM may roll: 1 obsessed with its hair; 2 craves the host's favourite food; 3 bites its nails when distracted; 4 irrational fear of spiders; 5 overly apologetic (even while killing); 6 loves dressing its corpse-body in outfits; 7 loves tales of famous adventurers; 8 inherited the host's nervousness (taps feet/fingers).

### Succubus — Medium Fiend (voidsent), Chaotic Evil
- AC 16 (natural) | HP 32 (6d8+10) | Speed 9 m, fly 12 m | CR 2 (450 XP)
- STR 8(-1) DEX 12(+1) CON 14(+2) INT 7(-2) WIS 8(-1) CHA 16(+3)
- Saving Throws Wisdom +1, Charisma +5 | Skills Deception +5, Persuasion +5 | Damage Resistances cold | Condition Immunities charmed | Senses darkvision 18 m, passive Perception 9 | Languages Abyssal, Common, Infernal
- Ethereal Sight (see 18 m into the Ethereal Plane and vice versa).
- Actions — Void Fira: ranged magic +5, reach 9 m, 10 (2d6+3) fire.
- Bonus Action — Cold Caress: melee +3, reach 1.5 m, 5 (1d8+1) cold; on a hit DC 13 Constitution save or poisoned until the end of the Succubus's next turn. (Credit: Brulen.)

### Lady Amandine — Medium Fiend (voidsent), Chaotic Evil
- AC 16 (natural) | HP 52 (8d8+16) | Speed 9 m, fly 12 m | CR 4 (1,100 XP)
- STR 8(-1) DEX 16(+3) CON 14(+2) INT 15(+2) WIS 10(+0) CHA 18(+4)
- Saving Throws Wisdom +4, Charisma +6 | Skills Arcana +4, Deception +6, Persuasion +6 | Damage Resistances cold, fire, poison; b/p/s from nonmagical attacks | Condition Immunities charmed | Senses darkvision 18 m, passive Perception 12 | Languages Abyssal, Common, Infernal
- Ethereal Sight (18 m).
- Actions — Multiattack: one Void Fira and one Void Thunder. Void Fira: ranged magic +6, reach 9 m, 11 (2d6+4) fire. Void Thunder: ranged magic +6, reach 9 m, 7 (1d6+4) lightning + an additional 7 (1d6+4) lightning at the end of the target's next turn.
- Bonus Actions — Cold Caress: melee +5, reach 1.5 m, 7 (1d8+3) cold; DC 14 Constitution save or poisoned until the end of Lady Amandine's next turn. Dark Caress: melee +5, reach 1.5 m, 7 (1d8+3) necrotic; DC 14 Constitution save or frightened until the end of Lady Amandine's next turn. (Credit: Brulen.)

### Carmilla — Medium Fiend (voidsent), Chaotic Evil
- AC 18 (natural) | HP 75 (10d8+30) | Speed 9 m, fly 18 m | CR 6 (2,300 XP)
- STR 8(-1) DEX 18(+4) CON 16(+3) INT 15(+2) WIS 10(+0) CHA 20(+5)
- Saving Throws Wisdom +5, Charisma +8 | Skills Arcana +5, Deception +8, Persuasion +8 | Damage Resistances cold, fire, lightning, poison; b/p/s from nonmagical attacks | Condition Immunities charmed | Senses darkvision 18 m, passive Perception 13 | Languages Abyssal, Common, Infernal
- Legendary Resistance (1/day). Ethereal Sight (18 m).
- Actions — Multiattack: one Void Thunder and either a Void Fira or a Crimson Blade. Crimson Blade: melee +7, reach 1.5 m, 15 (2d10+4) cold. Void Fira: ranged magic +8, reach 18 m, 12 (2d6+5) fire. Void Thunder: ranged magic +6, reach 9 m, 8 (1d6+5) lightning + an additional 8 (1d6+5) lightning at the end of the target's next turn.
- Bonus Actions — Cold Caress: melee +7, reach 1.5 m, 8 (1d8+4) cold; DC 15 Constitution save or poisoned until the end of Carmilla's next turn. Dark Caress: melee +7, reach 1.5 m, 8 (1d8+5) necrotic; DC 15 Constitution save or frightened until the end of Carmilla's next turn.
- Legendary Actions (3): Cold Mist (all creatures within 30 m make a DC 15 Wisdom save or are silenced until the start of Carmilla's next turn). Move (move up to speed without provoking opportunity attacks). Teleport (2 Actions: teleport up to 36 m to an unoccupied space it can see). (Credit: not named in source; section by Brulen.)

# CLASS: WAVEKIN
Defined by the ability to breathe underwater; often timid, but some defend territory fiercely.

## Genus: Eft
Electric-throated amphibians of La Noscea's caverns and shores.

### Eft — Medium Beast, unaligned
- AC 13 (natural) | HP 52 (7d8+21) | Speed 6 m, swim 9 m | CR 1 (200 XP)
- STR 14(+2) DEX 10(+0) CON 16(+3) INT 3(-4) WIS 12(+1) CHA 8(-1)
- Skills Stealth +2 | Senses passive Perception 11 | Languages —
- Actions — Bite: +4, reach 1.5 m, 5 (1d6+2) slashing + 3 (1d6) lightning. Stagnant Spray (Recharge 5–6): 4.5 m cone, DC 13 Dexterity save, 5 (2d4) cold (half).
- Bonus Action — Peculiar Light (Recharge 5–6): a 3 m radius jolt; the Eft has advantage on attacks against affected creatures until the end of its turn. (Credit: Soren of Asgard.)

### Mudpuppy — Large Beast, unaligned
- AC 14 (natural) | HP 119 (14d10+42) | Speed 9 m, swim 12 m | CR 4 (1,100 XP)
- STR 16(+3) DEX 10(+0) CON 18(+4) INT 3(-4) WIS 14(+2) CHA 8(-1)
- Skills Stealth +2 | Senses passive Perception 12 | Languages —
- Keen Sight.
- Actions — Bite: +5, reach 1.5 m, 14 (2d10+3) piercing + 14 (4d6) lightning. Bog Bomb (one per short rest): point within 9 m, 6 m radius sphere, DC 14 Dexterity save, 14 (4d6) bludgeoning + movement reduced 3 m (half, no other effect); difficult terrain 1 minute. Stagnant Spray (Recharge 5–6): 4.5 m cone, DC 14 Dexterity save, 10 (4d4) cold (half).
- Bonus Action — Peculiar Light (Recharge 5–6): a 3 m radius jolt; advantage on attacks against affected creatures until end of turn [OCR: source text says "the Eft"]. (Credit: Soren of Asgard.)

## Genus: Elbst
Amphibious quadrupeds; fierce hunters and the Sahagin's preferred beast of burden.

### Elbst — Medium beast, unaligned
- AC 15 (natural) | HP 82 (11d8+33) | Speed 9 m walk, swim 15 m | CR 3 (700 XP)
- STR 14(+2) DEX 18(+4) CON 16(+3) INT 7(-2) WIS 12(+1) CHA 10(+0)
- Skills Athletics +2, Perception +1, Stealth +4 | Senses darkvision 18 m, passive Perception 11 | Languages —
- Aggressive (bonus action: move up to speed toward a hostile creature). Amphibious. Underwater Camouflage (advantage on Stealth underwater).
- Actions — Multiattack: one Bite and one Claw. Bite: +6, reach 1.5 m, 8 (1d8+4) piercing. Claw: +6, reach 1.5 m, 7 (1d6+4) slashing. Flash Flood (Recharge 5–6): a 9 m long, 1.5 m wide line, DC 12 Dexterity save, 22 (4d10) cold (half); on a fail also pushed back 3 m. (Credit: Jotunn-Bane.)

## Genus: Gigantoad
Bloated toads with slippery hides; drag prey with sticky tongues and crush with their weight.

### Gigantoad — Large beast, unaligned
- AC 12 (natural) | HP 76 (9d10+27) | Speed 9 m | CR 2 (450 XP)
- STR 20(+5) DEX 10(+0) CON 16(+3) INT 2(-4) WIS 13(+1) CHA 7(-2)
- Skills Athletics +7 | Senses passive Perception 11 | Languages —
- Standing Leap (long jump up to 9 m, high jump up to 4.5 m, with or without a run).
- Actions — Multiattack: 2 Bites, or Tongue then Labored Leap if available [OCR: multiattack calls it "Deadly Leap"; the action below is named Labored Leap]. Bite: +7, reach 1.5 m, 8 (1d6+5) bludgeoning. Tongue: +7, reach 6 m, 7 (1d4+5) bludgeoning; DC 13 Strength save or pulled into an unoccupied space within 1.5 m of the Gigantoad. Labored Leap (Recharge 6): a standing high jump; creatures within 3 m make a DC 13 Strength or Dexterity save (target's choice) or are knocked prone and take 14 (4d6) bludgeoning (on success: half damage, not prone, pushed 1.5 m to an unoccupied space; if none, prone where it was). (Credit: Jotunn-Bane.)

## Genus: Jellyfish
Land-dwelling jellyfish that overpopulate without natural predators.

### Anemone — Small beast, unaligned
- AC 12 (natural) | HP 45 (7d7+21) [OCR: "7d7" is not a standard die; reproduced verbatim] | Speed 6 m fly (hover), 6 m swim | CR 2 (450 XP)
- STR 14(+2) DEX 10(+0) CON 16(+3) INT 2(-4) WIS 10(+0) CHA 2(-4)
- Saving Throws Constitution +5 | Damage Resistances slashing, piercing, bludgeoning | Senses darkvision 18 m, passive Perception 10 | Languages —
- Actions — Multiattack: 2 Tentacle (may replace one with Shock). Tentacle: +4, reach 1.5 m, 2 (1d4) lightning. Shock: one creature within 1.5 m makes a DC 13 Constitution save, 14 (4d6) lightning (half). (Credit: Yamil.)

### Aurelia — Small beast, unaligned
- AC 11 (natural) | HP 16 (3d6+6) | Speed 6 m fly (hover), 6 m swim | CR 1/2 (100 XP)
- STR 13(+1) DEX 8(-1) CON 14(+2) INT 2(-4) WIS 10(+0) CHA 2(-4)
- Saving Throws Constitution +4 | Damage Resistances slashing, piercing | Senses darkvision 18 m, passive Perception 10 | Languages —
- Actions — Tentacle: +3, reach 1.5 m, 4 (1d6+1) bludgeoning + 2 (1d4) poison. Numbing Tendrils: one creature within 1.5 m makes a DC 12 Constitution save or is paralyzed 1 minute (re-save at end of turns). (Credit: Yamil.)

## Genus: Pugil
Gas-bladder fish that hover just above the ground; eat anything that moves.

### Pugil — Medium beast, unaligned
- AC 13 (natural) | HP 18 (4d8) | Speed 9 m (hover), swim 9 m | CR 1/4 (50 XP)
- STR 13(+1) DEX 10(+0) CON 11(+0) INT 11(+0) WIS 10(+0) CHA 8(-1)
- Skills Perception +4 | Senses passive Perception 14 | Languages —
- Amphibious. Slippery (advantage on checks/saves to escape a grapple).
- Actions — Bite: +3, reach 1.5 m, 3 (1d4+1) piercing. Aqua Ball: ranged +3, range 9/18 m, 4 (1d6+1) cold. (Credit: Jotunn-Bane.)

END OF FILE — 04_Bestiary (COMPLETE — all 13 creature classes: Ashkin, Beastkin, Cloudkin, Dragon, Forgekin, Primals, Scalekin, Seedkin, Soulkin, Spoken, Vilekin, Voidsent, Wavekin). Note: the Playable Races section (Tribal Society) of the source Codex is NOT included here — it belongs in file 01.
