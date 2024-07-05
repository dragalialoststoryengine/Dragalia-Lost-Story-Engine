
    # Pia Character Procedures File

    # Paste this file into a story if you want to use Elisanne.  These procedures animate Elisanne as a speaker.
    # You'll also need to paste THIS line into your actual script above the script label whenever you're using Elisanne:

define pia = Character("Pia", callback=speaker("pia"))

    # This program assumes that the following folders exist:
    #     -"images/pia"
    #     -"images/pia/faces"
    #     -"images/pia/mouths"

    # Pia dynamically blinks and, while speaking, also moves her mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Pia appear*:
    #  -->  show pia_img with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # IMPORTANT NOTE:  "pia" refers to the SPEAKER Pia, and "pia_img" is her dynamic image.
    # The reason for this distinction is because Pia is already 3 letters, so her speaker tag and
    # image tag would be the same if i followed the usual convention.

    # *Changing whether Pia has a book or not*:
    #  -->  show pia_img [keyword]
    #  List of body keywords:
    #     -->  no_book (the default option), book

    # *Changing Pia's eyes*:
    #  -->  show pia_img [keyword]
    #  List of eye keywords:
    #     -->  neutral (the default option), neutral2, serious, cry, surprised, surprised2,
    #          sad, worried, closed_neutral

    # *Changing Pia's mouth*:
    #  -->  show pia_img [keyword]
    #  List of mouth keywords:
    #     -->  frown1 (the default option), frown2, frown3, frown4, frown5, frown6, frown7,
    #          smile1, smile2

    # *Writing dialogue for Pia*:
    #  --> pia "[Elisanne's line here]"

    # *Making Pia disappear*:
    #  --> hide pia_img with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage pia_img:

    group body:
        attribute no_book default:
            "images/pia/pia_body.png"

        attribute book:
            "images/pia/pia_body_with_book.png"

    group face:

        # 478/1028, 301/1028:
        pos (0.46498, 0.29280)

        attribute neutral default:
            "pia_neutral_eyes"

        attribute serious:
            "pia_serious_eyes"

        attribute neutral2:
            "pia_neutral2_eyes"

        attribute cry:
            "pia_cry_eyes"

        attribute surprised:
            "pia_surprised_eyes"

        attribute surprised2:
            "pia_surprised2_eyes"

        attribute sad:
            "pia_sad_eyes"

        attribute worried:
            "pia_worried_eyes"

        attribute closed_neutral:
            "images/pia/faces/110302_01_parts_c029.png"


    group mouth:

        pos (0.46498, 0.29280)

        attribute frown1 default:
            "pia_frown1"

        attribute frown2:
            "pia_frown2"

        attribute smile1:
            "pia_smile1"

        attribute frown3:
            "pia_frown3"

        attribute frown4:
            "pia_frown4"

        attribute smile2:
            "pia_smile2"

        attribute frown5:
            "pia_frown5"

        attribute frown6:
            "pia_frown6"

        attribute frown7:
            "pia_frown7"


## EYE animations start here.

image pia_neutral_eyes:
    "images/pia/faces/110302_01_parts_c000.png"
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
    "images/pia/faces/110302_01_parts_c001.png"
    0.05
    repeat

image pia_serious_eyes:
    "images/pia/faces/110302_01_parts_c002.png"
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
    "images/pia/faces/110302_01_parts_c003.png"
    0.05
    repeat

image pia_neutral2_eyes:
    "images/pia/faces/110302_01_parts_c009.png"
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
    "images/pia/faces/110302_01_parts_c010.png"
    0.05
    repeat

image pia_cry_eyes:
    "images/pia/faces/110302_01_parts_c011.png"
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
    "images/pia/faces/110302_01_parts_c012.png"
    0.05
    repeat


image pia_surprised_eyes:
    "images/pia/faces/110302_01_parts_c013.png"
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
    "images/pia/faces/110302_01_parts_c014.png"
    0.05
    repeat

