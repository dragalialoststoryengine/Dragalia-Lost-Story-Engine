
    # Gala Euden Character Procedures File

    # Paste this file into a story if you want to use Gala Euden.  These procedures animate Gala Euden as a speaker.
    # You'll also need to paste THIS line into your actual script above the script label whenever you're using Gala Euden:

define geud = Character("Euden", callback=speaker("geud"))

    # This program assumes that the following folders exist:
    #     -"images/euden_gala"
    #     -"images/euden_gala/faces"
    #     -"images/euden_gala/mouths"
    #     -"images/euden_gala/faces_normal"
    #     -"images/euden_gala/mouths_normal"

    # Gala Euden dynamically blinks and, while speaking, also moves her mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Gala Euden appear*:
    #  -->  show geuden with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Gala Euden's eyes*:
    #  -->  show geuden [keyword]
    #  List of eye keywords:
    #     -->  focused (default), focused2, closed_focused, angry, closed_angry,
    #          angry2, closed_angry2, flinch, relaxed, closed_relaxed, sad,
    #          closed_sad, sweat, pained, broken

    # *Changing Gala Euden's mouth*:
    #  -->  show geuden [keyword]
    #  List of mouth keywords:
    #     -->  frown1 (default), frown2, frown3, frown4, frown5, frown6, frown7,
    #          frown3, grin1, shout1, smile1

    # *Writing dialogue for Gala Euden*:
    #  --> geud "[Gala Euden's line here]"

    # *Making Gala Euden disappear*:
    #  --> hide geuden with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage geuden:

    always "images/euden_gala/euden_gala_body.png"

    group face:

        # 469/1024, 236/1024:
        pos (0.45801, 0.23046)

        attribute focused default:
            "geuden_focused_eyes"

        attribute closed_focused:
            "images/euden_gala/faces/100001_08_parts_c001.png"

        attribute relaxed:
            "geuden_relaxed_eyes"

        attribute closed_relaxed:
            "images/euden_gala/faces/100001_08_parts_c011.png"

        attribute flinch:
            "geuden_flinch_eyes"

        attribute sweat:
            "geuden_sweat_eyes"

        attribute focused2:
            "geuden_focused2_eyes"

        attribute angry:
            "geuden_angry_eyes"

        attribute closed_angry:
            "images/euden_gala/faces/100001_08_parts_c004.png"

        attribute angry2:
            "geuden_angry2_eyes"

        attribute closed_angry2:
            "images/euden_gala/faces/100001_08_parts_c029.png"

        attribute sad:
            "geuden_sad_eyes"

        attribute closed_sad:
            "images/euden_gala/faces/100001_08_parts_c017.png"

        attribute pained:
            "geuden_pained_eyes"

        attribute broken:
            "geuden_broken_eyes"

    group mouth:

        pos (0.45801, 0.23046)

        attribute frown1 default:
            "geuden_frown1"

        attribute frown2:
            "geuden_frown2"

        attribute smile1:
            "geuden_smile1"

        attribute grimace1:
            "geuden_grimace1"

        attribute frown3:
            "geuden_frown3"

        attribute grin1:
            "geuden_grin1"

        attribute frown4:
            "geuden_frown4"

        attribute shout1:
            "geuden_shout1"

        attribute frown5:
            "geuden_frown5"

        attribute frown6:
            "geuden_frown6"

        attribute frown7:
            "geuden_frown7"



## EYE animations start here.

image geuden_focused_eyes:
    "images/euden_gala/faces/100001_08_parts_c000.png"
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
    "images/euden_gala/faces/100001_08_parts_c001.png"
    0.05
    repeat

image geuden_relaxed_eyes:
    "images/euden_gala/faces/100001_08_parts_c010.png"
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
    "images/euden_gala/faces/100001_08_parts_c011.png"
    0.05
    repeat

image geuden_flinch_eyes:
    "images/euden_gala/faces/100001_08_parts_c012.png"
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
    "images/euden_gala/faces/100001_08_parts_c013.png"
    0.05
    repeat

image geuden_sweat_eyes:
    "images/euden_gala/faces/100001_08_parts_c014.png"
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
    "images/euden_gala/faces/100001_08_parts_c015.png"
    0.05
    repeat

image geuden_focused2_eyes:
    "images/euden_gala/faces/100001_08_parts_c037.png"
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
    "images/euden_gala/faces/100001_08_parts_c030.png"
    0.05
    repeat

