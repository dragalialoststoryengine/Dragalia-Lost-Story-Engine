
    # Giovanni Dragon Procedures File

    # Paste this file into a story if you want to use Giovanni.  These procedures animate giovanni as a speaker.
    # You'll also need to paste THIS line into your actual script above the script label whenever you're using Giovanni:

define gio = Character("Giovanni", callback=speaker("gio"))

    # This program assumes that the following folders exist:
    #     -"images/giovanni"
    #     -"images/giovanni/faces"

    # Giovanni dynamically blinks and, while speaking, also moves her mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Giovanni appear*:
    #  -->  show giovanni with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Giovanni's eyes*:
    #  -->  show giovanni [keyword]
    #  List of eye keywords:
    #     -->  closed_neutral (default), angry, happy, open, sad, surprised

    # *Writing dialogue for Giovanni*:
    #  --> gio "[Giovanni's line here]"

    # *Making Giovanni disappear*:
    #  --> hide giovanni with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage giovanni:

    always "images/giovanni/giovanni_body.png"

    group face:

        # 394/1028, 131/1028:
        # pos (0.38327, 0.12743)

        # 394/1024, 131/1024
        pos (0.38477, 0.12793)

        attribute closed_neutral default:
            "images/giovanni/faces/210135_01_parts_c000.png"

        attribute open:
            "giovanni_open_eyes"

        attribute angry:
            "images/giovanni/faces/210135_01_parts_c002.png"

        attribute happy:
            "images/giovanni/faces/210135_01_parts_c003.png"

        attribute surprised:
            "giovanni_surprised_eyes"

        attribute sad:
            "images/giovanni/faces/210135_01_parts_c005.png"

## EYE animations start here.

image giovanni_open_eyes:
    "images/giovanni/faces/210135_01_parts_c001.png"
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
    "images/giovanni/faces/210135_01_parts_c000.png"
    0.05
    repeat

image giovanni_surprised_eyes:
    "images/giovanni/faces/210135_01_parts_c004.png"
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
    "images/giovanni/faces/210135_01_parts_c000.png"
    0.05
    repeat









# The game starts here.

label giovanni_character_procedures:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image theater = "images/backgrounds/Sty_bg_0131_100_00.png"
    scene theater with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    show giovanni with dissolve

    gio "Benvenuto!  I thank you for coming to attend the debut performance of my latest work:  \"{i}Il Viaggio dell'amante Respinto{/i}\"!!"

    show giovanni closed_neutral

    gio "Although I am required as music director to maintain a 'neutral' face, let me assure you that the scores for this production are {i}davvero magnifico{/i}!!"

    show giovanni open

    gio "Quite an eye-'open'ing performance, if I do say so myself!  And based on real accounts of the wild voyages of the sailor and explorer Soldini after embarking on the journey of the lifetime to heal his broken heart!"

    show giovanni angry

    gio "The first movement captures how 'angry' he feels after being betrayed by his betrothed, but he channels that fury into a daring nautical voyage!"

    show giovanni sad

    gio "The second movement follows the 'sad' sailor as his initial flare of passion dies into a melancholy, mirrored by the fog and cold dampness of the seas he ventures through.  {i}Com'è tragico{/i}!"

    show giovanni surprised

    gio "But over time, he becomes 'surprised' and enthralled by the magnificent sights he encounters and falls in love with the coasts and sea breezes of the eastern lands!"

    show giovanni happy

    gio "I am extremely 'happy' with how this turned out.  I actually worked with several musicians within the Halidom in order to draft it, and have credited them accordingly in the playbill, {i}naturalmente{/i}!"

    gio "In any case, as the lights dim, please enjoy the work which has come from my heart and spirit!!!"

    hide giovanni with dissolve

    scene black with fade

    # This goes back to script

    jump testfiles