image pia_surprised2_eyes:
    "images/pia/faces/110302_01_parts_c015.png"
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
    "images/pia/faces/110302_01_parts_c016.png"
    0.05
    repeat

image pia_sad_eyes:
    "images/pia/faces/110302_01_parts_c025.png"
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
    "images/pia/faces/110302_01_parts_c026.png"
    0.05
    repeat

image pia_worried_eyes:
    "images/pia/faces/110302_01_parts_c027.png"
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
    "images/pia/faces/110302_01_parts_c028.png"
    0.05
    repeat




# MOUTH animations start here.

image pia_frown1_nottalking = "images/pia/mouths/110302_01_parts_c004.png"

image pia_frown1_talking:
    "images/pia/mouths/110302_01_parts_c004.png"
    0.15
    "images/pia/mouths/110302_01_parts_c005.png"
    0.15
    repeat

image pia_frown1 = WhileSpeaking("pia", "pia_frown1_talking", "pia_frown1_nottalking")


image pia_frown2_nottalking = "images/pia/mouths/110302_01_parts_c007.png"

image pia_frown2_talking:
    "images/pia/mouths/110302_01_parts_c007.png"
    0.15
    "images/pia/mouths/110302_01_parts_c008.png"
    0.15
    repeat

image pia_frown2 = WhileSpeaking("pia", "pia_frown2_talking", "pia_frown2_nottalking")


image pia_smile1_nottalking = "images/pia/mouths/110302_01_parts_c017.png"

image pia_smile1_talking:
    "images/pia/mouths/110302_01_parts_c017.png"
    0.15
    "images/pia/mouths/110302_01_parts_c018.png"
    0.15
    repeat

image pia_smile1 = WhileSpeaking("pia", "pia_smile1_talking", "pia_smile1_nottalking")


image pia_frown3_nottalking = "images/pia/mouths/110302_01_parts_c019.png"

image pia_frown3_talking:
    "images/pia/mouths/110302_01_parts_c019.png"
    0.15
    "images/pia/mouths/110302_01_parts_c020.png"
    0.15
    repeat

image pia_frown3 = WhileSpeaking("pia", "pia_frown3_talking", "pia_frown3_nottalking")


image pia_frown4_nottalking = "images/pia/mouths/110302_01_parts_c021.png"

image pia_frown4_talking:
    "images/pia/mouths/110302_01_parts_c021.png"
    0.15
    "images/pia/mouths/110302_01_parts_c022.png"
    0.15
    repeat

image pia_frown4 = WhileSpeaking("pia", "pia_frown4_talking", "pia_frown4_nottalking")


image pia_smile2_nottalking = "images/pia/mouths/110302_01_parts_c023.png"

image pia_smile2_talking:
    "images/pia/mouths/110302_01_parts_c023.png"
    0.15
    "images/pia/mouths/110302_01_parts_c024.png"
    0.15
    repeat

image pia_smile2 = WhileSpeaking("pia", "pia_smile2_talking", "pia_smile2_nottalking")


image pia_frown5_nottalking = "images/pia/mouths/110302_01_parts_c030.png"

image pia_frown5_talking:
    "images/pia/mouths/110302_01_parts_c030.png"
    0.15
    "images/pia/mouths/110302_01_parts_c031.png"
    0.15
    repeat

image pia_frown5 = WhileSpeaking("pia", "pia_frown5_talking", "pia_frown5_nottalking")


image pia_frown6_nottalking = "images/pia/mouths/110302_01_parts_c032.png"

image pia_frown6_talking:
    "images/pia/mouths/110302_01_parts_c032.png"
    0.15
    "images/pia/mouths/110302_01_parts_c033.png"
    0.15
    repeat

image pia_frown6 = WhileSpeaking("pia", "pia_frown6_talking", "pia_frown6_nottalking")


image pia_frown7_nottalking = "images/pia/mouths/110302_01_parts_c034.png"

image pia_frown7_talking:
    "images/pia/mouths/110302_01_parts_c034.png"
    0.15
    "images/pia/mouths/110302_01_parts_c035.png"
    0.15
    repeat

