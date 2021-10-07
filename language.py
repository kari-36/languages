
# languages
curr_chat_lang: "Hey. Your current language is {}, select the one you want from the buttons below :)"
set_chat_lang: "Great, {} it is from now on!"


pm_start_text: |
   Hi {}, I'm {},
   I am an Anime themed group management bot with some fun extras ;)
   
   I can do a variety of things, most common of em are:
   - Restrict users with *ban permissions*.
   - Greet users with media + text and buttons, with proper formatting.
   - Restrict users who flood your chat using my *anti-flood* module.
   - *Warn* users according to the options set and restrict em accordingly.
   - Save notes and filters with proper formatting and reply markup.
   
   Theres even more! this is just the tip of the iceberg. Do note I need
   to be promoted with proper admin permissions to function properly. 
   Else I won't be able to function as said.
   
   *Click on help to learn more!*
   
grp_start_text: "Hi, I'm Elaina."

pm_help_text: |
   Hello there! My name is *Elaina*.
   I'm a modular group management bot with a few fun extras! Have a look at the following for an idea of some of
   the things I can help you with.
   *Main* commands available:
    • /start: Starts me, can be used to check I'm alive or not.
    • /help: PM's you this message.
    • /language: Change bot language.
    • /settings:
      - in PM: will send you your settings for all supported modules.
      - in a group: will redirect you to pm, with all that chat's settings.
    Click on the buttons below to get documentation about specific modules!

add_bot_to_group_btn: "Add Elaina"
support_chat_link_btn: "Support"
updates_channel_link_btn: "Elaina News"
src_btn: "Source code"

admin_help: |
   • `/admins`*:* list of admins in the chat

   *Admins only:*
   • `/pin`*:* silently pins the message replied to - add `'loud'` or `'notify'` to give notifs to users.
   • `/unpin`*:* unpins the currently pinned message
   • `/invitelink`*:* gets invitelink
   • `/promote`*:* promotes the user replied to
   • `/demote`*:* demotes the user replied to
   • `/title <title here>`*:* sets a custom title for an admin that the bot promoted

afk_help: |
   - /afk <reason>: mark yourself as AFK(away from keyboard).
   - brb <reason>: same as the afk command - but not a command.
   When marked as AFK, any mentions will be replied to with a message to say you're not available!

anilist_help: |
    *AniList*
    Get information about anime, manga or characters with the help of this module! All data is fetched from [AniList](anilist.co).
    *Available commands:*
     - /anime <anime>: returns information about the anime.
     - /character <character>: returns information about the character.
     - /manga <manga>: returns information about the manga.

antiflood_help: |
    Antiflood allows you to take action on users that send more than x messages in a row. Exceeding the set flood
    will result in restricting that user.
     This will mute users if they send more than 10 messages in a row, bots are ignored.
     • `/flood`*:* Get the current flood control setting
    • *Admins only:*
     • `/setflood <int/'no'/'off'>`*:* enables or disables flood control
     *Example:* `/setflood 10`
     • `/setfloodmode <ban/kick/mute/tban/tmute> <value>`*:* Action to perform when user have exceeded flood limit. ban/kick/mute/tmute/tban
    • *Note:*
     • Value must be filled for tban and tmute!!
     It can be:
     `5m` = 5 minutes
     `6h` = 6 hours
     `3d` = 3 days
     `1w` = 1 week

approve_help: |
     Sometimes, you might trust a user not to send unwanted content.
     Maybe not enough to make them admin, but you might be ok with locks, blacklists, and antiflood not applying to them.
     That's what approvals are for - approve of trustworthy users to allow them to send
     *Admin commands:*
     • `/approval`*:* Check a user's approval status in current chat.
     • `/approve`*:* Approve of a user. Locks, blacklists, and antiflood won't apply to them anymore.
     • `/unapprove`*:* Unapprove of a user. They will now be subject to locks, blacklists, and antiflood again.
     • `/approved`*:* List all approved users.
     • `/unapproveall`*:* Unapprove *ALL* users in a chat. This cannot be undone.

backup_help: |
    *Admin only:*
     - /import: reply to a group butler backup file to import as much as possible, making the transfer super simple! Note \
       that files/photos can't be imported due to telegram restrictions.
     - /export: Export group data, which will be exported are: rules, notes (documents, images, music, video, audio, voice, text, text buttons)

