
    # Alex Character Procedures File

    # Paste this file into a story if you want to use Notte.  These procedures animate Notte as a speaker.
    # You'll also need to paste THIS line into your actual script above the script label whenever you're using Notte:

define mym = Character("Mym", callback=speaker("mym"))

    # This program assumes that the following folders exist:
    #     -"images/mym"
    #     -"images/mym/faces"
    #     -"images/mym/mouths"
    #     -"images/mym/faces_normal"
    #     -"images/mym/mouths_normal"

    # "alex_back" procedures are further down below, so you need to scroll!!


    # Alex dynamically blinks and, while speaking, also moves her mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Mym appear*:
    #  -->  show mym_img with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Mym's eyes*:
    #  -->  show mym_img [keyword]
    #  List of eye keywords:
    #     -->  neutral (default), closed_neutral, askance, blush,
    #          focused, focused2, pained, relaxed, surprised

    # *Changing Mym's mouth*:
    #  -->  show mym_img [keyword]
    #  List of mouth keywords:
    #     -->  smile1 (default), smile2, awkward1, frown1, frown2,
    #           grimace1, mutter1, shout1, shout2

    # *Writing dialogue for Mym*:
    #  --> mym "[Notte's line here]"

    # *Making Mym disappear*:
    #  --> hide mym_img with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage mym_img:

    always "images/mym/mym_normal_body.png"

    group face:

        # 442/1024, 221/1024:
        pos (0.43164, 0.21582)

        attribute neutral default:
            "mym_neutral_eyes"

        attribute closed_neutral:
            "images/mym/faces_normal/100010_05_parts_c001.png"

        attribute focused:
            "mym_focused_eyes"

        attribute relaxed:
            "mym_relaxed_eyes"

        attribute pained:
            "mym_pained_eyes"

        attribute surprised:
            "mym_surprised_eyes"

        attribute blush:
            "mym_blush_eyes"

        attribute askance:
            "mym_askance_eyes"

        attribute focused2:
            "mym_focused2_eyes"



    group mouth:

        pos (0.43164, 0.21582)

        attribute smile1 default:
            "mym_smile1"

        attribute frown1:
            "mym_frown1"

        attribute smile2:
            "mym_smile2"

        attribute frown2:
            "mym_frown2"

        attribute shout1:
            "mym_shout1"

        attribute awkward1:
            "mym_awkward1"

        attribute grimace1:
            "mym_grimace1"

        attribute mutter1:
            "mym_mutter1"

        attribute shout2:
            "mym_shout2"


## EYE animations start here.

image mym_neutral_eyes:
    "images/mym/faces_normal/100010_05_parts_c000.png"
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
    "images/mym/faces_normal/100010_05_parts_c001.png"
    0.05
    repeat

# 002 and 003 are the same as 001.  Deleted.

# 004/005 is the same as 000/001.  Deleted.

image mym_focused_eyes:
    "images/mym/faces_normal/100010_05_parts_c006.png"
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
    "images/mym/faces_normal/100010_05_parts_c007.png"
    0.05
    repeat

image mym_relaxed_eyes:
    "images/mym/faces_normal/100010_05_parts_c016.png"
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
    "images/mym/faces_normal/100010_05_parts_c017.png"
    0.05
    repeat

image mym_pained_eyes:
    "images/mym/faces_normal/100010_05_parts_c018.png"
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
    "images/mym/faces_normal/100010_05_parts_c019.png"
    0.05
    repeat

image mym_surprised_eyes:
    "images/mym/faces_normal/100010_05_parts_c020.png"
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
    "images/mym/faces_normal/100010_05_parts_c021.png"
    0.05
    repeat

image mym_blush_eyes:
    "images/mym/faces_normal/100010_05_parts_c022.png"
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
    "images/mym/faces_normal/100010_05_parts_c023.png"
    0.05
    repeat

image mym_askance_eyes:
    "images/mym/faces_normal/100010_05_parts_c032.png"
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
    "images/mym/faces_normal/100010_05_parts_c033.png"
    0.05
    repeat

# 034/035 is the same as 000/001.  Deleted.

image mym_focused2_eyes:
    "images/mym/faces_normal/100010_05_parts_c036.png"
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
    "images/mym/faces_normal/100010_05_parts_c037.png"
    0.05
    repeat





