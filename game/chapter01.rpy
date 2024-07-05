# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eireen")
define f = Character("Finni")
define b = Character("Berserker")
define a = Character("Ayaha")

transform middle:
    xalign 0.5
    yalign 0.5

transform leftspot:
    xalign -0.25
    yalign 0.5

transform rightspot:
    xalign 1.25
    yalign 0.5

transform berserkerfacepos:
    xalign 0.40137
    yalign 0.22461

# The game starts here.

label chapter01:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image sky = "images/backgrounds/Sty_bg_0015_100_00.png"
    scene sky at middle
    image village = "images/backgrounds/Sty_bg_0015_100_04_front.png"
    show village at middle

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    image finni happy = "images/finni/finni_body.png"
    show finni happy at middle

    # These display lines of dialogue.

    f "Die, cishet.  I'm busy kissing my lesbian android girlfriend."


    image berserker happy = "images/berserker/berserker_body.png"
    # image berserkercomposite = LiveComposite((1024, 1024), (0, 0), "images/berserker/berserker_body.png" (0, 0), "images/berserker/faces/110050_01_parts_c000.png")

    hide finni
    show berserker happy at middle

    b "Are you challenging me to combat?  Before we fight, you must know that I scare small children at night."

    image ayaha happy = "images/ayaha/ayaha_body.png"
    hide berserker
    show ayaha happy at middle

    a "lmfao you don't understand the meaning of fear i'm gonna teach you freedom aka murder you in your sleep rofl."

    image eirene happy = "images/eirene/eirene_body.png"
    image eirene leftcrop = "images/eirene/eirene_body_leftcrop.png"
    image finni rightcrop = "images/finni/finni_body_rightcrop.png"
    hide ayaha
    show eirene leftcrop at leftspot
    show finni rightcrop at rightspot

    e "Trans rights forever."

    hide eirene
    hide finni
    show ayaha happy at middle

    a "wait that doesn't have anything to do with the current situation--"

    hide ayaha
    show berserker happy at middle
    b "Holy Hildegarde, those robots just ran over a child in cold blood.  Clearly they are worthy adversaries."


    # image berserkercomposite = LiveComposite((1024, 1024), (0, 0), "images/berserker/berserker_body.png" (0, 0), "images/berserker/faces/110050_01_parts_c003.png")

    image berserkerfaceexcited = "images/berserker/faces/110050_01_parts_c003.png"
    show berserker happy at middle
    show berserkerfaceexcited at berserkerfacepos
    b "I demand a duel to the death!  We shall see whose wokeness stands on top!!!"



    # This goes back to script

    jump start
