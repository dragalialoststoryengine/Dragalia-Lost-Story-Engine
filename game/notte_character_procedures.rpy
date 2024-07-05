
    # Notte Character Procedures File

    # Paste this file into a story if you want to use Notte.  These procedures animate Notte as a speaker.
    # You'll also need to paste THIS line into your actual script above the script label whenever you're using Notte:

define nott = Character("Notte", callback=speaker("nott"))

    # This program assumes that the following folders exist:
    #     -"images/notte"
    #     -"images/notte/faces"
    #     -"images/notte/mouths"

    # Notte dynamically blinks and, while speaking, also moves her mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Notte appear*:
    #  -->  show notte with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Notte's eyes*:
    #  -->  show notte [keyword]
    #  List of eye keywords:
    #     -->  relaxed (default), closed_relaxed2, relaxed2, relaxed3, focused, grumpy,
    #          closed_grumpy, neutral, sad, sad2, shocked, surprised

    # *Changing Notte's mouth*:
    #  -->  show notte [keyword]
    #  List of mouth keywords:
    #     -->  smile1 (default), smile2, smile3, smile4, frown1, frown2, frown3,
    #          pout1, shout1, shout2, closed_smile1

    # *Writing dialogue for Notte*:
    #  --> nott "[Notte's line here]"

    # *Making Notte disappear*:
    #  --> hide notte with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage notte:

    always "images/notte/notte_body.png"

    group face:

        # 399/1028, 226/1028:
        pos (0.38813, 0.21984)

        attribute relaxed default:
            "notte_relaxed_eyes"

        attribute focused:
            "notte_focused_eyes"

        attribute relaxed2:
            "notte_relaxed2_eyes"

        attribute closed_relaxed2:
            "images/notte/faces/100007_01_parts_c017.png"

        attribute grumpy:
            "notte_grumpy_eyes"

        attribute closed_grumpy:
            "images/notte/faces/100007_01_parts_c019.png"

        attribute surprised:
            "notte_surprised_eyes"

        attribute sad:
            "notte_sad_eyes"

        attribute sad2:
            "notte_sad2_eyes"

        attribute shocked:
            "notte_shocked_eyes"

        attribute relaxed3:
            "notte_relaxed3_eyes"

        attribute neutral:
            "notte_neutral_eyes"


    group mouth:

        pos (0.38813, 0.21984)

        attribute smile1 default:
            "notte_smile1"

        attribute closed_smile1:
            "notte_smile1_nottalking"

        attribute frown1:
            "notte_frown1"

        attribute pout1:
            "notte_pout1"

        attribute shout1:
            "notte_shout1"

        attribute smile2:
            "notte_smile2"

        attribute frown2:
            "notte_frown2"

        attribute smile3:
            "notte_smile3"

        attribute shout2:
            "notte_shout2"

        attribute smile4:
            "notte_smile4"

        attribute frown3:
            "notte_frown3"


## EYE animations start here.

image notte_relaxed_eyes:
    "images/notte/faces/100007_01_parts_c000.png"
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
    "images/notte/faces/100007_01_parts_c001.png"
    0.05
    repeat

image notte_focused_eyes:
    "images/notte/faces/100007_01_parts_c006.png"
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
    "images/notte/faces/100007_01_parts_c007.png"
    0.05
    repeat

image notte_relaxed2_eyes:
    "images/notte/faces/100007_01_parts_c016.png"
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
    "images/notte/faces/100007_01_parts_c017.png"
    0.05
    repeat

image notte_grumpy_eyes:
    "images/notte/faces/100007_01_parts_c018.png"
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
    "images/notte/faces/100007_01_parts_c019.png"
    0.05
    repeat

image notte_surprised_eyes:
    "images/notte/faces/100007_01_parts_c020.png"
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
    "images/notte/faces/100007_01_parts_c021.png"
    0.05
    repeat

image notte_sad_eyes:
    "images/notte/faces/100007_01_parts_c022.png"
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
    "images/notte/faces/100007_01_parts_c023.png"
    0.05
    repeat

