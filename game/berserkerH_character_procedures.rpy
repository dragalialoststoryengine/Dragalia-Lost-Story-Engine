    # Hunter Berserker Character Procedures File

    # Paste this file into a story if you want to use Hunter Berserker.  These procedures animate Hunter Berserker as a speaker.


#define bers = Character("Berserker", callback=speaker("bers"))

    # This program assumes that the following folders exist:
    #     -"images/berserker_hunter"
    #     -"images/berserker_hunter/faces"
    #     -"images/berserker_hunter/faces_sword"

    # Hunter Berserker dynamically blinks and, while speaking, also moves his mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Hunter Berserker appear*:
    #  -->  show hberserker with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Hunter Berserker's eyes*:
    #  -->  show hberserker [keyword]
    #  List of eye keywords:
    #     -->  neutral (default), closed_neutral, glint, surprised, surprised2

    # *Writing dialogue for Hunter Berserker*:
    #  --> bers "[Hunter Berserker's line here]"

    # *Making Hunter Berserker disappear*:
    #  --> hide hberserker with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)


    # *Making Hunter Berserker appear with a SWORD pose*:
    #  -->  show hberserker_sword with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Hunter Berserker's eyes*:
    #  -->  show hberserker_sword [keyword]
    #  List of eye keywords:
    #     -->  neutral (default), closed_neutral, glint, surprised

    # *Writing dialogue for Hunter Berserker with a sword*:
    #  --> bers "[Hunter Berserker's line here]"

    # *Making Hunter Berserker with a sword disappear*:
    #  --> hide hberserker_sword with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)







layeredimage hberserker:

    always "images/berserker_hunter/berserker_hunter_body.png"

    group face:

        # 447/1024, 206/1024
        pos (0.43652, 0.20117)

        attribute neutral default:
            "hberserker_neutral_eyes"

        attribute closed_neutral:
            "images/berserker_hunter/faces/110050_03_parts_c002.png"

        attribute glint:
            "hberserker_glint_eyes"

        attribute surprised:
            "hberserker_surprised_eyes"

        attribute surprised2:
            "hberserker_surprised2_eyes"




image hberserker_neutral_eyes:
        "images/berserker_hunter/faces/110050_03_parts_c000.png"
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
        "images/berserker_hunter/faces/110050_03_parts_c002.png"
        0.05
        repeat

image hberserker_glint_eyes:
        "images/berserker_hunter/faces/110050_03_parts_c003.png"
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
        "images/berserker_hunter/faces/110050_03_parts_c002.png"
        0.05
        repeat

image hberserker_surprised_eyes:
        "images/berserker_hunter/faces/110050_03_parts_c009.png"
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
        "images/berserker_hunter/faces/110050_03_parts_c002.png"
        0.05
        repeat

image hberserker_surprised2_eyes:
        "images/berserker_hunter/faces/110050_03_parts_c010.png"
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
        "images/berserker_hunter/faces/110050_03_parts_c002.png"
        0.05
        repeat







layeredimage hberserker_sword:

    always "images/berserker_hunter/berserker_hunter_body_sword.png"

    group face:

        # 473/1024, 221/1024
        pos (0.46191, 0.21582)

        attribute neutral default:
            "hberserker_sword_neutral_eyes"

        attribute closed_neutral:
            "images/berserker_hunter/faces_sword/110050_02_parts_c002.png"

        attribute glint:
            "hberserker_sword_glint_eyes"

        attribute surprised:
            "hberserker_sword_surprised_eyes"




image hberserker_sword_neutral_eyes:
        "images/berserker_hunter/faces_sword/110050_02_parts_c000.png"
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
        "images/berserker_hunter/faces_sword/110050_02_parts_c002.png"
        0.05
        repeat

image hberserker_sword_glint_eyes:
        "images/berserker_hunter/faces_sword/110050_02_parts_c005.png"
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
        "images/berserker_hunter/faces_sword/110050_02_parts_c002.png"
        0.05
        repeat

image hberserker_sword_surprised_eyes:
        "images/berserker_hunter/faces_sword/110050_02_parts_c012.png"
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
        "images/berserker_hunter/faces_sword/110050_02_parts_c002.png"
        0.05
        repeat









# The game starts here.

label berserkerH_character_procedures:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image cliff_sunset = "images/backgrounds/Sty_bg_0038_200_00.png"
    scene cliff_sunset with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    show hberserker with dissolve

    bers "Ah, greetings.  How fortuitous that you would join me for this hunt."

    show hberserker neutral
    bers "(neutral) I have traced the Rathalos to this location.  This should be its nest."

    show hberserker closed_neutral
    bers "(closed_neutral) While invading a creature's natural home may be improper..."

    show hberserker surprised
    bers "(surprised) ...I will admit that the fruition of my efforts this past week fills me with excitement!"

    show hberserker surprised2
    bers "(surprised2) Ah yes, the scent of danger... the thought of facing such a dangerous beast... My blood rushes!"

    show hberserker glint
    bers "(glint) Hahahaha!!!  Yes, bring forth my foe, that we may tear into each other!!!  Let blood be spilt this day!!!"
    hide hberserker with dissolve


    show hberserker_sword with dissolve
    bers "...The beast approaches."

    show hberserker_sword neutral
    bers "It seems my excited chattering has alerted it to our location."

    show hberserker_sword closed_neutral
    bers "(closed_neutral) My apologies... I did not wish to put you in harm's way unnecessarily."

    show hberserker_sword surprised
    bers "(surprised) However, should you wish to fight alongside me this day, I urge you to steel yourself."

    show hberserker_sword glint
    bers "(glint) TODAY, WE SLAY THE BEAST, OR DIE GLORIOUS DEATHS!!!  WAHAHAHAHA!!!  EN GARDE!!!"

    hide hberserker_sword with dissolve


    # This goes back to script

    jump testfiles
