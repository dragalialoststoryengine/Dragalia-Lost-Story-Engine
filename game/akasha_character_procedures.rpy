transform fly_offscreeen_left:

    linear 2.0 xpos -1024

init python:

    # This is set to the name of the character that is speaking, or
    # None if no character is currently speaking.
    speaking = None

    # This returns speaking if the character is speaking, and done if the
    # character is not.
    def while_speaking(name, speak_d, done_d, st, at):
        if speaking == name:
            return speak_d, .1
        else:
            return done_d, None

    # Curried form of the above.
    curried_while_speaking = renpy.curry(while_speaking)

    # Displays speaking when the named character is speaking, and done otherwise.
    def WhileSpeaking(name, speaking_d, done_d=Null()):
        return DynamicDisplayable(curried_while_speaking(name, speaking_d, done_d))

    # This callback maintains the speaking variable.
    def speaker_callback(name, event, **kwargs):
        global speaking

        if event == "show":
            speaking = name
        elif event == "slow_done":
            speaking = None
        elif event == "end":
            speaking = None

    # Curried form of the same.
    speaker = renpy.curry(speaker_callback)
    # Akasha Character Procedures File

    # Paste this file into a story if you want to use Akasha.  These procedures animate Akasha as a speaker.

define aka = Character("Akasha", callback=speaker("aka"))

    # This program assumes that the following folders exist:
    #     -"images/akasha"
    #     -"images/akasha/faces"
    #     -"images/akasha/mouths"

    # Akasha dynamically blinks and, while speaking, also moves her mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Akasha appear*:
    #  -->  show akasha with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Akasha's eyes*:
    #  -->  show akasha [keyword]
    #  List of eye keywords:
    #     -->  relaxed (the default option), relaxed2, relaxed3, sad, sad2,
    #          surprised, surprised2, blushing, annoyed, annoyed2

    # *Changing Akasha's mouth*:
    #  -->  show akasha [keyword]
    #  List of mouth keywords:
    #     -->  grin1 (the default option), grin2, grin3, grin4, smile1, smile2, smile3,
    #          grimace1, grimace2, frown1

    # *Writing dialogue for Akasha*:
    #  --> aka "[Akasha's line here]"

    # *Making Akasha disappear*:
    #  --> hide akasha with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage akasha:

    always "images/akasha/akasha_body.png"

    group face:

        # 449/1028, 222/1028:
        pos (0.43677, 0.21595)

        attribute relaxed default:
            "akasha_relaxed_eyes"

        attribute relaxed2:
            "akasha_relaxed2_eyes"

        attribute relaxed3:
            "akasha_relaxed3_eyes"

        attribute sad:
            "akasha_sad_eyes"

        attribute surprised:
            "akasha_surprised_eyes"

        attribute blushing:
            "akasha_blushing_eyes"

        attribute sad2:
            "akasha_sad2_eyes"

        attribute surprised2:
            "akasha_surprised2_eyes"

        attribute annoyed:
            "akasha_annoyed_eyes"

        attribute annoyed2:
            "akasha_annoyed2_eyes"


    group mouth:

        pos (0.43677, 0.21595)

        attribute grin1 default:
            "akasha_grin1"

        attribute grin2:
            "akasha_grin2"

        attribute smile1:
            "akasha_smile1"

        attribute smile2:
            "akasha_smile2"

        attribute grin3:
            "akasha_grin3"

        attribute grin4:
            "akasha_grin4"

        attribute grimace1:
            "akasha_grimace1"

        attribute smile3:
            "akasha_smile3"

        attribute frown1:
            "akasha_frown1"

        attribute grimace2:
            "akasha_grimace2"



## EYE animations start here.

image akasha_relaxed_eyes:
    "images/akasha/faces/110341_01_parts_c000.png"
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
    "images/akasha/faces/110341_01_parts_c001.png"
    0.05
    repeat

image akasha_relaxed2_eyes:
    "images/akasha/faces/110341_01_parts_c002.png"
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
    "images/akasha/faces/110341_01_parts_c003.png"
    0.05
    repeat

image akasha_relaxed3_eyes:
    "images/akasha/faces/110341_01_parts_c009.png"
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
    "images/akasha/faces/110341_01_parts_c010.png"
    0.05
    repeat

image akasha_sad_eyes:
    "images/akasha/faces/110341_01_parts_c011.png"
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
    "images/akasha/faces/110341_01_parts_c012.png"
    0.05
    repeat

