
    # Cibella Character Procedures File

    # Paste this file into a story if you want to use Cibella.  These procedures animate Cibella as a speaker.
    # You'll also need to paste THIS line into your actual script above the script label whenever you're using Cibella:

define cib = Character("Cibella", callback=speaker("cib"))

    # This program assumes that the following folders exist:
    #     -"images/cibella"
    #     -"images/cibella/faces"
    #     -"images/cibella/mouths"



    # Cibella dynamically blinks and, while speaking, also moves her mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Cibella appear*:
    #  -->  show cibella with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Cibella's eyes*:
    #  -->  show cibella [keyword]
    #  List of eye keywords:
    #     -->  focused (default), angry, flinch, relaxed,
    #             closed_focused, closed_angry_, closed_flinch, closed_relaxed

    # *Changing Cleo's mouth*:
    #  -->  show cleo [keyword]
    #  List of mouth keywords:
    #     -->  frown1 (default), mutter1, shout1, smile1

    # *Writing dialogue for Cibella*:
    #  --> cib "[Cibella's line here]"

    # *Making Cibella disappear*:
    #  --> hide cibella with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage cibella:

    always "images/cibella/cibella_body.png"

    group face:

        # 434/1024, 249/1024:

        pos (0.423828125, 0.2431640625) 

        attribute focused default:
            "cibella_focused_eyes"

        attribute closed_focused:
            "images/cibella/faces/110014_01_parts_c001.png"
        
        attribute angry:
            "cibella_angry_eyes"

        attribute closed_angry:
            "images/cibella/faces/110014_01_parts_c004.png"

        attribute relaxed:
            "cibella_relaxed_eyes"

        attribute closed_relaxed:
            "images/cibella/faces/110014_01_parts_c011.png"

        attribute flinch:
            "cibella_flinch_eyes"

        attribute closed_flinch:
            "images/cibella/faces/110014_01_parts_c013.png"



    group mouth:

        pos (0.423828125, 0.2431640625)

        attribute frown1 default:
            "cibella_frown1"

        attribute mutter1:
            "cibella_mutter1"

        attribute smile1:
            "cibella_smile1"

        attribute shout1:
            "cibella_shout1"


## EYE animations start here.

image cibella_focused_eyes:
    "images/cibella/faces/110014_01_parts_c000.png"
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
    "images/cibella/faces/110014_01_parts_c001.png"
    0.05
    repeat

image cibella_angry_eyes:
    "images/cibella/faces/110014_01_parts_c003.png"
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
    "images/cibella/faces/110014_01_parts_c004.png"
    0.05
    repeat

image cibella_relaxed_eyes:
    "images/cibella/faces/110014_01_parts_c010.png"
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
    "images/cibella/faces/110014_01_parts_c011.png"
    0.05
    repeat

image cibella_flinch_eyes:
    "images/cibella/faces/110014_01_parts_c012.png"
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
    "images/cibella/faces/110014_01_parts_c013.png"
    0.05
    repeat



# MOUTH animations start here.

image cibella_frown1_nottalking = "images/cibella/mouths/110014_01_parts_c005.png"

image cibella_frown1_talking:
    "images/cibella/mouths/110014_01_parts_c006.png"
    0.15
    "images/cibella/mouths/110014_01_parts_c005.png"
    0.15
    repeat

image cibella_frown1 = WhileSpeaking("cib", "cibella_frown1_talking", "cibella_frown1_nottalking")


image cibella_mutter1_nottalking = "images/cibella/mouths/110014_01_parts_c008.png"

image cibella_mutter1_talking:
    "images/cibella/mouths/110014_01_parts_c009.png"
    0.15
    "images/cibella/mouths/110014_01_parts_c008.png"
    0.15
    repeat

image cibella_mutter1 = WhileSpeaking("cib", "cibella_mutter1_talking", "cibella_mutter1_nottalking")


image cibella_smile1_nottalking = "images/cibella/mouths/110014_01_parts_c014.png"

image cibella_smile1_talking:
    "images/cibella/mouths/110014_01_parts_c015.png"
    0.15
    "images/cibella/mouths/110014_01_parts_c014.png"
    0.15
    repeat

image cibella_smile1 = WhileSpeaking("cib", "cibella_smile1_talking", "cibella_smile1_nottalking")


image cibella_shout1_nottalking = "images/cibella/mouths/110014_01_parts_c016.png"

image cibella_shout1_talking:
    "images/cibella/mouths/110014_01_parts_c017.png"
    0.15
    "images/cibella/mouths/110014_01_parts_c016.png"
    0.15
    repeat

image cibella_shout1 = WhileSpeaking("cib", "cibella_shout1_talking", "cibella_shout1_nottalking")







# The game starts here.

label cibella_character_procedures:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image halidom_bridge = "images/backgrounds/Sty_bg_0017_100_00.png"
    scene halidom_bridge

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show cibella with dissolve
    cib "(dialogue)"

    show cibella focused frown1
    cib "(focused frown1) Dialogue"

    show cibella closed_focused
    cib "(closed_focused) Dialogue"

    show cibella angry mutter1
    cib "(angry mutter1) Dialogue."

    show cibella closed_angry
    cib "(closed_angry) Dialogue"

    show cibella relaxed smile1
    cib "(relaxed smile1) Dialogue."

    show cibella closed_relaxed
    cib "(closed_relaxed) Dialogue."

    show cibella flinch shout1
    cib "(flinch shout1) Dialogue."

    show cibella closed_flinch
    cib "(closed_flinch) Dialogue"


    hide cibella with dissolve

    # This goes back to script

    jump testfiles
