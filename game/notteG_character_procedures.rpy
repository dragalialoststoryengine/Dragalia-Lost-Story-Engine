
    # Notte Character Procedures File

    # Paste this file into a story if you want to use Notte.  These procedures animate Notte as a speaker.
    # You'll also need to paste THIS line into your actual script above the script label whenever you're using Notte:

define gnott = Character("Notte", callback=speaker("gnott"))

    # This program assumes that the following folders exist:
    #     -"images/notte_gala"
    #     -"images/notte_gala/faces"
    #     -"images/notte_gala/mouths"

    # Notte dynamically blinks and, while speaking, also moves her mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Notte appear*:
    #  -->  show notte_gala with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Notte's eyes*:
    #  -->  show notte_gala [keyword]
    #  List of eye keywords:
    #     -->  relaxed (default), focused, relaxed2, closed_relaxed2, grumpy, closed_grumpy,
    #          surprised, sad, sad2, sad3, shock, relaxed3, grumpy2, sad4, squint

    # *Changing Notte's mouth*:
    #  -->  show notte_gala [keyword]
    #  List of mouth keywords:
    #     -->  smile1 (default), closed_smile1, frown1, closed_frown1, gasp1, shout1, smile2,
    #          frown2, shout2, smile3, frown3, smile4, frown4, pout1

    # *Writing dialogue for Notte*:
    #  --> gnott "[Notte's line here]"

    # *Making Notte disappear*:
    #  --> hide notte_gala with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage notte_gala:

    always "images/notte_gala/notte_gala_body.png"

    group face:

        # 446/1024, 291/1024:
        pos (0.43555, 0.28418)

        attribute relaxed default:
            "notte_gala_relaxed_eyes"

        attribute focused:
            "notte_gala_focused_eyes"

        attribute relaxed2:
            "notte_gala_relaxed2_eyes"

        attribute closed_relaxed2:
            "images/notte_gala/faces/100007_07_parts_c010.png"

        attribute grumpy:
            "notte_gala_grumpy_eyes"

        attribute closed_grumpy:
            "images/notte_gala/faces/100007_07_parts_c012.png"

        attribute surprised:
            "notte_gala_surprised_eyes"

        attribute sad:
            "notte_gala_sad_eyes"

        attribute sad2:
            "notte_gala_sad2_eyes"

        attribute sad3:
            "notte_gala_sad3_eyes"

        attribute shock:
            "notte_gala_shock_eyes"

        attribute relaxed3:
            "notte_gala_relaxed3_eyes"

        attribute grumpy2:
            "notte_gala_grumpy2_eyes"

        attribute sad4:
            "notte_gala_sad4_eyes"

        attribute squint:
            "notte_gala_squint_eyes"


    group mouth:

        pos (0.43555, 0.28418)

        attribute smile1 default:
            "notte_gala_smile1"

        attribute closed_smile1:
            "notte_gala_smile1_nottalking"

        attribute frown1:
            "notte_gala_frown1"

        attribute closed_frown1:
            "notte_gala_frown1_nottalking"

        attribute smile2:
            "notte_gala_smile2"

        attribute gasp1:
            "notte_gala_gasp1"

        attribute shout1:
            "notte_gala_shout1"

        attribute smile3:
            "notte_gala_smile3"

        attribute frown2:
            "notte_gala_frown2"

        attribute shout2:
            "notte_gala_shout2"

        attribute smile4:
            "notte_gala_smile4"

        attribute frown3:
            "notte_gala_frown3"

        attribute smile5:
            "notte_gala_smile5"

        attribute frown4:
            "notte_gala_frown4"

        attribute pout1:
            "notte_gala_pout1"


## EYE animations start here.

image notte_gala_relaxed_eyes:
    "images/notte_gala/faces/100007_07_parts_c000.png"
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
    "images/notte_gala/faces/100007_07_parts_c001.png"
    0.05
    repeat

image notte_gala_focused_eyes:
    "images/notte_gala/faces/100007_07_parts_c002.png"
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
    "images/notte_gala/faces/100007_07_parts_c003.png"
    0.05
    repeat

