    # Linus Character Procedures File

    # Paste this file into a story if you want to use Linus.  These procedures animate Linus as a speaker.

define linu = Character("Linus", callback=speaker("linu"))

    # This program assumes that the following folders exist:
    #     -"images/linus"
    #     -"images/linus/faces"
    #     -"images/linus/mouths"

    # Linus dynamically blinks and, while speaking, also moves his mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Linus appear*:
    #  -->  show linus with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Linus's eyes*:
    #  -->  show linus [keyword]
    #  List of eye keywords:
    #     -->  focused (default), closed_focused, angry, relaxed, flinch

    # *Changing Linus's mouth*:
    #  -->  show linus [keyword]
    #  List of mouth keywords:
    #     -->  smile1 (default), duchenne1, frown1, grimace1, grin1, shout1

    # *Writing dialogue for Linus*:
    #  --> linu "[Linus's line here]"

    # *Making Linus disappear*:
    #  --> hide linus with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage linus:

    always "images/linus/linus_body.png"

    group face:

        # 467/1024, 266/1024:
        pos (0.4560546875, 0.259765625)

        attribute focused default:
            "linus_focused_eyes"

        attribute closed_focused:
            "images/linus/faces/110033_01_parts_c001.png"

        attribute angry:
            "linus_angry_eyes"

        attribute relaxed:
            "linus_relaxed_eyes"

        attribute flinch:
            "linus_flinch_eyes"


    group mouth:

        pos (0.4560546875, 0.259765625)

        attribute smile1 default:
            "linus_smile1"

        attribute shout1:
            "linus_shout1"

        attribute grin1:
            "linus_grin1"

        attribute grimace1:
            "linus_grimace1"

        attribute duchenne1:
            "linus_duchenne1"

        attribute frown1:
            "linus_frown1"





## EYE animations start here.

image linus_focused_eyes:
    "images/linus/faces/110033_01_parts_c000.png"
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
    "images/linus/faces/110033_01_parts_c001.png"
    0.05
    repeat

image linus_angry_eyes:
    "images/linus/faces/110033_01_parts_c002.png"
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
    "images/linus/faces/110033_01_parts_c003.png"
    0.05
    repeat

image linus_relaxed_eyes:
    "images/linus/faces/110033_01_parts_c008.png"
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
    "images/linus/faces/110033_01_parts_c009.png"
    0.05
    repeat

image linus_flinch_eyes:
    "images/linus/faces/110033_01_parts_c010.png"
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
    "images/linus/faces/110033_01_parts_c011.png"
    0.05
    repeat



# MOUTH animations start here.

image linus_smile1_nottalking = "images/linus/mouths/110033_01_parts_c004.png"

image linus_smile1_talking:
    "images/linus/mouths/110033_01_parts_c005.png"
    0.15
    "images/linus/mouths/110033_01_parts_c004.png"
    0.15
    repeat

image linus_smile1 = WhileSpeaking("linu", "linus_smile1_talking", "linus_smile1_nottalking")


image linus_shout1_nottalking = "images/linus/mouths/110033_01_parts_c006.png"

image linus_shout1_talking:
    "images/linus/mouths/110033_01_parts_c007.png"
    0.15
    "images/linus/mouths/110033_01_parts_c006.png"
    0.15
    repeat

image linus_shout1 = WhileSpeaking("linu", "linus_shout1_talking", "linus_shout1_nottalking")


image linus_grin1_nottalking = "images/linus/mouths/110033_01_parts_c012.png"

image linus_grin1_talking:
    "images/linus/mouths/110033_01_parts_c013.png"
    0.15
    "images/linus/mouths/110033_01_parts_c012.png"
    0.15
    repeat

image linus_grin1 = WhileSpeaking("linu", "linus_grin1_talking", "linus_grin1_nottalking")


image linus_grimace1_nottalking = "images/linus/mouths/110033_01_parts_c014.png"

image linus_grimace1_talking:
    "images/linus/mouths/110033_01_parts_c015.png"
    0.15
    "images/linus/mouths/110033_01_parts_c014.png"
    0.15
    repeat

image linus_grimace1 = WhileSpeaking("linu", "linus_grimace1_talking", "linus_grimace1_nottalking")


# It looks like there are smiles identical to smile1 (004 / 005), but reversed.  016/017 and 018 follow this pattern.
# As a result, I'm going to define a new smile 'duchenne' that's open-mouthed, but uses the same resources.
# 016, 017, 018 deleted.


image linus_duchenne1_nottalking = "images/linus/mouths/110033_01_parts_c005.png"

image linus_duchenne1_talking:
    "images/linus/mouths/110033_01_parts_c004.png"
    0.15
    "images/linus/mouths/110033_01_parts_c005.png"
    0.15
    repeat

image linus_duchenne1 = WhileSpeaking("linu", "linus_duchenne1_talking", "linus_duchenne1_nottalking")


image linus_frown1_nottalking = "images/linus/mouths/110033_01_parts_c019.png"

image linus_frown1_talking:
    "images/linus/mouths/110033_01_parts_c020.png"
    0.15
    "images/linus/mouths/110033_01_parts_c019.png"
    0.15
    repeat

image linus_frown1 = WhileSpeaking("linu", "linus_frown1_talking", "linus_frown1_nottalking")





# The test file script starts here.

label linus_character_procedures:

    image alleyway_day = "images/backgrounds/Sty_bg_0028_100_00.png"
    scene alleyway_day with fade

    show linus with dissolve
    linu "Heh.  Looks like things're going pretty well for the ol' hometown.  Even the alleyways are quiet 'n safe."

    show linus focused smile1
    linu "(focused smile1) Looks like they were able to pull through without me after all."

    show linus closed_focused frown1
    linu "(closed_focused frown1) But... why the heck're ya following me around again?  I don't need a babysitter."

    show linus flinch grimace1
    linu "(flinch grimce1) It's freakin' annoying, man.  Don't you have anything better to do than stare at me?"

    show linus angry shout1
    linu "(angry shout1) \"You had a short gap in your schedule?!\"  That had BETTER not be a height joke, or I'll smash yer sternum!!!"

    show linus relaxed grin1
    linu "(relaxed grin1) ...Heh, sorry, man.  I guess I still got a bit of a chip on my shoulder 'bout it.  I have to deal with hecklers all the time."

    show linus focused duchenne1
    linu "(duchenne1) But hey, lemme make it up to you at the tavern!  A real men's hangout, right?  Race ya there!"

    hide linus with dissolve


    # This goes back to script

    jump testfiles
