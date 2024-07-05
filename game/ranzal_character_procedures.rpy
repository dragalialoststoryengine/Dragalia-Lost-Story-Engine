    # Ranzal Character Procedures File

    # Paste this file into a story if you want to use Ranzal.  These procedures animate Ranzal as a speaker.

define ranz = Character("Ranzal", callback=speaker("ranz"))

    # This program assumes that the following folders exist:
    #     -"images/ranzal"
    #     -"images/ranzal/faces"
    #     -"images/ranzal/mouths"

    # Ranzal dynamically blinks and, while speaking, also moves his mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Ranzal appear*:
    #  -->  show ranzal with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Ranzal's eyes*:
    #  -->  show ranzal [keyword]
    #  List of eye keywords:
    #     -->  neutral (the default option), closed_neutral, angry, flinch,
    #          focused, relaxed, shocked, squint, surprised, wink

    # *Changing Ranzal's mouth*:
    #  -->  show ranzal [keyword]
    #  List of mouth keywords:
    #     -->  smile1 (the default option), smile2, frown1, frown2,
    #           grimace1, grimace2, grin1, mutter1, shout1, closed_frown1

    # *Writing dialogue for Ranzal*:
    #  --> ranz "[Ranzal's line here]"

    # *Making Ranzal disappear*:
    #  --> hide ranzal with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage ranzal:

    always "images/ranzal/ranzal_body.png"

    group face:

        # 423/1024, 164/1024:
        pos (0.4130859, 0.160156)

        attribute neutral default:
            "ranzal_neutral_eyes"

        attribute closed_neutral:
            "images/ranzal/faces/100003_01_parts_c001.png"

        attribute focused:
            "ranzal_focused_eyes"

        attribute relaxed:
            "ranzal_relaxed_eyes"

        attribute flinch:
            "ranzal_flinch_eyes"

        attribute surprised:
            "ranzal_surprised_eyes"

        attribute wink:
            "ranzal_wink_eyes"

        attribute squint:
            "ranzal_squint_eyes"

        attribute angry:
            "ranzal_angry_eyes"

        attribute shocked:
            "ranzal_shocked_eyes"


    group mouth:

        pos (0.4130859, 0.160156)

        attribute smile1 default:
            "ranzal_smile1"

        attribute frown1:
            "ranzal_frown1"

        attribute closed_frown1:
            "images/ranzal/mouths/100003_01_parts_c011.png"

        attribute smile2:
            "ranzal_smile2"

        attribute grimace1:
            "ranzal_grimace1"

        attribute frown2:
            "ranzal_frown2"

        attribute grin1:
            "ranzal_grin1"

        attribute grimace2:
            "ranzal_grimace2"

        attribute mutter1:
            "ranzal_mutter1"

        attribute shout1:
            "ranzal_shout1"



## EYE animations start here.

image ranzal_neutral_eyes:
    "images/ranzal/faces/100003_01_parts_c000.png"
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
    "images/ranzal/faces/100003_01_parts_c001.png"
    0.05
    repeat


# 002 and 003 are duplicates of 001.  Deleted.


# 004 / 005 are the same as 000 / 001.  Deleted.


image ranzal_focused_eyes:
    "images/ranzal/faces/100003_01_parts_c006.png"
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
    "images/ranzal/faces/100003_01_parts_c007.png"
    0.05
    repeat

image ranzal_relaxed_eyes:
    "images/ranzal/faces/100003_01_parts_c013.png"
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
    "images/ranzal/faces/100003_01_parts_c014.png"
    0.05
    repeat

image ranzal_flinch_eyes:
    "images/ranzal/faces/100003_01_parts_c015.png"
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
    "images/ranzal/faces/100003_01_parts_c016.png"
    0.05
    repeat

# 035 is the same as 000

image ranzal_surprised_eyes:
    "images/ranzal/faces/100003_01_parts_c017.png"
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
    "images/ranzal/faces/100003_01_parts_c018.png"
    0.05
    repeat

