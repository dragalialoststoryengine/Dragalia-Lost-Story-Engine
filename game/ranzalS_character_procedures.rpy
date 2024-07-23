    # Summer Ranzal Character Procedures File

    # Paste this file into a story if you want to use Summer Ranzal.  These procedures animate Summer Ranzal as a speaker.

#define ranz = Character("Ranzal", callback=speaker("ranz"))

    # This program assumes that the following folders exist:
    #     -"images/ranzal_summer"
    #     -"images/ranzal_summer/faces"
    #     -"images/ranzal_summer/mouths"

    # Summer Ranzal dynamically blinks and, while speaking, also moves his mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Summer Ranzal appear*:
    #  -->  show sranzal with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Summer Ranzal's body*:
    #  -->  show sranzal [keyword]
    #  List of body keywords:
    #     -->  normal (the default option), bbq

    # *Changing Summer Ranzal's eyes*:
    #  -->  show sranzal [keyword]
    #  List of eye keywords:
    #     -->  neutral (the default option), closed_neutral, angry, flinch,
    #          focused, relaxed, shocked, squint, surprised, wink

    # *Changing Summer Ranzal's mouth*:
    #  -->  show sranzal [keyword]
    #  List of mouth keywords:
    #     -->  grin1 (the default option), grin2, frown1, frown2, grimace1, grimace2, mutter1, shout1, smile1, smile2,
    #           mutter1_closed

    # *Writing dialogue for Summer Ranzal*:
    #  --> ranz "[Ranzal's line here]"

    # *Making Summer Ranzal disappear*:
    #  --> hide sranzal with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage sranzal:

    group body:

        attribute normal default:
            "images/ranzal_summer/ranzal_summer_body.png"

        attribute bbq:
            "images/ranzal_summer/ranzal_summer_bbq_body.png"

    group face:

        # 423/1024, 164/1024:
        pos (0.4130859, 0.160156)

        attribute neutral default:
            "sranzal_neutral_eyes"

        attribute closed_neutral:
            "images/ranzal_summer/faces/100003_04_parts_c001.png"

        attribute focused:
            "sranzal_focused_eyes"

        attribute relaxed:
            "sranzal_relaxed_eyes"

        attribute flinch:
            "sranzal_flinch_eyes"

        attribute surprised:
            "sranzal_surprised_eyes"

        attribute wink:
            "sranzal_wink_eyes"

        attribute squint:
            "sranzal_squint_eyes"

        attribute angry:
            "sranzal_angry_eyes"

        attribute shocked:
            "sranzal_shocked_eyes"


    group mouth:

        pos (0.4130859, 0.160156)

        attribute grin1 default:
            "sranzal_grin1"

        attribute frown2:
            "sranzal_frown2"

        attribute smile2:
            "sranzal_smile2"

        attribute grimace2:
            "sranzal_grimace2"
        
        attribute frown1:
            "sranzal_frown1"
        
        attribute grin2:
            "sranzal_grin2"

        attribute grimace1:
            "sranzal_grimace1"

        attribute mutter1:
            "sranzal_mutter1"

        attribute mutter1_closed:
            "sranzal_mutter1_nottalking"

        attribute shout1:
            "sranzal_shout1"

        attribute smile1:
            "sranzal_smile1"



## EYE animations start here.

image sranzal_neutral_eyes:
    "images/ranzal_summer/faces/100003_04_parts_c000.png"
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
    "images/ranzal_summer/faces/100003_04_parts_c001.png"
    0.05
    repeat

image sranzal_focused_eyes:
    "images/ranzal_summer/faces/100003_04_parts_c006.png"
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
    "images/ranzal_summer/faces/100003_04_parts_c007.png"
    0.05
    repeat

image sranzal_relaxed_eyes:
    "images/ranzal_summer/faces/100003_04_parts_c016.png"
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
    "images/ranzal_summer/faces/100003_04_parts_c017.png"
    0.05
    repeat

