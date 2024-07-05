
    # Philia Character Procedures File

    # Paste this file into a story if you want to use Philia.  These procedures animate Philia as a speaker.

    # Credit for this implementation goes to Kayu, with only very minor troubleshooting from DabblerDragon.

define phi = Character("Philia", callback=speaker("phi"))

    # This program assumes that the following folders exist:
    #     -"images/philia"
    #     -"images/philia/faces"
    #     -"images/philia/mouths"

    # Philia dynamically blinks and, while speaking, also moves her mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Philia appear*:
    #  -->  show philia with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Philia's eyes*:
    #  -->  show philia [keyword]
    #  List of eye keywords:
    #     -->  sad, closed, angry, happy, cry,
    #          cry2, realangry

    # *Changing Philia's mouth*:
    #  -->  show philia [keyword]
    #  List of mouth keywords:
    #     -->  smile1, neutral, smile2, oops, neutral2

    # *Writing dialogue for Philia*:
    #  --> phi "[Philia's line here]"

    # *Making Philia disappear*:
    #  --> hide philia with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage philia:

    always "images/philia/philia_body.png"

    group face:

        # 470/1028, 252/1028:
        pos (0.45914, 0.24513)

        attribute sad:
            "philia_sad_eyes"

        attribute closed:
            "philia_closed_eyes"

        attribute angry:
            "philia_angry_eyes"

        attribute happy:
            "philia_happy_eyes"

        attribute cry:
            "philia_cry_eyes"

        attribute cry2:
            "philia_cry2_eyes"

        attribute realangry:
            "philia_realangry_eyes"

    group mouth:

        pos (0.45914, 0.24513)

        attribute smile1 default:
            "philia_smile1"

        attribute neutral1:
            "philia_neutral1"

        attribute smile2:
            "philia_smile2"

        attribute oops:
            "philia_oops"

        attribute neutral2:
            "philia_neutral2"



## EYE animations start here.

image philia_sad_eyes:
    "images/philia/faces/110028_01_parts_c000.png"
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
    "images/philia/faces/110028_01_parts_c001.png"
    0.05
    repeat

image philia_closed_eyes:
    "images/philia/faces/110028_01_parts_c001.png"
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
    "images/philia/faces/110028_01_parts_c001.png"
    0.05
    repeat

image philia_angry_eyes:
    "images/philia/faces/110028_01_parts_c006.png"
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
    "images/philia/faces/110028_01_parts_c007.png"
    0.05
    repeat

image philia_happy_eyes:
    "images/philia/faces/110028_01_parts_c016.png"
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
    "images/philia/faces/110028_01_parts_c017.png"
    0.05
    repeat

image philia_cry_eyes:
    "images/philia/faces/110028_01_parts_c018.png"
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
    "images/philia/faces/110028_01_parts_c019.png"
    0.05
    repeat

image philia_cry2_eyes:
    "images/philia/faces/110028_01_parts_c027.png"
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
    "images/philia/faces/110028_01_parts_c027.png"
    0.05
    repeat

image philia_realangry_eyes:
    "images/philia/faces/110028_01_parts_c028.png"
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
    "images/philia/faces/110028_01_parts_c028.png"
    0.05
    repeat


# MOUTH animations start here.

image philia_smile1_nottalking = "images/philia/mouths/110028_01_parts_c008.png"

image philia_smile1_talking:
    "images/philia/mouths/110028_01_parts_c008.png"
    0.15
    "images/philia/mouths/110028_01_parts_c009.png"
    0.15
    repeat

image philia_smile1 = WhileSpeaking("phi", "philia_smile1_talking", "philia_smile1_nottalking")


image philia_neutral1_nottalking = "images/philia/mouths/110028_01_parts_c014.png"

image philia_neutral1_talking:
    "images/philia/mouths/110028_01_parts_c014.png"
    0.15
    "images/philia/mouths/110028_01_parts_c015.png"
    0.15
    repeat

image philia_neutral1 = WhileSpeaking("phi", "philia_neutral1_talking", "philia_neutral1_nottalking")


image philia_smile2_nottalking = "images/philia/mouths/110028_01_parts_c021.png"

image philia_smile2_talking:
    "images/philia/mouths/110028_01_parts_c021.png"
    0.15
    "images/philia/mouths/110028_01_parts_c022.png"
    0.15
    repeat

image philia_smile2 = WhileSpeaking("phi", "philia_smile2_talking", "philia_smile2_nottalking")


image philia_oops_nottalking = "images/philia/mouths/110028_01_parts_c023.png"

image philia_oops_talking:
    "images/philia/mouths/110028_01_parts_c023.png"
    0.15
    "images/philia/mouths/110028_01_parts_c024.png"
    0.15
    repeat

image philia_oops = WhileSpeaking("phi", "philia_oops_talking", "philia_oops_nottalking")


image philia_neutral2_nottalking = "images/philia/mouths/110028_01_parts_c035.png"

image philia_neutral2_talking:
    "images/philia/mouths/110028_01_parts_c035.png"
    0.15
    "images/philia/mouths/110028_01_parts_c035.png"
    0.15
    repeat

image philia_neutral2 = WhileSpeaking("phi", "philia_neutral2_talking", "philia_neutral2_nottalking")



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

label philia_character_procedures:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image forbiddenlibrary = "images/backgrounds/Sty_bg_0049_101_00.png"
    scene forbiddenlibrary at middle



    show philia with dissolve

    show philia angry
    show philia neutral1

    phi "Kayu is a Dodoo idiot who is smoking on the highest amount of copium possible."

    show philia realangry

    phi "DL2 happening is already a joke, how does he think a minor character such as me..."
    phi "even has a chance of getting in?"

    show philia closed

    phi "Then again I guess fate has its own weird ways of going, that is what is intriguing."

    show philia smile2
    show philia happy

    phi "While we see what becomes of us, I'll be going my way, after all my prince is nearly waking up!"
    phi "it would be a disaster if Melody failed to make breakfast, so I'd better go check on her!"

    hide philia with dissolve


    # This goes back to script

    jump testfiles