bans_help: |
    - /kickme: kicks the user who issued the command

     *Admin only:*
    - /ban <userhandle>: bans a user. (via handle, or reply)
    - /tban <userhandle> x(m/h/d): bans a user for x time. (via handle, or reply). m = minutes, h = hours, d = days.
    - /unban <userhandle>: unbans a user. (via handle, or reply)
    - /kick <userhandle>: kick a user out of the group, (via handle, or reply)

blacklist_help: |
    Blacklists are used to stop certain triggers from being said in a group. Any time the trigger is mentioned, the message will immediately be deleted. A good combo is sometimes to pair this up with warn filters!

    *NOTE*: Blacklists do not affect group admins.

     • `/blacklist`*:* View the current blacklisted words.

    Admin only:
     • `/addblacklist <triggers>`*:* Add a trigger to the blacklist. Each line is considered one trigger, so using different lines will allow you to add multiple triggers.
     • `/unblacklist <triggers>`*:* Remove triggers from the blacklist. Same newline logic applies here, so you can remove multiple triggers at once.
     • `/blacklistmode <off/del/warn/ban/kick/mute/tban/tmute>`*:* Action to perform when someone sends blacklisted words.

cleaner_help: |
    - /cleanbluetext <on/off/yes/no> - clean commands after sending
    - /ignorecleanbluetext <word> - prevent auto cleaning of the command
    - /unignorecleanbluetext <word> - remove prevent auto cleaning of the command
    - /listcleanbluetext - list currently whitelisted commands

connections_help: |
    - /connect: connect a chat (Can be done in a group by /connect or /connect <chat id> in PM)
    - /connection: list connected chats
    - /disconnect: disconnect from a chat
    - /helpconnect: list available commands that can be done remotely

     *Admin only:*
    - /allowconnect <yes/no>: allow a user to connect to a chat

cust_filters_help: |
    • `/filters`*:* List all active filters saved in the chat.

     *Admin only:*
    • `/filter <keyword> <reply message>`*:* Add a filter to this chat. The bot will now reply that message whenever 'keyword'
      is mentioned. If you reply to a sticker with a keyword, the bot will reply with that sticker. NOTE: all filter
      keywords are in lowercase. If you want your keyword to be a sentence, use quotes. eg: /filter "hey there" How you
      doin?
    • `/stop <filter keyword>`*:* Stop that filter.

     *Chat creator only:*
    • `/removeallfilters`*:* Remove all chat filters at once.

      *Note*: Filters also support markdown formatters like: {first}, {last} etc.. and buttons.
        Check `/markdownhelp` to know more!

disable_help: |
    Not everyone wants every feature that the bot offers. Some commands are best
    left unused; to avoid spam and abuse.

    This allows you to disable some commonly used commands, so noone can use them.
    It'll also allow you to autodelete them, stopping people from bluetexting.

     • /cmds: Check the current status of disabled commands

     *Admin only:*
     • /enable <cmd name>: Enable that command
     • /disable <cmd name>: Disable that command
     • /listcmds: List all possible disablable commands

feds_help: |
    Everything is fun, until a spammer starts entering your group, and you have to block it. Then you need to start banning more, and more, and it hurts.
    But then you have many groups, and you don't want this spammer to be in one of your groups - how can you deal? Do you have to manually block it, in all your groups?
    *No longer!* With Federation, you can make a ban in one chat overlap with all other chats.
    You can even designate federation admins, so your trusted admin can ban all the spammers from chats you want to protect.
    
    *Click on the buttons below to learn in depth about all the commands.*

FED_OWNER_HELP: | 
    *Fed Owner Only:*
    • `/newfed <fed_name>`*:* Creates a Federation, One allowed per user
    • `/renamefed <fed_id> <new_fed_name>`*:* Renames the fed id to a new name
    • `/delfed <fed_id>`*:* Delete a Federation, and any information related to it. Will not cancel blocked users
    • `/fpromote <user>`*:* Assigns the user as a federation admin. Enables all commands for the user under `Fed Admins`
    • `/fdemote <user>`*:* Drops the User from the admin Federation to a normal User
    • `/subfed <fed_id>`*:* Subscribes to a given fed ID, bans from that subscribed fed will also happen in your fed
    • `/unsubfed <fed_id>`*:* Unsubscribes to a given fed ID
    • `/setfedlog <fed_id>`*:* Sets the group as a fed log report base for the federation
    • `/unsetfedlog <fed_id>`*:* Removed the group as a fed log report base for the federation
    • `/fbroadcast <message>`*:* Broadcasts a messages to all groups that have joined your fed
    • `/fedsubs`*:* Shows the feds your group is subscribed to `(broken rn)`