image geuden_angry_eyes:
    "images/euden_gala/faces/100001_08_parts_c003.png"
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
    "images/euden_gala/faces/100001_08_parts_c004.png"
    0.05
    repeat

image geuden_angry2_eyes:
    "images/euden_gala/faces/100001_08_parts_c028.png"
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
    "images/euden_gala/faces/100001_08_parts_c029.png"
    0.05
    repeat

image geuden_sad_eyes:
    "images/euden_gala/faces/100001_08_parts_c016.png"
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
    "images/euden_gala/faces/100001_08_parts_c017.png"
    0.05
    repeat

image geuden_pained_eyes:
    "images/euden_gala/faces/100001_08_parts_c026.png"
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
    "images/euden_gala/faces/100001_08_parts_c027.png"
    0.05
    repeat

image geuden_broken_eyes:
    "images/euden_gala/faces/100001_08_parts_c038.png"
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
    "images/euden_gala/faces/100001_08_parts_c039.png"
    0.05
    repeat



# MOUTH animations start here.

image geuden_frown1_nottalking = "images/euden_gala/mouths/100001_08_parts_c005.png"

image geuden_frown1_talking:
    "images/euden_gala/mouths/100001_08_parts_c006.png"
    0.15
    "images/euden_gala/mouths/100001_08_parts_c005.png"
    0.15
    repeat

image geuden_frown1 = WhileSpeaking("geud", "geuden_frown1_talking", "geuden_frown1_nottalking")


# 005 is the same as 007.


image geuden_frown2_nottalking = "images/euden_gala/mouths/100001_08_parts_c008.png"

image geuden_frown2_talking:
    "images/euden_gala/mouths/100001_08_parts_c009.png"
    0.15
    "images/euden_gala/mouths/100001_08_parts_c008.png"
    0.15
    repeat

image geuden_frown2 = WhileSpeaking("geud", "geuden_frown2_talking", "geuden_frown2_nottalking")


image geuden_smile1_nottalking = "images/euden_gala/mouths/100001_08_parts_c018.png"

image geuden_smile1_talking:
    "images/euden_gala/mouths/100001_08_parts_c019.png"
    0.15
    "images/euden_gala/mouths/100001_08_parts_c018.png"
    0.15
    repeat

image geuden_smile1 = WhileSpeaking("geud", "geuden_smile1_talking", "geuden_smile1_nottalking")


image geuden_grimace1_nottalking = "images/euden_gala/mouths/100001_08_parts_c020.png"

image geuden_grimace1_talking:
    "images/euden_gala/mouths/100001_08_parts_c021.png"
    0.15
    "images/euden_gala/mouths/100001_08_parts_c020.png"
    0.15
    repeat

image geuden_grimace1 = WhileSpeaking("geud", "geuden_grimace1_talking", "geuden_grimace1_nottalking")


image geuden_frown3_nottalking = "images/euden_gala/mouths/100001_08_parts_c022.png"

image geuden_frown3_talking:
    "images/euden_gala/mouths/100001_08_parts_c023.png"
    0.15
    "images/euden_gala/mouths/100001_08_parts_c022.png"
    0.15
    repeat

image geuden_frown3 = WhileSpeaking("geud", "geuden_frown3_talking", "geuden_frown3_nottalking")


image geuden_grin1_nottalking = "images/euden_gala/mouths/100001_08_parts_c024.png"

image geuden_grin1_talking:
    "images/euden_gala/mouths/100001_08_parts_c025.png"
    0.15
    "images/euden_gala/mouths/100001_08_parts_c024.png"
    0.15
    repeat

image geuden_grin1 = WhileSpeaking("geud", "geuden_grin1_talking", "geuden_grin1_nottalking")


image geuden_frown4_nottalking = "images/euden_gala/mouths/100001_08_parts_c031.png"

image geuden_frown4_talking:
    "images/euden_gala/mouths/100001_08_parts_c032.png"
    0.15
    "images/euden_gala/mouths/100001_08_parts_c031.png"
    0.15
    repeat

image geuden_frown4 = WhileSpeaking("geud", "geuden_frown4_talking", "geuden_frown4_nottalking")


image geuden_shout1_nottalking = "images/euden_gala/mouths/100001_08_parts_c033.png"

image geuden_shout1_talking:
    "images/euden_gala/mouths/100001_08_parts_c034.png"
    0.15
    "images/euden_gala/mouths/100001_08_parts_c033.png"
    0.15
    repeat