image notte_gala_relaxed2_eyes:
    "images/notte_gala/faces/100007_07_parts_c009.png"
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
    "images/notte_gala/faces/100007_07_parts_c010.png"
    0.05
    repeat

image notte_gala_grumpy_eyes:
    "images/notte_gala/faces/100007_07_parts_c011.png"
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
    "images/notte_gala/faces/100007_07_parts_c012.png"
    0.05
    repeat

image notte_gala_surprised_eyes:
    "images/notte_gala/faces/100007_07_parts_c013.png"
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
    "images/notte_gala/faces/100007_07_parts_c014.png"
    0.05
    repeat

image notte_gala_sad_eyes:
    "images/notte_gala/faces/100007_07_parts_c015.png"
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
    "images/notte_gala/faces/100007_07_parts_c016.png"
    0.05
    repeat

image notte_gala_sad2_eyes:
    "images/notte_gala/faces/100007_07_parts_c025.png"
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
    "images/notte_gala/faces/100007_07_parts_c026.png"
    0.05
    repeat

image notte_gala_sad3_eyes:
    "images/notte_gala/faces/100007_07_parts_c027.png"
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
    "images/notte_gala/faces/100007_07_parts_c028.png"
    0.05
    repeat

image notte_gala_shock_eyes:
    "images/notte_gala/faces/100007_07_parts_c029.png"
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
    "images/notte_gala/faces/100007_07_parts_c030.png"
    0.05
    repeat

image notte_gala_relaxed3_eyes:
    "images/notte_gala/faces/100007_07_parts_c031.png"
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
    "images/notte_gala/faces/100007_07_parts_c032.png"
    0.05
    repeat

image notte_gala_grumpy2_eyes:
    "images/notte_gala/faces/100007_07_parts_c039.png"
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
    "images/notte_gala/faces/100007_07_parts_c040.png"
    0.05
    repeat

image notte_gala_sad4_eyes:
    "images/notte_gala/faces/100007_07_parts_c041.png"
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
    "images/notte_gala/faces/100007_07_parts_c042.png"
    0.05
    repeat

image notte_gala_squint_eyes:
    "images/notte_gala/faces/100007_07_parts_c043.png"
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
    "images/notte_gala/faces/100007_07_parts_c044.png"
    0.05
    repeat



# MOUTH animations start here.

image notte_gala_smile1_nottalking = "images/notte_gala/mouths/100007_07_parts_c004.png"

image notte_gala_smile1_talking:
    "images/notte_gala/mouths/100007_07_parts_c005.png"
    0.15
    "images/notte_gala/mouths/100007_07_parts_c004.png"
    0.15
    repeat

image notte_gala_smile1 = WhileSpeaking("gnott", "notte_gala_smile1_talking", "notte_gala_smile1_nottalking")


image notte_gala_frown1_nottalking = "images/notte_gala/mouths/100007_07_parts_c007.png"

image notte_gala_frown1_talking:
    "images/notte_gala/mouths/100007_07_parts_c008.png"
    0.15
    "images/notte_gala/mouths/100007_07_parts_c007.png"
    0.15
    repeat

image notte_gala_frown1 = WhileSpeaking("gnott", "notte_gala_frown1_talking", "notte_gala_frown1_nottalking")


image notte_gala_smile2_nottalking = "images/notte_gala/mouths/100007_07_parts_c017.png"

image notte_gala_smile2_talking:
    "images/notte_gala/mouths/100007_07_parts_c018.png"
    0.15
    "images/notte_gala/mouths/100007_07_parts_c017.png"
    0.15
    repeat

image notte_gala_smile2 = WhileSpeaking("gnott", "notte_gala_smile1_talking", "notte_gala_smile1_nottalking")


image notte_gala_gasp1_nottalking = "images/notte_gala/mouths/100007_07_parts_c019.png"

image notte_gala_gasp1_talking:
    "images/notte_gala/mouths/100007_07_parts_c020.png"
    0.15
    "images/notte_gala/mouths/100007_07_parts_c019.png"
    0.15
    repeat

