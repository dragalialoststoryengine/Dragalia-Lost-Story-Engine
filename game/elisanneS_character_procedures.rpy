
    # Summer Elisanne Character Procedures File

    # Paste this file into a story if you want to use Summer Elisanne.  These procedures animate Summer Elisanne as a speaker.
    # You'll also need to paste THIS line into your actual script above the script label whenever you're using Summer Elisanne:

define selly = Character("Elisanne", callback=speaker("selly"))

    # This program assumes that the following folders exist:
    #     -"images/elisanne_summer"
    #     -"images/elisanne_summer/faces"
    #     -"images/elisanne_summer/mouths"

    # Summer Elisanne dynamically blinks and, while speaking, also moves her mouth along with the text scroll.

    # Note:  there are TWO IMAGES for selisanne:  "selisanne" (normal) and "selisanneSTR" (stretch).
    # The body parts are the same for each, but you need to use one or the other.
    # (I couldn't make it a 'body' component because selly's FACES are slightly different for the two poses.)

    # FUNCTIONS:

    # *Making Summer Elisanne appear*:
    #  -->  show selisanne [OR selisanneSTR] with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Summer Elisanne's eyes*:
    #  -->  show selisanne [OR selisanneSTR] [keyword]
    #  List of eye keywords:
    #     --> wink (default), angry, blush, flinch, focused, relaxed, sad,
    #         squint, surprised

    # *Changing Summer Elisanne's mouth*:
    #  -->  show selisanne [OR selisanneSTR] [keyword]
    #  List of mouth keywords:
    #     --> smile1 (default), smile2, frown1, frown2, frown3, frown4,
    #         pout1, shout1

    # *Writing dialogue for Summer Elisanne*:
    #  --> selly "[Elisanne's line here]"

    # *Making Summer Elisanne disappear*:
    #  --> hide selisanne [OR selisanneSTR] with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #

layeredimage selisanne:

    always "images/elisanne_summer/elisanne_summer_body.png"

    group face:

        # image is 1024 by 1024!!

        # 447/1024, 244/1024:
        #pos (0.43652, 0.23828) seems to be slightly off

        # 447.5/1024, 245/1024:
        pos (0.43701, 0.23925)

        attribute wink default:
            "selisanne_wink_eyes"

        attribute focused:
            "selisanne_focused_eyes"

        attribute squint:
            "selisanne_squint_eyes"

        attribute flinch:
            "selisanne_flinch_eyes"

        attribute surprised:
            "selisanne_surprised_eyes"

        attribute blush:
            "selisanne_blush_eyes"

        attribute closed_blush:
            "images/elisanne_summer/faces/100002_14_parts_c016.png"

        attribute sad:
            "selisanne_sad_eyes"

        attribute angry:
            "selisanne_angry_eyes"

        attribute relaxed:
            "selisanne_relaxed_eyes"


    group mouth:

        pos (0.43701, 0.23925)

        attribute smile1 default:
            "selisanne_smile1"

        attribute frown1:
            "selisanne_frown1"

        attribute smile2:
            "selisanne_smile2"

        attribute frown2:
            "selisanne_frown2"

        attribute frown3:
            "selisanne_frown3"

        attribute pout1:
            "selisanne_pout1"

        attribute frown4:
            "selisanne_frown4"

        attribute shout1:
            "selisanne_shout1"

layeredimage selisanneSTR:

    always "images/elisanne_summer/elisanne_summer_stretch_body_crop.png"

    group face:

        # orig before crop was 447/1028, 244/1028

        # now is 527 x 977

        # 188/1024, 197/1024:
        # pos (0.18359, 0.19238) but doesn't exactly line up

        # 189/1028, 198/1028:
        pos (0.18385, 0.19261)

        attribute wink default:
            "selisanne_stretch_wink_eyes"

        attribute focused:
            "selisanne_stretch_focused_eyes"

        attribute squint:
            "selisanne_stretch_squint_eyes"

        attribute flinch:
            "selisanne_stretch_flinch_eyes"

        attribute surprised:
            "selisanne_stretch_surprised_eyes"

        attribute blush:
            "selisanne_stretch_blush_eyes"

        attribute closed_blush:
            "images/elisanne_summer/faces_stretch/100002_07_parts_c015.png"

        attribute sad:
            "selisanne_stretch_sad_eyes"

        attribute angry:
            "selisanne_stretch_angry_eyes"

        attribute relaxed:
            "selisanne_stretch_relaxed_eyes"


    group mouth:

        pos (0.18385, 0.19261)

        attribute smile1 default:
            "selisanne_smile1"

        attribute frown1:
            "selisanne_frown1"

        attribute smile2:
            "selisanne_smile2"

        attribute frown2:
            "selisanne_frown2"

        attribute frown3:
            "selisanne_frown3"

        attribute pout1:
            "selisanne_pout1"

        attribute frown4:
            "selisanne_frown4"

        attribute shout1:
            "selisanne_shout1"




