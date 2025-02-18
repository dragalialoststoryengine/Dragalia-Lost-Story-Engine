
    # Forager Cleo Character Procedures File

    # Paste this file into a story if you want to use Forager Cleo.  These procedures animate Forager Cleo as a speaker.

    # This program assumes that the following folders exist:
    #     -"images/cleo_forager"
    #     -"images/cleo_forager/faces"
    #     -"images/cleo_forager/mouths"



    # Forager Cleo dynamically blinks and, while speaking, also moves her mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Forager Cleo appear*:
    #  -->  show fcleo with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Forager Cleo's body*:
    #  -->  show fcleo [keyword]
    #  List of eye keywords:
    #     -->  normal (default), cocoa

    # *Changing Forager Cleo's eyes*:
    #  -->  show fcleo [keyword]
    #  List of eye keywords:
    #     -->  relaxed (default), angry, flinch, focused, neutral, pained, sad, surprised
    #          closed_relaxed

    # *Changing Forager Cleo's mouth*:
    #  -->  show fcleo [keyword]
    #  List of mouth keywords:
    #     -->  smile2 (default), smile1, mutter1, frown1, frown2, pout1, pout2,
    #          shout1, closed_frown1

    # *Writing dialogue for Forager Cleo*:
    #  --> cle "[Cleo's line here]"

    # *Making Forager Cleo disappear*:
    #  --> hide fcleo with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage fcleo:

    group body:
        
        attribute normal default:
            "images/cleo_forager/cleo_forager_body.png"

        attribute cocoa:
            "images/cleo_forager/cleo_forager_body_cocoa.png"

    group face:

        # 446/1024, 279/1024:

        pos (0.43555, 0.27246)

        attribute relaxed default:
            "fcleo_relaxed_eyes"

        attribute closed_relaxed:
            "images/cleo_forager/faces/100004_18_parts_c001.png"

        attribute neutral:
            "fcleo_neutral_eyes"

        attribute flinch:
            "fcleo_flinch_eyes"

        attribute focused:
            "fcleo_focused_eyes"
    
        attribute sad:
            "fcleo_sad_eyes"
    
        attribute pained:
            "fcleo_pained_eyes"
    
        attribute surprised:
            "fcleo_surprised_eyes"
            
        attribute angry:
            "fcleo_angry_eyes"




    group mouth:

        pos (0.43555, 0.27246)

        attribute smile2 default:
            "fcleo_smile2"

        attribute frown2:
            "fcleo_frown2"

        attribute pout2:
            "fcleo_pout2"

        attribute pout1:
            "fcleo_pout1"

        attribute smile1:
            "fcleo_smile1"

        attribute frown1:
            "fcleo_frown1"

        attribute closed_frown1:
            "images/cleo_forager/mouths/100004_18_parts_c029.png"

        attribute mutter1:
            "fcleo_mutter1"
        
        attribute shout1:
            "fcleo_shout1"




## EYE animations start here.

image fcleo_relaxed_eyes:
    "images/cleo_forager/faces/100004_18_parts_c000.png"
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
    "images/cleo_forager/faces/100004_18_parts_c002.png"
    0.05
    repeat

image fcleo_neutral_eyes:
    "images/cleo_forager/faces/100004_18_parts_c003.png"
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
    "images/cleo_forager/faces/100004_18_parts_c004.png"
    0.05
    repeat

image fcleo_flinch_eyes:
    "images/cleo_forager/faces/100004_18_parts_c010.png"
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
    "images/cleo_forager/faces/100004_18_parts_c011.png"
    0.05
    repeat

image fcleo_focused_eyes:
    "images/cleo_forager/faces/100004_18_parts_c012.png"
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
    "images/cleo_forager/faces/100004_18_parts_c013.png"
    0.05
    repeat

image fcleo_sad_eyes:
    "images/cleo_forager/faces/100004_18_parts_c014.png"
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
    "images/cleo_forager/faces/100004_18_parts_c015.png"
    0.05
    repeat

image fcleo_pained_eyes:
    "images/cleo_forager/faces/100004_18_parts_c022.png"
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
    "images/cleo_forager/faces/100004_18_parts_c023.png"
    0.05
    repeat

image fcleo_surprised_eyes:
    "images/cleo_forager/faces/100004_18_parts_c024.png"
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
    "images/cleo_forager/faces/100004_18_parts_c025.png"
    0.05
    repeat

image fcleo_angry_eyes:
    "images/cleo_forager/faces/100004_18_parts_c026.png"
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
    "images/cleo_forager/faces/100004_18_parts_c027.png"
    0.05
    repeat



# MOUTH animations start here.

image fcleo_smile2_nottalking = "images/cleo_forager/mouths/100004_18_parts_c005.png"

image fcleo_smile2_talking:
    "images/cleo_forager/mouths/100004_18_parts_c005.png"
    0.15
    "images/cleo_forager/mouths/100004_18_parts_c006.png"
    0.15
    repeat

image fcleo_smile2 = WhileSpeaking("cle", "fcleo_smile2_talking", "fcleo_smile2_nottalking")


image fcleo_frown2_nottalking = "images/cleo_forager/mouths/100004_18_parts_c008.png"

