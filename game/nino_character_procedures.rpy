
    # Nino Character Procedures File

    # Paste this file into a story if you want to use Nino.  These procedures animate Nino as a speaker.
    # You'll also need to paste THIS line into your actual script above the script label whenever you're using Nino:

define nino = Character("Nino", callback=speaker("nino"))

    # This program assumes that the following folders exist:
    #     -"images/nino"
    #     -"images/nino/faces"
    #     -"images/nino/mouths"

    # Nino dynamically blinks and, while speaking, also moves her mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Nino appear*:
    #  -->  show nino_img with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Nino's eyes*:
    #  -->  show nino_img [keyword]
    #  List of eye keywords:
    #     --> neutral (default), focused, glare, pained, relaxed, sad, shocked, surprised,
    #         blush_askance, blush_angry, closed_neutral, closed_focused

    # *Changing Nino's mouth*:
    #  -->  show nino_img [keyword]
    #  List of mouth keywords:
    #     --> frown1 (default), frown2, frown3, grimace1, grimace2, mutter1, shout1, shout2,
    #          smile1, smile2, closed_frown1

    # *Writing dialogue for Nino*:
    #  --> nino "[Notte's line here]"

    # *Making Nino disappear*:
    #  --> hide nino_img with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage nino_img:

    group body:
        attribute normal default:
            "images/nino/nino_body.png"

        attribute wing:
            "images/nino/nino_body_wing.png"

    group face:

        # 447/1024, 198/1024:
        pos (0.43652, 0.193359)

        attribute neutral default:
            "nino_neutral_eyes"

        attribute closed_neutral:
            "images/nino/faces/110392_01_parts_c001.png"

        attribute focused:
            "nino_focused_eyes"

        attribute closed_focused:
            "images/nino/faces/110392_01_parts_c004.png"

        attribute relaxed:
            "nino_relaxed_eyes"

        attribute pained:
            "nino_pained_eyes"

        attribute surprised:
            "nino_surprised_eyes"

        attribute blush_askance:
            "nino_blush_askance_eyes"

        attribute sad:
            "nino_sad_eyes"

        attribute shocked:
            "nino_shocked_eyes"

        attribute blush_angry:
            "nino_blush_angry_eyes"

        attribute glare:
            "nino_glare_eyes"

    group mouth:

        pos (0.43652, 0.193359)

        attribute frown1 default:
            "nino_frown1"

        attribute closed_frown1:
            "nino_frown1_nottalking"

        attribute frown2:
            "nino_frown2"

        attribute smile1:
            "nino_smile1"

        attribute grimace1:
            "nino_grimace1"

        attribute frown3:
            "nino_frown3"

        attribute mutter1:
            "nino_mutter1"

        attribute smile2:
            "nino_smile2"

        attribute shout1:
            "nino_shout1"

        attribute shout2:
            "nino_shout2"

        attribute grimace2:
            "nino_grimace2"




## EYE animations start here.

image nino_neutral_eyes:
    "images/nino/faces/110392_01_parts_c000.png"
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
    "images/nino/faces/110392_01_parts_c001.png"
    0.05
    repeat

# 002 is the same as 000.  Deleted.

image nino_focused_eyes:
    "images/nino/faces/110392_01_parts_c003.png"
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
    "images/nino/faces/110392_01_parts_c004.png"
    0.05
    repeat

image nino_relaxed_eyes:
    "images/nino/faces/110392_01_parts_c010.png"
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
    "images/nino/faces/110392_01_parts_c011.png"
    0.05
    repeat

image nino_pained_eyes:
    "images/nino/faces/110392_01_parts_c012.png"
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
    "images/nino/faces/110392_01_parts_c013.png"
    0.05
    repeat

image nino_surprised_eyes:
    "images/nino/faces/110392_01_parts_c014.png"
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
    "images/nino/faces/110392_01_parts_c015.png"
    0.05
    repeat

image nino_blush_askance_eyes:
    "images/nino/faces/110392_01_parts_c016.png"
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
    "images/nino/faces/110392_01_parts_c017.png"
    0.05
    repeat

image nino_sad_eyes:
    "images/nino/faces/110392_01_parts_c026.png"
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
    "images/nino/faces/110392_01_parts_c027.png"
    0.05
    repeat

image nino_shocked_eyes:
    "images/nino/faces/110392_01_parts_c028.png"
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
    "images/nino/faces/110392_01_parts_c029.png"
    0.05
    repeat

image nino_blush_angry_eyes:
    "images/nino/faces/110392_01_parts_c036.png"
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
    "images/nino/faces/110392_01_parts_c037.png"
    0.05
    repeat

image nino_glare_eyes:
    "images/nino/faces/110392_01_parts_c038.png"
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
    "images/nino/faces/110392_01_parts_c039.png"
    0.05
    repeat



# MOUTH animations start here.

image nino_frown1_nottalking = "images/nino/mouths/110392_01_parts_c005.png"

image nino_frown1_talking:
    "images/nino/mouths/110392_01_parts_c006.png"
    0.15
    "images/nino/mouths/110392_01_parts_c005.png"
    0.15
    repeat

