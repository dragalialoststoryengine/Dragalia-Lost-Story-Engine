

    # Paste this file into a story if you want to use edeline.  These procedures animate edeline as a speaker.

define edel = Character("Edeline", callback=speaker("edel"))

    # This program assumes that the following folders exist:
    #     -"images/edeline"
    #     -"images/edeline/faces"
    #     -"images/edeline/mouths"

    # edeline dynamically blinks and, while speaking, also moves her mouth along with the text scroll.

    # FUNCTIONS:

    # *Making edeline appear*:
    #  -->  show edeline with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing edeline's eyes*:
    #  -->  show edeline [keyword]
    #  List of eye keywords:
    #     -->  relaxed (the default option), relaxed2, relaxed3, sad, sad2,
    #          surprised, surprised2, blushing, annoyed, annoyed2

    # *Changing edeline's mouth*:
    #  -->  show edeline [keyword]
    #  List of mouth keywords:
    #     -->  grin1 (the default option), grin2, grin3, grin4, smile1, smile2, smile3,
    #          grimace1, grimace2, frown1

    # *Writing dialogue for edeline*:
    #  --> edel "[edeline's line here]"

    # *Making edeline disappear*:
    #  --> hide edeline with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage edeline:

    always "images/edeline/edeline_body.png"

    group face:

        # 449/1028, 222/1028:
        pos (0.434570312, 0.225585938)

        attribute relaxed default:
            "edeline_relaxed_eyes"

        attribute relaxed2:
            "edeline_relaxed2_eyes"

        attribute relaxed3:
            "edeline_relaxed3_eyes"

        attribute sad:
            "edeline_sad_eyes"

        attribute surprised:
            "edeline_surprised_eyes"

        attribute blushing:
            "edeline_blushing_eyes"

        attribute sad2:
            "edeline_sad2_eyes"

        attribute surprised2:
            "edeline_surprised2_eyes"

        attribute annoyed:
            "edeline_annoyed_eyes"

        attribute annoyed2:
            "edeline_annoyed2_eyes"


    group mouth:

        pos (0.434570312, 0.225585938)

        attribute grin1 default:
            "edeline_grin1"

        attribute grin2:
            "edeline_grin2"

        attribute smile1:
            "edeline_smile1"

        attribute smile2:
            "edeline_smile2"

        attribute grin3:
            "edeline_grin3"

        attribute grin4:
            "edeline_grin4"

        attribute grimace1:
            "edeline_grimace1"

        attribute smile3:
            "edeline_smile3"

        attribute frown1:
            "edeline_frown1"

        attribute grimace2:
            "edeline_grimace2"



## EYE animations start here.

image edeline_relaxed_eyes:
    "images/edeline/faces/100001_01_parts_c012.png"
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
    "images/edeline/faces/100001_01_parts_c013.png"
    0.05
    repeat

image edeline_relaxed2_eyes:
    "images/edeline/faces/100001_01_parts_c016.png"
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
    "images/edeline/faces/100001_01_parts_c017.png"
    0.05
    repeat

image edeline_relaxed3_eyes:
    "images/edeline/faces/100001_01_parts_c043.png"
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
    "images/edeline/faces/100001_01_parts_c044.png"
    0.05
    repeat

image edeline_sad_eyes:
    "images/edeline/faces/100001_01_parts_c045.png"
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
    "images/edeline/faces/100001_01_parts_c046.png"
    0.05
    repeat

image edeline_surprised_eyes:
    "images/edeline/faces/100001_01_parts_c018.png"
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
    "images/edeline/faces/100001_01_parts_c019.png"
    0.05
    repeat

image edeline_blushing_eyes:
    "images/edeline/faces/100001_01_parts_c030.png"
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
    "images/edeline/faces/100001_01_parts_c031.png"
    0.05
    repeat

image edeline_sad2_eyes:
    "images/edeline/faces/100001_01_parts_c028.png"
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
    "images/edeline/faces/100001_01_parts_c029.png"
    0.05
    repeat

