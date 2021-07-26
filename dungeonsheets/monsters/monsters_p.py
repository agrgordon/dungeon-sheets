"""
A collection of monsters from D&D 5e's SRD

This file was autogenerated by https://github.com/stravajiaxen/5e-srd-to-py
"""

from dungeonsheets.monsters.monsters import Monster
from dungeonsheets.stats import Ability


class Panther(Monster):
    """
    Keen Smell.
      The panther has advantage on Wisdom (Perception) checks that rely on
      smell.
    Pounce.
      If the panther moves at least 20 ft. straight toward a creature and
      then hits it with a claw attack on the same turn, that target must
      succeed on a DC 12 Strength saving throw or be knocked prone. If the
      target is prone, the panther can make one bite attack against it as a
      bonus action.
    Bite.
      Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 +
      2) piercing damage.
    Claw.
      Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 +
      2) slashing damage.
    """
    name = "Panther"
    description = "Medium beast, unaligned"
    challenge_rating = 0.25
    armor_class = 12
    skills = "Perception +4, Stealth +6"
    senses = "Passive Perception 14"
    languages = ""
    strength = Ability(14)
    dexterity = Ability(15)
    constitution = Ability(10)
    intelligence = Ability(3)
    wisdom = Ability(14)
    charisma = Ability(7)
    speed = 50
    swim_speed = 0
    fly_speed = 0
    climb_speed = 40
    hp_max = 13
    hit_dice = "3d8"
    spells = []


class Pegasus(Monster):
    """
    Hooves.
      Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 11 (2d6
      + 4) bludgeoning damage.
    """
    name = "Pegasus"
    description = "Large celestial, chaotic good"
    challenge_rating = 2
    armor_class = 12
    skills = "Perception +6"
    senses = "Passive Perception 16"
    languages = "understands Celestial, Common, Elvish, and Sylvan but can't speak"
    strength = Ability(18)
    dexterity = Ability(15)
    constitution = Ability(16)
    intelligence = Ability(10)
    wisdom = Ability(15)
    charisma = Ability(13)
    speed = 60
    swim_speed = 0
    fly_speed = 90
    climb_speed = 0
    hp_max = 59
    hit_dice = "7d10"
    spells = []


class PhaseSpider(Monster):
    """
    Ethereal Jaunt.
      As a bonus action, the spider can magically shift from the Material
      Plane to the Ethereal Plane, or vice versa.
    Spider Climb.
      The spider can climb difficult surfaces, including upside down on
      ceilings, without needing to make an ability check.
    Web Walker.
      The spider ignores movement restrictions caused by webbing.
    Bite.
      Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 7
      (1d10 + 2) piercing damage, and the target must make a DC 11
      Constitution saving throw, taking 18 (4d8) poison damage on a failed
      save, or half as much damage on a successful one. If the poison damage
      reduces the target to 0 hit points, the target is stable but poisoned
      for 1 hour, even after regaining hit points, and is paralyzed while
      poisoned in this way.
    """
    name = "Phase Spider"
    description = "Large monstrosity, unaligned"
    challenge_rating = 3
    armor_class = 13
    skills = "Stealth +6"
    senses = "Darkvision 60 ft., Passive Perception 10"
    languages = ""
    strength = Ability(15)
    dexterity = Ability(15)
    constitution = Ability(12)
    intelligence = Ability(6)
    wisdom = Ability(10)
    charisma = Ability(6)
    speed = 30
    swim_speed = 0
    fly_speed = 0
    climb_speed = 30
    hp_max = 32
    hit_dice = "5d10"
    spells = []


