
    # Alex Character Procedures File

    # Paste this file into a story if you want to use Notte.  These procedures animate Notte as a speaker.
    # You'll also need to paste THIS line into your actual script above the script label whenever you're using Notte:

define ale = Character("Alex", callback=speaker("ale"))

    # This program assumes that the following folders exist:
    #     -"images/alex"
    #     -"images/alex/faces"
    #     -"images/alex/mouths"
    #     -"images/alex/faces_back"
    #     -"images/alex/mouths_back"

    # "alex_back" procedures are further down below, so you need to scroll!!


    # Alex dynamically blinks and, while speaking, also moves her mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Alex appear*:
    #  -->  show alex with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Alex's eyes*:
    #  -->  show alex [keyword]
    #  List of eye keywords:
    #     -->  relaxed (default), angry, askance, blush, closed_blush, focused, sad, shock,
    #          squint, surprised, closed_sad

    # *Changing Alex's mouth*:
    #  -->  show alex [keyword]
    #  List of mouth keywords:
    #     -->  mutter1 (default), closed_mutter1, frown1, frown2, frown3, grimace1, grimace2,
    #          pout1, shout1, smile1, duchenne1

    # *Writing dialogue for Alex*:
    #  --> ale "[Notte's line here]"

    # *Making Alex disappear*:
    #  --> hide alex with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage alex:

    always "images/alex/alex_body.png"

    group face:

        # 420/1028, 246/1028:

        #slightly off now, try 422/1028, 247/1028
        pos (0.41050, 0.24027)

        attribute relaxed default:
            "alex_relaxed_eyes"

        attribute focused:
            "alex_focused_eyes"

        attribute closed_focused:
            "images/alex/faces/100005_05_parts_c003.png"

        attribute sad:
            "alex_sad_eyes"

        attribute closed_sad:
            "images/alex/faces/100005_05_parts_c009.png"

        attribute angry:
            "alex_angry_eyes"

        attribute surprised:
            "alex_surprised_eyes"

        attribute blush:
            "alex_blush_eyes"

        attribute closed_blush:
            "images/alex/faces/100005_05_parts_c016.png"

        attribute squint:
            "alex_squint_eyes"

        attribute shock:
            "alex_shock_eyes"

        attribute askance:
            "alex_askance_eyes"


    group mouth:

        pos (0.41050, 0.24027)

        attribute mutter1 default:
            "alex_mutter1"

        attribute closed_mutter1:
            "images/alex/mouths/100005_05_parts_c004.png"

        attribute frown1:
            "alex_frown1"

        attribute smile1:
            "alex_smile1"

        attribute grimace1:
            "alex_grimace1"

        attribute frown2:
            "alex_frown2"

        attribute frown3:
            "alex_frown3"

        attribute pout1:
            "alex_pout1"

        attribute shout1:
            "alex_shout1"

        attribute grimace2:
            "alex_grimace2"

        attribute duchenne1:
            "alex_duchenne1"


## EYE animations start here.

image alex_relaxed_eyes:
    "images/alex/faces/100005_05_parts_c000.png"
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
    "images/alex/faces/100005_05_parts_c001.png"
    0.05
    repeat

image alex_focused_eyes:
    "images/alex/faces/100005_05_parts_c002.png"
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
    "images/alex/faces/100005_05_parts_c003.png"
    0.05
    repeat

image alex_sad_eyes:
    "images/alex/faces/100005_05_parts_c009.png"
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
    "images/alex/faces/100005_05_parts_c010.png"
    0.05
    repeat

image alex_angry_eyes:
    "images/alex/faces/100005_05_parts_c011.png"
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
    "images/alex/faces/100005_05_parts_c012.png"
    0.05
    repeat

image alex_surprised_eyes:
    "images/alex/faces/100005_05_parts_c013.png"
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
    "images/alex/faces/100005_05_parts_c014.png"
    0.05
    repeat

image alex_blush_eyes:
    "images/alex/faces/100005_05_parts_c015.png"
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
    "images/alex/faces/100005_05_parts_c016.png"
    0.05
    repeat

image alex_squint_eyes:
    "images/alex/faces/100005_05_parts_c025.png"
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
    "images/alex/faces/100005_05_parts_c026.png"
    0.05
    repeat