image akasha_surprised_eyes:
    "images/akasha/faces/110341_01_parts_c013.png"
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
    "images/akasha/faces/110341_01_parts_c014.png"
    0.05
    repeat

image akasha_blushing_eyes:
    "images/akasha/faces/110341_01_parts_c015.png"
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
    "images/akasha/faces/110341_01_parts_c016.png"
    0.05
    repeat

image akasha_sad2_eyes:
    "images/akasha/faces/110341_01_parts_c025.png"
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
    "images/akasha/faces/110341_01_parts_c026.png"
    0.05
    repeat

image akasha_surprised2_eyes:
    "images/akasha/faces/110341_01_parts_c027.png"
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
    "images/akasha/faces/110341_01_parts_c028.png"
    0.05
    repeat

image akasha_annoyed_eyes:
    "images/akasha/faces/110341_01_parts_c035.png"
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
    "images/akasha/faces/110341_01_parts_c036.png"
    0.05
    repeat

image akasha_annoyed2_eyes:
    "images/akasha/faces/110341_01_parts_c037.png"
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
    "images/akasha/faces/110341_01_parts_c038.png"
    0.05
    repeat



# MOUTH animations start here.

image akasha_grin1_nottalking = "images/akasha/mouths/110341_01_parts_c005.png"

image akasha_grin1_talking:
    "images/akasha/mouths/110341_01_parts_c005.png"
    0.15
    "images/akasha/mouths/110341_01_parts_c004.png"
    0.15
    repeat

image akasha_grin1 = WhileSpeaking("aka", "akasha_grin1_talking", "akasha_grin1_nottalking")


image akasha_grin2_nottalking = "images/akasha/mouths/110341_01_parts_c008.png"

image akasha_grin2_talking:
    "images/akasha/mouths/110341_01_parts_c008.png"
    0.15
    "images/akasha/mouths/110341_01_parts_c007.png"
    0.15
    repeat

image akasha_grin2 = WhileSpeaking("aka", "akasha_grin2_talking", "akasha_grin2_nottalking")


image akasha_smile1_nottalking = "images/akasha/mouths/110341_01_parts_c017.png"

image akasha_smile1_talking:
    "images/akasha/mouths/110341_01_parts_c017.png"
    0.15
    "images/akasha/mouths/110341_01_parts_c018.png"
    0.15
    repeat

image akasha_smile1 = WhileSpeaking("aka", "akasha_smile1_talking", "akasha_smile1_nottalking")


image akasha_smile2_nottalking = "images/akasha/mouths/110341_01_parts_c019.png"

image akasha_smile2_talking:
    "images/akasha/mouths/110341_01_parts_c019.png"
    0.15
    "images/akasha/mouths/110341_01_parts_c020.png"
    0.15
    repeat

image akasha_smile2 = WhileSpeaking("aka", "akasha_smile2_talking", "akasha_smile2_nottalking")


image akasha_grin3_nottalking = "images/akasha/mouths/110341_01_parts_c022.png"

image akasha_grin3_talking:
    "images/akasha/mouths/110341_01_parts_c022.png"
    0.15
    "images/akasha/mouths/110341_01_parts_c021.png"
    0.15
    repeat

image akasha_grin3 = WhileSpeaking("aka", "akasha_grin3_talking", "akasha_grin3_nottalking")


image akasha_grin4_nottalking = "images/akasha/mouths/110341_01_parts_c024.png"

image akasha_grin4_talking:
    "images/akasha/mouths/110341_01_parts_c024.png"
    0.15
    "images/akasha/mouths/110341_01_parts_c023.png"
    0.15
    repeat

image akasha_grin4 = WhileSpeaking("aka", "akasha_grin4_talking", "akasha_grin4_nottalking")


image akasha_grimace1_nottalking = "images/akasha/mouths/110341_01_parts_c030.png"

image akasha_grimace1_talking:
    "images/akasha/mouths/110341_01_parts_c030.png"
    0.15
    "images/akasha/mouths/110341_01_parts_c029.png"
    0.15
    repeat

image akasha_grimace1 = WhileSpeaking("aka", "akasha_grimace1_talking", "akasha_grimace1_nottalking")


image akasha_smile3_nottalking = "images/akasha/mouths/110341_01_parts_c031.png"

