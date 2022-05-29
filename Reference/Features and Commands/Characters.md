# Character Commands

## New Character
To register a New Character: `v.chara new <chara_id> <name>`

When registering a new character to the databse you must assign them a **Character ID**, or `chara_id` for short.
- *Must be unique.*
- Can contain up to 5 characters.
- Can be a mix of letters and numbers.
- Are Case Sensitive.
- *Cannot be changed at this time.*

The `chara_id` is what will be used to search for, and update, their information.

You may add a character's name at the time of registration, or you may later use the Update Command to add their name.

## Information Cards
To view a Character Card: `v.chara <type> <chara_id>`

There are, at current, three different types of Character Cards that you can view. More cards are currently in consideration, however.
- **Base**
    - 'Type' Command: `base`
    - Contains a character's Summary, Pronouns, Age, Date of Birth, Physical Desription, and Notes.
- **Battle**
    - 'Type' Command: `battle`
    - Contains a character's Battle Style/Summary, Base Health, Evasion, and Defense, Weapons, and Specials/Skills.
- **Social**
    - 'Type' Command: `social`
    - Contains information on a character's relations to Family, Friends, Enemies, and 'Specific'.

*Note: A character's Name, Emoji, Avatar, and Hex Code are cross-card information, meaning it is used across all of the different card types.*

## Updating Information
To update a Character's Information: `v.chara update <field> <chara_id> <value>`

When updating characters, it is important to note the order you put the command in:
- The field being updated needs to go first.
- The ID of the character you're updating needs to be second.
- The information you're adding needs to be last.

It is important to note that only the Creator of a character can edit their information.

### Main

This contains information that can be found on most, if not all, the different types of Character Cards.
- **Name**
    - 'Field' Command: `name`
    - Can contain up to 20 characters.
    - May contain spaces and special characters.
- **Emoji**
    - 'Field' Command: `emoji`
    - Can either be inputted by copy & pasting a plain emoji, or by using discord's emoji format (i.e. `:smile:`)
    - Can contain multiple emojis.
- **Avatar**
    - 'Field' Command: `avi`
    - *Note: It is best to use a Discord Attachment URL.*
- **Hex Code**
    - 'Field' Command: `hexc` or `hex`
    - *Note: Only put the hexcode, do not include the #.*

### Base

This contains information that will be found on the Base Information card.
- **Summary**
    - 'Field' Command: `summary`
    - Can contain up to 250 characters.
    - Can contain line breaks.
    - Can contain formatting (bold, italic, underline, code)
- **Pronouns**
    - 'Field' Command: `pronouns`
    - Can contain line breaks.
- **Age**
    - 'Field' Command: `age`
- **Date of Birth**
    - 'Field' Command: `dob`, `birthday`, or `bday`
- **Physical Description**
    - 'Field' Command: `physdesc`
    - Can contain up to 1000 characters.
    - Can contain line breaks.
    - Can contain formatting (bold, italic, underline, code)
- **Notes**
    - 'Field' Command: `notes`
    - Can contain up to 1000 characters.
    - Can contain line breaks.
    - Can contain formatting (bold, italic, underline, code)

### Battle

This contains information that will be found on the Battle Information card.
- **Battle Style/Summary**
    - 'Field' Command: `bsum`, `bsummary`, or `bstyle`
    - Can contain up to 250 characters.
    - Can contain line breaks.
    - Can contain formatting (bold, italic, underline, code)
- **Base Health**
    - 'Field' Command: `health` or `hp`
- **Base Evasion**
    - 'Field' Command: `evasion` or `ev`
- **Base Defense**
    - 'Field' Command: `defense` or `def`
- **Weapons**
    - 'Field' Command: `weapons`
    - Can contain up to 1000 characters.
    - Can contain line breaks.
    - Can contain formatting (bold, italic, underline, code)
    - *Note: All Weapons and their information would need to be inputted together.*
- **Specials/Skills**
    - 'Field' Command: `specials`
    - Can contain up to 1000 characters.
    - Can contain line breaks.
    - Can contain formatting (bold, italic, underline, code)
    - *Note: All Specials/Skills and their information would need to be inputted together.*

### Social

This contains information that will be found on the Social Information card.   
*Note: All information for each relation type would need to be inputted together.*
- **Family**
    - 'Field' Command: `family` or `fam`
    - Can contain up to 1000 characters.
    - Can contain line breaks.
    - Can contain formatting (bold, italic, underline, code)
- **Friends**
    - 'Field' Command: `friends`
    - Can contain up to 1000 characters.
    - Can contain line breaks.
    - Can contain formatting (bold, italic, underline, code)
- **Enemies**
    - 'Field' Command: `enemies`
    - Can contain up to 1000 characters.
    - Can contain line breaks.
    - Can contain formatting (bold, italic, underline, code)
- **Specific**
    - 'Field' Command: `specific`
    - Can contain up to 1000 characters.
    - Can contain line breaks.
    - Can contain formatting (bold, italic, underline, code)
    - *Note: This would include relations specific to certain characters (e.g. Rival, Lover)*