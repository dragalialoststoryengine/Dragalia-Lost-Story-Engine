
    # Dragonyule Ilia Character Procedures File

    # Paste this file into a story if you want to use Dragonyule Ilia.  These procedures animate Dragonyule Ilia as a speaker.
    # You'll also need to paste THIS line into your actual script above the script label whenever you're using Ilia:

define dyili = Character("Ilia", callback=speaker("dyili"))

    # This program assumes that the following folders exist:
    #     -"images/ilia_dragonyule"
    #     -"images/ilia_dragonyule/faces"
    #     -"images/ilia_dragonyule/mouths"

    # Dragonyule Ilia dynamically blinks and, while speaking, also moves her mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Dragonyule Ilia appear*:
    #  -->  show dyilia with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Dragonyule Ilia's eyes*:
    #  -->  show dyilia [keyword]
    #  List of eye keywords:
    #     -->  relaxed (default), relaxed2, relaxed3, askance, blush, cry, flinch,
    #          focused, focused2, sad, smirk, surprised

    # *Changing Dragonyule Ilia's mouth*:
    #  -->  show dyilia [keyword]
    #  List of mouth keywords:
    #     -->  smile1 (default), smile2, smile3, frown1, frown2, frown3, frown4,
    #          frown5, frown6, grimace1, grimace2, grin1, grin2

    # *Writing dialogue for Dragonyule Ilia*:
    #  --> dyili "[Ilia's line here]"

    # *Making Dragonyule Ilia disappear*:
    #  --> hide dyilia with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage dyilia:

    always "images/ilia_dragonyule/ilia_dragonyule_body.png"

    group face:

        # 454/1028, 249/1028:
        pos (0.44163, 0.24222)

        attribute relaxed default:
            "dyilia_relaxed_eyes"

        attribute focused:
            "dyilia_focused_eyes"

        attribute relaxed2:
            "dyilia_relaxed2_eyes"

        attribute flinch:
            "dyilia_flinch_eyes"

        attribute surprised:
            "dyilia_surprised_eyes"

        attribute blush:
            "dyilia_blush_eyes"

        attribute sad:
            "dyilia_sad_eyes"

        attribute focused2:
            "dyilia_focused2_eyes"

        attribute relaxed3:
            "dyilia_relaxed3_eyes"

        attribute askance:
            "dyilia_askance_eyes"

        attribute smirk:
            "dyilia_smirk_eyes"

        attribute cry:
            "dyilia_cry_eyes"

    group mouth:

        pos (0.44163, 0.24222)

        attribute smile1 default:
            "dyilia_smile1"

        attribute frown1:
            "dyilia_frown1"

        attribute smile2:
            "dyilia_smile2"

        attribute frown2:
            "dyilia_frown2"

        attribute grimace1:
            "dyilia_grimace1"

        attribute grin1:
            "dyilia_grin1"

        attribute frown3:
            "dyilia_frown3"

        attribute grimace2:
            "dyilia_grimace2"

        attribute frown4:
            "dyilia_frown4"

        attribute smile3:
            "dyilia_smile3"

        attribute frown5:
            "dyilia_frown5"

        attribute grin2:
            "dyilia_grin2"

        attribute frown6:
            "dyilia_frown6"

## EYE animations start here.

image dyilia_relaxed_eyes:
    "images/ilia_dragonyule/faces/110367_04_parts_c000.png"
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
    "images/ilia_dragonyule/faces/110367_04_parts_c001.png"
    0.05
    repeat

image dyilia_focused_eyes:
    "images/ilia_dragonyule/faces/110367_04_parts_c003.png"
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
    "images/ilia_dragonyule/faces/110367_04_parts_c004.png"
    0.05
    repeat

image dyilia_relaxed2_eyes:
    "images/ilia_dragonyule/faces/110367_04_parts_c009.png"
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
    "images/ilia_dragonyule/faces/110367_04_parts_c010.png"
    0.05
    repeat

image dyilia_flinch_eyes:
    "images/ilia_dragonyule/faces/110367_04_parts_c011.png"
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
    "images/ilia_dragonyule/faces/110367_04_parts_c012.png"
    0.05
    repeat

