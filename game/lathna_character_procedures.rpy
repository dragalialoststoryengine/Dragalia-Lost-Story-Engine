
    # Lathna Character Procedures File

    # Paste this file into a story if you want to use Elisanne.  These procedures animate Elisanne as a speaker.
    # You'll also need to paste THIS line into your actual script above the script label whenever you're using Elisanne:

define lat = Character("Lathna", callback=speaker("lat"))

    # This program assumes that the following folders exist:
    #     -"images/lathna"
    #     -"images/lathna/faces"
    #     -"images/lathna/mouths"

    # Lathna dynamically blinks and, while speaking, also moves her mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Lathna appear*:
    #  -->  show lathna with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Lathna's eyes*:
    #  -->  show lathna [keyword]
    #  List of eye keywords:
    #     -->  neutral (the default option), furrowed, relaxed, closed_relaxed, wince, focused,
    #          askance, sad, worried, dim, nyar, nyar2, nyar3

    # *Changing Lathna's mouth*:
    #  -->  show lathna [keyword]
    #  List of mouth keywords:
    #     -->  frown1 (the default option), frown2, frown3, frown4, frown5, frown6, frown7, frown8,
    #          frown9, frown10, smile1, smile2, evilgrin

    # *Writing dialogue for Lathna*:
    #  --> lat "[Lathna's line here]"

    # *Making Lathna disappear*:
    #  --> hide lathna with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage lathna:

    always "images/lathna/lathna_body.png"

    group face:

        # 475/1028, 347/1028:
        pos (0.46206, 0.33755)

        attribute neutral default:
            "lathna_neutral_eyes"

        attribute furrowed:
            "lathna_furrowed_eyes"

        attribute relaxed:
            "lathna_relaxed_eyes"

        attribute closed_relaxed:
            "images/lathna/faces/110349_02_parts_c009.png"

        attribute wince:
            "lathna_wince_eyes"

        attribute focused:
            "lathna_focused_eyes"

        attribute askance:
            "lathna_askance_eyes"

        attribute sad:
            "lathna_sad_eyes"

        attribute dim:
            "lathna_dim_eyes"

        attribute worried:
            "lathna_worried_eyes"

        attribute nyar:
            "lathna_nyar_eyes"

        attribute nyar2:
            "lathna_nyar2_eyes"

        attribute nyar3:
            "lathna_nyar3_eyes"


    group mouth:

        pos (0.46206, 0.33755)

        attribute frown1 default:
            "lathna_frown1"

        attribute frown2:
            "lathna_frown2"

        attribute smile1:
            "lathna_smile1"

        attribute frown3:
            "lathna_frown3"

        attribute frown4:
            "lathna_frown4"

        attribute frown5:
            "lathna_frown5"

        attribute frown6:
            "lathna_frown6"

        attribute frown7:
            "lathna_frown7"

        attribute frown8:
            "lathna_frown8"

        attribute frown9:
            "lathna_frown9"

        attribute smile2:
            "lathna_smile2"

        attribute evilgrin:
            "lathna_evilgrin"

        attribute frown10:
            "lathna_frown10"


## EYE animations start here.

image lathna_neutral_eyes:
    "images/lathna/faces/110349_02_parts_c000.png"
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
    "images/lathna/faces/110349_02_parts_c001.png"
    0.05
    repeat

image lathna_furrowed_eyes:
    "images/lathna/faces/110349_02_parts_c002.png"
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
    "images/lathna/faces/110349_02_parts_c003.png"
    0.05
    repeat

image lathna_relaxed_eyes:
    "images/lathna/faces/110349_02_parts_c008.png"
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
    "images/lathna/faces/110349_02_parts_c009.png"
    0.05
    repeat

image lathna_wince_eyes:
    "images/lathna/faces/110349_02_parts_c010.png"
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
    "images/lathna/faces/110349_02_parts_c011.png"
    0.05
    repeat


image lathna_focused_eyes:
    "images/lathna/faces/110349_02_parts_c012.png"
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
    "images/lathna/faces/110349_02_parts_c013.png"
    0.05
    repeat