# MOUTH animations start here.

image mym_smile1_nottalking = "images/mym/mouths_normal/100010_05_parts_c008.png"

image mym_smile1_talking:
    "images/mym/mouths_normal/100010_05_parts_c009.png"
    0.15
    "images/mym/mouths_normal/100010_05_parts_c008.png"
    0.15
    repeat

image mym_smile1 = WhileSpeaking("mym", "mym_smile1_talking", "mym_smile1_nottalking")


# 010/011 are the same as 008/009.  Deleted.


# 012/013 are the same as 008/009.  Deleted.


image mym_frown1_nottalking = "images/mym/mouths_normal/100010_05_parts_c014.png"

image mym_frown1_talking:
    "images/mym/mouths_normal/100010_05_parts_c015.png"
    0.15
    "images/mym/mouths_normal/100010_05_parts_c014.png"
    0.15
    repeat

image mym_frown1 = WhileSpeaking("mym", "mym_frown1_talking", "mym_frown1_nottalking")


image mym_smile2_nottalking = "images/mym/mouths_normal/100010_05_parts_c024.png"

image mym_smile2_talking:
    "images/mym/mouths_normal/100010_05_parts_c025.png"
    0.15
    "images/mym/mouths_normal/100010_05_parts_c024.png"
    0.15
    repeat

image mym_smile2 = WhileSpeaking("mym", "mym_smile2_talking", "mym_smile2_nottalking")


image mym_frown2_nottalking = "images/mym/mouths_normal/100010_05_parts_c026.png"

image mym_frown2_talking:
    "images/mym/mouths_normal/100010_05_parts_c027.png"
    0.15
    "images/mym/mouths_normal/100010_05_parts_c026.png"
    0.15
    repeat

image mym_frown2 = WhileSpeaking("mym", "mym_frown2_talking", "mym_frown2_nottalking")


image mym_shout1_nottalking = "images/mym/mouths_normal/100010_05_parts_c028.png"

image mym_shout1_talking:
    "images/mym/mouths_normal/100010_05_parts_c029.png"
    0.15
    "images/mym/mouths_normal/100010_05_parts_c028.png"
    0.15
    repeat

image mym_shout1 = WhileSpeaking("mym", "mym_shout1_talking", "mym_shout1_nottalking")


image mym_awkward1_nottalking = "images/mym/mouths_normal/100010_05_parts_c030.png"

image mym_awkward1_talking:
    "images/mym/mouths_normal/100010_05_parts_c031.png"
    0.15
    "images/mym/mouths_normal/100010_05_parts_c030.png"
    0.15
    repeat

image mym_awkward1 = WhileSpeaking("mym", "mym_awkward1_talking", "mym_awkward1_nottalking")


image mym_grimace1_nottalking = "images/mym/mouths_normal/100010_05_parts_c038.png"

image mym_grimace1_talking:
    "images/mym/mouths_normal/100010_05_parts_c039.png"
    0.15
    "images/mym/mouths_normal/100010_05_parts_c038.png"
    0.15
    repeat

image mym_grimace1 = WhileSpeaking("mym", "mym_grimace1_talking", "mym_grimace1_nottalking")


image mym_mutter1_nottalking = "images/mym/mouths_normal/100010_05_parts_c040.png"

image mym_mutter1_talking:
    "images/mym/mouths_normal/100010_05_parts_c041.png"
    0.15
    "images/mym/mouths_normal/100010_05_parts_c040.png"
    0.15
    repeat

image mym_mutter1 = WhileSpeaking("mym", "mym_mutter1_talking", "mym_mutter1_nottalking")


image mym_shout2_nottalking = "images/mym/mouths_normal/100010_05_parts_c042.png"

image mym_shout2_talking:
    "images/mym/mouths_normal/100010_05_parts_c043.png"
    0.15
    "images/mym/mouths_normal/100010_05_parts_c042.png"
    0.15
    repeat

image mym_shout2 = WhileSpeaking("mym", "mym_shout2_talking", "mym_shout2_nottalking")