class PitFiend(Monster):
    """
    Fear Aura.
      Any creature hostile to the pit fiend that starts its turn within 20
      feet of the pit fiend must make a DC 21 Wisdom saving throw, unless
      the pit fiend is incapacitated. On a failed save, the creature is
      frightened until the start of its next turn. If a creature's saving
      throw is successful, the creature is immune to the pit fiend's Fear
      Aura for the next 24 hours.
    Magic Resistance.
      The pit fiend has advantage on saving throws against spells and other
      magical effects.
    Magic Weapons.
      The pit fiend's weapon attacks are magical.
    Innate Spellcasting.
      The pit fiend's spellcasting ability is Charisma (spell save DC 21).
      The pit fiend can innately cast the following spells, requiring no
      material components:
      
      At will: detect magic, fireball
      
      3/day each: hold monster, wall of fire
    Multiattack.
      The pit fiend makes four attacks: one with its bite, one with its
      claw, one with its mace, and one with its tail.
    Bite.
      Melee Weapon Attack: +14 to hit, reach 5 ft., one target. Hit: 22 (4d6
      + 8) piercing damage. The target must succeed on a DC 21 Constitution
      saving throw or become poisoned. While poisoned in this way, the
      target can't regain hit points, and it takes 21 (6d6) poison damage at
      the start of each of its turns. The poisoned target can repeat the
      saving throw at the end of each of its turns, ending the effect on
      itself on a success.
    Claw.
      Melee Weapon Attack: +14 to hit, reach 10 ft. , one target. Hit: 17
      (2d8 + 8) slashing damage.
    Mace.
      Melee Weapon Attack: +14 to hit, reach 10ft., one target. Hit: 15 (2d6
      + 8) bludgeoning damage plus 21 (6d6) fire damage.
    Tail.
      Melee Weapon Attack: +14 to hit, reach 10ft., one target. Hit: 24
      (3d1O + 8) bludgeoning damage.
    """
    name = "Pit Fiend"
    description = "Large fiend, lawful evil"
    challenge_rating = 20
    armor_class = 19
    skills = ""
    senses = "Truesight 120 ft., Passive Perception 14"
    languages = "Infernal, telepathy 120 ft."
    strength = Ability(26)
    dexterity = Ability(14)
    constitution = Ability(24)
    intelligence = Ability(22)
    wisdom = Ability(18)
    charisma = Ability(24)
    speed = 30
    swim_speed = 0
    fly_speed = 60
    climb_speed = 0
    hp_max = 300
    hit_dice = "24d10"
    spells = []


class Planetar(Monster):
    """
    Angelic Weapons.
      The planetar's weapon attacks are magical. When the planetar hits with
      any weapon, the weapon deals an extra 5d8 radiant damage (included in
      the attack).
    Divine Awareness.
      The planetar knows if it hears a lie.
    Innate Spellcasting.
      The planetar's spellcasting ability is Charisma (spell save DC 20).
      The planetar can innately cast the following spells, requiring no
      material components:
      
      At will: detect evil and good, invisibility (self only)
      
      3/day each: blade barrier, dispel evil and good, flame strike, raise
      dead
      
      1/day each: commune, control weather, insect plague
    Magic Resistance.
      The planetar has advantage on saving throws against spells and other
      magical effects.
    Multiattack.
      The planetar makes two melee attacks.
    Greatsword.
      Melee Weapon Attack: +12 to hit, reach 5 ft., one target. Hit: 21 (4d6
      + 7) slashing damage plus 22 (5d8) radiant damage.
    Healing Touch.
      The planetar touches another creature. The target magically regains 30
      (6d8 + 3) hit points and is freed from any curse, disease, poison,
      blindness, or deafness.
    """
    name = "Planetar"
    description = "Large celestial, lawful good"
    challenge_rating = 16
    armor_class = 19
    skills = "Perception +11"
    senses = "Truesight 120 ft., Passive Perception 21"
    languages = "all, telepathy 120 ft."
    strength = Ability(24)
    dexterity = Ability(20)
    constitution = Ability(24)
    intelligence = Ability(19)
    wisdom = Ability(22)
    charisma = Ability(25)
    speed = 40
    swim_speed = 0
    fly_speed = 120
    climb_speed = 0
    hp_max = 200
    hit_dice = "16d10"
    spells = []