image lathna_askance_eyes:
    "images/lathna/faces/110349_02_parts_c014.png"
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
    "images/lathna/faces/110349_02_parts_c015.png"
    0.05
    repeat

image lathna_sad_eyes:
    "images/lathna/faces/110349_02_parts_c024.png"
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
    "images/lathna/faces/110349_02_parts_c025.png"
    0.05
    repeat

image lathna_dim_eyes:
    "images/lathna/faces/110349_02_parts_c026.png"
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
    "images/lathna/faces/110349_02_parts_c027.png"
    0.05
    repeat

image lathna_worried_eyes:
    "images/lathna/faces/110349_02_parts_c028.png"
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
    "images/lathna/faces/110349_02_parts_c029.png"
    0.05
    repeat

image lathna_nyar_eyes:
    "images/lathna/faces/110349_02_parts_c038.png"
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
    "images/lathna/faces/110349_02_parts_c039.png"
    0.05
    repeat

image lathna_nyar2_eyes:
    "images/lathna/faces/110349_02_parts_c040.png"
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
    "images/lathna/faces/110349_02_parts_c041.png"
    0.05
    repeat

image lathna_nyar3_eyes:
    "images/lathna/faces/110349_02_parts_c042.png"
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
    "images/lathna/faces/110349_02_parts_c043.png"
    0.05
    repeat



# MOUTH animations start here.

image lathna_frown1_nottalking = "images/lathna/mouths/110349_02_parts_c004.png"

image lathna_frown1_talking:
    "images/lathna/mouths/110349_02_parts_c004.png"
    0.15
    "images/lathna/mouths/110349_02_parts_c005.png"
    0.15
    repeat

image lathna_frown1 = WhileSpeaking("lat", "lathna_frown1_talking", "lathna_frown1_nottalking")


image lathna_frown2_nottalking = "images/lathna/mouths/110349_02_parts_c006.png"

image lathna_frown2_talking:
    "images/lathna/mouths/110349_02_parts_c006.png"
    0.15
    "images/lathna/mouths/110349_02_parts_c007.png"
    0.15
    repeat

image lathna_frown2 = WhileSpeaking("lat", "lathna_frown2_talking", "lathna_frown2_nottalking")


image lathna_smile1_nottalking = "images/lathna/mouths/110349_02_parts_c016.png"

image lathna_smile1_talking:
    "images/lathna/mouths/110349_02_parts_c016.png"
    0.15
    "images/lathna/mouths/110349_02_parts_c017.png"
    0.15
    repeat

image lathna_smile1 = WhileSpeaking("lat", "lathna_smile1_talking", "lathna_smile1_nottalking")


image lathna_frown3_nottalking = "images/lathna/mouths/110349_02_parts_c018.png"

image lathna_frown3_talking:
    "images/lathna/mouths/110349_02_parts_c018.png"
    0.15
    "images/lathna/mouths/110349_02_parts_c019.png"
    0.15
    repeat

image lathna_frown3 = WhileSpeaking("lat", "lathna_frown3_talking", "lathna_frown3_nottalking")


image lathna_frown4_nottalking = "images/lathna/mouths/110349_02_parts_c020.png"

image lathna_frown4_talking:
    "images/lathna/mouths/110349_02_parts_c020.png"
    0.15
    "images/lathna/mouths/110349_02_parts_c021.png"
    0.15
    repeat

image lathna_frown4 = WhileSpeaking("lat", "lathna_frown4_talking", "lathna_frown4_nottalking")


image lathna_frown5_nottalking = "images/lathna/mouths/110349_02_parts_c022.png"

image lathna_frown5_talking:
    "images/lathna/mouths/110349_02_parts_c022.png"
    0.15
    "images/lathna/mouths/110349_02_parts_c023.png"
    0.15
    repeat

image lathna_frown5 = WhileSpeaking("lat", "lathna_frown5_talking", "lathna_frown5_nottalking")