image edeline_surprised2_eyes:
    "images/edeline/faces/100001_01_parts_c043.png"
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
    "images/edeline/faces/100001_01_parts_c044.png"
    0.05
    repeat

image edeline_annoyed_eyes:
    "images/edeline/faces/100001_01_parts_c032.png"
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
    "images/edeline/faces/100001_01_parts_c033.png"
    0.05
    repeat

image edeline_annoyed2_eyes:
    "images/edeline/faces/100001_01_parts_c028.png"
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
    "images/edeline/faces/100001_01_parts_c029.png"
    0.05
    repeat



# MOUTH animations start here.

image edeline_grin1_nottalking = "images/edeline/mouths/100001_01_parts_c006.png"

image edeline_grin1_talking:
    "images/edeline/mouths/100001_01_parts_c006.png"
    0.15
    "images/edeline/mouths/100001_01_parts_c007.png"
    0.15
    repeat

image edeline_grin1 = WhileSpeaking("edel", "edeline_grin1_talking", "edeline_grin1_nottalking")


image edeline_grin2_nottalking = "images/edeline/mouths/100001_01_parts_c008.png"

image edeline_grin2_talking:
    "images/edeline/mouths/100001_01_parts_c008.png"
    0.15
    "images/edeline/mouths/100001_01_parts_c009.png"
    0.15
    repeat

image edeline_grin2 = WhileSpeaking("edel", "edeline_grin2_talking", "edeline_grin2_nottalking")


image edeline_smile1_nottalking = "images/edeline/mouths/100001_01_parts_c037.png"

image edeline_smile1_talking:
    "images/edeline/mouths/100001_01_parts_c037.png"
    0.15
    "images/edeline/mouths/100001_01_parts_c038.png"
    0.15
    repeat

image edeline_smile1 = WhileSpeaking("edel", "edeline_smile1_talking", "edeline_smile1_nottalking")


image edeline_smile2_nottalking = "images/edeline/mouths/100001_01_parts_c049.png"

image edeline_smile2_talking:
    "images/edeline/mouths/100001_01_parts_c049.png"
    0.15
    "images/edeline/mouths/100001_01_parts_c050.png"
    0.15
    repeat

image edeline_smile2 = WhileSpeaking("edel", "edeline_smile2_talking", "edeline_smile2_nottalking")


image edeline_grin3_nottalking = "images/edeline/mouths/100001_01_parts_c051.png"

image edeline_grin3_talking:
    "images/edeline/mouths/100001_01_parts_c051.png"
    0.15
    "images/edeline/mouths/100001_01_parts_c052.png"
    0.15
    repeat

image edeline_grin3 = WhileSpeaking("edel", "edeline_grin3_talking", "edeline_grin3_nottalking")


image edeline_grin4_nottalking = "images/edeline/mouths/100001_01_parts_c055.png"

image edeline_grin4_talking:
    "images/edeline/mouths/100001_01_parts_c055.png"
    0.15
    "images/edeline/mouths/100001_01_parts_c056.png"
    0.15
    repeat

image edeline_grin4 = WhileSpeaking("edel", "edeline_grin4_talking", "edeline_grin4_nottalking")


image edeline_grimace1_nottalking = "images/edeline/mouths/100001_01_parts_c011.png"

image edeline_grimace1_talking:
    "images/edeline/mouths/100001_01_parts_c011.png"
    0.15
    "images/edeline/mouths/100001_01_parts_c036.png"
    0.15
    repeat

image edeline_grimace1 = WhileSpeaking("edel", "edeline_grimace1_talking", "edeline_grimace1_nottalking")


image edeline_smile3_nottalking = "images/edeline/mouths/100001_01_parts_c051.png"

image edeline_smile3_talking:
    "images/edeline/mouths/100001_01_parts_c051.png"
    0.15
    "images/edeline/mouths/100001_01_parts_c052.png"
    0.15
    repeat

image edeline_smile3 = WhileSpeaking("edel", "edeline_smile3_talking", "edeline_smile3_nottalking")

