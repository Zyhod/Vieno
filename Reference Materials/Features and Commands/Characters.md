# Character Commands

**Table of Contents**
- [Register Character](https://github.com/Zyhod/Vieno/blob/main/Reference%20Materials/Features%20and%20Commands/Characters.md#register-character)
- [Remove Character](https://github.com/Zyhod/Vieno/blob/main/Reference%20Materials/Features%20and%20Commands/Characters.md#remove-character)
- [Information Cards](https://github.com/Zyhod/Vieno/blob/main/Reference%20Materials/Features%20and%20Commands/Characters.md#information-cards)
- [Editing Information](https://github.com/Zyhod/Vieno/blob/main/Reference%20Materials/Features%20and%20Commands/Characters.md#editing-information)
    - [Main](https://github.com/Zyhod/Vieno/blob/main/Reference%20Materials/Features%20and%20Commands/Characters.md#main)
    - [Base](https://github.com/Zyhod/Vieno/blob/main/Reference%20Materials/Features%20and%20Commands/Characters.md#base)
    - [Links](https://github.com/Zyhod/Vieno/blob/main/Reference%20Materials/Features%20and%20Commands/Characters.md#links)
    - [Combat](https://github.com/Zyhod/Vieno/blob/main/Reference%20Materials/Features%20and%20Commands/Characters.md#combat)
    - [Social](https://github.com/Zyhod/Vieno/blob/main/Reference%20Materials/Features%20and%20Commands/Characters.md#social)

## Register Character
To Register a New Character: `v.chara register <chara_id> <name>`  
*Can use `reg` or `new` in place of `register`.*

When registering a new character to the database you must assign them a **Character ID**, or `chara_id` for short.
- *Must be unique.*
- Can contain up to 5 characters.
- Can be a mix of letters and numbers.
- Are Case Sensitive.
- *Cannot be changed at this time.*

The `chara_id` is what will be used to search for, and update, their information.

*(Optional) You may add a character's name at the time of registration, or you may later use the Update Command to add their name.*

*(Tip) Checking if the `chara_id` has already been taken may be beneficial.*

[^ Back to Top](https://github.com/Zyhod/Vieno/blob/main/Reference%20Materials/Features%20and%20Commands/Characters.md#character-commands)

## Remove Character
To remove a Character: `v.chara remove <chara_id>`  
*Can use `delete` or `del` in place of `remove`.*

This permanently removes all records of the specified character from:
- Main Records
- Base Records
- Battle Records
- Social Records
- Links Records

*(Note) It is important to note that only the Creator of a character can remove their records.*

[^ Back to Top](https://github.com/Zyhod/Vieno/blob/main/Reference%20Materials/Features%20and%20Commands/Characters.md#character-commands)

## Information Cards
To view a Character Card: `v.chara <type> <chara_id>`

There are, at current, three different types of Character Cards that you can view. More cards are currently in consideration, however.
- **Base**
    - 'Type' Command: `base`
    - Contains a character's Summary, Pronouns, Age, Date of Birth, Species, Size, Notes & Trivia, and Associated Links.
- **Battle**
    - 'Type' Command: `battle`
    - Contains a character's Battle Style/Summary, Base Health, Evasion, and Defense, Weapons, and Specials/Skills.
- **Social**
    - 'Type' Command: `social`
    - Contains information on a character's relations to Family, Friends, Enemies, and 'Specific'.

*(Note) A character's Name, Emoji, Avatar, and Hex Code are cross-card information, meaning it is used across all of the different card types.*

[^ Back to Top](https://github.com/Zyhod/Vieno/blob/main/Reference%20Materials/Features%20and%20Commands/Characters.md#character-commands)

## Editing Information
To update a Character's Information: `v.<update/strike> <area> <field> <chara_id> <value>`

There are two ways you can edit a character's information:
- Updating
    - Full Command: `v.update <area> <field> <chara_id> <value>`
    - Updates/Aadds information in the character's records in a specific field.
- Striking
    - Full Command: `v.strike <area> <field> <chara_id>`
    - Removes/Resets information in the character's records in a specific field.

When Updating Characters, it is important to note the order you put the command in:
- The area that information is being updated in needs to go first.
- The field being updated needs to go second.
- The ID of the character you're updating needs to be third.
- The information you're adding needs to be last.

*(Note) It is important to know that only the Creator of a character can edit their information.*

There are several Areas that information can be edited in.

---

### Main
'Area' Command: `main`

This contains information that can be found on most, if not all, the different types of Character Cards.
- **Name**
    - 'Field' Command: `name`
    - Can contain up to 20 characters.
    - May contain spaces and special characters.
    - *(Note) This information cannot be Removed/Reset.*
- **Emoji**
    - 'Field' Command: `emoji`
    - Can either be inputted by copy & pasting a plain emoji, or by using discord's emoji format (i.e. `:smile:`)
    - Can contain multiple emojis.
- **Avatar**
    - 'Field' Command: `avatar` or `avi`
    - *(Note) It is best to use a Discord Attachment URL.*
- **Hex Code**
    - 'Field' Command: `hexc` or `hex`
    - *(Note) Only put the hexcode, do not include the #.*

[^ Back to Top](https://github.com/Zyhod/Vieno/blob/main/Reference%20Materials/Features%20and%20Commands/Characters.md#character-commands)

---

### Base
'Area' Command: `base`

This contains information that will be found on the Base Information card.
- **Summary**
    - 'Field' Command: `summary` or `sum`
    - Can contain up to 250 characters.
    - Can contain emojis.
    - Can contain line breaks.
    - Can contain formatting (bold, italic, underline, code)
- **Pronouns**
    - 'Field' Command: `pronouns`
    - Can contain line breaks.
- **Age**
    - 'Field' Command: `age`
- **Date of Birth**
    - 'Field' Command: `dob`, `birthday`, or `bday`
- **Species**
    - 'Field' Command: `species`
    - Can contain up to 50 characters.
    - Can contain line breaks.
    - Can contain formatting (bold, italic, underline, code)
- **Size**
    - 'Field' Command: `size` or `height`
    - Can contain up to 50 characters.
    - Can contain line breaks.
    - Can contain formatting (bold, italic, underline, code)
    - *(Note) Doesn't seem like the bot likes it when quotations are inputed as part of the `value`.*
        - *If inputing in Imperial, use ft and in instead (e.g. 6'02" -> 6ft 02in)*
- **Notes**
    - 'Field' Command: `notes`
    - Can contain up to 1000 characters.
    - Can contain emojis.
    - Can contain line breaks.
    - Can contain formatting (bold, italic, underline, code)

[^ Back to Top](https://github.com/Zyhod/Vieno/blob/main/Reference%20Materials/Features%20and%20Commands/Characters.md#character-commands)

### Links
'Area' Command: `links` or `link`

This contains information that will be found on the Base Information card.

When updating Links, it is important to note that there are *two* 'value's after `chara_id` -- `url` and then `title`.
- The `url` can be any length.
- The `title` may contain up to 50 characters.
- The `title` may contain Spaces & Emojis.
- Neither may be left blank.

At the moment, you can set up to four Custom Links:
- **Link One**
    - 'Field' Command: `one` or `1`
    - Adds an associated link into Slot One.
- **Link Two**
    - 'Field' Command: `two` or `2`
    - Adds an associated link into Slot Two.
- **Link Three**
    - 'Field' Command: `three` or `3`
    - Adds an associated link into Slot Three.
- **Link Four**
    - 'Field' Command: `four` or `4`
    - Adds an associated link into Slot Four.

*There is an additional command when Striking information:*
- **All Links**
    - 'Field' Command: `all`
    - Removes all Associated Links from a character.

[^ Back to Top](https://github.com/Zyhod/Vieno/blob/main/Reference%20Materials/Features%20and%20Commands/Characters.md#character-commands)

---

### Combat
'Area' Command: `combat`

This contains information that will be found on the Combat Information card.
- **Combat Style/Summary**
    - 'Field' Command: `summary`, `sum`, or `style`
    - Can contain up to 250 characters.
    - Can contain emojis.
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
    - Can contain emojis.
    - Can contain line breaks.
    - Can contain formatting (bold, italic, underline, code)
    - *(Note) All Weapons and their information would need to be inputted together.*
- **Specials/Skills**
    - 'Field' Command: `specials` or `skills`
    - Can contain up to 1000 characters.
    - Can contain emojis.
    - Can contain line breaks.
    - Can contain formatting (bold, italic, underline, code)
    - *(Note) All Specials/Skills and their information would need to be inputted together.*

[^ Back to Top](https://github.com/Zyhod/Vieno/blob/main/Reference%20Materials/Features%20and%20Commands/Characters.md#character-commands)

---

### Social
'Area' Command: `social`

This contains information that will be found on the Social Information card.   
*(Note) All information for each relation type would need to be inputted together.*
- **Family Members**
    - 'Field' Command: `family` or `fam`
    - Can contain up to 1000 characters.
    - Can contain emojis.
    - Can contain line breaks.
    - Can contain formatting (bold, italic, underline, code)
- **Friends**
    - 'Field' Command: `friends`
    - Can contain up to 1000 characters.
    - Can contain emojis.
    - Can contain line breaks.
    - Can contain formatting (bold, italic, underline, code)
- **Enemies**
    - 'Field' Command: `enemies`
    - Can contain up to 1000 characters.
    - Can contain emojis.
    - Can contain line breaks.
    - Can contain formatting (bold, italic, underline, code)
- **Special Relations**
    - 'Field' Command: `specific`, `special` or `spec`
    - Can contain up to 1000 characters.
    - Can contain emojis.
    - Can contain line breaks.
    - Can contain formatting (bold, italic, underline, code)
    - *(Note) This would include relations specific to certain characters (e.g. Rival, Lover)*

[^ Back to Top](https://github.com/Zyhod/Vieno/blob/main/Reference%20Materials/Features%20and%20Commands/Characters.md#character-commands)