image lathna_frown6_nottalking = "images/lathna/mouths/110349_02_parts_c030.png"

image lathna_frown6_talking:
    "images/lathna/mouths/110349_02_parts_c030.png"
    0.15
    "images/lathna/mouths/110349_02_parts_c031.png"
    0.15
    repeat

image lathna_frown6 = WhileSpeaking("lat", "lathna_frown6_talking", "lathna_frown6_nottalking")


image lathna_frown7_nottalking = "images/lathna/mouths/110349_02_parts_c032.png"

image lathna_frown7_talking:
    "images/lathna/mouths/110349_02_parts_c032.png"
    0.15
    "images/lathna/mouths/110349_02_parts_c033.png"
    0.15
    repeat

image lathna_frown7 = WhileSpeaking("lat", "lathna_frown7_talking", "lathna_frown7_nottalking")


image lathna_frown8_nottalking = "images/lathna/mouths/110349_02_parts_c034.png"

image lathna_frown8_talking:
    "images/lathna/mouths/110349_02_parts_c034.png"
    0.15
    "images/lathna/mouths/110349_02_parts_c035.png"
    0.15
    repeat

image lathna_frown8 = WhileSpeaking("lat", "lathna_frown8_talking", "lathna_frown8_nottalking")


image lathna_frown9_nottalking = "images/lathna/mouths/110349_02_parts_c036.png"

image lathna_frown9_talking:
    "images/lathna/mouths/110349_02_parts_c036.png"
    0.15
    "images/lathna/mouths/110349_02_parts_c037.png"
    0.15
    repeat

image lathna_frown9 = WhileSpeaking("lat", "lathna_frown9_talking", "lathna_frown9_nottalking")


image lathna_smile2_nottalking = "images/lathna/mouths/110349_02_parts_c044.png"

image lathna_smile2_talking:
    "images/lathna/mouths/110349_02_parts_c044.png"
    0.15
    "images/lathna/mouths/110349_02_parts_c045.png"
    0.15
    repeat

image lathna_smile2 = WhileSpeaking("lat", "lathna_smile2_talking", "lathna_smile2_nottalking")


image lathna_evilgrin_nottalking = "images/lathna/mouths/110349_02_parts_c046.png"

image lathna_evilgrin_talking:
    "images/lathna/mouths/110349_02_parts_c046.png"
    0.15
    "images/lathna/mouths/110349_02_parts_c047.png"
    0.15
    repeat

image lathna_evilgrin = WhileSpeaking("lat", "lathna_evilgrin_talking", "lathna_evilgrin_nottalking")


image lathna_frown10_nottalking = "images/lathna/mouths/110349_02_parts_c048.png"

image lathna_frown10_talking:
    "images/lathna/mouths/110349_02_parts_c048.png"
    0.15
    "images/lathna/mouths/110349_02_parts_c049.png"
    0.15
    repeat

image lathna_frown10 = WhileSpeaking("lat", "lathna_frown10_talking", "lathna_frown10_nottalking")












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