image pia_frown7 = WhileSpeaking("pia", "pia_frown7_talking", "pia_frown7_nottalking")














# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

transform middle:
    xalign 0.5
    yalign 0.5

transform leftspot:
    xalign -0.25
    yalign 0.5

transform rightspot:
    xalign 1.25
    yalign 0.5









# The game starts here.

label pia_character_procedures:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image chapel = "images/backgrounds/Sty_bg_0013_100_00.png"
    scene chapel at middle

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    show pia_img with dissolve

    pia "Wh... What?  You want me to do... facial exercises?"
    pia "R-Really?  It helps with articulation and tone when singing?"
    pia "W-Well, ok then!  I'll try my best!"

    show pia_img book
    pia "Oh, but hang on, let me take out my choir excercises book first!"
    pia "Ok, I'm all set!  Now, let's try it!"

    show pia_img neutral
    pia "This is what I sound like when my face is neutral!  Ah... Ahhh!"

    show pia_img neutral2
    pia "And... this is a different neutral expresion (neutral2)!"

    show pia_img serious
    pia "Here's a more serious expression!  Apparently this is good for giving the song some... 'gravitas'?"

    show pia_img cry
    pia "I... I guess I can cry a little, if I'm feeling emotional."

    show pia_img surprised
    pia "Wow!  That really muffled things up!  I feel really surprised now!"

    show pia_img surprised2
    pia "And... this is a different surprised face (surprised2)!  I tried to soften it a little!"

    show pia_img sad
    pia "Here's a sad face, but... I'm not crying, because I'm a big girl!"

    show pia_img worried
    pia "And... this is a worried face!"

    show pia_img closed_neutral
    pia "And... if I close my eyes (closed_neutral), then... I can sound like this!"

    show pia_img neutral
    show pia_img no_book
    pia "Ok, I'm done now!  I'll put my book away-"

    show pia_img surprised
    pia "Wait, I'm not?  I have to change my mouth expression too?"
    pia "I-I'm sorry!  I'll do that next!"

    show pia_img neutral
    show pia_img frown1
    pia "Um... so this is my usual face, but... I guess it's a frown (frown1)?  I'll sing a scale:  la-la-la-la-la-la-la-la-la-laaa!"

    show pia_img frown2
    pia "And... this is another frown (frown2).  I'll sing a scale:  la-la-la-la-la-la-la-la-la-laaa!"

    show pia_img frown3
    pia "Uh... I'm getting nervous, but... here's a third frown (frown3).  I'll sing a scale:  la-la-la-la-la-la-la-la-la-laaa!"

    show pia_img frown4
    pia "A-And a fourth frown (frown4)!! I'll sing a scale:  la-la-la-la-la-la-la-la-la-laaa!"

    show pia_img frown5
    pia "Umm... I think I can make a fifth frown (frown5), maybe?...  I'll sing a scale:  la-la-la-la-la-la-la-la-la-laaa!"

    show pia_img frown6
    pia "Oh, and maybe this one (frown6)!  I'll sing a scale:  la-la-la-la-la-la-la-la-la-laaa!"

    show pia_img frown7
    pia "Uhhhh... I can't think of anything else besides this one (frown5)!!!  I'll sing a scale:  la-la-la-la-la-la-la-la-la-laaa!"

    show pia_img smile1
    pia "O-Oh, I can smile (smile1) now??  That's a relief! I'll sing a scale:  la-la-la-la-la-la-la-la-la-laaa!"

    show pia_img smile2
    pia "And here's another one (smile2):  la-la-la-la-la-la-la-la-la-laaa!"

    pia "Phew, this is really tricky!  This really took a lot of energy!"
    pia "I'm all tired now..."

    show pia_img frown1
    pia "Would you mind if I took a break to feed Mr. Mouse?  He looks hungry!"

    show pia_img smile2
    pia "Oh, ok then!  I'll be back soon!"


    # This goes back to script

    jump testfiles