image dyilia_surprised_eyes:
    "images/ilia_dragonyule/faces/110367_04_parts_c013.png"
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
    "images/ilia_dragonyule/faces/110367_04_parts_c014.png"
    0.05
    repeat

image dyilia_blush_eyes:
    "images/ilia_dragonyule/faces/110367_04_parts_c015.png"
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
    "images/ilia_dragonyule/faces/110367_04_parts_c016.png"
    0.05
    repeat

image dyilia_sad_eyes:
    "images/ilia_dragonyule/faces/110367_04_parts_c025.png"
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
    "images/ilia_dragonyule/faces/110367_04_parts_c026.png"
    0.05
    repeat

image dyilia_focused2_eyes:
    "images/ilia_dragonyule/faces/110367_04_parts_c027.png"
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
    "images/ilia_dragonyule/faces/110367_04_parts_c028.png"
    0.05
    repeat

image dyilia_relaxed3_eyes:
    "images/ilia_dragonyule/faces/110367_04_parts_c035.png"
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
    "images/ilia_dragonyule/faces/110367_04_parts_c036.png"
    0.05
    repeat

image dyilia_askance_eyes:
    "images/ilia_dragonyule/faces/110367_04_parts_c037.png"
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
    "images/ilia_dragonyule/faces/110367_04_parts_c038.png"
    0.05
    repeat

image dyilia_smirk_eyes:
    "images/ilia_dragonyule/faces/110367_04_parts_c039.png"
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
    "images/ilia_dragonyule/faces/110367_04_parts_c040.png"
    0.05
    repeat

image dyilia_cry_eyes:
    "images/ilia_dragonyule/faces/110367_04_parts_c041.png"
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
    "images/ilia_dragonyule/faces/110367_04_parts_c042.png"
    0.05
    repeat



# MOUTH animations start here.

image dyilia_smile1_nottalking = "images/ilia_dragonyule/mouths/110367_04_parts_c005.png"

image dyilia_smile1_talking:
    "images/ilia_dragonyule/mouths/110367_04_parts_c006.png"
    0.15
    "images/ilia_dragonyule/mouths/110367_04_parts_c005.png"
    0.15
    repeat

image dyilia_smile1 = WhileSpeaking("dyili", "dyilia_smile1_talking", "dyilia_smile1_nottalking")


image dyilia_frown1_nottalking = "images/ilia_dragonyule/mouths/110367_04_parts_c007.png"

image dyilia_frown1_talking:
    "images/ilia_dragonyule/mouths/110367_04_parts_c008.png"
    0.15
    "images/ilia_dragonyule/mouths/110367_04_parts_c007.png"
    0.15
    repeat

image dyilia_frown1 = WhileSpeaking("dyili", "dyilia_frown1_talking", "dyilia_frown1_nottalking")


image dyilia_smile2_nottalking = "images/ilia_dragonyule/mouths/110367_04_parts_c017.png"

image dyilia_smile2_talking:
    "images/ilia_dragonyule/mouths/110367_04_parts_c018.png"
    0.15
    "images/ilia_dragonyule/mouths/110367_04_parts_c017.png"
    0.15
    repeat

image dyilia_smile2 = WhileSpeaking("dyili", "dyilia_smile2_talking", "dyilia_smile2_nottalking")


image dyilia_frown2_nottalking = "images/ilia_dragonyule/mouths/110367_04_parts_c019.png"

image dyilia_frown2_talking:
    "images/ilia_dragonyule/mouths/110367_04_parts_c020.png"
    0.15
    "images/ilia_dragonyule/mouths/110367_04_parts_c019.png"
    0.15
    repeat

image dyilia_frown2 = WhileSpeaking("dyili", "dyilia_frown2_talking", "dyilia_frown2_nottalking")


image dyilia_grimace1_nottalking = "images/ilia_dragonyule/mouths/110367_04_parts_c021.png"

image dyilia_grimace1_talking:
    "images/ilia_dragonyule/mouths/110367_04_parts_c021.png"
    0.15
    "images/ilia_dragonyule/mouths/110367_04_parts_c022.png"
    0.15
    repeat

image dyilia_grimace1 = WhileSpeaking("dyili", "dyilia_grimace1_talking", "dyilia_grimace1_nottalking")


