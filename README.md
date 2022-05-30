# Vieno: An Archiver for Roleplay Servers
Vieno is a bot made specifically for use in Roleplay Servers. At the moment, use of this bot is *very* exclusive to a small group of people.

## Quick Links
- [Q & A](https://github.com/Zyhod/Vieno/blob/main/Reference%20Materials/QnA.md)
- Commands
    - [Characters](https://github.com/Zyhod/Vieno/blob/main/Reference%20Materials/Features%20and%20Commands/Characters.md)
    - ~~[Just for Fun](https://github.com/Zyhod/Vieno/blob/main/Reference%20Materials/Features%20and%20Commands/Just%20For%20Fun.md)~~ *Not Yet Complete*
    - [Muns](https://github.com/Zyhod/Vieno/blob/main/Reference%20Materials/Features%20and%20Commands/Muns.md)
    - ~~[Roleplay Related](https://github.com/Zyhod/Vieno/blob/main/Reference%20Materials/Features%20and%20Commands/Roleplay%20Related.md)~~ *Not Yet Complete*

## Future Plans
- [x] Character Cards...
    - [x] Create/Set Up Battle Card
    - [x] Create/Set Up Social Card
    - [x] Debate whether or not adding a Link Card would be necessary.
- [x] Figure out a way to remove a Character from The Archive.
    - *Should be simple enough, just need to refresh myself on SQL a bit.*
- [ ] Figure out a way to look up Character & Chara IDs; maybe by Mun IDs?
    - *Hardest part will probably be organizing information into an embed.*
- [ ] Example Command Group to show...
    - [ ] Example Mun Card
    - [ ] Example Character Cards (Base, Battle, Social, etc)

## Updates

__*May 30th, 2022*__
- Added a Strike Command in order to remove Character Information in all Fields except `name`.
- Created seperate Command Groups for `update` and `strike`.
    - *This was due to how the amount of available fields growing too large to contain under the `chara` group.*
- Renamed the area 'Battle' to 'Combat'.
- Created/Set Up Character Social Card

__*May 29th, 2022*__
- Can now Name a character upon registry (`v.chara new <chara_id> <name>`).
- Created/Set Up Battle Information Card.
    - Commands for updating Battle Information 
- Reference Materials Updated
    - Characters
    - Muns
- Added a Character Removal Command
- Added a Chara_Links table, which gets used in the Base Cards.