#  Parts 33 and 34 are identical to 004 and 005, i.e. grin1.

image edeline_frown1_nottalking = "images/edeline/mouths/100001_01_parts_c026.png"

image edeline_frown1_talking:
    "images/edeline/mouths/100001_01_parts_c026.png"
    0.15
    "images/edeline/mouths/100001_01_parts_c027.png"
    0.15
    repeat

image edeline_frown1 = WhileSpeaking("edel", "edeline_frown1_talking", "edeline_frown1_nottalking")


image edeline_grimace2_nottalking = "images/edeline/mouths/100001_01_parts_c022.png"

image edeline_grimace2_talking:
    "images/edeline/mouths/100001_01_parts_c022.png"
    0.15
    "images/edeline/mouths/100001_01_parts_c023.png"
    0.15
    repeat

image edeline_grimace2 = WhileSpeaking("edel", "edeline_grimace2_talking", "edeline_grimace2_nottalking")




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

label edeline_character_procedures:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image forbiddenlibrary = "images/backgrounds/Sty_bg_0042_100_00.png"
    scene forbiddenlibrary at middle



    show edeline with dissolve

    edel "Ah, what a pleasure to meet you! Welcome to the Halidom!"
    edel "I know it's not much... but, I hope you enjoy it here."
    edel "I'm quite glad actually, that someone still cares enough to show up..."
    edel "But I digress.  You came here to see my facial expressions, right?"
    edel "...Hm, how do I know? Girl's secret~!"
    edel "Either way, let me show you, and we can get you a room while we do it too!"

    show edeline relaxed
    edel "Here's my relaxed state! I think I look cute, at least."

    show edeline relaxed2
    edel "This is a second relaxed (relaxed2) expression.  Maybe you can tell if there's any difference?"

    show edeline relaxed3
    edel "This is a third relaxed (relaxed3) expression.  I might just be bad at facial expressions."

    show edeline sad
    edel "This is a sad expression.  I... I really miss them, you know?"

    show edeline sad2
    edel "Elisanne... Ranzal... Luca... (sad2) Ah! Sorry for reminiscing."

    show edeline surprised
    edel "Here is my surprised expression.  I... really might just be bad at facial expressions."

    show edeline surprised2
    edel "But of course, I also have another surprised (surprised2) expression.  Maybe I'll get a gift from Cleo this year?"

    show edeline blushing
    edel "In this expression, I am blushing.  It might be more accurate to say that it's flushed, but don't tell Mym that yet, okay?"

    show edeline annoyed
    edel "This is an annoyed expression, of course..."

    show edeline annoyed2
    edel "...and this is a second one (annoyed2).  And that about wraps things up."

    show edeline relaxed
    edel "Of course, you're also here for mouth movements!"

    show edeline grin1
    edel "This is my standard grin (grin1).  I find it quite easy to grin today. I wonder why?"

    show edeline grin2
    edel "This is a second grin (grin2).  I'm probably having a good day!"

    show edeline grin3
    edel "And now for a third one (grin3).  I can at least be happy Cleo, Notte, and Mym stuck around, right?"

    show edeline grin4
    edel "But I also have one last one (grin4) in my repertoire!  Perhaps there are some similarities, you know?"

    show edeline smile1
    edel "I have a wide repertoire of smiles! Here's my first."

    show edeline smile2
    edel "This is the smile for the days Cleo bakes a cake!"

    show edeline smile3
    edel "This one is for the days I spend with Mym!"

    show edeline grimace1
    edel "I... Do feel remorse for what happened in the throne room. If only there were some way... (grimace1) "

    show edeline grimace2
    edel "I would wish that things would change but... (grimace2)Well, I guess sometimes I need to keep moving forward."

    show edeline frown1
    edel "I let down the people I cared about... (frown1) Do I even deserve to lead?"

    show edeline sad2
    edel "Apologies... I... I need some time to think. Please, by all means, enjoy your stay! I... I need to go."

    hide edeline with dissolve


    # This goes back to script

    jump testfiles
