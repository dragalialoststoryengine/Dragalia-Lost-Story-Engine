
    # Euden Character Procedures File

    # Paste this file into a story if you want to use Euden.  These procedures animate Euden as a speaker.
    # You'll also need to paste THIS line into your actual script above the script label whenever you're using Euden:

define eud = Character("Euden", callback=speaker("eud"))

    # This program assumes that the following folders exist:
    #     -"images/euden"
    #     -"images/euden/faces"
    #     -"images/euden/mouths"

    # Euden dynamically blinks and, while speaking, also moves her mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Euden appear*:
    #  -->  show euden with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Euden's eyes*:
    #  -->  show euden [keyword]
    #  List of eye keywords:
    #     -->  focused (default), focused2, focused3, angry, blank, blush_surprised, blush_focused,
    #          closed_focused, flinch, relaxed, closed_relaxed, sad, closed_sad, smirk, surprised,
    #          closed_blush_focused


    # *Changing Euden's mouth*:
    #  -->  show euden [keyword]
    #  List of mouth keywords:
    #     -->  smile1 (default), smile2, smile3, smallsmile1, bigsmile1, frown1,
    #          grimace1, grimace2, grimace3, skew_smile1, skew_frown1, shout1, sweat_frown1,
    #          closed_smile1


    # smallsmile1 and smile3 are the ones with teeth.  frown1 is kind of a pout.  Maybe i should fix this terminology later...

    # *Writing dialogue for Euden*:
    #  --> eud "[Euden's line here]"

    # *Making Euden disappear*:
    #  --> hide euden with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage euden:

    always "images/euden/euden_body.png"

    group face:

        # 444/1028, 231/1028:
        pos (0.43191, 0.22471)

        attribute focused default:
            "euden_focused_eyes"

        attribute closed_focused:
            "images/euden/faces/100001_01_parts_c001.png"

        attribute focused2:
            "euden_focused2_eyes"

        attribute relaxed:
            "euden_relaxed_eyes"

        attribute closed_relaxed:
            "images/euden/faces/100001_01_parts_c013.png"

        attribute flinch:
            "euden_flinch_eyes"

        attribute surprised:
            "euden_surprised_eyes"

        attribute blush_surprised:
            "euden_blush_surprised_eyes"

        attribute angry:
            "euden_angry_eyes"

        attribute blush_focused:
            "euden_blush_focused_eyes"

        attribute closed_blush_focused:
            "images/euden/faces/100001_01_parts_c031.png"

        attribute focused3:
            "euden_focused3_eyes"

        attribute sad:
            "euden_sad_eyes"

        attribute closed_sad:
            "images/euden/faces/100001_01_parts_c042.png"

        attribute blank:
            "euden_blank_eyes"

        attribute pained:
            "euden_pained_eyes"

        attribute smirk:
            "euden_smirk_eyes"


    group mouth:

        pos (0.43191, 0.22471)

        attribute smile1 default:
            "euden_smile1"

        attribute closed_smile1:
            "euden_smile1_nottalking"

        attribute grimace1:
            "euden_grimace1"

        attribute smile2:
            "euden_smile2"

        attribute grimace2:
            "euden_grimace2"

        attribute sweat_frown1:
            "euden_sweat_frown1"

        attribute frown1:
            "euden_frown1"

        attribute skew_frown1:
            "euden_skew_frown1"

        attribute bigsmile1:
            "euden_bigsmile1"

        attribute shout1:
            "euden_shout1"

        attribute smallsmile1:
            "euden_smallsmile1"

        attribute smile3:
            "euden_smile3"

        attribute grimace3:
            "euden_grimace3"

        attribute skew_smile1:
            "euden_skew_smile1"


## EYE animations start here.

image euden_focused_eyes:
    "images/euden/faces/100001_01_parts_c000.png"
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
    "images/euden/faces/100001_01_parts_c001.png"
    0.05
    repeat

image euden_focused2_eyes:
    "images/euden/faces/100001_01_parts_c004.png"
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
    "images/euden/faces/100001_01_parts_c005.png"
    0.05
    repeat

image euden_relaxed_eyes:
    "images/euden/faces/100001_01_parts_c012.png"
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
    "images/euden/faces/100001_01_parts_c013.png"
    0.05
    repeat

image euden_flinch_eyes:
    "images/euden/faces/100001_01_parts_c014.png"
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
    "images/euden/faces/100001_01_parts_c015.png"
    0.05
    repeat

image euden_surprised_eyes:
    "images/euden/faces/100001_01_parts_c016.png"
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
    "images/euden/faces/100001_01_parts_c017.png"
    0.05
    repeat

