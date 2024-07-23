
    # Elisanne Character Procedures File

    # Paste this file into a story if you want to use Elisanne.  These procedures animate Elisanne as a speaker.
    # You'll also need to paste THIS line into your actual script above the script label whenever you're using Elisanne:

define elly = Character("Elisanne", callback=speaker("elly"))

    # This program assumes that the following folders exist:
    #     -"images/elisanne"
    #     -"images/elisanne/faces"
    #     -"images/elisanne/mouths"

    # Elisanne dynamically blinks and, while speaking, also moves her mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Elisanne appear*:
    #  -->  show elisanne with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Elisanne's eyes*:
    #  -->  show elisanne [keyword]
    #  List of eye keywords:
    #     -->  neutral (the default option), neutral2, closed_neutral, focused,
    #          relaxed, flinch, surprised, blush, sad, pained, angry, open_shout1, closed_blush

    # *Changing Elisanne's mouth*:
    #  -->  show elisanne [keyword]
    #  List of mouth keywords:
    #     -->  smile1 (the default option), smile2, smile3,
    #          frown1, frown2, pout1, pout2, shout1, shout2, frown1_closed

    # *Writing dialogue for Elisanne*:
    #  --> elly "[Elisanne's line here]"

    # *Making Elisanne disappear*:
    #  --> hide elisanne with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage elisanne:

    always "images/elisanne/elisanne_body.png"

    group face:

        # 454/1028, 244/1028:
        pos (0.44163, 0.23735)

        attribute neutral default:
            "elisanne_neutral_eyes"

        attribute closed_neutral:
            "images/elisanne/faces/100002_01_parts_c002.png"

        attribute neutral2:
            "elisanne_neutral2_eyes"

        attribute focused:
            "elisanne_focused_eyes"

        attribute relaxed:
            "elisanne_relaxed_eyes"

        attribute flinch:
            "elisanne_flinch_eyes"

        attribute surprised:
            "elisanne_surprised_eyes"

        attribute blush:
            "elisanne_blush_eyes"

        attribute closed_blush:
            "images/elisanne/faces/100002_01_parts_c023.png"

        attribute pained:
            "elisanne_pained_eyes"

        attribute angry:
            "elisanne_angry_eyes"

        attribute sad:
            "elisanne_sad_eyes"


    group mouth:

        pos (0.44163, 0.23735)

        attribute smile1 default:
            "elisanne_smile1"

        attribute frown1:
            "elisanne_frown1"

        attribute frown1_closed:
            "images/elisanne/mouths/100002_01_parts_c026.png"

        attribute smile2:
            "elisanne_smile2"

        attribute frown2:
            "elisanne_frown2"

        attribute shout1:
            "elisanne_shout1"

        attribute open_shout1:
            "images/elisanne/mouths/100002_01_parts_c029.png"

        attribute pout1:
            "elisanne_pout1"

        attribute pout2:
            "elisanne_pout2"

        attribute shout2:
            "elisanne_shout2"

        attribute smile3:
            "elisanne_smile3"


## EYE animations start here.

image elisanne_neutral_eyes:
    "images/elisanne/faces/100002_01_parts_c000.png"
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
    "images/elisanne/faces/100002_01_parts_c001.png"
    0.05
    repeat

image elisanne_neutral2_eyes:
    "images/elisanne/faces/100002_01_parts_c004.png"
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
    "images/elisanne/faces/100002_01_parts_c005.png"
    0.05
    repeat

image elisanne_focused_eyes:
    "images/elisanne/faces/100002_01_parts_c006.png"
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
    "images/elisanne/faces/100002_01_parts_c007.png"
    0.05
    repeat

image elisanne_relaxed_eyes:
    "images/elisanne/faces/100002_01_parts_c016.png"
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
    "images/elisanne/faces/100002_01_parts_c017.png"
    0.05
    repeat

image elisanne_flinch_eyes:
    "images/elisanne/faces/100002_01_parts_c018.png"
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
    "images/elisanne/faces/100002_01_parts_c019.png"
    0.05
    repeat