## EYE animations start here.

image selisanne_wink_eyes:
    "images/elisanne_summer/faces/100002_14_parts_c000.png"
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
    "images/elisanne_summer/faces/100002_14_parts_c001.png"
    0.05
    repeat

image selisanne_stretch_wink_eyes:
    "images/elisanne_summer/faces_stretch/100002_07_parts_c000.png"
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
    "images/elisanne_summer/faces_stretch/100002_07_parts_c001.png"
    0.05
    repeat


image selisanne_focused_eyes:
    "images/elisanne_summer/faces/100002_14_parts_c003.png"
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
    "images/elisanne_summer/faces/100002_14_parts_c004.png"
    0.05
    repeat

image selisanne_stretch_focused_eyes:
    "images/elisanne_summer/faces_stretch/100002_07_parts_c002.png"
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
    "images/elisanne_summer/faces_stretch/100002_07_parts_c003.png"
    0.05
    repeat



image selisanne_squint_eyes:
    "images/elisanne_summer/faces/100002_14_parts_c009.png"
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
    "images/elisanne_summer/faces/100002_14_parts_c0010.png"
    0.05
    repeat

image selisanne_stretch_squint_eyes:
    "images/elisanne_summer/faces_stretch/100002_07_parts_c008.png"
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
    "images/elisanne_summer/faces_stretch/100002_07_parts_c009.png"
    0.05
    repeat


image selisanne_flinch_eyes:
    "images/elisanne_summer/faces/100002_14_parts_c011.png"
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
    "images/elisanne_summer/faces/100002_14_parts_c012.png"
    0.05
    repeat

image selisanne_stretch_flinch_eyes:
    "images/elisanne_summer/faces_stretch/100002_07_parts_c010.png"
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
    "images/elisanne_summer/faces_stretch/100002_07_parts_c011.png"
    0.05
    repeat


image selisanne_surprised_eyes:
    "images/elisanne_summer/faces/100002_14_parts_c013.png"
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
    "images/elisanne_summer/faces/100002_14_parts_c014.png"
    0.05
    repeat

image selisanne_stretch_surprised_eyes:
    "images/elisanne_summer/faces_stretch/100002_07_parts_c012.png"
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
    "images/elisanne_summer/faces_stretch/100002_07_parts_c013.png"
    0.05
    repeat


image selisanne_blush_eyes:
    "images/elisanne_summer/faces/100002_14_parts_c015.png"
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
    "images/elisanne_summer/faces/100002_14_parts_c016.png"
    0.05
    repeat

image selisanne_stretch_blush_eyes:
    "images/elisanne_summer/faces_stretch/100002_07_parts_c014.png"
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
    "images/elisanne_summer/faces_stretch/100002_07_parts_c015.png"
    0.05
    repeat


image selisanne_sad_eyes:
    "images/elisanne_summer/faces/100002_14_parts_c025.png"
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
    "images/elisanne_summer/faces/100002_14_parts_c026.png"
    0.05
    repeat

image selisanne_stretch_sad_eyes:
    "images/elisanne_summer/faces_stretch/100002_07_parts_c024.png"
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
    "images/elisanne_summer/faces_stretch/100002_07_parts_c025.png"
    0.05
    repeat


image selisanne_angry_eyes:
    "images/elisanne_summer/faces/100002_14_parts_c027.png"
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
    "images/elisanne_summer/faces/100002_14_parts_c028.png"
    0.05
    repeat

