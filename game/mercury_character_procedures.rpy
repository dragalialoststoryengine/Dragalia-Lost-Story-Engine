
    # Mercury Character Procedures File

    # Paste this file into a story if you want to use Euden.  These procedures animate Mercury as a speaker.
    # You'll also need to paste THIS line into your actual script above the script label whenever you're using Mercury:

define merc = Character("Mercury", callback=speaker("merc"))

    # This program assumes that the following folders exist:
    #     -"images/mercury"
    #     -"images/mercury/faces"
    #     -"images/mercury/mouths"
    #
    #     -"images/mercury_high"
    #     -"images/mercury_high/faces"
    #     -"images/mercury_high/mouths"
    #
    #     -"images/mercury_zero"


    # Mercury dynamically blinks and, while speaking, can moves her mouth along with the text scroll (if desired).

    # FUNCTIONS:

    # *Making Mercury appear*:
    #  -->  show mercury with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Mercury's eyes*:
    #  -->  show mercury [keyword]
    #  List of eye keywords:
    #     -->  normal (default), narrowed, closed, closed2

    # *Changing Mercury's mouth*:
    #  -->  show mercury [keyword]
    #  List of mouth keywords:
    #     -->  mouth_closed1 (default)

    # *Writing dialogue for Mercury*:
    #  --> merc "[Mercury's line here]"

    # *Making Mercury disappear*:
    #  --> hide mercury with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # *Making High Brunhilda appear*:
    #  -->  show highbrunhilda with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing High Brunhilda's eyes*:
    #  -->  show highbrunhilda [keyword]
    #  List of eye keywords:
    #     -->  normal (default), closed

    # *Changing High Brunhilda's mouth*:
    #  -->  show highbrunhilda [keyword]
    #  List of mouth keywords:
    #     -->  wide1 (default), open1, wide1_flap

    # *Making High Brunhilda disappear*:
    #  --> hide highbrunhilda with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # *Making Brunhilda Zero appear*:
    #  -->  show brunhilda0 with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Making Brunhilda Zero disappear*:
    #  --> hide brunhilda0 with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)



    # # # # #


layeredimage mercury:

    always "images/mercury/mercury_body.png"

    group face:

        # 382/1024, 160/1024:
        # didn't work for some reason, manually adjusting x value
        # (382-33)/1024 = 

        pos (0.340820, 0.15625)

        attribute normal default:
            "mercury_normal_eyes"

        attribute narrowed:
            "mercury_narrowed_eyes"

        attribute closed:
            "images/mercury/faces/210003_01_parts_c001.png"
        
        attribute closed2:
            "images/mercury/faces/210003_01_parts_c002.png"


    group mouth:

        pos (0.340820, 0.15625)

        attribute mouth_closed1 default:
            "images/mercury/mouths/210003_01_parts_c004.png"




layeredimage highmercury:

    always "images/mercury_high/mercury_high_body.png"

    group face:

        # 385/1024, 181/1024:
        pos (0.375977, 0.176758)

        attribute normal default:
            "mercury_high_normal_eyes"

        attribute closed:
            "images/mercury_high/faces/210040_01_parts_c001.png"

        attribute narrowed:
            "mercury_high_narrowed_eyes"

    group mouth:

        pos (0.375977, 0.176758)

        attribute mouth_closed1 default:
            "images/mercury_high/mouths/210040_01_parts_c004.png"
        
        attribute mouth_open1:
            "images/mercury_high/mouths/210040_01_parts_c006.png"

        attribute mouth_flap1:
            "mercury_high_mouth_flap1"




image mercury0 = "images/mercury_zero/mercury_zero_body.png"








## EYE animations start here.

image mercury_normal_eyes:
    "images/mercury/faces/210003_01_parts_c000.png"
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
    "images/mercury/faces/210003_01_parts_c001.png"
    0.05
    repeat

image mercury_narrowed_eyes:
    "images/mercury/faces/210003_01_parts_c006.png"
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
    "images/mercury/faces/210003_01_parts_c001.png"
    0.05
    repeat

image mercury_high_normal_eyes:
    "images/mercury_high/faces/210040_01_parts_c000.png"
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
    "images/mercury_high/faces/210040_01_parts_c001.png"
    0.05
    repeat

image mercury_high_narrowed_eyes:
    "images/mercury_high/faces/210040_01_parts_c002.png"
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
    "images/mercury_high/faces/210040_01_parts_c001.png"
    0.05
    repeat


# MOUTH animations start here.

image mercury_high_mouth_flap1_nottalking = "images/mercury_high/mouths/210040_01_parts_c004.png"

image mercury_high_mouth_flap1_talking:
    "images/mercury_high/mouths/210040_01_parts_c006.png"
    0.15
    "images/mercury_high/mouths/210040_01_parts_c004.png"
    0.15
    repeat

image mercury_high_mouth_flap1 = WhileSpeaking("merc", "mercury_high_mouth_flap1_talking", "mercury_high_mouth_flap1_nottalking")







# The game starts here.

label mercury_character_procedures:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    layeredimage lake:

        always "images/backgrounds/Sty_bg_0068_100_00.png"
        always "images/backgrounds/Sty_bg_0068_100_01.png"
        always "images/backgrounds/Sty_bg_0068_100_02.png"        
        always "images/backgrounds/Sty_bg_0068_100_03.png"


    scene lake with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show mercury with dissolve
    merc "Ah, greetings.  I was wondering when you'd next come by for a visit."

    show mercury normal mouth_closed1
    merc "(normal mouth_closed1) As it happens, I was just about to address the mana imbalance in this area."

    show mercury closed
    merc "(closed) I can sense a great sickness in the mana of the lake."

    show mercury narrowed
    merc "(narrowed) It feels... artificial.  No doubt human activity was involved.  Extensive activity."

    show mercury closed2
    merc "(closed2) I must transform into my ascended form in order to purify these waters.  Please stand back."

    hide mercury with dissolve


    show highmercury with dissolve
    merc "Very well.  This much power should be sufficient to cleanse the lake."

    show highmercury normal mouth_closed1
    merc "(normal mouth_closed1) Waters of this lake, heed my call and bear forth that which poisons you to this location."

    show highmercury closed mouth_open1
    merc "(closed mouth_open1) ...I see, the damage is worse than I feared."

    show highmercury narrowed mouth_flap1
    merc "(narrowed mouth_flap1) ...Waters of this lake, heed my call!  Bear forth that which poisons you to this location!  HRRRAGH!"

    hide highmercury with dissolve

    show mercury0 with dissolve
    merc "THERE!  The mana pollution!!!  I will isolate it now!"
    merc "...I have isolated the corrupting mana.  I can scarce believe it took my full authority over water mana to remove."
    merc "We must find the ones who released this mana at once.  They will pay for defiling my waters."

    hide mercury0 with dissolve

    # This goes back to script

    jump testfiles
