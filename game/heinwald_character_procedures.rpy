
    # Heinwald Character Procedures File

    # Paste this file into a story if you want to use Heinwald.  These procedures animate Heinwald as a speaker.
    # You'll also need to paste THIS line into your actual script above the script label whenever you're using Heinwald:

define hein = Character("Heinwald", callback=speaker("hein"))

    # This program assumes that the following folders exist:
    #     -"images/heinwald"
    #     -"images/heinwald/faces"
    #     -"images/heinwald/mouths"

    # Heinwald dynamically blinks and, while speaking, also moves her mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Heinwald appear*:
    #  -->  show heinwald with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Heinwald's eyes*:
    #  -->  show heinwald [keyword]
    #  List of eye keywords:
    #     -->  focused (the default option), focused2, focused3, puzzled, puzzled2, annoyed
    #          surprised, surprised2, relaxed, sad, sad2, sad3

    # *Changing Heinwald's mouth*:
    #  -->  show heinwald [keyword]
    #  List of mouth keywords:
    #     -->  frown1 (the default option), frown2, frown3, frown4, frown5, smile1, smile2,
    #          grimace, grin

    # *Writing dialogue for Heinwald*:
    #  --> hein "[Heinwald's line here]"

    # *Making Heinwald disappear*:
    #  --> hide heinwald with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage heinwald:

    always "images/heinwald/heinwald_body.png"

    group face:

        # 438/1028, 180/1028:
        pos (0.42607, 0.1751)

        attribute focused default:
            "heinwald_focused_eyes"

        attribute puzzled:
            "heinwald_puzzled_eyes"

        attribute focused2:
            "heinwald_focused2_eyes"

        attribute annoyed:
            "heinwald_annoyed_eyes"

        attribute surprised:
            "heinwald_surprised_eyes"

        attribute relaxed:
            "heinwald_relaxed_eyes"

        attribute sad:
            "heinwald_sad_eyes"

        attribute surprised2:
            "heinwald_surprised2_eyes"

        attribute puzzled2:
            "heinwald_puzzled2_eyes"

        attribute focused3:
            "heinwald_focused3_eyes"

        attribute sad2:
            "heinwald_sad2_eyes"

        attribute sad3:
            "heinwald_sad3_eyes"


    group mouth:

        pos (0.42607, 0.1751)

        attribute frown1 default:
            "heinwald_frown1"

        attribute frown2:
            "heinwald_frown2"

        attribute smile1:
            "heinwald_smile1"

        attribute grimace:
            "heinwald_grimace"

        attribute frown3:
            "heinwald_frown3"

        attribute smile2:
            "heinwald_smile2"

        attribute frown4:
            "heinwald_frown4"

        attribute frown5:
            "heinwald_frown5"

        attribute grin:
            "heinwald_grin"



## EYE animations start here.

#note:  00, 02 and 28 are all the same.

image heinwald_focused_eyes:
    "images/heinwald/faces/110280_01_parts_c000.png"
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
    "images/heinwald/faces/110280_01_parts_c001.png"
    0.05
    repeat

# images/heinwald/faces/110280_01_parts_c002.png is the same as 01 so i won't do it twice.

image heinwald_puzzled_eyes:
    "images/heinwald/faces/110280_01_parts_c004.png"
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
    "images/heinwald/faces/110280_01_parts_c005.png"
    0.05
    repeat

image heinwald_focused2_eyes:
    "images/heinwald/faces/110280_01_parts_c010.png"
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
    "images/heinwald/faces/110280_01_parts_c011.png"
    0.05
    repeat


image heinwald_annoyed_eyes:
    "images/heinwald/faces/110280_01_parts_c012.png"
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
    "images/heinwald/faces/110280_01_parts_c013.png"
    0.05
    repeat

image heinwald_surprised_eyes:
    "images/heinwald/faces/110280_01_parts_c014.png"
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
    "images/heinwald/faces/110280_01_parts_c015.png"
    0.05
    repeat

image heinwald_relaxed_eyes:
    "images/heinwald/faces/110280_01_parts_c016.png"
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
    "images/heinwald/faces/110280_01_parts_c017.png"
    0.05
    repeat

