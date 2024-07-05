    # Gala Emile Character Procedures File

    # Paste this file into a story if you want to use Gala Emile.  These procedures animate Gala Emile as a speaker.

define emil = Character("Emile", callback=speaker("emil"))

    # This program assumes that the following folders exist:
    #     -"images/emile_gala"
    #     -"images/emile_gala/faces"
    #     -"images/emile_gala/mouths"

    # Gala Emile dynamically blinks and, while speaking, also moves his mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Gala Emile appear*:
    #  -->  show gemile with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Gala Emile's eyes*:
    #  -->  show gemile [keyword]
    #  List of eye keywords:
    #     -->  neutral (the default option), neutral2, closed_neutral, angry, askance, blush,
    #          cry, focused, sad, shocked, squint, surprised, closed_cry

    # *Changing Gala Emile's mouth*:
    #  -->  show gemile [keyword]
    #  List of mouth keywords:
    #     -->  smile1 (the default option), smile2, smile3, frown1, frown2, grimace1, grimace2,
    #          pout1, mutter1, shout1, sweat_grimace1

    # *Writing dialogue for Gala Emile*:
    #  --> emil "[Gala Emile's line here]"

    # *Making Gala Emile disappear*:
    #  --> hide gemile with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage gemile:

    always "images/emile_gala/emile_gala_body.png"

    group face:

        # 447/1024, 194/1024:
        pos (0.4365234, 0.1894531)

        attribute neutral default:
            "gemile_neutral_eyes"

        attribute closed_neutral:
            "images/emile_gala/faces/100017_03_parts_c001.png"

        attribute focused:
            "gemile_focused_eyes"

        attribute neutral2:
            "gemile_neutral2_eyes"

        attribute shocked:
            "gemile_shocked_eyes"

        attribute surprised:
            "gemile_surprised_eyes"

        attribute blush:
            "gemile_blush_eyes"

        attribute sad:
            "gemile_sad_eyes"

        attribute angry:
            "gemile_angry_eyes"

        attribute closed_cry:
            "images/emile_gala/faces/100017_03_parts_c036.png"

        attribute cry:
            "gemile_cry_eyes"

        attribute askance:
            "gemile_askance_eyes"

        attribute squint:
            "gemile_squint_eyes"



    group mouth:

        pos (0.4365234, 0.1894531)

        attribute smile1 default:
            "gemile_smile1"

        attribute frown1:
            "gemile_frown1"

        attribute closed_frown1:
            "images/emile_gala/mouths/100017_03_parts_c006.png"

        attribute smile2:
            "gemile_smile2"

        attribute grimace1:
            "gemile_grimace1"

        attribute frown2:
            "gemile_frown2"

        attribute smile3:
            "gemile_smile3"

        attribute grimace2:
            "gemile_grimace2"

        attribute sweat_grimace1:
            "gemile_sweat_grimace1"

        attribute pout1:
            "gemile_pout1"

        attribute mutter1:
            "gemile_mutter1"

        attribute shout1:
            "gemile_shout1"



## EYE animations start here.

image gemile_neutral_eyes:
    "images/emile_gala/faces/100017_03_parts_c000.png"
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
    "images/emile_gala/faces/100017_03_parts_c001.png"
    0.05
    repeat

image gemile_focused_eyes:
    "images/emile_gala/faces/100017_03_parts_c002.png"
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
    "images/emile_gala/faces/100017_03_parts_c003.png"
    0.05
    repeat

image gemile_neutral2_eyes:
    "images/emile_gala/faces/100017_03_parts_c008.png"
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
    "images/emile_gala/faces/100017_03_parts_c009.png"
    0.05
    repeat

image gemile_shocked_eyes:
    "images/emile_gala/faces/100017_03_parts_c010.png"
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
    "images/emile_gala/faces/100017_03_parts_c011.png"
    0.05
    repeat

image gemile_surprised_eyes:
    "images/emile_gala/faces/100017_03_parts_c012.png"
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
    "images/emile_gala/faces/100017_03_parts_c013.png"
    0.05
    repeat

image gemile_blush_eyes:
    "images/emile_gala/faces/100017_03_parts_c014.png"
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
    "images/emile_gala/faces/100017_03_parts_c015.png"
    0.05
    repeat

image gemile_sad_eyes:
    "images/emile_gala/faces/100017_03_parts_c024.png"
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
    "images/emile_gala/faces/100017_03_parts_c025.png"
    0.05
    repeat