image dyilia_grin1_nottalking = "images/ilia_dragonyule/mouths/110367_04_parts_c023.png"

image dyilia_grin1_talking:
    "images/ilia_dragonyule/mouths/110367_04_parts_c024.png"
    0.15
    "images/ilia_dragonyule/mouths/110367_04_parts_c023.png"
    0.15
    repeat

image dyilia_grin1 = WhileSpeaking("dyili", "dyilia_grin1_talking", "dyilia_grin1_nottalking")


image dyilia_frown3_nottalking = "images/ilia_dragonyule/mouths/110367_04_parts_c029.png"

image dyilia_frown3_talking:
    "images/ilia_dragonyule/mouths/110367_04_parts_c030.png"
    0.15
    "images/ilia_dragonyule/mouths/110367_04_parts_c029.png"
    0.15
    repeat

image dyilia_frown3 = WhileSpeaking("dyili", "dyilia_frown3_talking", "dyilia_frown3_nottalking")


image dyilia_grimace2_nottalking = "images/ilia_dragonyule/mouths/110367_04_parts_c031.png"

image dyilia_grimace2_talking:
    "images/ilia_dragonyule/mouths/110367_04_parts_c031.png"
    0.15
    "images/ilia_dragonyule/mouths/110367_04_parts_c032.png"
    0.15
    repeat

image dyilia_grimace2 = WhileSpeaking("dyili", "dyilia_grimace2_talking", "dyilia_grimace2_nottalking")


# This one's BASICALLY the same as frown1 but I think it shows a pixel's worth of teeth.
image dyilia_frown4_nottalking = "images/ilia_dragonyule/mouths/110367_04_parts_c033.png"

image dyilia_frown4_talking:
    "images/ilia_dragonyule/mouths/110367_04_parts_c034.png"
    0.15
    "images/ilia_dragonyule/mouths/110367_04_parts_c033.png"
    0.15
    repeat

image dyilia_frown4 = WhileSpeaking("dyili", "dyilia_frown4_talking", "dyilia_frown4_nottalking")


image dyilia_smile3_nottalking = "images/ilia_dragonyule/mouths/110367_04_parts_c043.png"

image dyilia_smile3_talking:
    "images/ilia_dragonyule/mouths/110367_04_parts_c044.png"
    0.15
    "images/ilia_dragonyule/mouths/110367_04_parts_c043.png"
    0.15
    repeat

image dyilia_smile3 = WhileSpeaking("dyili", "dyilia_smile3_talking", "dyilia_smile3_nottalking")


image dyilia_frown5_nottalking = "images/ilia_dragonyule/mouths/110367_04_parts_c045.png"

image dyilia_frown5_talking:
    "images/ilia_dragonyule/mouths/110367_04_parts_c046.png"
    0.15
    "images/ilia_dragonyule/mouths/110367_04_parts_c045.png"
    0.15
    repeat

image dyilia_frown5 = WhileSpeaking("dyili", "dyilia_frown5_talking", "dyilia_frown5_nottalking")


image dyilia_grin2_nottalking = "images/ilia_dragonyule/mouths/110367_04_parts_c047.png"

image dyilia_grin2_talking:
    "images/ilia_dragonyule/mouths/110367_04_parts_c047.png"
    0.15
    "images/ilia_dragonyule/mouths/110367_04_parts_c048.png"
    0.15
    repeat

image dyilia_grin2 = WhileSpeaking("dyili", "dyilia_grin2_talking", "dyilia_grin2_nottalking")


image dyilia_frown6_nottalking = "images/ilia_dragonyule/mouths/110367_04_parts_c049.png"

image dyilia_frown6_talking:
    "images/ilia_dragonyule/mouths/110367_04_parts_c050.png"
    0.15
    "images/ilia_dragonyule/mouths/110367_04_parts_c049.png"
    0.15
    repeat

image dyilia_frown6 = WhileSpeaking("dyili", "dyilia_frown6_talking", "dyilia_frown6_nottalking")




