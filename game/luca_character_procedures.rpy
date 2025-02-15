    # Luca Character Procedures File

    # Paste this file into a story if you want to use Luca.  These procedures animate Luca as a speaker.

define luc = Character("Luca", callback=speaker("luc"))

    # This program assumes that the following folders exist:
    #     -"images/luca"
    #     -"images/luca/faces"
    #     -"images/luca/mouths"

    # Luca dynamically blinks and, while speaking, also moves his mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Luca appear*:
    #  -->  show luca with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Luca's eyes*:
    #  -->  show luca [keyword]
    #  List of eye keywords:
    #     -->  focused (the default option), focused2, relaxed, relaxed_closed, shocked, surprised,
    #          blushing, flinch, askance, angry, crying, crying2, sad

    # *Changing Luca's mouth*:
    #  -->  show luca [keyword]
    #  List of mouth keywords:
    #     -->  grin1 (the default option), grin2, grin3, frown1, frown2, frown3, mutter1, frown5, shout1,
    #          smile1, smile2, grimace1, sweat, grin1_closed, frown1_closed

    # *Writing dialogue for Luca*:
    #  --> luc "[Luca's line here]"

    # *Making Luca disappear*:
    #  --> hide luca with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage luca:

    always "images/luca/luca_body.png"

    group face:

        # 436/1028, 200/1028:
        pos (0.42412, 0.19455)

        attribute focused default:
            "luca_focused_eyes"

        attribute focused2:
            "luca_focused2_eyes"

        attribute relaxed:
            "luca_relaxed_eyes"
        
        attribute relaxed_closed:
            "images/luca/faces/100006_01_parts_c017.png"

        attribute flinch:
            "luca_flinch_eyes"

        attribute shocked:
            "luca_shocked_eyes"

        attribute blushing:
            "luca_blushing_eyes"

        attribute askance:
            "luca_askance_eyes"

        attribute surprised:
            "luca_surprised_eyes"

        attribute angry:
            "luca_angry_eyes"

        attribute crying:
            "luca_crying_eyes"

        attribute crying2:
            "luca_crying2_eyes"

        attribute sad:
            "luca_sad_eyes"


    group mouth:

        pos (0.42412, 0.19455)

        attribute grin1 default:
            "luca_grin1"

        attribute grin1_closed:
            "images/luca/mouths/100006_01_parts_c008.png"

        attribute frown1:
            "luca_frown1"

        attribute frown1_closed:
            "images/luca/mouths/100006_01_parts_c014.png"

        attribute smile1:
            "luca_smile1"

        attribute grimace1:
            "luca_grimace1"

        attribute frown2:
            "luca_frown2"

        attribute frown3:
            "luca_frown3"

        attribute mutter1:
            "luca_mutter1"

        attribute frown5:
            "luca_frown5"

        attribute shout1:
            "luca_shout1"

        attribute grin2:
            "luca_grin2"

        attribute grin3:
            "luca_grin3"

        attribute smile2:
            "luca_smile2"

        attribute sweat:
            "luca_sweat"



## EYE animations start here.

# Note:  000-005 are all from the same expression, and 038, 039.

image luca_focused_eyes:
    "images/luca/faces/100006_01_parts_c000.png"
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
    "images/luca/faces/100006_01_parts_c001.png"
    0.05
    repeat

image luca_focused2_eyes:
    "images/luca/faces/100006_01_parts_c006.png"
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
    "images/luca/faces/100006_01_parts_c007.png"
    0.05
    repeat

image luca_relaxed_eyes:
    "images/luca/faces/100006_01_parts_c016.png"
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
    "images/luca/faces/100006_01_parts_c017.png"
    0.05
    repeat

image luca_flinch_eyes:
    "images/luca/faces/100006_01_parts_c018.png"
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
    "images/luca/faces/100006_01_parts_c019.png"
    0.05
    repeat

image luca_shocked_eyes:
    "images/luca/faces/100006_01_parts_c020.png"
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
    "images/luca/faces/100006_01_parts_c021.png"
    0.05
    repeat

