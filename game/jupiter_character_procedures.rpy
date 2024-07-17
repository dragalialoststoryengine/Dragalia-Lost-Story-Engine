
    # Jupiter Character Procedures File

    # Paste this file into a story if you want to use Jupiter.  These procedures animate Jupiter as a speaker.
    # You'll also need to paste THIS line into your actual script above the script label whenever you're using Jupiter:

define jupi = Character("Jupiter", callback=speaker("jupi"))

    # This program assumes that the following folders exist:
    #     -"images/jupiter"
    #     -"images/jupiter/faces"
    #     -"images/jupiter/mouths"
    #
    #     -"images/jupiter_high"
    #     -"images/jupiter_high/faces"
    #     -"images/jupiter_high/mouths"
    #
    #     -"images/jupiter_zero"


    # Jupiter dynamically blinks and, while speaking, can moves his mouth along with the text scroll (if desired).

    # FUNCTIONS:

    # *Making Jupiter appear*:
    #  -->  show jupiter with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Jupiter's eyes*:
    #  -->  show jupiter [keyword]
    #  List of eye keywords:
    #     -->  normal (default), closed, narrowed, smug, surprised

    # *Changing Jupiter's mouth*:
    #  -->  show jupiter [keyword]
    #  List of mouth keywords:
    #     -->  mouth_open1 (default), mouth_closed1, mouth_flap1

    # *Writing dialogue for Jupiter*:
    #  --> jupi "[Jupiter's line here]"

    # *Making Jupiter disappear*:
    #  --> hide jupiter with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # *Making High Jupiter appear*:
    #  -->  show highjupiter with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing High Jupiter's eyes*:
    #  -->  show highjupiter [keyword]
    #  List of eye keywords:
    #     -->  normal (default), closed, surprised

    # *Changing High Jupiter's mouth*:
    #  -->  show highjupiter [keyword]
    #  List of mouth keywords:
    #     -->  mouth_open1 (default), mouth_wide1, mouth_flap1

    # *Making High Jupiter disappear*:
    #  --> hide highjupiter with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # *Making Jupiter Zero appear*:
    #  -->  show jupiter0 with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Making Jupiter Zero disappear*:
    #  --> hide jupiter0 with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)



    # # # # #


layeredimage jupiter:

    always "images/jupiter/jupiter_body.png"

    group face:

        # 243/1024, 276/1024:

        pos (0.237305, 0.269531)

        attribute normal default:
            "jupiter_normal_eyes"

        attribute narrowed:
            "jupiter_narrowed_eyes"

        attribute closed:
            "images/jupiter/faces/210004_01_parts_c001.png"

        attribute surprised:
            "jupiter_surprised_eyes"

        attribute smug:
            "jupiter_smug_eyes"


    group mouth:

        pos (0.237305, 0.269531)

        attribute mouth_open1 default:
            "images/jupiter/mouths/210004_01_parts_c003.png"

        attribute mouth_closed1:
            "images/jupiter/mouths/210004_01_parts_c007.png"

        attribute mouth_flap1:
            "jupiter_mouth_flap1"



layeredimage highjupiter:

    always "images/jupiter_high/jupiter_high_body.png"

    group face:

        # 433/1024, 187/1024:
        pos (0.422852, 0.182617)

        attribute normal default:
            "jupiter_high_normal_eyes"

        attribute closed:
            "images/jupiter_high/faces/210041_01_parts_c001.png"

        attribute surprised:
            "jupiter_high_surprised_eyes"

    group mouth:

        pos (0.422852, 0.182617)

        attribute mouth_open1 default:
            "images/jupiter_high/mouths/210041_01_parts_c003.png"
        
        attribute mouth_wide1:
            "images/jupiter_high/mouths/210041_01_parts_c008.png"

        attribute mouth_flap1:
            "jupiter_high_mouth_flap1"




image jupiter0 = "images/jupiter_zero/jupiter_zero_body.png"








## EYE animations start here.

image jupiter_normal_eyes:
    "images/jupiter/faces/210004_01_parts_c000.png"
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
    "images/jupiter/faces/210004_01_parts_c001.png"
    0.05
    repeat

image jupiter_narrowed_eyes:
    "images/jupiter/faces/210004_01_parts_c005.png"
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
    "images/jupiter/faces/210004_01_parts_c001.png"
    0.05
    repeat