image alex_shock_eyes:
    "images/alex/faces/100005_05_parts_c027.png"
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
    "images/alex/faces/100005_05_parts_c028.png"
    0.05
    repeat

image alex_askance_eyes:
    "images/alex/faces/100005_05_parts_c037.png"
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
    "images/alex/faces/100005_05_parts_c038.png"
    0.05
    repeat




# MOUTH animations start here.

image alex_mutter1_nottalking = "images/alex/mouths/100005_05_parts_c004.png"

image alex_mutter1_talking:
    "images/alex/mouths/100005_05_parts_c005.png"
    0.15
    "images/alex/mouths/100005_05_parts_c004.png"
    0.15
    repeat

image alex_mutter1 = WhileSpeaking("ale", "alex_mutter1_talking", "alex_mutter1_nottalking")


image alex_frown1_nottalking = "images/alex/mouths/100005_05_parts_c007.png"

image alex_frown1_talking:
    "images/alex/mouths/100005_05_parts_c008.png"
    0.15
    "images/alex/mouths/100005_05_parts_c007.png"
    0.15
    repeat

image alex_frown1 = WhileSpeaking("ale", "alex_frown1_talking", "alex_frown1_nottalking")


image alex_smile1_nottalking = "images/alex/mouths/100005_05_parts_c017.png"

image alex_smile1_talking:
    "images/alex/mouths/100005_05_parts_c018.png"
    0.15
    "images/alex/mouths/100005_05_parts_c017.png"
    0.15
    repeat

image alex_smile1 = WhileSpeaking("ale", "alex_smile1_talking", "alex_smile1_nottalking")



image alex_duchenne1_nottalking = "images/alex/mouths/100005_05_parts_c018.png"

image alex_duchenne1_talking:
    "images/alex/mouths/100005_05_parts_c017.png"
    0.15
    "images/alex/mouths/100005_05_parts_c018.png"
    0.15
    repeat

image alex_duchenne1 = WhileSpeaking("ale", "alex_duchenne1_talking", "alex_duchenne1_nottalking")




image alex_grimace1_nottalking = "images/alex/mouths/100005_05_parts_c019.png"

image alex_grimace1_talking:
    "images/alex/mouths/100005_05_parts_c020.png"
    0.15
    "images/alex/mouths/100005_05_parts_c019.png"
    0.15
    repeat

image alex_grimace1 = WhileSpeaking("ale", "alex_grimace1_talking", "alex_grimace1_nottalking")


image alex_frown2_nottalking = "images/alex/mouths/100005_05_parts_c021.png"

image alex_frown2_talking:
    "images/alex/mouths/100005_05_parts_c022.png"
    0.15
    "images/alex/mouths/100005_05_parts_c021.png"
    0.15
    repeat

image alex_frown2 = WhileSpeaking("ale", "alex_frown2_talking", "alex_frown2_nottalking")


image alex_frown3_nottalking = "images/alex/mouths/100005_05_parts_c023.png"

image alex_frown3_talking:
    "images/alex/mouths/100005_05_parts_c024.png"
    0.15
    "images/alex/mouths/100005_05_parts_c023.png"
    0.15
    repeat

image alex_frown3 = WhileSpeaking("ale", "alex_frown3_talking", "alex_frown3_nottalking")


image alex_pout1_nottalking = "images/alex/mouths/100005_05_parts_c029.png"

image alex_pout1_talking:
    "images/alex/mouths/100005_05_parts_c030.png"
    0.15
    "images/alex/mouths/100005_05_parts_c029.png"
    0.15
    repeat

image alex_pout1 = WhileSpeaking("ale", "alex_pout1_talking", "alex_pout1_nottalking")


# 031/032 and 035/036 are the same as 004/005


image alex_shout1_nottalking = "images/alex/mouths/100005_05_parts_c033.png"

image alex_shout1_talking:
    "images/alex/mouths/100005_05_parts_c034.png"
    0.15
    "images/alex/mouths/100005_05_parts_c033.png"
    0.15
    repeat

image alex_shout1 = WhileSpeaking("ale", "alex_shout1_talking", "alex_shout1_nottalking")