image geuden_shout1 = WhileSpeaking("geud", "geuden_shout1_talking", "geuden_shout1_nottalking")


image geuden_frown5_nottalking = "images/euden_gala/mouths/100001_08_parts_c035.png"

image geuden_frown5_talking:
    "images/euden_gala/mouths/100001_08_parts_c036.png"
    0.15
    "images/euden_gala/mouths/100001_08_parts_c035.png"
    0.15
    repeat

image geuden_frown5 = WhileSpeaking("geud", "geuden_frown4_talking", "geuden_frown4_nottalking")


image geuden_frown6_nottalking = "images/euden_gala/mouths/100001_08_parts_c040.png"

image geuden_frown6_talking:
    "images/euden_gala/mouths/100001_08_parts_c041.png"
    0.15
    "images/euden_gala/mouths/100001_08_parts_c040.png"
    0.15
    repeat

image geuden_frown6 = WhileSpeaking("geud", "geuden_frown4_talking", "geuden_frown4_nottalking")


image geuden_frown7_nottalking = "images/euden_gala/mouths/100001_08_parts_c042.png"

image geuden_frown7_talking:
    "images/euden_gala/mouths/100001_08_parts_c043.png"
    0.15
    "images/euden_gala/mouths/100001_08_parts_c042.png"
    0.15
    repeat

image geuden_frown7 = WhileSpeaking("geud", "geuden_frown4_talking", "geuden_frown4_nottalking")


    # *Making Gala Euden appear with her normal*:
    #  -->  show geuden_normal with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Gala Euden's (normal) eyes*:
    #  -->  show geuden_normal [keyword]
    #  List of eye keywords:
    #     -->  focused (default), focused2, closed_focused, closed_focused2, relaxed,
    #          relaxed2, closed_relaxed, flinch, angry, angry2, closed_angry, closed_angry2,
    #          surprised, blush, closed_blush, surprised_blush, closed_surprised_blush, sad,
    #          closed_sad, pained, closed_pained, broken, evil_focused, evil_rage

    # *Changing Gala Euden's (normal) mouth*:
    #  -->  show geuden_normal [keyword]
    #  List of mouth keywords:
    #     -->  smile1 (default), smile2, smile3, smile4, smile5, smile6, frown1, frown2, frown3,
    #          frown4, mumble1, sweat_frown1, shout1, contempt1, evil_murmur1, evil_sneer1

    # *Writing dialogue for Gala Euden (normal)*:
    #  --> geuden "[Gala Euden's line here]"

    # *Making Gala Euden (normal) disappear*:
    #  --> hide geuden_normal with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




layeredimage geuden_normal:

    always "images/euden_gala/euden_gala_body_normal.png"

    group face:

        # 444/1024, 231/1024
        pos (0.43359, 0.22559)

        attribute focused default:
            "geuden_normal_focused_eyes"

        attribute focused2:
            "geuden_normal_focused2_eyes"

        attribute closed_focused:
            "images/euden_gala/faces_normal/100001_09_parts_c001.png"

        attribute closed_focused2:
            "images/euden_gala/faces_normal/100001_09_parts_c0036.png"

        attribute relaxed:
            "geuden_normal_relaxed_eyes"

        attribute relaxed2:
            "geuden_normal_relaxed2_eyes"

        attribute closed_relaxed:
            "images/euden_gala/faces_normal/100001_09_parts_c014.png"

        attribute flinch:
            "geuden_normal_flinch_eyes"

        attribute angry:
            "geuden_normal_angry_eyes"

        attribute angry2:
            "geuden_normal_angry2_eyes"

        attribute closed_angry:
            "images/euden_gala/faces_normal/100001_09_parts_c030.png"

        attribute closed_angry2:
            "images/euden_gala/faces_normal/100001_09_parts_c034.png"

        attribute surprised:
            "geuden_normal_surprised_eyes"

        attribute blush:
            "geuden_normal_blush_eyes"

        attribute closed_blush:
            "images/euden_gala/faces_normal/100001_09_parts_c032.png"

        attribute surprised_blush:
            "geuden_normal_surprised_blush_eyes"

        attribute closed_surprised_blush:
            "images/euden_gala/faces_normal/100001_09_parts_c020.png"

        attribute sad:
            "geuden_normal_sad_eyes"

        attribute closed_sad:
            "images/euden_gala/faces_normal/100001_09_parts_c044.png"

        attribute pained:
            "geuden_normal_pained_eyes"
        
        attribute closed_pained:
            "images/euden_gala/faces_normal/100001_09_parts_c048.png"

        attribute broken:
            "geuden_normal_broken_eyes"

        attribute evil_focused:
            "geuden_normal_evil_focused"

        attribute closed_evil_focused:
            "images/euden_gala/faces_normal/100001_10_parts_c001.png"

        attribute evil_rage:
            "geuden_normal_evil_rage"

        attribute closed_evil_rage:
            "images/euden_gala/faces_normal/100001_10_parts_c008.png"


    group mouth:

        pos (0.43359, 0.22559)

        attribute smile1 default:
            "geuden_normal_smile1"

        attribute smile2:
            "geuden_normal_smile2"

        attribute smile3:
            "geuden_normal_smile3"

        attribute smile4:
            "geuden_normal_smile4"
        
        attribute smile5:
            "geuden_normal_smile5"

        attribute smile6:
            "geuden_normal_smile6"

        attribute frown1:
            "geuden_normal_frown1"

        attribute frown2:
            "geuden_normal_frown2"

        attribute frown3:
            "geuden_normal_frown3"

        attribute frown4:
            "geuden_normal_frown4"

        attribute mumble1:
            "geuden_normal_mumble1"

        attribute sweat_frown1:
            "geuden_normal_sweat_frown1"

        attribute shout1:
            "geuden_normal_shout1"

        attribute contempt1:
            "geuden_normal_contempt1"

        attribute evil_murmur1:
            "geuden_normal_evil_murmur1"

        attribute evil_sneer1:
            "geuden_normal_evil_sneer1"