# 044/045 are the same as 008/009.  Deleted.











    # *Making Mym appear with her leaning sprite (first appearance)*:
    #  -->  show mym_lean with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Myms's (lean) eyes*:
    #  -->  show mym_lean [keyword]
    #  List of eye keywords:
    #     -->  neutral (default), neutral_closed, askance, blush, focused,
    #          pained, relaxed, relaxed2, surprised

    # *Changing Mym's (lean) mouth*:
    #  -->  show mym_lean [keyword]
    #  List of mouth keywords:
    #     -->  smile1 (default), awkward1, smile2, frown1, frown2,
    #          grimace1, mutter1, shout1, shout2

    # *Writing dialogue for Mym (lean)*:
    #  --> mym "[Mym's line here]"

    # *Making Mym (lean) disappear*:
    #  --> hide mym_lean with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)



layeredimage mym_lean:

    always "images/mym/mym_body.png"

    group face:

        # 467/1024, 218/1024:
        pos (0.4560546875, 0.212890625)

        attribute neutral default:
            "mym_lean_neutral_eyes"

        attribute neutral_closed:
            "images/mym/faces/100010_01_parts_c001.png"

        attribute focused:
            "mym_lean_focused_eyes"

        attribute relaxed:
            "mym_lean_relaxed_eyes"

        attribute pained:
            "mym_lean_pained_eyes"

        attribute surprised:
            "mym_lean_surprised_eyes"

        attribute blush:
            "mym_lean_blush_eyes"

        attribute askance:
            "mym_lean_askance_eyes"

        attribute relaxed2:
            "mym_lean_relaxed2_eyes"



    group mouth:

        pos (0.4560546875, 0.212890625)

        attribute smile1 default:
            "mym_lean_smile1"

        attribute frown1:
            "mym_lean_frown1"

        attribute smile2:
            "mym_lean_smile2"

        attribute shout1:
            "mym_lean_shout1"

        attribute frown2:
            "mym_lean_frown2"

        attribute awkward1:
            "mym_lean_awkward1"

        attribute grimace1:
            "mym_lean_grimace1"

        attribute mutter1:
            "mym_lean_mutter1"

        attribute shout2:
            "mym_lean_shout2"



## EYE animations start here.

image mym_lean_neutral_eyes:
    "images/mym/faces/100010_01_parts_c000.png"
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
    "images/mym/faces/100010_01_parts_c001.png"
    0.05
    repeat

# 002 and 003 are the same as 001; deleted.

# 004 / 005 are the same as 000 / 001; deleted.

image mym_lean_focused_eyes:
    "images/mym/faces/100010_01_parts_c006.png"
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
    "images/mym/faces/100010_01_parts_c007.png"
    0.05
    repeat

image mym_lean_relaxed_eyes:
    "images/mym/faces/100010_01_parts_c016.png"
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
    "images/mym/faces/100010_01_parts_c017.png"
    0.05
    repeat

image mym_lean_pained_eyes:
    "images/mym/faces/100010_01_parts_c018.png"
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
    "images/mym/faces/100010_01_parts_c019.png"
    0.05
    repeat

image mym_lean_surprised_eyes:
    "images/mym/faces/100010_01_parts_c020.png"
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
    "images/mym/faces/100010_01_parts_c021.png"
    0.05
    repeat

image mym_lean_blush_eyes:
    "images/mym/faces/100010_01_parts_c022.png"
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
    "images/mym/faces/100010_01_parts_c023.png"
    0.05
    repeat

image mym_lean_askance_eyes:
    "images/mym/faces/100010_01_parts_c032.png"
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
    "images/mym/faces/100010_01_parts_c033.png"
    0.05
    repeat

image mym_lean_relaxed2_eyes:
    "images/mym/faces/100010_01_parts_c034.png"
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
    "images/mym/faces/100010_01_parts_c035.png"
    0.05
    repeat

# 036 / 037 are the same as 006 / 007.  Deleted.

# 038 / 039 are the same as 034 / 035.  Deleted.





# MOUTH animations start here.

image mym_lean_smile1_nottalking = "images/mym/mouths/100010_01_parts_c008.png"

image mym_lean_smile1_talking:
    "images/mym/mouths/100010_01_parts_c009.png"
    0.15
    "images/mym/mouths/100010_01_parts_c008.png"
    0.15
    repeat

image mym_lean_smile1 = WhileSpeaking("mym", "mym_lean_smile1_talking", "mym_lean_smile1_nottalking")


