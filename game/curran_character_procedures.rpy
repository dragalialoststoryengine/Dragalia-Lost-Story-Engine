
    # Curran Character Procedures File

    # Paste this file into a story if you want to use Curran.  These procedures animate Curran as a speaker.
    # You'll also need to paste THIS line into your actual script above the script label whenever you're using Elisanne:

define cur = Character("Curran", callback=speaker("cur"))

    # This program assumes that the following folders exist:
    #     -"images/curran"
    #     -"images/curran/faces"
    #     -"images/curran/mouths"

    # Curran dynamically blinks and, while speaking, also moves her mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Curran appear*:
    #  -->  show curran with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Curran's eyes*:
    #  -->  show curran [keyword]
    #  List of eye keywords:
    #     -->  neutral (the default option), neutral2, closed_neutral, focused, focused2, focused3,
    #          sweat, blush, askance, angry

    # *Changing Curran's mouth*:
    #  -->  show curran [keyword]
    #  List of mouth keywords:
    #     -->  frown1 (the default option), frown2, frown3, frown4, frown5, frown6, frown7, frown8,
    #          frown9, grimace1, grimace2, smile1

    # *Writing dialogue for Curran*:
    #  --> cur "[Curran's line here]"

    # *Making Curran disappear*:
    #  --> hide curran with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage curran:

    always "images/curran/curran_body.png"

    group face:

        # 428/1028, 179/1028:
        pos (0.41634, 0.17412)

        attribute neutral default:
            "curran_neutral_eyes"

        attribute closed_neutral:
            "images/curran/faces/110281_01_parts_c002.png"

        attribute neutral2:
            "curran_neutral2_eyes"

        attribute focused:
            "curran_focused_eyes"

        attribute relaxed:
            "curran_relaxed_eyes"

        attribute focused2:
            "curran_focused2_eyes"

        attribute sweat:
            "curran_sweat_eyes"

        attribute blush:
            "curran_blush_eyes"

        attribute askance:
            "curran_askance_eyes"

        attribute focused3:
            "curran_focused3_eyes"

        attribute angry:
            "curran_angry_eyes"


    group mouth:

        pos (0.41634, 0.17412)

        attribute frown1 default:
            "curran_frown1"

        attribute frown2:
            "curran_frown2"

        attribute frown3:
            "curran_frown3"

        attribute grimace1:
            "curran_grimace1"

        attribute smile1:
            "curran_smile1"

        attribute grimace2:
            "curran_grimace2"

        attribute frown4:
            "curran_frown4"

        attribute frown5:
            "curran_frown5"

        attribute frown6:
            "curran_frown6"

        attribute frown7:
            "curran_frown7"

        attribute frown8:
            "curran_frown8"

        attribute frown9:
            "curran_frown9"


## EYE animations start here.

image curran_neutral_eyes:
    "images/curran/faces/110281_01_parts_c000.png"
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
    "images/curran/faces/110281_01_parts_c001.png"
    0.05
    repeat

image curran_neutral2_eyes:
    "images/curran/faces/110281_01_parts_c004.png"
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
    "images/curran/faces/110281_01_parts_c005.png"
    0.05
    repeat

image curran_focused_eyes:
    "images/curran/faces/110281_01_parts_c006.png"
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
    "images/curran/faces/110281_01_parts_c007.png"
    0.05
    repeat


image curran_relaxed_eyes:
    "images/curran/faces/110281_01_parts_c016.png"
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
    "images/curran/faces/110281_01_parts_c017.png"
    0.05
    repeat

image curran_focused2_eyes:
    "images/curran/faces/110281_01_parts_c018.png"
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
    "images/curran/faces/110281_01_parts_c019.png"
    0.05
    repeat

image curran_sweat_eyes:
    "images/curran/faces/110281_01_parts_c020.png"
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
    "images/curran/faces/110281_01_parts_c021.png"
    0.05
    repeat

image curran_blush_eyes:
    "images/curran/faces/110281_01_parts_c022.png"
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
    "images/curran/faces/110281_01_parts_c023.png"
    0.05
    repeat

image curran_askance_eyes:
    "images/curran/faces/110281_01_parts_c032.png"
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
    "images/curran/faces/110281_01_parts_c033.png"
    0.05
    repeat

image curran_focused3_eyes:
    "images/curran/faces/110281_01_parts_c034.png"
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
    "images/curran/faces/110281_01_parts_c005.png"
    0.05
    repeat