image notte_sad2_eyes:
    "images/notte/faces/100007_01_parts_c032.png"
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
    "images/notte/faces/100007_01_parts_c033.png"
    0.05
    repeat

# 034 and 004 are the same as 000

image notte_shocked_eyes:
    "images/notte/faces/100007_01_parts_c036.png"
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
    "images/notte/faces/100007_01_parts_c037.png"
    0.05
    repeat

image notte_relaxed3_eyes:
    "images/notte/faces/100007_01_parts_c038.png"
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
    "images/notte/faces/100007_01_parts_c039.png"
    0.05
    repeat

image notte_neutral_eyes:
    "images/notte/faces/100007_01_parts_c048.png"
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
    "images/notte/faces/100007_01_parts_c049.png"
    0.05
    repeat



# MOUTH animations start here.

image notte_smile1_nottalking = "images/notte/mouths/100007_01_parts_c008.png"

image notte_smile1_talking:
    "images/notte/mouths/100007_01_parts_c008.png"
    0.15
    "images/notte/mouths/100007_01_parts_c009.png"
    0.15
    repeat

image notte_smile1 = WhileSpeaking("nott", "notte_smile1_talking", "notte_smile1_nottalking")


# 010, 012 and 024 are the same as 008


image notte_frown1_nottalking = "images/notte/mouths/100007_01_parts_c014.png"

image notte_frown1_talking:
    "images/notte/mouths/100007_01_parts_c014.png"
    0.15
    "images/notte/mouths/100007_01_parts_c015.png"
    0.15
    repeat

image notte_frown1 = WhileSpeaking("nott", "notte_frown1_talking", "notte_frown1_nottalking")


image notte_pout1_nottalking = "images/notte/mouths/100007_01_parts_c026.png"

image notte_pout1_talking:
    "images/notte/mouths/100007_01_parts_c026.png"
    0.15
    "images/notte/mouths/100007_01_parts_c027.png"
    0.15
    repeat

image notte_pout1 = WhileSpeaking("nott", "notte_pout1_talking", "notte_pout1_nottalking")


image notte_shout1_nottalking = "images/notte/mouths/100007_01_parts_c028.png"

image notte_shout1_talking:
    "images/notte/mouths/100007_01_parts_c028.png"
    0.15
    "images/notte/mouths/100007_01_parts_c029.png"
    0.15
    repeat

image notte_shout1 = WhileSpeaking("nott", "notte_shout1_talking", "notte_shout1_nottalking")


image notte_smile2_nottalking = "images/notte/mouths/100007_01_parts_c030.png"

image notte_smile2_talking:
    "images/notte/mouths/100007_01_parts_c030.png"
    0.15
    "images/notte/mouths/100007_01_parts_c031.png"
    0.15
    repeat

image notte_smile2 = WhileSpeaking("nott", "notte_smile2_talking", "notte_smile2_nottalking")


image notte_frown2_nottalking = "images/notte/mouths/100007_01_parts_c040.png"

image notte_frown2_talking:
    "images/notte/mouths/100007_01_parts_c040.png"
    0.15
    "images/notte/mouths/100007_01_parts_c041.png"
    0.15
    repeat

image notte_frown2 = WhileSpeaking("nott", "notte_frown2_talking", "notte_frown2_nottalking")


image notte_smile3_nottalking = "images/notte/mouths/100007_01_parts_c042.png"

image notte_smile3_talking:
    "images/notte/mouths/100007_01_parts_c042.png"
    0.15
    "images/notte/mouths/100007_01_parts_c043.png"
    0.15
    repeat

image notte_smile3 = WhileSpeaking("nott", "notte_smile3_talking", "notte_smile3_nottalking")


image notte_shout2_nottalking = "images/notte/mouths/100007_01_parts_c044.png"

image notte_shout2_talking:
    "images/notte/mouths/100007_01_parts_c044.png"
    0.15
    "images/notte/mouths/100007_01_parts_c045.png"
    0.15
    repeat