# 010 / 011 are identical to 009 / 010.  Deleted.


# 012 / 013 are identical to 009 / 010.  Deleted.


image mym_lean_frown1_nottalking = "images/mym/mouths/100010_01_parts_c014.png"

image mym_lean_frown1_talking:
    "images/mym/mouths/100010_01_parts_c015.png"
    0.15
    "images/mym/mouths/100010_01_parts_c014.png"
    0.15
    repeat

image mym_lean_frown1 = WhileSpeaking("mym", "mym_lean_frown1_talking", "mym_lean_frown1_nottalking")


image mym_lean_smile2_nottalking = "images/mym/mouths/100010_01_parts_c024.png"

image mym_lean_smile2_talking:
    "images/mym/mouths/100010_01_parts_c025.png"
    0.15
    "images/mym/mouths/100010_01_parts_c024.png"
    0.15
    repeat

image mym_lean_smile2 = WhileSpeaking("mym", "mym_lean_smile2_talking", "mym_lean_smile2_nottalking")


image mym_lean_shout1_nottalking = "images/mym/mouths/100010_01_parts_c026.png"

image mym_lean_shout1_talking:
    "images/mym/mouths/100010_01_parts_c027.png"
    0.15
    "images/mym/mouths/100010_01_parts_c026.png"
    0.15
    repeat

image mym_lean_shout1 = WhileSpeaking("mym", "mym_lean_shout1_talking", "mym_lean_shout1_nottalking")


image mym_lean_frown2_nottalking = "images/mym/mouths/100010_01_parts_c028.png"

image mym_lean_frown2_talking:
    "images/mym/mouths/100010_01_parts_c029.png"
    0.15
    "images/mym/mouths/100010_01_parts_c028.png"
    0.15
    repeat

image mym_lean_frown2 = WhileSpeaking("mym", "mym_lean_frown2_talking", "mym_lean_frown2_nottalking")


image mym_lean_awkward1_nottalking = "images/mym/mouths/100010_01_parts_c030.png"

image mym_lean_awkward1_talking:
    "images/mym/mouths/100010_01_parts_c031.png"
    0.15
    "images/mym/mouths/100010_01_parts_c030.png"
    0.15
    repeat

image mym_lean_awkward1 = WhileSpeaking("mym", "mym_lean_awkward1_talking", "mym_lean_awkward1_nottalking")


image mym_lean_grimace1_nottalking = "images/mym/mouths/100010_01_parts_c040.png"

image mym_lean_grimace1_talking:
    "images/mym/mouths/100010_01_parts_c041.png"
    0.15
    "images/mym/mouths/100010_01_parts_c040.png"
    0.15
    repeat

image mym_lean_grimace1 = WhileSpeaking("mym", "mym_lean_grimace1_talking", "mym_lean_grimace1_nottalking")


image mym_lean_mutter1_nottalking = "images/mym/mouths/100010_01_parts_c042.png"

image mym_lean_mutter1_talking:
    "images/mym/mouths/100010_01_parts_c043.png"
    0.15
    "images/mym/mouths/100010_01_parts_c042.png"
    0.15
    repeat

image mym_lean_mutter1 = WhileSpeaking("mym", "mym_lean_mutter1_talking", "mym_lean_mutter1_nottalking")


image mym_lean_shout2_nottalking = "images/mym/mouths/100010_01_parts_c044.png"

image mym_lean_shout2_talking:
    "images/mym/mouths/100010_01_parts_c045.png"
    0.15
    "images/mym/mouths/100010_01_parts_c044.png"
    0.15
    repeat

image mym_lean_shout2 = WhileSpeaking("mym", "mym_lean_shout2_talking", "mym_lean_shout2_nottalking")



# 046 / 047 are identical to 009 / 010.  Deleted.







# The game starts here.