image alex_grimace2_nottalking = "images/alex/mouths/100005_05_parts_c039.png"

image alex_grimace2_talking:
    "images/alex/mouths/100005_05_parts_c040.png"
    0.15
    "images/alex/mouths/100005_05_parts_c039.png"
    0.15
    repeat

image alex_grimace2 = WhileSpeaking("ale", "alex_grimace2_talking", "alex_grimace2_nottalking")




    # *Making Alex appear with her back*:
    #  -->  show alex_back with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Alex's (back) eyes*:
    #  -->  show alex_back [keyword]
    #  List of eye keywords:
    #     -->  relaxed (default), angry, blush, closed_blush, focused, closed_focused,
    #          sad, shock, squint, surprised

    # *Changing Alex's (back) mouth*:
    #  -->  show alex_back [keyword]
    #  List of mouth keywords:
    #     -->  mutter1 (default), frown1, frown2, grimace1,
    #          pout1, shout1, smile1,

    # *Writing dialogue for Alex (back)*:
    #  --> ale "[Alex's line here]"

    # *Making Alex (back) disappear*:
    #  --> hide alex_back with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)



layeredimage alex_back:

    always "images/alex/alex_body_back_crop.png"

    group face:

        # orig 427/1028, 238/1028:

        # NOW 308/1028, 58/1028
        # slightly off, try 310/1028, 59/1028
        pos (0.30156, 0.05739)

        attribute relaxed default:
            "alex_back_relaxed_eyes"

        attribute focused:
            "alex_back_focused_eyes"

        attribute closed_focused:
            "images/alex/faces_back/100005_01_parts_c004.png"

        attribute sad:
            "alex_back_sad_eyes"

        attribute angry:
            "alex_back_angry_eyes"

        attribute surprised:
            "alex_back_surprised_eyes"

        attribute blush:
            "alex_back_blush_eyes"

        attribute closed_blush:
            "images/alex/faces_back/100005_01_parts_c017.png"

        attribute squint:
            "alex_back_squint_eyes"

        attribute shock:
            "alex_back_shock_eyes"


    group mouth:

        pos (0.30156, 0.05739)

        attribute mutter1 default:
            "alex_back_mutter1"

        attribute frown1:
            "alex_back_frown1"

        attribute smile1:
            "alex_back_smile1"

        attribute grimace1:
            "alex_back_grimace1"

        attribute frown2:
            "alex_back_frown2"

        attribute pout1:
            "alex_back_pout1"

        attribute shout1:
            "alex_back_shout1"


## EYE animations start here.

image alex_back_relaxed_eyes:
    "images/alex/faces_back/100005_01_parts_c000.png"
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
    "images/alex/faces_back/100005_01_parts_c001.png"
    0.05
    repeat

image alex_back_focused_eyes:
    "images/alex/faces_back/100005_01_parts_c003.png"
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
    "images/alex/faces_back/100005_01_parts_c004.png"
    0.05
    repeat

image alex_back_sad_eyes:
    "images/alex/faces_back/100005_01_parts_c010.png"
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
    "images/alex/faces_back/100005_01_parts_c011.png"
    0.05
    repeat

image alex_back_angry_eyes:
    "images/alex/faces_back/100005_01_parts_c012.png"
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
    "images/alex/faces_back/100005_01_parts_c013.png"
    0.05
    repeat

image alex_back_surprised_eyes:
    "images/alex/faces_back/100005_01_parts_c014.png"
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
    "images/alex/faces_back/100005_01_parts_c015.png"
    0.05
    repeat

image alex_back_blush_eyes:
    "images/alex/faces_back/100005_01_parts_c016.png"
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
    "images/alex/faces_back/100005_01_parts_c017.png"
    0.05
    repeat

image alex_back_squint_eyes:
    "images/alex/faces_back/100005_01_parts_c024.png"
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
    "images/alex/faces_back/100005_01_parts_c025.png"
    0.05
    repeat

image alex_back_shock_eyes:
    "images/alex/faces_back/100005_01_parts_c026.png"
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
    "images/alex/faces_back/100005_01_parts_c027.png"
    0.05
    repeat




# MOUTH animations start here.

