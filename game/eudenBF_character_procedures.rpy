
    # Bondforged Euden Character Procedures File

    # Paste this file into a story if you want to use Bondforged Euden.  These procedures animate Bondforged Euden as a speaker.
    # You'll also need to paste THIS line into your actual script above the script label whenever you're using Bondforged Euden:

define beud = Character("Euden", callback=speaker("beud"))

    # This program assumes that the following folders exist:
    #     -"images/euden_bondforged"
    #     -"images/euden_bondforged/faces"
    #     -"images/euden_bondforged/mouths"

    # Bondforged Euden dynamically blinks and, while speaking, also moves her mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Bondforged Euden appear*:
    #  -->  show beuden with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Bondforged Euden's eyes*:
    #  -->  show beuden [keyword]
    #  List of eye keywords:
    #     -->  focused (default), focused2, focused3, angry, flinch, relaxed,
    #          sad, sweat

    # *Changing Bondforged Euden's mouth*:
    #  -->  show beuden [keyword]
    #  List of mouth keywords:
    #     -->  frown1 (default), frown2, frown3, grimace1, grimace2, grin1,
    #          shout1, smile1, smile2, smile3

    # *Writing dialogue for Bondforged Euden*:
    #  --> beud "[Bondforged Euden's line here]"

    # *Making Bondforged Euden disappear*:
    #  --> hide beuden with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage beuden:

    always "images/euden_bondforged/euden_bondforged_body.png"

    group face:

        # 443/1028, 237/1028:
        pos (0.43093, 0.23054)

        attribute focused default:
            "beuden_focused_eyes"

        attribute relaxed:
            "beuden_relaxed_eyes"

        attribute flinch:
            "beuden_flinch_eyes"

        attribute sweat:
            "beuden_sweat_eyes"

        attribute focused2:
            "beuden_focused2_eyes"

        attribute angry:
            "beuden_angry_eyes"

        attribute focused3:
            "beuden_focused3_eyes"

        attribute sad:
            "beuden_sad_eyes"

    group mouth:

        pos (0.43093, 0.23054)

        attribute frown1 default:
            "beuden_frown1"

        attribute frown2:
            "beuden_frown2"

        attribute smile1:
            "beuden_smile1"

        attribute grimace1:
            "beuden_grimace1"

        attribute frown3:
            "beuden_frown3"

        attribute grin1:
            "beuden_grin1"

        attribute grimace2:
            "beuden_grimace2"

        attribute shout1:
            "beuden_shout1"

        attribute smile2:
            "beuden_smile2"

        attribute smile3:
            "beuden_smile3"



## EYE animations start here.

image beuden_focused_eyes:
    "images/euden_bondforged/faces/100001_14_parts_c000.png"
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
    "images/euden_bondforged/faces/100001_14_parts_c001.png"
    0.05
    repeat

image beuden_relaxed_eyes:
    "images/euden_bondforged/faces/100001_14_parts_c009.png"
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
    "images/euden_bondforged/faces/100001_14_parts_c010.png"
    0.05
    repeat

image beuden_flinch_eyes:
    "images/euden_bondforged/faces/100001_14_parts_c011.png"
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
    "images/euden_bondforged/faces/100001_14_parts_c012.png"
    0.05
    repeat

image beuden_sweat_eyes:
    "images/euden_bondforged/faces/100001_14_parts_c013.png"
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
    "images/euden_bondforged/faces/100001_14_parts_c014.png"
    0.05
    repeat

image beuden_focused2_eyes:
    "images/euden_bondforged/faces/100001_14_parts_c024.png"
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
    "images/euden_bondforged/faces/100001_14_parts_c025.png"
    0.05
    repeat

image beuden_angry_eyes:
    "images/euden_bondforged/faces/100001_14_parts_c026.png"
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
    "images/euden_bondforged/faces/100001_14_parts_c027.png"
    0.05
    repeat

image beuden_focused3_eyes:
    "images/euden_bondforged/faces/100001_14_parts_c028.png"
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
    "images/euden_bondforged/faces/100001_14_parts_c029.png"
    0.05
    repeat

image beuden_sad_eyes:
    "images/euden_bondforged/faces/100001_14_parts_c038.png"
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
    "images/euden_bondforged/faces/100001_14_parts_c039.png"
    0.05
    repeat




# MOUTH animations start here.

image beuden_frown1_nottalking = "images/euden_bondforged/mouths/100001_14_parts_c004.png"

image beuden_frown1_talking:
    "images/euden_bondforged/mouths/100001_14_parts_c005.png"
    0.15
    "images/euden_bondforged/mouths/100001_14_parts_c004.png"
    0.15
    repeat

image beuden_frown1 = WhileSpeaking("beud", "beuden_frown1_talking", "beuden_frown1_nottalking")


image beuden_frown2_nottalking = "images/euden_bondforged/mouths/100001_14_parts_c007.png"

image beuden_frown2_talking:
    "images/euden_bondforged/mouths/100001_14_parts_c008.png"
    0.15
    "images/euden_bondforged/mouths/100001_14_parts_c007.png"
    0.15
    repeat

image beuden_frown2 = WhileSpeaking("beud", "beuden_frown2_talking", "beuden_frown2_nottalking")


image beuden_smile1_nottalking = "images/euden_bondforged/mouths/100001_14_parts_c016.png"

