
    # Cleo Character Procedures File

    # Paste this file into a story if you want to use Cleo.  These procedures animate Cleo as a speaker.
    # You'll also need to paste THIS line into your actual script above the script label whenever you're using Cleoe:

define cle = Character("Cleo", callback=speaker("cle"))

    # This program assumes that the following folders exist:
    #     -"images/cleo"
    #     -"images/cleo/faces"
    #     -"images/cleo/mouths"



    # Cleo dynamically blinks and, while speaking, also moves her mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Cleo appear*:
    #  -->  show cleo with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Cleo's eyes*:
    #  -->  show cleo [keyword]
    #  List of eye keywords:
    #     -->  focused (default), focused2, angry, blush_angry, blush_askance,
    #          closed_focused, glare, relaxed, sad, shocked, surprised,

    # *Changing Cleo's mouth*:
    #  -->  show cleo [keyword]
    #  List of mouth keywords:
    #     -->  mutter1 (default), mutter2, frown1, frown2, pout1,
    #          shout1, smile1, smile2, smile3, triangle1, mutter1_closed

    # *Writing dialogue for Cleo*:
    #  --> cle "[Notte's line here]"

    # *Making Cleo disappear*:
    #  --> hide cleo with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage cleo:

    always "images/cleo/cleo_body.png"

    group face:

        # 441/1024, 269/1024:

        pos (0.430664, 0.262695)

        attribute focused default:
            "cleo_focused_eyes"

        attribute closed_focused:
            "images/cleo/faces/100004_01_parts_c001.png"

        attribute focused2:
            "cleo_focused2_eyes"

        attribute surprised:
            "cleo_surprised_eyes"

        attribute glare:
            "cleo_glare_eyes"

        attribute shocked:
            "cleo_shocked_eyes"

        attribute blush_askance:
            "cleo_blush_askance_eyes"

        attribute sad:
            "cleo_sad_eyes"

        attribute relaxed:
            "cleo_relaxed_eyes"

        attribute angry:
            "cleo_angry_eyes"

        attribute blush_angry:
            "cleo_blush_angry_eyes"


    group mouth:

        pos (0.430664, 0.262695)

        attribute mutter1 default:
            "cleo_mutter1"

        attribute mutter1_closed:
            "images/cleo/mouths/100004_01_parts_c004.png"

        attribute mutter2:
            "cleo_mutter2"

        attribute smile1:
            "cleo_smile1"

        attribute triangle1:
            "cleo_triangle1"

        attribute frown1:
            "cleo_frown1"

        attribute smile2:
            "cleo_smile2"

        attribute frown2:
            "cleo_frown2"

        attribute smile3:
            "cleo_smile3"

        attribute shout1:
            "cleo_shout1"

        attribute pout1:
            "cleo_pout1"


## EYE animations start here.

image cleo_focused_eyes:
    "images/cleo/faces/100004_01_parts_c000.png"
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
    "images/cleo/faces/100004_01_parts_c001.png"
    0.05
    repeat

image cleo_focused2_eyes:
    "images/cleo/faces/100004_01_parts_c002.png"
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
    "images/cleo/faces/100004_01_parts_c003.png"
    0.05
    repeat

image cleo_surprised_eyes:
    "images/cleo/faces/100004_01_parts_c009.png"
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
    "images/cleo/faces/100004_01_parts_c010.png"
    0.05
    repeat

image cleo_glare_eyes:
    "images/cleo/faces/100004_01_parts_c011.png"
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
    "images/cleo/faces/100004_01_parts_c012.png"
    0.05
    repeat

image cleo_shocked_eyes:
    "images/cleo/faces/100004_01_parts_c013.png"
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
    "images/cleo/faces/100004_01_parts_c014.png"
    0.05
    repeat

image cleo_blush_askance_eyes:
    "images/cleo/faces/100004_01_parts_c015.png"
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
    "images/cleo/faces/100004_01_parts_c016.png"
    0.05
    repeat

image cleo_sad_eyes:
    "images/cleo/faces/100004_01_parts_c025.png"
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
    "images/cleo/faces/100004_01_parts_c026.png"
    0.05
    repeat

image cleo_relaxed_eyes:
    "images/cleo/faces/100004_01_parts_c027.png"
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
    "images/cleo/faces/100004_01_parts_c028.png"
    0.05
    repeat