image elisanne_surprised_eyes:
    "images/elisanne/faces/100002_01_parts_c020.png"
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
    "images/elisanne/faces/100002_01_parts_c021.png"
    0.05
    repeat

image elisanne_blush_eyes:
    "images/elisanne/faces/100002_01_parts_c022.png"
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
    "images/elisanne/faces/100002_01_parts_c023.png"
    0.05
    repeat

image elisanne_pained_eyes:
    "images/elisanne/faces/100002_01_parts_c032.png"
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
    "images/elisanne/faces/100002_01_parts_c033.png"
    0.05
    repeat

image elisanne_angry_eyes:
    "images/elisanne/faces/100002_01_parts_c034.png"
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
    "images/elisanne/faces/100002_01_parts_c035.png"
    0.05
    repeat

image elisanne_sad_eyes:
    "images/elisanne/faces/100002_01_parts_c043.png"
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
    "images/elisanne/faces/100002_01_parts_c044.png"
    0.05
    repeat


# MOUTH animations start here.

image elisanne_smile1_nottalking = "images/elisanne/mouths/100002_01_parts_c008.png"

image elisanne_smile1_talking:
    "images/elisanne/mouths/100002_01_parts_c008.png"
    0.15
    "images/elisanne/mouths/100002_01_parts_c009.png"
    0.15
    repeat

image elisanne_smile1 = WhileSpeaking("elly", "elisanne_smile1_talking", "elisanne_smile1_nottalking")


# 010/011, formerly "smile2," is actually the same as smile1 (008/009)


# 012/013, formerly "smile3," is actually the same as smile1 (008/009)


image elisanne_frown1_nottalking = "images/elisanne/mouths/100002_01_parts_c014.png"

image elisanne_frown1_talking:
    "images/elisanne/mouths/100002_01_parts_c014.png"
    0.15
    "images/elisanne/mouths/100002_01_parts_c015.png"
    0.15
    repeat

image elisanne_frown1 = WhileSpeaking("elly", "elisanne_frown1_talking", "elisanne_frown1_nottalking")


image elisanne_smile2_nottalking = "images/elisanne/mouths/100002_01_parts_c024.png"

image elisanne_smile2_talking:
    "images/elisanne/mouths/100002_01_parts_c024.png"
    0.15
    "images/elisanne/mouths/100002_01_parts_c025.png"
    0.15
    repeat

image elisanne_smile2 = WhileSpeaking("elly", "elisanne_smile2_talking", "elisanne_smile2_nottalking")


image elisanne_frown2_nottalking = "images/elisanne/mouths/100002_01_parts_c026.png"

image elisanne_frown2_talking:
    "images/elisanne/mouths/100002_01_parts_c026.png"
    0.15
    "images/elisanne/mouths/100002_01_parts_c027.png"
    0.15
    repeat

image elisanne_frown2 = WhileSpeaking("elly", "elisanne_frown2_talking", "elisanne_frown2_nottalking")


image elisanne_shout1_nottalking = "images/elisanne/mouths/100002_01_parts_c028.png"

image elisanne_shout1_talking:
    "images/elisanne/mouths/100002_01_parts_c028.png"
    0.15
    "images/elisanne/mouths/100002_01_parts_c029.png"
    0.15
    repeat

image elisanne_shout1 = WhileSpeaking("elly", "elisanne_shout1_talking", "elisanne_shout1_nottalking")


image elisanne_pout1_nottalking = "images/elisanne/mouths/100002_01_parts_c030.png"

image elisanne_pout1_talking:
    "images/elisanne/mouths/100002_01_parts_c030.png"
    0.15
    "images/elisanne/mouths/100002_01_parts_c031.png"
    0.15
    repeat

image elisanne_pout1 = WhileSpeaking("elly", "elisanne_pout1_talking", "elisanne_pout1_nottalking")


image elisanne_pout2_nottalking = "images/elisanne/mouths/100002_01_parts_c036.png"

