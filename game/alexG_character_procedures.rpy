
    # Gala Alex Character Procedures File

    # Paste this file into a story if you want to use Notte.  These procedures animate Notte as a speaker.
    # You'll also need to paste THIS line into your actual script above the script label whenever you're using Notte:

define gale = Character("Alex", callback=speaker("gale"))

    # This program assumes that the following folders exist:
    #     -"images/alex_gala"
    #     -"images/alex_gala/faces"
    #     -"images/alex_gala/mouths"


    # Gala Alex dynamically blinks and, while speaking, also moves her mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Gala Alex appear*:
    #  -->  show alex_gala with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Gala Alex's eyes*:
    #  -->  show alex_gala [keyword]
    #  List of eye keywords:
    #     -->  relaxed (default), angry, askance, blush, blush2, closed_blush, focused, sad,
    #          shock, squint, surprised, closed_sad,

    # *Changing Gala Alex's mouth*:
    #  -->  show alex_gala [keyword]
    #  List of mouth keywords:
    #     -->  mutter1 (default), closed_mutter1, frown1, frown2, frown3, frown4, grimace1,
    #          pout1, shout1, smile1, smile2, duchenne1

    # *Writing dialogue for Gala Alex*:
    #  --> ale "[Notte's line here]"

    # *Making Gala Alex disappear*:
    #  --> hide alex_gala with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage alex_gala:

    always "images/alex_gala/alex_gala_body.png"

    group face:

        # 493/1024, 254/1024:
        pos (0.48145, 0.24805)

        attribute relaxed default:
            "alex_gala_relaxed_eyes"

        attribute focused:
            "alex_gala_focused_eyes"

        attribute closed_focused:
            "images/alex_gala/faces/100005_02_parts_c003.png"

        attribute sad:
            "alex_gala_sad_eyes"

        attribute closed_sad:
            "images/alex_gala/faces/100005_02_parts_c009.png"

        attribute angry:
            "alex_gala_angry_eyes"

        attribute surprised:
            "alex_gala_surprised_eyes"

        attribute blush:
            "alex_gala_blush_eyes"

        attribute closed_blush:
            "images/alex_gala/faces/100005_02_parts_c015.png"

        attribute squint:
            "alex_gala_squint_eyes"

        attribute shock:
            "alex_gala_shock_eyes"

        attribute blush2:
            "alex_gala_blush2_eyes"

        attribute closed_blush:
            "images/alex_gala/faces/100005_02_parts_c015.png"

        attribute closed_blush2:
            "images/alex_gala/faces/100005_02_parts_c036.png"

        attribute askance:
            "alex_gala_askance_eyes"


    group mouth:

        pos (0.48145, 0.24805)

        attribute mutter1 default:
            "alex_gala_mutter1"

        attribute closed_mutter1:
            "images/alex_gala/mouths/100005_02_parts_c004.png"

        attribute frown1:
            "alex_gala_frown1"

        attribute smile1:
            "alex_gala_smile1"

        attribute smile2:
            "alex_gala_smile2"

        attribute duchenne1:
            "alex_gala_duchenne1"

        attribute grimace1:
            "alex_gala_grimace1"

        attribute frown2:
            "alex_gala_frown2"

        attribute frown3:
            "alex_gala_frown3"

        attribute pout1:
            "alex_gala_pout1"

        attribute shout1:
            "alex_gala_shout1"

        attribute frown4:
            "alex_gala_frown4"


## EYE animations start here.

image alex_gala_relaxed_eyes:
    "images/alex_gala/faces/100005_02_parts_c000.png"
    choice:
        2
    choice:
        3
    choice:
        4
    choice:
        5
    choice:
        6
    "images/alex_gala/faces/100005_02_parts_c001.png"
    0.05
    repeat

image alex_gala_focused_eyes:
    "images/alex_gala/faces/100005_02_parts_c002.png"
    choice:
        2
    choice:
        3
    choice:
        4
    choice:
        5
    choice:
        6
    "images/alex_gala/faces/100005_02_parts_c003.png"
    0.05
    repeat

image alex_gala_sad_eyes:
    "images/alex_gala/faces/100005_02_parts_c008.png"
    choice:
        2
    choice:
        3
    choice:
        4
    choice:
        5
    choice:
        6
    "images/alex_gala/faces/100005_02_parts_c009.png"
    0.05
    repeat

image alex_gala_angry_eyes:
    "images/alex_gala/faces/100005_02_parts_c010.png"
    choice:
        2
    choice:
        3
    choice:
        4
    choice:
        5
    choice:
        6
    "images/alex_gala/faces/100005_02_parts_c011.png"
    0.05
    repeat

image alex_gala_surprised_eyes:
    "images/alex_gala/faces/100005_02_parts_c012.png"
    choice:
        2
    choice:
        3
    choice:
        4
    choice:
        5
    choice:
        6
    "images/alex_gala/faces/100005_02_parts_c013.png"
    0.05
    repeat

