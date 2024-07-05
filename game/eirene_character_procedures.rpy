
    # Eirene Character Procedures File

    # Paste this file into a story if you want to use Eirene.  These procedures animate Eirene as a speaker.
    # You'll also need to paste THIS line into your actual script above the script label whenever you're using Eirene:

define eir = Character("Eirene", callback=speaker("eir"))

    # This program assumes that the following folders exist:
    #     -"images/eirene"
    #     -"images/eirene/faces"
    #     -"images/eirene/mouths"

    # Eirene dynamically blinks and, while speaking, also moves her mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Eirene appear*:
    #  -->  show eirene with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Eirene's eyes*:
    #  -->  show eirene [keyword]
    #  List of eye keywords:
    #     -->  neutral (the default option), closed_neutral, angry, glow_angry, dull,
    #          focused, glow_focused, injured, closed_injured, pained, relaxed, sad, surprised

    # *Changing Eirene's mouth*:
    #  -->  show eirene [keyword]
    #  List of mouth keywords:
    #     -->  mutter1 (the default option), mutter2, frown1, frown2,
    #          grimace1, grimace2, shout1, smile1

    # *Writing dialogue for Eirene*:
    #  --> eir "[Eirene's line here]"

    # *Making Eirene disappear*:
    #  --> hide eirene with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage eirene:

    always "images/eirene/eirene_body.png"

    group face:

        # 478/1028, 266/1028:

        #adjust to 480/1028, 268/1028
        pos (0.466926, 0.26070)

        attribute neutral default:
            "eirene_relaxed_eyes"

        attribute closed_neutral:
            "images/eirene/faces/110384_01_parts_c001.png"

        attribute focused:
            "eirene_focused_eyes"

        attribute relaxed:
            "eirene_relaxed_eyes"

        attribute pained:
            "eirene_pained_eyes"

        attribute surprised:
            "eirene_surprised_eyes"

        attribute injured:
            "eirene_injured_eyes"

        attribute closed_injured:
            "images/eirene/faces/110384_01_parts_c018.png"

        attribute sad:
            "eirene_sad_eyes"

        attribute angry:
            "eirene_angry_eyes"

        attribute glow_focused:
            "eirene_glow_focused_eyes"

        attribute glow_angry:
            "eirene_glow_angry_eyes"

        attribute dull:
            "eirene_dull_eyes"

    group mouth:

        pos (0.466926, 0.26070)

        attribute mutter1 default:
            "eirene_mutter1"

        attribute frown1:
            "eirene_frown1"

        attribute smile1:
            "eirene_smile1"

        attribute grimace1:
            "eirene_grimace1"

        attribute frown2:
            "eirene_frown2"

        attribute mutter2:
            "eirene_mutter2"

        attribute grimace2:
            "eirene_grimace2"

        attribute shout1:
            "eirene_shout1"


layeredimage eirene_crop:

    always "images/eirene/eirene_body_crop.png"

    group face:

        # 478/1028, 266/1028:

        # Now 338/1028, 113/1028
        # Adjust to 340/1028, 114/1028
        pos (0.33074, 0.11089)

        attribute neutral default:
            "eirene_relaxed_eyes"

        attribute closed_neutral:
            "images/eirene/faces/110384_01_parts_c001.png"

        attribute focused:
            "eirene_focused_eyes"

        attribute relaxed:
            "eirene_relaxed_eyes"

        attribute pained:
            "eirene_pained_eyes"

        attribute surprised:
            "eirene_surprised_eyes"

        attribute injured:
            "eirene_injured_eyes"

        attribute closed_injured:
            "images/eirene/faces/110384_01_parts_c018.png"

        attribute sad:
            "eirene_sad_eyes"

        attribute angry:
            "eirene_angry_eyes"

        attribute glow_focused:
            "eirene_glow_focused_eyes"

        attribute glow_angry:
            "eirene_glow_angry_eyes"

        attribute dull:
            "eirene_dull_eyes"

    group mouth:

        pos (0.33074, 0.11089)

        attribute mutter1 default:
            "eirene_mutter1"

        attribute frown1:
            "eirene_frown1"

        attribute smile1:
            "eirene_smile1"

        attribute grimace1:
            "eirene_grimace1"

        attribute frown2:
            "eirene_frown2"

        attribute mutter2:
            "eirene_mutter2"

        attribute grimace2:
            "eirene_grimace2"

        attribute shout1:
            "eirene_shout1"