define dyiliSB = Character("Ilia", callback=speaker("dyiliSB"))

    # This program assumes that the following folders exist:
    #     -"images/ilia_dragonyule_sb"
    #     -"images/ilia_dragonyule_sb/faces"
    #     -"images/ilia_dragonyule_sb/mouths"

    # Dragonyule Ilia (snowboard form) dynamically blinks and, while speaking, also moves her mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Dragonyule Ilia (snowboard) appear with a snowboard*:
    #  -->  show dyiliaSB with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Dragonyule Ilia's (snowboard) eyes*:
    #  -->  show dyiliaSB [keyword]
    #  List of eye keywords:
    #     -->  relaxed (default), relaxed2, relaxed3, relaxed4, angry, askance,
    #          flinch, focused, focused2, surprised

    # *Changing Dragonyule Ilia's (snowboard) mouth*:
    #  -->  show dyiliaSB [keyword]
    #  List of mouth keywords:
    #     -->  smile1 (default), smile2, smile3, frown1, frown2, frown3, frown4,
    #          frown5, grimace1, grimace2, grin1, grin2

    # *Writing dialogue for Dragonyule Ilia (snowboard)*:
    #  --> dyiliSB "[Ilia's line here]"

    # *Making Dragonyule Ilia (snowboard) disappear*:
    #  --> hide dyiliaSB with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage dyiliaSB:

    always "images/ilia_dragonyule_sb/ilia_dragonyule_snowboard_body.png"

    group face:

        # 439/1028, 250/1028:
        pos (0.42704, 0.24319)

        attribute relaxed default:
            "dyiliaSB_relaxed_eyes"

        attribute focused:
            "dyiliaSB_focused_eyes"

        attribute relaxed2:
            "dyiliaSB_relaxed2_eyes"

        attribute flinch:
            "dyiliaSB_flinch_eyes"

        attribute surprised:
            "dyiliaSB_surprised_eyes"

        attribute relaxed3:
            "dyiliaSB_relaxed3_eyes"

        attribute furrowed:
            "dyiliaSB_furrowed_eyes"

        attribute angry:
            "dyiliaSB_angry_eyes"

        attribute relaxed4:
            "dyiliaSB_relaxed4_eyes"

        attribute askance:
            "dyiliaSB_askance_eyes"

        attribute focused2:
            "dyiliaSB_focused2_eyes"

    group mouth:

        pos (0.42704, 0.24319)

        attribute smile1 default:
            "dyiliaSB_smile1"

        attribute frown1:
            "dyiliaSB_frown1"

        attribute smile2:
            "dyiliaSB_smile2"

        attribute frown2:
            "dyiliaSB_frown2"

        attribute grimace1:
            "dyiliaSB_grimace1"

        attribute grin1:
            "dyiliaSB_grin1"

        attribute frown3:
            "dyiliaSB_frown3"

        attribute grimace2:
            "dyiliaSB_grimace2"

        attribute frown4:
            "dyiliaSB_frown4"

        attribute smile3:
            "dyiliaSB_smile3"

        attribute frown5:
            "dyiliaSB_frown5"

        attribute grin2:
            "dyiliaSB_grin2"


## EYE animations start here.

image dyiliaSB_relaxed_eyes:
    "images/ilia_dragonyule_sb/faces/110367_03_parts_c000.png"
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
    "images/ilia_dragonyule_sb/faces/110367_03_parts_c001.png"
    0.05
    repeat

image dyiliaSB_focused_eyes:
    "images/ilia_dragonyule_sb/faces/110367_03_parts_c002.png"
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
    "images/ilia_dragonyule_sb/faces/110367_03_parts_c003.png"
    0.05
    repeat

image dyiliaSB_relaxed2_eyes:
    "images/ilia_dragonyule_sb/faces/110367_03_parts_c009.png"
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
    "images/ilia_dragonyule_sb/faces/110367_03_parts_c010.png"
    0.05
    repeat

image dyiliaSB_flinch_eyes:
    "images/ilia_dragonyule_sb/faces/110367_03_parts_c011.png"
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
    "images/ilia_dragonyule_sb/faces/110367_03_parts_c012.png"
    0.05
    repeat

image dyiliaSB_surprised_eyes:
    "images/ilia_dragonyule_sb/faces/110367_03_parts_c013.png"
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
    "images/ilia_dragonyule_sb/faces/110367_03_parts_c014.png"
    0.05
    repeat