image ranzal_wink_eyes:
    "images/ranzal/faces/100003_01_parts_c019.png"
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
    "images/ranzal/faces/100003_01_parts_c020.png"
    0.05
    repeat

image ranzal_squint_eyes:
    "images/ranzal/faces/100003_01_parts_c029.png"
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
    "images/ranzal/faces/100003_01_parts_c030.png"
    0.05
    repeat

image ranzal_angry_eyes:
    "images/ranzal/faces/100003_01_parts_c031.png"
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
    "images/ranzal/faces/100003_01_parts_c032.png"
    0.05
    repeat

image ranzal_shocked_eyes:
    "images/ranzal/faces/100003_01_parts_c033.png"
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
    "images/ranzal/faces/100003_01_parts_c034.png"
    0.05
    repeat





# MOUTH animations start here.

image ranzal_smile1_nottalking = "images/ranzal/mouths/100003_01_parts_c008.png"

image ranzal_smile1_talking:
    "images/ranzal/mouths/100003_01_parts_c009.png"
    0.15
    "images/ranzal/mouths/100003_01_parts_c008.png"
    0.15
    repeat

image ranzal_smile1 = WhileSpeaking("ranz", "ranzal_smile1_talking", "ranzal_smile1_nottalking")


# 010 is the same as 008; deleted


image ranzal_frown1_nottalking = "images/ranzal/mouths/100003_01_parts_c011.png"

image ranzal_frown1_talking:
    "images/ranzal/mouths/100003_01_parts_c012.png"
    0.15
    "images/ranzal/mouths/100003_01_parts_c011.png"
    0.15
    repeat

image ranzal_frown1 = WhileSpeaking("ranz", "ranzal_frown1_talking", "ranzal_frown1_nottalking")


image ranzal_smile2_nottalking = "images/ranzal/mouths/100003_01_parts_c021.png"

image ranzal_smile2_talking:
    "images/ranzal/mouths/100003_01_parts_c022.png"
    0.15
    "images/ranzal/mouths/100003_01_parts_c021.png"
    0.15
    repeat

image ranzal_smile2 = WhileSpeaking("ranz", "ranzal_smile2_talking", "ranzal_smile2_nottalking")


image ranzal_grimace1_nottalking = "images/ranzal/mouths/100003_01_parts_c023.png"

image ranzal_grimace1_talking:
    "images/ranzal/mouths/100003_01_parts_c024.png"
    0.15
    "images/ranzal/mouths/100003_01_parts_c023.png"
    0.15
    repeat

image ranzal_grimace1 = WhileSpeaking("ranz", "ranzal_grimace1_talking", "ranzal_grimace1_nottalking")


image ranzal_frown2_nottalking = "images/ranzal/mouths/100003_01_parts_c025.png"

image ranzal_frown2_talking:
    "images/ranzal/mouths/100003_01_parts_c026.png"
    0.15
    "images/ranzal/mouths/100003_01_parts_c025.png"
    0.15
    repeat

image ranzal_frown2 = WhileSpeaking("ranz", "ranzal_frown2_talking", "ranzal_frown2_nottalking")


image ranzal_grin1_nottalking = "images/ranzal/mouths/100003_01_parts_c027.png"

image ranzal_grin1_talking:
    "images/ranzal/mouths/100003_01_parts_c028.png"
    0.15
    "images/ranzal/mouths/100003_01_parts_c027.png"
    0.15
    repeat

image ranzal_grin1 = WhileSpeaking("ranz", "ranzal_grin1_talking", "ranzal_grin1_nottalking")


image ranzal_grimace2_nottalking = "images/ranzal/mouths/100003_01_parts_c036.png"

image ranzal_grimace2_talking:
    "images/ranzal/mouths/100003_01_parts_c037.png"
    0.15
    "images/ranzal/mouths/100003_01_parts_c036.png"
    0.15
    repeat