image nino_frown1 = WhileSpeaking("nino", "nino_frown1_talking", "nino_frown1_nottalking")


# 007 is the same as 005.  Deleted.


image nino_frown2_nottalking = "images/nino/mouths/110392_01_parts_c008.png"

image nino_frown2_talking:
    "images/nino/mouths/110392_01_parts_c009.png"
    0.15
    "images/nino/mouths/110392_01_parts_c008.png"
    0.15
    repeat

image nino_frown2 = WhileSpeaking("nino", "nino_frown2_talking", "nino_frown2_nottalking")


image nino_smile1_nottalking = "images/nino/mouths/110392_01_parts_c018.png"

image nino_smile1_talking:
    "images/nino/mouths/110392_01_parts_c019.png"
    0.15
    "images/nino/mouths/110392_01_parts_c018.png"
    0.15
    repeat

image nino_smile1 = WhileSpeaking("nino", "nino_smile1_talking", "nino_smile1_nottalking")


image nino_grimace1_nottalking = "images/nino/mouths/110392_01_parts_c020.png"

image nino_grimace1_talking:
    "images/nino/mouths/110392_01_parts_c021.png"
    0.15
    "images/nino/mouths/110392_01_parts_c020.png"
    0.15
    repeat

image nino_grimace1 = WhileSpeaking("nino", "nino_grimace1_talking", "nino_grimace1_nottalking")


image nino_frown3_nottalking = "images/nino/mouths/110392_01_parts_c022.png"

image nino_frown3_talking:
    "images/nino/mouths/110392_01_parts_c023.png"
    0.15
    "images/nino/mouths/110392_01_parts_c022.png"
    0.15
    repeat

image nino_frown3 = WhileSpeaking("nino", "nino_frown3_talking", "nino_frown3_nottalking")


image nino_mutter1_nottalking = "images/nino/mouths/110392_01_parts_c024.png"

image nino_mutter1_talking:
    "images/nino/mouths/110392_01_parts_c025.png"
    0.15
    "images/nino/mouths/110392_01_parts_c024.png"
    0.15
    repeat

image nino_mutter1 = WhileSpeaking("nino", "nino_mutter1_talking", "nino_mutter1_nottalking")


image nino_smile2_nottalking = "images/nino/mouths/110392_01_parts_c030.png"

image nino_smile2_talking:
    "images/nino/mouths/110392_01_parts_c031.png"
    0.15
    "images/nino/mouths/110392_01_parts_c030.png"
    0.15
    repeat

image nino_smile2 = WhileSpeaking("nino", "nino_smile2_talking", "nino_smile2_nottalking")


image nino_shout1_nottalking = "images/nino/mouths/110392_01_parts_c032.png"

image nino_shout1_talking:
    "images/nino/mouths/110392_01_parts_c033.png"
    0.15
    "images/nino/mouths/110392_01_parts_c032.png"
    0.15
    repeat

image nino_shout1 = WhileSpeaking("nino", "nino_shout1_talking", "nino_shout1_nottalking")


# 034 / 035 is the same as 005/006.  Deleted.


image nino_shout2_nottalking = "images/nino/mouths/110392_01_parts_c040.png"

image nino_shout2_talking:
    "images/nino/mouths/110392_01_parts_c041.png"
    0.15
    "images/nino/mouths/110392_01_parts_c040.png"
    0.15
    repeat

image nino_shout2 = WhileSpeaking("nino", "nino_shout2_talking", "nino_shout2_nottalking")


image nino_grimace2_nottalking = "images/nino/mouths/110392_01_parts_c042.png"

image nino_grimace2_talking:
    "images/nino/mouths/110392_01_parts_c043.png"
    0.15
    "images/nino/mouths/110392_01_parts_c042.png"
    0.15
    repeat

image nino_grimace2 = WhileSpeaking("nino", "nino_grimace2_talking", "nino_grimace2_nottalking")







# The game starts here.

label nino_character_procedures:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image field_day = "images/backgrounds/Sty_bg_0029_100_00.png"
    scene field_day

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show nino_img with dissolve
    nino "Oh, hello there."

    show nino_img neutral frown1
    nino "(neutral frown1) Testing!"

    show nino_img focused frown2
    nino "(focused frown2) Testing!"

    show nino_img relaxed smile1
    nino "(relaxed smile1) Testing!"

    show nino_img pained grimace1
    nino "(pained grimace1) Testing!"

    show nino_img surprised frown3
    nino "(surprised frown3) Testing!"

    show nino_img blush_askance mutter1
    nino "(blush_askance mutter1) Testing!"

    show nino_img sad smile2
    nino "(sad smile2) Testing!"

    show nino_img shocked shout1
    nino "(shocked shout1) Testing!"

    show nino_img blush_angry shout2
    nino "(blush_angry shout2) Testing!"

    show nino_img glare grimace2
    nino "(glare grimace2) Testing!"



    show nino_img closed_neutral closed_frown1
    nino "(closed_frown1) my lips shouldn't be moving now"

    show nino_img closed_focused closed_frown1
    nino "(closed_frown1) my lips shouldn't be moving now"

    hide nino_img with dissolve


    # This goes back to script

    jump testfiles
