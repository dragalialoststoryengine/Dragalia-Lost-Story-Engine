    # Mascula Character Procedures File

    # Paste this file into a story if you want to use Laxi.  These procedures animate Mascula as a speaker.

define masc = Character("Mascula", callback=speaker("masc"))

    # This program assumes that the following folders exist:
    #     -"images/mascula"
    #     -"images/mascula/faces"
    #     -"images/mascula/mouths"

    # Mascula dynamically blinks and, while speaking, also moves his mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Mascula appear*:
    #  -->  show mascula with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Mascula's eyes*:
    #  -->  show mascula [keyword]
    #  List of eye keywords:
    #     -->  neutral (the default option), closed_neutral, angry, blush, focused,
    #          pained, relaxed, sad, surprised

    # *Changing Mascula's mouth*:
    #  -->  show mascula [keyword]
    #  List of mouth keywords:
    #     -->  mutter1 (the default option), frown1, grimace1, grimace2,
    #          pout1, shout1, smile1, smile2

    # *Writing dialogue for Mascula*:
    #  --> masc "[Mascula's line here]"

    # *Making Mascula disappear*:
    #  --> hide mascula with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage mascula:

    always "images/mascula/mascula_body.png"

    group face:

        # 444/1024, 257/1024:
        pos (0.43359375, 0.25097656)

        attribute neutral default:
            "mascula_neutral_eyes"

        attribute closed_neutral:
            "images/mascula/faces/120135_01_parts_c001.png"

        attribute focused:
            "mascula_focused_eyes"

        attribute relaxed:
            "mascula_relaxed_eyes"

        attribute pained:
            "mascula_pained_eyes"

        attribute surprised:
            "mascula_surprised_eyes"

        attribute blush:
            "mascula_blush_eyes"

        attribute sad:
            "mascula_sad_eyes"

        attribute angry:
            "mascula_angry_eyes"


    group mouth:

        pos (0.43359375, 0.25097656)

        attribute mutter1 default:
            "mascula_mutter1"

        attribute frown1:
            "mascula_frown1"

        attribute smile1:
            "mascula_smile1"

        attribute pout1:
            "mascula_pout1"

        attribute grimace1:
            "mascula_grimace1"

        attribute smile2:
            "mascula_smile2"

        attribute grimace2:
            "mascula_grimace2"

        attribute shout1:
            "mascula_shout1"





## EYE animations start here.

image mascula_neutral_eyes:
    "images/mascula/faces/120135_01_parts_c000.png"
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
    "images/mascula/faces/120135_01_parts_c001.png"
    0.05
    repeat

image mascula_focused_eyes:
    "images/mascula/faces/120135_01_parts_c003.png"
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
    "images/mascula/faces/120135_01_parts_c004.png"
    0.05
    repeat

image mascula_relaxed_eyes:
    "images/mascula/faces/120135_01_parts_c009.png"
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
    "images/mascula/faces/120135_01_parts_c010.png"
    0.05
    repeat

image mascula_pained_eyes:
    "images/mascula/faces/120135_01_parts_c011.png"
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
    "images/mascula/faces/120135_01_parts_c012.png"
    0.05
    repeat

image mascula_surprised_eyes:
    "images/mascula/faces/120135_01_parts_c013.png"
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
    "images/mascula/faces/120135_01_parts_c014.png"
    0.05
    repeat

image mascula_blush_eyes:
    "images/mascula/faces/120135_01_parts_c015.png"
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
    "images/mascula/faces/120135_01_parts_c016.png"
    0.05
    repeat

image mascula_sad_eyes:
    "images/mascula/faces/120135_01_parts_c025.png"
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
    "images/mascula/faces/120135_01_parts_c026.png"
    0.05
    repeat

image mascula_angry_eyes:
    "images/mascula/faces/120135_01_parts_c027.png"
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
    "images/mascula/faces/120135_01_parts_c028.png"
    0.05
    repeat







# MOUTH animations start here.

# Note:  'grimace's here are animated in reverse from usual (teeth not shown on resting).

image mascula_mutter1_nottalking = "images/mascula/mouths/120135_01_parts_c005.png"

image mascula_mutter1_talking:
    "images/mascula/mouths/120135_01_parts_c006.png"
    0.15
    "images/mascula/mouths/120135_01_parts_c005.png"
    0.15
    repeat

image mascula_mutter1 = WhileSpeaking("masc", "mascula_mutter1_talking", "mascula_mutter1_nottalking")


image mascula_frown1_nottalking = "images/mascula/mouths/120135_01_parts_c007.png"

image mascula_frown1_talking:
    "images/mascula/mouths/120135_01_parts_c008.png"
    0.15
    "images/mascula/mouths/120135_01_parts_c007.png"
    0.15
    repeat

