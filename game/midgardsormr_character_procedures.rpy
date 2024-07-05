
    # Brunhilda Character Procedures File

    # Paste this file into a story if you want to use Euden.  These procedures animate Brunhilda as a speaker.
    # You'll also need to paste THIS line into your actual script above the script label whenever you're using Brunhilda:

define mids = Character("Midgardsormr", callback=speaker("mids"))

    # This program assumes that the following folders exist:
    #     -"images/midgardsormr"
    #     -"images/midgardsormr/faces"
    #     -"images/midgardsormr/mouths"
    #
    #     -"images/midgardsormr_high"
    #
    #     -"images/midgardsormr_zero"
    #     -"images/midgardsormr_zero/faces"


    # Midgardsormr dynamically blinks and, while speaking, can moves her mouth along with the text scroll (if desired).

    # *Making Midgardsormr appear*:
    #  -->  show midgardsormr with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Midgardsormr's eyes*:
    #  -->  show midgardsormr [keyword]
    #  List of eye keywords:
    #     -->  normal (default), closed

    # *Changing Midgardsormr's mouth*:
    #  -->  show midgardsormr [keyword]
    #  List of mouth keywords:
    #     -->  closed1 (default), open1, open1_flap

    # *Writing dialogue for Midgardsormr*:
    #  --> mids "[Midgardsormr's line here]"

    # *Making Midgardsormr disappear*:
    #  --> hide midgardsormr with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # *Making High Midgardsormr appear*:
    #  -->  show highmidgardsormr with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Making High Midgardsormr disappear*:
    #  --> hide highmidgardsormr with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # *Making Midgardsormr Zero appear*:
    #  -->  show midgardsormr0 with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Midgardsormr Zero's mouth*:
    #  -->  show midgardsormr0 [keyword]
    #  List of mouth keywords:
    #     -->  closed1 (default), open1, open1_flap

    # *Making Midgardsormr Zero disappear*:
    #  --> hide midgardsormr0 with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage midgardsormr:

    always "images/midgardsormr/midgardsormr_body.png"

    group face:

        # 384/1024, 173/1024:
        pos (0.375, 0.168945)

        attribute normal default:
            "midgardsormr_normal_eyes"

        attribute closed:
            "images/midgardsormr/faces/210001_01_parts_c001.png"


    group mouth:

        pos (0.375, 0.168945)

        attribute closed1 default:
            "images/midgardsormr/mouths/210001_01_parts_c004.png"

        attribute open1:
            "images/midgardsormr/mouths/210001_01_parts_c006.png"

        attribute open1_flap:
            "midgardsormr_open1_flap"



image highmidgardsormr = "images/midgardsormr_high/midgardsormr_high_body.png"




layeredimage midgardsormr0:

    always "images/midgardsormr_zero/midgardsormr_zero_body.png"

    group mouth:

        # 391/1024, 158/1024:
        pos (0.3818359, 0.154296875)

        attribute closed1 default:
            "images/midgardsormr_zero/faces/210131_01_parts_c000.png"

        attribute open1:
            "images/midgardsormr_zero/faces/210131_01_parts_c004.png"

        attribute open1_flap:
            "midgardsormr_zero_open1_flap"













## EYE animations start here.

image midgardsormr_normal_eyes:
    "images/midgardsormr/faces/210001_01_parts_c000.png"
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
    "images/midgardsormr/faces/210001_01_parts_c001.png"
    0.05
    repeat






# MOUTH animations start here.

image midgardsormr_open1_flap_nottalking = "images/midgardsormr/mouths/210001_01_parts_c004.png"

image midgardsormr_open1_flap_talking:
    "images/midgardsormr/mouths/210001_01_parts_c006.png"
    0.15
    "images/midgardsormr/mouths/210001_01_parts_c004.png"
    0.15
    repeat

image midgardsormr_open1_flap = WhileSpeaking("mids", "midgardsormr_open1_flap_talking", "midgardsormr_open1_flap_nottalking")






image midgardsormr_zero_open1_flap_nottalking = "images/midgardsormr_zero/faces/210131_01_parts_c000.png"

image midgardsormr_zero_open1_flap_talking:
    "images/midgardsormr_zero/faces/210131_01_parts_c004.png"
    0.15
    "images/midgardsormr_zero/faces/210131_01_parts_c000.png"
    0.15
    repeat

image midgardsormr_zero_open1_flap = WhileSpeaking("mids", "midgardsormr_zero_open1_flap_talking", "midgardsormr_zero_open1_flap_nottalking")







# The game starts here.

label midgardsormr_character_procedures:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image plain_day = "images/backgrounds/Sty_bg_0029_100_00.png"
    scene plain_day

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show midgardsormr with dissolve
    mids "Ah.  Good day.  To what do I owe this visit?"

    show midgardsormr normal
    mids "(normal) You want to check my face for damage?  I assure you, my battle injuries are minor."

    show midgardsormr closed
    mids "(closed) ...However, if you insist, I suppose it would pose little harm to have a look."

    show midgardsormr normal closed1
    mids "(closed1) As you can see, both my eyes and mouth are in working order."

    show midgardsormr open1
    mids "(open1) I even practice excellent dental hygiene."

    show midgardsormr open1_flap
    mids "(open1_flap) ...You wish to check my other forms in addition?  Very well."


    hide midgardsormr with dissolve
    show highmidgardsormr with dissolve
    mids "As you can see, my high dragon form is just as it was before."


    hide highmidgardsormr with dissolve
    show midgardsormr0 with dissolve
    mids "As is my primal power.  Observe; my wings, horns and limbs are all perfectly functional."

    show midgardsormr0 closed1
    mids "(closed1) ...But I assume you already suspected so.  Am I wrong?"

    show midgardsormr0 open1
    mids "(open1) Tell me... are you merely trying to invent excuses to spend time together?"

    show midgardsormr0 open1_flap
    mids "(open1_flap) Ha ha ha!!  As I thought.  However, I enjoy our conversations.  You need not act so coyly.  I am hardly as aloof as I appear."


    hide midgardsormr0 with dissolve

    # This goes back to script

    jump testfiles
