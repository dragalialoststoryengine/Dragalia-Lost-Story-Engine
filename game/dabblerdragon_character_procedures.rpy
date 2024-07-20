    # DabblerDragon Character Procedures File

    # Paste this file into a story if you want to use DabblerDragon.  These procedures animate DabblerDragon as a speaker.

define dabbler = Character("DabblerDragon", callback=speaker("dabbler"))

    # This program assumes that the following folders exist:
    #     -"images/ocs/dabblerdragon"
    #     -"images/ocs/dabblerdragon/faces"
    #     -"images/ocs/dabblerdragon/mouths"

    # DabblerDragon dynamically blinks and, while speaking, also moves his mouth along with the text scroll.

    # FUNCTIONS:

    # *Making DabblerDragon appear*:
    #  -->  show dabblerdragon with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing DabblerDragon's eyes*:
    #  -->  show dabblerdragon [keyword]
    #  List of eye keywords:
    #     -->  relaxed (default), closed_relaxed

    # *Changing DabblerDragon's mouth*:
    #  -->  show dabblerdragon [keyword]
    #  List of mouth keywords:
    #     -->  grin1 (default), grin1_inverse

    # *Writing dialogue for DabblerDragon*:
    #  --> dabbler "[DabblerDragon's line here]"

    # *Making DabblerDragon disappear*:
    #  --> hide dabblerdragon with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage dabblerdragon:

    always "images/ocs/dabblerdragon/dabblerdragon_body.png"

    group face:

        # 304/1024, 152/1024:
        pos (0.296875, 0.1484375)

        attribute relaxed default:
            "dabblerdragon_relaxed_eyes"

        attribute closed_relaxed:
            "images/ocs/dabblerdragon/faces/dd_relaxed_closed_face.png"


    group mouth:

        pos (0.296875, 0.1484375)

        attribute grin1 default:
            "dabblerdragon_grin1"

        attribute grin1_inverse:
            "dabblerdragon_grin1_inverse"





## EYE animations start here.

image dabblerdragon_relaxed_eyes:
    "images/ocs/dabblerdragon/faces/dd_relaxed_face.png"
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
    "images/ocs/dabblerdragon/faces/dd_relaxed_closed_face.png"
    0.05
    repeat




# MOUTH animations start here.

image dabblerdragon_grin1_nottalking = "images/ocs/dabblerdragon/mouths/dd_grin_mouth.png"

image dabblerdragon_grin1_talking:
    "images/ocs/dabblerdragon/mouths/dd_wide_smile_mouth.png"
    0.15
    "images/ocs/dabblerdragon/mouths/dd_grin_mouth.png"
    0.15
    repeat

image dabblerdragon_grin1 = WhileSpeaking("dabbler", "dabblerdragon_grin1_talking", "dabblerdragon_grin1_nottalking")


image dabblerdragon_grin1_inverse_nottalking = "images/ocs/dabblerdragon/mouths/dd_wide_smile_mouth.png"

image dabblerdragon_grin1_inverse_talking:
    "images/ocs/dabblerdragon/mouths/dd_grin_mouth.png"
    0.15
    "images/ocs/dabblerdragon/mouths/dd_wide_smile_mouth.png"
    0.15
    repeat

image dabblerdragon_grin1_inverse = WhileSpeaking("dabbler", "dabblerdragon_grin1_inverse_talking", "dabblerdragon_grin1_inverse_nottalking")






# The test file script starts here.

label dabblerdragon_character_procedures:

    layeredimage sylvan_village_day:
        always "images/backgrounds/Sty_bg_0016_100_00.png"

        always "images/backgrounds/Sty_bg_0016_100_04_front.png"


    scene alleyway_day with fade

    show dabblerdragon at walk_in_right
    dabbler "Oops, looks like I've been found!  Hi everyone!"

    show dabblerdragon relaxed grin1
    dabbler "(relaxed grin1) I'm DabblerDragon, and I'm one of the developers of the Dragalia Lost Story Engine."

    show dabblerdragon closed_relaxed
    dabbler "(closed_relaxed) I'm a little embarrassed to be putting a self-insert here, but I wanted to test the ability of the engine to work with new art assets."

    show dabblerdragon relaxed
    dabbler "Anyway, I want to take this opportunity to thank everyone involved in the Dragalia Lost Story Engine project."
    dabbler "I really miss the Dragalia Lost game and it's been really nice to still find people who want to talk about it and be creative."

    show dabblerdragon grin1_inverse
    dabbler "(grin1_inverse) And just as importantly, I want to thank everyone who's taken an interest in the project over the years.  Without the energy from you guys, I wouldn't have had the motivation to keep going!"

    dabbler "I hope you all can enjoy the Dragalia Lost Story Engine for many years to come, and look forward to telling stories with you together!"



    show dabblerdragon at walk_out_left
    pause 1.0

    # This goes back to script

    jump octestfiles