image sranzal_flinch_eyes:
    "images/ranzal_summer/faces/100003_04_parts_c018.png"
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
    "images/ranzal_summer/faces/100003_04_parts_c019.png"
    0.05
    repeat

image sranzal_surprised_eyes:
    "images/ranzal_summer/faces/100003_04_parts_c020.png"
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
    "images/ranzal_summer/faces/100003_04_parts_c021.png"
    0.05
    repeat

image sranzal_wink_eyes:
    "images/ranzal_summer/faces/100003_04_parts_c022.png"
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
    "images/ranzal_summer/faces/100003_04_parts_c023.png"
    0.05
    repeat

image sranzal_squint_eyes:
    "images/ranzal_summer/faces/100003_04_parts_c032.png"
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
    "images/ranzal_summer/faces/100003_04_parts_c033.png"
    0.05
    repeat

image sranzal_angry_eyes:
    "images/ranzal_summer/faces/100003_04_parts_c034.png"
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
    "images/ranzal_summer/faces/100003_04_parts_c035.png"
    0.05
    repeat

image sranzal_shocked_eyes:
    "images/ranzal_summer/faces/100003_04_parts_c036.png"
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
    "images/ranzal_summer/faces/100003_04_parts_c037.png"
    0.05
    repeat







# MOUTH animations start here.

image sranzal_grin1_nottalking = "images/ranzal_summer/mouths/100003_04_parts_c008.png"

image sranzal_grin1_talking:
    "images/ranzal_summer/mouths/100003_04_parts_c009.png"
    0.15
    "images/ranzal_summer/mouths/100003_04_parts_c008.png"
    0.15
    repeat

image sranzal_grin1 = WhileSpeaking("ranz", "sranzal_grin1_talking", "sranzal_grin1_nottalking")


image sranzal_frown2_nottalking = "images/ranzal_summer/mouths/100003_04_parts_c014.png"

image sranzal_frown2_talking:
    "images/ranzal_summer/mouths/100003_04_parts_c015.png"
    0.15
    "images/ranzal_summer/mouths/100003_04_parts_c014.png"
    0.15
    repeat

image sranzal_frown2 = WhileSpeaking("ranz", "sranzal_frown2_talking", "sranzal_frown2_nottalking")


image sranzal_smile2_nottalking = "images/ranzal_summer/mouths/100003_04_parts_c024.png"

image sranzal_smile2_talking:
    "images/ranzal_summer/mouths/100003_04_parts_c025.png"
    0.15
    "images/ranzal_summer/mouths/100003_04_parts_c024.png"
    0.15
    repeat

image sranzal_smile2 = WhileSpeaking("ranz", "sranzal_smile2_talking", "sranzal_smile2_nottalking")


image sranzal_grimace2_nottalking = "images/ranzal_summer/mouths/100003_04_parts_c026.png"

image sranzal_grimace2_talking:
    "images/ranzal_summer/mouths/100003_04_parts_c027.png"
    0.15
    "images/ranzal_summer/mouths/100003_04_parts_c026.png"
    0.15
    repeat

image sranzal_grimace2 = WhileSpeaking("ranz", "sranzal_grimace2_talking", "sranzal_grimace2_nottalking")


image sranzal_frown1_nottalking = "images/ranzal_summer/mouths/100003_04_parts_c028.png"

image sranzal_frown1_talking:
    "images/ranzal_summer/mouths/100003_04_parts_c029.png"
    0.15
    "images/ranzal_summer/mouths/100003_04_parts_c028.png"
    0.15
    repeat

image sranzal_frown1 = WhileSpeaking("ranz", "sranzal_frown1_talking", "sranzal_frown1_nottalking")


image sranzal_grin2_nottalking = "images/ranzal_summer/mouths/100003_04_parts_c030.png"

image sranzal_grin2_talking:
    "images/ranzal_summer/mouths/100003_04_parts_c031.png"
    0.15
    "images/ranzal_summer/mouths/100003_04_parts_c030.png"
    0.15
    repeat