## EYE animations start here.

image geuden_normal_focused_eyes:
    "images/euden_gala/faces_normal/100001_09_parts_c000.png"
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
    "images/euden_gala/faces_normal/100001_09_parts_c001.png"
    0.05
    repeat

# 000 and 001 are the same as 035 and 036.

image geuden_normal_focused2_eyes:
    "images/euden_gala/faces_normal/100001_09_parts_c004.png"
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
    "images/euden_gala/faces_normal/100001_09_parts_c005.png"
    0.05
    repeat

image geuden_normal_relaxed_eyes:
    "images/euden_gala/faces_normal/100001_09_parts_c013.png"
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
    "images/euden_gala/faces_normal/100001_09_parts_c014.png"
    0.05
    repeat

image geuden_normal_relaxed2_eyes:
    "images/euden_gala/faces_normal/100001_09_parts_c045.png"
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
    "images/euden_gala/faces_normal/100001_09_parts_c046.png"
    0.05
    repeat

image geuden_normal_sad_eyes:
    "images/euden_gala/faces_normal/100001_09_parts_c043.png"
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
    "images/euden_gala/faces_normal/100001_09_parts_c044.png"
    0.05
    repeat

image geuden_normal_angry_eyes:
    "images/euden_gala/faces_normal/100001_09_parts_c029.png"
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
    "images/euden_gala/faces_normal/100001_09_parts_c030.png"
    0.05
    repeat

image geuden_normal_angry2_eyes:
    "images/euden_gala/faces_normal/100001_09_parts_c033.png"
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
    "images/euden_gala/faces_normal/100001_09_parts_c034.png"
    0.05
    repeat

image geuden_normal_surprised_eyes:
    "images/euden_gala/faces_normal/100001_09_parts_c017.png"
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
    "images/euden_gala/faces_normal/100001_09_parts_c018.png"
    0.05
    repeat

image geuden_normal_blush_eyes:
    "images/euden_gala/faces_normal/100001_09_parts_c031.png"
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
    "images/euden_gala/faces_normal/100001_09_parts_c032.png"
    0.05
    repeat

image geuden_normal_surprised_blush_eyes:
    "images/euden_gala/faces_normal/100001_09_parts_c019.png"
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
    "images/euden_gala/faces_normal/100001_09_parts_c020.png"
    0.05
    repeat

image geuden_normal_flinch_eyes:
    "images/euden_gala/faces_normal/100001_09_parts_c015.png"
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
    "images/euden_gala/faces_normal/100001_09_parts_c016.png"
    0.05
    repeat

image geuden_normal_pained_eyes:
    "images/euden_gala/faces_normal/100001_09_parts_c047.png"
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
    "images/euden_gala/faces_normal/100001_09_parts_c048.png"
    0.05
    repeat