image heinwald_sad_eyes:
    "images/heinwald/faces/110280_01_parts_c026.png"
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
    "images/heinwald/faces/110280_01_parts_c027.png"
    0.05
    repeat

image heinwald_surprised2_eyes:
    "images/heinwald/faces/110280_01_parts_c029.png"
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
    "images/heinwald/faces/110280_01_parts_c030.png"
    0.05
    repeat

image heinwald_puzzled2_eyes:
    "images/heinwald/faces/110280_01_parts_c031.png"
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
    "images/heinwald/faces/110280_01_parts_c032.png"
    0.05
    repeat

image heinwald_focused3_eyes:
    "images/heinwald/faces/110280_01_parts_c037.png"
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
    "images/heinwald/faces/110280_01_parts_c038.png"
    0.05
    repeat

image heinwald_sad2_eyes:
    "images/heinwald/faces/110280_01_parts_c039.png"
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
    "images/heinwald/faces/110280_01_parts_c040.png"
    0.05
    repeat

image heinwald_sad3_eyes:
    "images/heinwald/faces/110280_01_parts_c041.png"
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
    "images/heinwald/faces/110280_01_parts_c042.png"
    0.05
    repeat




# MOUTH animations start here.

image heinwald_frown1_nottalking = "images/heinwald/mouths/110280_01_parts_c006.png"

image heinwald_frown1_talking:
    "images/heinwald/mouths/110280_01_parts_c006.png"
    0.15
    "images/heinwald/mouths/110280_01_parts_c007.png"
    0.15
    repeat

image heinwald_frown1 = WhileSpeaking("hein", "heinwald_frown1_talking", "heinwald_frown1_nottalking")


image heinwald_frown2_nottalking = "images/heinwald/mouths/110280_01_parts_c008.png"

image heinwald_frown2_talking:
    "images/heinwald/mouths/110280_01_parts_c008.png"
    0.15
    "images/heinwald/mouths/110280_01_parts_c009.png"
    0.15
    repeat

image heinwald_frown2 = WhileSpeaking("hein", "heinwald_frown2_talking", "heinwald_frown2_nottalking")


image heinwald_smile1_nottalking = "images/heinwald/mouths/110280_01_parts_c018.png"

image heinwald_smile1_talking:
    "images/heinwald/mouths/110280_01_parts_c018.png"
    0.15
    "images/heinwald/mouths/110280_01_parts_c019.png"
    0.15
    repeat

image heinwald_smile1 = WhileSpeaking("hein", "heinwald_smile1_talking", "heinwald_smile1_nottalking")


image heinwald_grimace_nottalking = "images/heinwald/mouths/110280_01_parts_c021.png"

image heinwald_grimace_talking:
    "images/heinwald/mouths/110280_01_parts_c021.png"
    0.15
    "images/heinwald/mouths/110280_01_parts_c020.png"
    0.15
    repeat

image heinwald_grimace = WhileSpeaking("hein", "heinwald_grimace_talking", "heinwald_grimace_nottalking")


image heinwald_frown3_nottalking = "images/heinwald/mouths/110280_01_parts_c022.png"

image heinwald_frown3_talking:
    "images/heinwald/mouths/110280_01_parts_c022.png"
    0.15
    "images/heinwald/mouths/110280_01_parts_c023.png"
    0.15
    repeat

image heinwald_frown3 = WhileSpeaking("hein", "heinwald_frown3_talking", "heinwald_frown3_nottalking")


image heinwald_smile2_nottalking = "images/heinwald/mouths/110280_01_parts_c024.png"

image heinwald_smile2_talking:
    "images/heinwald/mouths/110280_01_parts_c024.png"
    0.15
    "images/heinwald/mouths/110280_01_parts_c025.png"
    0.15
    repeat

image heinwald_smile2 = WhileSpeaking("hein", "heinwald_smile2_talking", "heinwald_smile2_nottalking")


image heinwald_frown4_nottalking = "images/heinwald/mouths/110280_01_parts_c033.png"

image heinwald_frown4_talking:
    "images/heinwald/mouths/110280_01_parts_c033.png"
    0.15
    "images/heinwald/mouths/110280_01_parts_c034.png"
    0.15
    repeat

image heinwald_frown4 = WhileSpeaking("hein", "heinwald_frown4_talking", "heinwald_frown4_nottalking")