image alex_back_mutter1_nottalking = "images/alex/mouths_back/100005_01_parts_c005.png"

image alex_back_mutter1_talking:
    "images/alex/mouths_back/100005_01_parts_c006.png"
    0.15
    "images/alex/mouths_back/100005_01_parts_c005.png"
    0.15
    repeat

image alex_back_mutter1 = WhileSpeaking("ale", "alex_back_mutter1_talking", "alex_back_mutter1_nottalking")


image alex_back_frown1_nottalking = "images/alex/mouths_back/100005_01_parts_c008.png"

image alex_back_frown1_talking:
    "images/alex/mouths_back/100005_01_parts_c009.png"
    0.15
    "images/alex/mouths_back/100005_01_parts_c008.png"
    0.15
    repeat

image alex_back_frown1 = WhileSpeaking("ale", "alex_back_frown1_talking", "alex_back_frown1_nottalking")


image alex_back_smile1_nottalking = "images/alex/mouths_back/100005_01_parts_c018.png"

image alex_back_smile1_talking:
    "images/alex/mouths_back/100005_01_parts_c019.png"
    0.15
    "images/alex/mouths_back/100005_01_parts_c018.png"
    0.15
    repeat

image alex_back_smile1 = WhileSpeaking("ale", "alex_back_smile1_talking", "alex_back_smile1_nottalking")


image alex_back_grimace1_nottalking = "images/alex/mouths_back/100005_01_parts_c020.png"

image alex_back_grimace1_talking:
    "images/alex/mouths_back/100005_01_parts_c021.png"
    0.15
    "images/alex/mouths_back/100005_01_parts_c020.png"
    0.15
    repeat

image alex_back_grimace1 = WhileSpeaking("ale", "alex_back_grimace1_talking", "alex_back_grimace1_nottalking")


image alex_back_frown2_nottalking = "images/alex/mouths_back/100005_01_parts_c023.png"

image alex_back_frown2_talking:
    "images/alex/mouths_back/100005_01_parts_c022.png"
    0.15
    "images/alex/mouths_back/100005_01_parts_c023.png"
    0.15
    repeat

image alex_back_frown2 = WhileSpeaking("ale", "alex_back_frown2_talking", "alex_back_frown2_nottalking")


image alex_back_pout1_nottalking = "images/alex/mouths_back/100005_01_parts_c028.png"

image alex_back_pout1_talking:
    "images/alex/mouths_back/100005_01_parts_c029.png"
    0.15
    "images/alex/mouths_back/100005_01_parts_c028.png"
    0.15
    repeat

image alex_back_pout1 = WhileSpeaking("ale", "alex_back_pout1_talking", "alex_back_pout1_nottalking")


# 031/032 and 035/036 are the same as 004/005


image alex_back_shout1_nottalking = "images/alex/mouths_back/100005_01_parts_c032.png"

image alex_back_shout1_talking:
    "images/alex/mouths_back/100005_01_parts_c033.png"
    0.15
    "images/alex/mouths_back/100005_01_parts_c032.png"
    0.15
    repeat

image alex_back_shout1 = WhileSpeaking("ale", "alex_back_shout1_talking", "alex_back_shout1_nottalking")









# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

transform alex_back_pos:
    #118, 180 ->> 118/1028 ?

    # no, try (118 + (770/2))/1028
    xalign 0.48930
    yalign 1.0

transform alex_back_ambush_pos:
    xalign 0.0
    yalign 1.0

transform alex_back_ambush_to_regular:
    xalign 0.0
    yalign 1.0
    linear 1.0 xalign 0.48930 yalign 1.0








# The game starts here.