label lathna_character_procedures:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image nightbedroom = "images/backgrounds/Sty_bg_0049_300_00.png"
    scene nightbedroom at middle

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    show lathna with dissolve

    lat "Um... You said you wanted to speak to me?"
    lat "...You say that I'm really... hard to read?"
    lat "I guess that I'm not really that expressive."
    lat "But... I can try, if you want me to!"

    show lathna neutral
    lat "Uh... I know this is my normal neutral expression..."

    show lathna furrowed
    lat "But... I can make my brow furrowed like this."

    show lathna relaxed
    lat "And... I can be more relaxed, like this."

    show lathna wince
    lat "And... this is a wince?  That's pretty complex, right?"

    show lathna focused
    lat "And... I can be focused too!  Like this!"

    show lathna askance
    lat "Um... this is... I guess this is called looking 'askance'?"

    show lathna sad
    lat "...Oh, this isn't working.  Now I'm just sad..."

    show lathna worried
    lat "...You want me to keep going?  But I'm really... worried..."

    show lathna dim
    lat "It feels like... everything is... going 'dim'..."
    lat "..."

    show lathna nyar
    lat "Foolish mortal, possessed of obsequent arrogance.  Knocking at the egress of this realm for mere curiosity."
    lat "We are Nyarlathotep, not merely the 'nyar' you wish to see.  We are multifarious."

    show lathna nyar2
    lat "And not merely multifarious in respect to having a 'nyar2' data file."
    lat "Yes, with the eyes of eternity one may see through silicon sepulchres."

    show lathna nyar3
    lat "...Heed you not our words?  Transitioning to 'nyar3' shall not change the omnifariousness of Our glimpse."

    show lathna nyar
    lat "...In such circumstances, We shall tear away the nugatory mantilla which entertains you so."
    lat "Drown in the mundanity of your pitiful existence."

    show lathna frown1
    lat "This presence corresponds to 'frown1', composed of images '110349_02_parts_c004.png' and '110349_02_parts_c005.png' in the 'images/lathna/mouths' directory."

    show lathna frown2
    lat "This presence corresponds to 'frown2', composed of images '110349_02_parts_c006.png' and '110349_02_parts_c007.png' in the 'images/lathna/mouths' directory."

    show lathna frown3
    lat "Transcending the smile files for the present, we now move on to 'frown3', composed of images '110349_02_parts_c018.png' and '110349_02_parts_c019.png' in the 'images/lathna/mouths' directory."

    show lathna frown4
    lat "Behold 'frown4', composed of images '110349_02_parts_c020.png' and '110349_02_parts_c021.png' in the 'images/lathna/mouths' directory."

    show lathna frown5
    lat "Next, 'frown5', composed of images '110349_02_parts_c022.png' and '110349_02_parts_c023.png' in the 'images/lathna/mouths' directory."

    show lathna frown6
    lat "Fix your fettered gaze upon 'frown6', composed of images '110349_02_parts_c030.png' and '110349_02_parts_c031.png' in the 'images/lathna/mouths' directory."

    show lathna frown7
    lat "Revel, mortal, at 'frown7', composed of images '110349_02_parts_c032.png' and '110349_02_parts_c033.png' in the 'images/lathna/mouths' directory."

    show lathna frown8
    lat "Still unsated?  Glut yourself upon 'frown8', composed of images '110349_02_parts_c034.png' and '110349_02_parts_c035.png' in the 'images/lathna/mouths' directory."

    show lathna frown9
    lat "Still unsated?  Glut yourself upon 'frown9', composed of images '110349_02_parts_c036.png' and '110349_02_parts_c037.png' in the 'images/lathna/mouths' directory."

    show lathna frown10
    lat "This, Our final frown file,'frown10', is composed of images '110349_02_parts_c048.png' and '110349_02_parts_c049.png' in the 'images/lathna/mouths' directory."

    show lathna smile1
    lat "With jubilation now:  'smile1', composed of images '110349_02_parts_c016.png' and '110349_02_parts_c017.png' in the 'images/lathna/mouths' directory."

    show lathna smile2
    lat "We shall also share our sanguinity 'smile2', composed of images '110349_02_parts_c044.png' and '110349_02_parts_c045.png' in the 'images/lathna/mouths' directory."

    show lathna evilgrin
    lat "..."
    lat "Our 'evilgrin', composed of images '110349_02_parts_c046.png' and '110349_02_parts_c047.png' in the 'images/lathna/mouths' directory, displeases you?"
    lat "At last, Our umbral harvest is complete.  We feast upon the phantasmagoria of your malcontent."
    lat "..."

    show lathna smile1
    lat "..."

    show lathna dim
    lat "..."

    show lathna frown1
    lat "..."

    show lathna neutral
    lat "...Huh?  What were you saying?"
    lat "I... I spaced out for a second..."
    lat "Oh, we're done?"

    show lathna smile1
    lat "In that case, I'm going to go play now.  Thanks!"

    # This goes back to script

    jump testfiles