class Plesiosaurus(Monster):
    """
    Hold Breath.
      The plesiosaurus can hold its breath for 1 hour.
    Bite.
      Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 14 (3d6
      + 4) piercing damage.
    """
    name = "Plesiosaurus"
    description = "Large beast, unaligned"
    challenge_rating = 2
    armor_class = 13
    skills = "Perception +3, Stealth +4"
    senses = "Passive Perception 13"
    languages = ""
    strength = Ability(18)
    dexterity = Ability(15)
    constitution = Ability(16)
    intelligence = Ability(2)
    wisdom = Ability(12)
    charisma = Ability(5)
    speed = 20
    swim_speed = 40
    fly_speed = 0
    climb_speed = 0
    hp_max = 68
    hit_dice = "8d10"
    spells = []


class PoisonousSnake(Monster):
    """
    Bite.
      Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 1
      piercing damage, and the target must make a DC 10 Constitution saving
      throw, taking 5 (2d4) poison damage on a failed save, or half as much
      damage on a successful one.
    """
    name = "Poisonous Snake"
    description = "Tiny beast, unaligned"
    challenge_rating = 0.125
    armor_class = 13
    skills = ""
    senses = "Blindsight 10 ft., Passive Perception 10"
    languages = ""
    strength = Ability(2)
    dexterity = Ability(16)
    constitution = Ability(11)
    intelligence = Ability(1)
    wisdom = Ability(10)
    charisma = Ability(3)
    speed = 30
    swim_speed = 30
    fly_speed = 0
    climb_speed = 0
    hp_max = 2
    hit_dice = "1d4"
    spells = []


class PolarBear(Monster):
    """
    Keen Smell.
      The bear has advantage on Wisdom (Perception) checks that rely on
      smell.
    Multiattack.
      The bear makes two attacks: one with its bite and one with its claws.
    Bite.
      Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 9 (1d8 +
      5) piercing damage.
    Claws.
      Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 12 (2d6
      + 5) slashing damage.
    """
    name = "Polar Bear"
    description = "Large beast, unaligned"
    challenge_rating = 2
    armor_class = 12
    skills = "Perception +3"
    senses = "Passive Perception 13"
    languages = ""
    strength = Ability(20)
    dexterity = Ability(10)
    constitution = Ability(16)
    intelligence = Ability(2)
    wisdom = Ability(13)
    charisma = Ability(7)
    speed = 40
    swim_speed = 30
    fly_speed = 0
    climb_speed = 0
    hp_max = 42
    hit_dice = "5d10"
    spells = []


class Pony(Monster):
    """
    Hooves.
      Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (2d4 +
      2) bludgeoning damage.
    """
    name = "Pony"
    description = "Medium beast, unaligned"
    challenge_rating = 0.125
    armor_class = 10
    skills = ""
    senses = "Passive Perception 10"
    languages = ""
    strength = Ability(15)
    dexterity = Ability(10)
    constitution = Ability(13)
    intelligence = Ability(2)
    wisdom = Ability(11)
    charisma = Ability(7)
    speed = 40
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    hp_max = 11
    hit_dice = "2d8"
    spells = []


class Priest(Monster):
    """
    Divine Eminence.
      As a bonus action, the priest can expend a spell slot to cause its
      melee weapon attacks to magically deal an extra 10 (3d6) radiant
      damage to a target on a hit. This benefit lasts until the end of the
      turn. If the priest expends a spell slot of 2nd level or higher, the
      extra damage increases by 1d6 for each level above 1st.
    Spellcasting.
      The priest is a 5th-level spellcaster. Its spellcasting ability is
      Wisdom (spell save DC 13, +5 to hit with spell attacks). The priest
      has the following cleric spells prepared:
      
  
      
      - Cantrips (at will): light, sacred flame, thaumaturgy
      
      - 1st level (4 slots): cure wounds, guiding bolt, sanctuary
      
      - 2nd level (3 slots): lesser restoration, spiritual weapon
      
      - 3rd level (2 slots): dispel magic, spirit guardians
    Mace.
      Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 3 (1d6)
      bludgeoning damage.
    """
    name = "Priest"
    description = "Medium humanoid, any alignment"
    challenge_rating = 2
    armor_class = 13
    skills = "Medicine +7, Persuasion +3, Religion +4"
    senses = "Passive Perception 13"
    languages = "any two languages"
    strength = Ability(10)
    dexterity = Ability(10)
    constitution = Ability(12)
    intelligence = Ability(13)
    wisdom = Ability(16)
    charisma = Ability(13)
    speed = 25
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    hp_max = 27
    hit_dice = "5d8"
    spells = ["light", "sacred flame", "thaumaturgy", "cure wounds", "guiding bolt", "sanctuary", "lesser restoration", "spiritual weapon", "dispel magic", "spirit guardians"]


