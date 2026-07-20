# 02_CLASSES — Jobs
Version v0.7 | Source: FFXIV x D&D 5e Player Compendium (Dawntrail Edition)

## SCHEMA NOTES
- PRINCIPLE: completeness over brevity. NO content cut; only reformatted for parsing.
- DATA LANGUAGE = English (single source of truth). The GEM renders flavor into Italian at OUTPUT.
- MEASUREMENTS = metric, pre-converted (decimal POINT in data; render with comma at output). Key: 5 ft=1.5 m, 10 ft=3 m, 15 ft=4.5 m, 20 ft=6 m, 30 ft=9 m, 40 ft=12 m, 60 ft=18 m, 100 ft=30 m, 120 ft=36 m.
- Mechanics (feature names, conditions, spells, dice) stay English and verbatim. Do NOT invent features.
- HP_ref = default pre-calculated hit points per level (fixed-average method, WITHOUT Constitution). Default PF = HP_ref[level] + (CON modifier x level). This value is STABLE — reuse it identically for the same Job+level. It anchors PF in-range so impossible totals never appear. By Hit Die: d6 = 6 +4/lvl; d8 = 8 +5/lvl; d10 = 10 +6/lvl; d12 = 12 +7/lvl.

# ASTROLOGIAN
**Hit Die:** d8 | **Saving Throws:** Wisdom, Charisma | **Spellcasting:** Wisdom (prepared)

**Flavor.** Gazing at the stars through their intricate telescope, the Astrologian notes the expected time until the next wave of attacks would fall upon the city, allowing their home to place their defenses properly. The mysterious rot running through the forest threatened the lives of the small village; with a chime of their bell and the reading of the land's lifeblood, the geomancer found the secret behind the plague. In the back of a lively tavern, the veiled fortune teller overturned card after card, weaving the story of their patrons' future. Humanity has always sought insight into the future, and the astrologians are one of the many groups formed of this primal wish, using a variety of methods and rituals to discern the highs and lows of fate.
- The Celestial Web: fate is said to be written in the stars; Astrologians look to the stars (and the planet, itself called a star) to understand the interconnected net of information.
- To Read Fate: some use lens-and-measurement devices imparting findings via tarot; some use sacred bells to read leylines; others use the traditional Deck of Sixty alone.
- Creating an Astrologian: an art usually passed down by a mentor (Sharlayan education, geomancer tutelage, or a wandering fortuneteller). Consider why you set off — a grave danger found in divination, a wish to guide others, or to hone your skills.

**HP_ref (d8):** 1:8 | 2:13 | 3:18 | 4:23 | 5:28 | 6:33 | 7:38 | 8:43 | 9:48 | 10:53 | 11:58 | 12:63 | 13:68 | 14:73 | 15:78 | 16:83 | 17:88 | 18:93 | 19:98 | 20:103. (Default PF = HP_ref[N] + CON mod x N.)

**Progression — spell slots per level**
| Lvl | PB | Cantrips | Features | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | +2 | 3 | Spellcasting, Divination, Divination School | 2 | — | — | — | — | — | — | — | — |
| 2 | +2 | 3 | Astrodyne, Time Dilation | 3 | — | — | — | — | — | — | — | — |
| 3 | +2 | 3 | Divination School Feature | 4 | 2 | — | — | — | — | — | — | — |
| 4 | +2 | 4 | Ability Score Improvement | 4 | 3 | — | — | — | — | — | — | — |
| 5 | +3 | 4 | Redivine | 4 | 3 | 2 | — | — | — | — | — | — |
| 6 | +3 | 4 | Divination School Feature | 4 | 3 | 3 | — | — | — | — | — | — |
| 7 | +3 | 4 | — | 4 | 3 | 3 | 1 | — | — | — | — | — |
| 8 | +3 | 4 | Ability Score Improvement | 4 | 3 | 3 | 2 | — | — | — | — | — |
| 9 | +4 | 4 | — | 4 | 3 | 3 | 3 | 1 | — | — | — | — |
| 10 | +4 | 5 | Divination School Feature | 4 | 3 | 3 | 3 | 2 | — | — | — | — |
| 11 | +4 | 5 | Spread | 4 | 3 | 3 | 3 | 2 | 1 | — | — | — |
| 12 | +4 | 5 | Ability Score Improvement | 4 | 3 | 3 | 3 | 2 | 1 | — | — | — |
| 13 | +5 | 5 | — | 4 | 3 | 3 | 3 | 2 | 1 | 1 | — | — |
| 14 | +5 | 5 | Divination School Feature | 4 | 3 | 3 | 3 | 2 | 1 | 1 | — | — |
| 15 | +5 | 5 | — | 4 | 3 | 3 | 3 | 2 | 1 | 1 | 1 | — |
| 16 | +5 | 5 | Ability Score Improvement | 4 | 3 | 3 | 3 | 2 | 1 | 1 | 1 | — |
| 17 | +6 | 5 | Dual Divination | 4 | 3 | 3 | 3 | 2 | 1 | 1 | 1 | 1 |
| 18 | +6 | 5 | Exaltation | 4 | 3 | 3 | 3 | 3 | 1 | 1 | 1 | 1 |
| 19 | +6 | 5 | Ability Score Improvement | 4 | 3 | 3 | 3 | 3 | 2 | 1 | 1 | 1 |
| 20 | +6 | 5 | Strings of Fate | 4 | 3 | 3 | 3 | 3 | 2 | 2 | 1 | 1 |

**Quick Build.** Make Wisdom highest, then Constitution. Sage background. Take Dancing Lights, Sacred Flame, Guidance cantrips and choose the Sharlayan Astrology school. Prepare Cure Wounds and Guiding Bolt.

**Proficiencies.** Armor: none. Weapons: Daggers, Darts, Slings, Quarterstaffs, Light Crossbows. Tools: Divination Tools. Saving Throws: Wisdom, Charisma. Skills: choose two from Arcana, Deception, Insight, Persuasion, History, Religion.
**Equipment.** (a) a dagger or (b) a quarterstaff; (a) a light crossbow and 20 bolts or (a) a simple weapon; a Star Globe; a Divination Deck; (a) an explorer's pack or (b) a scholar's pack.
- Divination Deck: a tool used to perform fortune telling; this proficiency lets you tell fortunes via tarot decks.

**Spellcasting.** You cast Astrologian spells (Wisdom). Spell save DC = 8 + PB + WIS mod; Spell attack = PB + WIS mod.
- Cantrips: know three at 1st level from the Astrologian list; more at higher levels (Cantrips Known column).
- Preparing: prepare WIS modifier + Astrologian level spells (min 1), of levels you have slots for; change on a long rest (1 minute per spell level per spell).
- Ritual Casting: can cast an Astrologian spell as a ritual if it has the ritual tag and is prepared.
- Focus: a star globe, planisphere, or similar arcane focus.

**Divination School (subclass at 1st).** Choose Sharlayan, Geomancy, or Fortuneteller. Grants features at 1st, 3rd, 6th, 10th, 14th.

**Divination (1st).** As an action, perform a reading: roll 1d6 and apply the corresponding effect to yourself or a creature within 9 m you can see. The boon lasts a number of rounds equal to your WIS modifier (min 1). A creature may have only one Divination effect at a time (a new one replaces the old). Uses = your Astrologian level, recovered on a short or long rest.

*Divination Effects:*
- 1 — Bravery: the creature gains a 1d6 bonus to damage rolls, once per action, bonus action, and reaction. Increases to 2d6 at 5th, 3d6 at 11th, 4d6 at 17th.
- 2 — Resilience: all damage the creature takes is reduced by 1d6. Increases to 2d6 at 5th, 3d6 at 11th, 4d6 at 17th.
- 3 — Activity: the creature gains one extra attack when it takes the Attack action.
- 4 — Precision: the creature's attack rolls crit on a 19 or 20.
- 5 — Knowledge: the creature has advantage on saving throws against spell effects.
- 6 — Triumph: the creature has advantage on attack rolls.
- Creator's note: results were renamed to general terms to accommodate Geomancy; you may use the original FFXIV card names if preferred — e.g. The Balance (Resilience), The Arrow (Activity), The Ewer (Knowledge), The Spire (Triumph), plus the cards for Bravery and Precision. (Source OCR partially corrupted on this note.)

**Astrodyne (2nd).** When you cast a spell using a spell slot, you regain a Divination.
**Time Dilation (2nd).** When you cast a spell you may concentrate on it and release it as a reaction. If you concentrate until your next turn, it releases as though cast one level higher (max +1 level). If concentration breaks, the spell releases.
**Ability Score Improvement (4th, 8th, 12th, 16th, 19th).** +2 to one or +1 to two (max 20).
**Redivine (5th).** When you use Divination, as a bonus action you may reroll the d6 before applying; you must use the new result.
**Spread (11th).** When you use Divination, as a bonus action you may set the effect aside into your spread (max = WIS modifier). On your turn, as a bonus action, use any effect from your spread. Spread divinations expire on a long rest.
**Dual Divination (17th).** When you use the Divination action, perform and use two divinations (each consumes an available divination); as a bonus action you may place one or both into your spread.
**Exaltation (18th).** As an action, expend an available divination to reapply a Divination effect on a creature within Divination range.
**Strings of Fate (20th).** When you roll initiative, recover available divinations equal to your WIS modifier.

## Astrologian — Subclass: Sharlayan Astrology
Uses astrometers and the Deck of Sixty (twelve gods of Eorzea); stellar magic to punish foes and celestial energy to heal.
- Fortunate Healer (1st): whenever you use a spell of 1st level or higher to restore HP, you may expend an available divination to add 1d6 + WIS modifier healing.
- Premonition Reading (3rd): as an action, expend an available draw to scan for traps, gaining advantage on Perception checks for 1 minute.
- Aspected Benefic (6th): when you cast a 1st-level-or-higher spell that restores an ally's HP, you may leave a regenerative effect on all affected allies — they recover 1d6 HP at the start of their turn for rounds equal to your WIS modifier. Must finish a short or long rest to use again.
- Lightspeed (10th): cast a prepared 1st-, 2nd-, or 3rd-level spell as a bonus action by spending available divinations equal to its level.
- Astral Fortune (14th): the Fortunate Healer additional healing becomes 6 + WIS modifier; additionally, you may roll 1d6 and apply the appropriate Divination effect as if you had used the Divination action.

## Astrologian — Subclass: Geomancy
Diviners of Hingashi who read the planet's leylines.
- Expanded Spells added to your list: 1st — Create or Destroy Water, Earth Tremor; 2nd — Dust Devil, Gust of Wind; 3rd — Erupting Earth, Tidal Wave; 4th — Stone Shape, Watery Sphere; 5th — Control Winds, Wall of Stone.
- Whispers of the Earth (1st): advantage on Survival checks and tremorsense in a 3 m radius.
- Leyline Manipulation: Troubled Roads (3rd): spend one Divination to influence an area within 9 m, radius up to 9 m, for 1 minute, with one effect:
  - Stable Footing: up to WIS-modifier creatures in the area ignore difficult terrain.
  - Shimmering Ice: the area is difficult terrain (ice); a creature entering or moving there makes a DEX save vs your spell save DC or falls prone. On water, it becomes solid ground for the duration.
  - Rushing Rapids: difficult terrain (tides); a creature entering for the first time makes a STR save vs your DC or is pushed 6 m straight back from the center.
  - Roaring Winds: difficult terrain (winds); creatures are deafened, have disadvantage on concentration checks, and must make a concentration check at the end of their turns if concentrating.
- Leyline Manipulation: Cleared Paths (6th): spend one Divination to influence an area radius up to 9 m for 1 minute:
  - Sacred Shoal: creatures making saves within gain a bonus equal to your WIS modifier.
  - Sanctified: at the start of their turn, creatures within gain temp HP = PB + WIS modifier.
  - Updraft: a creature in the area gains a flight speed equal to its movement, up to 18 m above the ground.
- Blessed Traveller (10th): difficult terrain doesn't impede you; you gain a climbing speed equal to your movement and can move on vertical surfaces hands-free.
- Gaia Aura (14th): use Leyline Manipulation centered on yourself, radius up to 6 m; you are unaffected by its negatives and may designate up to WIS-modifier creatures immune as well. The area moves with you.