image dyiliaSB_relaxed3_eyes:
    "images/ilia_dragonyule_sb/faces/110367_03_parts_c015.png"
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
    "images/ilia_dragonyule_sb/faces/110367_03_parts_c016.png"
    0.05
    repeat

image dyiliaSB_furrowed_eyes:
    "images/ilia_dragonyule_sb/faces/110367_03_parts_c025.png"
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
    "images/ilia_dragonyule_sb/faces/110367_03_parts_c026.png"
    0.05
    repeat

image dyiliaSB_angry_eyes:
    "images/ilia_dragonyule_sb/faces/110367_03_parts_c027.png"
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
    "images/ilia_dragonyule_sb/faces/110367_03_parts_c028.png"
    0.05
    repeat

image dyiliaSB_relaxed4_eyes:
    "images/ilia_dragonyule_sb/faces/110367_03_parts_c035.png"
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
    "images/ilia_dragonyule_sb/faces/110367_03_parts_c036.png"
    0.05
    repeat

image dyiliaSB_askance_eyes:
    "images/ilia_dragonyule_sb/faces/110367_03_parts_c037.png"
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
    "images/ilia_dragonyule_sb/faces/110367_03_parts_c038.png"
    0.05
    repeat

image dyiliaSB_focused2_eyes:
    "images/ilia_dragonyule_sb/faces/110367_03_parts_c002.png"
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
    "images/ilia_dragonyule_sb/faces/110367_03_parts_c003.png"
    0.05
    repeat


# MOUTH animations start here.

image dyiliaSB_smile1_nottalking = "images/ilia_dragonyule_sb/mouths/110367_03_parts_c004.png"

image dyiliaSB_smile1_talking:
    "images/ilia_dragonyule_sb/mouths/110367_03_parts_c005.png"
    0.15
    "images/ilia_dragonyule_sb/mouths/110367_03_parts_c004.png"
    0.15
    repeat

image dyiliaSB_smile1 = WhileSpeaking("dyiliSB", "dyiliaSB_smile1_talking", "dyiliaSB_smile1_nottalking")


image dyiliaSB_frown1_nottalking = "images/ilia_dragonyule_sb/mouths/110367_03_parts_c007.png"

image dyiliaSB_frown1_talking:
    "images/ilia_dragonyule_sb/mouths/110367_03_parts_c008.png"
    0.15
    "images/ilia_dragonyule_sb/mouths/110367_03_parts_c007.png"
    0.15
    repeat

image dyiliaSB_frown1 = WhileSpeaking("dyiliSB", "dyiliaSB_frown1_talking", "dyiliaSB_frown1_nottalking")


image dyiliaSB_smile2_nottalking = "images/ilia_dragonyule_sb/mouths/110367_03_parts_c017.png"

image dyiliaSB_smile2_talking:
    "images/ilia_dragonyule_sb/mouths/110367_03_parts_c018.png"
    0.15
    "images/ilia_dragonyule_sb/mouths/110367_03_parts_c017.png"
    0.15
    repeat

image dyiliaSB_smile2 = WhileSpeaking("dyiliSB", "dyiliaSB_smile2_talking", "dyiliaSB_smile2_nottalking")


image dyiliaSB_frown2_nottalking = "images/ilia_dragonyule_sb/mouths/110367_03_parts_c019.png"

image dyiliaSB_frown2_talking:
    "images/ilia_dragonyule_sb/mouths/110367_03_parts_c020.png"
    0.15
    "images/ilia_dragonyule_sb/mouths/110367_03_parts_c019.png"
    0.15
    repeat

image dyiliaSB_frown2 = WhileSpeaking("dyiliSB", "dyiliaSB_frown2_talking", "dyiliaSB_frown2_nottalking")


image dyiliaSB_grimace1_nottalking = "images/ilia_dragonyule_sb/mouths/110367_03_parts_c021.png"

image dyiliaSB_grimace1_talking:
    "images/ilia_dragonyule_sb/mouths/110367_03_parts_c021.png"
    0.15
    "images/ilia_dragonyule_sb/mouths/110367_03_parts_c022.png"
    0.15
    repeat

image dyiliaSB_grimace1 = WhileSpeaking("dyiliSB", "dyiliaSB_grimace1_talking", "dyiliaSB_grimace1_nottalking")