class Pseudodragon(Monster):
    """
    Keen Senses.
      The pseudodragon has advantage on Wisdom (Perception) checks that rely
      on sight, hearing, or smell.
    Magic Resistance.
      The pseudodragon has advantage on saving throws against spells and
      other magical effects.
    Limited Telepathy.
      The pseudodragon can magically communicate simple ideas, emotions, and
      images telepathically with any creature within 100 ft. of it that can
      understand a language.
    Variant: Familiar.
      The pseudodragon can serve another creature as a familiar, forming a
      magic, telepathic bond with that willing companion. While the two are
      bonded, the companion can sense what the pseudodragon senses as long
      as they are within 1 mile of each other. While the pseudodragon is
      within 10 feet of its companion, the companion shares the
      pseudodragon's Magic Resistance trait. At any time and for any reason,
      the pseudodragon can end its service as a familiar, ending the
      telepathic bond.
    Bite.
      Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 +
      2) piercing damage.
    Sting.
      Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 4 (1d4
      + 2) piercing damage, and the target must succeed on a DC 11
      Constitution saving throw or become poisoned for 1 hour. If the saving
      throw fails by 5 or more, the target falls unconscious for the same
      duration, or until it takes damage or another creature uses an action
      to shake it awake.
    """
    name = "Pseudodragon"
    description = "Tiny dragon, neutral good"
    challenge_rating = 0.25
    armor_class = 13
    skills = "Perception +3, Stealth +4"
    senses = "Blindsight 10 ft., Darkvision 60 ft., Passive Perception 13"
    languages = "understands Common and Draconic but can't speak"
    strength = Ability(6)
    dexterity = Ability(15)
    constitution = Ability(13)
    intelligence = Ability(10)
    wisdom = Ability(12)
    charisma = Ability(10)
    speed = 15
    swim_speed = 0
    fly_speed = 60
    climb_speed = 0
    hp_max = 7
    hit_dice = "2d4"
    spells = []


class PurpleWorm(Monster):
    """
    Tunneler.
      The worm can burrow through solid rock at half its burrow speed and
      leaves a 10-foot-diameter tunnel in its wake.
    Multiattack.
      The worm makes two attacks: one with its bite and one with its
      stinger.
    Bite.
      Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 22 (3d8
      + 9) piercing damage. If the target is a Large or smaller creature, it
      must succeed on a DC 19 Dexterity saving throw or be swallowed by the
      worm. A swallowed creature is blinded and restrained, it has total
      cover against attacks and other effects outside the worm, and it takes
      21 (6d6) acid damage at the start of each of the worm's turns.
      
      If the worm takes 30 damage or more on a single turn from a creature
      inside it, the worm must succeed on a DC 21 Constitution saving throw
      at the end of that turn or regurgitate all swallowed creatures, which
      fall prone in a space within 10 feet of the worm. If the worm dies, a
      swallowed creature is no longer restrained by it and can escape from
      the corpse by using 20 feet of movement, exiting prone.
    Tail Stinger.
      Melee Weapon Attack: +9 to hit, reach 10 ft., one creature. Hit: 19
      (3d6 + 9) piercing damage, and the target must make a DC 19
      Constitution saving throw, taking 42 (12d6) poison damage on a failed
      save, or half as much damage on a successful one.
    """
    name = "Purple Worm"
    description = "Gargantuan monstrosity, unaligned"
    challenge_rating = 15
    armor_class = 18
    skills = ""
    senses = "Blindsight 30 ft., Tremorsense 60 ft., Passive Perception 9"
    languages = ""
    strength = Ability(28)
    dexterity = Ability(7)
    constitution = Ability(22)
    intelligence = Ability(1)
    wisdom = Ability(8)
    charisma = Ability(4)
    speed = 50
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    hp_max = 247
    hit_dice = "15d20"
    spells = []