image luca_blushing_eyes:
    "images/luca/faces/100006_01_parts_c022.png"
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
    "images/luca/faces/100006_01_parts_c023.png"
    0.05
    repeat

image luca_askance_eyes:
    "images/luca/faces/100006_01_parts_c032.png"
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
    "images/luca/faces/100006_01_parts_c033.png"
    0.05
    repeat

image luca_surprised_eyes:
    "images/luca/faces/100006_01_parts_c034.png"
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
    "images/luca/faces/100006_01_parts_c035.png"
    0.05
    repeat

image luca_angry_eyes:
    "images/luca/faces/100006_01_parts_c036.png"
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
    "images/luca/faces/100006_01_parts_c037.png"
    0.05
    repeat

image luca_crying_eyes:
    "images/luca/faces/100006_01_parts_c048.png"
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
    "images/luca/faces/100006_01_parts_c049.png"
    0.05
    repeat


image luca_crying2_eyes:
    "images/luca/faces/100006_01_parts_c050.png"
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
    "images/luca/faces/100006_01_parts_c051.png"
    0.05
    repeat


image luca_sad_eyes:
    "images/luca/faces/100006_01_parts_c052.png"
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
    "images/luca/faces/100006_01_parts_c053.png"
    0.05
    repeat


# MOUTH animations start here.

# 008-013 are all from the same grin.

image luca_grin1_nottalking = "images/luca/mouths/100006_01_parts_c008.png"

image luca_grin1_talking:
    "images/luca/mouths/100006_01_parts_c008.png"
    0.15
    "images/luca/mouths/100006_01_parts_c009.png"
    0.15
    repeat

image luca_grin1 = WhileSpeaking("luc", "luca_grin1_talking", "luca_grin1_nottalking")


image luca_frown1_nottalking = "images/luca/mouths/100006_01_parts_c014.png"

image luca_frown1_talking:
    "images/luca/mouths/100006_01_parts_c014.png"
    0.15
    "images/luca/mouths/100006_01_parts_c015.png"
    0.15
    repeat

image luca_frown1 = WhileSpeaking("luc", "luca_frown1_talking", "luca_frown1_nottalking")


image luca_smile1_nottalking = "images/luca/mouths/100006_01_parts_c024.png"

image luca_smile1_talking:
    "images/luca/mouths/100006_01_parts_c024.png"
    0.15
    "images/luca/mouths/100006_01_parts_c025.png"
    0.15
    repeat

image luca_smile1 = WhileSpeaking("luc", "luca_smile1_talking", "luca_smile1_nottalking")


image luca_grimace1_nottalking = "images/luca/mouths/100006_01_parts_c026.png"

image luca_grimace1_talking:
    "images/luca/mouths/100006_01_parts_c026.png"
    0.15
    "images/luca/mouths/100006_01_parts_c027.png"
    0.15
    repeat

image luca_grimace1 = WhileSpeaking("luc", "luca_grimace1_talking", "luca_grimace1_nottalking")


image luca_frown2_nottalking = "images/luca/mouths/100006_01_parts_c028.png"

image luca_frown2_talking:
    "images/luca/mouths/100006_01_parts_c028.png"
    0.15
    "images/luca/mouths/100006_01_parts_c029.png"
    0.15
    repeat

image luca_frown2 = WhileSpeaking("luc", "luca_frown2_talking", "luca_frown2_nottalking")


image luca_frown3_nottalking = "images/luca/mouths/100006_01_parts_c030.png"

image luca_frown3_talking:
    "images/luca/mouths/100006_01_parts_c030.png"
    0.15
    "images/luca/mouths/100006_01_parts_c031.png"
    0.15
    repeat

image luca_frown3 = WhileSpeaking("luc", "luca_frown3_talking", "luca_frown3_nottalking")


image luca_mutter1_nottalking = "images/luca/mouths/100006_01_parts_c040.png"