image dyiliaSB_grin1_nottalking = "images/ilia_dragonyule_sb/mouths/110367_03_parts_c023.png"

image dyiliaSB_grin1_talking:
    "images/ilia_dragonyule_sb/mouths/110367_03_parts_c023.png"
    0.15
    "images/ilia_dragonyule_sb/mouths/110367_03_parts_c024.png"
    0.15
    repeat

image dyiliaSB_grin1 = WhileSpeaking("dyiliSB", "dyiliaSB_grin1_talking", "dyiliaSB_grin1_nottalking")


image dyiliaSB_frown3_nottalking = "images/ilia_dragonyule_sb/mouths/110367_03_parts_c029.png"

image dyiliaSB_frown3_talking:
    "images/ilia_dragonyule_sb/mouths/110367_03_parts_c030.png"
    0.15
    "images/ilia_dragonyule_sb/mouths/110367_03_parts_c029.png"
    0.15
    repeat

image dyiliaSB_frown3 = WhileSpeaking("dyiliSB", "dyiliaSB_frown3_talking", "dyiliaSB_frown3_nottalking")


image dyiliaSB_grimace2_nottalking = "images/ilia_dragonyule_sb/mouths/110367_03_parts_c031.png"

image dyiliaSB_grimace2_talking:
    "images/ilia_dragonyule_sb/mouths/110367_03_parts_c031.png"
    0.15
    "images/ilia_dragonyule_sb/mouths/110367_03_parts_c032.png"
    0.15
    repeat

image dyiliaSB_grimace2 = WhileSpeaking("dyiliSB", "dyiliaSB_grimace2_talking", "dyiliaSB_grimace2_nottalking")


image dyiliaSB_frown4_nottalking = "images/ilia_dragonyule_sb/mouths/110367_03_parts_c033.png"

image dyiliaSB_frown4_talking:
    "images/ilia_dragonyule_sb/mouths/110367_03_parts_c034.png"
    0.15
    "images/ilia_dragonyule_sb/mouths/110367_03_parts_c033.png"
    0.15
    repeat

image dyiliaSB_frown4 = WhileSpeaking("dyiliSB", "dyiliaSB_frown4_talking", "dyiliaSB_frown4_nottalking")


image dyiliaSB_smile3_nottalking = "images/ilia_dragonyule_sb/mouths/110367_03_parts_c041.png"

image dyiliaSB_smile3_talking:
    "images/ilia_dragonyule_sb/mouths/110367_03_parts_c042.png"
    0.15
    "images/ilia_dragonyule_sb/mouths/110367_03_parts_c041.png"
    0.15
    repeat

image dyiliaSB_smile3 = WhileSpeaking("dyiliSB", "dyiliaSB_smile3_talking", "dyiliaSB_smile3_nottalking")


image dyiliaSB_frown5_nottalking = "images/ilia_dragonyule_sb/mouths/110367_03_parts_c043.png"

image dyiliaSB_frown5_talking:
    "images/ilia_dragonyule_sb/mouths/110367_03_parts_c044.png"
    0.15
    "images/ilia_dragonyule_sb/mouths/110367_03_parts_c043.png"
    0.15
    repeat

image dyiliaSB_frown5 = WhileSpeaking("dyiliSB", "dyiliaSB_frown5_talking", "dyiliaSB_frown5_nottalking")


image dyiliaSB_grin2_nottalking = "images/ilia_dragonyule_sb/mouths/110367_03_parts_c045.png"

image dyiliaSB_grin2_talking:
    "images/ilia_dragonyule_sb/mouths/110367_03_parts_c045.png"
    0.15
    "images/ilia_dragonyule_sb/mouths/110367_03_parts_c046.png"
    0.15
    repeat

image dyiliaSB_grin2 = WhileSpeaking("dyiliSB", "dyiliaSB_grin2_talking", "dyiliaSB_grin2_nottalking")






# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

transform middle:
    xalign 0.5
    yalign 0.5

transform leftspot:
    xalign -0.25
    yalign 0.5

transform rightspot:
    xalign 1.25
    yalign 0.5









# The game starts here.