image cleo_angry_eyes:
    "images/cleo/faces/100004_01_parts_c029.png"
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
    "images/cleo/faces/100004_01_parts_c030.png"
    0.05
    repeat

# 031 is the same as 001

image cleo_blush_angry_eyes:
    "images/cleo/faces/100004_01_parts_c040.png"
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
    "images/cleo/faces/100004_01_parts_c041.png"
    0.05
    repeat






# MOUTH animations start here.

image cleo_mutter1_nottalking = "images/cleo/mouths/100004_01_parts_c004.png"

image cleo_mutter1_talking:
    "images/cleo/mouths/100004_01_parts_c005.png"
    0.15
    "images/cleo/mouths/100004_01_parts_c004.png"
    0.15
    repeat

image cleo_mutter1 = WhileSpeaking("cle", "cleo_mutter1_talking", "cleo_mutter1_nottalking")


image cleo_mutter2_nottalking = "images/cleo/mouths/100004_01_parts_c007.png"

image cleo_mutter2_talking:
    "images/cleo/mouths/100004_01_parts_c008.png"
    0.15
    "images/cleo/mouths/100004_01_parts_c007.png"
    0.15
    repeat

image cleo_mutter2 = WhileSpeaking("cle", "cleo_mutter2_talking", "cleo_mutter2_nottalking")


image cleo_smile1_nottalking = "images/cleo/mouths/100004_01_parts_c017.png"

image cleo_smile1_talking:
    "images/cleo/mouths/100004_01_parts_c018.png"
    0.15
    "images/cleo/mouths/100004_01_parts_c017.png"
    0.15
    repeat

image cleo_smile1 = WhileSpeaking("cle", "cleo_smile1_talking", "cleo_smile1_nottalking")


image cleo_triangle1_nottalking = "images/cleo/mouths/100004_01_parts_c019.png"

image cleo_triangle1_talking:
    "images/cleo/mouths/100004_01_parts_c020.png"
    0.15
    "images/cleo/mouths/100004_01_parts_c019.png"
    0.15
    repeat

image cleo_triangle1 = WhileSpeaking("cle", "cleo_triangle1_talking", "cleo_triangle1_nottalking")


image cleo_frown1_nottalking = "images/cleo/mouths/100004_01_parts_c021.png"

image cleo_frown1_talking:
    "images/cleo/mouths/100004_01_parts_c022.png"
    0.15
    "images/cleo/mouths/100004_01_parts_c021.png"
    0.15
    repeat

image cleo_frown1 = WhileSpeaking("cle", "cleo_frown1_talking", "cleo_frown1_nottalking")


image cleo_smile2_nottalking = "images/cleo/mouths/100004_01_parts_c023.png"

image cleo_smile2_talking:
    "images/cleo/mouths/100004_01_parts_c024.png"
    0.15
    "images/cleo/mouths/100004_01_parts_c023.png"
    0.15
    repeat

image cleo_smile2 = WhileSpeaking("cle", "cleo_smile2_talking", "cleo_smile2_nottalking")


image cleo_frown2_nottalking = "images/cleo/mouths/100004_01_parts_c032.png"

image cleo_frown2_talking:
    "images/cleo/mouths/100004_01_parts_c033.png"
    0.15
    "images/cleo/mouths/100004_01_parts_c032.png"
    0.15
    repeat

image cleo_frown2 = WhileSpeaking("cle", "cleo_frown2_talking", "cleo_frown2_nottalking")


image cleo_smile3_nottalking = "images/cleo/mouths/100004_01_parts_c034.png"

image cleo_smile3_talking:
    "images/cleo/mouths/100004_01_parts_c035.png"
    0.15
    "images/cleo/mouths/100004_01_parts_c034.png"
    0.15
    repeat

image cleo_smile3 = WhileSpeaking("cle", "cleo_smile3_talking", "cleo_smile3_nottalking")


image cleo_shout1_nottalking = "images/cleo/mouths/100004_01_parts_c036.png"

image cleo_shout1_talking:
    "images/cleo/mouths/100004_01_parts_c037.png"
    0.15
    "images/cleo/mouths/100004_01_parts_c036.png"
    0.15
    repeat