image geuden_normal_broken_eyes:
    "images/euden_gala/faces_normal/100001_09_parts_c002.png"
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
    "images/euden_gala/faces_normal/100001_09_parts_c003.png"
    0.05
    repeat

image geuden_normal_smirk_eyes:
    "images/euden_gala/faces_normal/100001_09_parts_c049.png"
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
    "images/euden_gala/faces_normal/100001_09_parts_c050.png"
    0.05
    repeat

image geuden_normal_evil_focused:
    "images/euden_gala/faces_normal/100001_10_parts_c000.png"
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
    "images/euden_gala/faces_normal/100001_10_parts_c001.png"
    0.05
    repeat

image geuden_normal_evil_rage:
    "images/euden_gala/faces_normal/100001_10_parts_c007.png"
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
    "images/euden_gala/faces_normal/100001_10_parts_c008.png"
    0.05
    repeat




# MOUTH animations start here.

image geuden_normal_smile1_nottalking = "images/euden_gala/mouths_normal/100001_09_parts_c006.png"

image geuden_normal_smile1_talking:
    "images/euden_gala/mouths_normal/100001_09_parts_c007.png"
    0.15
    "images/euden_gala/mouths_normal/100001_09_parts_c006.png"
    0.15
    repeat

image geuden_normal_smile1 = WhileSpeaking("geud", "geuden_normal_smile1_talking", "geuden_normal_smile1_nottalking")


image geuden_normal_smile2_nottalking = "images/euden_gala/mouths_normal/100001_09_parts_c021.png"

image geuden_normal_smile2_talking:
    "images/euden_gala/mouths_normal/100001_09_parts_c022.png"
    0.15
    "images/euden_gala/mouths_normal/100001_09_parts_c021.png"
    0.15
    repeat

image geuden_normal_smile2 = WhileSpeaking("geud", "geuden_normal_smile2_talking", "geuden_normal_smile2_nottalking")


image geuden_normal_smile3_nottalking = "images/euden_gala/mouths_normal/100001_09_parts_c039.png"

image geuden_normal_smile3_talking:
    "images/euden_gala/mouths_normal/100001_09_parts_c040.png"
    0.15
    "images/euden_gala/mouths_normal/100001_09_parts_c039.png"
    0.15
    repeat

image geuden_normal_smile3 = WhileSpeaking("geud", "geuden_normal_smile3_talking", "geuden_normal_smile3_nottalking")


image geuden_normal_smile4_nottalking = "images/euden_gala/mouths_normal/100001_09_parts_c051.png"

image geuden_normal_smile4_talking:
    "images/euden_gala/mouths_normal/100001_09_parts_c052.png"
    0.15
    "images/euden_gala/mouths_normal/100001_09_parts_c051.png"
    0.15
    repeat

image geuden_normal_smile4 = WhileSpeaking("geud", "geuden_normal_smile4_talking", "geuden_normal_smile4_nottalking")


image geuden_normal_smile5_nottalking = "images/euden_gala/mouths_normal/100001_09_parts_c053.png"

image geuden_normal_smile5_talking:
    "images/euden_gala/mouths_normal/100001_09_parts_c054.png"
    0.15
    "images/euden_gala/mouths_normal/100001_09_parts_c053.png"
    0.15
    repeat

image geuden_normal_smile5 = WhileSpeaking("geud", "geuden_normal_smile5_talking", "geuden_normal_smile5_nottalking")


image geuden_normal_smile6_nottalking = "images/euden_gala/mouths_normal/100001_09_parts_c057.png"

image geuden_normal_smile6_talking:
    "images/euden_gala/mouths_normal/100001_09_parts_c058.png"
    0.15
    "images/euden_gala/mouths_normal/100001_09_parts_c057.png"
    0.15
    repeat

image geuden_normal_smile6 = WhileSpeaking("geud", "geuden_normal_smile6_talking", "geuden_normal_smile6_nottalking")


image geuden_normal_frown1_nottalking = "images/euden_gala/mouths_normal/100001_09_parts_c009.png"

image geuden_normal_frown1_talking:
    "images/euden_gala/mouths_normal/100001_09_parts_c010.png"
    0.15
    "images/euden_gala/mouths_normal/100001_09_parts_c009.png"
    0.15
    repeat

image geuden_normal_frown1 = WhileSpeaking("geud", "geuden_normal_frown1_talking", "geuden_normal_frown1_nottalking")


