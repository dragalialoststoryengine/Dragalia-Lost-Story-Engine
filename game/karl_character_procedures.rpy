    # Karl Character Procedures File

    # Paste this file into a story if you want to use Karl.  These procedures animate Karl as a speaker.

define kar = Character("Karl", callback=speaker("kar"))

    # This program assumes that the following folders exist:
    #     -"images/karl"
    #     -"images/karl/faces"
    #     -"images/karl/mouths"

    # Karl dynamically blinks and, while speaking, also moves his mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Karl appear*:
    #  -->  show karl with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Karl's eyes*:
    #  -->  show karl [keyword]
    #  List of eye keywords:
    #     -->  focused (default), closed_focused, angry, blush, cry,
    #          gloom, neutral, shocked, squint, surprised

    # *Changing Karl's mouth*:
    #  -->  show karl [keyword]
    #  List of mouth keywords:
    #     -->  smile1 (default), smile2, smile3, frown1, frown2,
    #          grimace1, grin1, mutter1, shout1

    # *Writing dialogue for Karl*:
    #  --> kar "[Karl's line here]"

    # *Making Karl disappear*:
    #  --> hide karl with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage karl:

    always "images/karl/karl_body.png"

    group face:

        # 448/1024, 234/1024:
        pos (0.4375, 0.2285156)

        attribute focused default:
            "karl_focused_eyes"

        attribute closed_focused:
            "images/karl/faces/110008_01_parts_c001.png"

        attribute neutral:
            "karl_neutral_eyes"

        attribute glint:
            "karl_glint_eyes"

        attribute angry:
            "karl_angry_eyes"

        attribute surprised:
            "karl_surprised_eyes"

        attribute blush:
            "karl_blush_eyes"

        attribute gloom:
            "karl_gloom_eyes"

        attribute cry:
            "karl_cry_eyes"

        attribute squint:
            "karl_squint_eyes"

        attribute shocked:
            "karl_shocked_eyes"


    group mouth:

        pos (0.4375, 0.2285156)

        attribute smile1 default:
            "karl_smile1"

        attribute frown1:
            "karl_frown1"

        attribute grin1:
            "karl_grin1"

        attribute grimace1:
            "karl_grimace1"

        attribute shout1:
            "karl_shout1"

        attribute mutter1:
            "karl_mutter1"

        attribute smile2:
            "karl_smile2"

        attribute smile3:
            "karl_smile3"

        attribute frown2:
            "karl_frown2"



## EYE animations start here.

image karl_focused_eyes:
    "images/karl/faces/110008_01_parts_c000.png"
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
    "images/karl/faces/110008_01_parts_c001.png"
    0.05
    repeat

# 002 and 003 are the same as 001.  Deleted.

# 004 and 005 are the same as 000 / 001.  Deleted.

image karl_neutral_eyes:
    "images/karl/faces/110008_01_parts_c006.png"
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
    "images/karl/faces/110008_01_parts_c007.png"
    0.05
    repeat

image karl_glint_eyes:
    "images/karl/faces/110008_01_parts_c016.png"
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
    "images/karl/faces/110008_01_parts_c017.png"
    0.05
    repeat

image karl_angry_eyes:
    "images/karl/faces/110008_01_parts_c018.png"
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
    "images/karl/faces/110008_01_parts_c019.png"
    0.05
    repeat

image karl_surprised_eyes:
    "images/karl/faces/110008_01_parts_c020.png"
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
    "images/karl/faces/110008_01_parts_c021.png"
    0.05
    repeat

image karl_blush_eyes:
    "images/karl/faces/110008_01_parts_c022.png"
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
    "images/karl/faces/110008_01_parts_c023.png"
    0.05
    repeat

image karl_gloom_eyes:
    "images/karl/faces/110008_01_parts_c032.png"
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
    "images/karl/faces/110008_01_parts_c033.png"
    0.05
    repeat

image karl_cry_eyes:
    "images/karl/faces/110008_01_parts_c034.png"
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
    "images/karl/faces/110008_01_parts_c035.png"
    0.05
    repeat

image karl_squint_eyes:
    "images/karl/faces/110008_01_parts_c036.png"
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
    "images/karl/faces/110008_01_parts_c038.png"
    0.05
    repeat

# 037 is the same as 000.  Deleted.

image karl_shocked_eyes:
    "images/karl/faces/110008_01_parts_c047.png"
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
    "images/karl/faces/110008_01_parts_c048.png"
    0.05
    repeat




# MOUTH animations start here.

image karl_smile1_nottalking = "images/karl/mouths/110008_01_parts_c008.png"

image karl_smile1_talking:
    "images/karl/mouths/110008_01_parts_c009.png"
    0.15
    "images/karl/mouths/110008_01_parts_c008.png"
    0.15
    repeat

image karl_smile1 = WhileSpeaking("kar", "karl_smile1_talking", "karl_smile1_nottalking")


# 010 / 011 is the same as 008 / 009.  Deleted.


# 012 / 013 is the same as 008 / 009.  Deleted.


image karl_frown1_nottalking = "images/karl/mouths/110008_01_parts_c014.png"

