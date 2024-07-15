
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




layeredimage highbrunhilda:

    always "images/brunhilda_high/brunhilda_high_body.png"

    group face:

        # 473/1024, 192/1024:
        pos (0.461914, 0.1875)

        attribute normal default:
            "brunhilda_high_normal_eyes"

        attribute closed:
            "images/brunhilda_high/faces/210039_01_parts_c001.png"


    group mouth:

        pos (0.461914, 0.1875)

        attribute mouth_closed default:
            "images/brunhilda_high/mouths/210039_01_parts_c003.png"




image brunhilda0 = "images/brunhilda_zero/brunhilda_zero_body.png"








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

image brunhilda_high_normal_eyes:
    "images/brunhilda_high/faces/210039_01_parts_c000.png"
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
    "images/brunhilda_high/faces/210039_01_parts_c001.png"
    0.05
    repeat


# MOUTH animations start here.

image brunhilda_open1_flap_nottalking = "images/brunhilda/mouths/210002_01_parts_c015.png"

image brunhilda_open1_flap_talking:
    "images/brunhilda/mouths/210002_01_parts_c005.png"
    0.15
    "images/brunhilda/mouths/210002_01_parts_c015.png"
    0.15
    repeat

image brunhilda_open1_flap = WhileSpeaking("brun", "brunhilda_open1_flap_talking", "brunhilda_open1_flap_nottalking")


image brunhilda_wide1_flap_nottalking = "images/brunhilda/mouths/210002_01_parts_c015.png"

image brunhilda_wide1_flap_talking:
    "images/brunhilda/mouths/210002_01_parts_c007.png"
    0.15
    "images/brunhilda/mouths/210002_01_parts_c015.png"
    0.15
    repeat

image brunhilda_wide1_flap = WhileSpeaking("brun", "brunhilda_wide1_flap_talking", "brunhilda_wide1_flap_nottalking")






image brunhilda_high_wide1_flap_nottalking = "images/brunhilda_high/mouths/210039_01_parts_c005.png"

image brunhilda_high_wide1_flap_talking:
    "images/brunhilda_high/mouths/210039_01_parts_c003.png"
    0.15
    "images/brunhilda_high/mouths/210039_01_parts_c005.png"
    0.15
    repeat

image brunhilda_high_wide1_flap = WhileSpeaking("brun", "brunhilda_high_wide1_flap_talking", "brunhilda_high_wide1_flap_nottalking")







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

    show highbrunhilda normal wide1
    brun "(normal wide1) Behold the true wrath of a woman scorned!!!"

    show highbrunhilda closed open1
    brun "(closed open1) Y-You're not even going to pretend to be afraid?!"

    show highbrunhilda normal wide1_flap
    brun "(wide1_flap) H-Hey!!!  Don't just walk away!!!!"

    hide highbrunhilda with dissolve
    show brunhilda0 with dissolve
    brun "PAY ATTENTION TO ME, DANGIT!!!!!!  GEEZ!!!!"

    hide brunhilda0 with dissolve

    # This goes back to script

    jump testfiles
