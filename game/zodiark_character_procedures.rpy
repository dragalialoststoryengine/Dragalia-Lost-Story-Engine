
    # Zodiark Character Procedures File

    # Paste this file into a story if you want to use Euden.  These procedures animate Zodiark as a speaker.
    # You'll also need to paste THIS line into your actual script above the script label whenever you're using Mercury:

define zodi = Character("Zodiark", callback=speaker("zodi"))

    # This program assumes that the following folders exist:
    #     -"images/zodiark"
    #     -"images/zodiark/faces"
    #     -"images/zodiark/mouths"
    #
    #     -"images/zodiark_high"
    #     -"images/zodiark_high/faces"
    #     -"images/zodiark_high/mouths"
    #
    #     -"images/zodiark_zero"


    # Zodiark dynamically blinks and, while speaking, can moves her mouth along with the text scroll (if desired).

    # FUNCTIONS:

    # *Making Zodiark appear*:
    #  -->  show zodiark with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Zodiark's eyes*:
    #  -->  show zodiark [keyword]
    #  List of eye keywords:
    #     -->  normal (default), surprised, closed

    # *Changing Zodiark's mouth*:
    #  -->  show Zodiark [keyword]
    #  List of mouth keywords:
    #     -->  mouth_open1 (default), mouth_closed1, mouth_wide1, mouth_open_flap1, mouth_wide_flap1

    # *Writing dialogue for Zodiark*:
    #  --> zodi "[Zodiark's line here]"

    # *Making Zodiark disappear*:
    #  --> hide zodiark with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)



    # *Making High Zodiark appear*:
    #  -->  show highzodiark with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Making High Zodiark disappear*:
    #  --> hide highzodiark with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)



    # *Making Zodiark Zero appear*:
    #  -->  show zodiark0 with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Making Zodiark Zero disappear*:
    #  --> hide zodiark0 with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)



    # # # # #


layeredimage zodiark:

    always "images/zodiark/zodiark_body.png"

    group face:

        # 404/1024, 144/1024:

        pos (0.39453, 0.140625)

        attribute normal default:
            "zodiark_normal_eyes"

        attribute surprised:
            "zodiark_surprised_eyes"

        attribute closed:
            "images/zodiark/faces/210005_01_parts_c001.png"


    group mouth:

        pos (0.39453, 0.140625)

        attribute mouth_open1 default:
            "images/zodiark/mouths/210005_01_parts_c005.png"

        attribute mouth_closed1:
            "images/zodiark/mouths/210005_01_parts_c007.png"

        attribute mouth_wide1:
            "images/zodiark/mouths/210005_01_parts_c009.png"
         
        attribute mouth_open_flap1:
            "zodiark_mouth_open_flap1"   
                 
        attribute mouth_wide_flap1:
            "zodiark_mouth_wide_flap1"   


image highzodiark = "images/zodiark_high/zodiark_high_body.png"


image zodiark0 = "images/zodiark_zero/zodiark_zero_body.png"








## EYE animations start here.

image zodiark_normal_eyes:
    "images/zodiark/faces/210005_01_parts_c000.png"
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
    "images/zodiark/faces/210005_01_parts_c001.png"
    0.05
    repeat

image zodiark_surprised_eyes:
    "images/zodiark/faces/210005_01_parts_c003.png"
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
    "images/zodiark/faces/210005_01_parts_c001.png"
    0.05
    repeat

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

image zodiark_mouth_open_flap1_nottalking = "images/zodiark/mouths/210005_01_parts_c007.png"

image zodiark_mouth_open_flap1_talking:
    "images/zodiark/mouths/210005_01_parts_c005.png"
    0.15
    "images/zodiark/mouths/210005_01_parts_c007.png"
    0.15
    repeat

image zodiark_mouth_open_flap1 = WhileSpeaking("zodi", "zodiark_mouth_open_flap1_talking", "zodiark_mouth_open_flap1_nottalking")


image zodiark_mouth_wide_flap1_nottalking = "images/zodiark/mouths/210005_01_parts_c007.png"

image zodiark_mouth_wide_flap1_talking:
    "images/zodiark/mouths/210005_01_parts_c009.png"
    0.15
    "images/zodiark/mouths/210005_01_parts_c007.png"
    0.15
    repeat

image zodiark_mouth_wide_flap1 = WhileSpeaking("zodi", "zodiark_mouth_wide_flap1_talking", "zodiark_mouth_wide_flap1_nottalking")




# The game starts here.

label zodiark_character_procedures:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image shadow_caverns = "images/backgrounds/Sty_bg_0100_100_00.png"


    scene shadow_caverns with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show zodiark with dissolve
    zodi "Oh, hello, scion of Aurelius.  What brings you to a place of gloom such as this?"

    show zodiark normal mouth_open1
    zodi "(normal mouth_open1) ...I see.  You have questions about your father."

    show zodiark closed mouth_closed1
    zodi "(closed mouth_closed1) The memories I have recieved from Aurelius are limited, but I will still answer to the best of my abilities."

    show zodiark surprised mouth_wide1
    zodi "(surprised mouth_wide1) ...You wish to know what {i}I{/i} thought of your father?"

    show zodiark mouth_wide_flap1
    zodi "(mouth_wide_flap1) ...Well, obviously I had great respect for him, given that I chose to form a pact with him."

    show zodiark closed mouth_open_flap1
    zodi "(mouth_open_flap1) During his reign, I thought he made choices to wield power for the sake of his family and kingdom."

    hide zodiark with dissolve


    show highzodiark with dissolve
    zodi "However, while I was by Aurelius's side for many years, only you were able to unlock my true potential."
    hide highzodiark with dissolve

    show zodiark0 with dissolve
    zodi "This form is something you and you alone have witnessed over the past millenia.  Aurelius and I are both so proud of you, child."
    hide zodiark0 with dissolve

    # This goes back to script

    jump testfiles