image geuden_normal_frown2_nottalking = "images/euden_gala/mouths_normal/100001_09_parts_c011.png"

image geuden_normal_frown2_talking:
    "images/euden_gala/mouths_normal/100001_09_parts_c012.png"
    0.15
    "images/euden_gala/mouths_normal/100001_09_parts_c011.png"
    0.15
    repeat

image geuden_normal_frown2 = WhileSpeaking("geud", "geuden_normal_frown2_talking", "geuden_normal_frown2_nottalking")


image geuden_normal_frown3_nottalking = "images/euden_gala/mouths_normal/100001_09_parts_c027.png"

image geuden_normal_frown3_talking:
    "images/euden_gala/mouths_normal/100001_09_parts_c028.png"
    0.15
    "images/euden_gala/mouths_normal/100001_09_parts_c027.png"
    0.15
    repeat

image geuden_normal_frown3 = WhileSpeaking("geud", "geuden_normal_frown3_talking", "geuden_normal_frown3_nottalking")


image geuden_normal_frown4_nottalking = "images/euden_gala/mouths_normal/100001_09_parts_c037.png"

image geuden_normal_frown4_talking:
    "images/euden_gala/mouths_normal/100001_09_parts_c038.png"
    0.15
    "images/euden_gala/mouths_normal/100001_09_parts_c037.png"
    0.15
    repeat

image geuden_normal_frown4 = WhileSpeaking("geud", "geuden_normal_frown4_talking", "geuden_normal_frown4_nottalking")


image geuden_normal_mumble1_nottalking = "images/euden_gala/mouths_normal/100001_09_parts_c055.png"

image geuden_normal_mumble1_talking:
    "images/euden_gala/mouths_normal/100001_09_parts_c056.png"
    0.15
    "images/euden_gala/mouths_normal/100001_09_parts_c055.png"
    0.15
    repeat

image geuden_normal_mumble1 = WhileSpeaking("geud", "geuden_normal_mumble1_talking", "geuden_normal_mumble1_nottalking")


image geuden_normal_sweat_frown1_nottalking = "images/euden_gala/mouths_normal/100001_09_parts_c025.png"

image geuden_normal_sweat_frown1_talking:
    "images/euden_gala/mouths_normal/100001_09_parts_c026.png"
    0.15
    "images/euden_gala/mouths_normal/100001_09_parts_c025.png"
    0.15
    repeat

image geuden_normal_sweat_frown1 = WhileSpeaking("geud", "geuden_normal_sweat_frown1_talking", "geuden_normal_sweat_frown1_nottalking")


image geuden_normal_shout1_nottalking = "images/euden_gala/mouths_normal/100001_09_parts_c041.png"

image geuden_normal_shout1_talking:
    "images/euden_gala/mouths_normal/100001_09_parts_c042.png"
    0.15
    "images/euden_gala/mouths_normal/100001_09_parts_c041.png"
    0.15
    repeat

image geuden_normal_shout1 = WhileSpeaking("geud", "geuden_normal_shout1_talking", "geuden_normal_shout1_nottalking")


image geuden_normal_contempt1_nottalking = "images/euden_gala/mouths_normal/100001_09_parts_c023.png"

image geuden_normal_contempt1_talking:
    "images/euden_gala/mouths_normal/100001_09_parts_c024.png"
    0.15
    "images/euden_gala/mouths_normal/100001_09_parts_c023.png"
    0.15
    repeat

image geuden_normal_contempt1 = WhileSpeaking("geud", "geuden_normal_contempt1_talking", "geuden_normal_contempt1_nottalking")


image geuden_normal_evil_murmur1_nottalking = "images/euden_gala/mouths_normal/100001_10_parts_c004.png"

image geuden_normal_evil_murmur1_talking:
    "images/euden_gala/mouths_normal/100001_10_parts_c005.png"
    0.15
    "images/euden_gala/mouths_normal/100001_10_parts_c004.png"
    0.15
    repeat

image geuden_normal_evil_murmur1 = WhileSpeaking("geud", "geuden_normal_evil_murmur1_talking", "geuden_normal_evil_murmur1_nottalking")


image geuden_normal_evil_sneer1_nottalking = "images/euden_gala/mouths_normal/100001_10_parts_c009.png"

image geuden_normal_evil_sneer1_talking:
    "images/euden_gala/mouths_normal/100001_10_parts_c010.png"
    0.15
    "images/euden_gala/mouths_normal/100001_10_parts_c009.png"
    0.15
    repeat