image karl_frown1_talking:
    "images/karl/mouths/110008_01_parts_c015.png"
    0.15
    "images/karl/mouths/110008_01_parts_c014.png"
    0.15
    repeat

image karl_frown1 = WhileSpeaking("kar", "karl_frown1_talking", "karl_frown1_nottalking")


image karl_grin1_nottalking = "images/karl/mouths/110008_01_parts_c024.png"

image karl_grin1_talking:
    "images/karl/mouths/110008_01_parts_c025.png"
    0.15
    "images/karl/mouths/110008_01_parts_c024.png"
    0.15
    repeat

image karl_grin1 = WhileSpeaking("kar", "karl_grin1_talking", "karl_grin1_nottalking")


image karl_grimace1_nottalking = "images/karl/mouths/110008_01_parts_c026.png"

image karl_grimace1_talking:
    "images/karl/mouths/110008_01_parts_c027.png"
    0.15
    "images/karl/mouths/110008_01_parts_c026.png"
    0.15
    repeat

image karl_grimace1 = WhileSpeaking("kar", "karl_grimace1_talking", "karl_grimace1_nottalking")


image karl_shout1_nottalking = "images/karl/mouths/110008_01_parts_c028.png"

image karl_shout1_talking:
    "images/karl/mouths/110008_01_parts_c029.png"
    0.15
    "images/karl/mouths/110008_01_parts_c028.png"
    0.15
    repeat

image karl_shout1 = WhileSpeaking("kar", "karl_shout1_talking", "karl_shout1_nottalking")


# 030 / 031 are TECHNICALLY different from 014 / 015 but it's just one pixel lower with the same shape, so it's not worth keeping.  Deleted.


image karl_mutter1_nottalking = "images/karl/mouths/110008_01_parts_c039.png"

image karl_mutter1_talking:
    "images/karl/mouths/110008_01_parts_c040.png"
    0.15
    "images/karl/mouths/110008_01_parts_c039.png"
    0.15
    repeat

image karl_mutter1 = WhileSpeaking("kar", "karl_mutter1_talking", "karl_mutter1_nottalking")


# 041 / 042 are the same as 026 / 027.  Deleted.


image karl_smile2_nottalking = "images/karl/mouths/110008_01_parts_c043.png"

image karl_smile2_talking:
    "images/karl/mouths/110008_01_parts_c044.png"
    0.15
    "images/karl/mouths/110008_01_parts_c043.png"
    0.15
    repeat

image karl_smile2 = WhileSpeaking("kar", "karl_smile2_talking", "karl_smile2_nottalking")


image karl_smile3_nottalking = "images/karl/mouths/110008_01_parts_c045.png"

image karl_smile3_talking:
    "images/karl/mouths/110008_01_parts_c046.png"
    0.15
    "images/karl/mouths/110008_01_parts_c045.png"
    0.15
    repeat

image karl_smile3 = WhileSpeaking("kar", "karl_smile3_talking", "karl_smile3_nottalking")


image karl_frown2_nottalking = "images/karl/mouths/110008_01_parts_c049.png"

image karl_frown2_talking:
    "images/karl/mouths/110008_01_parts_c050.png"
    0.15
    "images/karl/mouths/110008_01_parts_c049.png"
    0.15
    repeat

image karl_frown2 = WhileSpeaking("kar", "karl_frown2_talking", "karl_frown2_nottalking")






# The test file script starts here.

label karl_character_procedures:

    image drawbridge_night = "images/backgrounds/Sty_bg_0017_300_00.png"
    scene drawbridge_night with fade

    show karl with dissolve
    kar "Aha!  Well met and good greetings!  It's good to have the newest recruit for the JUSTICE PATROL!!"

    show karl focused smile1
    kar "(focused smile1) Now, I'm going to run through the rules of being an emblem of justice!"

    show karl closed_focused smile2
    kar "(closed_focused smile2) The first rule of epitomizing justice is to practice your FACE OF JUSTICE!"

    show karl angry smile3
    kar "(angry smile3) You know, a striking face that will bolster the courage of allies of justice, and strike terror into the hearts of villains?"

    show karl blush frown1
    kar "(blush frown1) ...What kind of face IS that?  Uh... well... it's hard to put into words..."

    show karl cry frown2
    kar "(cry frown2) Like... justice is expressed in the noble tears that the purehearted shed when they weep against the injustices in the world."

    show karl glint grin1
    kar "(glint grin1) Justice is the glint in the eyes of those who would seek to protect the weak and punish evildoers!"

    show karl surprised shout1
    kar "(surprised shout1) Justice is full of surprises, constantly reinventing itself like a shining supernova!!"

    show karl neutral mutter1
    kar "(neutral mutter1) Justice is as tranquil as a forest, moving softly like an owl in the dead of night."

    show karl shocked grimace1
    kar "(shocked grimace1) ...What?  That's not an explanation at all for how to compose a \"face of justice?\""

    show karl gloom smile3
    kar "(gloom smile3) ...Maybe I'm not skilled enough in carrying out the justice of education...  The Karlsplosion... is fading..."

    hide karl with dissolve


    # This goes back to script

    jump testfiles