image notte_shout2 = WhileSpeaking("nott", "notte_shout2_talking", "notte_shout2_nottalking")


image notte_smile4_nottalking = "images/notte/mouths/100007_01_parts_c046.png"

image notte_smile4_talking:
    "images/notte/mouths/100007_01_parts_c046.png"
    0.15
    "images/notte/mouths/100007_01_parts_c047.png"
    0.15
    repeat

image notte_smile4 = WhileSpeaking("nott", "notte_smile4_talking", "notte_smile4_nottalking")


image notte_frown3_nottalking = "images/notte/mouths/100007_01_parts_c050.png"

image notte_frown3_talking:
    "images/notte/mouths/100007_01_parts_c050.png"
    0.15
    "images/notte/mouths/100007_01_parts_c051.png"
    0.15
    repeat

image notte_frown3 = WhileSpeaking("nott", "notte_frown3_talking", "notte_frown3_nottalking")



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

label notte_character_procedures:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image halidom_hall = "images/backgrounds/Sty_bg_0024_100_00.png"
    scene halidom_hall

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show notte with dissolve
    nott "♪ Hmmm hmmm hmm, la la la... ♫"

    show notte closed_relaxed2
    nott "It's not very often I have the whole Halidom to myself!  Time to majorly chillax!"

    show notte surprised frown1
    nott "...Oh?  Has this mirror always been here?"

    show notte neutral smile2
    nott "Well, there's only one thing to do in this situation..."

    show notte focused smile1
    nott "...FUNNY FACES TIME!!!"

    nott "That's right!  Time for this gal to get out ALL the goofy!"

    show notte relaxed smile1
    nott "Alright, FIRST, we start with a nice 'relaxed' face and a regular ol' smile (smile1)..."

    show notte relaxed2 smile2
    nott "Now, we tilt the eyes up a little (relaxed2), and put a little skew on that smile (smile2)."

    show notte closed_relaxed2 smile3
    nott "Close the eyes (closed_relaxed2) for a few seconds to mix things up, and close in the corners of the mouth (smile3)..."

    show notte relaxed3 smile4
    nott "Now we make it all loose!  Lower the eyebrows a bit (relaxed3) and relax the smile (smile4)."

    show notte focused frown1
    nott "No, no!  I gotta focus (focused)!  Not NEARLY silly enough.  Break out the frowns (frown1), 'cause Notte's gonna go all out!!!"

    show notte grumpy pout1
    nott "Time for CLASSIC GRUMP NOTTE!  We're talking pouty eyes (grumpy), pouty mouth (pout1), the whole works!"

    show notte neutral frown2
    nott "...Nah, let's go for a more 'neutral' face and a tiny frown (frown2)."

    show notte sad frown3
    nott "Ok, time to break out the pathos!  'Sad' eyes, super tiny mouth (frown3).  Oh, it's all just so much!!"

    show notte sad2 shout1
    nott "Now, we RAISE THE VOICE with a SHOUT (shout1)!  And we'll raise the eyebrows on the sad (sad2) face.  \"Alas, poor Nedrick!  I knew him, Cleo!!\""

    show notte closed_relaxed2 smile1
    nott "...PFFT!  Hahaha!  Ok, now we've got some Grade-A silliness going on here!"

    show notte shocked shout2
    nott "...EEEK!!!!"
    nott "What are YOU doing here?!?  I thought I was alone!  Are you trying to make me die of 'shock'!!"

    show notte surprised shout2
    nott "...You came because you heard me shout (shout2)?  ...W-Well, I thought I was alone!  You still 'surprised' me, mister!"
    nott "..."

    show notte grumpy pout1
    nott "--I was NOT practicing funny faces!  Th-That is my LEAST favorite thing to do!"

    show notte closed_grumpy pout1
    nott "...AAAA, stop teasing me (closed_grumpy)!!!  It's not fair, you know me too well!!!"

    hide notte with dissolve


    # This goes back to script

    jump testfiles