image fcleo_frown2_talking:
    "images/cleo_forager/mouths/100004_18_parts_c008.png"
    0.15
    "images/cleo_forager/mouths/100004_18_parts_c009.png"
    0.15
    repeat

image fcleo_frown2 = WhileSpeaking("cle", "fcleo_frown2_talking", "fcleo_frown2_nottalking")


image fcleo_pout2_nottalking = "images/cleo_forager/mouths/100004_18_parts_c016.png"

image fcleo_pout2_talking:
    "images/cleo_forager/mouths/100004_18_parts_c016.png"
    0.15
    "images/cleo_forager/mouths/100004_18_parts_c017.png"
    0.15
    repeat

image fcleo_pout2 = WhileSpeaking("cle", "fcleo_pout2_talking", "fcleo_pout2_nottalking")


image fcleo_pout1_nottalking = "images/cleo_forager/mouths/100004_18_parts_c018.png"

image fcleo_pout1_talking:
    "images/cleo_forager/mouths/100004_18_parts_c018.png"
    0.15
    "images/cleo_forager/mouths/100004_18_parts_c019.png"
    0.15
    repeat

image fcleo_pout1 = WhileSpeaking("cle", "fcleo_pout1_talking", "fcleo_pout1_nottalking")


image fcleo_smile1_nottalking = "images/cleo_forager/mouths/100004_18_parts_c020.png"

image fcleo_smile1_talking:
    "images/cleo_forager/mouths/100004_18_parts_c020.png"
    0.15
    "images/cleo_forager/mouths/100004_18_parts_c021.png"
    0.15
    repeat

image fcleo_smile1 = WhileSpeaking("cle", "fcleo_smile1_talking", "fcleo_smile1_nottalking")


image fcleo_frown1_nottalking = "images/cleo_forager/mouths/100004_18_parts_c029.png"

image fcleo_frown1_talking:
    "images/cleo_forager/mouths/100004_18_parts_c029.png"
    0.15
    "images/cleo_forager/mouths/100004_18_parts_c030.png"
    0.15
    repeat

image fcleo_frown1 = WhileSpeaking("cle", "fcleo_frown1_talking", "fcleo_frown1_nottalking")


image fcleo_mutter1_nottalking = "images/cleo_forager/mouths/100004_18_parts_c031.png"

image fcleo_mutter1_talking:
    "images/cleo_forager/mouths/100004_18_parts_c031.png"
    0.15
    "images/cleo_forager/mouths/100004_18_parts_c032.png"
    0.15
    repeat

image fcleo_mutter1 = WhileSpeaking("cle", "fcleo_mutter1_talking", "fcleo_mutter1_nottalking")


image fcleo_shout1_nottalking = "images/cleo_forager/mouths/100004_18_parts_c033.png"

image fcleo_shout1_talking:
    "images/cleo_forager/mouths/100004_18_parts_c033.png"
    0.15
    "images/cleo_forager/mouths/100004_18_parts_c034.png"
    0.15
    repeat

image fcleo_shout1 = WhileSpeaking("cle", "fcleo_shout1_talking", "fcleo_shout1_nottalking")








# The game starts here.

label cleoF_character_procedures:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image woods_sunset = "images/backgrounds/Sty_bg_0073_200_00.png"
    scene woods_sunset

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show fcleo with dissolve
    cle "Oh, hello there, Your Highness.  You've caught me just as I was heading back from foraging."

    show fcleo relaxed smile2
    cle "(relaxed smile2) Shall we head back to the Halidom together, then?"

    show fcleo closed_relaxed smile1
    cle "(closed_relaxed smile1) You know, it's not often that the two of us have the chance to spend time together."

    show fcleo sad frown1
    cle "(sad frown1) My daily chores have been keeping me busy as of late, after all."

    show fcleo focused pout2
    cle "(focused pout2) And that would already be enough to occupy my time, except Luca decided to set off a berry-juice bomb!"

    show fcleo angry shout1
    cle "(angry shout1) I mean, does that fool of a sylvan have a SHRED of respect for anyone else?!"
    cle "I've had to wash the curtains and carpets THRICE!!!"

    show fcleo flinch pout1
    cle "(flinch pout1) S-Sorry, I shouldn't while away our precious time together with complaints."

    show fcleo pained frown2
    cle "(pained frown2) It's just that... sometimes I wonder if I'm really making the most out of life."

    show fcleo neutral mutter1
    cle "(neutral mutter1) I mean... I haven't done any painting in ages, and I've been getting so frustrated at how ungrateful everyone seems to be..."

    show fcleo surprised closed_frown1
    cle "(surprised closed_frown1) ........."

    show fcleo relaxed smile1
    cle "Thank you, Your Highness.  Perhaps I will take a vacation soon."

    show fcleo closed_relaxed
    cle "Surely it wouldn't be too hard to have Mitsuba fill in for a few days, would it?"
    cle "And then we could spend some time foraging again afterwards!"

    show fcleo relaxed normal
    cle "(normal) But before that, I have something to share with you, as it happens."

    show fcleo cocoa
    cle "(cocoa) I was just about to prepare myself some warm cocoa, with seasonal ingredients."
    cle "Would you care to try some as well, Your Highness?"


    hide fcleo with dissolve

    # This goes back to script

    jump testfiles