## EYE animations start here.

image eirene_neutral_eyes:
    "images/eirene/faces/110384_01_parts_c000.png"
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
    "images/eirene/faces/110384_01_parts_c001.png"
    0.05
    repeat

image eirene_focused_eyes:
    "images/eirene/faces/110384_01_parts_c002.png"
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
    "images/eirene/faces/110384_01_parts_c003.png"
    0.05
    repeat

image eirene_relaxed_eyes:
    "images/eirene/faces/110384_01_parts_c011.png"
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
    "images/eirene/faces/110384_01_parts_c012.png"
    0.05
    repeat

image eirene_pained_eyes:
    "images/eirene/faces/110384_01_parts_c013.png"
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
    "images/eirene/faces/110384_01_parts_c014.png"
    0.05
    repeat

image eirene_surprised_eyes:
    "images/eirene/faces/110384_01_parts_c015.png"
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
    "images/eirene/faces/110384_01_parts_c016.png"
    0.05
    repeat

image eirene_injured_eyes:
    "images/eirene/faces/110384_01_parts_c017.png"
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
    "images/eirene/faces/110384_01_parts_c018.png"
    0.05
    repeat

image eirene_sad_eyes:
    "images/eirene/faces/110384_01_parts_c027.png"
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
    "images/eirene/faces/110384_01_parts_c028.png"
    0.05
    repeat

image eirene_angry_eyes:
    "images/eirene/faces/110384_01_parts_c029.png"
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
    "images/eirene/faces/110384_01_parts_c030.png"
    0.05
    repeat

image eirene_glow_focused_eyes:
    "images/eirene/faces/110384_01_parts_c037.png"
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
    "images/eirene/faces/110384_01_parts_c003.png"
    0.05
    repeat

image eirene_glow_angry_eyes:
    "images/eirene/faces/110384_01_parts_c038.png"
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
    "images/eirene/faces/110384_01_parts_c030.png"
    0.05
    repeat

image eirene_dull_eyes:
    "images/eirene/faces/110384_01_parts_c039.png"
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
    "images/eirene/faces/110384_01_parts_c040.png"
    0.05
    repeat


# MOUTH animations start here.

image eirene_mutter1_nottalking = "images/eirene/mouths/110384_01_parts_c004.png"

image eirene_mutter1_talking:
    "images/eirene/mouths/110384_01_parts_c004.png"
    0.15
    "images/eirene/mouths/110384_01_parts_c005.png"
    0.15
    repeat

image eirene_mutter1 = WhileSpeaking("eir", "eirene_mutter1_talking", "eirene_mutter1_nottalking")


# 006/007, formerly 'frown2', is actually the same as mutter1 (004/005)


image eirene_frown1_nottalking = "images/eirene/mouths/110384_01_parts_c009.png"

image eirene_frown1_talking:
    "images/eirene/mouths/110384_01_parts_c009.png"
    0.15
    "images/eirene/mouths/110384_01_parts_c010.png"
    0.15
    repeat

image eirene_frown1 = WhileSpeaking("eir", "eirene_frown1_talking", "eirene_frown1_nottalking")


image eirene_smile1_nottalking = "images/eirene/mouths/110384_01_parts_c019.png"

image eirene_smile1_talking:
    "images/eirene/mouths/110384_01_parts_c019.png"
    0.15
    "images/eirene/mouths/110384_01_parts_c020.png"
    0.15
    repeat

image eirene_smile1 = WhileSpeaking("eir", "eirene_smile1_talking", "eirene_smile1_nottalking")


image eirene_grimace1_nottalking = "images/eirene/mouths/110384_01_parts_c022.png"

image eirene_grimace1_talking:
    "images/eirene/mouths/110384_01_parts_c022.png"
    0.15
    "images/eirene/mouths/110384_01_parts_c021.png"
    0.15
    repeat

image eirene_grimace1 = WhileSpeaking("eir", "eirene_grimace1_talking", "eirene_grimace1_nottalking")


image eirene_frown2_nottalking = "images/eirene/mouths/110384_01_parts_c023.png"

image eirene_frown2_talking:
    "images/eirene/mouths/110384_01_parts_c023.png"
    0.15
    "images/eirene/mouths/110384_01_parts_c024.png"
    0.15
    repeat