image notte_gala_gasp1 = WhileSpeaking("gnott", "notte_gala_gasp1_talking", "notte_gala_gasp1_nottalking")


image notte_gala_shout1_nottalking = "images/notte_gala/mouths/100007_07_parts_c021.png"

image notte_gala_shout1_talking:
    "images/notte_gala/mouths/100007_07_parts_c022.png"
    0.15
    "images/notte_gala/mouths/100007_07_parts_c021.png"
    0.15
    repeat

image notte_gala_shout1 = WhileSpeaking("gnott", "notte_gala_shout1_talking", "notte_gala_shout1_nottalking")


image notte_gala_smile3_nottalking = "images/notte_gala/mouths/100007_07_parts_c023.png"

image notte_gala_smile3_talking:
    "images/notte_gala/mouths/100007_07_parts_c024.png"
    0.15
    "images/notte_gala/mouths/100007_07_parts_c023.png"
    0.15
    repeat

image notte_gala_smile3 = WhileSpeaking("gnott", "notte_gala_smile2_talking", "notte_gala_smile2_nottalking")


image notte_gala_frown2_nottalking = "images/notte_gala/mouths/100007_07_parts_c033.png"

image notte_gala_frown2_talking:
    "images/notte_gala/mouths/100007_07_parts_c034.png"
    0.15
    "images/notte_gala/mouths/100007_07_parts_c033.png"
    0.15
    repeat

image notte_gala_frown2 = WhileSpeaking("gnott", "notte_gala_frown2_talking", "notte_gala_frown2_nottalking")


image notte_gala_shout2_nottalking = "images/notte_gala/mouths/100007_07_parts_c035.png"

image notte_gala_shout2_talking:
    "images/notte_gala/mouths/100007_07_parts_c036.png"
    0.15
    "images/notte_gala/mouths/100007_07_parts_c035.png"
    0.15
    repeat

image notte_gala_shout2 = WhileSpeaking("gnott", "notte_gala_shout2_talking", "notte_gala_shout2_nottalking")


image notte_gala_smile4_nottalking = "images/notte_gala/mouths/100007_07_parts_c037.png"

image notte_gala_smile4_talking:
    "images/notte_gala/mouths/100007_07_parts_c038.png"
    0.15
    "images/notte_gala/mouths/100007_07_parts_c037.png"
    0.15
    repeat

image notte_gala_smile4 = WhileSpeaking("gnott", "notte_gala_smile3_talking", "notte_gala_smile3_nottalking")


image notte_gala_frown3_nottalking = "images/notte_gala/mouths/100007_07_parts_c045.png"

image notte_gala_frown3_talking:
    "images/notte_gala/mouths/100007_07_parts_c046.png"
    0.15
    "images/notte_gala/mouths/100007_07_parts_c045.png"
    0.15
    repeat

image notte_gala_frown3 = WhileSpeaking("gnott", "notte_gala_frown3_talking", "notte_gala_frown3_nottalking")


image notte_gala_smile5_nottalking = "images/notte_gala/mouths/100007_07_parts_c047.png"

image notte_gala_smile5_talking:
    "images/notte_gala/mouths/100007_07_parts_c048.png"
    0.15
    "images/notte_gala/mouths/100007_07_parts_c047.png"
    0.15
    repeat

image notte_gala_smile5 = WhileSpeaking("gnott", "notte_gala_smile4_talking", "notte_gala_smile4_nottalking")


image notte_gala_frown4_nottalking = "images/notte_gala/mouths/100007_07_parts_c049.png"

image notte_gala_frown4_talking:
    "images/notte_gala/mouths/100007_07_parts_c050.png"
    0.15
    "images/notte_gala/mouths/100007_07_parts_c049.png"
    0.15
    repeat

image notte_gala_frown4 = WhileSpeaking("gnott", "notte_gala_frown4_talking", "notte_gala_frown4_nottalking")