image alex_gala_blush_eyes:
    "images/alex_gala/faces/100005_02_parts_c014.png"
    choice:
        2
    choice:
        3
    choice:
        4
    choice:
        5
    choice:
        6
    "images/alex_gala/faces/100005_02_parts_c015.png"
    0.05
    repeat

image alex_gala_squint_eyes:
    "images/alex_gala/faces/100005_02_parts_c024.png"
    choice:
        2
    choice:
        3
    choice:
        4
    choice:
        5
    choice:
        6
    "images/alex_gala/faces/100005_02_parts_c025.png"
    0.05
    repeat

image alex_gala_shock_eyes:
    "images/alex_gala/faces/100005_02_parts_c026.png"
    choice:
        2
    choice:
        3
    choice:
        4
    choice:
        5
    choice:
        6
    "images/alex_gala/faces/100005_02_parts_c027.png"
    0.05
    repeat

image alex_gala_blush2_eyes:
    "images/alex_gala/faces/100005_02_parts_c035.png"
    choice:
        2
    choice:
        3
    choice:
        4
    choice:
        5
    choice:
        6
    "images/alex_gala/faces/100005_02_parts_c036.png"
    0.05
    repeat

image alex_gala_askance_eyes:
    "images/alex_gala/faces/100005_02_parts_c037.png"
    choice:
        2
    choice:
        3
    choice:
        4
    choice:
        5
    choice:
        6
    "images/alex_gala/faces/100005_02_parts_c038.png"
    0.05
    repeat




# MOUTH animations start here.

image alex_gala_mutter1_nottalking = "images/alex_gala/mouths/100005_02_parts_c004.png"

image alex_gala_mutter1_talking:
    "images/alex_gala/mouths/100005_02_parts_c005.png"
    0.15
    "images/alex_gala/mouths/100005_02_parts_c004.png"
    0.15
    repeat

image alex_gala_mutter1 = WhileSpeaking("gale", "alex_gala_mutter1_talking", "alex_gala_mutter1_nottalking")


image alex_gala_frown1_nottalking = "images/alex_gala/mouths/100005_02_parts_c006.png"

image alex_gala_frown1_talking:
    "images/alex_gala/mouths/100005_02_parts_c007.png"
    0.15
    "images/alex_gala/mouths/100005_02_parts_c006.png"
    0.15
    repeat

image alex_gala_frown1 = WhileSpeaking("gale", "alex_gala_frown1_talking", "alex_gala_frown1_nottalking")


image alex_gala_smile1_nottalking = "images/alex_gala/mouths/100005_02_parts_c039.png"

image alex_gala_smile1_talking:
    "images/alex_gala/mouths/100005_02_parts_c040.png"
    0.15
    "images/alex_gala/mouths/100005_02_parts_c039.png"
    0.15
    repeat

image alex_gala_smile1 = WhileSpeaking("gale", "alex_gala_smile1_talking", "alex_gala_smile1_nottalking")


image alex_gala_smile2_nottalking = "images/alex_gala/mouths/100005_02_parts_c016.png"

image alex_gala_smile2_talking:
    "images/alex_gala/mouths/100005_02_parts_c017.png"
    0.15
    "images/alex_gala/mouths/100005_02_parts_c016.png"
    0.15
    repeat

image alex_gala_smile2 = WhileSpeaking("gale", "alex_gala_smile2_talking", "alex_gala_smile2_nottalking")


image alex_gala_duchenne1_nottalking = "images/alex_gala/mouths/100005_02_parts_c040.png"

image alex_gala_duchenne1_talking:
    "images/alex_gala/mouths/100005_02_parts_c039.png"
    0.15
    "images/alex_gala/mouths/100005_02_parts_c040.png"
    0.15
    repeat

image alex_gala_duchenne1 = WhileSpeaking("gale", "alex_gala_duchenne1_talking", "alex_gala_duchenne1_nottalking")


image alex_gala_grimace1_nottalking = "images/alex_gala/mouths/100005_02_parts_c018.png"

image alex_gala_grimace1_talking:
    "images/alex_gala/mouths/100005_02_parts_c019.png"
    0.15
    "images/alex_gala/mouths/100005_02_parts_c018.png"
    0.15
    repeat

image alex_gala_grimace1 = WhileSpeaking("gale", "alex_gala_grimace1_talking", "alex_gala_grimace1_nottalking")


image alex_gala_frown2_nottalking = "images/alex_gala/mouths/100005_02_parts_c020.png"

image alex_gala_frown2_talking:
    "images/alex_gala/mouths/100005_02_parts_c021.png"
    0.15
    "images/alex_gala/mouths/100005_02_parts_c020.png"
    0.15
    repeat

image alex_gala_frown2 = WhileSpeaking("gale", "alex_gala_frown2_talking", "alex_gala_frown2_nottalking")


image alex_gala_frown3_nottalking = "images/alex_gala/mouths/100005_02_parts_c022.png"

image alex_gala_frown3_talking:
    "images/alex_gala/mouths/100005_02_parts_c023.png"
    0.15
    "images/alex_gala/mouths/100005_02_parts_c022.png"
    0.15
    repeat