image curran_angry_eyes:
    "images/curran/faces/110281_01_parts_c035.png"
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
    "images/curran/faces/110281_01_parts_c036.png"
    0.05
    repeat



# MOUTH animations start here.

image curran_frown1_nottalking = "images/curran/mouths/110281_01_parts_c008.png"

image curran_frown1_talking:
    "images/curran/mouths/110281_01_parts_c008.png"
    0.15
    "images/curran/mouths/110281_01_parts_c009.png"
    0.15
    repeat

image curran_frown1 = WhileSpeaking("cur", "curran_frown1_talking", "curran_frown1_nottalking")


image curran_frown2_nottalking = "images/curran/mouths/110281_01_parts_c010.png"

image curran_frown2_talking:
    "images/curran/mouths/110281_01_parts_c010.png"
    0.15
    "images/curran/mouths/110281_01_parts_c011.png"
    0.15
    repeat

image curran_frown2 = WhileSpeaking("cur", "curran_frown2_talking", "curran_frown2_nottalking")


image curran_frown3_nottalking = "images/curran/mouths/110281_01_parts_c012.png"

image curran_frown3_talking:
    "images/curran/mouths/110281_01_parts_c012.png"
    0.15
    "images/curran/mouths/110281_01_parts_c013.png"
    0.15
    repeat

image curran_frown3 = WhileSpeaking("cur", "curran_frown3_talking", "curran_frown3_nottalking")


image curran_grimace1_nottalking = "images/curran/mouths/110281_01_parts_c015.png"

image curran_grimace1_talking:
    "images/curran/mouths/110281_01_parts_c015.png"
    0.15
    "images/curran/mouths/110281_01_parts_c014.png"
    0.15
    repeat

image curran_grimace1 = WhileSpeaking("cur", "curran_grimace1_talking", "curran_grimace1_nottalking")


image curran_smile1_nottalking = "images/curran/mouths/110281_01_parts_c024.png"

image curran_smile1_talking:
    "images/curran/mouths/110281_01_parts_c024.png"
    0.15
    "images/curran/mouths/110281_01_parts_c025.png"
    0.15
    repeat

image curran_smile1 = WhileSpeaking("cur", "curran_smile1_talking", "curran_smile1_nottalking")


image curran_grimace2_nottalking = "images/curran/mouths/110281_01_parts_c026.png"

image curran_grimace2_talking:
    "images/curran/mouths/110281_01_parts_c026.png"
    0.15
    "images/curran/mouths/110281_01_parts_c027.png"
    0.15
    repeat

image curran_grimace2 = WhileSpeaking("cur", "curran_grimace2_talking", "curran_grimace2_nottalking")


image curran_frown4_nottalking = "images/curran/mouths/110281_01_parts_c028.png"

image curran_frown4_talking:
    "images/curran/mouths/110281_01_parts_c028.png"
    0.15
    "images/curran/mouths/110281_01_parts_c029.png"
    0.15
    repeat

image curran_frown4 = WhileSpeaking("cur", "curran_frown4_talking", "curran_frown4_nottalking")


image curran_frown5_nottalking = "images/curran/mouths/110281_01_parts_c030.png"

image curran_frown5_talking:
    "images/curran/mouths/110281_01_parts_c030.png"
    0.15
    "images/curran/mouths/110281_01_parts_c031.png"
    0.15
    repeat

image curran_frown5 = WhileSpeaking("cur", "curran_frown5_talking", "curran_frown5_nottalking")


image curran_frown6_nottalking = "images/curran/mouths/110281_01_parts_c037.png"

image curran_frown6_talking:
    "images/curran/mouths/110281_01_parts_c037.png"
    0.15
    "images/curran/mouths/110281_01_parts_c038.png"
    0.15
    repeat

image curran_frown6 = WhileSpeaking("cur", "curran_frown6_talking", "curran_frown6_nottalking")


image curran_frown7_nottalking = "images/curran/mouths/110281_01_parts_c039.png"

image curran_frown7_talking:
    "images/curran/mouths/110281_01_parts_c039.png"
    0.15
    "images/curran/mouths/110281_01_parts_c040.png"
    0.15
    repeat

image curran_frown7 = WhileSpeaking("cur", "curran_frown7_talking", "curran_frown7_nottalking")