image geuden_normal_evil_sneer1 = WhileSpeaking("geud", "geuden_normal_evil_sneer1_talking", "geuden_normal_evil_sneer1_nottalking")









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

label eudenG_character_procedures:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image castle_exterior = "images/backgrounds/Sty_bg_0017_100_00.png"
    scene castle_exterior

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    show geuden with dissolve
    geud "..."

    show geuden relaxed
    geud "Hmm?"

    show geuden smile1
    geud "Oh, hey again! Nice seeing you drop by!"
    geud "Thanks for checking on my 'files' for if they're working."

    show geuden frown1
    geud "I should probably warn you that I have a lot more expressions than normal."
    geud "Hopefully it's not too much of a bother for you."

    show geuden focused frown1
    geud "This is the 'focused' face and 'frown1' mouth."

    show geuden relaxed frown2
    geud "This is the 'relaxed' face and 'frown2' mouth."

    show geuden flinch smile1
    geud "This is the 'flinch' face and 'smile1' mouth."

    show geuden sweat grimace1
    geud "This is the 'sweat' face and 'grimace1' mouth."

    show geuden focused2 frown3
    geud "This is the 'focused2' face and 'frown3' mouth."

    show geuden angry grin1
    geud "This is the 'angry' face and 'grin1' mouth."

    show geuden angry2 frown4
    geud "This is the 'angry2' face and 'frown4' mouth."

    show geuden sad shout1
    geud "This is the 'sad' face and 'shout1' mouth."

    show geuden pained frown5
    geud "This is the 'pained' face and 'frown5' mouth."

    show geuden broken frown6
    geud "This is the 'broken' face and 'frown6' mouth."

    show geuden relaxed frown7
    geud "I also have this 'frown7' mouth."

    show geuden sad frown1
    geud "Sorry if I seem a bit more upset at things angle."

    hide geuden
    show geuden_normal relaxed frown1
    geud "How about this angle?"

    show geuden_normal focused smile1
    geud "This is the 'focused' face and 'smile1' mouth."

    show geuden_normal focused2 smile2
    geud "This is the 'focused2' face and 'smile2' mouth."

    show geuden_normal relaxed smile3
    geud "This is the 'relaxed' face and 'smile3' mouth."

    show geuden_normal relaxed2 smile4
    geud "This is the 'relaxed2' face and 'smile4' mouth."

    show geuden_normal flinch smile5
    geud "This is the 'flinch' face and 'smile5' mouth."

    show geuden_normal angry smile6
    geud "This is the 'angry' face and 'smile6' mouth."

    show geuden_normal angry2 frown1
    geud "This is the 'angry2' face and 'frown1' mouth."

    show geuden_normal surprised frown2
    geud "This is the 'surprised' face and 'frown2' mouth."

    show geuden_normal blush frown3
    geud "This is the 'blush' face and 'frown3' mouth."

    show geuden_normal surprised_blush frown4
    geud "This is the 'surprised_blush' face and 'frown4' mouth."

    show geuden_normal sad mumble1
    geud "This is the 'sad' face and 'mumble1' mouth."

    show geuden_normal pained sweat_frown1
    geud "This is the 'pained' face and 'sweat_frown1' mouth."

    show geuden_normal broken shout1
    geud "This is the 'broken' face and 'shout1' mouth."

    show geuden_normal angry contempt1
    geud "That doesn't mean I can't be upset at someone ('contempt1') at this angle if my friends are threatened."

    show geuden_normal relaxed sweat_frown1
    geud "Hmm?"
    geud "You want to see my \"evil\" face?"
    geud "I think I have some contacts...\nHold on..."

    show geuden_normal closed_focused frown2
    geud "..."

    show geuden_normal evil_focused evil_sneer1
    geud "Mwahahaha! I am evil and such!\n('evil_focused' and 'evil_sneer1')"

    show geuden_normal evil_rage evil_murmur1
    geud "I will get you and your little dog too!\n('evil_rage' and 'evil_murmur')"

    show geuden_normal relaxed frown3
    geud "Was that good?"

    show geuden_normal relaxed smile1
    geud "That's great! I'm glad you're here to help us!"

    show geuden_normal closed_relaxed
    geud "Thanks again!"


    hide geuden_normal with dissolve

    # This goes back to script

    jump testfiles