image gemile_angry_eyes:
    "images/emile_gala/faces/100017_03_parts_c026.png"
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
    "images/emile_gala/faces/100017_03_parts_c027.png"
    0.05
    repeat

image gemile_cry_eyes:
    "images/emile_gala/faces/100017_03_parts_c035.png"
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
    "images/emile_gala/faces/100017_03_parts_c036.png"
    0.05
    repeat

image gemile_askance_eyes:
    "images/emile_gala/faces/100017_03_parts_c037.png"
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
    "images/emile_gala/faces/100017_03_parts_c038.png"
    0.05
    repeat

image gemile_squint_eyes:
    "images/emile_gala/faces/100017_03_parts_c039.png"
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
    "images/emile_gala/faces/100017_03_parts_c040.png"
    0.05
    repeat



# MOUTH animations start here.

image gemile_smile1_nottalking = "images/emile_gala/mouths/100017_03_parts_c004.png"

image gemile_smile1_talking:
    "images/emile_gala/mouths/100017_03_parts_c005.png"
    0.15
    "images/emile_gala/mouths/100017_03_parts_c004.png"
    0.15
    repeat

image gemile_smile1 = WhileSpeaking("emil", "gemile_smile1_talking", "gemile_smile1_nottalking")


image gemile_frown1_nottalking = "images/emile_gala/mouths/100017_03_parts_c006.png"

image gemile_frown1_talking:
    "images/emile_gala/mouths/100017_03_parts_c007.png"
    0.15
    "images/emile_gala/mouths/100017_03_parts_c006.png"
    0.15
    repeat

image gemile_frown1 = WhileSpeaking("emil", "gemile_frown1_talking", "gemile_frown1_nottalking")


image gemile_smile2_nottalking = "images/emile_gala/mouths/100017_03_parts_c016.png"

image gemile_smile2_talking:
    "images/emile_gala/mouths/100017_03_parts_c017.png"
    0.15
    "images/emile_gala/mouths/100017_03_parts_c016.png"
    0.15
    repeat

image gemile_smile2 = WhileSpeaking("emil", "gemile_smile2_talking", "gemile_smile2_nottalking")


image gemile_grimace1_nottalking = "images/emile_gala/mouths/100017_03_parts_c018.png"

image gemile_grimace1_talking:
    "images/emile_gala/mouths/100017_03_parts_c019.png"
    0.15
    "images/emile_gala/mouths/100017_03_parts_c018.png"
    0.15
    repeat

image gemile_grimace1 = WhileSpeaking("emil", "gemile_grimace1_talking", "gemile_grimace1_nottalking")


image gemile_frown2_nottalking = "images/emile_gala/mouths/100017_03_parts_c020.png"

image gemile_frown2_talking:
    "images/emile_gala/mouths/100017_03_parts_c021.png"
    0.15
    "images/emile_gala/mouths/100017_03_parts_c020.png"
    0.15
    repeat

image gemile_frown2 = WhileSpeaking("emil", "gemile_frown2_talking", "gemile_frown2_nottalking")


image gemile_smile3_nottalking = "images/emile_gala/mouths/100017_03_parts_c022.png"

image gemile_smile3_talking:
    "images/emile_gala/mouths/100017_03_parts_c023.png"
    0.15
    "images/emile_gala/mouths/100017_03_parts_c022.png"
    0.15
    repeat

image gemile_smile3 = WhileSpeaking("emil", "gemile_smile3_talking", "gemile_smile3_nottalking")


image gemile_grimace2_nottalking = "images/emile_gala/mouths/100017_03_parts_c029.png"

image gemile_grimace2_talking:
    "images/emile_gala/mouths/100017_03_parts_c030.png"
    0.15
    "images/emile_gala/mouths/100017_03_parts_c029.png"
    0.15
    repeat

image gemile_grimace2 = WhileSpeaking("emil", "gemile_grimace2_talking", "gemile_grimace2_nottalking")


image gemile_sweat_grimace1_nottalking = "images/emile_gala/mouths/100017_03_parts_c031.png"

image gemile_sweat_grimace1_talking:
    "images/emile_gala/mouths/100017_03_parts_c032.png"
    0.15
    "images/emile_gala/mouths/100017_03_parts_c031.png"
    0.15
    repeat