## Astrologian — Subclass: Fortuneteller
Focus on the Deck of Sixty, supplemented by other methods; arts passed master-to-student.
- Minor Arcana (1st): when you use Divination, on a die result of 1/3/5 you may instead make a ranged spell attack dealing 1d6 + WIS modifier force damage to a creature within 9 m; on 2/4/6 you may heal 1d6 + WIS modifier HP to a creature within 9 m. Potency rises to 2d6 at 6th, 3d6 at 10th, 4d6 at 14th. You can't use both Divination and Minor Arcana in a single action.
- Twisting Fate (3rd): when you use Divination, roll 2d6 and choose which die is the true result.
- Horoscope (6th): use Time Dilation on your Divination or Minor Arcana; if you maintain concentration until your next turn you can change the result to one of your choice.
- Reversed Fortune (10th): when you use Divination you may apply a reversed divination to a creature — it makes a CHA save vs your spell save DC, suffering the effect for 1 minute on a failure (it may re-save as an action on its turn). Effects: 1 Cowardice (its damage reduced by 2d6 on its first attack each turn; 3d6 at 11th, 4d6 at 17th); 2 Frailty (damage it takes increased by 2d6 on the first attack against it until its next turn; 3d6 at 11th, 4d6 at 17th); 3 Apathy (only one attack action on its turn); 4 Wavering (its attack rolls -2 and a natural 20 isn't a crit); 5 Foolishness (disadvantage on saves vs spell effects); 6 Failure (disadvantage on attack rolls).
- Greater Divination (14th): as an action, use each of your card divination features — roll 6d6, select 3 results: two are added to your Spread and one may be used for Divination or Minor Arcana. Expends three uses of Divination. Once per short or long rest.

# BARD (Gridanian)
**Hit Die:** d8 | **Saving Throws:** Dexterity, Charisma | **Spellcasting:** Charisma (known)

**Flavor.** Nestled in the trees, a skilled bowmaster watches their mark wander the plains 100 yalms away and topples it with a single arrow. In the thick of battle, a fearless singer's magic-imbued voice ushers power to their allies. A careful hunter douses arrowheads in homemade poison. Gridanian Bards are a young but effective profession of the Black Shroud, beginning as archers who mix sword and song.
- Songs for the Souls: an originator was a disgraced commander who travelled singing to soothe the spirits of dead allies; the commemorative art found battlefield utility.
- Of Lyres and Lyrics: bards use instruments and voice to weave magical pieces that soothe wounds, fend off danger, and weaken foes.
- Creating a Bard: usually trained by a mentor (some self-taught). Consider whether you follow the old military/spirit-soothing purpose or wander free, weaving songs for the masses.

**HP_ref (d8):** 1:8 | 2:13 | 3:18 | 4:23 | 5:28 | 6:33 | 7:38 | 8:43 | 9:48 | 10:53 | 11:58 | 12:63 | 13:68 | 14:73 | 15:78 | 16:83 | 17:88 | 18:93 | 19:98 | 20:103. (Default PF = HP_ref[N] + CON mod x N.)

**Progression — spell slots per level**
| Lvl | PB | Spells Known | Features | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|---|---|
| 1 | +2 | — | Bardic Inspiration (d6), Fighting Style | — | — | — | — | — |
| 2 | +2 | 2 | Minstrel's Music, Spellcasting | 2 | — | — | — | — |
| 3 | +2 | 3 | Bardic Focus | 3 | — | — | — | — |
| 4 | +2 | 3 | Ability Score Improvement | 3 | — | — | — | — |
| 5 | +3 | 4 | Bardic Inspiration (d8), Extra Attack | 4 | 2 | — | — | — |
| 6 | +3 | 4 | Troubadour Training | 4 | 2 | — | — | — |
| 7 | +3 | 5 | Bardic Focus Feature | 4 | 3 | — | — | — |
| 8 | +3 | 5 | Ability Score Improvement | 4 | 3 | — | — | — |
| 9 | +4 | 6 | — | 4 | 3 | 2 | — | — |
| 10 | +4 | 6 | Bardic Inspiration (d10), Expertise, Unshakeable Performer | 4 | 3 | 2 | — | — |
| 11 | +4 | 7 | Bardic Focus Feature | 4 | 3 | 3 | — | — |
| 12 | +4 | 7 | Ability Score Improvement | 4 | 3 | 3 | — | — |
| 13 | +5 | 8 | — | 4 | 3 | 3 | 1 | — |
| 14 | +5 | 8 | Radiant Finale | 4 | 3 | 3 | 1 | — |
| 15 | +5 | 9 | Bardic Inspiration (d12), Bardic Focus Feature | 4 | 3 | 3 | 2 | — |
| 16 | +5 | 9 | Ability Score Improvement | 4 | 3 | 3 | 2 | — |
| 17 | +6 | 10 | — | 4 | 3 | 3 | 3 | 1 |
| 18 | +6 | 10 | Final Fantasia | 4 | 3 | 3 | 3 | 1 |
| 19 | +6 | 11 | Ability Score Improvement | 4 | 3 | 3 | 3 | 2 |
| 20 | +6 | 11 | Minstrel's Coda | 4 | 3 | 3 | 3 | 2 |

**Quick Build.** Dexterity highest, then Charisma. Entertainer background. Archery fighting style.

**Proficiencies.** Armor: Light. Weapons: simple weapons, longbows, longswords, rapiers, shortswords. Tools: three musical instruments of your choice. Saving Throws: Dexterity, Charisma. Skills: choose any three.
**Equipment.** A set of leather armor; (a) rapier or (b) two simple melee weapons; a longbow and 20 arrows; (a) an explorer's pack or (b) a scholar's pack; a musical instrument of your choice.

**Bardic Inspiration (1st).** Bonus action: choose one creature other than yourself within 18 m who can hear you; it gains one Bardic Inspiration die (d6). Within 10 minutes it can add the die to one ability check, attack roll, or saving throw (decide before the DM says success/fail). One die at a time. Uses = CHA modifier + PB, recovered on a long rest. Die grows: d8 at 5th, d10 at 10th, d12 at 15th.

**Fighting Style (1st).** Choose one (no option twice): Archery (+2 to ranged attack rolls); Defense (+1 AC while wearing armor); Dueling (+2 damage with a one-handed melee weapon and no other weapon); Two-Weapon Fighting (add ability modifier to the second attack's damage).

**Spellcasting (2nd).** Charisma. Spell save DC = 8 + PB + CHA mod; attack = PB + CHA mod. Spells Known per table; on level up you may replace one known spell. Focus: any instrument you are proficient with.

**Minstrel's Music (2nd).** As an action, expend a use of Bardic Inspiration and sing, affecting you and creatures who can hear you within 9 m. Maintain concentration (as a spell), up to 1 minute. Two songs:
- The Warden's Paean: when you or an allied creature takes damage, reduce it by your Bardic Inspiration die.
- Foe's Requiem: when you or an allied creature in range deals damage, as a reaction expend one Bardic Inspiration die and add the roll as bonus damage.

**Bardic Focus (subclass, 3rd).** Choose God's Quiver, Soul Voice, or Shadowpoint. Features at 3rd, 7th, 11th, 15th.
**Ability Score Improvement (4th, 8th, 12th, 16th, 19th).** +2 to one or +1 to two (max 20).
**Extra Attack (5th).** Attack twice when you take the Attack action.
**Troubadour Training (6th).** New songs:
- Army's Paeon: when you or an allied creature in range is targeted by an attack, as a reaction expend one Bardic Inspiration die and add the roll to that creature's AC for the attack.
- Wanderer's Minuet: when you or an allied creature starts its turn in range, its base speed increases by 3 m and it gains advantage on Dexterity saves until the start of its next turn.
**Unshakeable Performer (10th).** Advantage on Charisma saving throws.
**Radiant Finale (14th).** While a Minstrel's Music song is active, as an action add a stylized ending:
- Forte: a creature in range makes a CHA save vs your Bard save DC, taking 2d8 psychic damage and disadvantage on its next attack on a failure, or half damage and no effect on a success.
- Piano: a creature in range is healed 2d8 HP.
**Final Fantasia (18th).** When you use Minstrel's Music, choose two effects to apply to your song. Once per long rest.
**Minstrel's Coda (20th).** When you roll initiative with no Bardic Inspiration uses left, regain one use.

## Bard — Subclass: God Quiver
Marksmen who rely on accuracy, using song mainly to empower themselves.
- Straight Shot (3rd): when you roll a ranged weapon attack, expend a Bardic Inspiration die and add it to the attack roll; if the sum is 20 or higher, the attack becomes a critical hit.
- Hawkeye (7th): advantage on Perception checks relying on sight; the effective range of your ranged weapons increases by 15 m.
- Bardic Barrage (11th): when you take the Attack action to make a ranged weapon attack, as a bonus action make one additional attack. Uses = DEX modifier, recovered on a long rest.
- Misery's End (15th): when one of your attacks is a critical hit, it deals bonus damage equal to twice the weapon's damage die.

## Bard — Subclass: Soul Voice
Archers who lean into the magical power of song to empower allies.
- Soothing Songs (3rd): new Minstrel's Music options — Nature's Minne (at the start of your turn, you and all allied creatures recover 1d4 HP); Silent Nocturne (when a creature attempts to cast a spell with verbal components, as a reaction it makes a CHA save vs your Bard save DC or becomes unable to speak).
- Endless Performance (7th): as a bonus action, spend a spell slot and regain Bardic Inspiration uses equal to the slot's level.
- Mage's Ballad (11th): during a short rest, spend a Bardic Inspiration die and recover spell slots whose total level is <= the die result. Once; refreshes on a long rest.
- Battle Voice (15th): the effective range of your Minstrel's Music increases to an 18 m radius.

## Bard — Subclass: Shadowpoint
Bards who debilitate foes with homemade poisons delivered via weapons.
- Arrow Bites (3rd): proficiency with the poisoner's kit. As a bonus action, apply one dose to ten arrowheads or a single weapon (effective 1 minute). On a long rest, create a fresh batch (potent 24 hours) of bites equal to twice your PB; you know two poison types and decide the mix. A struck creature takes bonus 1d4 poison damage and makes a CON save vs your Bard save DC or suffers an effect by type:
  - Venomous Bite: poisoned, taking 1d4 poison at the start of its turn for 1 minute (may re-save as an action).
  - Wind Bite: poisoned, speed reduced by 3 m for 1 minute (may re-save as an action).
- Degenerative Toxicity (7th): resistance to poison damage; saves against your bite poisons have their DC increased by half your PB (round up).
- Advanced Toxins (11th): when creating a batch, combine two doses into one to make:
  - Caustic Bite: on-hit poison damage becomes 2d4; poisoned, taking 1d4 at start of turn and dealing 1d4 less damage (may re-save as an action).
  - Shadow Bite: poisoned and unable to speak for 1 minute (no re-save).
  - Storm Bite: poisoned and paralyzed (re-save at end of its turn).
- Fever Pitch (15th): a creature poisoned by caustic/shadow/storm bite becomes feverish — at the start of its turn it makes a WIS save vs your Bard save DC or is stunned until end of turn (success = immune 1 hour). Additionally, at the start of a poisoned creature's turn it takes 2d6 necrotic damage.

# BLACK MAGE
**Hit Die:** d6 | **Saving Throws:** Intelligence, Wisdom | **Spellcasting:** Intelligence (spellbook, prepared)

**Flavor.** A Lalafell levels a horde of kobolds with a fiery explosion from a gem-tipped staff. A dark-robed woman bends a guard's will with a few choice words. An Elezen laughs at the umbral hue of his fireball as a demonic servant chuckles beside him. A black mage wields forbidden magic of pure destructive force, their power rivaled only by their thirst for more.
- A Dark Past: black magic was born from a sorceress of unparalleled power; great power corrupts, setting its wielders on the path of ruin.
- Ties to the Void: to don the black, a mage researches the void — another plane from which they draw knowledge; most study via tomes, some tap the void directly.
- Creating a Black Mage: know why you pursue this power (ambition or curiosity) and where you began (a cult, a proper school, or a master's tutelage).

**HP_ref (d6):** 1:6 | 2:10 | 3:14 | 4:18 | 5:22 | 6:26 | 7:30 | 8:34 | 9:38 | 10:42 | 11:46 | 12:50 | 13:54 | 14:58 | 15:62 | 16:66 | 17:70 | 18:74 | 19:78 | 20:82. (Default PF = HP_ref[N] + CON mod x N.)

**Progression — spell slots per level**
| Lvl | PB | Mana | Cantrips | Features | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | +2 | 1 | 3 | Spellcasting, Manafont | 2 | — | — | — | — | — | — | — | — |
| 2 | +2 | 2 | 3 | Magical Discipline | 3 | — | — | — | — | — | — | — | — |
| 3 | +2 | 3 | 3 | — | 4 | 2 | — | — | — | — | — | — | — |
| 4 | +2 | 4 | 4 | Ability Score Improvement | 4 | 3 | — | — | — | — | — | — | — |
| 5 | +3 | 5 | 4 | — | 4 | 3 | 2 | — | — | — | — | — | — |
| 6 | +3 | 6 | 4 | Magical Discipline Feature | 4 | 3 | 3 | — | — | — | — | — | — |
| 7 | +3 | 7 | 4 | — | 4 | 3 | 3 | 1 | — | — | — | — | — |
| 8 | +3 | 8 | 4 | Ability Score Improvement | 4 | 3 | 3 | 2 | — | — | — | — | — |
| 9 | +4 | 9 | 4 | — | 4 | 3 | 3 | 3 | 1 | — | — | — | — |
| 10 | +4 | 10 | 5 | Magical Discipline Feature | 4 | 3 | 3 | 3 | 2 | — | — | — | — |
| 11 | +4 | 11 | 5 | — | 4 | 3 | 3 | 3 | 2 | 1 | — | — | — |
| 12 | +4 | 12 | 5 | Ability Score Improvement | 4 | 3 | 3 | 3 | 2 | 1 | — | — | — |
| 13 | +5 | 13 | 5 | — | 4 | 3 | 3 | 3 | 2 | 1 | 1 | — | — |
| 14 | +5 | 14 | 5 | Magical Discipline Feature | 4 | 3 | 3 | 3 | 2 | 1 | 1 | — | — |
| 15 | +5 | 15 | 5 | — | 4 | 3 | 3 | 3 | 2 | 1 | 1 | 1 | — |
| 16 | +5 | 16 | 5 | Ability Score Improvement | 4 | 3 | 3 | 3 | 2 | 1 | 1 | 1 | — |
| 17 | +6 | 17 | 5 | — | 4 | 3 | 3 | 3 | 2 | 1 | 1 | 1 | 1 |
| 18 | +6 | 18 | 5 | Surecaster | 4 | 3 | 3 | 3 | 3 | 1 | 1 | 1 | 1 |
| 19 | +6 | 19 | 5 | Ability Score Improvement | 4 | 3 | 3 | 3 | 3 | 2 | 1 | 1 | 1 |
| 20 | +6 | 20 | 5 | Resonating Aether | 4 | 3 | 3 | 3 | 3 | 2 | 2 | 1 | 1 |

**Quick Build.** Intelligence highest, then Constitution or Dexterity. Sage background. Mage Hand, Light, Ray of Frost cantrips; spellbook 1st-level: Burning Hands, Charm Person, Feather Fall, Mage Armor, Magic Missile, Sleep.

**Proficiencies.** Armor: none. Weapons: Daggers, Darts, Slings, Quarterstaffs, Maces, Light Crossbows. Tools: none. Saving Throws: Intelligence, Wisdom. Skills: choose two from Arcana, Deception, History, Insight, Intimidation, Persuasion, Religion.
**Equipment.** (a) a dagger or (b) a quarterstaff; (a) a light crossbow and 20 bolts or (a) a simple weapon; a spellcasting focus (cane, staff, wand, or similar); (a) an explorer's pack or (b) a scholar's pack; a spellbook.

**Spellcasting.** Intelligence. Spell save DC = 8 + PB + INT mod; attack = PB + INT mod.
- Cantrips: three at 1st level (more per table).
- Spellbook: starts with six 1st-level Black Mage spells.
- Preparing: prepare INT modifier + Black Mage level spells (min 1) from your spellbook, of levels you have slots for; change on a long rest.
- Ritual Casting: cast a Black Mage spell as a ritual if it has the ritual tag and is in your spellbook (need not be prepared).
- Your Spellbook: copying a found spell costs 2 hours and 50 gp per spell level; making a backup copy costs 1 hour and 10 gp per level.
- Learning Spells: each Black Mage level, add two Black Mage spells of your choice to your spellbook for free (of levels you have slots for).
- Focus: a rod, cane, wand, or similar.

**Manafont (1st).** You store magical energy as Mana points (Mana column; never exceed the table value; regained on a long rest).
- Leylines: when you cast a spell, residual mana creates a leyline. If you cast a spell last turn and have not moved or taken other actions this turn, you may spend mana points equal to that spell's level to cast an evocation spell of equal or lower level without a slot. Your turn immediately ends. No higher than 5th level this way.

**Magical Discipline (subclass, 2nd).** Choose Mhachi, Enchanter, or Void Mage. Features at 2nd, 6th, 10th, 14th.
**Ability Score Improvement (4th, 8th, 12th, 16th, 19th).** +2 to one or +1 to two (max 20).
**Surecaster (18th).** As a bonus action, expend 5 mana points to automatically pass all concentration checks for the next 10 minutes.
**Resonating Aether (20th).** Regain half your missing mana points when you roll initiative.

## Black Mage — Subclass: Mhachi
Mages of the destructive arts; creators of black magic.
- Expanded Spells: 1st — Chromatic Orb, Witch Bolt; 2nd — Aganazzar's Scorcher, Snilloc's Snowball Swarm; 3rd — Call Lightning, Sleet Storm; 4th — Ice Storm, Storm Sphere; 5th — Cone of Cold, Immolation.
- Unstable Aether (2nd): when you cast a spell, spend one mana point to reroll any damage die that rolled a 1 or 2; use the new rolls.
- Polyglot (6th): you can read all writing.
- Aetherial Manipulation (10th): your movement is no longer restricted when using Leylines (casting a Leylines spell still ends your turn). Additionally, if you expended a spell slot last turn, as a bonus action spend one mana point to teleport back to where you cast it (if unoccupied).
- Devastating Force (14th): when you roll a spell's damage and roll the maximum on any die, choose one such die, reroll it, and add it. Uses = INT modifier (min 1), recovered on a long rest.

## Black Mage — Subclass: Enchanter
Empower allies and weaken foes with charms and control.
- Expanded Spells: 1st — Bless, Cause Fear; 2nd — Enlarge/Reduce, Magic Weapon; 3rd — Slow, Haste; 4th — Blight, Charm Monster; 5th — Dominate Person, Hold Monster.
- Point of Influence (2nd): you may use Leylines for both enchantment and evocation spells.
- Silvered Tongue (6th): gain proficiency in one of Deception, Intimidation, or Persuasion (expertise if already proficient — double PB on that skill); you may use Intelligence as the ability for the chosen skill.
- Unshaken Will (10th): when you must make a Wisdom save, spend 1 mana point to gain advantage.
- Deep Influence (14th): when you cast an enchantment spell, spend 1 mana point to give the target disadvantage on its save.

## Black Mage — Subclass: Void Mage
Harness the Void and its dark creatures.
- Expanded Spells: 1st — Armor of Agathys, Arms of Hadar; 2nd — Ray of Enfeeblement, Shadow Blade; 3rd — Hunger of Hadar, Summon Lesser Demons; 4th — Banishment, Summon Greater Demon; 5th — Contact Other Plane (Ritual), Negative Energy Flood.
- Void Casting (2nd): when you cast a spell, spend one mana point to change its damage type to necrotic; doing so adds damage equal to your INT modifier once.
- Void Sense (6th): spend 1 mana point to gain darkvision out to 18 m for one hour (if you already have darkvision, its range increases by 18 m); you also gain advantage on Perception checks using your eyes while under this effect (your eyes glow dim red).
- Ebony Offense (10th): necrotic damage you deal ignores resistances. As a bonus action, spend a mana point to overcome necrotic immunity for your next spell.
- Bloody Veil (14th): when you kill a creature with a 1st-level-or-higher spell dealing necrotic damage, gain temp HP equal to the spell's level x your INT modifier.

# BLUE MAGE
**Hit Die:** d8 | **Saving Throws:** Dexterity, Intelligence | **Spellcasting:** varies by Azure Calling (Lore Keeper = INT, Fell Guard = WIS, Whalaqee = CHA)

**Flavor.** With a critical eye, the researcher records notes with perfect accuracy to complete their newest monstrous magic. Bathing in a dying beast's aether, the azure warrior comes to understand its nature and wield its strength. Speaking words of power, the cerulean shaman twists their spirit to unleash a griffon's gales. Blue Mages learn the magic of monsters through varied methods, able to adapt to nearly any role.
- The Souls of Beasts: the three renowned backgrounds are the Lore Keepers (catalogue monsters), the Fell Guard (absorb fallen foes' strength), and the Whalaqee tradition (twist one's aether to mimic monsters).
- The Well of Knowledge: a Blue Mage's greatest asset is rapidly discerning details about creatures and wielding those strengths.
- Creating a Blue Mage: usually taught by a mentor; ever curious, as that enterprising spirit is rewarded with greater power.
- DM NOTE (from the creator): the Blue Mage learns/steals spells from monsters rather than the traditional way. It is best experienced with the DM's buy-in to allow Monster Mimicries as rewards for defeating tough creatures or as research finds. Talk to your DM before playing this class.

**HP_ref (d8):** 1:8 | 2:13 | 3:18 | 4:23 | 5:28 | 6:33 | 7:38 | 8:43 | 9:48 | 10:53 | 11:58 | 12:63 | 13:68 | 14:73 | 15:78 | 16:83 | 17:88 | 18:93 | 19:98 | 20:103. (Default PF = HP_ref[N] + CON mod x N.)

**Progression — spell slots per level** (verbatim; this homebrew table's mid-level columns are intentionally irregular)
| Lvl | PB | Cantrips | Features | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | +2 | 3 | Azure Calling, Azure Lore, Libra | 2 | — | — | — | — | — | — | — | — |
| 2 | +2 | 3 | Deep Blue Heart | 3 | — | — | — | — | — | — | — | — |
| 3 | +2 | 3 | Azure Calling Feature | 4 | 2 | — | — | — | — | — | — | — |
| 4 | +2 | 4 | Ability Score Improvement | 4 | 3 | — | — | — | — | — | — | — |
| 5 | +3 | 4 | — | 4 | 3 | 2 | — | — | — | — | — | — |
| 6 | +3 | 4 | Azure Calling Feature | 4 | 3 | 3 | — | — | — | — | — | — |
| 7 | +3 | 4 | — | 4 | 3 | 3 | 1 | — | — | — | — | — |
| 8 | +3 | 4 | Ability Score Improvement | 4 | 3 | 3 | 2 | — | — | — | — | — |
| 9 | +4 | 4 | — | 4 | 3 | 3 | 2 | 1 | — | — | — | — |
| 10 | +4 | 5 | Azure Calling Feature | 4 | 3 | 3 | 2 | 2 | — | — | — | — |
| 11 | +4 | 5 | — | 4 | 3 | 3 | 2 | 3 | 1 | — | — | — |
| 12 | +4 | 5 | Ability Score Improvement | 4 | 3 | 3 | 2 | 3 | 1 | — | — | — |
| 13 | +5 | 5 | — | 4 | 3 | 3 | 2 | 3 | 1 | 1 | — | — |
| 14 | +5 | 5 | Azure Calling Feature | 4 | 3 | 3 | 2 | 3 | 1 | 1 | — | — |
| 15 | +5 | 5 | — | 4 | 3 | 3 | 2 | 3 | 1 | 1 | 1 | — |
| 16 | +5 | 5 | Ability Score Improvement | 4 | 3 | 3 | 2 | 3 | 1 | 1 | 1 | — |
| 17 | +6 | 5 | — | 4 | 3 | 3 | 2 | 3 | 1 | 1 | 1 | 1 |
| 18 | +6 | 5 | Azure Adaptation | 4 | 3 | 3 | 3 | 3 | 1 | 1 | 1 | 1 |
| 19 | +6 | 5 | Ability Score Improvement | 4 | 3 | 3 | 3 | 3 | 2 | 1 | 1 | 1 |
| 20 | +6 | 5 | Shifting Azure Soul | 4 | 3 | 3 | 3 | 3 | 2 | 2 | 1 | 1 |

**Quick Build.** Intelligence highest, then Constitution, then Dexterity. Lore Keeper Azure Calling. Sage background. Mage Hand, Light, Prestidigitation cantrips; research journal: Burning Hands, Frog's Legs, Mage Armor, Magic Missile, Ochu's Stench, Zu's Sonic Boom.

**Proficiencies.** Armor: Light. Weapons: Simple Weapons, Longswords, Scimitars, Shortswords. Tools: none. Saving Throws: Dexterity, Intelligence. Skills: choose two from Athletics, Animal Handling, Arcana, History, Intimidation, Nature, Perception, Survival.
**Equipment.** (a) a dagger or (b) a simple weapon; (a) a longsword or (b) scimitar; a cane spellcasting focus; a set of clothes; a components pouch; leather armour; (a) an explorer's pack or (b) a scholar's pack; a research journal.

**Azure Calling (subclass, 1st).** Choose Lore Keeper, Fell Guard, or Whalaqee. Grants features at 1st, 3rd, 6th, 10th, 14th, and sets your spellcasting ability (see below).

**Azure Lore (1st).** You gain spellcasting from your monster research. Spell save DC = 8 + PB + your ability modifier; attack = PB + ability modifier (the ability is set by your Azure Calling: Lore Keeper INT, Fell Guard WIS, Whalaqee CHA).
- Cantrips: know two at 1st level (more per Cantrips Known column).
- Research Journal: at 1st level it holds three monster mimicries recorded by you; at 1st level you start with six blue mage spells or monster mimicries of your choice. On level up, add a mix of two blue mage spells or mimicries (of levels you have slots for, or a mimicry you meet the prerequisite for).
- Using a monstrous mimicry that is not a passive enhancement counts as spellcasting; spending a spell slot to use a mimicry counts as casting a spell that uses a slot.
- Copying a monster link costs 2 hours and 50 gp per spell level (backup copy: 1 hour and 10 gp per level).
- Preparing: prepare spells/mimicries equal to your spellcasting modifier + Blue Mage level (min 1); attuning to a monster mimicry takes up two of these prepared slots. Change on a long rest.
- Ritual Casting: cast a blue mage spell as a ritual if it has the ritual tag and is in your journal.
- Focus: an arcane focus.
- The Hunt for Knowledge (DM guidance): mimicries can be granted as rewards for hard-fought battles with rare creatures, especially if Libra is used before/after the fight — even using spells outside the Blue Mage list.

**Libra (1st).** As an action, spend a 1st-level-or-higher spell slot, or spend 1 minute outside combat observing a creature (or its corpse), to learn whether it is your equal, superior, or inferior in two of your choice: Strength score, Dexterity score, Constitution score, Armor Class, current hit points, total class levels (if any).

**Deep Blue Heart (2nd).** When you finish a short rest, recover expended spell slots whose combined level is <= half your Blue Mage level (round up); none can be 6th level or higher.
**Ability Score Improvement (4th, 8th, 12th, 16th, 19th).** +2 to one or +1 to two (max 20).
**Azure Adaptation (18th).** On a long rest, choose one: Azure Scales (resistance to all damage except psychic); Draconic Wings (flying speed 18 m); Monstrous Vitality (when you expend a spell slot, recover HP = slot level + spellcasting modifier).
**Shifting Azure Soul (20th).** As a bonus action, change one of your monster mimicries to another.

## Blue Mage — Subclass: Lore Keeper (INT)
- Azure Knowledge (1st): learn two additional cantrips from the blue mage list (don't count against cantrips known).
- Focused Assessment (3rd): proficiency in Investigation (expertise if already proficient). You may use Libra as an action without spending a slot, and may now also learn: damage resistances, vulnerabilities, immunities.
- Quick Assessment (6th): as a bonus action, use Libra in combat on a creature within 9 m.
- Extracurricular Studies (10th): learn two spells of your choice from any class (5th level or lower, or a cantrip); they count as blue mage spells.
- Ace Tutor (14th): as an action, advise on a beast/monster within 9 m you have used Libra on; choose an ally within 18 m — until your next turn they have advantage on attack rolls against that creature.

## Blue Mage — Subclass: Fell Guard (WIS)
- Azure Guard (1st): use one-handed melee weapons as a spellcasting focus; gain proficiency with medium armour and martial weapons; HP maximum increases by 1, and by 1 again each level in this class.
- Monstrous Vanguard (3rd): choose a fighting focus — Colossus Slayer (when you hit a creature below its HP max with a weapon attack, +1d8 damage, once per turn); Giant Killer (when a creature within 1.5 m attacks you, reaction to make one weapon attack against it); Horde Breaker (once per turn, make another weapon attack vs a different creature within 1.5 m of the first and within range).
- Survival Tactics (6th): choose one — Escape the Horde (opportunity attacks against you have disadvantage); Multiattack Defense (when a creature hits you, +4 AC vs that creature's later attacks that turn); Steel Will (advantage on saves vs frightened).
- Azure Warrior (10th): on a long rest, choose acid/fire/cold/lightning/poison/necrotic/thunder; gain resistance to it and your weapon attacks deal bonus damage of that type equal to your PB.
- Absorb Ability (14th): as an action, touch a creature; it makes a CHA save vs your spell save DC or takes -2 to an ability score of your choice (you gain +2 to that score for 10 minutes); on a success it is immune for 1 minute. Failed attempts don't expend the use. Recharges on a long rest.

## Blue Mage — Subclass: Whalaqee (CHA)
Original creators of blue magic from "The New World."
- Mimic Blood (1st): +1 HP per level up; attune to an additional mimicry at 1st (doesn't count against prepared); gain one more additional mimicry at 3rd, 6th, 10th, 14th. You may also use Libra as an action without spending a slot, learning damage resistances, vulnerabilities, immunities.
- Misdirection (3rd): when hit by a melee attack, reaction to move 1.5 m back (no OAs) and reduce the damage by your CHA modifier. Uses = PB, recovered on a long rest.
- Protection of Monsters (6th): when you spend a slot to use a monstrous mimicry, gain temp HP = slot level + spellcasting modifier.
- Focus Mimicry (10th): bonus action; the next mimicry you use to deal damage or heal gains bonus equal to your spellcasting modifier.
- Masterful Mimicry (14th): when you expend a slot that increases a mimicry's range/area, creatures have disadvantage on saves against it.

## Blue Mage — Monstrous Mimicries
("#" = number of dice; scaling noted per entry. Spending a slot to use a mimicry counts as casting a spell.)
- **Adamantoise Shell** (Prereq: 3rd): while attuned, your AC becomes 17; DEX modifier doesn't affect it and you don't benefit from armor or a shield.
- **Ahriman's Gaze** (3rd): action, spend a slot; creatures that can see you in a 3 m cone make a WIS save vs your spell save DC or are paralyzed until the end of your next turn. +1.5 m cone per slot level above 1st.
- **Antlion's Antennae** (11th): gain 9 m tremorsense (detect vibrations through shared ground; not flying/incorporeal).
- **Archdemon's Abyssal Transfixion** (9th): action, spend a slot; a creature within 9 m makes a DEX save, taking #d12 piercing on a fail (half on success), # = twice the slot level. +3 m range per slot level above 1st.
- **Bandersnatch's Pounce** (7th): if you move at least 6 m straight toward a creature and hit it (melee weapon or spell) that turn, it makes a STR save vs your DC or is knocked prone; if prone, make one weapon attack as a bonus action.
- **Bat's Echolocation** (5th): while not deafened, you have blindsight up to 9 m.
- **Behemoth's Ecliptic Meteor** (11th): action, expend a 5th-level-or-higher slot; creatures within a 12 m radius sphere around you make a DEX save, taking #d12 force on a fail (half on success), # = twice the slot level. Full cover = no damage. +3 m radius per slot level above 5th.
- **Bomb's Detonation** (5th): action, spend a slot; creatures within a 6 m radius around you make a DEX save, #d10 fire (half on success), # = twice the slot level. +1.5 m radius per slot level above 3rd.
- **Cactuar's 1000 Needles** (None): reaction when hit by a melee weapon attack; creatures in a 1.5 m radius make a DEX save vs your spell save DC, taking 1d10 piercing (half on success); failures are poisoned for 1 minute (a creature poisoned this way can't make opportunity attacks).
- **Chocobo's Meteor** (7th): action, spend a slot; drop aether at a point within 36 m, exploding in a 6 m radius sphere; DEX save, #d10 force (half on success), # = twice the slot level. +1.5 m radius per slot level above 4th.
- **Chocobo's Rush** (3rd): use the Dash action as a bonus action.
- **Coeurl's Blaster** (5th): action, spend a slot; 9 m cone, DEX save, #d8 lightning (half on success), # = twice the slot level. +1.5 m cone per slot level above 3rd.
- **Crab's Grab** (None): when you use the Attack action to grapple a creature your size or smaller, advantage on the Strength (Athletics) check.
- **Demon Wall's Repel** (7th): action, spend a slot; a creature within 9 m makes a STR save vs your DC, #d8 thunder and pushed 9 m straight back on a fail (# = twice the slot level), half damage and pushed 3 m on a success if Large or smaller. +1.5 m push per slot level above 3rd.
- **Drake's Flame Breath** (3rd): action, spend a slot; 4.5 m cone, DEX save, #d6 fire (half on success), # = the slot level. +1.5 m cone per slot level above 1st.
- **Elbst's Water Bomb** (3rd): action, spend a slot; a sphere within 18 m explodes in a 6 m radius; CON save, #d8 cold (half on success), # = twice the slot level. +3 m landing range per slot level above 3rd.
- **Flan's Elemental Consumption** (5th): reaction when hit; spend a slot of any level to gain resistance to that damage type until the start of your next turn; for 1 minute, your next attack deals bonus #d6 of that type, # = twice the slot level.
- **Frog's Legs** (None): long jump up to 6 m, high jump up to 3 m, with or without a run; no fall damage from your own jumps.
- **Goblin's Operations** (3rd): proficiency in Sleight of Hand and Stealth.
- **Gremlin's Tongue** (None): you can cast Vicious Mockery; gain proficiency in Deception.
- **Griffon's Alpine Draft** (5th): action, spend a slot; a 30 m line; STR save, #d8 thunder + #d8 slashing on a fail, # = the slot level. +3 m length per slot level above 3rd; with a 7th-level-or-higher slot, also +1.5 m width each side. Snuffs open flames and dissipates fog/mist in the area.
- **Luminary's Aetheric Mimicry** (5th): on a long rest, choose until next long rest — Aether of Power (weapon attacks +PB damage); Aether of Health (+PB to HP you restore); Aether of Resilience (reaction to reduce damage you take by PB).
- **Mandragora's Shriek** (None): action or reaction after being hit; creatures within 6 m that can hear you make a CHA save vs your spell save DC or become deafened and frightened for 1 minute (re-save at end of turn; resisting = immune to your frighten for 1 hour).
- **Mantis' Claws** (5th): attack twice instead of once when you take the Attack action.
- **Mimic's Nature** (3rd): cast Disguise Self at will, without a slot or components.
- **Mindflayer's Blast** (11th): action, expend a 5th-level-or-higher slot; 4.5 m cone, INT save; fail = stunned 1 minute and #d8 psychic (# = the slot level); success = half, no stun (re-save as an action).
- **Minotaur's Recall** (3rd): perfectly recall any path you have travelled since attuning.
- **Moogle's Pom Cure** (None): healing pool = your Blue Mage level x 5 (refreshes on a long rest); as an action, restore HP to a creature within 9 m from the pool.
- **Morbol's Bad Breath** (9th): action, spend a slot; 9 m cone, CON save, #d6 poison and paralyzed 1 minute on a fail (# = twice the slot level); success = half, no paralyze. +3 m cone per slot level above 5th.
- **Namazu's Tingle** (3rd): use your spell attack bonus for melee attack rolls; your melee weapon attacks deal bonus damage = spellcasting modifier (instead of STR/DEX).
- **Ochu's Stench** (None): when a creature enters or starts its turn within 1.5 m of you, it makes a CON save vs your spell save DC or is poisoned until the start of its next turn.
- **Opo-opo's Agility** (None): proficiency in Athletics and Acrobatics.
- **Owl's Predation** (None): advantage on Wisdom (Perception) checks relying on hearing or sight.
- **Queen Hawk's Avail** (7th): action; you and a willing creature form a bond while within 6 m of each other — you take half damage from all sources and the bonded creature takes the other half.
- **Sahagin's Gills** (5th): breathe air and water; swim speed equal to your movement.
- **Shark's Blood Frenzy** (11th): advantage on melee attacks against any creature not at full HP.
- **Spider's Climb** (3rd): climb difficult surfaces, including ceilings, without a check.
- **Succubus' Eyes** (7th): see in darkness (magical and nonmagical) to 18 m; advantage on saves against charms.
- **Tonberry's Grudge** (9th): when you hit a stunned or paralyzed creature with a melee weapon, bonus damage = the average of the weapon's damage die.
- **Undead's Touch** (None): unarmed strikes use your spell attack bonus and deal 1d6 + spellcasting modifier necrotic; a creature you damage can't be healed until the end of your next turn.
- **Wamoura's Exuviation** (5th): action, spend a slot; a 6 m sphere heals allies for HP = the slot level; with a 5th-level-or-higher slot, allies also recover from blinded, deafened, paralyzed, or poisoned.
- **Wolf's Tactics** (7th): advantage on an attack against a creature if at least one ally is within 1.5 m of it and not incapacitated.
- **Zu's Sonic Boom** (None): action or bonus action, ranged spell attack vs a creature within 9 m for 2d4 + spellcasting modifier thunder (once per turn as action or bonus action). At 5th level you may use it as both your action and bonus action. Spend a slot to gain advantage and bonus #d4, # = twice the slot level.
- **Creating Mimicries (DM guidance):** attacks scale at 2 damage dice per slot level; choose a die by area size and consider range scaling. Always get DM approval.

# DANCER
**Hit Die:** d8 | **Saving Throws:** Dexterity, Charisma | **Spellcasting:** Charisma (prepared, half-caster)

**Flavor.** The spotlights focus on a lightly dressed performer who moves effortlessly with the music, filling hearts with joy and determination. Amid the battlefield, a maiden slides in and out of combat, soothing allies' wounds and empowering their wills. A seemingly sweet woman dances through would-be assailants, cutting them down with her signature scimitar. Dancers combine magic and art into a spectacle that turns the battlefield into a show, guiding their allies to a happy conclusion.
- Of Silk and Steel: Dancers use small weapons to pick at foes while their dances debilitate marks and empower allies.
- Ornaments of Power: they cast not through staves but specially made jewelry worn on wrists and ankles, moving in patterns to gather residual magic; they must keep moving to keep a spell active.
- Creating a Dancer: consider where you honed your craft (self-taught or under a mentor) and your motivation (fame, joy for the masses, or mastery).

**HP_ref (d8):** 1:8 | 2:13 | 3:18 | 4:23 | 5:28 | 6:33 | 7:38 | 8:43 | 9:48 | 10:53 | 11:58 | 12:63 | 13:68 | 14:73 | 15:78 | 16:83 | 17:88 | 18:93 | 19:98 | 20:103. (Default PF = HP_ref[N] + CON mod x N.)

**Progression — spell slots per level**
| Lvl | PB | Flourish | Features | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|---|---|
| 1 | +2 | 1d6 | Dazzling Dance, Flourish | — | — | — | — | — |
| 2 | +2 | 1d6 | Spellcasting, Whirling Steel | 2 | — | — | — | — |
| 3 | +2 | 2d6 | Dancer Archetype | 3 | — | — | — | — |
| 4 | +2 | 2d6 | Ability Score Improvement | 3 | — | — | — | — |
| 5 | +3 | 3d6 | Uncanny Dodge | 4 | 2 | — | — | — |
| 6 | +3 | 3d6 | Dancer Archetype Feature | 4 | 2 | — | — | — |
| 7 | +3 | 4d6 | Evasion | 4 | 3 | — | — | — |
| 8 | +3 | 4d6 | Ability Score Improvement | 4 | 3 | — | — | — |
| 9 | +4 | 5d6 | — | 4 | 3 | 2 | — | — |
| 10 | +4 | 5d6 | Motivating Mambo | 4 | 3 | 2 | — | — |
| 11 | +4 | 6d6 | Dancer Archetype Feature | 4 | 3 | 3 | — | — |
| 12 | +4 | 6d6 | Ability Score Improvement | 4 | 3 | 3 | — | — |
| 13 | +5 | 7d6 | Bewildering Grace | 4 | 3 | 3 | 1 | — |
| 14 | +5 | 7d6 | Spell Dancer | 4 | 3 | 3 | 1 | — |
| 15 | +5 | 8d6 | Dancer Archetype Feature | 4 | 3 | 3 | 2 | — |
| 16 | +5 | 8d6 | Ability Score Improvement | 4 | 3 | 3 | 2 | — |
| 17 | +6 | 9d6 | — | 4 | 3 | 3 | 3 | 1 |
| 18 | +6 | 9d6 | Stage Presence | 4 | 3 | 3 | 3 | 1 |
| 19 | +6 | 10d6 | Ability Score Improvement | 4 | 3 | 3 | 3 | 2 |
| 20 | +6 | 10d6 | Rhythmic Heart | 4 | 3 | 3 | 3 | 2 |

**Quick Build.** Dexterity highest, then Charisma. Entertainer background.

**Proficiencies.** Armor: Light. Weapons: Chakrams, Rapiers, Scimitars, Short Swords, Simple Weapons, Whips. Tools: none. Saving Throws: Dexterity, Charisma. Skills: choose two from Acrobatics, Deception, Insight, Perception, Performance, Persuasion.
**Equipment.** (a) two daggers or (b) two chakrams; (a) whip or (b) scimitar; a set of bracelets and anklets for spellcasting; a set of clothes; (a) a costume or (b) light armour; (a) an explorer's pack or (b) an entertainer's pack.
- Chakrams: suggested to use the Handaxe statblock, cost 15 gp, with the Finesse quality.

**Dazzling Dance (1st).** When you use the Attack action against a hostile creature, gain a Dazzling Dance charge (max = CHA modifier; charges dissipate 1 minute after combat). Spend 1 charge to take the Dash or Disengage action as a bonus action.
**Flourish (1st).** Once per turn, deal extra 1d6 damage to a creature you hit with a ranged weapon attack if you have advantage (or if another enemy of the target is within 1.5 m, isn't incapacitated, and you don't have disadvantage). Must use a finesse weapon. Damage scales per the Flourish column.
**Unarmoured Defense.** While not wearing armor, AC = 10 + DEX modifier + CHA modifier. You can use a shield and still gain this benefit.

**Spellcasting (2nd).** Charisma. Spell save DC = 8 + PB + CHA mod; attack = PB + CHA mod. Prepare CHA modifier + half Dancer level (round down, min 1).
- Dance Magic: you ignore the verbal component of Dancer spells, but must spend 3 m of movement (alongside the slot) to cast or maintain a spell. Any effect that drops your speed to 0 blocks your spells (instead of Silence).
- Focus: bangles, anklets, or gem-inlaid jewelry.
**Whirling Steel (2nd).** Spend 1 hour attuning up to two finesse throwing weapons; a thrown attuned weapon returns to your hand after the attack.
**Dancer Archetype (3rd).** Choose Paragon, Peace Bringer, or Exotic Wonder. Features at 3rd, 6th, 11th, 15th.
**Ability Score Improvement (4th, 8th, 12th, 16th, 19th).** +2 to one or +1 to two (max 20).
**Uncanny Dodge (5th).** When an attacker you can see hits you, reaction to halve the damage.
**Evasion (7th).** On a DEX save for half damage, take none on success and half on failure.
**Motivating Mambo (10th).** When you use the Help action, spend 1 Dazzling Dance charge to add your CHA modifier to their roll. Also, spend 1 charge to use Help as a bonus action.
**Bewildering Grace (13th).** As an action, perform an unpredictable dance: roll a d20 and resolve the effect (spells cast this way use no slot; non-spell effects last 1 hour). Uses = CHA modifier (min 1), recovered on a long rest.
**Spell Dancer (14th).** When you cast a spell, gain Dazzling Dance charges = half the expended slot's level (round down). Not from Bewildering Grace.
**Stage Presence (18th).** Attackers can't attack you with advantage unless you are grappled, incapacitated, paralyzed, or petrified. Standing from prone costs only 1.5 m of movement.
**Rhythmic Heart (20th).** When you roll initiative, gain 2 Dazzling Dance charges.

*Bewildering Grace Effects (d20):*
- 1: cast Banishment on yourself (can't end early; return where you were at the end).
- 2: become petrified for one round of combat.
- 3: lights and small magical explosions surround you. Nothing happens.
- 4: creatures within a 6 m radius centered on you make a DEX save vs your spell save DC or are knocked prone (you are excluded).
- 5: creatures within 6 m make a WIS save or are blinded (re-save at end of each turn; you excluded).
- 6: creatures within 6 m make a CON save or are poisoned (re-save at end of each turn; you excluded).
- 7: cast Faerie Fire centered on you (you excluded).
- 8-9: cast Cause Fear on an ally within range.
- 10-11: cast Hold Person.
- 12: cast Mass Healing Word.
- 13: select a creature within 9 m; it makes a CON save vs your spell DC or gains a level of exhaustion.
- 14-15: you gain the maximum number of Dazzling Dance charges possible.
- 16-17: cast Mass Cure Wounds.
- 18-19: cast Heal.
- 20: cast Reverse Gravity.
- (Source note: additional effects appear OCR-detached without a clear die mapping — Invisibility, Magic Weapon, Insect Plague, Otto's Irresistible Dance, Mordenkainen's Sword. Mapping unverifiable; flagged, not invented.)

## Dancer — Subclass: Paragon
A purist of dance as an art form.
- Inspiring Salsa (3rd): as a bonus action, spend up to 2 Dazzling Dance charges to inspire an ally within 1.5 m; they add a bonus to one attack roll/save/ability check equal to twice the charges spent. At 10th level you may spend any number of charges this way.
- Magic of Movement (6th): when you cast a spell, you may spend Dazzling Dance charges equal to the spell level instead of a slot. Such casts don't generate charges.
- Improvised Flow (11th): when you make a concentration check, spend a Dazzling Dance charge to roll with advantage.
- Forte Fusion (15th): cast a second concentration spell without ending the first — use your action to spend 1 charge plus the required slot. Each turn you maintain the second spell, use your action to spend 1 charge and 3 m of movement per spell.

## Dancer — Subclass: Peace Bringer
Wields restorative spells while dancing.
- Succor Swing (3rd): healing pool = Dancer level x 5 (refreshes on a long rest); as an action, perform for a creature within 1.5 m to restore HP from the pool.
- Refreshing Round (6th): when you use Succor Swing, you may target any number of creatures within 3 m.
- Safe Haven Hop (11th): select Aura of Life, Aura of Purity, or Aura of Vitality and cast it without a slot. Uses = half CHA modifier (round down, min 1), recovered on a long rest.
- The Solace Swing (15th): spend Dazzling Dance charges to restore your healing pool; each point spent recovers pool points equal to your CHA modifier.

## Dancer — Subclass: Exotic Wonder
Incorporates weapons into the dance.
- Flourishing Swing (3rd): your melee weapon attacks with finesse weapons activate Flourish.
- Fighting Style (3rd): choose Defense (+1 AC in armor); Dueling (+2 damage one-handed, no other weapon); Fleet Foot (+1.5 m movement speed); Two-Weapon Fighting (add ability modifier to the second attack's damage).
- Double Step (6th): when you take the Attack action, spend 1 Dazzling Dance charge to make an extra melee weapon attack.
- Flawless Flow (11th): make a melee weapon attack as a bonus action after casting a spell.
- Lamia Bite (15th): spend 4 Dazzling Dance charges before a weapon attack to lower your critical hit threshold by 4 for the rest of the turn.

# DARK KNIGHT
**Hit Die:** d10 | **Saving Throws:** Constitution, Charisma | **Resource:** Well of Darkness (CHA-based)

**Flavor.** An Auri man cleaves through foe after foe, the enemy claiming they battled a demon. A downtrodden woman shelters behind an ebony-clad Hyur who pulls greater strength from exhaustion to protect the weak. A Lalafell weaves shadow magics to end a demon and silently protect a village. A dark knight is unconcerned with what is lawful, concerned with what is ethical; tyrants best prepare for one who aims to break the chains of oppressors.
- Protecting the Meek: they serve no lords, protecting commonfolk from banditry, beasts, and corrupt oppressors; supported by those they protect or by bounty hunting.
- Internal Darkness: they sacrifice their own life force to power a well of darkness, causing themselves pain and exhaustion to harness dark power.
- Creating a Dark Knight: they live outside the law and expect to be demonized by history rather than celebrated like Paladins. One must be introduced via an ancient tome or a mentor.

**HP_ref (d10):** 1:10 | 2:16 | 3:22 | 4:28 | 5:34 | 6:40 | 7:46 | 8:52 | 9:58 | 10:64 | 11:70 | 12:76 | 13:82 | 14:88 | 15:94 | 16:100 | 17:106 | 18:112 | 19:118 | 20:124. (Default PF = HP_ref[N] + CON mod x N.)

**Progression**
| Lvl | PB | WoD Points | Darkside Dmg | Features |
|---|---|---|---|---|
| 1 | +2 | 1 | 1d6 | Well of Darkness, Darkside |
| 2 | +2 | 2 | 1d6 | Fighting Style, Burning Blood |
| 3 | +2 | 3 | 1d6 | Dark Knight Archetype |
| 4 | +2 | 4 | 1d6 | Ability Score Improvement |
| 5 | +3 | 5 | 1d8 | Extra Attack |
| 6 | +3 | 6 | 1d8 | Archetype Feature |
| 7 | +3 | 7 | 1d8 | The Blackest Night |
| 8 | +3 | 8 | 1d8 | Ability Score Improvement |
| 9 | +4 | 9 | 1d8 | Fight or Flight |
| 10 | +4 | 10 | 1d8 | Curse of the Abyss |
| 11 | +4 | 11 | 1d10 | Archetype Feature |
| 12 | +4 | 12 | 1d10 | Ability Score Improvement |
| 13 | +5 | 13 | 1d10 | Abyssal Communion |
| 14 | +5 | 14 | 1d10 | Quietus |
| 15 | +5 | 15 | 1d10 | Dark Mind |
| 16 | +5 | 16 | 1d10 | Ability Score Improvement |
| 17 | +6 | 17 | 1d12 | Archetype Feature |
| 18 | +6 | 18 | 1d12 | Stalwart Soul |
| 19 | +6 | 19 | 1d12 | Ability Score Improvement |
| 20 | +6 | 20 | 1d12 | Living Dead |

**Quick Build.** Strength highest, then Charisma. Folk Hero background.

**Proficiencies.** Armor: All Armor, shields. Weapons: Simple and Martial Weapons. Tools: none. Saving Throws: Constitution, Charisma. Skills: choose two from Athletics, Arcana, History, Insight, Intimidation, Perception, Survival.
**Equipment.** (a) chain mail or (b) hide armour; (a) a martial weapon and a shield or (b) two martial weapons; (a) a short bow and 20 arrows or (b) two daggers; (a) an explorer's pack or (b) a dungeoneer's pack.

**Well of Darkness (1st).** You have Well of Darkness points (WoD column), regained on a long rest. Dark Knight Spell DC = 8 + PB + CHA modifier; Dark Knight Spell Attack = PB + CHA modifier.
**Darkside (1st).** As a bonus action, spend 1 WoD point to enter Darkside for rounds equal to your CHA modifier; melee weapon attacks deal additional necrotic damage per the Darkside Dmg column.
**Fighting Style (2nd).** Choose Defense / Dueling / Great Weapon Fighting / Protection / Two-Weapon Fighting (standard wording).
**Burning Blood (2nd).** As a bonus action, expend one Hit Die and roll it; recover that many WoD points (cannot exceed max).
**Dark Knight Archetype (3rd).** Choose Blackblood, Abyss Knight, or Dark Magus. Features at 3rd, 6th, 11th, 17th.
**Ability Score Improvement (4th, 8th, 12th, 16th, 19th).** +2 to one or +1 to two (max 20).
**Extra Attack (5th).** Attack twice when you take the Attack action.
**The Blackest Night (7th).** As a bonus action, expend one Hit Die to shield yourself or a creature within 9 m; the target gains temp HP = die result + your CHA modifier.
**Fight or Flight (9th).** Spend 2 WoD points to cast Cause Fear or Compelled Duel.
**Curse of the Abyss (10th).** Bonus action to curse a creature for 1 minute (ends if it dies, you die, or are incapacitated): +PB damage vs the cursed target; your attacks crit on 19-20 vs it; if it dies, regain HP = Dark Knight level + CHA modifier (min 1) and 1 WoD point. Long rest to reuse.
**Abyssal Communion (13th).** Spend 6 WoD points to cast Rary's Telepathic Bond.
**Quietus (14th).** As an action, spend 2 WoD points to make a melee weapon attack against all creatures within 3 m; you may expend one Hit Die and roll it to add that much necrotic damage to all targets.
**Dark Mind (15th).** Proficiency in Wisdom saving throws.
**Stalwart Soul (18th).** At the start of each of your turns, if at half HP or less (and not at 0), regain HP = 5 + CON modifier.
**Living Dead (20th).** When reduced to 0 HP but not killed outright, instead of being incapacitated, expend one Hit Die and recover HP = die result + CON modifier.

## Dark Knight — Subclass: Blackblood
Martial power infused with inner darkness.
- Plunge (3rd): bonus action, spend 1 WoD point to jump to an unoccupied space beside a target within 6 m (clearing obstacles/creatures up to 3 m tall, no OAs); on landing, make a melee weapon attack against it.
- Piercing Intimidation (6th): on an Intimidation check, spend 1 WoD point to roll your Darkside damage die and add it to the check.
- Soul Eater (11th): once per turn on a melee weapon attack, recover HP = half the Darkside bonus damage dealt (round down).
- Ravaging Darkness (17th): add your CHA modifier to the Darkside bonus damage.

## Dark Knight — Subclass: Abyss Knight
Grows stronger the more dire the situation.
- Dark Burst (3rd): while in Darkside, as an action spend 2d4 HP to cast Burning Hands dealing necrotic instead of fire (no ignition; uses Well of Darkness DC). Increase the spell level by taking +1d4 self-damage per level, up to CHA modifier levels.
- Adversity (6th): for every 20 HP you are missing, +1 to attack and damage rolls (max = CHA modifier). Also resistance to necrotic damage.
- Supernatural Sense (11th): cast Detect Good and Evil at will; cast Detect Thoughts at will on a willing creature, or spend 2 WoD points on an unwilling one.
- Dark Star (17th): all damage you take is reduced by your current Adversity bonus. When you cast Burning Hands via Dark Burst, deal bonus damage = CHA modifier + Adversity bonus, and may change the 4.5 m cone to a 9 m line. (Adversity is referenced after spending HP for Dark Burst.)

## Dark Knight — Subclass: Dark Magus
Converts life force into Dark Arts.
- At 3rd level know two Dark Arts (one more at 6th, 11th, 17th). Know the Toll the Dead cantrip; your max WoD points increases by your CHA modifier.
- Casting Dark Arts: cast using normal casting time/rules but no material components. From 6th level, spend additional WoD points to raise a Dark Art's level (if it has a higher-level effect): +1 level per extra WoD point. Default cast at lowest level.
- Spells and Well of Darkness Points (max points per spell): 6th-8th = 4; 9th-12th = 5; 13th-16th = 6; 17th-20th = 7.
- Dark Arts list: Abyssal Drain (17th, 6 pts) = Contagion; Creeping Darkness (2 pts) = Darkness; Damning Curse (1 pt) = Bane; Dark Dance (2 pts) = Mirror Image; Dark Passenger (11th, 3 pts) = Lightning Bolt (necrotic); Delirium (2 pts) = Suggestion; Edge of Shadow (2 pts) = Shatter; Flood of Darkness (17th, 6 pts) = Negative Energy Flood; Helter Skelter (11th, 4 pts) = Hypnotic Pattern; Power Slash (6th, 3 pts) = Elemental Weapon; Reprisal (2 pts) = Hellish Rebuke; Salted Earth (6th, 3 pts) = Hunger of Hadar; Scourge (1 pt) = Hex; Shadow Skin (11th, 4 pts) = Shadow of Moil; Shadow Wall (17th, 6 pts) = Wall of Force; Syphon Touch (6th, 3 pts) = Vampiric Touch; Unleash (1 pt) = Arms of Hadar; Unmend (1 pt) = Magic Missile.

# DRAGOON
**Hit Die:** d10 | **Saving Throws:** Strength, Dexterity | **Resource:** Dragoon Trance / draconic blood charges

**Flavor.** A seasoned warrior leaps high and crashes down on a beast, driving it to the ground lance-first. Donned in dragon-hide scale mail, a Dragoon whirls their spear and unleashes a plume of dragon's fire. Lightly armored, another takes to the sky on spectral wings. These fearless warriors stand against dragons, demons, and fiends, commanding both sky and ground.
- Dragon's Bane: born of a homeland locked in a centuries-long war with dragonkind; renowned for their jumping, powered by a magical gem received upon completing basic training.
- Master of the Sky: they crash down from the sky to drive skyborn foes into the ground.
- Creating a Dragoon: consider aptitude, heritage, or legend that drew them in, and whether they hunt a specific dragon or simply wander.

**HP_ref (d10):** 1:10 | 2:16 | 3:22 | 4:28 | 5:34 | 6:40 | 7:46 | 8:52 | 9:58 | 10:64 | 11:70 | 12:76 | 13:82 | 14:88 | 15:94 | 16:100 | 17:106 | 18:112 | 19:118 | 20:124. (Default PF = HP_ref[N] + CON mod x N.)

**Progression**
| Lvl | PB | Trances | Features |
|---|---|---|---|
| 1 | +2 | 2 | Dragoon Trance, Jump |
| 2 | +2 | 2 | Fighting Style, Lancet |
| 3 | +2 | 3 | Dragoon Archetype |
| 4 | +2 | 3 | Ability Score Improvement |
| 5 | +3 | 3 | Extra Attack |
| 6 | +3 | 4 | Stall, True Thrust |
| 7 | +3 | 4 | Archetype Feature, Heavy Thrust |
| 8 | +3 | 4 | Ability Score Improvement |
| 9 | +4 | 4 | Life of the Dragon |
| 10 | +4 | 4 | High Jump, Wing Clipper |
| 11 | +4 | 4 | Archetype Feature |
| 12 | +4 | 5 | Ability Score Improvement |
| 13 | +5 | 5 | Fang and Claw |
| 14 | +5 | 5 | Heavy Impact |
| 15 | +5 | 5 | Archetype Feature |
| 16 | +5 | 5 | Ability Score Improvement |
| 17 | +6 | 6 | Invigorate |
| 18 | +6 | 6 | Battle Litany |
| 19 | +6 | 6 | Ability Score Improvement |
| 20 | +6 | 6 | Dragon Blooded |

**Quick Build.** Strength highest, then Wisdom. Soldier background.

**Proficiencies.** Armor: Light and Medium armour, shields. Weapons: Simple and Martial Weapons. Tools: none. Saving Throws: Strength, Dexterity. Skills: choose two from Animal Handling, Athletics, Acrobatics, History, Nature, Perception, Religion, Survival.
**Equipment.** (a) scale mail or (b) leather armor; (a) a martial weapon or (b) two spears; (a) a short bow and 20 arrows or (b) two hand axes; (a) an explorer's pack or (b) a dungeoneer's pack; a blessed Dragoon's Stone.

**Dragoon Trance (1st).** As a bonus action, enter a trance: while in it, your long jump is up to 9 m and high jump up to 4.5 m (with or without a run); no fall damage from your own jumps; if your racial base speed is below 9 m, it is set to 9 m. On entering, gain draconic blood charges = PB + WIS modifier (these persist until you re-enter the trance or finish a long rest). Dragoon DC = 8 + PB + STR modifier. The trance lasts 10 minutes (ends early if knocked unconscious or as a bonus action). If you have a draconic blood charge while not in a trance, as a bonus action gain the trance's effect until end of turn. Uses per the Trances column; long rest to recover.
**Jump (1st).** If you jump at least 4.5 m as part of your movement while wielding a melee weapon, use your action to crash down on a creature: it makes a DEX save or is knocked prone and takes damage equal to your weapon's damage (half and not prone on a success); you land in an adjacent unoccupied space. At 5th level, Jump damage is doubled.
**Fighting Style (2nd).** Choose Archery / Defense / Dueling / Great Weapon Fighting / Protection / Two-Weapon Fighting (standard wording). (Note: 5e jump distance is capped by movement speed; several Dragoon features address this.)
**Lancet (2nd).** When you land a melee weapon attack, expend a draconic blood charge to recover HP = half the weapon attack's damage (round up).
**Dragoon Archetype (3rd).** Choose Slayer, Dragon Heart, or Valkyrie. Features at 3rd, 7th, 11th, 15th.
**Ability Score Improvement (4th, 8th, 12th, 16th, 19th).** +2 to one or +1 to two (max 20).
**Extra Attack (5th).** Attack twice when you take the Attack action.
**Stall (6th).** While in a trance, at the peak of any jump you may pause in place until the end of your next turn (acting normally while suspended; on your next turn you may move as though jumping when coming down). Usable once per landing.
**True Thrust (6th).** Bonus action, spend one draconic blood charge to add your WIS modifier to your attack rolls until the end of your next turn.
**Heavy Thrust (7th).** Bonus action, spend one draconic blood charge to add your WIS modifier to your weapon damage rolls until the end of your next turn.
**Life of the Dragon (9th).** Permanently: long jump up to 9 m, high jump up to 4.5 m at all times. While in a trance: long jump max 27 m, high jump max 18 m; you may Dash as a bonus action.
**High Jump (10th).** If you used Stall last turn and jump at least 9 m while wielding a melee weapon, use your action to crash down: the creature makes a DEX save (with disadvantage) or is knocked prone and takes quadruple your weapon's damage (half and not prone on success); land in an adjacent space.
**Wing Clipper (10th).** When a creature fails its save vs your Jump attack and has a flying speed, its flying speed becomes 0; it must use an action to re-save vs your Dragoon DC to regain flight.
**Fang and Claw (13th).** While in a trance, make a melee weapon attack as a bonus action.
**Heavy Impact (14th).** When using a jump attack, spend one draconic blood charge so each creature within 3 m of the target is also affected by the jump attack.
**Invigorate (17th).** When you fail a save, reroll it (use the new number). Uses = WIS modifier, recovered on a long rest.
**Battle Litany (18th).** While in a trance, as a bonus action your and allies' (within 3 m) melee weapon attacks crit on 19-20 for rounds equal to half your STR modifier (doesn't stack with other crit-range increases). Once per trance.
**Dragon Blooded (20th).** If you have no Dragoon Trance uses left when you roll initiative, recover 2 uses.

## Dragoon — Subclass: Slayer
- Spineshatter Dive (3rd): on a jump or high jump attack, spend one draconic blood charge; if the creature fails its DEX save, it is stunned until the end of your next turn.
- Familiar Contempt (7th): advantage on History, Nature, and Perception checks involving tracking or gathering information about creatures.
- Elusive Jump (11th): while in a trance, when targeted by an attack roll, reaction to impose disadvantage and make a standing leap up to 3 m high to an unoccupied spot up to 4.5 m away (no OAs).
- Geirskogul (15th): as an action, spend any number of draconic blood charges; creatures in a 30 m long, 1.5 m wide line make a DEX save, taking #d8 force (half on success), # = twice the charges spent.

## Dragoon — Subclass: Dragon Heart
- Breath of the Dragon (3rd): while in a trance, bonus action and one draconic blood charge to cast Dragon's Breath on yourself at 2nd level (3rd level at 9th, 4th level at 17th). Strength is your spellcasting ability for it.
- Dragon Sense (7th): 9 m blindsight and 18 m darksight; in battle, make a Perception check as a bonus action.
- Scales of the Dragon (11th): while in a trance, when you take damage, reaction and one draconic blood charge to gain resistance to slashing, bludgeoning, piercing, and fire until the end of your next turn. Also, your concentration on Dragon's Breath can't be broken.
- Raging Dragon (15th): while under Breath of the Dragon, use the Dragon's Breath spell's effect as a bonus action on your turn.

## Dragoon — Subclass: Valkyrie
- Mirage Dive (3rd): after a Jump attack, until the end of your next turn you may use your bonus action to release an aetheric after-image that performs a jump attack for half damage.
- Flight of the Valkyrie (7th): while in a trance, gain a flying speed equal to your movement; flight distance counts for your Jump features.
- Barrel Roll (11th): you don't provoke opportunity attacks when you fly out of enemies' reach.
- Stardiver (15th): use High Jump without using Stall first, instead spending one draconic blood charge.

# GUNBREAKER
**Hit Die:** d10 | **Saving Throws:** Strength, Dexterity | **Resource:** Munitions (STR/DEX-based)

**Flavor.** An imposing guard ends a knife-wielding assassin with a swift step and strike. A gunblade's bursts of fire and ice fell a rampaging beast. From the dark, a gunbreaker's blade bursts with force, slaying a guarded criminal and vanishing without a sound. Gunbreakers excel at protection, destruction, or subtlety, overwhelming foes with thunderous gunblade strikes.
- Historical Shields: their origin traces to the royal guard of Bozja — the Queen's Blades — who developed gunblades to defend their lands.
- Innovation of War: gunblades once ignited ceruleum to create explosions; today they use rechargeable cartridges for sustained, self-reliant campaigns.
- Creating a Gunbreaker: few in number, often self-taught or mentor-trained; most take mercenary or protection work, with the grit to do any job.

**HP_ref (d10):** 1:10 | 2:16 | 3:22 | 4:28 | 5:34 | 6:40 | 7:46 | 8:52 | 9:58 | 10:64 | 11:70 | 12:76 | 13:82 | 14:88 | 15:94 | 16:100 | 17:106 | 18:112 | 19:118 | 20:124. (Default PF = HP_ref[N] + CON mod x N.)

**Progression**
| Lvl | PB | Features |
|---|---|---|
| 1 | +2 | Trigger System, Munitions, Burst Strike |
| 2 | +2 | Fighting Style, Lightning Blade |
| 3 | +2 | Breaker Style |
| 4 | +2 | Ability Score Improvement |
| 5 | +3 | Extra Attack |
| 6 | +3 | Breaker Style Feature |
| 7 | +3 | Draw and Junction |
| 8 | +3 | Ability Score Improvement |
| 9 | +4 | Diplomatic Enforcer |
| 10 | +4 | Breaker Style Feature |
| 11 | +4 | Rough Divide |
| 12 | +4 | Ability Score Improvement |
| 13 | +5 | Unyielding Heart |
| 14 | +5 | Breaker Style Feature |
| 15 | +5 | Bloodfest |
| 16 | +5 | Ability Score Improvement |
| 17 | +6 | Bow Shock |
| 18 | +6 | Superbolide |
| 19 | +6 | Ability Score Improvement |
| 20 | +6 | Reserve Cache |

**Quick Build.** Strength highest, then Constitution. Soldier background.

**Proficiencies.** Armor: All armour, Shields. Weapons: simple weapons, martial weapons, pistols, muskets. Tools: Smith's Tools. Saving Throws: Strength, Dexterity. Skills: choose two from Athletics, Acrobatics, History, Investigation, Intimidation, Persuasion, Stealth, Survival.
**Equipment.** (a) scale mail or (b) leather armor; (a) a martial weapon already converted to a gunblade; (a) a shield or (b) a pistol and 20 bullets; (a) an explorer's pack or (b) a dungeoneer's pack; (a) Smith's tools.

**Trigger System (1st).** You can modify a weapon to incorporate the trigger system (1 day of work); you may wield only one trigger-system weapon at a time. Such weapons are called Gunblades (typically a longsword/greatsword, or any weapon with DM approval; magic weapons may take extra time).
**Munitions (1st).** You charge cells using your body's energy, keeping a number = your Gunbreaker level. Recover half (round up) on a short rest, all on a long rest. Gunbreaker Save DC = 8 + PB + STR or DEX modifier.
**Burst Strike (1st).** When you hit with a melee weapon attack using a trigger-system weapon, expend one munition to deal +2d8 thunder damage. From 9th level, spend 2 munitions for 4d8; at 17th level, 3 munitions for 6d8.
**Fighting Style (2nd).** Choose Defense / Dueling / Great Weapon Fighting / Protection / Two-Weapon Fighting (standard wording).
**Lightning Blade (2nd).** As an action, spend one munition to make a gunblade weapon attack against a creature within 9 m, dealing lightning damage = weapon's damage + PB. With Extra Attack, make two ranged Lightning Blade attacks when you use this feature.
**Breaker Style (3rd).** Choose Guardians (Vanguard), Lionheart, or Infiltrator. Features at 3rd, 6th, 10th, 14th.
**Ability Score Improvement (4th, 8th, 12th, 16th, 19th).** +2 to one or +1 to two (max 20).
**Extra Attack (5th).** Attack twice when you take the Attack action.
**Draw and Junction (7th).** New munition uses:
- Fated Circle: as an action, spend up to 3 munitions for a 3 m circular explosion centered on you; creatures make a DEX save vs your Gunbreaker DC, taking 2d8 thunder per munition spent (half on success). Can replace Burst Strike.
- Gnashing Fang: with Burst Strike, spend an extra munition; the creature makes a CON save vs your DC or is stunned until the end of your next turn.
- Heart of Stone: when you or an ally within 9 m takes damage, reaction to expend a munition and grant resistance to slashing, piercing, and bludgeoning until the start of your next turn.
- Savage Claw: with Burst Strike, spend an extra munition; the creature makes a STR save or is pushed back 3 m or knocked prone (your choice).
**Diplomatic Enforcer (9th).** While within 3 m of an ally and visible to the target, they add your PB to Persuasion, Deception, and Intimidation checks. If a Medium or smaller creature is missing HP, you have advantage on Intimidation checks against it.
**Rough Divide (11th).** Bonus action, expend one munition to move as though under Jump or Longstrider (your choice) until the start of your next turn; your attacks while under Rough Divide crit on 18-20.
**Unyielding Heart (13th).** Advantage on saves vs Charmed and Frightened; proficiency in Intimidation (expertise if already proficient).
**Bloodfest (15th).** When you land a critical hit, recover 1 munition.
**Bow Shock (17th).** As an action, spend any number of munitions to release a lightning blast centered on you: each munition increases the radius by 3 m and adds 2d8 lightning. Creatures make a CON save vs your DC, taking full damage and paralyzed 1 minute on a fail (half and no paralysis on success; re-save at end of turn).
**Superbolide (18th).** When an attack would reduce you to 0 HP, reaction to drop to 1 HP instead by expending a munition; you become invulnerable until the end of your next turn. Once per long rest.
**Reserve Cache (20th).** When you roll initiative, gain 3 munitions.

## Gunbreaker — Subclass: Guardians (Vanguard)
Stalwart protectors descended from the Queen's Blades.
- Vanguard (3rd): when you hit a creature with an opportunity attack, its speed becomes 0 for the rest of the turn. When a creature within 1.5 m attacks a target other than you, reaction to make a melee weapon attack against the attacker.
- High Alert (6th): proficiency in Investigation, with advantage when searching for hidden objects and traps; if surprised at the start of combat and not incapacitated, you can act normally on your first turn.
- Zone Coverage (10th): when a creature moves within 4.5 m of you, reaction to move up to half your speed toward it and make an opportunity attack.
- Merciless Defender (14th): creatures provoke opportunity attacks even after Disengaging; you make opportunity attacks without using your reaction, and may use your reaction to make a melee attack against a creature that moves more than 1.5 m while in your reach.

## Gunbreaker — Subclass: Lionheart
Elemental strikes and a wild, lion-like assault.
- Elemental Burst (3rd): Burst Strike's bonus damage increases by your PB and you may change its damage type to fire, cold, or lightning. From 10th level, also force, necrotic, or radiant.
- Hunter's Sense (6th): advantage on Perception checks; no disadvantage on attacks while blinded.
- Continuation (10th): when you use Burst Strike, as a bonus action make an additional gunblade weapon attack.
- Relentless Rush (14th): when you land a Continuation attack, spend a munition to make an additional attack; if it lands, spend another munition for another, repeating until you miss.

## Gunbreaker — Subclass: Infiltrator
Uses munitions to hide and strike key targets.
- Camouflage (3rd): spend a munition to cast Invisibility on yourself; at 14th level, spend two munitions to cast Greater Invisibility on yourself.
- Break and Enter (6th): climbing and swim speed equal to your movement; proficiency in thieves' tools; while invisible, your attacks crit on 18-20.
- Aetherial Hunter (10th): while invisible, your base movement speed is doubled and you have advantage on concentration checks.
- Terminal Trigger (14th): when you land a critical hit and use Burst Strike, the creature makes a CON save vs your Gunbreaker DC or the Burst Strike damage is doubled.

# MACHINIST
**Hit Die:** d8 | **Saving Throws:** Dexterity, Intelligence | **Resource:** Aether Batteries (INT-based, Tech)

**Flavor.** A marksman exhales and drops a foe with a single piercing shot, unseen. A mechanized warrior holds the line while the machinist picks off prey from behind it. An inventor finishes a device that lets an ally run and jump like a chocobo. The machinist is a skilled inventor who supports allies with a wide array of devices — mechanical allies, sharpshooting, and innovative solutions.
- Tradition of Innovation: rare talents (the famed Skysteel Forge among them) whose journeys trace to gritty workshops.
- The Power of Aether: they use an aetheroconverter to turn their body's aether into a usable form, stored in batteries that fuel their devices — blood, sweat, and tears are the true fuel.
- Creating a Machinist: a prodigy or guild/forge-trained craftsman who adventures to defend home, fund projects, or field-test their work.

**HP_ref (d8):** 1:8 | 2:13 | 3:18 | 4:23 | 5:28 | 6:33 | 7:38 | 8:43 | 9:48 | 10:53 | 11:58 | 12:63 | 13:68 | 14:73 | 15:78 | 16:83 | 17:88 | 18:93 | 19:98 | 20:103. (Default PF = HP_ref[N] + CON mod x N.)

**Progression**
| Lvl | PB | Features |
|---|---|---|
| 1 | +2 | Inventions, Aether Battery |
| 2 | +2 | Mechanical Turret, Technical Support |
| 3 | +2 | Magnum Opus |
| 4 | +2 | Ability Score Improvement |
| 5 | +3 | Extra Attack, Reload |
| 6 | +3 | Eye for Design, Additional Invention |
| 7 | +3 | Magnum Opus Feature |
| 8 | +3 | Ability Score Improvement |
| 9 | +4 | Additional Invention |
| 10 | +4 | Graze |
| 11 | +4 | Magnum Opus Feature |
| 12 | +4 | Ability Score Improvement |
| 13 | +5 | Additional Invention |
| 14 | +5 | Combat Roll |
| 15 | +5 | Magnum Opus Feature |
| 16 | +5 | Ability Score Improvement |
| 17 | +6 | Additional Invention |
| 18 | +6 | Quick Charge |
| 19 | +6 | Ability Score Improvement |
| 20 | +6 | Magnum Opus Feature |

**Quick Build.** Dexterity highest, then Intelligence. Guild Member background.

**Proficiencies.** Armor: Light. Weapons: Simple weapons, Pistols, Hunting Rifles, Revolvers, Muskets. Tools: two sets of Artisan's Tools. Saving Throws: Dexterity, Intelligence. Skills: choose two from Athletics, Arcana, History, Insight, Intimidation, Perception, Survival.
**Equipment.** (a) leather armour; (a) a pistol and 20 bullets or (b) a dagger; (a) a musket and 20 bullets; (a) an explorer's pack or (b) a dungeoneer's pack; (a) a set of artisan's tools of your choice; (a) an aetherconverter.

**Inventions (1st).** You can support 2 functional inventions, gaining more at 6th, 9th, 13th, 17th. After three long rests you may disassemble one invention and build a new one. Tech Attack Bonus = INT modifier + PB; Tech save DC = 8 + INT modifier + PB. (Inventions list at the end.)
**Aether Battery (1st).** You support a number of aether batteries = PB + INT modifier. Recharge a number = PB on a short rest, all on a long rest. Each battery has 10 energy charges, expended by inventions (cost varies by device). (Optional simplification: drop charge-tracking and give each invention X uses per the listed battery usage, recharging half on a short rest.)
**Mechanical Turret (2nd).** You build a construct ally (statblock below). In combat it acts on your turn: it moves and uses its reaction on its own but only Dodges unless you use a bonus action to command another action; you can sacrifice one of your attacks to command it to Attack. If incapacitated, it acts freely. At 0 HP it shuts off; use your action and expend one aether battery to reboot it (back in 1 minute at full HP). It regains all HP on a long rest if active.
- *Mechanical Turret* — Small Construct. AC 13 + PB. HP 5 + four times your class level (Hit Dice [d6s] = your Machinist level). Speed 9 m (hover). STR 10(+0) DEX 16(+3) CON 14(+2) INT 1(-5) WIS 10(+0) CHA 1(-5). Damage Immunities poison, psychic. Condition Immunities blinded, charmed, deafened, exhaustion, frightened, paralyzed, petrified, poisoned. Senses passive Perception 10. Languages understands its creator's languages but can't speak. Proficiency Bonus = yours. Aetheric Programming: add your PB to any ability check or save the turret makes. Actions — Point Blank: melee weapon attack, your Tech attack bonus (source: spell attack modifier) to hit, reach 1.5 m, 8 (1d6 + 2 + PB) piercing. Turret Shot: ranged weapon attack, range 9 m, 9 (1d8 + 2 + PB) piercing.
**Technical Support (2nd).** Use artisan's tools to disarm mechanical traps.
**Ability Score Improvement (4th, 8th, 12th, 16th, 19th).** +2 to one or +1 to two (max 20).
**Extra Attack (5th).** Attack twice when you take the Attack action.
**Reload (5th).** Ranged weapons you use lose their loading property.
**Eye for Design (6th).** Advantage on Investigation checks to understand mechanical systems and on Survival checks to track a creature within a building, village, town, or city.
**Graze (10th).** Bonus action to empower your next shot to target a limb; on a hit, the target makes a DEX save vs your Machinist save DC or suffers an effect (until your next action where applicable): Head = Stunned; Heart = Frightened; Arm = Disarmed; Leg = Prone. Uses = INT modifier (min 1), recovered on a long rest.
**Combat Roll (14th).** When targeted by an attack, reaction to impose disadvantage and move 1.5 m to an open space without provoking OAs. Uses = PB, recovered on a short or long rest.
**Quick Charge (18th).** All batteries recharge on a short rest.

## Machinist — Subclass: Gaussian Marksman
- Gauss Barrel (3rd): a firearm/crossbow attachment requiring one Aether Battery; on a ranged weapon attack with it, spend two battery charges to add your INT modifier to the attack and damage rolls.
- Heat Blast (7th): each Gauss Barrel ranged attack grants two heat charges (max = PB); spend two heat charges to add 1d6 fire damage (2d6 at 15th).
- Sharpshooter (11th): Gauss Barrel attacks crit on 19-20.
- Heated Clean Shot (15th): on a Gauss Barrel attack, spend a battery charge to gain advantage.
- Marksman's Spite (20th): critical hit damage is tripled; Gauss Barrel attacks crit on 18-20.

## Machinist — Subclass: Roboticist
- Regal Automoton (3rd): an enhanced mechanical ally housing your turret (replaces it); as a bonus action, release the turret to operate separately (automoton inactive) or reconnect it within 1.5 m. Controlled like the Mechanical Turret, using the statblock below.
  - *Regal Automoton* — Medium Construct. AC 14 + PB. HP 10 + five times your class level (Hit Dice [d8s] = your Machinist level). Speed 9 m. STR 16(+3) DEX 14(+2) CON 14(+2) INT 1(-5) WIS 10(+0) CHA 1(-5). Damage Immunities poison, psychic. Condition Immunities blinded, charmed, deafened, exhaustion, frightened, paralyzed, petrified, poisoned. Senses passive Perception 10. Languages understands its creator's languages but can't speak. PB = yours. Aetheric Programming: add your PB to its checks/saves. Actions — Unarmed Strike: melee weapon attack, your Tech attack bonus, reach 1.5 m, 11 (1d10 + 3 + PB) bludgeoning. Regal Shot: ranged weapon attack, range 9 m, 8 (1d6 + 2 + PB) piercing.
- Variable Armor (7th): enhancements for the Automoton — Queen's Armor (adds your INT modifier to its weapon attacks, +1.5 m speed, may change unarmed damage to slashing/piercing/lightning); Knight's Armor (+3 m speed; Standing Leap: long jump up to 9 m, high jump up to 4.5 m; Deadly Leap: if it jumps at least 4.5 m, land in a creature's space — STR or DEX save (target's choice) vs your Tech save DC or knocked prone and 11 (1d10 + 3 + PB) bludgeoning; on success, half damage, not prone, pushed 1.5 m to an unoccupied space, or prone in the automoton's space if none); Rook's Armor (AC increased by your INT modifier; when a creature attacks a target other than you within 1.5 m of the automoton, reaction to impose disadvantage).
- Advanced Combat Protocol (11th): the Regal Automaton and Mechanical Turret attack twice when ordered to Attack.
- Battery Charge Attack (15th): attach up to three batteries; each special feature needs one full battery — Aetherial Ray (chest cannon, 5 charges: a 30 m line, 1.5 m wide; DEX save vs Tech save DC, 10d6 force, half on success); Crowned Collider (2 charges: Dash then an unarmed strike with advantage dealing 2d10 bonus damage); Pilebunker (2 charges: all creatures in a 6 m radius make a DEX save, 4d6 bludgeoning and prone on a fail, half and not prone on success).
- Style Change (20th): as an action, change the Automoton's armor and battery charge attack loadout.

## Machinist — Subclass: Inventor's Legacy
- Well Oiled Machines (3rd): attacks made with your inventions deal bonus damage = your INT modifier.
- Overnight Success (7th): on a long rest, disassemble one invention and replace it (counts as done during the rest).
- Battery Stabilizer (11th): your batteries have twice the normal charges.
- Jerry-Rigged (15th): combine 1- or 2-handed inventions into a single machine (total hands required <= 5); you can hold the combined machine with 2 hands.
- Hyper Charger (20th): as an action, charge 2 aether batteries (once per long rest). Also, Well Oiled Machines bonus damage is doubled.

## Machinist — Inventions (powered by Aether Batteries)
1st level builds Tier 1; 5th level Tier 2; 9th level Tier 3.

### Tier 1
- **Aether Detector** (10 minutes, 1 charge/min): sense magic within 9 m; as an action, see a faint aura around magical creatures/objects. Blocked by 0.3 m stone, 2.5 cm common metal, a thin sheet of lead, or 0.9 m wood or dirt.
- **Bio Blaster** (5 attacks, 2 charges each): a 4.5 m cone of toxic mist; CON save vs your invention DC or poisoned and 4d4 poison (half, not poisoned on success); a poisoned creature re-saves with disadvantage at end of turn.
- **Chocobo Boots** (10 uses, 1/charge): +1.5 m base speed; as a bonus action, gain Longstrider or Jump until the end of your next turn.
- **Climber's Claws** (10 hours, 1 charge/hr): bonus action to gain a climbing speed = your base movement; unarmed strikes deal 1d4 piercing while equipped.
- **Flash Bulb** (2 attacks, 5 charges each): emits 18 m bright + 18 m dim light (1 charge = 1 hour of light). As an action, a 9 m cone; CON save vs your Tech save DC or 2d6 radiant and blinded 1 minute (half, not blinded on success; re-save as an action). Sunlight-sensitive creatures have disadvantage.
- **Noise Blaster** (2 attacks, 5 charges each): a 4.5 m cone; CON save vs your Tech save DC, 2d6 thunder and stunned until start of its next turn on a fail (half, not stunned on success).
- **Pictobox** (10 uses, 1/charge): captures images onto parchment; needs good lighting.
- **Snare Trap** (10 hours, 1 hr/charge): a near-invisible trap covering a 1.5 m radius (found with an INT (Investigation) check vs your spell save DC). A Small or larger creature entering makes a DEX save or falls prone and is hoisted ~0.9 m up, restrained (re-save with disadvantage at end of turn; or another creature uses an action on an INT (Arcana) check vs your Tech save DC to end it).
- **Sounding Sentry** (10 hours, 1 hr/charge): warding alarm on an area up to a 6 m cube for up to 10 hours; alerts you (mental within 1.6 km, or audible — a hand bell for 10 seconds within 18 m) when a Tiny+ creature enters; you may designate non-triggering creatures.

### Tier 2
- **Aetheric Launcher** (5 attacks, 2 charges each): launch a bomb within 9 m; creatures in a 1.5 m sphere make a DEX save vs Tech DC, 2d8 fire (half on success).
- **Auto Crossbow** (5 attacks, 2 charges each): bonus action; a 4.5 m cone; DEX save vs Tech DC, 2d6 piercing (half on success). Counts as a light crossbow for proficiency.
- **Grappling Gauntlet** (10 uses, 1/attack): a grappling hook with 18 m range anchoring as an action (advantage on climb checks toward the anchor, +3 m speed toward it; usable as a swing rope). As an action, spend one charge to grapple a creature within 18 m using your Tech attack bonus, 2d6 piercing on hit and grappled (STR save vs Tech DC to break free). As a bonus action, drag it 3 m closer (STR save negates). Within 1.5 m, its speed becomes 0.
- **Gust Bellows** (10 uses, 1/charge): as an action, a 9 m cone of wind until the start of your next turn; creatures starting their turn in it make a STR save or are pushed 4.5 m from the device; moving toward the device costs 2 m of movement per 1 m moved. Disperses gas/vapor and extinguishes/dances flames; projectiles against the wind have disadvantage.
- **Hawkeye Mask** (10 hours, 1 hr/charge): proficiency in Perception (sight) using INT; see up to ~6.4 km in clear conditions; +9 m to your ranged weapons' normal range.
- **Mog Boots** (10 minutes, 1 charge/min): hover up to 1.5 m above a surface (bonus action to toggle).
- **Remote Control Unit** (10 minutes, 1 charge/min): see/hear through the turret via a controller; while directly controlling it you may attack twice with your Attack action (but not also order it via bonus action); works with the Regal Automoton too.
- **Sahagin Set** (10 hours, 1 charge/hr): swim speed = your movement and hold breath for 1 hour while active.
- **Titan Belt** (10 uses, 1/charge): when an effect would forcibly move you, reaction to gain advantage on the save; also, reaction + charge to gain advantage on a concentration check.

### Tier 3
- **Air Anchor** (5 attacks, 2 charges each): ranged weapon attack (Tech attack bonus or DEX), 3d12 piercing; on hit, STR save vs Tech DC or restrained and flying speed reduced to 0 (re-save as an action).
- **Air Gear** (10 minutes, 1 charge/min): a hover-board granting flying speed 18 m (hover), supporting up to ~227 kg.
- **Chain Saw Blade** (10 attacks, 1/attack): upgrade a sword to deal double its base damage die; on a hit, rev for bonus damage = your INT modifier. You may use your Tech attack modifier for attack rolls with it.
- **Cloaking Stave** (1 minute, 1 charge/round): turns you and creatures within a 1.5 m radius invisible for 1 minute (must stay within 1.5 m of the device, which can stand on its own).
- **Drill** (5 attacks, 2 charges each): a target within 18 m makes a DEX save with disadvantage vs Tech DC, 3d12 force on a fail.
- **Emergency Defibrillator** (1 use, 10 charges): casts Cure Wounds at 3rd level (INT as spellcasting ability); activates as an action or automatically if the creature is at 0 HP at the start of its turn.
- **Flamethrower** (5 attacks, 2 charges each): as an action, a 9 m cone, a 27 m line (1.5 m wide), or a 3 m radius burst within 18 m; DEX save vs Tech DC, 4d8 fire (half on success).
- **Proximity Lightning Mine** (10 hours, 1 hr/charge): a near-invisible mine (found with INT (Investigation) or WIS (Perception) vs your spell save DC); a creature within a 1.5 m radius triggers it, discharging all charges: DEX save vs Tech DC or 1d6 lightning per charge spent; also CON save vs Tech DC or paralyzed 1 minute (re-save at end of each turn).
- **Trailblazer** (10 hours, 1 hr/charge): a two-seater motorbike; covers twice the usual fast-pace distance, tows up to ~227 kg. In combat, bonus action to steer for a movement speed of 24 m. AC 14, 100 HP (inoperable at 0); repaired on a long rest.

# NINJA
**Hit Die:** d8 | **Saving Throws:** Dexterity, Intelligence | **Resource:** Mudra points (WIS-based)

**Flavor.** A dual-wielder leaves a thug in a heap without a sound. A cloaked figure links unseen hand symbols and unleashes a blaze. An uninvited guest gleans secrets from the shadows of an imperial meeting. Lightly armoured and versatile, ninjas mix magicks, steel, and stealth, rooted as the special operatives of Doma.
- Of Heaven, Earth and Man: ninjas manipulate life energy via mudras — sacred hand symbols representing heaven (Ten), earth (Chi), and man (Jin) — combining them for superhuman effects.
- Cloak and Dagger: they adapt to any situation with aether, blades, or shadows.
- Creating a Ninja: consider your training (bloodline or recruited by a master) and why you travel.

**HP_ref (d8):** 1:8 | 2:13 | 3:18 | 4:23 | 5:28 | 6:33 | 7:38 | 8:43 | 9:48 | 10:53 | 11:58 | 12:63 | 13:68 | 14:73 | 15:78 | 16:83 | 17:88 | 18:93 | 19:98 | 20:103. (Default PF = HP_ref[N] + CON mod x N.)

**Progression**
| Lvl | PB | Aeolian Edge | Fleet of Foot | Features |
|---|---|---|---|---|
| 1 | +2 | 1d6 | — | Expertise, Mudra, Ninjutsu |
| 2 | +2 | 1d6 | +1.5 m | Adaptive Tactic, Fleet of Foot |
| 3 | +2 | 2d6 | +1.5 m | Class Archetype |
| 4 | +2 | 2d6 | +1.5 m | Ability Score Improvement |
| 5 | +3 | 3d6 | +1.5 m | Extra Attack |
| 6 | +3 | 3d6 | +3 m | Class Archetype Feature, Fleet of Foot Improvement, Mudra Improvement |
| 7 | +3 | 4d6 | +3 m | Assassinate, Expertise Improvement |
| 8 | +3 | 4d6 | +3 m | Ability Score Improvement |
| 9 | +4 | 5d6 | +3 m | Uncanny Dodge, Mudra Improvement |
| 10 | +4 | 5d6 | +4.5 m | Reliable Talent, Fleet of Foot Improvement |
| 11 | +4 | 6d6 | +4.5 m | Class Archetype Feature |
| 12 | +4 | 6d6 | +4.5 m | Ability Score Improvement |
| 13 | +5 | 7d6 | +4.5 m | Blindsense |
| 14 | +5 | 7d6 | +6 m | First Striker, Fleet of Foot Improvement |
| 15 | +5 | 8d6 | +6 m | Perfect Dodge |
| 16 | +5 | 8d6 | +6 m | Ability Score Improvement |
| 17 | +6 | 9d6 | +6 m | Class Archetype Feature |
| 18 | +6 | 9d6 | +7.5 m | Elusive, Fleet of Foot Improvement |
| 19 | +6 | 10d6 | +7.5 m | Ability Score Improvement |
| 20 | +6 | 10d6 | +7.5 m | Kassatsu |

**Quick Build.** Dexterity highest, then Wisdom. Criminal background (spy variant).

**Proficiencies.** Armor: Light. Weapons: Simple Weapons, blowguns, longswords, shortswords. Tools: Disguise Kit, Thieves' tools. Saving Throws: Dexterity, Intelligence. Skills: choose four from Acrobatics, Athletics, Deception, Insight, Intimidation, Investigation, Perception, Performance, Persuasion, Sleight of Hand, Stealth.
**Equipment.** (a) 2 Daggers; (a) a simple weapon; (a) a short bow and 20 arrows; (a) a set of leather armour; (a) a set of Thieves' Tools; (a) a dungeoneer's pack or (b) an explorer's pack.

**Mudra (1st).** Channel life energy. You gain the Ten mudra at 1st, Chi at 6th, Jin at 9th. You have mudra points of each type = PB + WIS modifier, spent on certain features; regained on a short or long rest. Mudra save DC = 8 + PB + WIS modifier; Mudra attack = PB + WIS modifier.
**Ninjutsu (1st).** You can cast ninjutsu (list at the end), paying mudra costs.
**Expertise (1st).** Two skill proficiencies (or one skill + thieves' tools) gain double PB. Two more at 7th.
**Adaptive Tactics (2nd).** A bonus action each turn for Dash, Disengage, or Hide. At 13th, gain a second bonus action usable only for Adaptive Tactics.
**Fleet of Foot (2nd).** Speed increases per the Fleet of Foot column.
**Class Archetype (3rd).** Choose Yoshimitsu, Shinobi, or Shadow. Features at 3rd, 11th, 17th.
**Ability Score Improvement (4th, 8th, 12th, 16th, 19th).** +2 to one or +1 to two (max 20). (May take a feat instead via the optional rule.)
**Extra Attack (5th).** Attack twice when you take the Attack action.
**Assassinate (7th).** While invisible, melee weapon attacks crit on 18-20.
**Uncanny Dodge (9th).** When an attacker you can see hits you, reaction to halve the damage.
**Reliable Talent (10th).** On an ability check using your PB, treat a d20 roll of 9 or lower as a 10.
**Blindsense (13th).** If you can hear, you know the location of hidden/invisible creatures within 3 m.
**First Striker (14th).** Advantage on initiative; your first attack roll in combat has advantage.
**Perfect Dodge (15th).** When you take the Dodge action, until the start of your next turn gain a bonus = your WIS modifier to AC and DEX saves.
**Elusive (18th).** No attack roll has advantage against you while you aren't incapacitated.
**Kassatsu (20th).** When you roll initiative, recover 3 mudra points, split across the three types as you wish.

## Ninja — Subclass: Yoshimitsu
- Dual Wielding Adept (3rd): add your ability modifier to the second attack's damage in two-weapon fighting; +1 AC.
- Mug (6th): attempt to steal from a creature within 1.5 m as part of Adaptive Tactics; add your WIS modifier to Sleight of Hand checks (not when used via Adaptive Tactics).
- Dream Within A Dream (11th): when you make a melee weapon attack as a bonus-action off-hand attack, make two attacks.
- Shuhiko (17th): add your WIS modifier to weapon damage rolls.

## Ninja — Subclass: Shinobi
- Meisui (3rd): as a bonus action, take 1 level of exhaustion to recover all missing mudra points.
- Tangential Understanding (6th): proficiency in Arcana.
- Advanced Ninjutsu (11th): spend twice a ninjutsu's mudra cost for its Enhanced Ninjutsu effect.
- Ten Chi Jin (17th): create a 3 m radius field (centered on you) for 1 minute or until you cast three ninjutsu, letting you cast ninjutsu without spending mudra points. Once per long rest.

## Ninja — Subclass: Shadow
- Thinning (3rd): bonus action, expend one Hit Die to become invisible (gear included); ends when you attack, cast a spell/ninjutsu, or after 1 minute.
- All Fours (6th): your steps make no sound; fall damage you take is halved.
- Trick Attack (11th): while invisible, action to make a melee weapon attack; on hit, the creature makes an INT save vs your Mudra save DC or all attacks against it have advantage until the start of your next turn.
- Unseen Shadow (17th): spend one mudra of any type to attack, cast a spell, or cast a ninjutsu without losing invisibility.

## Ninja — Ninjutsu List
- **Aeolian Edge** (1st; 1 mudra any): when you land a melee weapon attack made with advantage, deal extra damage per the Aeolian Edge column. Finesse weapon; once per turn.
- **Armor Crush** (3rd; 2 mudra any): bonus action; until the start of your next turn, instead of rolling attacks, your targets make a DEX save vs your Mudra save DC or are hit, taking bonus force damage = your WIS modifier. *Enhanced:* +2 to the Mudra save DC for these attacks and bonus damage = double your WIS modifier.
- **Choho** (1st; 1 mudra any): bonus action, become invisible (gear included); ends when you attack, cast a spell/ninjutsu, or after 10 minutes.
- **Doton** (9th; 1 of each mudra): action; a 3 m radius circle of corrupted earth (difficult terrain for others), dealing 2d4 necrotic per 1.5 m travelled within; on appearance, creatures in the ring make a DEX save, 4d4 necrotic (half on success). You are unaffected. *Enhanced:* movement damage +2d4 and each time a creature takes Doton damage it makes a CON save or is poisoned 1 minute.
- **Fuma Shuriken** (1st; 1 mudra any): action; a wind shuriken at a creature within 18 m; mudra spell attack, 1d12 thunder. *Enhanced:* hit or miss it explodes — the target and creatures within 1.5 m make a DEX save or take 2d8 thunder.
- **Goka Mekkyau** (15th; 2 Ten + 3 any): action; a fiery typhoon within 36 m; creatures in a 6 m radius make a DEX save or take 4d6 fire + 4d6 thunder (half on success). The area burns 1 minute (entering/starting turn = 1d10 fire). *Enhanced:* +4d6 fire and the area becomes difficult terrain while burning.
- **Hollow Nozuchi** (15th; 2 Jin + 3 any): action; aetherial snake tails make up to 5 attacks vs creatures within a 36 m radius (split or focused); mudra spell attack, 2d6 bludgeoning each. *Enhanced:* deals piercing instead with +1d6 poison; each hit forces a CON save or poisoned 1 hour.
- **Huraijin** (13th; 2 Ten + 2 any): bonus action; for 1 hour, +1 to attack rolls and +1d4 thunder damage with one weapon. *Enhanced:* +2 to attacks and +2d4 thunder.
- **Huton** (9th; 1 of each mudra): bonus action; for 1 minute, your speed is doubled, +2 AC, advantage on DEX saves, and an extra action each turn (Attack [one weapon attack], Dash, Disengage, Hide, or Use an Object). When it ends, you can't move or act until after your next turn. *Enhanced:* cast Huton on a willing creature you touch (maintain concentration as a spell).
- **Hyosho Ranryu** (13th; 2 Chi + 2 any): action; create 6 ice shurikens, each hitting a creature you can see within range for 1d4 + 1 cold (direct one or several). *Enhanced:* twice the number of shurikens.
- **Hyoton** (9th; 1 Chi + 1 any): action; a 9 m cone; STR save vs your Mudra save DC, 4d6 cold and restrained (half, not restrained on success). *Enhanced:* +2d6 cold and the area becomes difficult terrain for 1 minute.
- **Katon** (6th; 1 Ten + 1 any): action; a fireball within 18 m exploding in a 6 m radius sphere; DEX save, 6d6 fire (half on success). *Enhanced:* +2d6 fire and +3 m radius.
- **Meiton** (3rd; 1 mudra any): bonus action; a 6 m radius sphere of smoke (heavily obscured, spreads around corners) for 10 minutes or until dispersed by moderate wind. *Enhanced:* creatures starting their turn in the smoke make a CON save or are poisoned 1 minute (you are immune).
- **Phantom Kamaitachi** (15th; 2 Chi + 3 any): action; a phantom copy attacks with you — make two melee mudra attacks, 2d10 thunder each; also gain the Dodge action. *Enhanced:* the phantom makes two additional weapon attacks.
- **Raiju** (17th; 3 Chi + 3 any): action; wreathe yourself in lightning — Forked Raiju (appear in an unoccupied space next to a creature within 9 m; creatures within 1.5 m make a DEX save vs your Mudra save DC, 10d6 lightning, half on success) or Fleeting Raiju (mudra spell attack vs a touched creature, 10d8 lightning). *Enhanced:* double the chosen Raiju's damage dice.
- **Raiton** (6th; 1 Chi + 1 any): action; a lightning bolt within 18 m bursting in a 3 m radius; DEX save vs your Mudra save DC, 5d8 lightning (half on success). *Enhanced:* call down two bolts (same or different location; re-save).
- **Shukuchi** (3rd; 2 mudra any): bonus action, teleport up to 9 m to an unoccupied space you can see.
- **Suiton** (9th; 1 of each mudra): action; a geyser in a 3 m radius circle beneath you; DEX save, 4d8 bludgeoning (half on success); you and your gear become invisible for 1 minute (ends if you attack/cast/ninjutsu or after 1 minute). *Enhanced:* +2d8 bludgeoning and creatures make a STR save vs your Mudra save DC or are knocked back 4.5 m.

# MONK (Ala Mhigan)
**Hit Die:** d10 | **Saving Throws:** Strength, Dexterity | **Resource:** Chakra / Elemental / Perfect Balance charges (WIS-based)

**Flavor.** A stoic wanderer's skin turns hard as stone and his earth-shaking blows send bandits fleeing. A martial artist's flaming fists strike a beast as he seeks ever-greater challenges. A cheerful traveler wanders mountain paths, helping those they meet. Monks of the Fist of Rhalgr draw on chakra — the life energy within their bodies — to perform powerful martial arts and superhuman feats.
- Guided By A Falling Star: refugees of the great flood were led by Rhalgr the Destroyer (via a meteorite) to the Gyr Albanian highlands, where the Fist of Rhalgr formed; their order was later broken by civil war.
- By Their Hands: they fight chiefly with fists (augmented with claws, knuckles, tonfas), sometimes weaving staves, spears, or blades.
- Creating an Ala Mhigan Monk: consider your training (a Fist of Rhalgr master, a monastery, or self-unlocked) and your elemental Riddle.

**HP_ref (d10):** 1:10 | 2:16 | 3:22 | 4:28 | 5:34 | 6:40 | 7:46 | 8:52 | 9:58 | 10:64 | 11:70 | 12:76 | 13:82 | 14:88 | 15:94 | 16:100 | 17:106 | 18:112 | 19:118 | 20:124. (Default PF = HP_ref[N] + CON mod x N.)

**Progression**
| Lvl | PB | Martial Arts Die | Features |
|---|---|---|---|
| 1 | +2 | 1d4 | Martial Arts, Unarmoured Defense |
| 2 | +2 | 1d4 | Chakra Gate, Monastic Artes |
| 3 | +2 | 1d4 | Elemental Gate, Monastic Riddle |
| 4 | +2 | 1d4 | Ability Score Improvement |
| 5 | +3 | 1d6 | Extra Attack |
| 6 | +3 | 1d6 | Riddle Feature, Fists of Rhalgr |
| 7 | +3 | 1d6 | Evasion |
| 8 | +3 | 1d6 | Ability Score Improvement |
| 9 | +4 | 1d6 | Master of Movement |
| 10 | +4 | 1d6 | Aura Veil |
| 11 | +4 | 1d8 | Perfect Balance, Riddle Feature |
| 12 | +4 | 1d8 | Ability Score Improvement |
| 13 | +5 | 1d8 | Aura Speech |
| 14 | +5 | 1d8 | Iron Will |
| 15 | +5 | 1d8 | Aura Sense |
| 16 | +5 | 1d8 | Ability Score Improvement |
| 17 | +6 | 1d10 | Riddle Feature |
| 18 | +6 | 1d10 | Anatman |
| 19 | +6 | 1d10 | Ability Score Improvement |
| 20 | +6 | 1d10 | Transcendence |

**Quick Build.** Dexterity highest, then Wisdom. Hermit background.

**Proficiencies.** Armor: none. Weapons: Simple Weapons, Martial Weapons. Tools: none. Saving Throws: Strength, Dexterity. Skills: choose two from Acrobatics, Athletics, History, Insight, Religion, Stealth.
**Equipment.** (a) a shortsword or (b) any simple weapon; (a) a dungeoneer's pack or (b) an explorer's pack; 10 darts.

**Unarmoured Defense (1st).** While wearing no armor and no shield, AC = 10 + DEX modifier + WIS modifier.
**Martial Arts (1st).** While unarmed or wielding only monk weapons (shortswords and simple melee weapons without two-handed or heavy), and not wearing armor or a shield: use DEX for unarmed/monk-weapon attack and damage; roll the Martial Arts die in place of normal damage (scales per table); when you take the Attack action with an unarmed strike or monk weapon, make one unarmed strike as a bonus action.
**Chakra Gate (2nd).** Bonus action to open a chakra gate, gaining chakra charges = WIS modifier (persist until a short/long rest or you reopen the gate). Uses = PB, refreshed on a short or long rest.
**Monastic Artes (2nd).** Special techniques using chakra (list at the end). Monastic Artes save DC = 8 + PB + WIS modifier; attack = PB + WIS modifier.
**Monastic Riddle (subclass, 3rd).** Choose Riddle of Earth, Fire, or Wind. Features at 3rd, 6th, 11th, 17th.
**Elemental Gate (3rd).** Bonus action to open the elemental chakra gate, gaining elemental chakra = WIS modifier (persist until a long rest or reopen). Uses = PB, refreshed on a long rest.
**Ability Score Improvement (4th, 8th, 12th, 16th, 19th).** +2 to one or +1 to two (max 20).
**Extra Attack (5th).** Attack twice when you take the Attack action.
**Fists of Rhalgr (6th).** Unarmed strikes count as magical for overcoming resistance/immunity to nonmagical damage.
**Evasion (7th).** On a DEX save for half damage, take none on success and half on failure.
**Master of Movement (9th).** On an Athletics (STR) or Acrobatics (DEX) check, spend one chakra charge for advantage.
**Aura Veil (10th).** When you take damage, spend Chakra and Element charges up to your PB; gain temp HP = PB per charge spent (before applying the damage).
**Perfect Balance (11th).** Bonus action to gain Perfect Balance charges = WIS modifier (for specific Monastic Artes or as a substitute for Chakra/Element charge costs); persist until a long rest. Refreshes on a long rest.
**Aura Speech (13th).** Understand all spoken languages, and any creature that understands a language can understand you.
**Iron Will (14th).** Proficiency in all saving throws; when you fail a save, spend 1 chakra charge to reroll and take the second result.
**Aura Sense (15th).** Gain 3 m of blindsight.
**Anatman (18th).** When you use Chakra Gate, Elemental Gate, or Perfect Balance, gain one additional charge.
**Transcendence (20th).** As a bonus action, gain the benefit of Chakra Gate, Elemental Gate, and Perfect Balance. Once per long rest.

## Monk — Subclass: Riddle of Earth
- Stone Skin (3rd): while you have Elemental chakra, when hit by an attack, expend one chakra to gain resistance to slashing, piercing, and bludgeoning until the start of your next turn.
- Lore of the Land (6th): proficiency in the Nature skill.
- Earth's Reply (11th): when you take damage from a creature you can see within 9 m, reaction and one elemental chakra — it makes a STR save, 2d10 magical bludgeoning (half on success).
- Heart of Solid Earth (17th): bonus action, spend 1 Perfect Balance chakra and up to your monk level in HP to create a protective layer with that many HP (resistance to slashing/piercing/bludgeoning while it lasts; can't be healed; excess damage not applied). Once per long rest.

## Monk — Subclass: Riddle of Fire
- Fists of Fire (3rd): when you hit with an unarmed weapon attack, expend one Chakra or Elemental charge for an additional fire damage die.
- Chakra Candle (6th): action, spend an Elemental chakra to create a white flame hovering 1.5 m off the ground for 1 minute, emitting 3 m bright + 3 m dim light; hidden objects/passages within 3 m are outlined; an invisible creature within 3 m makes a CHA save vs your Monastic Artes DC or is outlined in light.
- Inferno Strikes (11th): when you use Fists of Fire, spend an extra Elemental charge to force creatures within 3 m of the target to make a DEX save vs your Monastic Artes DC, taking damage equal to the unarmed strike's (half on success).
- Heart of Raging Flames (17th): bonus action, cloak yourself in flames for 1 minute — a hostile creature entering within 1.5 m, or starting its turn within 1.5 m, takes 5 fire. While cloaked, as an action expend Hit Dice up to your WIS modifier and recover HP equal to the rolls. Once per long rest.

## Monk — Subclass: Riddle of Wind
- Second Wind Infusion (3rd): healing pool = monk level x 5 (refreshes on a long rest); as an action touch a creature to restore HP from the pool, or expend 5 HP to cure a disease or neutralize a poison. No effect on undead/constructs.
- Featherfoot (6th): base movement speed +3 m; jump height and distance +3 m.
- Mantra (11th): as an action, heal a number of creatures up to your PB within 3 m using your Second Wind Infusion pool.
- Heart of Soothing Winds (17th): bonus action to gain a flying speed equal to your walking speed for 1 minute. Once per long rest.

## Monk — Monastic Artes List
- **Arm of the Destroyer** (3rd, Riddle of Earth; 2 Element): cast Earth Tremor at 1st level; +1 casting level per extra Element charge.
- **Brotherhood** (17th, Riddle of Earth; 1 Perfect Balance + 3 Element): bonus action; infuse up to WIS-modifier creatures with a ward — each gains 1d10 + WIS modifier temp HP and +3 AC while it lasts.
- **Celestial Revolution** (17th, Riddle of Wind; 1 Perfect Balance + 3 Element): when you hit with a melee weapon attack, deal 6d8 thunder and teleport up to 18 m to a space you can see.
- **Chakra Shot** (2nd; 1 Chakra): action; ranged Monastic Arte attack within 18 m, force damage = Martial Arts die + WIS modifier. At 5th level, make two ranged attacks.
- **Demolish** (6th, Riddle of Earth; 3 Element): on a melee weapon hit, the creature makes a CON save or attack rolls against it gain +2 until the start of your next turn.
- **Dragon Kick** (9th; 3 Chakra): on a melee weapon hit, until the start of your next turn add your WIS modifier to your unarmed strike damage rolls.
- **Elixir Field** (14th; 1 Perfect Balance + 3 Chakra): action; a 6 m radius sphere around you; DEX save or 6d6 force and blinded 1 minute (half, not blinded on success).
- **Enlightenment** (14th; 1 Perfect Balance + 3 Chakra): action; a ray 4.5 m wide and 18 m long; DEX save, 6d8 force (half on success).
- **Flash Fire** (3rd, Riddle of Fire; 2 Element): cast Burning Hands at 1st level; +1 casting level per extra Element charge.
- **Flint Strike** (11th, Riddle of Fire; 3 Element): a 6 m radius circle around you; DEX save or 8d6 fire (half on success). The area stays ignited 1 minute (entering/starting turn = 2d4 fire).
- **Greased Lightning** (2nd; 1 Chakra): immediately after the Attack action or a Monastic Arte (as an action), make two unarmed strikes as a bonus action.
- **Howling Fist** (6th, Riddle of Fire; 2 Element): a 1.5 m wide, 18 m long line; DEX save or 3d8 fire and knocked prone (half, not prone on success).
- **Phantom Rush** (18th; 3 Perfect Balance): spend any number of Chakra/Elemental charges against a creature within 9 m — one unarmed strike per charge; then appear adjacent to it.
- **Rising Phoenix** (17th, Riddle of Fire; 1 Perfect Balance + 3 Element): a 9 m radius sphere; for each creature choose — Heal (1d8 + WIS modifier HP) or Wound (DEX save, 8d8 + WIS modifier fire, half on success).
- **Rockbreaker** (11th, Riddle of Earth; 3 Element): a 9 m cone; STR save, 4d8 magical bludgeoning and knocked back 9 m or knocked prone (your choice).
- **Steel Peak** (5th; 2 Chakra): on a melee weapon hit, the creature makes a STR save or is stunned until the start of your next turn.
- **Six-Sided Star** (2nd; 1 Chakra): on a melee weapon hit, until end of turn you may Disengage as a bonus action.
- **Snap Punch** (5th; 2 Chakra): when a creature enters within 1.5 m, reaction to make one unarmed strike.
- **Tailwind** (3rd, Riddle of Wind; 2 Element): cast Longstrider or Jump on yourself.
- **Thunderclap** (6th, Riddle of Wind; 3 Element): bonus action, teleport up to 9 m to a space you can see.
- **Tornado Kick** (11th, Riddle of Wind; 3 Element): a 6 m radius sphere around you; STR save or 5d8 thunder and knocked back 9 m (half, not knocked back on success).
- **True Strike** (9th; 3 Chakra): an unarmed strike with doubled PB on the attack roll and +WIS modifier damage.

# PALADIN (Sultansworn)
**Hit Die:** d10 | **Saving Throws:** Charisma, Constitution | **Spellcasting:** Charisma (cleric-style, prepared, half-caster)

**Flavor.** A light-shrouded blade fells a roaming dark creature. A knight steps into an arrow's path to shield their noble, the shot clanking off armor. A robed adventurer's incantations bring divine light down on foes. Paladins infuse their will into weapon and armour, fighting far beyond their limits.
- Conviction Made Manifest: the first Sultansworn fused their life force into a shield to block a mage's deadly blow in early Ul'dah — the cornerstone of paladin arts.
- Divine Words and Sacred Steel: immovable defenders in heavy armour who pair peerless defense with divine incantations powered by conviction.
- Creating a Paladin: from soldiers, trained warriors, or self-taught heroes; consider your purpose (protect home, serve a master, redemption, revenge).

**HP_ref (d10):** 1:10 | 2:16 | 3:22 | 4:28 | 5:34 | 6:40 | 7:46 | 8:52 | 9:58 | 10:64 | 11:70 | 12:76 | 13:82 | 14:88 | 15:94 | 16:100 | 17:106 | 18:112 | 19:118 | 20:124. (Default PF = HP_ref[N] + CON mod x N.)

**Progression — spell slots per level**
| Lvl | PB | Features | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|---|
| 1 | +2 | Aetherial Arms, Sworn Protector | — | — | — | — | — |
| 2 | +2 | Fighting Style, Spellcasting | 2 | — | — | — | — |
| 3 | +2 | Martial Devotion | 3 | — | — | — | — |
| 4 | +2 | Ability Score Improvement | 3 | — | — | — | — |
| 5 | +3 | Extra Attack | 4 | 2 | — | — | — |
| 6 | +3 | Devotion Archetype Feature | 4 | 2 | — | — | — |
| 7 | +3 | Aura of Intervention | 4 | 3 | — | — | — |
| 8 | +3 | Ability Score Improvement | 4 | 3 | — | — | — |
| 9 | +4 | — | 4 | 3 | 2 | — | — |
| 10 | +4 | Devotion Archetype Feature | 4 | 3 | 2 | — | — |
| 11 | +4 | Seasoned Fighting Style | 4 | 3 | 3 | — | — |
| 12 | +4 | Ability Score Improvement | 4 | 3 | 3 | — | — |
| 13 | +5 | — | 4 | 3 | 3 | 1 | — |
| 14 | +5 | Devotion Archetype Feature | 4 | 3 | 3 | 1 | — |
| 15 | +5 | Spell and Steel | 4 | 3 | 3 | 2 | — |
| 16 | +5 | Ability Score Improvement | 4 | 3 | 3 | 2 | — |
| 17 | +6 | — | 4 | 3 | 3 | 3 | 1 |
| 18 | +6 | Knight's Benediction | 4 | 3 | 3 | 3 | 1 |
| 19 | +6 | Ability Score Improvement | 4 | 3 | 3 | 3 | 2 |
| 20 | +6 | Unending Conviction | 4 | 3 | 3 | 3 | 2 |

**Quick Build.** Strength highest, then Charisma. Soldier background.

**Proficiencies.** Armor: All armor, Shields. Weapons: simple weapons, martial weapons. Tools: none. Saving Throws: Charisma, Constitution. Skills: choose two from Athletics, Insight, Intimidation, Medicine, Persuasion, Religion.
**Equipment.** (a) a martial weapon and shield or (b) two martial weapons; (a) 5 javelins or (b) a simple weapon; (a) an explorer's pack or (b) a dungeoneer's pack; (a) a chain shirt and a holy symbol related to your home region.

**Aetherial Arms (1st).** As a bonus action, infuse weapon, shield, or armour for 1 minute: Weapon (attacks deal bonus radiant damage = PB); Shield (AC bonus = half PB, round down); Armor (damage you take is reduced by your PB). Uses = PB; one item at a time (two at 9th). Refreshed on a long rest.
**Sworn Protector (1st).** Bonus action to swear protection to an ally within 3 m: while within 3 m, they have resistance to all damage but you take the same damage they take. Bonus action to end or move the oath.
**Fighting Style (2nd).** Choose Blessed Warrior (two cleric cantrips, CHA-based); Blind Fighting (blindsight 3 m); Defense (+1 AC in armor); Dueling (+2 one-handed damage); Great Weapon Fighting; Interception (reaction, reduce damage to an ally within 1.5 m by 1d10 + PB; need a shield or weapon); Protection (reaction, disadvantage on an attack vs an ally within 1.5 m; need a shield).
**Spellcasting (2nd).** Charisma (cleric-style). Spell save DC = 8 + PB + CHA mod; attack = PB + CHA mod. Prepare CHA modifier + half paladin level (round down, min 1). Focus: a holy symbol.
**Martial Devotion (subclass, 3rd).** Choose Arms Master, Great Knight, or Crusader. Features at 3rd, 6th, 10th, 14th.
**Ability Score Improvement (4th, 8th, 12th, 16th, 19th).** +2 to one or +1 to two (max 20).
**Extra Attack (5th).** Attack twice when you take the Attack action.
**Aura of Intervention (7th).** A 3 m aura (not through total cover): when an allied creature in it drops to 0 HP, reaction to make them drop to 1 HP instead (once per long rest per creature). At 18th, range 9 m.
**Seasoned Fighting Style (11th).** Choose a second Fighting Style.
**Spell and Steel (15th).** When you cast a spell, use your bonus action to make a melee weapon attack.
**Knight's Benediction (18th).** At the start of each turn, if at half HP or less (and not 0), regain HP = 5 + CON modifier.
**Unending Conviction (20th).** When you roll initiative with no Aetherial Arms uses left, gain 2 uses.

## Paladin — Subclass: Arms Master
- Sword Oath (3rd): while Aetherial Arms empowers your weapon, it sheds bright light in a 6 m radius + 6 m dim, and gains an attack bonus = half your PB.
- Aura of Valor (6th): a 3 m aura (not through total cover); you and allies in it gain a bonus to saves = your CHA modifier (min +1) while you're conscious. At 18th, range 9 m.
- Rage of Halone (10th): while Aetherial Arms empowers your weapon, bonus action to attack with it.
- Spirits Within (14th): while Aetherial Arms empowers your weapon, it deals bonus radiant damage = your CHA modifier.

## Paladin — Subclass: Great Knight
- Shield Oath (3rd): while Aetherial Arms empowers your shield, it sheds bright light in a 6 m radius + 6 m dim, and the shield's bonus AC is increased by your full PB (instead of half).
- Aura of Truth (6th): a 3 m aura; an enemy entering it makes a CHA save or has its intentions revealed and disadvantage on its next attack against you (invisible creatures that fail are revealed). At 18th, range 9 m.
- Sentinel (10th): while Aetherial Arms empowers your shield and you have a Sworn Protector target, reaction to apply your shield's bonus AC to them while in range until the start of your next turn.
- Passage of Arms (14th): while your shield is empowered, as an action all allies in a 9 m cone take reduced damage = PB + CHA modifier until the start of your next turn. Ends the current Aetherial Arms effect.

## Paladin — Subclass: Crusader
- Stave Oath (3rd): a pool of points = your PB; spend points equal to a paladin spell's level to cast it instead of a slot. Recovered on a long rest.
- Aura of Faith (6th): a 3 m aura; when you cast a paladin spell, bonus action to heal yourself and up to half-PB creatures (round down) for HP = your CHA modifier. At 18th, range 9 m.
- Chivalrous Casting (10th): when you cast a spell using a slot, gain Stave Oath points = half the spell level (round down, min 1). Not from Stave Oath casts.
- Requiescat (14th): when you cast a spell, spend Stave Oath points = the spell's level to apply Careful Spell (up to CHA-modifier creatures auto-succeed their save) or Quickened Spell (action-cast spell becomes a bonus action). No Stave Oath points gained from a manipulated cast.

# PICTOMANCER
**Hit Die:** d8 | **Saving Throws:** Wisdom, Charisma | **Spellcasting:** Charisma (known)

**Flavor.** A few flourishes bring a fairy to life to distract foes; bold brush-swings conjure a giant hammer that topples an opponent; quick strokes spread the dungeon walls with greenery and flowers to repel a relentless foe. Wandering Pictomancers seek new experiences to expand their imaginations — and their magic — weaving aether into wondrous art and wicked spells.
- Arts of a Folk Hero: the Sharlayan Archon Relm became the first pictomancer, teaching students to seek experiences and do good.
- Not Just a Brush: they wield brush-modified staves and a palette to capture and manipulate aether.
- Creating a Pictomancer: the more they've seen and done, the more powerful their imagination.

**HP_ref (d8):** 1:8 | 2:13 | 3:18 | 4:23 | 5:28 | 6:33 | 7:38 | 8:43 | 9:48 | 10:53 | 11:58 | 12:63 | 13:68 | 14:73 | 15:78 | 16:83 | 17:88 | 18:93 | 19:98 | 20:103. (Default PF = HP_ref[N] + CON mod x N.)

**Progression — spell slots per level**
| Lvl | PB | Cantrips | Spells Known | Features | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | +2 | 3 | 4 | Spellcasting, Sketchwork | 2 | — | — | — | — | — | — | — | — |
| 2 | +2 | 3 | 5 | Aetherial Studio, Smudge | 3 | — | — | — | — | — | — | — | — |
| 3 | +2 | 3 | 6 | Artistic Motif, Aetheric Palette | 4 | 2 | — | — | — | — | — | — | — |
| 4 | +2 | 4 | 7 | Ability Score Improvement | 4 | 3 | — | — | — | — | — | — | — |
| 5 | +3 | 4 | 8 | Subtractive Palette, Tempera Coat | 4 | 3 | 2 | — | — | — | — | — | — |
| 6 | +3 | 4 | 9 | Artistic Motif Feature | 4 | 3 | 3 | — | — | — | — | — | — |
| 7 | +3 | 4 | 10 | — | 4 | 3 | 3 | 1 | — | — | — | — | — |
| 8 | +3 | 4 | 11 | Ability Score Improvement | 4 | 3 | 3 | 2 | — | — | — | — | — |
| 9 | +4 | 4 | 12 | Palette Preparation, Tempera Coat Improvement (1d8) | 4 | 3 | 3 | 3 | 1 | — | — | — | — |
| 10 | +4 | 5 | 14 | Artistic Motif Feature | 4 | 3 | 3 | 3 | 2 | — | — | — | — |
| 11 | +4 | 5 | 15 | — | 4 | 3 | 3 | 3 | 2 | 1 | — | — | — |
| 12 | +4 | 5 | 15 | Ability Score Improvement | 4 | 3 | 3 | 3 | 2 | 1 | — | — | — |
| 13 | +5 | 5 | 16 | Tempera Coat (1d10) | 4 | 3 | 3 | 3 | 2 | 1 | 1 | — | — |
| 14 | +5 | 5 | 17 | Artistic Motif Feature | 4 | 3 | 3 | 3 | 2 | 1 | 1 | — | — |
| 15 | +5 | 5 | 18 | — | 4 | 3 | 3 | 3 | 2 | 1 | 1 | 1 | — |
| 16 | +5 | 5 | 18 | Ability Score Improvement | 4 | 3 | 3 | 3 | 2 | 1 | 1 | 1 | — |
| 17 | +6 | 5 | 19 | Tempera Coat (1d12) | 4 | 3 | 3 | 3 | 2 | 1 | 1 | 1 | 1 |
| 18 | +6 | 5 | 20 | World Canvas | 4 | 3 | 3 | 3 | 3 | 1 | 1 | 1 | 1 |
| 19 | +6 | 5 | 20 | Ability Score Improvement | 4 | 3 | 3 | 3 | 3 | 2 | 1 | 1 | 1 |
| 20 | +6 | 5 | 20 | Recolor The World | 4 | 3 | 3 | 3 | 3 | 2 | 2 | 1 | 1 |
(The table's 6th/10th/14th archetype rows are printed as "Magical Discipline Feature" in the source but refer to the Artistic Motif.)

**Quick Build.** Charisma highest, then Constitution. Folk Hero background. Mage Hand, Prestidigitation, Produce Flame cantrips; Arms of Hadar, Find Familiar, Healing Word, Mage Armor spells.

**Proficiencies.** Armor: none. Weapons: Daggers, Darts, Slings, Quarterstaffs, Maces, Light Crossbows. Tools: Painter's supplies. Saving Throws: Wisdom, Charisma. Skills: choose two from Arcana, Investigation, Insight, Perception, Performance, Persuasion.
**Equipment.** (a) a dagger; (a) a light crossbow and 20 bolts; a brush-based spellcasting focus; painter's supplies; (a) an explorer's pack or (b) a scholar's pack.

**Spellcasting.** Charisma. Spell save DC = 8 + PB + CHA mod; attack = PB + CHA mod. Known caster (Spells Known column); on level up you may replace one known spell. Ritual casting if the spell has the ritual tag and is prepared. Focus: a staff/stave/wand (often brush-and-palette).
**Sketch Work (1st).** Action to conjure an inanimate nonmagical object you've seen, in hand or within 3 m, no larger than ~0.9 m per side and ~4.5 kg, radiating dim light to 1.5 m. Disappears after 1 hour, when reused, or if it takes/deals damage.
**Aetherial Studio (2nd).** When you expend a spell slot, leave a 3 m sphere of aetherial paint (difficult terrain for non-allies) until the end of your next turn; used by various features.
**Smudge (2nd).** While in an Aetherial Studio field, bonus action to dispel it, gain 3 m movement and Disengage until end of turn.
**Artistic Motif (subclass, 3rd).** Choose Creature Realism, Weapon Expressionism, or Scenery Impressionism. Features at 3rd, 6th, 10th, 14th.
**Aetheric Palette (3rd).** Points = your PB; when you cast a spell, spend points = the spell level instead of a slot (no paint field left behind). Recovered on a long rest.
**Ability Score Improvement (4th, 8th, 12th, 16th, 19th).** +2 to one or +1 to two (max 20).
**Subtractive Palette (5th).** When you cast a damaging spell while inside or within 6 m of an Aetherial Studio field, dispel it to add your CHA modifier to the spell's damage (once for multi-hit spells).
**Tempera Coat (5th).** While in an Aetherial Studio field, bonus action to dispel it and gain temp HP = 1d6 + CHA modifier (fade after 1 minute). Die grows: d8 at 9th, d10 at 13th, d12 at 17th.
**Palette Preparation (9th).** When you roll initiative, set up a paint field as though you used Aetherial Studio.
**World Canvas (18th).** When you expend a slot and activate Aetherial Studio, you may place the field at a point within 9 m instead. Also, as an action create a paint field as though you expended a slot; uses = PB, recovered on a long rest.
**Recolor The World (20th).** Your paint fields last up to 1 minute and you can have up to three at a time.

## Pictomancer — Subclass: Creature Realism
- Twisting Traits (3rd): creatures you summon/create gain one — Dangerous (attacks deal bonus damage = your CHA modifier); Indomitable (AC increased by your PB); Swiftness (movement speed +6 m, including fly/swim). (Source merges "Indomitable Swiftness" into one row; presented as the two effects it describes.)
- Touchup Work (6th): while in a paint field, bonus action to dispel it and heal your summoned creature an amount equal to Tempera Coat's temp HP.
- Stable Creations (10th): while concentrating on a conjuration spell, your concentration can't be broken by taking damage.
- Beasts of Lore (14th): summoned creatures gain one — Enduring Presence (30 temp HP); Inspiring Presence (allies attacking within 6 m get +1d4 to attack rolls); Unnerving Presence (creatures attacking within 6 m get -1d4 to attack rolls).

## Pictomancer — Subclass: Weapon Expressionism
- Artist of War (3rd): action to create a magical melee weapon in an empty hand (you're proficient; counts as magical; usable as your spellcasting focus). Also gain proficiency with light and medium armor and shields.
- Heroic Effects (3rd): bonus action to select a weapon within 9 m; for 1 minute it deals bonus damage = your CHA modifier (one weapon at a time; a second at 9th level).
- Extra Attack (6th): attack twice when you take the Attack action; you can replace one attack with a cantrip.
- Prismatic Defense (10th): while protected by Tempera Coat, resistance to all damage except psychic.
- Polishing Strike (14th): when a creature benefiting from Heroic Effect hits with their weapon, reaction to expend a slot — the weapon deals bonus force damage = CHA modifier + #d8, # = the slot level.

## Pictomancer — Subclass: Scenery Impressionism
- Aetherial Scenery (3rd): while in a paint field, bonus action to rework it into a 3 m radius sphere within 6 m for 1 minute; specify up to PB creatures — attacks against them within it have disadvantage. Only one active at a time.
- Colour Your World (6th): while in a paint field, bonus action; a creature makes a CHA save vs your spell save DC or becomes vulnerable to fire, cold, lightning, or thunder (your choice) until the end of your next turn (advantage on the save if already immune/resistant).
- Tempera Grassa (10th): Tempera Coat can grant its temp HP to up to PB creatures.
- Landscape Mastery (14th): Aetherial Scenery can be up to a 6 m radius sphere; creatures affected by it take reduced damage = your CHA modifier.

# REAPER
**Hit Die:** d10 | **Saving Throws:** Strength, Wisdom | **Spellcasting:** Wisdom (prepared, half-caster) | **Languages:** Abyssal

**Flavor.** A black-draped figure cuts down realm-harmers one by one. Two black figures — a reaper and their void ally — take down a beast in tandem. A shadowed caster rains destruction while a haunting specter keeps invaders busy. Believed lost during the Garlean magitek revolution, reapers still combine void power and deadly scythes from the shadows.
- Allies From Beyond: once Garlean special forces and assassins who forged voidsent contracts; today they operate as mercenaries or alone.
- Dark Vows: they draw power from the Void Avatar, offering life force in exchange for a macabre momento to channel dark magic.
- Creating a Reaper: consider how you formed your voidsent contract and where you learned to balance martial prowess with dark magic.

**HP_ref (d10):** 1:10 | 2:16 | 3:22 | 4:28 | 5:34 | 6:40 | 7:46 | 8:52 | 9:58 | 10:64 | 11:70 | 12:76 | 13:82 | 14:88 | 15:94 | 16:100 | 17:106 | 18:112 | 19:118 | 20:124. (Default PF = HP_ref[N] + CON mod x N.)

**Progression — spell slots per level**
| Lvl | PB | Features | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|---|
| 1 | +2 | Dark Alliance | — | — | — | — | — |
| 2 | +2 | Fighting Style, Spellcasting | 2 | — | — | — | — |
| 3 | +2 | Reaper Archetype, Enshroud | 3 | — | — | — | — |
| 4 | +2 | Ability Score Improvement | 3 | — | — | — | — |
| 5 | +3 | Extra Attack | 4 | 2 | — | — | — |
| 6 | +3 | Sixth Sense | 4 | 2 | — | — | — |
| 7 | +3 | Archetype Feature | 4 | 3 | — | — | — |
| 8 | +3 | Ability Score Improvement | 4 | 3 | — | — | — |
| 9 | +4 | Harvest Moon | 4 | 3 | 2 | — | — |
| 10 | +4 | Death's Design | 4 | 3 | 2 | — | — |
| 11 | +4 | Archetype Feature | 4 | 3 | 3 | — | — |
| 12 | +4 | Ability Score Improvement | 4 | 3 | 3 | — | — |
| 13 | +5 | Shadow Walk | 4 | 3 | 3 | 1 | — |
| 14 | +5 | Void Gaze | 4 | 3 | 3 | 1 | — |
| 15 | +5 | Archetype Feature | 4 | 3 | 3 | 2 | — |
| 16 | +5 | Ability Score Improvement | 4 | 3 | 3 | 2 | — |
| 17 | +6 | Dark Martyr | 4 | 3 | 3 | 3 | 1 |
| 18 | +6 | Gate of Tartarus | 4 | 3 | 3 | 3 | 1 |
| 19 | +6 | Ability Score Improvement | 4 | 3 | 3 | 3 | 2 |
| 20 | +6 | Vessel of Death | 4 | 3 | 3 | 3 | 2 |

**Quick Build.** Strength highest, then Wisdom. Folk Hero background.

**Proficiencies.** Armor: Light, Medium. Weapons: Simple, Martial. Tools: none. Saving Throws: Strength, Wisdom. Skills: choose two from Arcana, Athletics, Insight, Intimidation, Perception, Religion. Languages: Abyssal.
- Battle Scythe: Two-Handed, Finesse, 2d4 slashing, 20 gp.
**Equipment.** (a) Battle Scythe or (b) one martial melee weapon; (a) two Handaxes or (b) a Light Crossbow and 20 bolts; (a) scale mail or (b) leather armor; (a) a Dungeoneer's Pack or (b) an Explorer's Pack; a Momento bestowed by the voidsent.

**Dark Alliance (1st).** You contract a Void Avatar (statblock below). It acts on your turn (moves/reacts on its own but only Dodges unless you bonus-action command it; you may sacrifice an attack to command it to Attack). At 0 HP its essence returns to your momento; action + a 1st-level-or-higher slot to reform it (1 minute, full HP). Resummon on a long rest.
- *Void Avatar* — Medium Fiend (Voidsent). AC 13 + PB. HP 5 + four times your class level (Hit Dice [d6s] = your Reaper level). Speed 9 m (hover). STR 14(+2) DEX 14(+2) CON 15(+2) INT 8(-1) WIS 14(+2) CHA 11(0). Senses darkvision 18 m, passive Perception 12. Languages understands its summoner's languages but can't speak. PB = yours. Void Bond: add your PB to its checks/saves. Actions — Rend: melee weapon attack, your spell attack modifier to hit, reach 1.5 m, 9 (1d8 + 2 + PB) slashing.
**Fighting Style (2nd).** Choose Blind Fighting (blindsight 3 m); Defense; Dueling; Great Weapon Fighting; Interception (reduce damage to an ally within 1.5 m by 1d10 + PB; need a shield or weapon); Thrown Weapon Fighting; Two-Weapon Fighting.
**Spellcasting (2nd).** Wisdom. Spell save DC = 8 + PB + WIS mod; attack = PB + WIS mod. Prepare WIS modifier + Reaper level (min 1). Focus: your momento.
**Reaper Archetype (3rd).** Choose Lemure, Grim Keeper, or Doomsinger. Features at 3rd, 7th, 11th, 15th.
**Enshroud (3rd).** While your voidsent is active, bonus action to host it (it leaves the field, cloaking you): spend Hit Dice up to your PB and gain temp HP = the rolls. Bonus action to return it to the field or gain temp HP again.
**Ability Score Improvement (4th, 8th, 12th, 16th, 19th).** +2 to one or +1 to two (max 20).
**Extra Attack (5th).** Attack twice when you take the Attack action.
**Sixth Sense (6th).** Cast See Invisibility or Speak with Dead without a slot, once per day.
**Harvest Moon (9th).** As an action, creatures in a 3 m radius circle make a DEX save vs your Reaper save DC, taking weapon damage + 1d12 necrotic (half on success). While hosting your avatar, bonus necrotic = your WIS modifier.
**Death's Design (10th).** On a melee weapon hit, expend a Reaper slot — the creature makes a CHA save vs your Reaper save DC, 3d8 necrotic and frightened on a fail (half, not frightened on success); +1d8 per slot level above 1st.
**Shadow Walk (13th).** While hosting the avatar, bonus action to become incorporeal until end of turn (move through creatures/objects as difficult terrain; 5 (1d10) force and ejected if you end inside an object). Uses = WIS modifier, recovered on a long rest.
**Void Gaze (14th).** While hosting the avatar, gain 9 m of truesight.
**Dark Martyr (17th).** When reduced to 0 HP but not killed outright, reaction to dismiss your avatar and recover 4d8 + WIS modifier HP before falling prone. Can't resummon until a long rest.
**Gate of Tartarus (18th).** Cast Plane Shift without material components (not to banish an unwilling creature); once without ill effect, further uses before a long rest cause a level of exhaustion to all affected.
**Vessel of Death (20th).** You always have the benefit of hosting the void avatar.

## Reaper — Subclass: Lemure
- Soul Slice (3rd): on a melee weapon hit, expend a Reaper slot — all creatures within 1.5 m of the target make a DEX save vs your Reaper save DC, 2d6 necrotic (half on success); +1d6 per slot above 1st. While hosting the avatar, the area becomes a 4.5 m cone from the target.
- Wraith Walk (7th): spend a 1st-level-or-higher slot to gain hovering and +1.5 m base speed for 1 minute; +1.5 m more per slot above 1st.
- Reaper's Rend (11th): while hosting the avatar, bonus action to order it to make an attack.
- Hands of Death (15th): while hosting the avatar, your melee reach increases by 1.5 m; creatures provoke opportunity attacks when entering your reach.

## Reaper — Subclass: Grim Keeper
- Shared Presence (3rd): when you cast a spell, you may treat your avatar as the point of origin (no damage to it). Three uses, recovered on a long rest.
- Death Perception (7th): while your avatar is within 30 m, communicate telepathically; as an action, see/hear through it until the start of your next turn (you're deaf and blind to your own senses meanwhile), gaining its special senses.
- Ravenous Rending (11th): your avatar makes two attacks when commanded to Attack.
- Gluttony (15th): as an action, imbue the avatar with necrotic energy — a hostile creature moving within 3 m of it for the first time on a turn makes a DEX save vs your Reaper save DC, 20 necrotic (half on success); fades after dealing 60 total. Uses = half PB (round down), recovered on a long rest.

## Reaper — Subclass: Doomsinger
- Soulsow (3rd): when a hostile creature dies within 9 m, capture its soul in your momento (max = PB; dissipate on a long rest). Cast a Reaper spell by spending souls = twice the spell's level. While hosting the avatar, capture range is 18 m.
- Bonus Cantrip (3rd): you know Toll the Dead.
- Keeper of Shadowy Secrets (7th): proficiency in one of Arcana, History, Insight, Medicine, Religion (expertise if already proficient).
- Void Curse (11th): while hosting the avatar, bonus action to spend 2 souls and curse a creature within 9 m — CHA save vs your Reaper save DC or its next save takes a penalty = your PB.
- Hell's Regress (15th): when hit by a melee weapon attack, reaction to spend 1 soul and teleport up to 9 m to a space you can see (no soul needed while hosting the avatar).

# RED MAGE (Crimson Mage)
**Hit Die:** d8 | **Saving Throws:** Dexterity, Charisma | **Spellcasting:** Charisma (known) | **Resource:** Flair points

**Flavor.** Like a lightning bolt streaking through the battlefield, she makes quick work of foe after foe; at the first sign of danger, the crimson beauty flips over the head of the foe behind her, letting loose a wave of energy. A confident veteran unleashes spell after spell in quick succession, drawing on countless elements until his foe is annihilated. Like a flower amongst weeds, the red mage leads allies into battle, turning friends into perfect dancing partners and empowering them to match their grace. Red Mages mix black and white magic with focused swordplay and style.
- Crimson Mage: fairy tales of Gyr Abania speak of mages clothed in crimson who protect the good of the world by drawing on both white and black magic while mixing martial prowess into a flawless battle style.
- It's Not About Fame: despite their flashy style, those who take the Red do so to protect the good in the world and bring wrongdoers to justice.
- Creating a Red Mage: consider why you set out (oppression, a plot endangering home, or the thrill of adventure) and where you learned your skills (old tomes or a mentor).

**HP_ref (d8):** 1:8 | 2:13 | 3:18 | 4:23 | 5:28 | 6:33 | 7:38 | 8:43 | 9:48 | 10:53 | 11:58 | 12:63 | 13:68 | 14:73 | 15:78 | 16:83 | 17:88 | 18:93 | 19:98 | 20:103. (Default PF = HP_ref[N] + CON mod x N.)

**Progression — spell slots per level** (verbatim from source; this homebrew full-caster table sets 5th-level slots to 3 from 16th)
| Lvl | PB | Flair | Cantrips | Spells Known | Features | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | +2 | 1 | 4 | 2 | Spellcasting, Dual Casting | 2 | — | — | — | — | — | — | — | — |
| 2 | +2 | 2 | 4 | 3 | Red Mage Style, Style Feature | 3 | — | — | — | — | — | — | — | — |
| 3 | +2 | 3 | 4 | 4 | — | 4 | 2 | — | — | — | — | — | — | — |
| 4 | +2 | 4 | 5 | 5 | Ability Score Improvement | 4 | 3 | — | — | — | — | — | — | — |
| 5 | +3 | 4 | 5 | 6 | Extra Attack | 4 | 3 | 2 | — | — | — | — | — | — |
| 6 | +3 | 4 | 5 | 7 | Style Feature | 4 | 3 | 3 | — | — | — | — | — | — |
| 7 | +3 | 4 | 5 | 8 | — | 4 | 3 | 3 | 1 | — | — | — | — | — |
| 8 | +3 | 4 | 5 | 9 | Ability Score Improvement | 4 | 3 | 3 | 2 | — | — | — | — | — |
| 9 | +4 | 4 | 5 | 10 | — | 4 | 3 | 3 | 3 | 1 | — | — | — | — |
| 10 | +4 | 5 | 6 | 11 | Style Feature | 4 | 3 | 3 | 3 | 2 | — | — | — | — |
| 11 | +4 | 5 | 6 | 12 | — | 4 | 3 | 3 | 3 | 2 | 1 | — | — | — |
| 12 | +4 | 6 | 6 | 12 | Ability Score Improvement | 4 | 3 | 3 | 3 | 2 | 1 | — | — | — |
| 13 | +5 | 6 | 6 | 13 | — | 4 | 3 | 3 | 3 | 2 | 1 | 1 | — | — |
| 14 | +5 | 7 | 6 | 13 | Style Feature | 4 | 3 | 3 | 3 | 2 | 1 | 1 | — | — |
| 15 | +5 | 7 | 6 | 14 | — | 4 | 3 | 3 | 3 | 2 | 1 | 1 | 1 | — |
| 16 | +5 | 8 | 6 | 14 | Ability Score Improvement | 4 | 3 | 3 | 3 | 3 | 1 | 1 | 1 | — |
| 17 | +6 | 8 | 6 | 15 | — | 4 | 3 | 3 | 3 | 3 | 1 | 1 | 1 | 1 |
| 18 | +6 | 9 | 6 | 15 | Battle Flourish | 4 | 3 | 3 | 3 | 3 | 1 | 1 | 1 | 1 |
| 19 | +6 | 9 | 6 | 15 | Ability Score Improvement | 4 | 3 | 3 | 3 | 3 | 2 | 1 | 1 | 1 |
| 20 | +6 | 10 | 6 | 15 | Acceleration | 4 | 3 | 3 | 3 | 3 | 2 | 2 | 1 | 1 |

**Quick Build.** Charisma highest, then Dexterity. Folk Hero background. Fire Bolt, Jolt, Mage Hand, Prestidigitation cantrips; 1st-level Chromatic Orb and Cure Wounds.

**Proficiencies.** Armor: Light, Medium. Weapons: simple weapons, short swords, rapiers. Tools: two sets of Artisan's Tools. Saving Throws: Dexterity, Charisma. Skills: choose two from Athletics, Acrobatics, Arcana, History, Insight, Persuasion.
**Equipment.** (a) leather armour or (b) hide armour; (a) a rapier; (a) a light crossbow and 20 bolts or (a) a simple weapon; a spellcasting focus; (a) an explorer's pack or (b) a dungeoneer's pack.

**Spellcasting.** Charisma. Spell save DC = 8 + PB + CHA mod; attack = PB + CHA mod. Known caster (4 cantrips at 1st, 2 first-level spells; learn more per table; may replace one known spell on level up). Ritual casting if the spell has the ritual tag. Focus: a magically conductive stone in a decorative mount or similar.
**Flair Points (1st).** You have flair points per the Flair column; regained on a short or long rest.
**Dual Cast (1st).** When you cast a spell with a casting time of 1 action, spend 1 flair point to change the casting time to 1 bonus action for that casting (not with a spell higher than 4th level). Standard bonus-action-casting rules apply (no other spell that turn except a cantrip with a 1-action casting time).
**Combat Style (subclass, 2nd).** Choose Sword Dancer, Spell Slinger, or Battle Rose. Features at 2nd, 6th, 10th, 14th.
**Ability Score Improvement (4th, 8th, 12th, 16th, 19th).** +2 to one or +1 to two (max 20).
**Extra Attack (5th).** Attack twice when you take the Attack action.
**Battle Flourish (18th).** When you roll initiative with 0 flair points remaining, recover 1d4 flair points.
**Acceleration (20th).** You may cast two spells using Dual Cast (rather than one spell and one cantrip). Once per long rest.

## Red Mage — Subclass: Sword Dancer
Weave magic and might into a deadly dance.
- Corps-a-corps (2nd): as a bonus action, spend 1 flair point and select a target within 9 m; move in a straight line toward it, stopping at the first creature in your path (no opportunity attacks), and make a weapon attack dealing +1d8 piercing on a hit.
- Heroic Charm (6th): spend 1 flair point to reroll any Charisma-based ability check; gain proficiency in a Charisma skill of your choice.
- Displacement (10th): after the Attack action, spend 1 flair point to leap up to 9 m straight backward through the air (over Medium-or-smaller creatures; stopped by larger; no opportunity attacks), then make a ranged spell attack against your attack's target for 2d8 + CHA modifier force.
- Enchanted Blade (14th): after attuning to a one-handed weapon for 1 hour (magical or not), summon it to hand as an action; spend 1 flair point (declared before the attack roll) to deal +2d8 force on each damage roll with it.

## Red Mage — Subclass: Spell Slinger
Master rapid casting.
- Manafication (2nd): as a bonus action, spend flair points equal to twice a spell's level in place of a spell slot.
- Charmed I'm Sure (6th): spend a flair point to gain advantage on a Charisma ability check.
- Quicksilver Casting (10th): if you deal damage to a target with a cantrip, spend 1 flair point to gain advantage on a ranged spell attack against it, or make it roll Dexterity saves against your spells with disadvantage, until the end of your turn.
- Liquification (14th): as a bonus action, spend a spell slot of any level to gain flair points equal to twice the slot level (not above your maximum).

## Red Mage — Subclass: Battle Rose
Support allies to fight more effectively.
- Dazzling Diversion (2nd): as an action, spend 1 flair point to distract a target in melee within 1.5 m; all melee weapon attacks by your allies against it gain advantage until your next turn.
- In Good Company (6th): spend 1 flair point to let one ally use your Charisma modifiers for Charisma checks for up to 5 minutes (share once; short rest to reuse).
- Embolden (10th): as an action, spend 1 flair point to empower all allies within 3 m; their damaging effects deal +1d8 damage until the end of your next turn.
- Follow My Lead (14th): as a bonus action, spend 2 flair points to move an ally lower in initiative up to act directly after you (once; short rest to reuse).

# SAGE
**Hit Die:** d6 | **Saving Throws:** Intelligence, Wisdom | **Spellcasting:** Intelligence (prepared)

**Flavor.** Surrounded by foes, a steel-hearted fighter feels the tide shifting away — then a goblin's blade is blocked by a magical wall, a sage weaving magic to protect an ally. From the backline, each blast of magic sends excess aether flowing into allies, filling them with new energy. A beam of aether strikes a monstrous foe; its limbs swing heavily, eyes droop, stomach churns — something is wrong, and its advantage is lost. Sages are highly skilled, effective healers; with a sage at your back you can breathe easier no matter how dire the situation.
- To Heal and Protect: sages master the intersection of natural and formal healing disciplines, driven by a burning desire to help others.
- Stones of Eld: ancient healers used Adderstones to form leylines for powerful healing; these form the basis of the Sage's greatest tool — the Nouliths, four enhanced adderstones controlled by a held anchor stone, weaving sigils to heal and harm.
- Creating a Sage: most had success in medicine first or were mentored young; a strong understanding of self and healing arts is needed to even wield the nouliths.

**HP_ref (d6):** 1:6 | 2:10 | 3:14 | 4:18 | 5:22 | 6:26 | 7:30 | 8:34 | 9:38 | 10:42 | 11:46 | 12:50 | 13:54 | 14:58 | 15:62 | 16:66 | 17:70 | 18:74 | 19:78 | 20:82. (Default PF = HP_ref[N] + CON mod x N.)

**Progression — spell slots per level**
| Lvl | PB | Cantrips | Features | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | +2 | 3 | Dosis, Eukrasia, Spellcasting | 2 | — | — | — | — | — | — | — | — |
| 2 | +2 | 3 | Kardia, Sagely Specialization | 3 | — | — | — | — | — | — | — | — |
| 3 | +2 | 3 | — | 4 | 2 | — | — | — | — | — | — | — |
| 4 | +2 | 4 | Ability Score Improvement | 4 | 3 | — | — | — | — | — | — | — |
| 5 | +3 | 4 | Teichos | 4 | 3 | 2 | — | — | — | — | — | — |
| 6 | +3 | 4 | Specialization Feature | 4 | 3 | 3 | — | — | — | — | — | — |
| 7 | +3 | 4 | — | 4 | 3 | 3 | 1 | — | — | — | — | — |
| 8 | +3 | 4 | Ability Score Improvement | 4 | 3 | 3 | 2 | — | — | — | — | — |
| 9 | +4 | 4 | — | 4 | 3 | 3 | 3 | 1 | — | — | — | — |
| 10 | +4 | 5 | Specialization Feature | 4 | 3 | 3 | 3 | 2 | — | — | — | — |
| 11 | +4 | 5 | — | 4 | 3 | 3 | 3 | 2 | 1 | — | — | — |
| 12 | +4 | 5 | Ability Score Improvement | 4 | 3 | 3 | 3 | 2 | 1 | — | — | — |
| 13 | +5 | 5 | — | 4 | 3 | 3 | 3 | 2 | 1 | 1 | — | — |
| 14 | +5 | 5 | Specialization Feature | 4 | 3 | 3 | 3 | 2 | 1 | 1 | — | — |
| 15 | +5 | 5 | — | 4 | 3 | 3 | 3 | 2 | 1 | 1 | 1 | — |
| 16 | +5 | 5 | Ability Score Improvement | 4 | 3 | 3 | 3 | 2 | 1 | 1 | 1 | — |
| 17 | +6 | 5 | — | 4 | 3 | 3 | 3 | 2 | 1 | 1 | 1 | 1 |
| 18 | +6 | 5 | Icarus | 4 | 3 | 3 | 3 | 3 | 1 | 1 | 1 | 1 |
| 19 | +6 | 5 | Ability Score Improvement | 4 | 3 | 3 | 3 | 3 | 2 | 1 | 1 | 1 |
| 20 | +6 | 5 | Somanoutic Recovery | 4 | 3 | 3 | 3 | 3 | 2 | 2 | 1 | 1 |

**Quick Build.** Intelligence highest, then Constitution. Sage background. Mage Hand, Mending, Prestidigitation cantrips; 1st-level Healing Word, Mage Armor, Magic Missile.

**Proficiencies.** Armor: none. Weapons: daggers, darts, slings, quarterstaffs, light crossbows. Tools: none. Saving Throws: Intelligence, Wisdom. Skills: choose two from Arcana, History, Insight, Investigation, Medicine, Religion.
**Equipment.** (a) a quarterstaff or (b) a dagger; (a) a light crossbow and 20 bolts or (a) a simple weapon; (a) a component pouch or (b) an arcane focus; (a) a scholar's pack or (b) an explorer's pack; a set of four nouliths and an anchor stone.

**Spellcasting.** Intelligence. Spell save DC = 8 + PB + INT mod; attack = PB + INT mod. Prepare INT modifier + Sage level spells (min 1) from the Sage list; change on a long rest. Ritual casting if prepared and ritual-tagged. Focus: a set of nouliths and your anchor stone.
**Dosis (1st).** As an action, order a noulith to make a ranged spell attack (your ranged spell attack bonus) against a creature within 18 m; on a hit each beam deals 1d8 force. Beams: two at 5th, three at 11th, four at 17th (different targets allowed). Counts as casting a cantrip.
**Eukrasia (1st).** When you cast a spell that restores HP, you may instead grant the target temp HP equal to the healing + your INT modifier.
**Kardia (2nd).** As a bonus action, form a lasting aetherial link with one willing creature within 9 m (one at a time; lasts until reused). When you cast a spell using a spell slot, that creature heals #d4 HP, # = your PB.
**Sagely Specialization (subclass, 2nd).** Choose Savant, Philosopher, or Erudite. Features at 2nd, 6th, 10th, 14th.
**Ability Score Improvement (4th, 8th, 12th, 16th, 19th).** +2 to one or +1 to two (max 20).
**Teichos (5th).** As an action, create a 3 m x 3 m sheet of aether (2.5 cm thick) centered on a point within 9 m, lasting 1 minute. It has AC = your spell save DC and 10 HP, supports a standing creature, and gives three-quarters cover to ranged attacks/spells through it (translucent). Pushing through it requires a STR (Athletics) check vs your spell save DC. Additional sheets at 10th, 15th, 20th; chain them outside range if each new center is within 6 m of the previous; dismiss any number as a bonus action.
**Icarus (18th).** Gain a flying speed of 18 m.
**Somanoutic Recovery (20th).** When reduced to 0 HP but not killed outright, your nouliths encase you in an impenetrable barrier (no damage) until the end of your next turn and you recover 3d8 + INT modifier HP. Once; recovered on a long rest.

## Sage — Subclass: Savant
Reach the pinnacle of healing magic.
- Diagnosis (2nd): when you use a spell of 1st level or higher to restore HP, the creature regains additional HP = 2 + the spell's level. If cast via Eukrasia, you may apply this additional healing to HP instead of temp HP.
- Inverse Kardion (6th): when you cast a 1st-level-or-higher spell restoring HP to a creature other than you, you regain HP = 2 + the spell's level.
- Pepsis (10th): as a bonus action, convert all temp HP you granted to creatures within 18 m into healing = those temp HP + your INT modifier.
- Perfected Eukrasia (14th): while using Eukrasia, treat all healing dice as their maximum (e.g. 2d6 = 12).

## Sage — Subclass: Philosopher
Prevent damage through defensive maneuvers.
- Soteria (2nd): your self-targeting spells can also target a creature affected by Kardia. From 6th level, creatures under Kardia gain a bonus to saves = your PB.
- Barrier Parry (6th): when a creature under your Kardia is the target of an attack, reaction to grant it +2 AC until the start of your turn. Uses = PB, refreshed on a long rest.
- Kardion Network (10th): apply Kardia to up to four creatures (all receive Kardia healing; self-targeted spells still affect only one).
- Haima (14th): as an action, weave a barrier giving a Kardia creature half cover for 1 minute (+2 AC and +2 to Dexterity saves); more than one creature may be affected. Uses = PB, recovered on a long rest.

## Sage — Subclass: Erudite
Weaken foes by destabilizing their aether.
- Eukrasian Dosis (2nd): when you land a Dosis attack, you may overcharge it for bonus damage = your INT modifier; the creature makes an INT save or is poisoned 1 minute (re-save as an action on its turn). Uses = PB, recovered on a short or long rest.
- Aether Sickness (6th): Eukrasian Dosis poison ignores poison immunity; attack rolls against a creature poisoned by it have advantage.
- Aether Burn (10th): a creature starting its turn poisoned by Eukrasian Dosis takes 2d4 + INT modifier necrotic; creatures not inherently immune/resistant to poison have disadvantage on saves vs the effect.
- Aether Plague (14th): use Eukrasian Dosis up to twice your PB times.

# SAMURAI (Hingashi)
**Hit Die:** d10 | **Saving Throws:** Strength, Wisdom | **Resource:** Sen charges (PB + WIS-based)

**Flavor.** With blade sheathed they watch the enemy form ranks and charge — then unleash a sweeping strike, cutting through with ease. Patiently awaiting the first move, they dodge the opening strike and deliver a ruthless counter. With wild speed and reckless abandon they charge in, cutting down foe after foe before retreating to do it all again. Samurai are highly skilled swordsmen who wield katanas and varied weapons with skillful, powerful strokes.
- The Hingashi Style: samurai trace their roots to the eastern Hingashi region, transcending a martial art into a true art form — strikes faster than the eye, blows that rip through armour with a single clean edge.
- A Crossing of Art and War: their signature weapon is the katana, formed by folding steel and honing a razor edge; artisans impart artistic flair, and wealthy merchants seek ceremonial pieces.
- Creating a Samurai: often from wartime — formal military instruction, a master's school, or self-taught with an inherited blade; consider why you became a wanderer.

**HP_ref (d10):** 1:10 | 2:16 | 3:22 | 4:28 | 5:34 | 6:40 | 7:46 | 8:52 | 9:58 | 10:64 | 11:70 | 12:76 | 13:82 | 14:88 | 15:94 | 16:100 | 17:106 | 18:112 | 19:118 | 20:124. (Default PF = HP_ref[N] + CON mod x N.)

**Progression**
| Lvl | PB | Features |
|---|---|---|
| 1 | +2 | Artful Combat, Unarmoured Defense, Fighting Style |
| 2 | +2 | Sen, Sword Artes |
| 3 | +2 | Way of the Blade |
| 4 | +2 | Ability Score Improvement |
| 5 | +3 | Extra Attack |
| 6 | +3 | Way Feature |
| 7 | +3 | Spirit Infusion |
| 8 | +3 | Ability Score Improvement |
| 9 | +4 | Precise Critical |
| 10 | +4 | Way Feature |
| 11 | +4 | Renaissance Warrior |
| 12 | +4 | Ability Score Improvement |
| 13 | +5 | Precise Critical (2 dice) |
| 14 | +5 | Way Feature |
| 15 | +5 | Whispers of the Kami |
| 16 | +5 | Ability Score Improvement |
| 17 | +6 | Precise Critical (3 dice) |
| 18 | +6 | Battle Field Artisan |
| 19 | +6 | Ability Score Improvement |
| 20 | +6 | Meikyo Shisui |

**Quick Build.** Strength highest, then Wisdom. Soldier background.

**Proficiencies.** Armor: Light, Medium. Weapons: simple weapons, martial weapons. Tools: none. Saving Throws: Strength, Wisdom. Skills: choose two from Athletics, Acrobatics, History, Insight, Intimidation.
**Equipment.** (a) a katana; (a) a short bow and 20 arrows; (a) a chain shirt or (b) leather armor or (c) a martial weapon; (a) an explorer's pack or (b) a dungeoneer's pack; a decorative scabbard for your katana.
- Katana: use the longsword statblock (per DMG p.41).

**Artful Combat (1st).** While wielding a versatile weapon with two hands, your weapon attacks crit on a roll of 19 or 20.
**Unarmoured Defense (1st).** While wearing no armor, AC = 10 + STR modifier + WIS modifier, or 10 + DEX modifier + WIS modifier. No shield.
**Fighting Style (1st).** Choose one: Archery (+2 ranged attack rolls); Blind Fighting (blindsight 3 m); Defense (+1 AC in armor); Dextrous Versatility (wielding a versatile weapon in two hands, it gains finesse and +1 to attack rolls; use its one-handed damage); Dueling (+2 damage one-handed, no other weapon); Great Weapon Fighting (reroll 1s/2s on two-handed/versatile melee damage); Two-Weapon Fighting (add ability modifier to the second attack's damage).
**Sen (2nd).** Manifest fighting spirit as Sen. Max Sen = PB + WIS modifier. On initiative, gain Sen = PB. As a bonus action, meditate to gain Sen = PB. After a battle, Sen remains for 1 minute.
**Sword Artes (2nd).** Sword Art DC = 8 + PB + STR or DEX modifier. (List at the end.)
**Way of the Blade (subclass, 3rd).** Choose Iaijutsu, Blademaster, or Ronin. Features at 3rd, 6th, 10th, 14th.
**Ability Score Improvement (4th, 8th, 12th, 16th, 19th).** +2 to one or +1 to two (max 20).
**Extra Attack (5th).** Attack twice when you take the Attack action.
**Spirit Infusion (7th).** As a bonus action, spend 2 Sen charges to change your weapon damage type for 1 minute to fire, cold, thunder, or lightning, and deal bonus damage = your PB.
**Precise Critical (9th).** Roll one additional weapon damage die on a melee critical hit (two dice at 13th, three at 17th).
**Renaissance Warrior (11th).** Add half your PB (round up) to any Intelligence, Wisdom, or Charisma check that doesn't already use your PB.
**Whispers of the Kami (15th).** Cast Augury, Detect Evil and Good, Speak with Dead, or Speak with Plants — each once; long rest to reuse.
**Battle Field Artisan (18th).** Your Artful Combat crit range increases to 18-20.
**Meikyo Shisui (20th).** When you roll initiative, begin with your maximum Sen charges.

## Samurai — Way of the Blade: Iaijutsu
Mastery of fundamentals and practiced techniques.
- Rallying Spirit (3rd): when you use a Sword Arte, gain temp HP = #d4, # = Sen charges spent.
- Steel Spirit (6th): add half your PB (round up) to any Strength, Dexterity, or Constitution check that doesn't already use your PB; running long-jump distance increases by feet equal to your STR modifier (about 0.3 m per point).
- Tsubame-gaeshi (10th): when you use a Sword Arte with more than one attack roll, use your bonus action for an additional attack.
- Spirit Cycle (14th): when a Sword Arte costing more than 1 Sen is used, regain half the Sen spent.

## Samurai — Way of the Blade: Blademaster
Defensive positioning and counterattacks.
- Strategic Edge (3rd): your opportunity attacks have advantage.
- Nothing Ventured (6th): advantage on Perception and Investigation checks when looking for traps and hidden passages.
- Know Thy Enemy (10th): when you make an opportunity attack, you attack twice.
- The Worm Turns (14th): you have two reactions per round in combat.

## Samurai — Way of the Blade: Ronin
Masterless, wild and swift.
- Rascally Wanderer (3rd): proficiency in Thieves' Tools and Sleight of Hand; when you make a melee weapon attack against a creature, it can't make opportunity attacks against you for the rest of your turn.
- Fleet of Foot (6th): base movement speed +3 m (applies to climb/swim speeds too).
- Wicked Speed (10th): advantage on initiative; until the end of your first turn your attacks have advantage and you have the Dash action's benefit.
- Turning Swallow Cut (14th): when you use the Attack action or a Sword Arte, spend movement to outmaneuver your target — +1 to attack and damage rolls per 3 m of movement spent.

## Samurai — Sword Artes List
- **Enpi** (2nd; 1 Sen): action; a ranged weapon attack at 9 m using blades of wind (roll as a melee weapon attack/damage), dealing thunder. At 5th level, two ranged attacks.
- **Gekko** (6th, Iaijutsu; 1 Sen): bonus action; until end of your next turn, melee weapon attacks deal bonus damage = your WIS modifier.
- **Hissatsu: Chiten** (3rd, Blademaster; 1 Sen): when a creature attacks you, reaction to make an opportunity attack against it.
- **Hissatsu: Gyoten** (6th, Ronin; 1 Sen): bonus action; Dash, and your first melee attack has advantage until end of turn.
- **Hissatsu: Kyuten** (9th, Iaijutsu; 2 Sen): bonus action; each creature within a 3 m radius makes a Dexterity save, taking your weapon damage (half on success).
- **Hissatsu: Shinten** (9th; 1 Sen): bonus action; make a melee weapon attack.
- **Hissatsu: Yaten** (3rd, Ronin; 1 Sen): bonus action; Disengage, and you may use Enpi without spending Sen until end of turn.
- **Iron Will** (10th, Blademaster; 2 Sen): when targeted by an attack, reaction to gain resistance to slashing, bludgeoning, and piercing until the start of your next turn.
- **Jinpu** (2nd; 1 Sen): action; a melee weapon attack adding your WIS modifier to the damage roll. At 5th level, two melee attacks.
- **Kasha** (10th, Ronin; 2 Sen): action; a melee weapon attack, then gain the Dodge action's benefit.
- **Mangetsu** (3rd, Iaijutsu; 2 Sen): action; a whirling attack — each creature within a 3 m radius makes a Dexterity save, taking your weapon damage (half on success).
- **Midare Setsugekka** (13th; 3 Sen): action; a melee weapon attack against a target; spend up to 3 additional Sen for one extra melee attack each (max four attacks total).
- **Mineuchi** (6th, Blademaster; 2 Sen): on a melee weapon hit, the target makes a Constitution save or is stunned until the end of your next turn.
- **Ogi Namikiri** (17th; 4 Sen): action; two melee weapon attacks — the first that hits is a critical hit.
- **Shifu** (2nd; 1 Sen): bonus action; melee weapon attacks until end of turn have advantage.
- **Tenka Goken** (14th, Iaijutsu; 3 Sen): action; select up to 3 creatures in a 9 m cone and make a weapon attack against each (may target the same creature multiple times).
- **Third Eye** (14th, Blademaster; # Sen): when targeted by an attack, reaction to spend up to 5 Sen, +1 AC per charge (declared before the roll is resolved).
- **Yukikaze** (14th, Ronin; 3 Sen): action; two melee weapon attacks; if one hits, the creature makes a Constitution save or attacks against it have advantage until the end of your next turn.
- **Zantetsuken** (20th; 8 Sen): bonus action to prepare, then as an action a melee weapon attack that crits on a die result of 10 or higher. On a 10+ result against a creature with a head, you sever a head (the creature dies if it can't survive without it). Immune creatures (immune to slashing, no/needs-no head, has legendary actions, or too big per GM) instead take +6d8 slashing. On a sub-10 hit, the target takes +6d8 slashing.

# SCHOLAR
**Hit Die:** d6 | **Saving Throws:** Intelligence, Wisdom | **Spellcasting:** Intelligence (spellbook, prepared) | **Resource:** Tactics uses

**Flavor.** Surrounded by foes, a fallen fighter feels doom looming — then a familiar aetherial rodent runs to their side and a blinding flash gives the opening to sway the battle. A warrior fights on, soothed by a nearby fey and pushed onward by a scholar's supportive power. A poisoned ranger awaits doom until a piercing voice orders the party into position, saving their life. Scholars control the battlefield with impeccable healing and a mind for tactics, turning a ragtag group into a proper fighting force.
- Aether Given Form: Scholars summon aetherial allies — the vicious carbuncle or the graceful Nymian fey — often splitting their power to support allies.
- Arcane Symbols: their magic derives from grimoires, using intricate diagrams and sigils to cast spells and summon allies.
- Creating a Scholar: skilled individuals trained alone or under a mentor, often with roots in organizations or the military; consider how you trained and why you set off.

**HP_ref (d6):** 1:6 | 2:10 | 3:14 | 4:18 | 5:22 | 6:26 | 7:30 | 8:34 | 9:38 | 10:42 | 11:46 | 12:50 | 13:54 | 14:58 | 15:62 | 16:66 | 17:70 | 18:74 | 19:78 | 20:82. (Default PF = HP_ref[N] + CON mod x N.)

**Progression — spell slots per level** (verbatim; this homebrew table's mid-level columns are intentionally irregular, matching Blue Mage)
| Lvl | PB | Cantrips | Features | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | +2 | 3 | Spellcasting, Tactics | 2 | — | — | — | — | — | — | — | — |
| 2 | +2 | 3 | Scholar Specialization, Aetherial Ally | 3 | — | — | — | — | — | — | — | — |
| 3 | +2 | 3 | — | 4 | 2 | — | — | — | — | — | — | — |
| 4 | +2 | 4 | Ability Score Improvement | 4 | 3 | — | — | — | — | — | — | — |
| 5 | +3 | 4 | — | 4 | 3 | 2 | — | — | — | — | — | — |
| 6 | +3 | 4 | Specialization Feature | 4 | 3 | 3 | — | — | — | — | — | — |
| 7 | +3 | 4 | — | 4 | 3 | 3 | 1 | — | — | — | — | — |
| 8 | +3 | 4 | Ability Score Improvement | 4 | 3 | 3 | 2 | — | — | — | — | — |
| 9 | +4 | 4 | — | 4 | 3 | 3 | 2 | 1 | — | — | — | — |
| 10 | +4 | 5 | Specialization Feature | 4 | 3 | 3 | 2 | 2 | — | — | — | — |
| 11 | +4 | 5 | — | 4 | 3 | 3 | 2 | 3 | 1 | — | — | — |
| 12 | +4 | 5 | Ability Score Improvement | 4 | 3 | 3 | 2 | 3 | 1 | — | — | — |
| 13 | +5 | 5 | — | 4 | 3 | 3 | 2 | 3 | 1 | 1 | — | — |
| 14 | +5 | 5 | Specialization Feature | 4 | 3 | 3 | 2 | 3 | 1 | 1 | — | — |
| 15 | +5 | 5 | — | 4 | 3 | 3 | 2 | 3 | 1 | 1 | 1 | — |
| 16 | +5 | 5 | Ability Score Improvement | 4 | 3 | 3 | 2 | 3 | 1 | 1 | 1 | — |
| 17 | +6 | 5 | — | 4 | 3 | 3 | 2 | 3 | 1 | 1 | 1 | 1 |
| 18 | +6 | 5 | Quicksilver Summoning | 4 | 3 | 3 | 3 | 3 | 1 | 1 | 1 | 1 |
| 19 | +6 | 5 | Ability Score Improvement | 4 | 3 | 3 | 3 | 3 | 2 | 1 | 1 | 1 |
| 20 | +6 | 5 | Grand Design | 4 | 3 | 3 | 3 | 3 | 2 | 2 | 1 | 1 |

**Quick Build.** Intelligence highest, then Constitution. Soldier background. Mage Hand, Prestidigitation, Ruin cantrips.

**Proficiencies.** Armor: none. Weapons: daggers, darts, slings, quarterstaffs, shortswords, light crossbows. Tools: none. Saving Throws: Intelligence, Wisdom. Skills: choose two from Arcana, History, Insight, Investigation, Medicine, Religion.
**Equipment.** (a) a quarterstaff or (b) a shortsword; (a) a dagger; (a) a light crossbow and 20 bolts or (a) a simple weapon; (a) a grimoire (your spellcasting focus); (a) a scholar's pack or (b) an explorer's pack.

**Spellcasting.** Intelligence (spellbook). Spell save DC = 8 + PB + INT mod; attack = PB + INT mod. Spellbook starts with six 1st-level Scholar spells; copying a found spell costs 2 hours and 50 gp per level (backup 1 hour, 10 gp/level). Prepare INT modifier + Scholar level spells (min 1) from your spellbook; change on a long rest. Each Scholar level, add two Scholar spells to your spellbook for free. Ritual casting if ritual-tagged. Focus: a grimoire or tome.
**Tactics (1st).** Uses = PB, regained on a short or long rest. Memorize tactics (list at the end) equal to your INT modifier (min 1); change on a long rest. Some tactics have prerequisites.
**Scholar Specialization (subclass, 2nd).** Choose Arcanist, Nymian, or Tactician. Features at 2nd, 6th, 10th, 14th.
**Aetherial Ally (2nd).** Summon an aetherial creature (statblocks below) when you finish a long rest (choose Carbuncle or Nymian Fey; a new summon replaces the old). It is friendly and obeys you. In combat it acts on your turn: moves and uses its reaction on its own but only Dodges unless you bonus-action command another action; you may sacrifice one of your attacks to command it to Attack. If incapacitated, it acts freely. At 0 HP it dissipates into a fog (intact 1 minute); use your action and a 1st-level-or-higher slot to revive it after 1 minute at full HP. Vanishes if you die.
**Ability Score Improvement (4th, 8th, 12th, 16th, 19th).** +2 to one or +1 to two (max 20).
**Quicksilver Summoning (18th).** Use your action to summon an aetherial ally. Once; recovered on a long rest.
**Grand Design (20th).** Recover half your expended Tactics uses when you roll initiative.

## Scholar — Subclass: Arcanist
Summon carbuncles and wear down foes.
- Stabilized Aether (2nd): your aetherial ally deals bonus damage = your INT modifier on its attacks.
- Aether Sight (6th): gain blindsight in a 3 m radius around your aetherial ally.
- Gemstone Summoner (10th): when you summon an ally, choose — Diamond (+2 AC); Moonstone (when a friendly creature within 3 m of the ally takes damage, it may reaction-reduce the damage by your PB); Obsidian (the ally makes a second attack when it Attacks).
- Theoretical Origin (14th): transform your carbuncle into the Proto Carbuncle for 1 minute or until 0 HP (on return, it keeps its remaining HP, or its max, whichever is lower). Once; recovered on a long rest.

## Scholar — Subclass: Nymian
Legendary healers who summon the Nymian fey.
- Critical Heal (2nd): when a healing spell's die rolls its maximum, roll another die of the same value and add it (once per healing spell).
- Nymian Healer (6th): when you use a 1st-level-or-higher spell to restore HP, the creature regains additional HP = your PB + the spell's level.
- Adloquium (10th): when you cast a 1st-level-or-higher spell restoring HP, spend one Tactics use to grant temp HP = the HP recovered for 10 minutes (on a critical heal, +half the HP recovered as temp HP).
- Nymian Savior (14th): transform your Nymian fey into the Seraph for 1 minute or until 0 HP (on return, keeps remaining HP or max, whichever is lower). Once; recovered on a long rest.

## Scholar — Subclass: Tactician
Timeless practitioners of the art of war.
- Field Commander (2nd): proficiency in light armor, shields, simple and martial weapons; use your weapon as a casting focus for somatic components; +1 HP per level (including 2nd); memorize additional tactics = your PB.
- Tactical Eye (2nd): when you use the Help action to aid an attack, the target may be within 9 m of you if it can see or hear you.
- Strategic Preparation (6th): spend 1 minute observing a creature to learn whether it is your equal/superior/inferior in two of — STR, DEX, CON, INT, WIS, CHA, AC, current HP, class levels (and possibly a history/personality note at GM discretion).
- Chain Stratagem (10th): when an ally attacks a creature affected by your Help action, they crit on a 19 or 20.
- Always Prepared (14th): as an action, swap one memorized tactic for another. Once; recovered on a long rest.

## Scholar — Tactics List
- **Advantageous:** when rolling initiative, spend one Tactics use to increase an ally's or your own initiative by your PB (once per initiative roll).
- **Aetherial Barrier:** when a creature attacks a target (not you) within 4.5 m of you or your ally, reaction to impose disadvantage on the attack roll.
- **Aetherial Bind** (req. 6th Arcanist): when your ally lands a melee attack, the target makes a Strength save or is restrained and grappled by the ally for 1d4 rounds.
- **Aetherial Catalyst** (req. 2nd Scholar): spend one Tactics use to cast a damaging spell as though you stand where your ally stands.
- **Aetherial Enthrallment** (req. 2nd Arcanist): when you order your ally to act, the target makes a Charisma save vs your spell save DC or has disadvantage on attacks against targets other than your ally for 1 minute (re-save at end of turn).
- **Aetherial Fear** (req. 2nd Arcanist): when you order your ally to act, the target makes a Wisdom save vs your spell save DC or is frightened of you and your ally for 1 minute (re-save at end of each turn).
- **Aetherial Shine** (req. 6th Arcanist): bonus action; creatures within 3 m that can see your ally make a Constitution save or are blinded for 1d4 rounds.
- **Art of War** (req. 10th Tactician): as an action, mark a creature within 9 m; the first attack against it by each attacker has advantage until the start of your next turn.
- **Blessing of Nym** (req. 2nd Nymian): cast an HP-restoring spell through your ally (it is the point of origin; touch spells cast as though from the ally).
- **Bombarding** (req. 2nd Tactician): when you Attack or cast a spell, bonus action to let a friendly creature who can see/hear you use its reaction for one weapon attack.
- **Bulwark Formation** (req. 6th Tactician): as an action, designate a creature; its AC +2 per friendly creature within 1.5 m of it until the start of your next turn.
- **Castle** (req. 10th Scholar): as a bonus action, your ally and a willing creature within 9 m of it swap positions (no opportunity attacks).
- **Deployment Tactics:** as a bonus action, two friendly creatures who can see/hear you may move up to half speed without provoking opportunity attacks.
- **Emergency Tactics** (req. 6th Nymian): when a creature takes damage, reaction to cast an HP-restoring spell on it.
- **Expedience** (req. 10th Nymian): as an action, up to PB creatures within 18 m of you or your ally gain +9 m speed and 2d4 + INT modifier temp HP until the start of your next turn.
- **Excogitation** (req. 2nd Nymian): when you cast a healing spell, delay its effect up to 1 minute (triggers after the target takes a declared amount of damage, or immediately at 0 HP).
- **Logistics Preparation:** as a bonus action, allied creatures within 6 m of you or your ally gain +3 m movement until the start of your next turn.
- **Nymian Preparation** (req. 6th Nymian): when you cast a dice-rolled healing spell, grant temp HP = half the HP that would be healed instead; if any die rolls its max, grant temp HP = the full amount.
- **Plan of Attack:** as a reaction, add your PB to the attack roll of an ally within 3 m.
- **Rally** (req. 6th Tactician): as a bonus action, an ally within 18 m gains 2d4 + INT modifier temp HP and advantage on saves vs fear until the temp HP are gone (+2d4 at 10th, 14th, 18th).
- **Rouse** (req. 2nd Scholar): when you order your ally to act within 9 m, for rounds = INT modifier add your INT modifier to its damage and healing.
- **Spreading Strike** (req. 6th Scholar): when you order your ally to Attack, it makes a second attack on a creature within 1.5 m of the first target.
- **Spur** (req. 2nd Arcanist): when you order your carbuncle to act, it gains advantage on its attack roll and the PB bonus damage is doubled for that attack.
- **Switching Step** (req. 6th Scholar): as a bonus action, swap places with your ally if within 18 m (no opportunity attacks).
- **Tactical Position** (req. 2nd Tactician): use the Help action as a bonus action.

## Scholar — Aetherial Ally Statblocks
- *Carbuncle* — Small Elemental. AC 12 + PB. HP 5 + four times your class level (Hit Dice [d6s] = your Scholar level). Speed 9 m. STR 14(+2) DEX 14(+2) CON 15(+2) INT 8(-1) WIS 14(+2) CHA 11(0). Senses passive Perception 12. Languages understands its summoner's languages but can't speak. PB = yours. Aetheric Bond: add your PB to its checks/saves. Actions — Gouge: melee weapon attack, your spell attack modifier, reach 1.5 m, 7 (1d6 + 2 + PB) bludgeoning. Special Action (by gemstone): Emerald — Emerald Gust (ranged magical attack, range 9 m, 7 (1d6 + 2 + PB) thunder); Ruby — Ruby Ignition (Gouge dealing +2 damage); Topaz — Shining Strike (Gouge dealing 2 less damage, +2 AC until the start of your next turn; no stacking, applies even on a miss).
- *Nymian Fey* — Small Fey. AC 13 + PB. HP 3 + three times your class level (Hit Dice [d4s] = your Scholar level). Speed 9 m. STR 2(-4) DEX 16(+3) CON 10(0) INT 10(0) WIS 12(+1) CHA 16(+3). Senses passive Perception 14. Languages understands its summoner's languages but can't speak. PB = yours. Aetheric Bond: add your PB to its checks/saves. Aetheric Transference: if out of spell slots, it may spend one of yours to cast its spell. Innate Spellcasting (Charisma; shares your spell save DC and attack bonus, no material components): At Will — Blade Ward, Light; 2/day each — Cure Wounds, Healing Word; 1/day — Aid. Actions — Unarmed: melee weapon attack, your spell attack modifier, reach 1.5 m, 1 bludgeoning. Fey Bolt: ranged magical attack, range 9 m, 8 (1d4 + 3 + PB) radiant. Fey Shield: grant a creature within 18 m a temp-HP shield of 1d4 + your spellcasting modifier (lasts until the start of the fey's next turn).
- *Proto Carbuncle* — Large Elemental (Theoretical Origin). AC 15 + PB. HP 50 + four times your class level. Speed 12 m. STR 18(+4) DEX 14(+2) CON 18(+4) INT 8(-1) WIS 14(+2) CHA 11(0). Damage Immunities acid, poison. Condition Immunities poisoned. Senses darkvision 18 m, passive Perception 12. Languages understands its summoner's languages but can't speak. PB = yours. Aetheric Bond: add your PB to its checks/saves. Magic Resistance: advantage on saves vs spells and magical effects. Sure Footed: unaffected by difficult terrain. Actions — Claws: melee weapon attack, your spell attack modifier, reach 1.5 m, 17 (2d6 + 4 + PB) slashing. Bite: melee weapon attack, reach 1.5 m, 17 (1d12 + 4 + PB) piercing. Acidic Spit: ranged weapon attack, range 9 m, 15 (1d8 + 4 + PB) acid. Venomous Mass: a toxic mass at a point within 18 m it can see; creatures in a 6 m radius make a Dexterity save (DC = your spell save DC), taking 3d8 poison + 3d8 acid on a fail (half on success); the area is difficult terrain for 1 minute and a creature starting its turn there takes 2d4 acid. Once per summon.
- *Seraph* — Medium Elemental (Nymian Savior). AC 14 + PB. HP 15 + three times your class level. Speed 9 m (hover). STR 2(-4) DEX 18(+4) CON 14(+2) INT 10(0) WIS 12(+1) CHA 18(+3). Senses passive Perception 14. Languages understands its summoner's languages but can't speak. PB = yours. Aetheric Bond: add your PB to its checks/saves. Aetheric Transference: if out of spell slots, may spend one of yours. Innate Spellcasting (Charisma; shares your spell save DC and attack bonus): At Will — Blade Ward, Light; 4/day each — Cure Wounds, Healing Word; 3/day — Lesser Restoration; 2/day — Mass Healing Word; 1/day — Revivify. Actions — Unarmed: melee weapon attack, your spell attack modifier, reach 1.5 m, 1 bludgeoning. Seraphic Bolt: ranged magical attack, range 9 m, 16 (1d8 + 4 + PB) radiant. Seraphic Shield: grant up to three creatures within 18 m a temp-HP shield of 2d4 + your spellcasting modifier (lasts until the start of the Seraph's next turn).

# SUMMONER
**Hit Die:** d6 | **Saving Throws:** Charisma, Wisdom | **Spellcasting:** Charisma (known)

**Flavor.** A bestial being wreathed in flames leaps into battle, flailing flaming arms to scatter enemy soldiers; at its back, the cloaked caster who shared their essence to give it birth. Coated in body paint to improve magic flow, an ambitious summoner lets the power of godly creatures flow through them, channeling an eikon. With a smug grin, a rocky summoned elemental wears the foe down before the summoner draws its life force to empower a finishing blow. Summoners practice ancient arts that used the powers of primals and eikons against them; the art is re-emerging today.
- A Personal Investment: summoners use their own aether and a powerful force of will to wield beings regarded as gods; without a steady hand and stout heart they put themselves and others at risk.
- Carefully Crafted Summoning: like Scholars, they use grimoires of special formulas, fueling summons with personal aether infused with the influence of legendary deities to give rise to the egi.
- Creating a Summoner: a rich history and a renaissance; learned from ancient tomes, a mentor, or natural affinity; equally heroic or villainous in their goals.

**HP_ref (d6):** 1:6 | 2:10 | 3:14 | 4:18 | 5:22 | 6:26 | 7:30 | 8:34 | 9:38 | 10:42 | 11:46 | 12:50 | 13:54 | 14:58 | 15:62 | 16:66 | 17:70 | 18:74 | 19:78 | 20:82. (Default PF = HP_ref[N] + CON mod x N.)

**Progression — spell slots per level** (verbatim; mid-level columns are intentionally irregular, matching Scholar/Blue Mage)
| Lvl | PB | Cantrips | Spells Known | Features | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | +2 | 4 | 4 | Spellcasting, Eikonic Ally | 2 | — | — | — | — | — | — | — | — |
| 2 | +2 | 4 | 5 | Aetheric Rust, Eikonic Recovery | 3 | — | — | — | — | — | — | — | — |
| 3 | +2 | 4 | 6 | Summoner Calling | 4 | 2 | — | — | — | — | — | — | — |
| 4 | +2 | 5 | 7 | Ability Score Improvement | 4 | 3 | — | — | — | — | — | — | — |
| 5 | +3 | 5 | 8 | — | 4 | 3 | 2 | — | — | — | — | — | — |
| 6 | +3 | 5 | 9 | Calling Feature | 4 | 3 | 3 | — | — | — | — | — | — |
| 7 | +3 | 5 | 10 | — | 4 | 3 | 3 | 1 | — | — | — | — | — |
| 8 | +3 | 5 | 11 | Ability Score Improvement | 4 | 3 | 3 | 2 | — | — | — | — | — |
| 9 | +4 | 5 | 12 | — | 4 | 3 | 3 | 2 | 1 | — | — | — | — |
| 10 | +4 | 6 | 13 | Calling Feature | 4 | 3 | 3 | 2 | 2 | — | — | — | — |
| 11 | +4 | 6 | 14 | — | 4 | 3 | 3 | 2 | 3 | 1 | — | — | — |
| 12 | +4 | 6 | 15 | Ability Score Improvement | 4 | 3 | 3 | 2 | 3 | 1 | — | — | — |
| 13 | +5 | 6 | 16 | — | 4 | 3 | 3 | 2 | 3 | 1 | 1 | — | — |
| 14 | +5 | 6 | 17 | Calling Feature | 4 | 3 | 3 | 2 | 3 | 1 | 1 | — | — |
| 15 | +5 | 6 | 18 | — | 4 | 3 | 3 | 2 | 3 | 1 | 1 | 1 | — |
| 16 | +5 | 6 | 19 | Ability Score Improvement | 4 | 3 | 3 | 2 | 3 | 1 | 1 | 1 | — |
| 17 | +6 | 6 | 20 | — | 4 | 3 | 3 | 2 | 3 | 1 | 1 | 1 | 1 |
| 18 | +6 | 6 | 21 | Enkindle | 4 | 3 | 3 | 3 | 3 | 1 | 1 | 1 | 1 |
| 19 | +6 | 6 | 22 | Ability Score Improvement | 4 | 3 | 3 | 3 | 3 | 2 | 1 | 1 | 1 |
| 20 | +6 | 6 | 23 | Perfected Equation | 4 | 3 | 3 | 3 | 3 | 2 | 2 | 1 | 1 |

**Quick Build.** Charisma highest, then Constitution. Hermit background. Mage Hand, Minor Illusion, Thaumaturgy, Ruin cantrips.

**Proficiencies.** Armor: none. Weapons: daggers, darts, slings, quarterstaffs, light crossbows. Tools: none. Saving Throws: Charisma, Wisdom. Skills: choose two from Arcana, History, Insight, Investigation, Medicine, Religion.
**Equipment.** (a) a quarterstaff or (b) a dagger; (a) a light crossbow and 20 bolts or (a) a simple weapon; (a) a grimoire (your spellcasting focus); (a) a scholar's pack or (b) an explorer's pack.

**Spellcasting.** Charisma. Spell save DC = 8 + PB + CHA mod; attack = PB + CHA mod. Known caster (4 cantrips and four 1st-level spells at 1st; learn more per table; may replace one known spell on level up). Ritual casting if ritual-tagged. Focus: a grimoire or tome.
**Eikonic Ally (1st).** Summon an Egi (statblock below) representing a primal element — choose Earth, Fire, Ice, Lightning, Water, or Wind. It is friendly and obeys you; acts on your turn (moves/reacts on its own but only Dodges unless you bonus-action command it; you may sacrifice an attack to command it to Attack; acts freely if you are incapacitated). At 0 HP it dissipates into a fog (intact 1 minute); use your action + a 1st-level-or-higher slot to revive it after 1 minute at full HP. Summon (and may change element) on a long rest; vanishes if you die.
**Aetheric Rust (2nd).** When you damage a creature with a slot-spending spell, choose one creature hit; until the end of your next turn, when it takes damage it takes extra force damage = your PB. Uses = PB, recovered on a long rest.
**Eikonic Recovery (2nd).** Once per day on a short rest (if your egi is alive), recover expended spell slots of combined level <= half your Summoner level (round up); none 6th level or higher.
**Summoner Calling (subclass, 3rd).** Choose Evoker, Eikonic Channeler, or Allagan. Features at 3rd, 6th, 10th, 14th.
**Ability Score Improvement (4th, 8th, 12th, 16th, 19th).** +2 to one or +1 to two (max 20).
**Enkindle (18th).** As an action, ignite your egi's full potential for an area attack (see Egi statblock; effect by element below). Once; recovered on a long rest.
- Enkindle by element: Earth — STR save, magical bludgeoning + prone; Fire — DEX save, fire + blinded 1 minute (re-save as an action); Ice — CON save, cold + restrained 1 minute (re-save as an action); Lightning — DEX save, lightning + paralyzed until end of its next turn; Water — STR save, cold + knocked back 9 m from the egi; Wind — CON save, thunder + stunned until end of its next turn.
**Perfected Equation (20th).** As an action, summon your egi. Once; recovered on a long rest.

## Summoner — Subclass: Evoker
Empower the egi to the peak of its strength.
- Empowered Egi (3rd): when you summon your egi, choose — Rageful (its attacks deal bonus damage = your CHA modifier); Swift (its attacks are unaffected by opportunity attacks until end of your turn); Tough (+1 AC and +2 HP per Summoner level).
- Primal Summoning (6th): summon the Primal Egi (Medium elemental) which can cast spells (your spell attack bonus and save DC; two 1st-level slots and one 2nd-level slot, recovered on a long rest; may use your slots if out). Order it to cast as your action. Spells by element: Earth — Earth Tremor, Maximilian's Earthen Grasp; Fire — Burning Hands, Scorching Ray; Ice — Frost Fingers, Snilloc's Snowball Storm; Lightning — Witch Bolt, Hold Person; Water — Ice Knife, Melf's Acid Arrow; Wind — Thunderwave, Dust Devil.
- Eikonic Rage (10th): the egi makes two attacks when commanded to Attack.
- Eikonic Summoning (14th): summon the Eikonic Egi (up to Large elemental), gaining a 9 m flying speed and improved casting (four 1st-level, two 2nd-level, one 3rd-level slot). Added spells by element: Earth — Erupting Earth; Fire — Fireball; Ice — Sleet Storm; Lightning — Lightning Bolt; Water — Tidal Wave; Wind — Thunder Step.

## Summoner — Subclass: Eikonic Channeler
Wield primal power through your own body rather than on the field.
- Eikonic Trance (3rd): on a long rest, attune to an elemental primal (need not match your egi). Each grants a cantrip + resistance, and lets you change a slot-spell's damage to that type: Earth — Magic Stone, resist bludgeoning (change to magical bludgeoning); Fire — Fire Bolt, resist fire (change to fire); Ice — Ray of Frost, resist cold (change to cold); Lightning — Shocking Grasp, resist lightning (change to lightning); Water — Acid Splash (deals cold via this feature), resist cold, swim speed = movement and hold breath 1 hour; Wind — Thunderclap, resist thunder (change to thunder). As a bonus action, unleash the primal: add your CHA modifier to your spells' damage rolls (and the primal cantrip's) for 1 minute. Uses = PB, recovered on a long rest.
- Dual Elementalist (6th): on a long rest, attune to a second elemental primal.
- Eikonic Icon (6th): per attuned element — Earth (1.5 m tremorsense); Fire (bonus action: 3 m bright + 6 m dim light, toggle off); Ice (unaffected by difficult terrain); Lightning (advantage on Perception checks); Water (swim speed = movement, breathe underwater); Wind (bonus action: hover 1.5 m above ground, end at will).
- Eikonic Master (10th): as a bonus action, change one attuned elemental primal. Uses = CHA modifier, recovered on a long rest.
- Ascended Trance (14th): when you unleash your trance, pick — Dreaded Ascendance (flying speed = movement; while unleashed, when you cast a spell you may make a ranged spell attack for 3d8 + CHA modifier force); Inspiring Ascendance (flying speed = movement; a friendly creature starting its turn within 9 m recovers 1d8 + CHA modifier HP; when you cast a spell you may make a ranged spell attack for 1d8 + CHA modifier fire).

## Summoner — Subclass: Allagan
Use the egi pragmatically as a tool of war.
- Energy Drain (3rd): as an action, ranged spell attack vs a creature within 9 m of you or your egi; on hit, #d4 necrotic (# = PB), and you or your egi (whichever is the source) recover HP = damage dealt; the creature makes a CHA save vs your spell save DC or has disadvantage on attack rolls and skill checks until the start of your next turn. Uses = PB, recovered on a short or long rest.
- Allagan Infusion (6th): when you cast a spell, deal damage up to your PB to your egi; add half that damage (round up) to your spell attack bonus and save DC for that spell.
- Eikonic Ward (10th): when you take damage, reaction to split half (round up) between you and your egi.
- Eikonic Explosion (14th): as an action, order your egi to explode (reduced to 0 HP, gone until resummoned); chosen creatures in a 9 m radius make a DEX save vs your spell save DC, taking #d10 (# = PB) of the egi's damage type on a fail (half on success). A creature that fails also has disadvantage on attack rolls and skill checks and -3 m speed for 1 minute (CHA save at end of its turn: first success ends the speed penalty, second success ends the effect).

## Summoner — Egi Statblock
- *Elemental Egi* — Small Elemental. AC 12 + PB. HP 5 + five times your Summoner level (Hit Dice [d8s] = your Summoner level). Speed 9 m (hover). STR 10(+0) DEX 14(+2) CON 14(+2) INT 10(+0) WIS 12(+1) CHA 16(+3). Senses passive Perception 10. Languages understands its summoner's languages but can't speak. PB = yours. Actions — Egi Strike: melee magic attack, your spell attack modifier, reach 1.5 m, 12 (1d8 + 3 + PB) elemental damage. Egi Blast: ranged magic attack, range 18 m, 12 (1d6 + 3 + PB) elemental damage. Eikonic Enkindle (via the Enkindle feature): creatures within a 9 m radius make the relevant save or take 8d10 elemental damage + a negative effect (half, no effect on success); damage type, effect, and save by element per the Enkindle feature.
- Egi Element Effect: Earth — damage becomes bludgeoning, +2 AC, bonus HP becomes 8x Summoner level; Fire — damage becomes fire, Egi Strike die becomes d10, immune to fire; Ice — damage becomes cold, speed +3 m, immune to cold; Lightning — damage becomes lightning, Egi Blast die becomes d8, immune to lightning; Water — damage becomes bludgeoning or cold, immune to cold, swim speed 18 m; Wind — damage becomes thunder, immune to thunder, flying speed 12 m. (Source OCR garbled the Wind row with an author's note: the note simply encourages players to base their egi on favourite entities/creatures rather than specific primals like Ifrit or Titan, using the neutrally named actions; established primals are also welcome.)

# VIPER
**Hit Die:** d8 | **Saving Throws:** Strength, Dexterity | **Resource:** Flow charges (DEX-based)

**Flavor.** A great flaming beast crunches a poisoned carcass and is lulled into stupor as the viper closes in and finishes it with a few swift strikes. Glistening twin blades attack in an endless flurry, finding every gap until the foe falls. With incense and a meditative state, the viper feels a surge of power summoning flames and ice. Vipers are expert monster slayers who emulate the snake's skill and swiftness, with deadly fangs and lightning speed.
- To Fell The Indomitable: in Tural, beasts sometimes mutate into mystic, monstrous Tural Vidraal; hunters honed the viper's arts — poisons, swordsmanship, cunning — to stop them.
- The Steel Fangs: vipers wield twin swords (the fangs) that combine into a double-bladed Viper Staff, whirled to extend range, misdirect, and find the perfect angle.
- Creating a Viper: consider why you became a monster hunter (retribution, glory, mastery) and how you learned the arts (secluded village or one-on-one with an experienced viper).

**HP_ref (d8):** 1:8 | 2:13 | 3:18 | 4:23 | 5:28 | 6:33 | 7:38 | 8:43 | 9:48 | 10:53 | 11:58 | 12:63 | 13:68 | 14:73 | 15:78 | 16:83 | 17:88 | 18:93 | 19:98 | 20:103. (Default PF = HP_ref[N] + CON mod x N.)

**Progression**
| Lvl | PB | Features |
|---|---|---|
| 1 | +2 | Viper Style, Focus of Caduceus |
| 2 | +2 | Flow of the Viper, Viper Stance |
| 3 | +2 | Serpentine Inspiration |
| 4 | +2 | Ability Score Improvement |
| 5 | +3 | Extra Attack |
| 6 | +3 | Inspiration Feature |
| 7 | +3 | Swiftscaled |
| 8 | +3 | Ability Score Improvement |
| 9 | +4 | Serpentine Aspect, Evasion |
| 10 | +4 | Inspiration Feature |
| 11 | +4 | Ambidextrous Fighter |
| 12 | +4 | Ability Score Improvement |
| 13 | +5 | Serpent's Ire |
| 14 | +5 | Inspiration Feature |
| 15 | +5 | Stalwart Hunter |
| 16 | +5 | Ability Score Improvement |
| 17 | +6 | Swiftscaled (x2), Rattling Coil |
| 18 | +6 | Reawaken |
| 19 | +6 | Ability Score Improvement |
| 20 | +6 | Serpent's Legacy |

**Quick Build.** Dexterity highest, then Wisdom. Outlander background.

**Proficiencies.** Armor: light. Weapons: simple weapons, martial weapons. Tools: none. Saving Throws: Strength, Dexterity. Skills: choose two from Acrobatics, Animal Handling, Athletics, Insight, Nature, Stealth, Survival.
**Equipment.** (a) two shortswords; (a) a short bow and 20 arrows; (a) leather armor; (a) a dungeoneer's pack or (b) an explorer's pack.

**Viper Style (1st).** In two-weapon fighting, add your ability modifier to the second attack's damage; draw/stow two one-handed light weapons when you could normally draw/stow one. Movement speed +1.5 m, and when you Disengage you ignore difficult terrain. At 9th level, speed +1.5 m more and you can move along vertical surfaces on your turn without falling during the move.
**Focus of Caduceus (1st).** Bonus action to regain HP = 1d8 + Viper level. Uses = PB, refreshed on a long rest.
**Flow of the Viper (2nd).** When you make a melee weapon attack you gain one Flow charge; spend charges to replace attacks with Viper Strikes (a Viper Strike doesn't grant a charge; no limit on replacements per turn). Max Flow = PB. Viper Strike save DC = 8 + PB + DEX modifier. (Strikes list at the end.)
**Viper Stance (2nd).** Combine two one-handed light finesse weapons into a Viper Staff (two-handed, light, finesse; you choose the damage type and apply that weapon's effects; attacks deal bonus damage = your PB). While wielding it, bonus action to misdirect (advantage on your next weapon attack until end of turn). Bonus action to enter/exit Viper Stance (some strikes also switch it).
**Serpentine Inspiration (subclass, 3rd).** Choose Vidraal Bane, Bloody Maw, or Serpent Shaman. Features at 3rd, 6th, 10th, 14th.
**Ability Score Improvement (4th, 8th, 12th, 16th, 19th).** +2 to one or +1 to two (max 20). (Source also lists 14th; standard ASI levels assumed.)
**Extra Attack (5th).** Attack twice when you take the Attack action.
**Swiftscaled (7th).** On your turn, take one additional action. Short or long rest to reuse; at 17th, twice per rest but once per turn.
**Serpentine Aspect (9th).** Proficiency in Sleight of Hand and Stealth (expertise if already proficient).
**Evasion (9th).** On a DEX save for half damage, take none on success and half on failure.
**Ambidextrous Fighter (11th).** Gain a second bonus action, usable only to make an off-hand melee weapon attack or to gain advantage while wielding the Viper Staff.
**Serpent's Ire (13th).** When you use a Viper Strike costing more than 1 Flow charge, recover half the spent charges (round down).
**Stalwart Hunter (15th).** Proficiency in Wisdom saving throws.
**Rattling Coil (17th).** When you roll initiative, gain 2 Flow charges and you can't be surprised.
**Reawaken (18th).** As an action, cast Haste on yourself with advantage on Constitution saves for the duration. Once; recovered on a long rest.
**Serpent's Legacy (20th).** When you use Reawaken, cast Haste as a bonus action instead, and your concentration on it can't be broken.

## Viper — Subclass: Vidraal Bane
Poisons and cunning to slay foes far larger than yourself.
- Noxious Gash (3rd): on a short/long rest, make toxin vials = PB (old batch becomes impotent). Bonus action to apply one vial to a weapon or three pieces of ammunition (active 1 minute or until it lands). Noxious Gash save DC = 8 + PB + WIS modifier; a struck creature makes a CON save vs it (re-save at end of its turn). Toxins: Gorgon's Kiss (speed halved 1 minute, no opportunity attacks); Viper's Fang (poisoned 1 minute, 2d8 poison); Shaaloani Sunset (asleep 1 minute or until damaged/shaken); Twilight in Tural (blinded 1 minute).
- Master Tracker (6th): proficiency in Survival (expertise if already proficient); advantage on Survival checks to track or find signs of a known creature in the area.
- Toxic Shock (10th): when a creature resists one of your toxins, its next save vs your toxins takes a -1 penalty, increasing by 1 each resist until a toxin lands (max = WIS modifier). Also, a toxin-laced weapon deals bonus poison damage = WIS modifier for 1 minute (continues even after landing the toxin, until a new toxin is applied).
- Serpent's Kiss (14th): your melee attacks against a creature affected by your Noxious Gash crit on 19 or 20.

## Viper — Subclass: Bloody Maw
Ceaseless attacks and slippery defense.
- Tenacious Onslaught (3rd): when you hit a creature below its HP max with a weapon attack, +1d8 damage (once per turn).
- Masterful Movement (6th): bonus action to gain advantage on Athletics/Acrobatics checks and add your WIS modifier to the result.
- Sidewinding Strike (10th): once per turn when you miss with a weapon attack, make another weapon attack as part of the same action (no Flow charge).
- Deadly Precision (14th): your weapon attack rolls gain a bonus = your current Flow charges.

## Viper — Subclass: Serpent Shaman
Nature magic fuels the hunt.
- Spellcasting (3rd): WIS-based half-caster from the druid list. Spell save DC = 8 + PB + WIS modifier; attack = PB + WIS modifier. Two druid cantrips (a third at 10th); prepare WIS modifier + half Viper level (round down, min 1). Slots per the table below.
- Blessing of the Serpent (3rd): a 1-hour ritual (during a short rest) bonds a weapon to you (can't be disarmed unless incapacitated; summon it as a bonus action if on the same plane). Up to two bonded weapons (summon one at a time); bonding a third breaks one bond.
- Serpentine Weaving (6th): when you cast a cantrip with your action, make one weapon attack as a bonus action.
- Slithering Strike (10th): as an attack, throw a bonded weapon at a target/point within 6 m (or up to 12 m with disadvantage) for a ranged weapon attack; then bonus action to teleport to the weapon's location. Once; recovered on a short or long rest.
- Nature's Sting (14th): your weapon attacks deal bonus damage = your WIS modifier.

**Serpent Shaman Spellcasting — spell slots per level**
| Lvl | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| 3 | 2 | — | — | — |
| 4 | 3 | — | — | — |
| 5 | 3 | — | — | — |
| 6 | 3 | — | — | — |
| 7 | 4 | 2 | — | — |
| 8 | 4 | 2 | — | — |
| 9 | 4 | 2 | — | — |
| 10 | 4 | 3 | — | — |
| 11 | 4 | 3 | — | — |
| 12 | 4 | 3 | — | — |
| 13 | 4 | 3 | 2 | — |
| 14 | 4 | 3 | 2 | — |
| 15 | 4 | 3 | 2 | — |
| 16 | 4 | 3 | 3 | — |
| 17 | 4 | 3 | 3 | — |
| 18 | 4 | 3 | 3 | — |
| 19 | 4 | 3 | 3 | 1 |
| 20 | 4 | 3 | 3 | 1 |

## Viper — Viper Strikes List
(Replace attacks from the Attack action unless noted; costs are Flow charges.)
- **Hunter's Bite** (2nd; 1): on a melee hit, +1d8 damage.
- **Swiftskin's Coil** (2nd; 1): a melee weapon attack plus the Disengage action.
- **Hunter's Sting** (3rd; 1): enter Viper Stance and make a weapon attack with +1.5 m range.
- **Steel Fangs** (3rd; 2): a jumping piercing attack vs a creature within 3 m; move to within 1.5 m of it (no opportunity attacks); on a hit, bonus damage = your PB. Ends Viper Stance if you were in it.
- **Steel Maw** (3rd; 2): enter Viper Stance, then each creature within 1.5 m makes a DEX save or takes your weapon damage.
- **Piercing Fangs** (5th; 1): on a melee hit, +1d8 damage; you lose Viper Stance.
- **Hunter's Strike** (5th; 1): on a melee hit, +1d8 damage; you gain Viper Stance.
- **Slither** (5th; 3): bonus action; teleport up to 9 m to an unoccupied space you can see.
- **Reaving Fangs** (7th; 1): the creature makes a CON save vs your Viper Strike DC or is poisoned 1 minute.
- **Vicepit** (7th; 2): on a hit, the creature makes a STR save vs your Viper Strike DC or is knocked prone.
- **Backlash** (10th; 1): when a melee attack misses you, reaction to make a melee weapon attack against the attacker.
- **Snake Scales** (10th; 2): when you use Focus of Caduceus, spend 2 Flow to gain resistance to slashing, piercing, and bludgeoning until the start of your next turn.
- **Uncoiled Fury** (10th; 4): a spinning strike with a 3 m radius; each creature makes a DEX save, taking your weapon damage + 1d8 on a fail (half on success).
- **Barbarous Bite** (15th; 3): on a hit, the creature makes a CON save or its AC is reduced by 2 and it deals 1d4 less damage on its weapon attacks until the end of its next turn.
- **Ouroboros** (18th; 5): the creature makes a DEX save; on a fail, you hit it with a melee weapon attack dealing critical damage (half damage on a success).
- **World-Swallower** (20th; 6): bonus action; if your next attack roll against a creature has a die result of 11 or higher, it is a critical hit; if it misses, regain 2 Flow charges.

# WARRIOR
**Hit Die:** d12 | **Saving Throws:** Strength, Constitution | **Resource:** Berserk / Brutality Die

**Flavor.** A wayward blade flies toward a chirurgeon healing a fallen ally — only for a great axe to block it at the last second. Fueled by unbridled fury, a man screams as he slams a greatsword through a beast, sundering its armour like butter. A brutish man raises his fists in a tavern, striking with the force of a dragon's tail. History is littered with those who let rage carry them beyond all limits.
- The Inner Beast: a concept across Eorzea — blessing or curse; the warrior tribes of Abalathia train to tame their inner beast and wield it as a weapon.
- Rage and Steel: warriors wield massive weapons like great axes, swung effortlessly by the inner beast — walking tempests, steel cyclones commanding the battlefield.
- Creating a Warrior: consider how you connected with your inner beast and whether you master it to protect, or feed it and wreak havoc; reckless use will consume you.

**HP_ref (d12):** 1:12 | 2:19 | 3:26 | 4:33 | 5:40 | 6:47 | 7:54 | 8:61 | 9:68 | 10:75 | 11:82 | 12:89 | 13:96 | 14:103 | 15:110 | 16:117 | 17:124 | 18:131 | 19:138 | 20:145. (Default PF = HP_ref[N] + CON mod x N.)

**Progression**
| Lvl | PB | Brutality Die | Berserks | Features |
|---|---|---|---|---|
| 1 | +2 | d4 | 2 | Berserk, Unarmoured Defense |
| 2 | +2 | d4 | 2 | Fighting Style, Reckless Attack |
| 3 | +2 | d4 | 3 | Bestial Archetype |
| 4 | +2 | d4 | 3 | Ability Score Improvement |
| 5 | +3 | d4 | 3 | Extra Attack |
| 6 | +3 | d4 | 4 | Archetype Feature |
| 7 | +3 | d4 | 4 | Onslaught, Tongue of Beasts |
| 8 | +3 | d6 | 4 | Ability Score Improvement |
| 9 | +4 | d6 | 4 | Raw Intuition |
| 10 | +4 | d6 | 4 | Archetype Feature |
| 11 | +4 | d6 | 4 | Overpower |
| 12 | +4 | d6 | 5 | Ability Score Improvement |
| 13 | +5 | d6 | 5 | Vengeance |
| 14 | +5 | d6 | 5 | Archetype Feature |
| 15 | +5 | d6 | 5 | Shake it Off |
| 16 | +5 | d8 | 5 | Ability Score Improvement |
| 17 | +6 | d8 | 6 | Beastly Reflexes |
| 18 | +6 | d8 | 6 | Holmgang |
| 19 | +6 | d8 | 6 | Ability Score Improvement |
| 20 | +6 | d10 | 6 | Infuriate |

**Quick Build.** Strength highest, then Constitution. Outlander background.

**Proficiencies.** Armor: Light, Medium, Shields. Weapons: simple weapons, martial weapons. Tools: none. Saving Throws: Strength, Constitution. Skills: choose two from Animal Handling, Athletics, Intimidation, Insight, Survival.
**Equipment.** (a) a martial or simple weapon; (a) a martial or simple weapon; (a) two handaxes or (b) a light crossbow and 20 bolts; (a) a dungeoneer's pack or (b) an explorer's pack; (a) scale mail or (b) leather armour; a carved wooden idol related to your heritage.

**Berserk (1st).** Bonus action to enter a berserk trance (if not in heavy armor): advantage on Strength checks and saves; melee Strength attacks deal bonus damage = your Brutality Die (per table); resistance to bludgeoning, piercing, slashing; can't cast or concentrate on spells. Berserk DC = 8 + PB + STR modifier. Lasts 1 minute (ends early if knocked unconscious, if your turn ends and you haven't attacked a hostile creature or taken damage since your last turn, or as a bonus action). Uses = Berserks column, refreshed on a long rest.
**Unarmored Defense (1st).** While wearing no armor, AC = 10 + DEX modifier + CON modifier. Shield allowed.
**Reckless Attack (2nd).** On your first attack on your turn, attack recklessly for advantage on melee Strength attacks this turn, but attacks against you have advantage until your next turn.
**Fighting Style (2nd).** Choose Defense / Dueling / Great Weapon Fighting / Two-Weapon Fighting (standard wording).
**Bestial Archetype (subclass, 3rd).** Choose Beast of Defiance, Beast of Deliverance, or Unchained Beast. Features at 3rd, 6th, 10th, 14th.
**Ability Score Improvement (4th, 8th, 12th, 16th, 19th).** +2 to one or +1 to two (max 20). (Optional: take a feat instead.)
**Extra Attack (5th).** Attack twice when you take the Attack action.
**Onslaught (7th).** When you use the Dash action, bonus action to make a melee weapon attack dealing bonus damage = your CON modifier.
**Tongue of Beasts (7th).** Cast Speak with Animals. Once; refreshed on a long rest.
**Raw Intuition (9th).** When you take damage, reaction to move 1.5 m directly away (no opportunity attacks) and reduce the damage by your Brutality Die + PB. Once (twice at 13th, three times at 18th); refreshed on a long rest.
**Overpower (11th).** As an action, slam the ground: each creature within a 3 m radius makes a STR save vs your Berserk DC, taking thunder damage = Brutality Die + STR modifier + CON modifier and knocked prone on a fail (half, not prone on success).
**Vengeance (13th).** When you take damage from a creature within 1.5 m, reaction to make a melee weapon attack against it.
**Shake It Off (15th).** While berserking, when you make a save vs a status condition (excluding Exhaustion, Incapacitated, Prone, Restrained, Unconscious), you may end Berserk to auto-succeed (after the roll, before the outcome is declared).
**Beastly Reflexes (17th).** While berserking, you have two reactions per round.
**Holmgang (18th).** Bonus action or reaction (when a creature damages you): until the end of your third turn after, you can't fall below 1 HP. If used as a bonus action, a 4.5 m radius ring of fire forms between you and a target creature within 9 m; the creature makes a WIS save vs your Berserk DC to cross (4d8 fire and stops on a fail; half and passes on a success). You auto-pass, taking half damage when you cross. Once; refreshed on a long rest.
**Infuriate (20th).** If you have no Berserk uses left when you roll initiative, recover 2 uses.

## Warrior — Subclass: Beast of Defiance
Tame the beast to protect allies.
- Imposition (3rd): while berserking, when a creature attacks a target (not you) within 1.5 m of you, reaction to impose disadvantage.
- Storm's Path (6th): while berserking, on a weapon hit you may declare this feature; the creature makes a CON save vs your Berserk DC or, for rounds = PB, its damage is reduced by your Brutality Die. Once per Berserk trance.
- Bestial Empathy (10th): cast Beast Sense once; refreshed on a long rest.
- Nascent Flash (14th): while berserking, bonus action to share your inner beast with a creature within 9 m — it gains temp HP = your Brutality Die; until the end of your next turn, each weapon hit you land heals both of you for your Brutality Die + PB. Your Berserk ends after using this.

## Warrior — Subclass: Beast of Deliverance
A precise destructive force.
- Inner Release (3rd): while berserking, melee weapon attacks crit on 19-20 (18-20 at 14th).
- Storm's Eye (6th): while berserking, on a weapon hit you may declare this feature; the creature makes a CON save vs your Berserk DC or, for rounds = PB, takes additional damage = your Brutality Die when hit by a melee weapon attack. Once per Berserk trance.
- Bellow of the Beast (10th): on an Intimidation check, expend one Berserk use to gain advantage and add your STR modifier.
- Fell Cleave (14th): bonus action; your next landed melee attack is a critical hit and deals bonus damage = your CON modifier (if the roll would already crit, roll the extra crit dice a second time). Lost if you leave Berserk before landing it; your Berserk ends after the attack lands and can't be reused until the start of your next turn.

## Warrior — Subclass: Unchained Beast
Let the beast run free with fist and steel.
- Bestial Brawling (3rd): unarmed strikes may use your Brutality Die for damage.
- Raging Follow Through (3rd): when you make a weapon attack with a two-handed weapon or an unarmed strike, bonus action to make an unarmed strike.
- Orogeny (6th): as an action, make an unarmed strike against each creature within 1.5 m, up to PB creatures. Once per Berserk trance.
- Bestial Avatar (10th): proficiency in one of Acrobatics, Athletics, Stealth, Survival (double PB if already proficient).
- Primal Scream (14th): each creature in a 9 m cone makes a CON save vs your Berserk DC, taking 6d6 thunder and -2 AC for rounds = half PB (round up) on a fail (half, no AC loss on success). Your Berserk ends after using this.

# WHITE MAGE
**Hit Die:** d6 | **Saving Throws:** Wisdom, Charisma | **Spellcasting:** Wisdom (prepared) | **Resource:** Confession charges

**Flavor.** A well-groomed man waves his cane, drawing magic from the land; the earth parts and erupts, toppling his foe. A gentle woman rushes to an ally's side, sharing the land's power through prayer to close mortal wounds. A stern robed figure calls down shining light to banish the undead. White Mages commune with the world, borrowing power from elementals; level-headed and respectful, they keep order in magic while mending wounds.
- One with the Land: their strength stems from conjury — calling earth, wind, and water and concentrating them through meditation, focused via an unworked-wood wand or cane; they are also accomplished healers.
- Patrons of Light: rooted in a society that revered nature; past overuse caused elementals to smite the land, contributing to a dark age; today White Mages are few, practicing the forbidden art to drive off evil.
- Creating a White Mage: consider how you came to conjury (a mentor, study of the past, or whispers of the elementals).

**HP_ref (d6):** 1:6 | 2:10 | 3:14 | 4:18 | 5:22 | 6:26 | 7:30 | 8:34 | 9:38 | 10:42 | 11:46 | 12:50 | 13:54 | 14:58 | 15:62 | 16:66 | 17:70 | 18:74 | 19:78 | 20:82. (Default PF = HP_ref[N] + CON mod x N.)

**Progression — spell slots per level**
| Lvl | PB | Cantrips | Features | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | +2 | 3 | Spellcasting, Confession, Reach of the Unseen | 2 | — | — | — | — | — | — | — | — |
| 2 | +2 | 3 | Conjury Discipline, Afflatus Solace | 3 | — | — | — | — | — | — | — | — |
| 3 | +2 | 3 | — | 4 | 2 | — | — | — | — | — | — | — |
| 4 | +2 | 4 | Ability Score Improvement | 4 | 3 | — | — | — | — | — | — | — |
| 5 | +3 | 4 | — | 4 | 3 | 2 | — | — | — | — | — | — |
| 6 | +3 | 4 | Discipline Feature | 4 | 3 | 3 | — | — | — | — | — | — |
| 7 | +3 | 4 | — | 4 | 3 | 3 | 1 | — | — | — | — | — |
| 8 | +3 | 5 | Ability Score Improvement | 4 | 3 | 3 | 2 | — | — | — | — | — |
| 9 | +4 | 5 | — | 4 | 3 | 3 | 3 | 1 | — | — | — | — |
| 10 | +4 | 5 | Discipline Feature | 4 | 3 | 3 | 3 | 2 | — | — | — | — |
| 11 | +4 | 5 | — | 4 | 3 | 3 | 3 | 2 | 1 | — | — | — |
| 12 | +4 | 5 | Ability Score Improvement | 4 | 3 | 3 | 3 | 2 | 1 | — | — | — |
| 13 | +5 | 5 | — | 4 | 3 | 3 | 3 | 2 | 1 | 1 | — | — |
| 14 | +5 | 5 | Discipline Feature | 4 | 3 | 3 | 3 | 2 | 1 | 1 | — | — |
| 15 | +5 | 5 | — | 4 | 3 | 3 | 3 | 2 | 1 | 1 | 1 | — |
| 16 | +5 | 5 | Ability Score Improvement | 4 | 3 | 3 | 3 | 2 | 1 | 1 | 1 | — |
| 17 | +6 | 5 | — | 4 | 3 | 3 | 3 | 2 | 1 | 1 | 1 | 1 |
| 18 | +6 | 5 | Conservation of Life | 4 | 3 | 3 | 3 | 3 | 1 | 1 | 1 | 1 |
| 19 | +6 | 5 | Ability Score Improvement | 4 | 3 | 3 | 3 | 3 | 2 | 1 | 1 | 1 |
| 20 | +6 | 5 | Graceful Healer | 4 | 3 | 3 | 3 | 3 | 2 | 2 | 1 | 1 |

**Quick Build.** Wisdom highest, then Charisma. Healer (Spirit Master) discipline. Acolyte background. Guidance, Light, Sacred Flame, Spare the Dying cantrips; 1st-level Cure Wounds and Heroism.

**Proficiencies.** Armor: none. Weapons: daggers, darts, slings, quarterstaffs, light crossbows. Tools: none. Saving Throws: Wisdom, Charisma. Skills: choose two from Arcana, Deception, Insight, Persuasion, History, Religion, Medicine.
**Equipment.** (a) a dagger or (b) a quarterstaff; (a) a light crossbow and 20 bolts or (a) a simple weapon; a spellcasting focus (cane, staff, wand, or similar); (a) an explorer's pack or (b) a scholar's pack.

**Spellcasting.** Wisdom. Spell save DC = 8 + PB + WIS mod; attack = PB + WIS mod. Prepare WIS modifier + White Mage level spells (min 1) from the White Mage list; change on a long rest. Ritual casting if ritual-tagged. Focus: a rod, cane, or wand.
**Confession (1st).** Borrow elemental power as Confession charges. Max = PB + WIS modifier. On initiative, gain charges = PB. As a bonus action in combat, pray to gain charges = PB. After a battle, charges remain for 1 minute.
**Reach of the Unseen (1st).** When you cast a spell, spend 1 Confession charge to make a touch spell a ranged spell up to 9 m.
**Conjury Discipline (subclass, 2nd).** Choose Elementalist, Spirit Master, or Ampdapori. Features at 2nd, 6th, 10th, 14th.
**Afflatus Solace (2nd).** Bonus action; spend up to PB Confession charges to heal a creature within 9 m for #d4 + PB HP (# = charges spent; target must be above 0 HP).
**Ability Score Improvement (4th, 8th, 12th, 16th, 19th).** +2 to one or +1 to two (max 20).
**Conservation of Life (18th).** When reduced to 0 HP and unconscious, release a pulse: all allies within a 9 m radius (not you) heal 2d8 + WIS modifier HP. Once; long rest to reuse.
**Graceful Healer (20th).** When you roll initiative, gain your maximum Confession charges.

## White Mage — Subclass: Elementalist
Manipulate earth, wind, and water alongside the elementals.
- Expanded Spell List: 1st — Earth Tremor, Thunderwave; 2nd — Earthbind, Maximilian's Earthen Grasp; 3rd — Erupting Earth, Melf's Minute Meteors; 4th — Stoneskin, Watery Sphere; 5th — Conjure Elemental, Control Winds.
- Elemental Blessing (2nd): as an action, spend up to 3 Confession charges to bless a weapon within 9 m for rounds = WIS modifier — 1 charge: change damage type to cold, radiant, or thunder; 2: also +1 to attack rolls; 3: also bonus damage = your PB.
- Eyes of the Elementals (6th): meditate 15 minutes to gain a mental map within a ~3.2 km radius (once; refreshed on a long rest). Also gain darkvision (magical and nonmagical) to 36 m.
- Elemental Armour (10th): as an action, spend 1 Confession charge to grant a touched creature resistance to cold, radiant, or thunder for rounds = WIS modifier.
- Aetherial Conjuration (14th): as a bonus action, spend up to PB Confession charges to cast a spell whose level = half the charges spent (round up).

## White Mage — Subclass: Spirit Master
Master healers and supporters.
- Expanded Spell List: 1st — Heroism, Sanctuary; 2nd — Enhance Ability, Protection from Poison; 3rd — Aura of Vitality, Beacon of Hope; 4th — Regenerate (Regen), Tetragrammaton; 5th — Assize, Asylum.
- Soothe Sayer (2nd): when you cast a 1st-level-or-higher spell restoring HP, the creature regains additional HP = your PB + the spell's level.
- Medicine Master (6th): proficiency in Medicine; advantage on WIS (Medicine) checks to stabilize creatures and diagnose diseases.
- Clerical Smite (10th): when you cast a dice-rolled healing spell, spend a Confession charge to deal its healing as radiant damage instead (Soothe Sayer bonus applies as bonus damage); the target makes a WIS save vs your spell save DC for half.
- Touch of the Padjal (14th): as a bonus action, spend a Confession charge; your next HP-restoring spell uses the maximum value on each healing die.

## White Mage — Subclass: Ampdapori
Repel the undead and fiends with holy light.
- Expanded Spell List: 1st — Magic Missile, Sleep; 2nd — Moonbeam, Silence; 3rd — Daylight, Spirit Guardians; 4th — Banishment, Wall of Fire; 5th — Dawn, Hallow.
- Afflatus Misery (2nd): as an action, spend up to PB Confession charges to make a ranged spell attack within 18 m for #d6 + PB radiant damage (# = charges spent).
- Inquisitor's Report (6th): meditate 15 minutes to learn the location of undead or fiends within a ~1.6 km radius. Once; refreshed on a long rest.
- Aura of Ampdapor (10th): while you hold a Confession charge, emit a 3 m aura — you and friendly creatures in it have resistance to necrotic damage, and HP-restoring spells on them recover additional HP = your WIS modifier.
- Void Bane (14th): as a bonus action, spend 1 Confession charge to empower your next spell; if the target is undead or a fiend, you gain advantage on the spell attack (or it has disadvantage on the save) and the spell deals bonus damage on hit = your PB.

END OF FILE — 02_Classes (COMPLETE — all 22 Jobs: Astrologian, Bard, Black Mage, Blue Mage, Dancer, Dark Knight, Dragoon, Gunbreaker, Machinist, Ninja, Monk, Paladin, Pictomancer, Reaper, Red Mage, Sage, Samurai, Scholar, Summoner, Viper, Warrior, White Mage)