image heinwald_frown5_nottalking = "images/heinwald/mouths/110280_01_parts_c035.png"

image heinwald_frown5_talking:
    "images/heinwald/mouths/110280_01_parts_c035.png"
    0.15
    "images/heinwald/mouths/110280_01_parts_c036.png"
    0.15
    repeat

image heinwald_frown5 = WhileSpeaking("hein", "heinwald_frown5_talking", "heinwald_frown5_nottalking")


image heinwald_grin_nottalking = "images/heinwald/mouths/110280_01_parts_c044.png"

image heinwald_grin_talking:
    "images/heinwald/mouths/110280_01_parts_c044.png"
    0.15
    "images/heinwald/mouths/110280_01_parts_c043.png"
    0.15
    repeat

image heinwald_grin = WhileSpeaking("hein", "heinwald_grin_talking", "heinwald_grin_nottalking")












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

label heinwald_character_procedures:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image forbiddenlibrary = "images/backgrounds/Sty_bg_0042_100_00.png"
    scene forbiddenlibrary at middle

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    show heinwald with dissolve

    hein "Ah, you've come to visit me.  I was just reading about the most fascinating ritual..."
    hein "Oh, but this is fortuitous timing.  There's something that's been bothering me that I think you could help with."
    hein "I've been told lately that I'm a difficult person to read... emotionally speaking."
    hein "I consider this somewhat of a feature, but I will admit that there are situations where being able to convey emotion would be logistically convenient."
    hein "I want to make a number of facial expressions; would you mind giving me feedback?"

    show heinwald focused
    hein "Very well.  In that case I will begin with my usual 'focused' expression."

    show heinwald focused2
    hein "But I have other facial expression with equal focus (focused2)."

    show heinwald focused3
    hein "And I can look focused in a different manner as well (focused3)."

    show heinwald puzzled
    hein "If I were puzzled about a particular piece of information, I might look something like this."

    show heinwald puzzled2
    hein "And this is a different puzzled expression (puzzled2)."

    show heinwald annoyed
    hein "Now, here's an important one:  I want to convey that I'm annoyed.  Is this an effective way to do so?"

    show heinwald surprised
    hein "Now, this is more of a 'surprised' look, I suppose?"

    show heinwald surprised2
    hein "And here is a slightly different surprised face (surprised2)."

    show heinwald relaxed
    hein "This is perhaps a face I would wear if I were relaxed."

    show heinwald sad
    hein "Here's another appropriate one.  I want to convey when I'm sad... or at least appear that way for sympathetic reasons.  Is this effective?"

    show heinwald sad2
    hein "If that one doesn't suit me, then maybe this one (sad2)?"

    show heinwald sad3
    hein "And... what about this one (sad3)?  Or is this more of a hopeless look?"

    show heinwald focused
    hein "Very well.  Now, I'd like to change up my mouth a little.  Would you bear with me for a few more moments?"

    show heinwald frown1
    hein "This is a frown (frown1) that I usually wear, but there are others."

    show heinwald frown2
    hein "This is a different but similar frown (frown2)."

    show heinwald frown3
    hein "This is a slightly more noticeable frown (frown3).  When I'm projecting more, perhaps."

    show heinwald frown4
    hein "This frown (frown4) is larger and is intended for shouting, for instance!"

    show heinwald frown5
    hein "And this frown (frown5) is more in the style of the first two."

    show heinwald smile1
    hein "Now I'm going to try to smile (smile1).  People say this is disarming for me, but I don't intend to be an unpleasant person."

    show heinwald smile2
    hein "If this is uncomfortable, maybe this smile (smile2) is better?  I think it's a little more understated."

    show heinwald grimace
    hein "Very well.  In this case, here's a grimace to show my displeasure."

    show heinwald grin
    hein "And a grin, to convey my confidence.  I'm hoping this is somewhat intimidating, so I can deter my foes with my logic."

    show heinwald frown1
    hein "Perfect.  I appreciate your feedback; I'll have to practice more at being expressive, I suppose.  But this was already helpful."

    hein "Well... I'm done with what I needed you for, and I want to get back to reading, so... you should leave now."


    # This goes back to script

    jump testfiles