image selisanne_stretch_angry_eyes:
    "images/elisanne_summer/faces_stretch/100002_07_parts_c026.png"
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
    "images/elisanne_summer/faces_stretch/100002_07_parts_c027.png"
    0.05
    repeat


image selisanne_relaxed_eyes:
    "images/elisanne_summer/faces/100002_14_parts_c029.png"
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
    "images/elisanne_summer/faces/100002_14_parts_c030.png"
    0.05
    repeat

image selisanne_stretch_relaxed_eyes:
    "images/elisanne_summer/faces_stretch/100002_07_parts_c028.png"
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
    "images/elisanne_summer/faces_stretch/100002_07_parts_c001.png"
    0.05
    repeat





# MOUTH animations start here.

image selisanne_smile1_nottalking = "images/elisanne_summer/mouths/100002_07_parts_c004.png"

image selisanne_smile1_talking:
    "images/elisanne_summer/mouths/100002_07_parts_c005.png"
    0.15
    "images/elisanne_summer/mouths/100002_07_parts_c004.png"
    0.15
    repeat

image selisanne_smile1 = WhileSpeaking("selly", "selisanne_smile1_talking", "selisanne_smile1_nottalking")


image selisanne_frown1_nottalking = "images/elisanne_summer/mouths/100002_07_parts_c006.png"

image selisanne_frown1_talking:
    "images/elisanne_summer/mouths/100002_07_parts_c007.png"
    0.15
    "images/elisanne_summer/mouths/100002_07_parts_c006.png"
    0.15
    repeat

image selisanne_frown1 = WhileSpeaking("selly", "selisanne_frown1_talking", "selisanne_frown1_nottalking")


image selisanne_smile2_nottalking = "images/elisanne_summer/mouths/100002_07_parts_c016.png"

image selisanne_smile2_talking:
    "images/elisanne_summer/mouths/100002_07_parts_c017.png"
    0.15
    "images/elisanne_summer/mouths/100002_07_parts_c016.png"
    0.15
    repeat

image selisanne_smile2 = WhileSpeaking("selly", "selisanne_smile2_talking", "selisanne_smile2_nottalking")


image selisanne_frown2_nottalking = "images/elisanne_summer/mouths/100002_07_parts_c018.png"

image selisanne_frown2_talking:
    "images/elisanne_summer/mouths/100002_07_parts_c019.png"
    0.15
    "images/elisanne_summer/mouths/100002_07_parts_c018.png"
    0.15
    repeat

image selisanne_frown2 = WhileSpeaking("selly", "selisanne_frown2_talking", "selisanne_frown2_nottalking")


image selisanne_frown3_nottalking = "images/elisanne_summer/mouths/100002_07_parts_c020.png"

image selisanne_frown3_talking:
    "images/elisanne_summer/mouths/100002_07_parts_c021.png"
    0.15
    "images/elisanne_summer/mouths/100002_07_parts_c020.png"
    0.15
    repeat

image selisanne_frown3 = WhileSpeaking("selly", "selisanne_frown3_talking", "selisanne_frown3_nottalking")


image selisanne_pout1_nottalking = "images/elisanne_summer/mouths/100002_07_parts_c022.png"

image selisanne_pout1_talking:
    "images/elisanne_summer/mouths/100002_07_parts_c023.png"
    0.15
    "images/elisanne_summer/mouths/100002_07_parts_c022.png"
    0.15
    repeat

image selisanne_pout1 = WhileSpeaking("selly", "selisanne_pout1_talking", "selisanne_pout1_nottalking")


image selisanne_frown4_nottalking = "images/elisanne_summer/mouths/100002_07_parts_c029.png"

image selisanne_frown4_talking:
    "images/elisanne_summer/mouths/100002_07_parts_c030.png"
    0.15
    "images/elisanne_summer/mouths/100002_07_parts_c029.png"
    0.15
    repeat

image selisanne_frown4 = WhileSpeaking("selly", "selisanne_frown4_talking", "selisanne_frown4_nottalking")


# 031/032 is the same as 001/002


image selisanne_shout1_nottalking = "images/elisanne_summer/mouths/100002_07_parts_c033.png"