image sranzal_grin2 = WhileSpeaking("ranz", "sranzal_grin2_talking", "sranzal_grin2_nottalking")


image sranzal_grimace1_nottalking = "images/ranzal_summer/mouths/100003_04_parts_c040.png"

image sranzal_grimace1_talking:
    "images/ranzal_summer/mouths/100003_04_parts_c041.png"
    0.15
    "images/ranzal_summer/mouths/100003_04_parts_c040.png"
    0.15
    repeat

image sranzal_grimace1 = WhileSpeaking("ranz", "sranzal_grimace1_talking", "sranzal_grimace1_nottalking")


image sranzal_mutter1_nottalking = "images/ranzal_summer/mouths/100003_04_parts_c042.png"

image sranzal_mutter1_talking:
    "images/ranzal_summer/mouths/100003_04_parts_c043.png"
    0.15
    "images/ranzal_summer/mouths/100003_04_parts_c042.png"
    0.15
    repeat

image sranzal_mutter1 = WhileSpeaking("ranz", "sranzal_mutter1_talking", "sranzal_mutter1_nottalking")


image sranzal_shout1_nottalking = "images/ranzal_summer/mouths/100003_04_parts_c044.png"

image sranzal_shout1_talking:
    "images/ranzal_summer/mouths/100003_04_parts_c045.png"
    0.15
    "images/ranzal_summer/mouths/100003_04_parts_c044.png"
    0.15
    repeat

image sranzal_shout1 = WhileSpeaking("ranz", "sranzal_shout1_talking", "sranzal_shout1_nottalking")


image sranzal_smile1_nottalking = "images/ranzal_summer/mouths/100003_04_parts_c046.png"

image sranzal_smile1_talking:
    "images/ranzal_summer/mouths/100003_04_parts_c047.png"
    0.15
    "images/ranzal_summer/mouths/100003_04_parts_c046.png"
    0.15
    repeat

image sranzal_smile1 = WhileSpeaking("ranz", "sranzal_smile1_talking", "sranzal_smile1_nottalking")




# The test file script starts here.

label sranzal_character_procedures:

    layeredimage beach2_day:

        always "images/backgrounds/Sty_bg_0079_100_00.png"

        always "images/backgrounds/Sty_bg_0079_100_03.png"



    scene beach2_day with fade

    show sranzal with dissolve
    ranz "Oh, hey!  You back with some tasty catches?"

    show sranzal normal neutral grin1
    ranz "(normal neutral grin1) I've been setting up a fire pit and the barbeque spits."
    
    show sranzal relaxed grin2
    ranz "(relaxed grin2) Once I finish chopping up the rest of this firewood, we should be all set to go."

    show sranzal surprised mutter1
    ranz "(surprised mutter1) Wait, is that..."

    show sranzal shocked shout1
    ranz "(shocked shout1) Look out!!!"

    show sranzal at lunge_out_right
    pause 0.75
    show sranzal flinch grimace1 at walk_in_right
    ranz "(flinch grimace1) Those darn Inazumans playing volleyball..."

    show sranzal angry grimace2 at disagree_shake
    ranz "(angry grimace2) Hey, morons!  Yer ball almost knocked the boss out cold!!!"

    show sranzal focused frown1
    ranz "(focused frown1) Sorry about that.  What was I saying again?"

    show sranzal squint frown2 at agree_dip
    ranz "(squint frown2) Oh yeah, the firewood.  Yeesh, there's a lot still to do."
    
    show sranzal closed_neutral smile1
    ranz "(closed_neutral smile1) Uhh... any chance you could help me out with some of this?"

    show sranzal neutral mutter1_closed
    ranz "(mutter1_closed) ..."

    show sranzal bbq wink smile2
    ranz "(bbq wink smile2) Perfect.  With you taking care of that, I can get to grillin'."
    ranz "Don't worry, I'll let you have first dibs on the grub once it's done."


    hide sranzal with dissolve


    # This goes back to script

    jump testfiles