image elisanne_pout2_talking:
    "images/elisanne/mouths/100002_01_parts_c036.png"
    0.15
    "images/elisanne/mouths/100002_01_parts_c037.png"
    0.15
    repeat

image elisanne_pout2 = WhileSpeaking("elly", "elisanne_pout2_talking", "elisanne_pout2_nottalking")


# 038/039, formerly "smile5," is actually the same as smile1 (008/009)


image elisanne_shout2_nottalking = "images/elisanne/mouths/100002_01_parts_c040.png"

image elisanne_shout2_talking:
    "images/elisanne/mouths/100002_01_parts_c040.png"
    0.15
    "images/elisanne/mouths/100002_01_parts_c041.png"
    0.15
    repeat

image elisanne_shout2 = WhileSpeaking("elly", "elisanne_shout2_talking", "elisanne_shout2_nottalking")


image elisanne_smile3_nottalking = "images/elisanne/mouths/100002_01_parts_c045.png"

image elisanne_smile3_talking:
    "images/elisanne/mouths/100002_01_parts_c045.png"
    0.15
    "images/elisanne/mouths/100002_01_parts_c046.png"
    0.15
    repeat

image elisanne_smile3 = WhileSpeaking("elly", "elisanne_smile3_talking", "elisanne_smile3_nottalking")














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

label elisanne_character_procedures:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image ellybedroom = "images/backgrounds/Sty_bg_0049_101_00.png"
    scene ellybedroom at middle

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    show elisanne with dissolve

    elly "Oh, hello, your Highness!"
    elly "I must admit that I was surprised when you said you wanted to check my facial expressions."
    elly "I'm a little nervous, but I suppose it won't be too bad if I imagine I'm an actor in a play."

    show elisanne neutral
    elly "I guess this is what I look like when I'm... neutral?"

    show elisanne neutral2
    elly "And this is sort of... a second neutral expression (neutral2)?"

    show elisanne closed_neutral
    elly "If I want to look neutral with closed eyes (closed_neutral), I suppose it would look like this."

    show elisanne focused
    elly "This is what I look like when I'm focused."

    show elisanne relaxed
    elly "I suppose this is more of a... relaxed expression?"

    show elisanne flinch
    elly "And... this is more of a flinch."

    show elisanne surprised
    elly "This is me acting... surprised!!"

    show elisanne blush
    elly "You... you want to see me blush?!  That is... quite uncouth, your Highness!"

    show elisanne sad
    elly "Yes... I suppose I shouldn't have reacted so.  This is me when i have sad eyes, i suppose."

    show elisanne pained
    elly "And this would be a slightly more pained expression."

    show elisanne angry
    elly "Oh!  And, these are, uh, my angry eyes!  Grr!"

    show elisanne neutral
    elly "Is that sufficient, your Highness?"
    elly "What?  You want me to change my mouth as well?"
    elly "Well, I suppose I can try."

    show elisanne smile1
    elly "But... this is my normal smile (smile1), is it not?"

    show elisanne smile2
    elly "Well.. here is a second smile (smile2)!"

    show elisanne smile3
    elly "And a third one (smile3)!"

    show elisanne frown1
    elly "Here's me frowning (frown1).  Although I've heard it takes more muscles to frown than to smile."

    show elisanne frown2
    elly "Well, we can make it a sort of paladin training regiment with this second one (frown2)!"

    show elisanne pout1
    elly "And this is a pout (pout1).  Don't I look cross?"

    show elisanne pout2
    elly "And... a second one that's slightly smaller (pout2)."

    show elisanne shout1
    elly "And... here is a mighty shout!!!  (shout1)"

    show elisanne shout2
    elly "And an even louder one!!!! (shout2)"

    show elisanne smile1
    elly "What?  I can stop now?  Whew, I'm relieved."
    elly "I do not fully understand why you asked me to do this, but..."
    elly "...if i was able to assist you, that makes me happy."
    elly "Let us both continue to do our best moving forward!"


    # This goes back to script

    jump testfiles
