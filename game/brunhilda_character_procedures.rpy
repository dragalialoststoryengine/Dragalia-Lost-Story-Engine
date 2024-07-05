
    # Brunhilda Character Procedures File

    # Paste this file into a story if you want to use Euden.  These procedures animate Brunhilda as a speaker.
    # You'll also need to paste THIS line into your actual script above the script label whenever you're using Brunhilda:

define brun = Character("Brunhilda", callback=speaker("brun"))

    # This program assumes that the following folders exist:
    #     -"images/brunhilda"
    #     -"images/brunhilda/faces"
    #     -"images/brunhilda/mouths"
    #
    #     -"images/brunhilda_high"
    #     -"images/brunhilda_high/faces"
    #     -"images/brunhilda_high/mouths"
    #
    #     -"images/brunhilda_zero"


    # Brunhilda dynamically blinks and, while speaking, can moves her mouth along with the text scroll (if desired).

    # FUNCTIONS:

    # *Making Brunhilda appear*:
    #  -->  show brunhilda with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Brunhilda's eyes*:
    #  -->  show brunhilda [keyword]
    #  List of eye keywords:
    #     -->  normal (default), surprised, closed

    # *Changing Brunhilda's mouth*:
    #  -->  show brunhilda [keyword]
    #  List of mouth keywords:
    #     -->  open1 (default), closed1, wide1, open1_flap, wide1_flap

    # *Writing dialogue for Brunhilda*:
    #  --> brun "[Brunhilda's line here]"

    # *Making Brunhilda disappear*:
    #  --> hide brunhilda with dissolve
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


layeredimage brunhilda:

    always "images/brunhilda/brunhilda_body.png"

    group face:

        # 370/1024, 133/1024:
        pos (0.361328, 0.1298828)

        attribute normal default:
            "brunhilda_normal_eyes"

        attribute surprised:
            "brunhilda_surprised_eyes"

        attribute closed:
            "images/brunhilda/faces/210002_01_parts_c001.png"


    group mouth:

        pos (0.361328, 0.1298828)

        attribute open1 default:
            "images/brunhilda/mouths/210002_01_parts_c005.png"

        attribute closed1:
            "images/brunhilda/mouths/210002_01_parts_c015.png"

        attribute wide1:
            "images/brunhilda/mouths/210002_01_parts_c007.png"

        attribute open1_flap:
            "brunhilda_open1_flap"

        attribute wide1_flap:
            "brunhilda_wide1_flap"




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

        attribute wide1 default:
            "images/brunhilda_high/mouths/210039_01_parts_c003.png"

        attribute open1:
            "images/brunhilda_high/mouths/210039_01_parts_c005.png"

        attribute wide1_flap:
            "brunhilda_high_wide1_flap"




image brunhilda0 = "images/brunhilda_zero/brunhilda_zero_body.png"








## EYE animations start here.

image brunhilda_normal_eyes:
    "images/brunhilda/faces/210002_01_parts_c000.png"
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
    "images/brunhilda/faces/210002_01_parts_c001.png"
    0.05
    repeat

image brunhilda_surprised_eyes:
    "images/brunhilda/faces/210002_01_parts_c003.png"
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
    "images/brunhilda/faces/210002_01_parts_c004.png"
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

label brunhilda_character_procedures:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image volcano = "images/backgrounds/Sty_bg_0023_100_00.png"
    scene volcano

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show brunhilda with dissolve
    brun "I see you've come to the heart of my domain.  How exciting!"

    show brunhilda normal
    brun "(normal) I would say, \"welcome home, darling,\" but I think these conditions may be a little extreme to be our love nest..."

    show brunhilda surprised
    brun "(surprised) Plus, I haven't had a chance to clean up!  You really must tell me when you're coming over, darling!"

    show brunhilda closed
    brun "(closed) You don't have to try so hard to accomodate me!  I've already gone through the trouble of forming a pact with you, so you don't have to impress me with recklessness."

    show brunhilda normal open1
    brun "(open1) Of course, my doors are always open to you when you come for a visit!"

    show brunhilda surprised wide1
    brun "(wide1) ...What?!  You're just here for some flame ore?!"

    show brunhilda closed1
    brun "(closed1) And here I thought you wanted to see me..."

    show brunhilda normal open1_flap
    brun "(open1_flap) HMPH!  Well, do what you want!!  It's none of my concern!!!  Just scram, then!!"

    show brunhilda surprised wide1_flap
    brun "(wide1_flap) H-Huffy?!!   You're saying I'm acting huffy?!!  Oh, you haven't seen anything!!!"

    hide brunhilda with dissolve
    show highbrunhilda with dissolve

    brun "THIS is acting huffy!!!"

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