image mascula_frown1 = WhileSpeaking("masc", "mascula_frown1_talking", "mascula_frown1_nottalking")


image mascula_smile1_nottalking = "images/mascula/mouths/120135_01_parts_c017.png"

image mascula_smile1_talking:
    "images/mascula/mouths/120135_01_parts_c018.png"
    0.15
    "images/mascula/mouths/120135_01_parts_c017.png"
    0.15
    repeat

image mascula_smile1 = WhileSpeaking("masc", "mascula_smile1_talking", "mascula_smile1_nottalking")


# The classification of this one was tricky because it's like a grimace but also poutlike.
# He has other grimaces so I made this pout.
image mascula_pout1_nottalking = "images/mascula/mouths/120135_01_parts_c019.png"

image mascula_pout1_talking:
    "images/mascula/mouths/120135_01_parts_c020.png"
    0.15
    "images/mascula/mouths/120135_01_parts_c019.png"
    0.15
    repeat

image mascula_pout1 = WhileSpeaking("masc", "mascula_pout1_talking", "mascula_pout1_nottalking")


image mascula_grimace1_nottalking = "images/mascula/mouths/120135_01_parts_c021.png"

image mascula_grimace1_talking:
    "images/mascula/mouths/120135_01_parts_c022.png"
    0.15
    "images/mascula/mouths/120135_01_parts_c021.png"
    0.15
    repeat

image mascula_grimace1 = WhileSpeaking("masc", "mascula_grimace1_talking", "mascula_grimace1_nottalking")


image mascula_smile2_nottalking = "images/mascula/mouths/120135_01_parts_c023.png"

image mascula_smile2_talking:
    "images/mascula/mouths/120135_01_parts_c024.png"
    0.15
    "images/mascula/mouths/120135_01_parts_c023.png"
    0.15
    repeat

image mascula_smile2 = WhileSpeaking("masc", "mascula_smile2_talking", "mascula_smile2_nottalking")


image mascula_grimace2_nottalking = "images/mascula/mouths/120135_01_parts_c030.png"

image mascula_grimace2_talking:
    "images/mascula/mouths/120135_01_parts_c031.png"
    0.15
    "images/mascula/mouths/120135_01_parts_c030.png"
    0.15
    repeat

image mascula_grimace2 = WhileSpeaking("masc", "mascula_grimace2_talking", "mascula_grimace2_nottalking")


image mascula_shout1_nottalking = "images/mascula/mouths/120135_01_parts_c034.png"

image mascula_shout1_talking:
    "images/mascula/mouths/120135_01_parts_c035.png"
    0.15
    "images/mascula/mouths/120135_01_parts_c034.png"
    0.15
    repeat

image mascula_shout1 = WhileSpeaking("masc", "mascula_shout1_talking", "mascula_shout1_nottalking")






# The game starts here.

label mascula_character_procedures:

    # I'd like to use the ▷ and ◁ characters but Ren'py rejects it in dialogue for some reason.


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image drawbridgeday = "images/backgrounds/Sty_bg_0017_100_00.png"
    scene drawbridgeday at middle

    show mascula with dissolve
    masc "Hello there.  Would you mind if I asked your opinion on something?"

    show mascula neutral mutter1
    masc "(neutral mutter1) I've been thinking a lot about what it means to have my own identity separate from Laxi, now that I have my own body."

    show mascula angry frown1
    masc "(angry frown1) For the longest time, I thought that Laxi acted too cold and emotionless all the time."

    show mascula blush grimace1
    masc "(blush grimace1) But... now that I have my own body to pilot, I'm finding it a lot more difficult to emote properly and talk to people than I originally anticipated."

    show mascula focused grimace2
    masc "(focused grimace2) We don't have to do it right now, but... would you give me some feedback occasionally on whether you feel like my relationships with people are progressing well enough?"

    show mascula pained pout1
    masc "(pained pout1) Look, I know you think I'm worrying too much, but I think it would really help me, okay?"

    show mascula surprised shout1
    masc "(surprised shout1) Wait, you really will?!  Wow, thank you so much!!"

    show mascula sad smile2
    masc "(sad smile2) I know that maybe I'm overthinking here.  It's not a secret that I have a bit of an identity crisis, being intermingled with Laxi and all."

    show mascula relaxed smile1
    masc "(relaxed smile1) But that's why I think an outside opinion like yours will really help me!  You're friends with so many people, so you're in a great position to advise me on how to connect with others."

    show mascula closed_neutral
    masc "(closed_neutral) Thank you again.  This is a major relief, and I promise to assist you as always in whatever ways I can."

    hide mascula with dissolve


    # This goes back to script

    jump testfiles