image alex_gala_frown3 = WhileSpeaking("gale", "alex_gala_frown3_talking", "alex_gala_frown3_nottalking")


image alex_gala_pout1_nottalking = "images/alex_gala/mouths/100005_02_parts_c029.png"

image alex_gala_pout1_talking:
    "images/alex_gala/mouths/100005_02_parts_c030.png"
    0.15
    "images/alex_gala/mouths/100005_02_parts_c029.png"
    0.15
    repeat

image alex_gala_pout1 = WhileSpeaking("gale", "alex_gala_pout1_talking", "alex_gala_pout1_nottalking")


# 035/036 are the same as 004/005


image alex_gala_shout1_nottalking = "images/alex_gala/mouths/100005_02_parts_c031.png"

image alex_gala_shout1_talking:
    "images/alex_gala/mouths/100005_02_parts_c032.png"
    0.15
    "images/alex_gala/mouths/100005_02_parts_c031.png"
    0.15
    repeat

image alex_gala_shout1 = WhileSpeaking("gale", "alex_gala_shout1_talking", "alex_gala_shout1_nottalking")


image alex_gala_frown4_nottalking = "images/alex_gala/mouths/100005_02_parts_c041.png"

image alex_gala_frown4_talking:
    "images/alex_gala/mouths/100005_02_parts_c042.png"
    0.15
    "images/alex_gala/mouths/100005_02_parts_c041.png"
    0.15
    repeat

image alex_gala_frown4 = WhileSpeaking("gale", "alex_gala_frown4_talking", "alex_gala_frown4_nottalking")








# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

transform alex_gala_back_pos:
    #118, 180 ->> 118/1028 ?

    # no, try (118 + (770/2))/1028
    xalign 0.48930
    yalign 1.0

transform alex_gala_back_ambush_pos:
    xalign 0.0
    yalign 1.0

transform alex_gala_back_ambush_to_regular:
    xalign 0.0
    yalign 1.0
    linear 1.0 xalign 0.48930 yalign 1.0








# The game starts here.

label alexG_character_procedures:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image sky = "images/backgrounds/Sty_bg_0015_100_00.png"
    scene sky at middle
    image village = "images/backgrounds/Sty_bg_0016_104_03_front.png"
    show village at middle


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show alex_gala with dissolve
    gale "It's certainly peculiar being here."
    gale "There's still a lot about others I have yet to learn."

    show alex_gala surprised frown2
    gale "Oh, Elisanne! I’m surprised to see you at this hour!\n('surprised' face and 'frown2' mouth)"

    show alex_gala sad smile1
    gale "Oh, me? I’m doing well. The orphanage matron asked me to watch over the children this holiday.\n('sad' face and 'smile1' mouth)"

    show alex_gala askance frown3
    gale "I just assumed that you would be helping His Majesty at the moment.\n('askance' face and 'frown3' mouth)"

    show alex_gala relaxed frown1
    gale "But while you’re here, you wouldn’t mind assisting me, would you?\n('relaxed' face and 'frown1' mouth)"

    show alex_gala squint pout1
    gale "I’m not too familiar with events like this and could use all the help I can.\n('squint' face and 'pout1' mouth)"

    show alex_gala sad smile2
    gale "You will? Thank you, Elisanne! I can’t express how much it means to have you by my side today!\n('smile2' mouth)"
    gale "I believe I see someone over there right now! I believe he’s the festival mascot."

    show alex_gala shock shout1
    gale "Wait, what are the children doing to them!\n('shock' face and 'shout1' mouth)"

    show alex_gala angry grimace1
    gale "Hey! No attacking the jackrabbit! Everyone, wait your turn to play with them!\n('angry' face and 'grimace1' mouth)"

    show alex_gala focused mutter1
    gale "See? Now that’s safer.\n('focused' face and 'mutter1' mouth)"

    show alex_gala sad frown3
    gale "Oh, Elisanne? You want to play with the rabbit man?"

    show alex_gala smile2
    gale "You know, I actually remember dressing up as one some time ago!"

    show alex_gala askance frown4
    gale "Though that was back when you and I were still enemies and…\n('frown4' mouth)"

    show alex_gala sad duchenne1
    gale "At least we can be together again, fighting together.\n('duchenne1' mouth)"

    show alex_gala surprised frown1
    gale "Oh, one of the children is here!"

    show alex_gala sad smile2
    gale "What did you need help with?"

    show alex_gala blush pout1
    gale "…!\nHuh?! No, Ms. Elisanne and I are simply together to help out!\n('blush' face)"

    show alex_gala closed_blush
    gale "…\n('closed_blush' face)"

    show alex_gala blush2 closed_mutter1
    gale "…?\n('blush2' face and 'closed_mutter1' mouth)"

    show alex_gala closed_blush2 duchenne1
    gale "Heh, you know how children can be…\n('closed_blush2' face)"

    show alex_gala blush2
    gale "Come on now! We don't want them getting to crazy again!"


    hide alex_gala with dissolve

    # This goes back to script

    jump testfiles
