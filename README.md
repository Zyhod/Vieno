# Vieno: An Archiver for Roleplay Servers
Vieno is a bot made specifically for use in Roleplay Servers. At the moment, use of this bot is *very* exclusive to a small group of people.

## Quick Links
- [Q & A](https://github.com/Zyhod/Vieno/blob/main/Reference%20Materials/QnA.md)
- Commands
    - [Characters](https://github.com/Zyhod/Vieno/blob/main/Reference%20Materials/Features%20and%20Commands/Characters.md)
    - [Muns](https://github.com/Zyhod/Vieno/blob/main/Reference%20Materials/Features%20and%20Commands/Muns.md)
    - [Roleplay Related](https://github.com/Zyhod/Vieno/blob/main/Reference%20Materials/Features%20and%20Commands/Roleplay%20Related.md)
    - [Misc Commands](https://github.com/Zyhod/Vieno/blob/main/Reference%20Materials/Features%20and%20Commands/Misc%20Commands.md)

## Future Plans
*Update June 3rd, 2022*
- [x] Add 'Server ID' to Characters
    - This would take in What Server a character was made in, setting it as their 'Home Server'.
- [x] Funds/Balance section.
    - Plan is so that only Mods of the character's 'Home Server' can change how much a Character has.

## Updates

__*June 3rd, 2022*__
- Added 'Server ID' to Character's Main Information.
- Added Funds/Balance to Character's Base Information.
    - Made it so only Mods of a character's Home Server can use this command.

__*May 31st, 2022*__
- Created/Set Up Example Command Group.
- Added ability to define whether a character is an Original, Fan, or Canon character.
- Added ability to define what instance/story/campaign a character comes from.
- Added ability to look up a Mun's characters based on Original, Fan, Canon, or 'Unspecified'.

__*May 30th, 2022*__
- ~~Added a Strike Command in order to remove Character Information in all Fields except `name`.~~
    - Removed this in favor of leaving `value` blank in update commands.
- Created seperate Command Groups for `update` ~~and `strike`.~~
    - *This was due to how the amount of available fields growing too large to contain under the `chara` group.*
- Renamed the area 'Battle' to 'Combat'.
- Created/Set Up Character Social Card.
- Made a way to search up Character & Character IDs by Mun IDs.
    - *I was wrong; the hardest part was figuring out how to list the information.*
- Added ability to add Modifiers to Roll command.
- Renamed 'Just for Fun' to 'Misc Commands'.
- Added information to both '[Roleplay Related](https://github.com/Zyhod/Vieno/blob/main/Reference%20Materials/Features%20and%20Commands/Roleplay%20Related.md)' and '[Misc Commands](https://github.com/Zyhod/Vieno/blob/main/Reference%20Materials/Features%20and%20Commands/Misc%20Commands.md)' Reference Materials.

__*May 29th, 2022*__
- Can now Name a character upon registry (`v.chara new <chara_id> <name>`).
- Created/Set Up Battle Information Card.
    - Commands for updating Battle Information 
- Reference Materials Updated
    - Characters
    - Muns
- Added a Character Removal Command
- Added a Chara_Links table, which gets used in the Base Cards.