image notte_gala_pout1_nottalking = "images/notte_gala/mouths/100007_07_parts_c051.png"

image notte_gala_pout1_talking:
    "images/notte_gala/mouths/100007_07_parts_c052.png"
    0.15
    "images/notte_gala/mouths/100007_07_parts_c051.png"
    0.15
    repeat

image notte_gala_pout1 = WhileSpeaking("gnott", "notte_gala_pout1_talking", "notte_gala_pout1_nottalking")





    # Meta Notte Character Procedures File

    # Paste this file into a story if you want to use Meta Notte.  These procedures animate Notte as a speaker.
    # You'll also need to paste THIS line into your actual script above the script label whenever you're using Notte:

define mnott = Character("Notte", callback=speaker("mnott"))

    # This program assumes that the following folders exist:
    #     -"images/notte_gala"
    #     -"images/notte_gala/faces"
    #     -"images/notte_gala/mouths"

    # Notte dynamically blinks and, while speaking, also moves her mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Meta Notte appear*:
    #  -->  show notte_meta with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Meta Notte's eyes*:
    #  -->  show notte_meta [keyword]
    #  List of eye keywords:
    #     -->  relaxed (default), focused, relaxed2, closed_relaxed2, grumpy, closed_grumpy,
    #          surprised, sad, sad2, sad3, shock, relaxed3, relaxed4, grumpy2, sad4, squint

    # *Changing Meta Notte's mouth*:
    #  -->  show notte_meta [keyword]
    #  List of mouth keywords:
    #     -->  smile1 (default), closed_smile1, frown1, closed_frown1, gasp1, shout1, smile2,
    #          frown2, shout2, smile3, frown3, smile4, frown4, pout1

    # *Writing dialogue for Meta Notte*:
    #  --> mnott "[Notte's line here]"

    # *Making Meta Notte disappear*:
    #  --> hide notte_meta with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage notte_meta:

    always "images/notte_meta/notte_meta_body.png"

    group face:

        # 363/1024, 114/1024:
        pos (0.35449, 0.11133)

        attribute relaxed default:
            "notte_meta_relaxed_eyes"

        attribute closed_relaxed:
            "images/notte_meta/faces/210153_01_parts_c001.png"

        attribute focused:
            "notte_meta_focused_eyes"

        attribute relaxed2:
            "notte_meta_relaxed2_eyes"

        attribute closed_relaxed2:
            "images/notte_meta/faces/210153_01_parts_c012.png"

        attribute grumpy:
            "notte_meta_grumpy_eyes"

        attribute closed_grumpy:
            "images/notte_meta/faces/210153_01_parts_c014.png"

        attribute surprised:
            "notte_meta_surprised_eyes"

        attribute sad:
            "notte_meta_sad_eyes"

        attribute sad2:
            "notte_meta_sad2_eyes"

        attribute sad3:
            "notte_meta_sad3_eyes"

        attribute shock:
            "notte_meta_shock_eyes"

        attribute relaxed3:
            "notte_meta_relaxed3_eyes"

        attribute relaxed4:
            "notte_meta_relaxed4_eyes"

        attribute grumpy2:
            "notte_meta_grumpy2_eyes"

        attribute closed_grumpy2:
            "images/notte_meta/faces/210153_01_parts_c044.png"

        attribute sad4:
            "notte_meta_sad4_eyes"

        attribute squint:
            "notte_meta_squint_eyes"


    group mouth:

        pos (0.35449, 0.11133)

        attribute smile1 default:
            "notte_meta_smile1"

        attribute closed_smile1:
            "notte_meta_smile1_nottalking"

        attribute frown1:
            "notte_meta_frown1"

        attribute closed_frown1:
            "notte_meta_frown1_nottalking"

        attribute smile2:
            "notte_meta_smile2"

        attribute gasp1:
            "notte_meta_gasp1"

        attribute shout1:
            "notte_meta_shout1"

        attribute smile3:
            "notte_meta_smile3"

        attribute frown2:
            "notte_meta_frown2"

        attribute shout2:
            "notte_meta_shout2"

        attribute smile4:
            "notte_meta_smile4"

        attribute frown3:
            "notte_meta_frown3"

        attribute smile5:
            "notte_meta_smile5"

        attribute frown4:
            "notte_meta_frown4"

        attribute pout1:
            "notte_meta_pout1"


