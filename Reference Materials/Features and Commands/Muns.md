# Mun Commands
This will get some more in depth information later, I promise.

**Table of Contents:**
- [New Mun](https://github.com/Zyhod/Vieno/blob/main/Reference%20Materials/Features%20and%20Commands/Muns.md#new-mun)
- [Mun Cards](https://github.com/Zyhod/Vieno/blob/main/Reference%20Materials/Features%20and%20Commands/Muns.md#mun-cards)
- [Updating Information](https://github.com/Zyhod/Vieno/blob/main/Reference%20Materials/Features%20and%20Commands/Muns.md#updating-information)

## New Mun
To register yourself as a New Mun: `v.mun new <mun_id>`

When registering a New Mun to the databse you must assign yourself a **Mun ID**, or `mun_id`.
- *Must be unique.*
- Can contain up to 5 characters.
- Can be a mix of letters and numbers.
- Are Case Sensitive.

The `chara_id` is what will be used to search for your information.

*(Tip) Checking if the `mun_id` has already been taken may be beneficial.*

[^ Back to Top](https://github.com/Zyhod/Vieno/blob/main/Reference%20Materials/Features%20and%20Commands/Muns.md#mun-commands)

## Mun Cards
To view a Mun Card: `v.mun <type> <mun_id>`

At the moment, there are two types of Mun Cards that can be found.
- **Info Card**
    - 'Type' Command: `information` or `info`
    - Contains information about a Mun's Name, Description, Pronouns, Age & Date of Birth, Timezone, Activity Status, and Number of Characters Registered.
    - Shows a Mun's Avatar, Banner, and Hex Code.
- **All Characters**
    - 'Type' Command: `characters`, `charas`, or `muses`
    - Contains the `chara_id` and `names` of all characters registered to that mun.
- **Original Characters**
    - 'Type' Command: `originalc`, `original`, or `oc`
    - Contains the `chara_id` and `names` of all original characters registered to that mun.
- **Fan Characters**
    - 'Type' Command: `fanc`, `fan`, or `fc`
    - Contains the `chara_id` and `names` of all original characters registered to that mun.
- **Canon Characters**
    - 'Type' Command: `canonc`, `canon`, or `cc`
    - Contains the `chara_id` and `names` of all original characters registered to that mun.
- **Unspecified Characters**
    - 'Type' Command: `unspecifiedc`, `unspecified`, or `uc`
    - Contains the `chara_id` and `names` of all original characters registered to that mun.

    [^ Back to Top](https://github.com/Zyhod/Vieno/blob/main/Reference%20Materials/Features%20and%20Commands/Muns.md#mun-commands)

## Updating Information
To update your Information: `v.mun update <field> <value>`

Unlike Characters, you do not need to add your mun_id in order to update your information.

You are able to update/change most, if not all, information found on your Mun Card.
- **Mun ID**
    - 'Field' Command: `m_id`, `mid`, or `munid`
    - See [New Mun](https://github.com/Zyhod/Vieno/blob/main/Reference%20Materials/Features%20and%20Commands/Muns.md#new-mun) for specifications.
- **Name**
    - 'Field' Command: `name`
    - Can contain up to 20 characters.
    - May contain spaces and special characters.
- **Emoji**
    - 'Field' Command: `emoji`
    - Can either be inputted by copy & pasting a plain emoji, or by using discord's emoji format (i.e. `:smile:`)
    - Can contain multiple emojis.
- **Description**
    - 'Field' Command: `description` or `desc`
    - Can contain up to 1000 characters.
    - Can contain emojis.
    - Can contain line breaks.
    - Can contain formatting (bold, italic, underline, code)
- **Pronouns**
    - 'Field' Command: `pronouns`
    - Can contain line breaks.
- **Date of Birth (Age)**
    - 'Field' Command: `dobage`
    - *(Note) Shares the field, so putting both is beneficial.*
- **Timezone**
    - 'Field' Command: `timezone` or `tz`
    - Can use any formatting, though UTC is most universal.
- **Activity Status**
    - 'Field' Command: `status`
    - Can contain up to 200 characters.
    - Can contain emojis.
    - Can contain line breaks.
    - Can contain formatting (bold, italic, underline, code)
- **Avatar**
    - 'Field' Command: `avi`
    - *(Note) It is best to use a Discord Attachment URL.*
- **Hex Code**
    - 'Field' Command: `hexc` or `hex`
    - *(Note) Only put the hexcode, do not include the #.*
- **Banner**
    - 'Field' Command: `banner`
    - *(Note) It is best to use a Discord Attachment URL.*

[^ Back to Top](https://github.com/Zyhod/Vieno/blob/main/Reference%20Materials/Features%20and%20Commands/Muns.md#mun-commands)