label alex_character_procedures:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image bedroom_night = "images/backgrounds/Sty_bg_0049_300_00.png"
    scene bedroom_night

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show alex with dissolve
    ale "Your Highness, there's something I wish to discuss with you."
    ale "Now that I'm a part of your inner circle, I'm privy to a host of sensitive information that could greatly endanger our comrades if it slipped."

    show alex askance grimace2
    ale "(askance grimace2) And I'm sure I don't have to remind you of the methods my former employers have used to gain information from others in the past..."

    show alex focused frown1
    ale "That's why I need to gain as much control over my bodily and facial motions as possible.  Even a small twitch at the wrong moment under torture could leak a sensitive piece of information to our enemies."

    show alex askance frown3
    ale "(frown3) ...You say you're going to make sure I'm never in that position?..."

    show alex askance smile1
    ale "...I don't know if I'll ever be able to be that confident, but... when you say it, it somehow reassures me a bit..."

    show alex focused frown1
    ale "In any case, I've made up my mind.  In order to not be a liability to you, I want you to make sure I can maintain composure from all angles and control my facial expressions."
    ale "If you're ok doing so, I'd like you to check my physiological responses from a variety of angles while I change my expression."

    show alex relaxed mutter1
    ale "I'll start with a 'relaxed' expression and a mutter ('mutter1') that's a restrained as possible.  If there's any discrepancies you notice, please let me know."

    hide alex
    show alex_back relaxed mutter1 at alex_back_pos
    ale "And please also check the same expression ('relaxed, mutter1') from the back to make sure there aren't any wayward twitches in my neck or back muscles."
    hide alex_back


    show alex angry frown1
    ale "Now I'll switch to an 'angry' expression and a frown ('frown1').  Again, let me know about any discrepancies."

    hide alex
    show alex_back angry frown1 at alex_back_pos
    ale "And please also check the same expression ('angry, frown1') from the back to make sure there aren't any wayward twitches in my neck or back muscles."
    hide alex_back


    show alex blush frown2
    ale "Now I'll try to make myself 'blush' and also have a second frown ('frown2').  Altering the circulation in my face is an important skill.  Again, let me know about any discrepancies."

    hide alex
    show alex_back blush frown2 at alex_back_pos
    ale "And please also check the same expression ('blush, frown2') from the back to make sure there aren't any wayward twitches in my neck or back muscles."
    hide alex_back


    show alex focused grimace1
    ale "Now I'll try a 'focused' expression and a grimace ('grimace1').  Again, let me know about any discrepancies."

    hide alex
    show alex_back focused grimace1 at alex_back_pos
    ale "And please also check the same expression ('focused, grimace1') from the back to make sure there aren't any wayward twitches in my neck or back muscles."
    hide alex_back


    show alex sad pout1
    ale "Now I'll try a 'sad' expression and a pout ('pout1').  Again, let me know about any discrepancies."

    hide alex
    show alex_back sad pout1 at alex_back_pos
    ale "And please also check the same expression ('sad, pout1') from the back to make sure there aren't any wayward twitches in my neck or back muscles."
    hide alex_back


    show alex shock shout1
    ale "It's also important to be able to maintain composure at high speaking volume so... I'm going to try a shocked ('shock') expression and a shout ('shout1')!!!  Sorry about this, let me know if you see anything off!!"

    hide alex
    show alex_back shock shout1 at alex_back_pos
    ale "And also do the same thing from the back and check my expression ('shock, shout1')!  Make sure there's nothing out of order!!"
    hide alex_back


    show alex squint smile1
    ale "...I'm really sorry about subjecting you to that.  I promise I'm almost done.  Just check this squinting ('squint') expression with a smile ('smile1') and make sure it's all fairly composed."

    hide alex
    show alex_back squint smile1 at alex_back_pos
    ale "And... also do the same thing from the back, please, like usual ('squint, smile1')."
    hide alex_back


    show alex surprised frown1
    ale "And last but not least, I want to be able to convincingly feign surprise if given information that I said I didn't know.  Does this 'surprised' expression look real enough?"

    hide alex
    show alex_back surprised frown1 at alex_back_pos
    ale "Even from the back ('surprised')?  If nothing's off, that probably means I have the required level of facial control to pull it off."
    hide alex_back

    show alex relaxed smile1
    ale "...Well, I think that's a pretty exhaustive routine.  If you think everything's in order, then that puts me at ease..."

    show alex blush smile1
    ale "...even if it meant I had to put on a somewhat, erm, embarrassing display back there...  Thank goodness Elisanne wasn't around..."

    show alex surprised pout1
    ale "...\"Were you making your face blush again intentionally just now?\"  ...Oh no, perhaps I still have a little ways to go on my facial control..."

    hide alex with dissolve

    # This goes back to script

    jump testfiles