FED_ADMIN_HELP: |
    *Fed Admins:*
    • `/fban <user> <reason>`*:* Fed bans a user
    • `/unfban <user> <reason>`*:* Removes a user from a fed ban
    • `/fedinfo <fed_id>`*:* Information about the specified Federation
    • `/joinfed <fed_id>`*:* Join the current chat to the Federation. Only chat owners can do this. Every chat can only be in one Federation
    • `/leavefed <fed_id>`*:* Leave the Federation given. Only chat owners can do this
    • `/setfrules <rules>`*:* Arrange Federation rules
    • `/fedadmins`*:* Show Federation admin
    • `/fbanlist`*:* Displays all users who are victimized at the Federation at this time
    • `/fedchats`*:* Get all the chats that are connected in the Federation
    • `/chatfed `*:* See the Federation in the current chat

FED_USER_HELP: | 
    *Any user:*
    • `/fbanstat`*:* Shows if you/or the user you are replying to or their username is fbanned somewhere or not
    • `/fednotif <on/off>`*:* Federation settings not in PM when there are users who are fbaned/unfbanned
    • `/frules`*:* See Federation regulations

formt_help_bse: |
    Elaina supports a large number of formatting options to make your messages more expressive. Take a look!

md_help: |
    <b>Markdown Formatting</b>
      You can format your message using *bold*, _italics_, -underline-, and much more. Go ahead and experiment!
      <b>Supported markdown</b>:
      - <code>`code words`</code>: Backticks are used for monospace fonts. Shows as: <code>code words</code>.
      - <code>_italic words_</code>: Underscores are used for italic fonts. Shows as: <i>italic words</i>.
      - <code>*bold words*</code>: Asterisks are used for bold fonts. Shows as: <b>bold words</b>.
      - <code>~strikethrough~</code>: Tildes are used for strikethrough. Shows as: <strike>strikethrough</strike>.
      - <code>[hyperlink](example.com)</code>: This is the formatting used for hyperlinks. Shows as: <a href="https://example.com/">hyperlink</a>.
      - <code>[My Button](buttonurl://example.com)</code>: This is the formatting used for creating buttons. This example will create a button named "My button" which opens <code>example.com</code> when clicked.
      If you would like to send buttons on the same row, use the <code>:same</code> formatting.
      <b>Example:</b>
      <code>[button 1](buttonurl://example.com)</code>
      <code>[button 2](buttonurl://example.com:same)</code>
      <code>[button 3](buttonurl://example.com)</code>
      This will show button 1 and 2 on the same line, with 3 underneath.
filling_help: |
      <b>Fillings</b>
      You can also customise the contents of your message with contextual data. For example, you could mention a user by name in the welcome message, or mention them in a filter!
      You can use these to mention a user in notes too!
      <b>Supported fillings:</b>
      - <code>{first}</code>: The user's first name.
      - <code>{last}</code>: The user's last name.
      - <code>{fullname}</code>: The user's full name.
      - <code>{username}</code>: The user's username. If they don't have one, mentions the user instead.
      - <code>{mention}</code>: Mentions the user with their firstname.
      - <code>{id}</code>: The user's ID.
      - <code>{chatname}</code>: The chat's name.

fun_help: |
     • /runs: reply a random string from an array of replies.
     • /pat: pat a person, cool thing to have for cute ones :3
     • /slap: slap a user, or get slapped if not a reply.
     • /shrug : get shrug XD.
     • /table : get flip/unflip :v.
     • /decide : Randomly answers yes/no/maybe
     • /toss : Tosses A coin
     • /roll : Roll a dice.
     • /rlg : Join ears,nose,mouth and create an emo ;-;
     • /shout <keyword>: write anything you want to give loud shout.
     • /stickerid: reply to a sticker to get its ID.
     • /getsticker: reply to a sticker to get the raw PNG image.
     • /steal: reply to a sticker or image to add it to your pack.

antispam_help: |
     *Admins only:*
      • `/antispam <on/off/yes/no>`*:* Will toggle our antispam tech or return your current settings.

     Anti-Spam, used by bot devs to ban spammers across all groups. This helps protect
     you and your groups by removing spam flooders as quickly as possible.
     *Note:* Users can appeal gbans or report spammers at @YorkTownEagleUnion

     Elaina also integrates @Spamwatch and @Intellivoid's SpamProtectionBot API to remove Spammers as much as possible from your chatroom!
     *What is SpamWatch?*
     SpamWatch maintains a large constantly updated ban-list of spambots, trolls, bitcoin spammers and unsavoury characters.
     Constantly help banning spammers off from your group automatically So, you wont have to worry about spammers storming your group.
     *Note:* Users can appeal spamwatch bans at @SpamwatchSupport

     *What is Spam protection?*
     SpamProtection is the new AI antispam service which makes sure that your chat is free of spambots, scammers, and pedophiles.
     Uses @Intellivoid's Coffeehouse Artificial Engine. Every ban is checked by real trusty people before being finalized.

gtranslate_help: |
     • `/tr` or `/tl` (language code) as reply to a long message
      *Example:*
       `/tr en`*:* translates something to english
       `/tr hi//en`*:* translates hindi to english
     • `/langs`: get a list of supported languages for translation.
locks_help: |
     Do stickers annoy you? or want to avoid people sharing links? or pictures?
     You're in the right place!
     The locks module allows you to lock away some common items in the
     telegram world; the bot will automatically delete them!

      • `/locktypes`*:* Lists all possible locktypes

     *Admins only:*
      • `/lock <type>`*:* Lock items of a certain type (not available in private)
      • `/unlock <type>`*:* Unlock items of a certain type (not available in private)
      • `/locks`*:* The current list of locks in this chat.

     Locks can be used to restrict a group's users.
     eg:
     Locking urls will auto-delete all messages with urls, locking stickers will restrict all
     non-admin users from sending stickers, etc.
     Locking bots will stop non-admins from adding bots to the chat.

     *Note:*
      • Unlocking permission *info* will allow members (non-admins) to change the group information, such as the description or the group name
      • Unlocking permission *pin* will allow members (non-admins) to pinned a message in a group

log_help: |
      *Admins only:*
      • `/logchannel`*:* get log channel info
      • `/setlog`*:* set the log channel.
      • `/unsetlog`*:* unset the log channel.

      Setting the log channel is done by:
      • adding the bot to the desired channel (as an admin!)
      • sending `/setlog` in the channel
      • forwarding the `/setlog` to the group

markdown_help_text: |
      Markdown is a very powerful formatting tool supported by telegram. Kigyo has some enhancements, to make sure that
      saved messages are correctly parsed, and to allow you to create buttons.

      - <code>_italic_</code>: wrapping text with '_' will produce italic text
      - <code>*bold*</code>: wrapping text with '*' will produce bold text
      - <code>`code`</code>: wrapping text with '`' will produce monospaced text, also known as 'code'
      - <code>[sometext](someURL)</code>: this will create a link - the message will just show <code>sometext</code>,
      and tapping on it will open the page at <code>someURL</code>.
      EG: <code>[test](example.com)</code>

      - <code>[buttontext](buttonurl:someURL)</code>: this is a special enhancement to allow users to have telegram
      buttons in their markdown. <code>buttontext</code> will be what is displayed on the button, and <code>someurl</code>
      will be the url which is opened.
      EG: <code>[This is a button](buttonurl:example.com)</code>

      If you want multiple buttons on the same line, use :same, as such:
      <code>[one](buttonurl://example.com)
      [two](buttonurl://google.com:same)</code>
      This will create two buttons on a single line, instead of one button per line.

      Keep in mind that your message <b>MUST</b> contain some text other than just a button!

misc_help: |
      • /id: get the current group id. If used by replying to a message, gets that user's id.
      • /gifid: reply to a gif to me to tell you its file ID.
      • /info: get information about a user.
      • /markdownhelp: quick summary of how markdown works in telegram - can only be called in private chats.
      • /ud <word>: Type the word or expression you want to search use.
      • /urban <word>: Same as /ud
      • /paste - Do a paste at `nekobin.com`
      • /react: Reacts with a random reaction
      • /weebify <text>: returns a weebified text
      • /tr (language code) as reply to a long message.
      • /time <query> : Gives information about a timezone.
      • /cash : currency converter
        example syntax: /cash 1 USD INR
      • /getid : get IDs of chat, user and chat message.
      • /spbinfo : get info about a user from @Intellivoid's SpamProtection API
      ───────────────────────────────
      *Last.FM*
      Share what you're what listening to with the help of this module!
      *Available commands:*
      • /setuser <username>: sets your last.fm username.
      • /clearuser: removes your last.fm username from the bot's database.
      • /lastfm: returns what you're scrobbling on last.fm.

muting_help: |
      *Admins only:*
       • `/mute <userhandle>`*:* silences a user. Can also be used as a reply, muting the replied to user.
       • `/tmute <userhandle> x(m/h/d)`*:* mutes a user for x time. (via handle, or reply). `m` = `minutes`, `h` = `hours`, `d` = `days`.
       • `/unmute <userhandle>`*:* unmutes a user. Can also be used as a reply, muting the replied to user.

notes_help: |
       • `/get <notename>`*:* get the note with this notename
       • `#<notename>`*:* same as /get
       • `/notes` or `/saved`*:* list all saved notes in this chat
       • `/number` *:* Will pull the note of that number in the list.
        If you would like to retrieve the contents of a note without any formatting, use `/get <notename> noformat`. This can
        be useful when updating a current note.

        *Admins only:*
       • `/save <notename> <notedata>`*:* saves notedata as a note with name notename
        A button can be added to a note by using standard markdown link syntax - the link should just be prepended with a
         `buttonurl:` section, as such: `[somelink](buttonurl:example.com)`. Check `/markdownhelp` for more info.
       • `/save <notename>`*:* save the replied message as a note with name notename
       • `/clear <notename>`*:* clear note with this name
       • `/removeallnotes`*:* removes all notes from the group
       *Note:* Note names are case-insensitive, and they are automatically converted to lowercase before getting saved.

purge_help: |
       *Admin only:*
        • /del: deletes the message you replied to
        • /purge: deletes all messages between this and the replied to message.
        • /purge <integer X>: deletes the replied message, and X messages following it if replied to a message.

reports_help: |
        • `/report <reason>`*:* reply to a message to report it to admins.
        • `@admin`*:* reply to a message to report it to admins.
         *NOTE:* Neither of these will get triggered if used by admins.

         *Admins only:*
          • `/reports <on/off>`*:* change report setting, or view current status.
          • If done in pm, toggles your status.
          • If in group, toggles that groups's status.

rules_help: |
      • `/rules`*:* get the rules for this chat.
       *Admins only:*
      • `/setrules <your rules here>`*:* set the rules for this chat.
      • `/clearrules`*:* clear the rules for this chat.

userinfo_help: |
      - /setbio <text>: while replying, will save another user's bio
      - /bio: will get your or another user's bio. This cannot be set by yourself.
      - /setme <text>: will set your info
      - /me: will get your or another user's info

warns_help: |
      • `/warns <userhandle>`*:* get a user's number, and reason, of warns.
      • `/warnlist`*:* list of all current warning filters

      *Admins only:*
      • `/warn <userhandle>`*:* warn a user. After 3 warns, the user will be banned from the group. Can also be used as a reply.
      • `/resetwarn <userhandle>`*:* reset the warns for a user. Can also be used as a reply.
      • `/addwarn <keyword> <reply message>`*:* set a warning filter on a certain keyword. If you want your keyword to
      be a sentence, encompass it with quotes, as such: `/addwarn "very angry" This is an angry user`.
      • `/nowarn <keyword>`*:* stop a warning filter
      • `/warnlimit <num>`*:* set the warning limit
      • `/strongwarn <on/yes/off/no>`*:* If set to on, exceeding the warn limit will result in a ban. Else, will just kick.

greetings_help: |
      *Admins only:*
       • `/welcome <on/off>`*:* enable/disable welcome messages.
       • `/welcome`*:* shows current welcome settings.
       • `/welcome noformat`*:* shows current welcome settings, without the formatting - useful to recycle your welcome messages!
       • `/goodbye`*:* same usage and args as `/welcome`.
       • `/setwelcome <sometext>`*:* set a custom welcome message. If used replying to media, uses that media.
       • `/setgoodbye <sometext>`*:* set a custom goodbye message. If used replying to media, uses that media.
       • `/resetwelcome`*:* reset to the default welcome message.
       • `/resetgoodbye`*:* reset to the default goodbye message.
       • `/cleanwelcome <on/off>`*:* On new member, try to delete the previous welcome message to avoid spamming the chat.
       • `/welcomemutehelp`*:* gives information about welcome mutes.
       • `/cleanservice <on/off`*:* deletes telegrams welcome/left service messages.
       *Example:*
      user joined chat, user left chat.

      *Welcome markdown:*
       • `/welcomehelp`*:* view more formatting information for custom welcome/goodbye messages.

nlp_help: |

      *Chatroom Spam Prediction*
       This feature uses @Intellivoid's Coffeehouse AI to
       process chat messages and detect spam.
       This comes under Coffehouse' NLP. Learn more about
       it [here](https://docs.intellivoid.net/coffeehouse/v1/nlp/spam_prediction/chatroom)
       *Command:*
        • `/nlpstat <on/off/yes/no>`*:* toggle NLP in your chat.