image curran_frown8_nottalking = "images/curran/mouths/110281_01_parts_c041.png"

image curran_frown8_talking:
    "images/curran/mouths/110281_01_parts_c041.png"
    0.15
    "images/curran/mouths/110281_01_parts_c042.png"
    0.15
    repeat

image curran_frown8 = WhileSpeaking("cur", "curran_frown8_talking", "curran_frown8_nottalking")


image curran_frown9_nottalking = "images/curran/mouths/110281_01_parts_c043.png"

image curran_frown9_talking:
    "images/curran/mouths/110281_01_parts_c043.png"
    0.15
    "images/curran/mouths/110281_01_parts_c044.png"
    0.15
    repeat

image curran_frown9 = WhileSpeaking("cur", "curran_frown9_talking", "curran_frown9_nottalking")












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

label curran_character_procedures:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image pub = "images/backgrounds/Sty_bg_0026_100_00.png"
    scene pub at middle

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    show curran with dissolve

    cur "Oh, hello.  Fancy seeing somebody like you here."

    cur "...You say there's a shapeshifting fiend that takes on people's appearances?"
    cur "That does sound serious.  ...Why are you looking at me like that?"
    cur "...Do you REALLY need me to make a bunch of faces?  How is that supposed to help?"
    cur "...(sigh) FINE, if you're really serious about it..."

    show curran neutral
    cur "This is my neutral face."

    show curran neutral2
    cur "And here's another one (neutral2)."

    show curran closed_neutral
    cur "If I close my eyes, then this is a different neutral face (closed_neutral)."

    show curran focused
    cur "This is my focused face."

    show curran focused2
    cur "And this is a different focused face (focused2)."

    show curran focused3
    cur "And I think I can even look focused in a third way (focused3)."

    show curran sweat
    cur "Look, can we wrap this up?  I'm starting to sweat here."

    show curran blush
    cur "Y-You say I'm blushing (blush)??  Well, it's your fault for making me do this..."

    show curran askance
    cur "Thank goodness that's over with.  I'm just gonna avoid eye contact with you now if you don't mind (askance)."

    show curran angry
    cur "Wh-what do you MEAN, 'you want to examine my mouth too'?  Are you TRYING to make me angry?"

    show curran closed_neutral
    cur "(Sigh) ...FINE...  But you'd better explain the full situation to me afterwards!"

    show curran neutral
    show curran frown1
    cur "This is a frown (frown1).  It's the natural response when someone asks you to do something this stupid."

    show curran frown2
    cur "Here's another frown (frown2).  Wow, it's so original and exciting."

    show curran frown3
    cur "Here's another frown (frown3).  Are you getting the pattern here, partner?"

    show curran frown4
    cur "I've got another expression for you.  It's... surprise! ...another frown (frown4)."

    show curran frown5
    cur "Alright, I've run out of commentary, so... another frown (frown5).  Amazing, isn't it?"

    show curran frown6
    cur "Sixth frown (frown6) coming up right now.  I bet you're really glad you asked me to do this now, aren't you?"

    show curran frown7
    cur "Geez, you're still not satisfied?  Here's a seventh frown (frown7)."

    show curran frown8
    cur "...And an eigth one (frown8)!!!  Do I have to keep going?? I'm really getting annoyed here!!"

    show curran frown9
    cur "You're still not satisfied?  This is the only frown I have left (frown9)."

    show curran grimace1
    cur "Urgh, I can't believe you weren't happy until I made nine different frowns.  Having to interact with you is definitely worth a grimace (grimace1)..."

    show curran grimace2
    cur "...You want me to cycle through these too?  Fine, another grimace for the stickler (grimace2)."

    show curran smile1
    cur "Wait, we're done?  ...Whew.  In that case, I'll treat you to one of my rare smiles (smile1)."

    show curran sweat
    cur "...What?"

    show curran frown5
    cur "..."

    show curran angry
    show curran frown8
    cur "YOU MADE IT UP?!?  YOU JUST WANTED TO SEE ME MAKE STUPID FACES?!?"

    show curran blush
    cur "You're such an arrogant PRICK!  I'll NEVER forgive you for this!!!!"
    cur "And NO, you can't just bribe me with an interesting case to..."

    show curran focused
    show curran frown7
    cur "...Oh.  That actually IS interesting..."

    # This goes back to script

    jump testfiles