## EYE animations start here.

image notte_meta_relaxed_eyes:
    "images/notte_meta/faces/210153_01_parts_c000.png"
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
    "images/notte_meta/faces/210153_01_parts_c001.png"
    0.05
    repeat

image notte_meta_focused_eyes:
    "images/notte_meta/faces/210153_01_parts_c004.png"
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
    "images/notte_meta/faces/210153_01_parts_c005.png"
    0.05
    repeat

image notte_meta_relaxed2_eyes:
    "images/notte_meta/faces/210153_01_parts_c011.png"
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
    "images/notte_meta/faces/210153_01_parts_c012.png"
    0.05
    repeat

image notte_meta_grumpy_eyes:
    "images/notte_meta/faces/210153_01_parts_c013.png"
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
    "images/notte_meta/faces/210153_01_parts_c014.png"
    0.05
    repeat

image notte_meta_surprised_eyes:
    "images/notte_meta/faces/210153_01_parts_c015.png"
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
    "images/notte_meta/faces/210153_01_parts_c016.png"
    0.05
    repeat

image notte_meta_sad_eyes:
    "images/notte_meta/faces/210153_01_parts_c017.png"
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
    "images/notte_meta/faces/210153_01_parts_c018.png"
    0.05
    repeat

image notte_meta_sad2_eyes:
    "images/notte_meta/faces/210153_01_parts_c027.png"
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
    "images/notte_meta/faces/210153_01_parts_c028.png"
    0.05
    repeat

image notte_meta_sad3_eyes:
    "images/notte_meta/faces/210153_01_parts_c029.png"
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
    "images/notte_meta/faces/210153_01_parts_c030.png"
    0.05
    repeat

image notte_meta_shock_eyes:
    "images/notte_meta/faces/210153_01_parts_c031.png"
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
    "images/notte_meta/faces/210153_01_parts_c032.png"
    0.05
    repeat

image notte_meta_relaxed3_eyes:
    "images/notte_meta/faces/210153_01_parts_c033.png"
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
    "images/notte_meta/faces/210153_01_parts_c034.png"
    0.05
    repeat

image notte_meta_relaxed4_eyes:
    "images/notte_meta/faces/210153_01_parts_c042.png"
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
    "images/notte_meta/faces/210153_01_parts_c001.png"
    0.05
    repeat

image notte_meta_grumpy2_eyes:
    "images/notte_meta/faces/210153_01_parts_c043.png"
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
    "images/notte_meta/faces/210153_01_parts_c044.png"
    0.05
    repeat

image notte_meta_sad4_eyes:
    "images/notte_meta/faces/210153_01_parts_c045.png"
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
    "images/notte_meta/faces/210153_01_parts_c046.png"
    0.05
    repeat

image notte_meta_squint_eyes:
    "images/notte_meta/faces/210153_01_parts_c047.png"
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
    "images/notte_meta/faces/210153_01_parts_c048.png"
    0.05
    repeat



# MOUTH animations start here.

image notte_meta_smile1_nottalking = "images/notte_meta/mouths/210153_01_parts_c006.png"

image notte_meta_smile1_talking:
    "images/notte_meta/mouths/210153_01_parts_c007.png"
    0.15
    "images/notte_meta/mouths/210153_01_parts_c006.png"
    0.15
    repeat

image notte_meta_smile1 = WhileSpeaking("mnott", "notte_meta_smile1_talking", "notte_meta_smile1_nottalking")


image notte_meta_frown1_nottalking = "images/notte_meta/mouths/210153_01_parts_c009.png"

image notte_meta_frown1_talking:
    "images/notte_meta/mouths/210153_01_parts_c010.png"
    0.15
    "images/notte_meta/mouths/210153_01_parts_c009.png"
    0.15
    repeat