image jupiter_surprised_eyes:
    "images/jupiter/faces/210004_01_parts_c006.png"
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
    "images/jupiter/faces/210004_01_parts_c001.png"
    0.05
    repeat

image jupiter_smug_eyes:
    "images/jupiter/faces/210004_01_parts_c011.png"
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
    "images/jupiter/faces/210004_01_parts_c001.png"
    0.05
    repeat



image jupiter_high_normal_eyes:
    "images/jupiter_high/faces/210041_01_parts_c000.png"
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
    "images/jupiter_high/faces/210041_01_parts_c001.png"
    0.05
    repeat

image jupiter_high_surprised_eyes:
    "images/jupiter_high/faces/210041_01_parts_c005.png"
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
    "images/jupiter_high/faces/210041_01_parts_c001.png"
    0.05
    repeat


# MOUTH animations start here.


image jupiter_mouth_flap1_nottalking = "images/jupiter/mouths/210004_01_parts_c007.png"

image jupiter_mouth_flap1_talking:
    "images/jupiter/mouths/210004_01_parts_c003.png"
    0.15
    "images/jupiter/mouths/210004_01_parts_c007.png"
    0.15
    repeat

image jupiter_mouth_flap1 = WhileSpeaking("jupi", "jupiter_mouth_flap1_talking", "jupiter_mouth_flap1_nottalking")



image jupiter_high_mouth_flap1_nottalking = "images/jupiter_high/mouths/210041_01_parts_c003.png"

image jupiter_high_mouth_flap1_talking:
    "images/jupiter_high/mouths/210041_01_parts_c008.png"
    0.15
    "images/jupiter_high/mouths/210041_01_parts_c003.png"
    0.15
    repeat

image jupiter_high_mouth_flap1 = WhileSpeaking("jupi", "jupiter_high_mouth_flap1_talking", "jupiter_high_mouth_flap1_nottalking")







# The game starts here.

label jupiter_character_procedures:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image mountain_sunset = "images/backgrounds/Sty_bg_0038_200_00.png"


    scene mountain_sunset with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show jupiter with dissolve
    jupi "Oho, welcome, welcome!  You know, I was just wondering how things were going with you!"

    show jupiter normal mouth_open1
    jupi "(normal mouth_open1) You know, since that whole lawyer situation, I've actually had people coming all the way up the mountain to give me cases."

    show jupiter smug
    jupi "(smug) It's been an excellent side hustle, in addition to the whole 'saving the world' thing.  My hoard of rupies is growing like a weed, hee hee!"

    show jupiter narrowed mouth_closed1
    jupi "(narrowed mouth_closed1) So anyway, what can I do for you?  If it's time-consuming, I hope you're prepared to compensate me for my efforts."

    show jupiter surprised mouth_flap1
    jupi "(surprised mouth_flap1) ...Well, of COURSE we're friends!  I haven't met anyone as entertaining as you since Alberius himself!  But still, remuneration is remuneration."

    show jupiter smug mouth_open1
    jupi "...Oh, so the request comes from Princess Chelle?  How intriguing.  Maybe I should actually take this seriously." 


    hide jupiter with dissolve


    show highjupiter with dissolve
    jupi "There.  A more formal look for a more formal occasion."

    show highjupiter normal mouth_open1
    jupi "(normal mouth_open1) This ought to be a guise more fitting of a royal meeting."

    show highjupiter surprised mouth_wide1
    jupi "(surprised mouth_wide1) ...Yes, yes, obviously you're ALSO a royal.  But... well, you don't act like it very much, do you?"

    show highjupiter closed mouth_flap1
    jupi "(closed mouth_flap1) Chelle conducts herself like a ruler, her eyes full of ambition and yet inscrutable.  Meanwhile... you're a bit of an open book who wouldn't hurt a fly."
    jupi "...I'm not saying I'd rather be pactbound to her, I'm just saying you could take some pointers from her.  She's interesting and fun."

    hide highjupiter with dissolve

    show jupiter0 with dissolve
    jupi "Urgh... FINE!  This is an even MORE formal form, just for you!  Are you done being jealous, or can I go take my leave to find out what the princess wants of me?"
    jupi "And I thought {i}I{/i} was the self-centered one.  Hmph!"

    hide mercury0 with dissolve

    # This goes back to script

    jump testfiles