image selisanne_shout1_talking:
    "images/elisanne_summer/mouths/100002_07_parts_c034.png"
    0.15
    "images/elisanne_summer/mouths/100002_07_parts_c033.png"
    0.15
    repeat

image selisanne_shout1 = WhileSpeaking("selly", "selisanne_shout1_talking", "selisanne_shout1_nottalking")



# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



# corner of selly stretch goes from 248, 23 at exact middle to 259, 47
# middle moves by (259-248)/1028 = 0.01070, (47-23)/1028 = 0.02335
# y goes UP?  No

transform selisanneSTRpos:
    xalign 0.52140
    yalign 1.0


transform selisanneSTRpos_embrace:
    xalign 0.25
    yalign 1.0







# The game starts here.

label elisanneS_character_procedures:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image ellybedroom = "images/backgrounds/Sty_bg_0049_101_00.png"
    scene ellybedroom at middle

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    show selisanne with dissolve
    selly "Whew, it's been a while since we all scheduled a beach trip. ('selisanne' body)"

    hide selisanne

    show selisanneSTR at selisanneSTRpos
    selly "Hrrrgh!  Well, it looks like it still fits just fine!  ('selisanneSTR' body)"

    show selisanneSTR blush pout1
    selly "But... I dunno, can I still pull it off?  It's a little more... revealing than my usual attire."
    hide selisanneSTR

    show selisanne focused frown1
    selly "...N-No, Elly, you bought this because you wanted to have more confidence!  You can totally do this."
    selly "You just have some jitters!  And the answer for that is calisthenics and a facial workout.  Let's loosen everything up!"
    hide selisanne

    show selisanneSTR wink smile1 at selisanneSTRpos
    selly "Just breathe in... (wink, smile1)"
    hide selisanneSTR

    show selisanne wink smile1
    selly "...and breathe out... (wink, smile1)"
    hide selisanne

    show selisanneSTR angry smile2 at selisanneSTRpos
    selly "Breathe in... (angry, smile2)"
    hide selisanneSTR

    show selisanne angry smile2
    selly "...and breathe out... (angry, smile2)"
    hide selisanne

    show selisanneSTR blush frown1 at selisanneSTRpos
    selly "Breathe in... (blush, frown1)"
    hide selisanneSTR

    show selisanne blush frown1
    selly "...and breathe out... (blush, frown1)"
    hide selisanne

    show selisanneSTR flinch frown2 at selisanneSTRpos
    selly "Breathe in... (flinch, frown2)"
    hide selisanneSTR

    show selisanne flinch frown2
    selly "...and breathe out... (flinch, frown2)"
    hide selisanne

    show selisanneSTR focused frown3 at selisanneSTRpos
    selly "Breathe in... (focused, frown3)"
    hide selisanneSTR

    show selisanne focused frown3
    selly "...and breathe out... (focused, frown3)"
    hide selisanne

    show selisanneSTR relaxed frown4 at selisanneSTRpos
    selly "Breathe in... (relaxed, frown4)"
    hide selisanneSTR

    show selisanne relaxed frown4
    selly "...and breathe out... (relaxed, frown4)"
    hide selisanne

    show selisanneSTR sad pout1 at selisanneSTRpos
    selly "Breathe in... (sad, pout1)"
    hide selisanneSTR

    show selisanne sad pout1
    selly "...and breathe out... (sad, pout1)"
    hide selisanne

    show selisanneSTR squint shout1 at selisanneSTRpos
    selly "Two more to go!  Breathe in... (squint, shout1)!"
    hide selisanneSTR

    show selisanne squint shout1
    selly "...and breathe out... (squint, shout1)!"
    hide selisanne

    show selisanneSTR surprised shout1 at selisanneSTRpos
    selly "Last one!  Breathe in... (surprised, shout1)!"
    hide selisanneSTR

    show selisanne surprised shout1
    selly "...and breathe out... (surprised, shout1)!"

    show selisanne relaxed smile1
    selly "Whew!  That was a great body AND facial workout!"
    selly "Ok, I'm ready for the beach!  Let's hope that I can make it the best vacation possible for everyone!"

    hide selisanne with dissolve

    # This goes back to script

    jump testfiles