image notte_meta_frown1 = WhileSpeaking("mnott", "notte_meta_frown1_talking", "notte_meta_frown1_nottalking")


image notte_meta_smile2_nottalking = "images/notte_meta/mouths/210153_01_parts_c019.png"

image notte_meta_smile2_talking:
    "images/notte_meta/mouths/210153_01_parts_c020.png"
    0.15
    "images/notte_meta/mouths/210153_01_parts_c019.png"
    0.15
    repeat

image notte_meta_smile2 = WhileSpeaking("mnott", "notte_meta_smile1_talking", "notte_meta_smile1_nottalking")


image notte_meta_gasp1_nottalking = "images/notte_meta/mouths/210153_01_parts_c021.png"

image notte_meta_gasp1_talking:
    "images/notte_meta/mouths/210153_01_parts_c022.png"
    0.15
    "images/notte_meta/mouths/210153_01_parts_c021.png"
    0.15
    repeat

image notte_meta_gasp1 = WhileSpeaking("mnott", "notte_meta_gasp1_talking", "notte_meta_gasp1_nottalking")


image notte_meta_shout1_nottalking = "images/notte_meta/mouths/210153_01_parts_c023.png"

image notte_meta_shout1_talking:
    "images/notte_meta/mouths/210153_01_parts_c024.png"
    0.15
    "images/notte_meta/mouths/210153_01_parts_c023.png"
    0.15
    repeat

image notte_meta_shout1 = WhileSpeaking("mnott", "notte_meta_shout1_talking", "notte_meta_shout1_nottalking")


image notte_meta_smile3_nottalking = "images/notte_meta/mouths/210153_01_parts_c025.png"

image notte_meta_smile3_talking:
    "images/notte_meta/mouths/210153_01_parts_c026.png"
    0.15
    "images/notte_meta/mouths/210153_01_parts_c025.png"
    0.15
    repeat

image notte_meta_smile3 = WhileSpeaking("mnott", "notte_meta_smile2_talking", "notte_meta_smile2_nottalking")


image notte_meta_frown2_nottalking = "images/notte_meta/mouths/210153_01_parts_c035.png"

image notte_meta_frown2_talking:
    "images/notte_meta/mouths/210153_01_parts_c036.png"
    0.15
    "images/notte_meta/mouths/210153_01_parts_c035.png"
    0.15
    repeat

image notte_meta_frown2 = WhileSpeaking("mnott", "notte_meta_frown2_talking", "notte_meta_frown2_nottalking")


image notte_meta_shout2_nottalking = "images/notte_meta/mouths/210153_01_parts_c038.png"

image notte_meta_shout2_talking:
    "images/notte_meta/mouths/210153_01_parts_c039.png"
    0.15
    "images/notte_meta/mouths/210153_01_parts_c038.png"
    0.15
    repeat

image notte_meta_shout2 = WhileSpeaking("mnott", "notte_meta_shout2_talking", "notte_meta_shout2_nottalking")


image notte_meta_smile4_nottalking = "images/notte_meta/mouths/210153_01_parts_c040.png"

image notte_meta_smile4_talking:
    "images/notte_meta/mouths/210153_01_parts_c041.png"
    0.15
    "images/notte_meta/mouths/210153_01_parts_c040.png"
    0.15
    repeat

image notte_meta_smile4 = WhileSpeaking("mnott", "notte_meta_smile3_talking", "notte_meta_smile3_nottalking")


image notte_meta_frown3_nottalking = "images/notte_meta/mouths/210153_01_parts_c049.png"

image notte_meta_frown3_talking:
    "images/notte_meta/mouths/210153_01_parts_c050.png"
    0.15
    "images/notte_meta/mouths/210153_01_parts_c049.png"
    0.15
    repeat

image notte_meta_frown3 = WhileSpeaking("mnott", "notte_meta_frown3_talking", "notte_meta_frown3_nottalking")


image notte_meta_smile5_nottalking = "images/notte_meta/mouths/210153_01_parts_c051.png"