image eirene_frown2 = WhileSpeaking("eir", "eirene_frown2_talking", "eirene_frown2_nottalking")


image eirene_mutter2_nottalking = "images/eirene/mouths/110384_01_parts_c026.png"

image eirene_mutter2_talking:
    "images/eirene/mouths/110384_01_parts_c026.png"
    0.15
    "images/eirene/mouths/110384_01_parts_c025.png"
    0.15
    repeat

image eirene_mutter2 = WhileSpeaking("eir", "eirene_mutter2_talking", "eirene_mutter2_nottalking")


image eirene_grimace2_nottalking = "images/eirene/mouths/110384_01_parts_c032.png"

image eirene_grimace2_talking:
    "images/eirene/mouths/110384_01_parts_c032.png"
    0.15
    "images/eirene/mouths/110384_01_parts_c033.png"
    0.15
    repeat

image eirene_grimace2 = WhileSpeaking("eir", "eirene_grimace2_talking", "eirene_grimace2_nottalking")


image eirene_shout1_nottalking = "images/eirene/mouths/110384_01_parts_c033.png"

image eirene_shout1_talking:
    "images/eirene/mouths/110384_01_parts_c033.png"
    0.15
    "images/eirene/mouths/110384_01_parts_c034.png"
    0.15
    repeat

image eirene_shout1 = WhileSpeaking("eir", "eirene_shout1_talking", "eirene_shout1_nottalking")


# 035/036, originally 'frown6', is actually identical to mutter1, i.e. 004/005


# 041/042, originally 'frown7', is actually identical to frown1, i.e. 009/010


# 043/044, originally 'frown8', is actually identical to shout1, i.e. 033/034


# 045/046, originally 'frown9', is actually identical to mutter1, i.e. 004/005


transform eirene_crop_pos:
    # 140, 153 relative to main image.
    # Typically 2 pixels off afterwards
    # Try 142/1028, 155/1028:

    # code was for upper left pixel.  Have to add half width of image to x:
    #  (142 + (745/2)))/1028

    # Adjust to 516.5 / 1028, 1028 / 1028

    xalign 0.50243
    yalign 1.0


transform eirene_crop_shake:
    xalign 0.50243
    yalign 1.0
    linear 0.1 xalign 0.50743
    linear 0.1 xalign 0.50243
    repeat





# The game starts here.

label eirene_character_procedures:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image twilightcity = "images/backgrounds/Sty_bg_0018_200_00.png"
    scene twilightcity at middle

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    show eirene with dissolve

    eir "Greetings.  Initiating emotion simulation procedure."


    show eirene_crop at eirene_crop_pos

    eir "System reevaluation needed after 1/4/2023 renaming procedure."

    hide eirene_crop

    eir "System check... all readings normal."
    eir "I will now attempt to display all eye-based emotions."

    show eirene neutral mutter1
    eir "Displaying 'neutral' facial procedure and 'mutter1' oral procedure."

    show eirene closed_neutral mutter2
    eir "Displaying 'closed_neutral' facial procedure and 'mutter2' oral procedure."

    show eirene angry frown1
    eir "Displaying 'angry' facial procedure and 'frown1' oral procedure."

    show eirene glow_angry
    eir "Activating glow for angry expression to produce 'glow_angry' facial procedure."

    show eirene focused frown2
    eir "Displaying 'focused' facial procedure and 'frown2' oral procedure."

    show eirene glow_focused
    eir "Activating glow for angry expression to produce 'glow_angry' facial procedure."

    show eirene injured grimace1
    eir "Displaying 'injured' facial procedure and 'grimace1' oral procedure."

    show eirene pained grimace2
    eir "Displaying 'pained' facial procedure and 'grimace2' oral procedure."

    show eirene relaxed smile1
    eir "Displaying 'relaxed' facial procedure and 'smile1' oral procedure."

    show eirene sad shout1
    eir "Displaying 'sad' facial procedure and 'shout1' oral procedure."

    show eirene surprised
    eir "Maintaining 'shout1' oral procedure but switching to 'surprised' facial expression."

    show eirene dull
    eir "Maintaining 'shout1' oral procedure but switching to 'dull' facial expression."

    show eirene frown1
    eir "Confirmation:  all emotional expression mechanisms are in functioning order."
    eir "Abnormalities minimal.  Eirene unit is deemed cleared for further operations.  Commence orders."

    # This goes back to script

    jump testfiles
