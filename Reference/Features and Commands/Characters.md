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
- **Name**
    - Field Command: `name`
    - Can contain up to 20 characters.
    - May contain spaces and special characters.
- **Emoji**
    - Field Command: `emoji`
    - Can either be inputted by copy & pasting a plain emoji, or by using discord's emoji format (i.e. `:smile:`)
    - Can contain multiple emojis.
- **Avatar**
    - Field Command: `avi`
    - *Note: It is best to use a Discord Attachment URL.*
- **Hex Code**
    - Field Command: `hexc` or `hex`
    - *Note: Only put the hexcode, do not include the #.*

### Base

This contains information that will be found on the Base Information card.
- **Summary**
    - Field Command: `summary`
    - Can contain up to 250 characters.
    - Can contain line breaks.
    - Can contain formatting (bold, italic, underline, code)
- **Pronouns**
    - Field Command: `pronouns`
    - Can contain line breaks.
- **Age**
    - Field Command: `age`
- **Date of Birth**
    - Field Command: `dob`, `birthday`, or `bday`
- **Physical Description**
    - Field Command: `physdesc`
    - Can contain up to 1000 characters.
    - Can contain line breaks.
    - Can contain formatting (bold, italic, underline, code)
- **Notes**
    - Field Command: `notes`
    - Can contain up to 1000 characters.
    - Can contain line breaks.
    - Can contain formatting (bold, italic, underline, code)

### Battle

This contains information that will be found on the Battle Information card.
- **Battle Style/Summary**
    - Field Command: `bsum`, `bsummary`, or `bstyle`
    - Can contain up to 250 characters.
    - Can contain line breaks.
    - Can contain formatting (bold, italic, underline, code)
- **Base Health**
    - Field Command: `health` or `hp`
- **Base Evasion**
    - Field Command: `evasion` or `ev`
- **Base Defense**
    - Field Command: `defense` or `def`
- **Weapons**
    - Field Command: `weapons`
    - Can contain up to 1000 characters.
    - Can contain line breaks.
    - Can contain formatting (bold, italic, underline, code)
    - *Note: All Weapons and their information would need to be inputted together.*
- **Specials/Skills**
    - Field Command: `specials`
    - Can contain up to 1000 characters.
    - Can contain line breaks.
    - Can contain formatting (bold, italic, underline, code)
    - *Note: All Specials/Skills and their information would need to be inputted together.*

### Social

This contains information that will be found on the Social Information card.   
*Note: All information for each relation type would need to be inputted together.*
- **Family**
    - Field Command: `family` or `fam`
    - Can contain up to 1000 characters.
    - Can contain line breaks.
    - Can contain formatting (bold, italic, underline, code)
- **Friends**
    - Field Command: `friends`
    - Can contain up to 1000 characters.
    - Can contain line breaks.
    - Can contain formatting (bold, italic, underline, code)
- **Enemies**
    - Field Command: `enemies`
    - Can contain up to 1000 characters.
    - Can contain line breaks.
    - Can contain formatting (bold, italic, underline, code)
- **Specific**
    - Field Command: `specific`
    - Can contain up to 1000 characters.
    - Can contain line breaks.
    - Can contain formatting (bold, italic, underline, code)
    - *Note: This would include relations specific to certain characters (e.g. Rival, Lover)*