image notte_meta_smile5_talking:
    "images/notte_meta/mouths/210153_01_parts_c052.png"
    0.15
    "images/notte_meta/mouths/210153_01_parts_c051.png"
    0.15
    repeat

image notte_meta_smile5 = WhileSpeaking("mnott", "notte_meta_smile4_talking", "notte_meta_smile4_nottalking")


image notte_meta_frown4_nottalking = "images/notte_meta/mouths/210153_01_parts_c053.png"

image notte_meta_frown4_talking:
    "images/notte_meta/mouths/210153_01_parts_c054.png"
    0.15
    "images/notte_meta/mouths/210153_01_parts_c053.png"
    0.15
    repeat

image notte_meta_frown4 = WhileSpeaking("mnott", "notte_meta_frown4_talking", "notte_meta_frown4_nottalking")


image notte_meta_pout1_nottalking = "images/notte_meta/mouths/210153_01_parts_c055.png"

image notte_meta_pout1_talking:
    "images/notte_meta/mouths/210153_01_parts_c056.png"
    0.15
    "images/notte_meta/mouths/210153_01_parts_c055.png"
    0.15
    repeat

image notte_meta_pout1 = WhileSpeaking("mnott", "notte_meta_pout1_talking", "notte_meta_pout1_nottalking")












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