image ranzal_grimace2 = WhileSpeaking("ranz", "ranzal_grimace2_talking", "ranzal_grimace2_nottalking")


image ranzal_mutter1_nottalking = "images/ranzal/mouths/100003_01_parts_c038.png"

image ranzal_mutter1_talking:
    "images/ranzal/mouths/100003_01_parts_c039.png"
    0.15
    "images/ranzal/mouths/100003_01_parts_c038.png"
    0.15
    repeat

image ranzal_mutter1 = WhileSpeaking("ranz", "ranzal_mutter1_talking", "ranzal_mutter1_nottalking")


image ranzal_shout1_nottalking = "images/ranzal/mouths/100003_01_parts_c040.png"

image ranzal_shout1_talking:
    "images/ranzal/mouths/100003_01_parts_c041.png"
    0.15
    "images/ranzal/mouths/100003_01_parts_c040.png"
    0.15
    repeat

image ranzal_shout1 = WhileSpeaking("ranz", "ranzal_shout1_talking", "ranzal_shout1_nottalking")


# 042 / 043 are the same as 008 / 009; deleted






# The test file script starts here.

label ranzal_character_procedures:

    image wasteland_sunset = "images/backgrounds/Sty_bg_0019_200_00.png"
    scene wasteland_sunset with fade

    show ranzal with dissolve
    ranz "Heh heh, I'm beat!  Beatin' up all these fiends for the village sure makes me feel like I'm gettin' back to my merc roots."

    show ranzal neutral smile1
    ranz "(neutral smile1) Well, in the mercenary spirit, what say we make camp here for the night?  Sun's gettin' pretty low, and there's a spring over here for water."

    show ranzal closed_neutral smile2
    ranz "(closed_neutral smile2) Hm... you know, Boss, this feels like back when we first met.  Campin' out under the stars, travelling through the Mistholt..."

    show ranzal surprised mutter1
    ranz "(surprised mutter1) ...Huh?  You remember things differently?  How so?"

    show ranzal flinch grimace1
    ranz "(flinch grimace1) ...O-Oh yeah, I kinda forgot that we kinda duked it out axe-to-sword...  Guess I was engaging in a little revisionist history..."

    show ranzal angry grimace2
    ranz "(angry grimace2) --Wait, whaddya mean, \"you won?\"  You can't seriously think that was a real fight?!  I was definitely holding back!!!"

    show ranzal focused frown1
    ranz "(focused frown1) Yeah, that's right, I, er, was just testin' yer resolve and called it off when I saw enough!"

    show ranzal shocked shout1
    ranz "(shocked shout1) S-Stop laughing!  I-I ain't kiddin'!  I could totally take ya down anytime!  Just bring it on and I'll show you the REAL ol' Ranzal Smackdown!"

    show ranzal closed_neutral grin1
    ranz "(grin1) ...snk..."
    ranz "...BAHAHAHAHA!!!  Ya know, I don't think you and I've actually butted heads much at all recently.  Now THIS is nostalgic for real!"

    show ranzal relaxed frown2
    ranz "(relaxed frown1) You know, Boss, I've been really focused lately on watchin' yer back and stuff.  Ya got a lot on your plate.  But I always forget, you're not a kid anymore."

    show ranzal squint smile1
    ranz "(squint) You're a real pal.  More like... one of my merc buddies from way back when.  But it's also... better, because ya aren't just in it fer the cash.  Ya care about people."

    show ranzal wink grin1
    ranz "(wink) But that DOES remind me... I used'ta spar a TON with my merc buddies.  When we get back to the castle, you'd better put yer money where yer mouth is, 'cause Ranzal's gonna be yer next opponent!"

    show ranzal flinch mutter1
    ranz "But... uh... shapeshifting's off-limits, alright?  ...Skill can only go SO far when yer opponent weighs as much as a freakin' HOUSE..."

    hide ranzal with dissolve


    # This goes back to script

    jump testfiles
