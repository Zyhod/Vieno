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

When updating characters, it is important to note the order you put the command in.  
`v.chara update <field> <chara_id> <value>`
- The field being updated needs to go first.
- The ID of the character you're updating needs to be second.
- The information you're adding needs to be last.

### Main

This contains information that can be found on most, if not all, the different types of Character Cards.
- Name (*name*)
- Emoji (*emoji*)
- Avatar (*avi*)
    - *Note: It is best to use a Discord Attachment URL.*
- Hex Code (*hexc, hex*)
    - *Note: Only put the hexcode, not the #.*

### Base

This contains information that will be found on the Base Information card.
- Summary (*summary*)
- Pronouns (*pronouns*)
- Age (*age*)
- Date of Birth (*dob, birthday, bday*)
- Physical Description (*physdesc*)
- Notes (*notes*)

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