image luca_mutter1_talking:
    "images/luca/mouths/100006_01_parts_c040.png"
    0.15
    "images/luca/mouths/100006_01_parts_c041.png"
    0.15
    repeat

image luca_mutter1 = WhileSpeaking("luc", "luca_mutter1_talking", "luca_mutter1_nottalking")


image luca_frown5_nottalking = "images/luca/mouths/100006_01_parts_c042.png"

image luca_frown5_talking:
    "images/luca/mouths/100006_01_parts_c042.png"
    0.15
    "images/luca/mouths/100006_01_parts_c043.png"
    0.15
    repeat

image luca_frown5 = WhileSpeaking("luc", "luca_frown5_talking", "luca_frown5_nottalking")


image luca_shout1_nottalking = "images/luca/mouths/100006_01_parts_c044.png"

image luca_shout1_talking:
    "images/luca/mouths/100006_01_parts_c044.png"
    0.15
    "images/luca/mouths/100006_01_parts_c045.png"
    0.15
    repeat

image luca_shout1 = WhileSpeaking("luc", "luca_shout1_talking", "luca_shout1_nottalking")


image luca_frown7_nottalking = "images/luca/mouths/100006_01_parts_c046.png"

image luca_frown7_talking:
    "images/luca/mouths/100006_01_parts_c046.png"
    0.15
    "images/luca/mouths/100006_01_parts_c047.png"
    0.15
    repeat

image luca_frown7 = WhileSpeaking("luc", "luca_frown7_talking", "luca_frown7_nottalking")


image luca_grin2_nottalking = "images/luca/mouths/100006_01_parts_c055.png"

image luca_grin2_talking:
    "images/luca/mouths/100006_01_parts_c055.png"
    0.15
    "images/luca/mouths/100006_01_parts_c056.png"
    0.15
    repeat

image luca_grin2 = WhileSpeaking("luc", "luca_grin2_talking", "luca_grin2_nottalking")


image luca_grin3_nottalking = "images/luca/mouths/100006_01_parts_c057.png"

image luca_grin3_talking:
    "images/luca/mouths/100006_01_parts_c057.png"
    0.15
    "images/luca/mouths/100006_01_parts_c058.png"
    0.15
    repeat

image luca_grin3 = WhileSpeaking("luc", "luca_grin3_talking", "luca_grin3_nottalking")


image luca_smile2_nottalking = "images/luca/mouths/100006_01_parts_c059.png"

image luca_smile2_talking:
    "images/luca/mouths/100006_01_parts_c059.png"
    0.15
    "images/luca/mouths/100006_01_parts_c060.png"
    0.15
    repeat

image luca_smile2 = WhileSpeaking("luc", "luca_smile2_talking", "luca_smile2_nottalking")


image luca_sweat_nottalking = "images/luca/mouths/100006_01_parts_c061.png"

image luca_sweat_talking:
    "images/luca/mouths/100006_01_parts_c061.png"
    0.15
    "images/luca/mouths/100006_01_parts_c062.png"
    0.15
    repeat

image luca_sweat = WhileSpeaking("luc", "luca_sweat_talking", "luca_sweat_nottalking")



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

