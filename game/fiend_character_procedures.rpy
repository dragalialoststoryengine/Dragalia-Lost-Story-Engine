    # Fiend Character Procedures File

    # Paste this file into a story if you want to use a generic fiend.  These procedures animate Fiend as a speaker.

define fie = Character("Fiend", callback=speaker("fie"))

    # This program assumes that the following folders exist:
    #     -"images/fiend"

    # Fiend has no image procedures.

    # FUNCTIONS:

    # *Making a fiend appear*:
    #  -->  show fiend with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Writing dialogue for Grace*:
    #  --> fie "[Fiend's line here]"

    # *Making Grace disappear*:
    #  --> hide fiend with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage fiend:

    group race:

        attribute fiend1 default:
            "images/fiend/fiend_1.png"

        attribute fiend2:
            "images/fiend/fiend_2.png"

        attribute fiend3:
            "images/fiend/fiend_3.png"

        attribute leader:
            "images/fiend/fiend_leader.png"

        attribute cyclops:
            "images/fiend/fiend_cyclops_aquatic.png"

        attribute cyclops_light:
            "images/fiend/fiend_cyclops_shining.png"

        attribute cyclops_red:
            "images/fiend/fiend_cyclops_king_archeole.png"

        attribute pumpking:
            "images/fiend/fiend_cyclops_pumpking.png"









# The game starts here.

label fiend_character_procedures:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image otherworld = "images/backgrounds/Sty_bg_0040_100_00.png"
    scene otherworld at middle

    show fiend with dissolve

    fie "..."
    fie "..."
    fie "...rawr?"
    fie "Rawr rawr rawr rawwwr."
    fie "(unintelligable gargling noises)"
    fie "GROAAAAAAAR rawwwwr reeeee!!!"
    fie "..."
    fie "...Roar?"
    fie "..."

    hide fiend with dissolve
    show fiend fiend2 with dissolve

    fie "Rawr."

    hide fiend with dissolve
    show fiend fiend3 with dissolve

    fie "Rawr?"

    hide fiend with dissolve
    show fiend leader with dissolve

    fie "Rawr!"

    hide fiend with dissolve
    show fiend cyclops with dissolve

    fie "RAWR!!!"

    hide fiend with dissolve
    show fiend cyclops_light with dissolve

    fie "RAWR."

    hide fiend with dissolve
    show fiend cyclops_red with dissolve

    fie "RAAAAAAAWR!!"

    hide fiend with dissolve
    show fiend pumpking with dissolve

    fie "...Trick or treat."

    hide fiend with dissolve


    # This goes back to script

    jump npctestfiles
