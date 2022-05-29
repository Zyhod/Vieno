# Character Commands

## Information Cards

There are, at the moment, three types of Character Cards. More types of cards are in consideration, however.

*Note: A character's Name, Emoji, Avatar, and Hex Code are cross-card information, meaning it is used across all of the different card types.*

### Base
`v.chara base <chara_id>`

This contains base information about the character.
- Character Summary
- Pronouns
- Age
- Date of Birth
- Physical Description
- Character Notes

### Battle
`v.chara battle <chara_id>`

This contains battle information about the character.
- Battle Style/Summary
- Base Health, Evasion, and Defense
- Weapons
- Specials/Skills

### Social
`v.chara social <chara_id>`

This contains information regarding relations to other characters.
- Family
- Friends
- Enemies
- Specific

## Updating Information

Updating information regarding to a character currently falls into four seperate categories.

### Main

This contains information that can be found on most, if not all, the different types of Character Cards.
- Name `v.chara update name <chara_id> <name>`
- Emoji `v.chara update emoji <chara_id> <emoji>`
- Avatar `v.chara update avi <chara_id> <url>`
    - *Note: It is best to use a Discord Attachment URL.*
- Hex Code `v.chara update hexc <chara_id> <hex>`
    - *Note: Only put the hexcode, not the #.*

### Base

This contains information that will be found on the Base Information card.
- Summary `v.chara update summary <chara_id> <summary>`
- Pronouns `v.chara update pronouns <chara_id> <pronouns>`
- Age `v.chara update age <chara_id> <age>`
- Date of Birth `v.chara update dob <chara_id> <Month 00>`
- Physical Description `v.chara update physdesc <chara_id> <desc>`
- Notes `v.chara update notes <chara_id> <notes>`

### Battle

This contains information that will be found on the Battle Information card.
- Battle Style/Summary `v.chara update bsum <chara_id> <desc>`
- Base Health `v.chara update hp <chara_id> <value>`
- Base Evasion `v.chara update ev <chara_id> <value>`
- Base Defense `v.chara update def <chara_id> <value>`
- Weapons `v.chara update weapons <chara_id> <weapons>`
    - *Note: All Weapons and their information would need to be inputted together.*
- Specials/Skills `v.chara update specials <chara_id> <specials>`
    - *Note: All Specials/Skills and their information would need to be inputted together.*

### Social

This contains information that will be found on the Social Information card.
    *Note: All information for each relation type would need to be inputted together.*
- Family `v.chara update family <chara_id> <family>`
- Friends `v.chara update friends <chara_id> <friends>`
- Enemies `v.chara update enemies <chara_id> <enemies>`
- Specific `v.chara update specific <chara_id> <specific>`
    - *This would include relations specific to certain characters. An Example would be a Rival, or a Lover.*