image euden_blush_surprised_eyes:
    "images/euden/faces/100001_01_parts_c018.png"
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
    "images/euden/faces/100001_01_parts_c019.png"
    0.05
    repeat

image euden_angry_eyes:
    "images/euden/faces/100001_01_parts_c028.png"
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
    "images/euden/faces/100001_01_parts_c029.png"
    0.05
    repeat

image euden_blush_focused_eyes:
    "images/euden/faces/100001_01_parts_c030.png"
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
    "images/euden/faces/100001_01_parts_c031.png"
    0.05
    repeat

image euden_focused3_eyes:
    "images/euden/faces/100001_01_parts_c032.png"
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
    "images/euden/faces/100001_01_parts_c033.png"
    0.05
    repeat

image euden_sad_eyes:
    "images/euden/faces/100001_01_parts_c041.png"
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
    "images/euden/faces/100001_01_parts_c042.png"
    0.05
    repeat

image euden_blank_eyes:
    "images/euden/faces/100001_01_parts_c043.png"
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
    "images/euden/faces/100001_01_parts_c044.png"
    0.05
    repeat

image euden_pained_eyes:
    "images/euden/faces/100001_01_parts_c045.png"
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
    "images/euden/faces/100001_01_parts_c046.png"
    0.05
    repeat

image euden_smirk_eyes:
    "images/euden/faces/100001_01_parts_c047.png"
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
    "images/euden/faces/100001_01_parts_c048.png"
    0.05
    repeat



# MOUTH animations start here.

image euden_smile1_nottalking = "images/euden/mouths/100001_01_parts_c006.png"

image euden_smile1_talking:
    "images/euden/mouths/100001_01_parts_c007.png"
    0.15
    "images/euden/mouths/100001_01_parts_c006.png"
    0.15
    repeat

image euden_smile1 = WhileSpeaking("eud", "euden_smile1_talking", "euden_smile1_nottalking")


#008 and 009 are the same as 006 and 007.


image euden_grimace1_nottalking = "images/euden/mouths/100001_01_parts_c010.png"

image euden_grimace1_talking:
    "images/euden/mouths/100001_01_parts_c011.png"
    0.15
    "images/euden/mouths/100001_01_parts_c010.png"
    0.15
    repeat

image euden_grimace1 = WhileSpeaking("eud", "euden_grimace1_talking", "euden_grimace1_nottalking")


image euden_smile2_nottalking = "images/euden/mouths/100001_01_parts_c020.png"

image euden_smile2_talking:
    "images/euden/mouths/100001_01_parts_c021.png"
    0.15
    "images/euden/mouths/100001_01_parts_c020.png"
    0.15
    repeat

image euden_smile2 = WhileSpeaking("eud", "euden_smile2_talking", "euden_smile2_nottalking")


image euden_grimace2_nottalking = "images/euden/mouths/100001_01_parts_c022.png"

image euden_grimace2_talking:
    "images/euden/mouths/100001_01_parts_c023.png"
    0.15
    "images/euden/mouths/100001_01_parts_c022.png"
    0.15
    repeat

image euden_grimace2 = WhileSpeaking("eud", "euden_grimace2_talking", "euden_grimace2_nottalking")


image euden_sweat_frown1_nottalking = "images/euden/mouths/100001_01_parts_c024.png"

image euden_sweat_frown1_talking:
    "images/euden/mouths/100001_01_parts_c025.png"
    0.15
    "images/euden/mouths/100001_01_parts_c024.png"
    0.15
    repeat

image euden_sweat_frown1 = WhileSpeaking("eud", "euden_sweat_frown1_talking", "euden_sweat_frown1_nottalking")


image euden_frown1_nottalking = "images/euden/mouths/100001_01_parts_c026.png"

image euden_frown1_talking:
    "images/euden/mouths/100001_01_parts_c027.png"
    0.15
    "images/euden/mouths/100001_01_parts_c026.png"
    0.15
    repeat

image euden_frown1 = WhileSpeaking("eud", "euden_frown1_talking", "euden_frown1_nottalking")


image euden_skew_frown1_nottalking = "images/euden/mouths/100001_01_parts_c035.png"

image euden_skew_frown1_talking:
    "images/euden/mouths/100001_01_parts_c036.png"
    0.15
    "images/euden/mouths/100001_01_parts_c035.png"
    0.15
    repeat

image euden_skew_frown1 = WhileSpeaking("eud", "euden_skew_frown1_talking", "euden_skew_frown1_nottalking")