label notteG_character_procedures:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image town_exterior = "images/backgrounds/Sty_bg_0018_100_00.png"
    scene town_exterior

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show notte_gala with dissolve
    gnott "Woohoo! Being people-sized rules!"

    show notte_gala focused
    gnott "Even just being able to just hitchhike around town feels like I'm in a totally new world!"

    show notte_gala grumpy frown1
    gnott "Ouchie!\nMan, but my face still cramps sometimes when I get bigger!"

    show notte_gala focused smile1
    gnott "Well, just some tiny face stretches won't get in the way of walking!"

    show notte_gala relaxed frown1
    gnott "Just make sure my face is 'relaxed' and mouth is small (frown1)..."

    show notte_gala relaxed2 smile1
    gnott "And back we go!\n(relaxed2 smile1)"

    show notte_gala closed_relaxed2 gasp1
    gnott "Now close my eyes (closed_relaxed2) and shake my mouth (gasp1) before…"

    show notte_gala grumpy shout1
    gnott "HIYA!!\n(grumpy shout1)"

    show notte_gala closed_grumpy smile3
    gnott "Heh! Already hurting a bit less!\n(closed_grumpy smile3)"

    show notte_gala surprised frown2
    gnott "Oh! Maybe drooping my eyes in a fake cry and opening wide can help!\n(surprised frown2)"

    show notte_gala sad shout2
    gnott "WhooAAAAAA!! (sad) WIIIIIIDE!!! (shout2)"

    show notte_gala sad2 frown3
    gnott "Geez! Now my eyes (sad2) feel tired from all that! Mouth not doing so hot either (frown3)!"

    show notte_gala sad3 smile4
    gnott "But hey! That seemed to help with the cramps!\n(sad3 smile4)"

    show notte_gala shock smile5
    gnott "Alright! Now I'm ready for the day!\n(shock smile5)"

    show notte_gala relaxed3 shout2
    gnott "Oh! This looks like a nice store!\n(relaxed3)"

    show notte_gala sad4 smile2
    gnott "*gasp!* This clothing all looks sooooo pretty!\n(sad4 smile2)"

    show notte_gala sad3 closed_smile1
    gnott "*Aww man! So many in my size! And bigger too!*\n(closed_smile1)"

    show notte_gala sad3 closed_frown1
    gnott "*I feel like I'm about to go crazy just looking at it!*\n(closed_frown1)"

    show notte_gala squint pout1
    gnott "Alright, Notte. You know what to do.\n(squint pout1))"

    show notte_gala grumpy2 frown4
    gnott "You're gonna go in there, and show everyone that this girl is the boss!\n(grumpy2 frown4)"

    show notte_gala focused smile1
    gnott "Alright! Here we go! It's time for BIG me to shine!!\n(focused)"



    image clothing_shop = "images/backgrounds/Sty_bg_0061_100_00.png"
    scene clothing_shop with fade

    show notte_meta surprised frown1 with dissolve
    mnott "Sweet sassy molassy! They're even prettier in person!"

    show notte_meta focused frown1
    mnott "Alright, I shouldn't go TOO crazy. I just want maybe one or two.\n(focused frown1)"

    show notte_meta relaxed smile1
    mnott "Buuuuuuut~ nothing's stopping me from looking at them all first!\n(relaxed smile1)"

    show notte_meta relaxed2 smile2
    mnott "Ooooo! This one is nice! Really flowery!\n(relaxed2 smile2)"

    show notte_meta relaxed3 frown2
    mnott "Hmm.\n(relaxed3 frown2)"

    show notte_meta grumpy2 smile3
    mnott "Not any more flowery than mine!\n(grumpy2 smile3)"

    show notte_meta relaxed4 frown4
    mnott "Maybe I could get this one instead?\n(relaxed4 frown4)"

    show notte_meta surprised frown2
    mnott "Holy moly, is this one tight! So curvy and slinky! (surprised frown2)"

    show notte_meta grumpy2 smile4
    mnott "Heh… Imagine how they'll all react seeing me wear this! I'll be hotter than Mym!\n(grumpy2 smile4)"

    show notte_meta relaxed4 frown1
    mnott "Actually, nah. She already has this. I'll just ask her nicely!"

    show notte_meta focused smile3
    mnott "Or sneak it for myself. Whichever's easier."

    show notte_meta surprised shout2
    mnott "*gasp!* This one!\n(shout2)"

    show notte_meta sad smile3
    mnott "Those poofy sleeves! The perfect amount of flowers! Those beautiful pearls!\n(sad)"

    show notte_meta sad3 smile2
    mnott "Oh wow! I didn't even know that black was a good color on me!\n(sad3)"

    show notte_meta sad2 smile3
    mnott "Can't wait to bust this out at the ball!\n(sad2)"

    show notte_meta sad4 smile1
    mnott "Everyone will be so starstruck!\n(sad4)"

    show notte_meta closed_relaxed
    mnott "\"Oh, Notte! You have the coolest dress! Will you have this dance with me?\"\n(closed_relaxed)"

    show notte_meta closed_grumpy2 smile3
    mnott "And I can be all, \"Hmmph! Of course, sir or ma'am! Then after that, we can fill our bellies with fruit punch and cake and stuff!\"\n(closed_grumpy2)"

    show notte_meta closed_grumpy frown2
    mnott "And then Elly will be all, \"Oh~! A Paladyn shouldn't be so superficial, but I bet His Highness would love to go on a date with me wearing this!\"\n(closed_grumpy)"

    show notte_meta closed_relaxed2 smile1
    mnott "And I bet Euden would be all like, \"Hey, Notte! Cool dress! And look, you match with Zethia and I. Color buddies!\"\n(closed_relaxed2)"

    show notte_meta grumpy shout1
    mnott "...Oh…\n … I forgot to bring my wallet.\n(grumpy shout1)"

    show notte_meta frown3
    mnott "Or to even buy a wallet.\n(frown3)"

    show notte_meta squint pout1
    mnott "Hmmm…\n(squint pout1)"

    show notte_meta relaxed frown2
    mnott "Excuse me, do you have more like this somewhere?"

    show notte_meta relaxed frown3
    mnott "I'd love to ask my friends what they think."

    show notte_meta relaxed2 smile2
    mnott "You do? Oh, thanks a bunch!"

    show notte_meta relaxed gasp1
    mnott "I'll be back in a jiffy!\n(gasp1)"

    show notte_meta surprised closed_frown1
    mnott "*Phew! That was close!*\n(closed_frown1)"

    show notte_meta grumpy2 closed_smile1
    mnott "*I have to get Euden and Zethia to see!\n(closed_smile1)*"

    

    hide notte_meta with dissolve

    # This goes back to script

    jump testfiles