label luca_character_procedures:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image forestday = "images/backgrounds/Sty_bg_0021_100_00.png"
    scene forestday at middle



    show luca with dissolve
    luc "Heh, these chuckleberries ought to go nicely with--"

    show luca surprised2 frown5
    luc "Oh, you're here!  Uh... Hi!"

    show luca frown3
    luc "So, uh... you're probably asking why I asked you to come here."

    show luca smile2 relaxed
    luc "Well... would you mind... looking at some faces of mine?"

    show luca frustrated sweat
    luc "See, you know that I enjoy the occasional prank or two, but..."

    show luca grimace
    luc "...Well, Sarisse can basically read me like an open look at this point.  It's super annoying..."

    show luca grin2 focused
    luc "My thought is that if I practice controlling my expression more, I'll be able to actually surprise her for once."

    show luca sweat
    luc "Does... that make sense to you?"

    show luca blushing grin1
    luc "You'll do it??  That's great!!"

    show luca focused grin1
    luc "Anyway... this is my default 'focused' expression, I think?"

    show luca focused2
    luc "And... this is a focused expression that's a little more intense (focused2)?"

    show luca relaxed
    luc "Now, this is more of a relaxed look.  I really want to be able to pull this one off, so make sure it looks good!"

    show luca surprised
    luc "This is a surprised look.  Now, could you quickly say, 'Hey, Luca, what's this thing over there?  Do you have something to do with that?'"

    show luca surprised2
    luc "What?  You can tell I'm faking?? That's... kind of surprising (surprised2) in its own right..."

    show luca blushing
    luc "I guess I still have a lot to work on before I can hide my emotions convincingly.  Heh, look at me, I'm blushing!"

    show luca flinch
    luc "Uh... well, anyway, this next one is more of a flinch.  Not really helpful unless I'm already caught, but... anyway..."

    show luca frustrated
    luc "And this is more of a frustrated look.  Maybe this looks real?"

    show luca angry
    luc "And, if Sarisse keeps pressing me, I could look angry like this?"

    show luca crying grin
    luc "BAHAHAHA!  I'm sorry!!  I just can't keep a straight face anymore!  Look at me, I'm crying!!!"

    show luca crying2 sweat
    luc "Ahhh, you're a good sport for being patient with me.  I guess if I'm crying (crying2) like this, then this may be a bust."

    show luca sad
    luc "Oh well... I'm sad that I wasted your time, but... it looks like you had fun as well?"

    show luca shocked frown1
    luc "Wait... you don't think I should give up yet?  I should try to control my mouth a little more?"

    show luca focused grin1
    luc "You're... you're right!  Thanks, I should at least give that a shot!"

    show luca grin1
    luc "Well, this is my trademark grin (grin1), but I should probably try some other expressions out."

    show luca grin2
    luc "This is a second grin (grin2) that... shows a little more teeth when I'm talking, I guess?"

    show luca grin3
    luc "And this is a really big grin (grin3)!  This would be good for yelling 'SURPRISE'!!"

    show luca frown1
    luc "Oh, but I should practice serious faces too.  Here's a frown (frown1)..."

    show luca frown2
    luc "And this is a second frown (frown2) that has... a little more emotion in it?  Maybe some annoyance?"

    show luca frown3
    luc "This is more of an understated frown (frown3).  Maybe a little neutral?  What do you think?"

    show luca mutter1
    luc "This frown (mutter1) has more teeth and is also wider and thinner.  This would be good to express frustration."

    show luca frown5
    luc "Oops! This one (frown5)'s kind of goofy and awkward.  ...What?  You think it's cute?  That's embarrassing!"

    show luca shout1
    luc "Oh!  I almost forgot!!!  If I'm shouting and upset, I might look something like this (shout1)!!!"

    show luca smile1
    luc "Uh... Well, let me try some smiles with a little less teeth now (smile1)."

    show luca smile2
    luc "Wait... that last one still had some teeth?  Uh... well, let me try smiling while being more careful about that (smile2)..."

    show luca grimace1
    luc "Geez, this is a lot harder than I expected... Definitely worth a grimace (grimace1), huh?"

    show luca sweat
    luc "For crying out loud, this is so much effort that I've got a bead of sweat!"

    show luca relaxed
    luc "Man... I guess I am really hopeless when it comes to keeping a poker face, aren't I?"

    show luca surprised frown5
    luc "What??  You think that's 'part of my charm?'  And it's a good thing that I can be honest about my feelings?"

    show luca relaxed smile1
    luc "Heh...  I guess there's maybe some truth to that."

    luc "Well, I guess I probably shouldn't take up any more of your time.  I'll keep looking for prank supp--"

    show luca surprised grin2
    luc " I mean, uh, gathering food for dinner!  Ha ha ha ha..."

    hide luca with dissolve


    # This goes back to script

    jump testfiles