image akasha_smile3_talking:
    "images/akasha/mouths/110341_01_parts_c031.png"
    0.15
    "images/akasha/mouths/110341_01_parts_c032.png"
    0.15
    repeat

image akasha_smile3 = WhileSpeaking("aka", "akasha_smile3_talking", "akasha_smile3_nottalking")

#  Parts 33 and 34 are identical to 004 and 005, i.e. grin1.

image akasha_frown1_nottalking = "images/akasha/mouths/110341_01_parts_c039.png"

image akasha_frown1_talking:
    "images/akasha/mouths/110341_01_parts_c039.png"
    0.15
    "images/akasha/mouths/110341_01_parts_c040.png"
    0.15
    repeat

image akasha_frown1 = WhileSpeaking("aka", "akasha_frown1_talking", "akasha_frown1_nottalking")


image akasha_grimace2_nottalking = "images/akasha/mouths/110341_01_parts_c042.png"

image akasha_grimace2_talking:
    "images/akasha/mouths/110341_01_parts_c042.png"
    0.15
    "images/akasha/mouths/110341_01_parts_c041.png"
    0.15
    repeat

image akasha_grimace2 = WhileSpeaking("aka", "akasha_grimace2_talking", "akasha_grimace2_nottalking")




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

label akasha_character_procedures:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image forbiddenlibrary = "images/backgrounds/Sty_bg_0042_100_00.png"
    scene forbiddenlibrary at middle



    show akasha with dissolve

    aka "Ah, good evening to you.  I was merely perusing these tomes."
    aka "So many secrets here.  How tantalizing..."
    aka "To think that each of these was collected by the Ancient One before Alberius was even born..."
    aka "But I digress.  You came here to observe my ability to make facial expressions, have you not?"
    aka "...How do I know this, you ask?  Surely you must allow a lady to have some secrets, no?"
    aka "Rather, let us proceed with all haste so you may resume your business, and I... may resume mine."

    show akasha relaxed
    aka "As you can see, this is my default relaxed expression.  Quite enjoyable."

    show akasha relaxed2
    aka "This is a second relaxed (relaxed2) expression.  My eyes are a little wider in this one, no?"

    show akasha relaxed3
    aka "This is a third relaxed (relaxed3) expression.  Here my eyes are squinting more."

    show akasha sad
    aka "This is a sad expression.  I might wear it to express pity."

    show akasha sad2
    aka "That's just an act, you say?  It saddens me (sad2) for you to have to ask.  How tedious."

    show akasha surprised
    aka "Here is my surprised expression.  In addition to having wide eyes, my eyebrows are also higher."

    show akasha surprised2
    aka "But of course, I also have another surprised (surprised2) expression.  Here my irises are more contracted."

    show akasha blushing
    aka "In this expression, I am blushing.  It might be more accurate to say that it's flushed, but there are conventions to obey, of course."

    show akasha annoyed
    aka "This is an annoyed expression, of course..."

    show akasha annoyed2
    aka "...and this is a second one (annoyed2).  And that about wraps things up."

    show akasha relaxed
    aka "Worry not, I know that you also want to see me change my mouth."

    show akasha grin1
    aka "This is my standard grin (grin1).  I find it a pleasant demeanor."

    show akasha grin2
    aka "This is a second grin (grin2).  A bit wide and thin, don't you agree?"

    show akasha grin3
    aka "And now for a third one (grin3).  I like the subtlety of the upturned corners here."

    show akasha grin4
    aka "But I also have one last one (grin4) in my repertoire!  This one is similar to the third but the corners of my mouth are wider."

    show akasha smile1
    aka "Of course, I can smile without my teeth.  Do you find this one (smile1) pleasing to you?"

    show akasha smile2
    aka "This one (smile2) is a bit wider and the corners of my mouth are upturned."

    show akasha smile3
    aka "This one (smile3) is quite wide!!  I would use it to exclaim something in excitement!!!"

    show akasha grimace1
    aka "You find this unnerving?  How unfortunate--it brings a grimace (grimace1) to my face."

    show akasha grimace2
    aka "I feel rather nervous now (grimace2), and there's some sweat on my face.  How unladylike."

    show akasha frown1
    aka "This whole experimence has been more unpleasant than I anticipated.  Allow this frown (frown1) to express my innermost feelings."

    show akasha sad2
    aka "Are we done now?  I'd very much like to get back to my exploration now..."

    hide akasha with dissolve


    # This goes back to script

    jump testfiles