image euden_bigsmile1_nottalking = "images/euden/mouths/100001_01_parts_c037.png"

image euden_bigsmile1_talking:
    "images/euden/mouths/100001_01_parts_c038.png"
    0.15
    "images/euden/mouths/100001_01_parts_c037.png"
    0.15
    repeat

image euden_bigsmile1 = WhileSpeaking("eud", "euden_bigsmile1_talking", "euden_bigsmile1_nottalking")


image euden_shout1_nottalking = "images/euden/mouths/100001_01_parts_c039.png"

image euden_shout1_talking:
    "images/euden/mouths/100001_01_parts_c040.png"
    0.15
    "images/euden/mouths/100001_01_parts_c039.png"
    0.15
    repeat

image euden_shout1 = WhileSpeaking("eud", "euden_shout1_talking", "euden_shout1_nottalking")


image euden_smallsmile1_nottalking = "images/euden/mouths/100001_01_parts_c049.png"

image euden_smallsmile1_talking:
    "images/euden/mouths/100001_01_parts_c050.png"
    0.15
    "images/euden/mouths/100001_01_parts_c049.png"
    0.15
    repeat

image euden_smallsmile1 = WhileSpeaking("eud", "euden_smallsmile1_talking", "euden_smallsmile1_nottalking")


image euden_smile3_nottalking = "images/euden/mouths/100001_01_parts_c051.png"

image euden_smile3_talking:
    "images/euden/mouths/100001_01_parts_c052.png"
    0.15
    "images/euden/mouths/100001_01_parts_c051.png"
    0.15
    repeat

image euden_smile3 = WhileSpeaking("eud", "euden_smile3_talking", "euden_smile3_nottalking")


image euden_grimace3_nottalking = "images/euden/mouths/100001_01_parts_c053.png"

image euden_grimace3_talking:
    "images/euden/mouths/100001_01_parts_c053.png"
    0.15
    "images/euden/mouths/100001_01_parts_c054.png"
    0.15
    repeat

image euden_grimace3 = WhileSpeaking("eud", "euden_grimace3_talking", "euden_grimace3_nottalking")


image euden_skew_smile1_nottalking = "images/euden/mouths/100001_01_parts_c055.png"

image euden_skew_smile1_talking:
    "images/euden/mouths/100001_01_parts_c056.png"
    0.15
    "images/euden/mouths/100001_01_parts_c055.png"
    0.15
    repeat

image euden_skew_smile1 = WhileSpeaking("eud", "euden_skew_smile1_talking", "euden_skew_smile1_nottalking")




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

label euden_character_procedures:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image halidom_hall = "images/backgrounds/Sty_bg_0024_100_00.png"
    scene halidom_hall

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show euden with dissolve
    eud "Hey there!  Thanks for trying out the Dragalia Lost Story Engine!"
    eud "If you're delving into this file, it means you want to make sure all my animations are working properly."
    eud "I appreciate you taking the time to take care of me!  Please make sure everything's in order, ok?"

    show euden focused smile1
    eud "This is the 'focused' face and 'smile1' mouth."

    show euden focused2 smile2
    eud "This is the 'focused2' face and 'smile2' mouth."

    show euden focused3 smile3
    eud "This is the 'focused3' face and 'smile3' mouth."

    show euden angry grimace3
    eud "This is the 'angry' face and 'grimace3' mouth."

    show euden blank bigsmile1
    eud "This is the 'blank' face and 'bigsmile1' mouth."

    show euden blush_focused frown1
    eud "This is the 'blush_focused' face and 'frown1' mouth."

    show euden blush_surprised grimace1
    eud "This is the 'blush_surprised' face and 'grimace1' mouth."

    show euden flinch grimace2
    eud "This is the 'flinch' face and 'grimace2' mouth."

    show euden relaxed smallsmile1
    eud "This is the 'relaxed' face and 'smallsmile1' mouth."

    show euden sad skew_frown1
    eud "This is the sad' face and 'skew_frown1' mouth."

    show euden smirk skew_smile1
    eud "This is the 'smirk' face and 'skew_smile1' mouth."

    show euden surprised shout1
    eud "This is the 'surprised' face and 'shout1' mouth."

    show euden closed_focused sweat_frown1
    eud "And, last but not least, this is the 'closed_focused' face and 'sweat_frown1' mouth."

    show euden relaxed smile1
    eud "Did everything come out ok?  If not, let me know!"
    eud "And while you're here, please enjoy your time with the Dragalia Lost Story Engine."
    eud "Thanks again!"


    hide euden with dissolve

    # This goes back to script

    jump testfiles