image beuden_smile1_talking:
    "images/euden_bondforged/mouths/100001_14_parts_c017.png"
    0.15
    "images/euden_bondforged/mouths/100001_14_parts_c016.png"
    0.15
    repeat

image beuden_smile1 = WhileSpeaking("beud", "beuden_smile1_talking", "beuden_smile1_nottalking")


image beuden_grimace1_nottalking = "images/euden_bondforged/mouths/100001_14_parts_c018.png"

image beuden_grimace1_talking:
    "images/euden_bondforged/mouths/100001_14_parts_c018.png"
    0.15
    "images/euden_bondforged/mouths/100001_14_parts_c020.png"
    0.15
    repeat

image beuden_grimace1 = WhileSpeaking("beud", "beuden_grimace1_talking", "beuden_grimace1_nottalking")


image beuden_frown3_nottalking = "images/euden_bondforged/mouths/100001_14_parts_c020.png"

image beuden_frown3_talking:
    "images/euden_bondforged/mouths/100001_14_parts_c021.png"
    0.15
    "images/euden_bondforged/mouths/100001_14_parts_c020.png"
    0.15
    repeat

image beuden_frown3 = WhileSpeaking("beud", "beuden_frown3_talking", "beuden_frown3_nottalking")


image beuden_grin1_nottalking = "images/euden_bondforged/mouths/100001_14_parts_c022.png"

image beuden_grin1_talking:
    "images/euden_bondforged/mouths/100001_14_parts_c022.png"
    0.15
    "images/euden_bondforged/mouths/100001_14_parts_c023.png"
    0.15
    repeat

image beuden_grin1 = WhileSpeaking("beud", "beuden_grin1_talking", "beuden_grin1_nottalking")


image beuden_grimace2_nottalking = "images/euden_bondforged/mouths/100001_14_parts_c030.png"

image beuden_grimace2_talking:
    "images/euden_bondforged/mouths/100001_14_parts_c031.png"
    0.15
    "images/euden_bondforged/mouths/100001_14_parts_c030.png"
    0.15
    repeat

image beuden_grimace2 = WhileSpeaking("beud", "beuden_grimace2_talking", "beuden_grimace2_nottalking")


#032 and 033 are the same as 004 and 005.


image beuden_shout1_nottalking = "images/euden_bondforged/mouths/100001_14_parts_c034.png"

image beuden_shout1_talking:
    "images/euden_bondforged/mouths/100001_14_parts_c035.png"
    0.15
    "images/euden_bondforged/mouths/100001_14_parts_c034.png"
    0.15
    repeat

image beuden_shout1 = WhileSpeaking("beud", "beuden_shout1_talking", "beuden_shout1_nottalking")


image beuden_smile2_nottalking = "images/euden_bondforged/mouths/100001_14_parts_c036.png"

image beuden_smile2_talking:
    "images/euden_bondforged/mouths/100001_14_parts_c037.png"
    0.15
    "images/euden_bondforged/mouths/100001_14_parts_c036.png"
    0.15
    repeat

image beuden_smile2 = WhileSpeaking("beud", "beuden_smile2_talking", "beuden_smile2_nottalking")


image beuden_smile3_nottalking = "images/euden_bondforged/mouths/100001_14_parts_c040.png"

image beuden_smile3_talking:
    "images/euden_bondforged/mouths/100001_14_parts_c041.png"
    0.15
    "images/euden_bondforged/mouths/100001_14_parts_c040.png"
    0.15
    repeat

image beuden_smile3 = WhileSpeaking("beud", "beuden_smile3_talking", "beuden_smile3_nottalking")




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

label eudenBF_character_procedures:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image otherworld2 = "images/backgrounds/Sty_bg_0146_200_00.png"
    scene otherworld2

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    show beuden with dissolve
    beud "Hey there.  I'm glad you came to check if all my 'files' are working."
    beud "You're one of the few people holding this world together, so I appreciate your efforts."

    show beuden smile1
    beud "I actually have no way to check my own appearance outside the universe like this, so you're the only one who can do this... sorry..."
    beud "Well, let's run through them together, and then you can relax."

    show beuden focused frown1
    beud "This is the 'focused' face and the 'frown1' mouth."

    show beuden focused2 frown2
    beud "This is the 'focused2' face and the 'frown2' mouth."

    show beuden focused3 frown3
    beud "This is the 'focused3' face and the 'frown3' mouth."

    show beuden angry grimace1
    beud "This is the 'angry' face and the 'grimace1' mouth."

    show beuden flinch grimace2
    beud "This is the 'flinch' face and the 'grimace2' mouth."

    show beuden relaxed grin1
    beud "This is the 'relaxed' face and the 'grin1' mouth."

    show beuden sad shout1
    beud "This is the 'sad' face and the 'shout1' mouth."

    show beuden sweat smile1
    beud "This is the 'sweat' face and the 'smile1' mouth."

    show beuden relaxed smile2
    beud "That's all the faces, but this is the 'smile2' mouth."

    show beuden smile3
    beud "And, of course, this is the 'smile3' mouth."

    show beuden smile1
    beud "Well, that's everything.  Assuming you didn't see anything funny, that means my own personal stability is intact."
    beud "But please also check on my friend's 'instantiation' too, if it's not too much trouble."
    beud "And... I want to let you how much I appreciate you sticking around.  It's nice to have some company."

    hide beuden with dissolve

    # This goes back to script

    jump testfiles