image gemile_sweat_grimace1 = WhileSpeaking("emil", "gemile_sweat_grimace1_talking", "gemile_sweat_grimace1_nottalking")


image gemile_pout1_nottalking = "images/emile_gala/mouths/100017_03_parts_c041.png"

image gemile_pout1_talking:
    "images/emile_gala/mouths/100017_03_parts_c042.png"
    0.15
    "images/emile_gala/mouths/100017_03_parts_c041.png"
    0.15
    repeat

image gemile_pout1 = WhileSpeaking("emil", "gemile_pout1_talking", "gemile_pout1_nottalking")


# 033 / 034 are the same as 004 / 005


image gemile_mutter1_nottalking = "images/emile_gala/mouths/100017_03_parts_c043.png"

image gemile_mutter1_talking:
    "images/emile_gala/mouths/100017_03_parts_c044.png"
    0.15
    "images/emile_gala/mouths/100017_03_parts_c043.png"
    0.15
    repeat

image gemile_mutter1 = WhileSpeaking("emil", "gemile_mutter1_talking", "gemile_mutter1_nottalking")


image gemile_shout1_nottalking = "images/emile_gala/mouths/100017_03_parts_c045.png"

image gemile_shout1_talking:
    "images/emile_gala/mouths/100017_03_parts_c046.png"
    0.15
    "images/emile_gala/mouths/100017_03_parts_c045.png"
    0.15
    repeat

image gemile_shout1 = WhileSpeaking("emil", "gemile_shout1_talking", "gemile_shout1_nottalking")





# The test file script starts here.

label emileG_character_procedures:

    image schoolroom = "images/backgrounds/Sty_bg_0035_100_00.png"
    scene schoolroom with fade

    show gemile with dissolve
    emil "Hmmhmmhmm!  It looks like I'm early to the classroom today!"

    show gemile neutral smile1
    emil "(neutral smile1) And that means I have the perfect chance to decide exactly how to pose as the class's model!"

    show gemile neutral2 smile2
    emil "(neutral2 smile2) It's a good thing I came equipped with this mirror!  Now I can pick exactly the right face and angle to capture my unmatcheable brilliance!!"

    show gemile closed_neutral smile3
    emil "(closed_neutral smile3) Now... let me think... The class is used to most of my usual poses, so I've got to think of something really outside the box!!"

    show gemile neutral smile1
    emil "(neutral smile1) And that means I have the perfect chance to decide exactly how to pose as the class's model!"

    show gemile angry frown1
    emil "(angry frown1) How about... a dramatic battle pose!  I could hold my scepter aloft with a dramatic expresison like this!!"

    show gemile askance frown2
    emil "(askance frown2) ...No, as much as I want to flout my military might, I don't think that's the impression I want to leave on these children..."

    show gemile blush grimace1
    emil "(blush grimace1) I... I know too well what it's like for my family to be torn apart by war.  I... I want to be remembered, but not for being a warmonger.  Not anymore."

    show gemile focused grimace2
    emil "(focused grimace2) Ok, well... if not that, what SHOULD I do for a pose?"

    show gemile sad mutter1
    emil "(sad mutter1) What about... pathos!  I'm the Artist King!  To live in this world is to suffer, and if I strike an impassioned pose, these childern will be prepared for those tragedies!"

    show gemile cry pout1
    emil "(cry pout1) Yes... the suffering of being outshone by all your siblings... (sniff) and being mocked by your own people... (sniffle) and having a vengeful ex-pactdragon with a vendetta against you..."

    show gemile squint sweat_grimace1
    emil "(squint sweat_grimace1) ...Okay, that's a little TOO real... if I start crying in front of a bunch of children, I'll never hear the end of it!  Especially if it was ALSO in front of..."

    "(click)"

    show gemile surprised mutter1
    emil "(surprised mutter1) ...Mercur...y..."

    show gemile shocked shout1
    emil "(shocked shout1) -M-M-MERCURY?!?  H-HOW LONG HAVE YOU BEEN STANDING THERE?!?"

    show gemile askance sweat_grimace1
    emil "I-I'll have you know that I was simply... rehearsing a PLAY for the children!!!  Involving a... tragic hero character!!!  It DEFINITELY wasn't about ME or anything!"

    show gemile blush pout1
    emil "Wh-WHY ARE YOU LOOKING AT ME LIKE THAT?!??!?"



    hide gemile with dissolve


    # This goes back to script

    jump testfiles