image cleo_shout1 = WhileSpeaking("cle", "cleo_shout1_talking", "cleo_shout1_nottalking")


image cleo_pout1_nottalking = "images/cleo/mouths/100004_01_parts_c042.png"

image cleo_pout1_talking:
    "images/cleo/mouths/100004_01_parts_c043.png"
    0.15
    "images/cleo/mouths/100004_01_parts_c042.png"
    0.15
    repeat

image cleo_pout1 = WhileSpeaking("cle", "cleo_pout1_talking", "cleo_pout1_nottalking")







# The game starts here.

label cleo_character_procedures:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image kitchen = "images/backgrounds/Sty_bg_0031_100_00.png"
    scene kitchen

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show cleo with dissolve
    cle "Oh, hello there, Your Highness.  I'll have to multitask with this stew, but there's something I wanted to discuss with you."

    show cleo focused mutter1
    cle "(focused mutter1) After talking with Mitsuba, I've been thinking.  According to her, cooking is more than just the dish itself, but also the atmosphere and presentation."

    show cleo focused2 mutter2
    cle "(focused2 mutter2) Now... I know that everyone in the Halidom likes my cooking, but I can't help but think how Mitsuba has a sort of... infectious enthusiasm to her.  A certain charisma factor, if you will."

    show cleo angry frown1
    cle "(angry frown1) As the Halidom's primary caretaker, I think I should learn from her example and try to emulate her positive and outgoing demeanor when serving food."

    show cleo blush_angry triangle1
    cle "(blush_angry triangle1) And... that's why I want to first attempt this with you!  Because I... value your feedback most highly!  And... as the master of the castle, it only makes sense that my demeanor should be approved by you first!"

    show cleo blush_askance pout1
    cle "(blush_askance pout1) Wh-What do you mean, \"you think I'm perfect the way I am?\"  With lines like that...!  I-I don't see why I shouldn't try to strive for perfection in every aspect of my duties!"

    show cleo closed_focused frown2
    cle "(closed_focused frown2) I-In any case, I would like you to evaluate several different faces I've practiced to see which one you find most appropriate."

    show cleo relaxed smile1
    cle "(relaxed smile1) Expression #1 is one that I think is the most neutral.  Relaxed eyes, and a smile that's not too large or small.  (ahem)  \"Hello, everone!  Dinner is ready, so please enjoy!\""

    show cleo sad smile2
    cle "(sad smile2) The second option is something a little more subdued, trying to stay humble and sympathetic.  (ahem) \"Greetings; I hope your day hasn't been too hard.  Please enjoy this meal and recover your strength.  It's the least I can do to help.\""

    show cleo surprised smile3
    cle "(surprised smile3) And, uh, Expression #3 is one where I'm trying to match Mitsuba's energy!!   High eyebrows, and a large smile!  (ahem) \"Hey, everyone!!!  Dinner is served!!!  Please dig in!!!\""

    show cleo focused frown1
    cle "...Well?  Which did you find most pleasing?"
    cle "\"It seems like you're overthinking in all of them?!\"  \"Just be yourself?!\"  What kind of answer is that?!"
    cle "I implore you, Your Highness, please give some THOUGHT to this; I'm very serious about what I meant.  You needn't try to spare my feelings--"


    show cleo shocked shout1
    cle "(shocked shout1) --AAAAACK!!!  THE STEW IS BOILING OVER!!!  I lost track thanks to all this fuss about my face!!!"

    cle "Quickly stir, stir... (pant) reduce the heat... Whew, I think I've managed to salvage--"

    show cleo glare mutter2
    cle "(glare mutter2) --Excuse, me.  Your Highness.  I KNOW that you weren't just trying to steal one of those cookies while my attention was diverted by the stew, CORRECT?"
    cle "Those cookies are for AFTER SUPPER, Your Highness.  You'll ruin your appetite for a stew that I've simmered painstakingly for hours."

    show cleo glare triangle1
    cle "...What do you mean, \"so much for your demeanor\"?  I'll obviously make sure to smile when I'm ACTUALLY serving them.  Now see yourself out, I don't have time for food-filchers!"

    show cleo closed_focused
    cle "(ahem) ...respectfully.  Your Highness..."


    hide cleo with dissolve

    # This goes back to script

    jump testfiles