label iliaDY_character_procedures:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image wintervillage = "images/backgrounds/Sty_bg_0047_400.png"
    scene wintervillage at middle

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    show dyilia with dissolve
    dyili "Hey, everyone!  I don't have much time to chat."

    show dyilia askance grin1
    dyili "DabblerDragon doesn't have time to come up with a clever excuse because it's Dragonyule Eve 2022, so he said it was ok for me to break the fourth wall."
    dyili "Let's just say it's the awakening of my Auspex powers letting me look into other worlds... heh heh, sorry..."

    show dyilia focused smile2
    dyili "-Aaaaanyway, there's no time for turning this into a clever story, but we wanna wish you guys a Merry Dragonyule."
    dyili "So I'm gonna speedrun through my expressions so we can all just cut to the chase and enjoy the holiday!"

    show dyilia focused2 grin2
    dyili "So hang onto your butts, 'cause this is happening!"

# Expression test start
    show dyilia relaxed smile1
    dyili "These are my 'relaxed' face and 'smile1' mouth."

    show dyilia relaxed2 smile2
    dyili "These are my 'relaxed2' face and 'smile2' mouth."

    show dyilia relaxed3 smile3
    dyili "These are my 'relaxed3' face and 'smile3' mouth."

    show dyilia askance frown1
    dyili "These are my 'askance' face and 'frown1' mouth."

    show dyilia blush frown2
    dyili "These are my 'blush' face and 'frown2' mouth."

    show dyilia cry frown3
    dyili "These are my 'cry' face and 'frown3' mouth."

    show dyilia flinch frown4
    dyili "These are my 'flinch' face and 'frown4' mouth."

    show dyilia focused frown5
    dyili "These are my 'focused' face and 'frown5' mouth."

    show dyilia focused2 frown6
    dyili "These are my 'focused2' face and 'frown6' mouth."

    show dyilia sad grimace1
    dyili "These are my 'sad' face and 'grimace1' mouth."

    show dyilia smirk grin1
    dyili "Interrupting the 'grimace' sequence so this makes more sense:  These are my 'smirk' face and 'grin1' mouth."

    show dyilia surprised grimace2
    dyili "These are my 'surpised' face and 'grimace2' mouth."

    show dyilia grin2
    dyili "I'm done with the faces, but last but not least, here's my 'grin2' mouth."


    show dyilia relaxed smile1
    dyili "Well, that was fun!  Anyway, hope you all have a fun Dragonyule!  I'm gonna go head out in the snow now."
    dyili "And one more thing:  Thanks so much for all the support you've shown DabblerDragon for this silly little project; you guys are the best!"

    hide dyilia with dissolve



    image snowstorm = "images/backgrounds/Sty_bg_0055_100_00.png"
    scene snowstorm at middle

    "..."

    show dyiliaSB focused with fade
    play music "audio/music/BGM (Arikitari)  WON Dragalia Lost - One Starry Dragonyule.mp3"

    dyiliSB "PSYCH!  As if DabblerDragon would just leave it at that for DRAGONYULE!"

    show dyiliaSB relaxed2 smile2
    dyiliSB "As you can see, he also implemented my SNOWBOARD version!"

    show dyiliaSB surprised smile2
    dyiliSB "Unfortunately it's treated as a separate character at a certain level, so you need to say 'dyiliSB' instead of 'dyili', but it totally works!"

    show dyiliaSB focused2 smile1
    dyiliSB "And can you hear that?  This update's coming with the gift of music, baby! (You should turn on your speakers if they're off.)"
    dyiliSB "This is the BGM version since DabblerDragon doesn't wanna get sued by the powers-that-be, but it's (Arikitari) by WON!"
    dyiliSB "It was from the 'One Starry Dragonyule' event featuring yours truly!"
    dyiliSB "He still has a lot to figure out, but right now you can use the phrase 'play music \"audio/music/filename.mp3\"' to play music!"

    show dyiliaSB askance smile3
    dyiliSB "Or, like, whatever the directory is, of course.  I hear he tried to figure out how to loop it but hasn't quite sorted it out yet."

    show dyiliaSB surprised frown1
    dyiliSB "Oh!  And you type 'stop music' to have the music stop."

    show dyiliaSB relaxed smile1
    dyiliSB "Anyway, lemme go through my expressions real quick while relaying a message from DabblerDragon."

    show dyiliaSB relaxed smile1
    dyiliSB "(relaxed smile1) He said, \"Thanks so much everybody for taking the time to try out Dragalia Lost Story Engine!\""

    show dyiliaSB relaxed2 smile2
    dyiliSB "(relaxed2 smile2) \"I wasn't sure at first whether it was something that I should even reach out to people about, but everyone's been super supportive.\""

    show dyiliaSB relaxed3 smile3
    dyiliSB "(relaxed3 smile3) \"I know that there's still a ton of work left to do, but just being able to share this project with other people is really special and meaningful to me.\""

    show dyiliaSB relaxed4 frown1
    dyiliSB "(relaxed4 frown1) \"There's some big changes in my life coming very soon, so I'm not sure how regularly I'll be able to keep implementing new characters over the next few months.\""

    show dyiliaSB angry frown2
    dyiliSB "(angry frown2) \"But I'm gonna do my absolute best to keep this project going!  We Dragalia Losties deserve to keep enjoying these characters for years to come!\""

    show dyiliaSB askance frown3
    dyiliSB "(askance frown3) \"I feel really far behind compared to where I wanted to be.  At this rate I'll be lucky if I can get 'My Finni Valentine' done by Valentine's Day...\""

    show dyiliaSB flinch frown4
    dyiliSB "(flinch frown4) \"I really don't wanna rope other people into spending their time on this, but if you want certain characters, you may need to take point on implementing the characters you want.\""

    show dyiliaSB focused frown5
    dyiliSB "(focused frown5) \"You guys have done some really amazing things already, and I'm super impressed by your creativity and tenacity.\""

    show dyiliaSB focused2 grimace1
    dyiliSB "(focused2 grimace1) \"I know I'm just kind of a random guy doing stuff to cope with Dragalia Lost ending, so I hope you guys haven't found this annoying or attention-seeking.\""

    show dyiliaSB surprised grimace2
    dyiliSB "(surprised grimace2) \"I have a ton of stuff that is half-complete too, like Laxi's expressions / test file, and I really need to make progress on quality-of-life stuff too like a tutorial 'story', attack animations and those emotes that appear in speech bubbles...\""

    show dyiliaSB relaxed grin1
    dyiliSB "(relaxed grin1) \"But this project has been a lot of fun so far, and I'm sure I'll get to them eventually.\""

    show dyiliaSB relaxed grin2
    dyiliSB "(relaxed grin2) \"And you guys should feel free to keep telling me what you want implemented next.  The more I have feedback on what people want, the better I can tailor 'Dragalia Lost Story Engine' to people's needs and enable them to make all kinds of cool stuff!\""

    show dyiliaSB relaxed smile1
    dyiliSB "Anyway, that's what he said!  It seems like he really was thankful for you guys."

    show dyiliaSB flinch grin1
    dyiliSB "Man, 2022 was a wild ride, what with Dragalia suddenly EoS'ing and experiencing all the emotions that came along with that."

    show dyiliaSB relaxed2 smile3
    dyiliSB "I know I'm just a fictional character, but I'm personally flattered that you guys care enough about our little world to try to keep us alive."

    show dyiliaSB askance grin2
    dyiliSB "And... maybe I'll get a reincarnation eventually in some sequel/reboot?  'Dragalia Lost: Re:Dive?'  'Dragalia Found'?  I swear, this isn't copium!"

    show dyiliaSB relaxed smile1
    dyiliSB "Anyway, it's about time for me to check out, but I wanna express gratitude to Nintendo and Cygames for making such a cool world for me to live in, and you guys for taking part in that journey."

    show dyiliaSB relaxed smile1
    dyiliSB "Please continue to support their official releases, and I'll see you in the New Year 2023.  Maybe that rabbit Wyrmclan leader will finally make an appearance?"

    show dyiliaSB relaxed grin1
    dyiliSB "Regardless of where this goes, have a Merry Dragonyule and all the best blessings in 2023.  The blessings of ME be upon you, hehe!!!"

    hide dyiliaSB with dissolve

    stop music fadeout 1.0

    # This goes back to script

    jump testfiles