label mym_character_procedures:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image city_day = "images/backgrounds/Sty_bg_0018_100_00.png"
    scene city_day

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show mym_img with dissolve
    mym "Ah, darling, you're right on time!!!"

    show mym_img neutral smile1
    mym "(neutral smile1) I'm so excited for our date today, darling!!"

    show mym_img closed_neutral smile2
    mym "(closed_neutral smile2) It feels like I can never get you alone lately, so right now I'm the luckiest girl--or dragon--in the world!!"

    show mym_img askance awkward1
    mym "(askance awkward1) I hardlly have any idea what we should do first--there's so many things I've wanted to do with you in town!!"

    show mym_img blush shout1
    mym "(blush shout1) O-Or, if you want to skip right ahead, maybe we could go get a hotel room together, darling!!!"

    show mym_img focused frown1
    mym "(focused frown1) ...Aww, pooh.  I was mostly joking, but you sure know how to kill the chance for romance..."

    show mym_img focused2 frown2
    mym "(focused2 frown2) You know, it wouldn't hurt to give yourself a chance to find love with me, darling.  I know there's a lot going on right now, but..."

    show mym_img pained grimace1
    mym "(pained grimace1) ...I mean, as a human, you have, like, what?  Seventy to eighty years left, at most?  If we don't start dating seriously, you'll be an old fossil by the time you make your mind up."

    show mym_img surprised shout2
    mym "(surprised shout2) Seriously, darling!  I thought humans took things at a quicker pace than dragons, so it's ridiculous to make ME into the one pushing us forward!"

    show mym_img relaxed mutter1
    mym "(relaxed mutter1) (sigh) But I suppose this stubborn, impertinent side of you is something I've grown accustomed to loving as well...  I guess it can't be helped."

    show mym_img closed_neutral shout1
    mym "...Fine, I guess you're not ready to commit yet... but in that case, you'd BETTER buy me something really nice for our shopping date today!  I've roasted people to a crisp for far less!"

    hide mym_img with dissolve



    image store_day = "images/backgrounds/Sty_bg_0061_100_00.png"
    scene store_day with fade

    show mym_lean with dissolve
    mym "Ahhh, I always love this store so much!  I'm sooooo excited to finally shop here with you, darling!"

    show mym_lean neutral smile1
    mym "(neutral smile1) I've been meaning to replace some of my old accessories; it's hard for a girl's fashion to survive white-hot flames, after all!"

    show mym_lean neutral_closed smile2
    mym "(neutral_closed smile2) But with a prince of Alberia fronting the bill, I should be able to get something a little more flame-resilient!  Hee hee!"

    show mym_lean relaxed frown2
    mym "(relaxed frown2) Ok, so... I'm gonna need THIS purse, and THIS shawl, and... ooh, these boots look so sleek and refined!  Wouldn't I just look DIVINE in these?"

    show mym_lean surprised awkward1
    mym "(surprised awkward1) ...Uh... the cost?  Well, I guess I hadn't really budgeted it all in advance, but... um..."

    show mym_lean focused shout1
    mym "(focused shout1) ...Ohhhhh come on, darling, surely you can't be pinching rupies when a girl's heart is at stake, can you?  With all the quests I've been helping you clear, I think I earned a token of your affection!"

    show mym_lean pained grimace1
    mym "(pained grimace1) ...Look, it's not like I don't realize we need to stock up on supplies for the challenges ahead, but I think there's something to be said for living in the moment."

    show mym_lean askance shout2
    mym "(askance shout2) It's just... I first formed a pact with you because you said we could accomplish amazing things together, but lately it's like I can't even do ANYTHING with you!  You're always off on your own."

    show mym_lean relaxed2 frown1
    mym "(relaxed2 frown1) And... I know, I promised recently that I would wait until you could sort out your own feelings, but... when you're so busy all the time, I feel like you've forgotten about that."

    show mym_lean blush mutter1
    mym "(blush mutter1) S-So, maybe I'm just being silly, but... I want something I can hold onto as a representation of that second promise!  Because... we're bound by TWO pacts, you know?"

    show mym_lean askance mutter1
    mym "And... we don't have that long together, so I wanted it to be something I can keep as a memento.  After... you know."

    show mym_lean surprised mutter1
    mym "...O-Oh!  \"Then we should really be shopping at a jeweler's?\"  Wait, does that mean...!"

    show mym_lean blush awkward1
    mym "...We're getting an ENGAGEMENT RING?!?  OH, MY DARLINGG!!!!"

    show mym_lean surprised awkward1
    mym "...O-Oh, not quite?  W-Well, if it's from you, anything would be nice..."

    hide mym_lean with dissolve


    # This goes back to script

    jump testfiles
