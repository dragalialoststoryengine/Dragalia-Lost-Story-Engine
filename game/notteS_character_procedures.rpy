
    # Summer Notte Character Procedures File

    # Paste this file into a story if you want to use Summer Notte.  These procedures animate Summer Notte as a speaker.
    # You'll also need to paste THIS line into your actual script above the script label whenever you're using Summer Notte:

define snott = Character("Notte", callback=speaker("snott"))

    # This program assumes that the following folders exist:
    #     -"images/notte_summer"
    #     -"images/notte_summer/faces"
    #     -"images/notte_summer/mouths"

    # Summer Notte dynamically blinks and, while speaking, also moves her mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Summer Notte appear*:
    #  -->  show notte_summer with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Summer Notte's eyes*:
    #  -->  show notte_summer [keyword]
    #  List of eye keywords:
    #     -->  relaxed (default), closed_relaxed, relaxed2, closed_relaxed2, focused,
    #          sad, closed_sad, sad2, shock, surprised, blush, closed_blush

    # *Changing Summer Notte's mouth*:
    #  -->  show notte_summer [keyword]
    #  List of mouth keywords:
    #     -->  smile1 (default), smile2, frown1, frown2, sweat_frown1,
    #          shout1, shout2, closed_smile1

    # *Writing dialogue for Summer Notte*:
    #  --> snott "[Summer Notte's line here]"

    # *Making Summer Notte disappear*:
    #  --> hide notte_summer with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage notte_summer:

    always "images/notte_summer/notte_summer_body.png"

    group face:

        # 441/1024, 209/1024:
        pos (0.43066, 0.20410)

        attribute relaxed default:
            "notte_summer_relaxed_eyes"

        attribute closed_relaxed:
            "images/notte_summer/faces/100007_06_parts_c001.png"

        attribute focused:
            "notte_summer_focused_eyes"

        attribute relaxed2:
            "notte_summer_relaxed2_eyes"

        attribute closed_relaxed2:
            "images/notte_summer/faces/100007_06_parts_c008.png"

        attribute sad:
            "notte_summer_sad_eyes"

        attribute closed_sad:
            "images/notte_summer/faces/100007_06_parts_c010.png"

        attribute surprised:
            "notte_summer_surprised_eyes"

        attribute blush:
            "notte_summer_blush_eyes"

        attribute closed_blush:
            "images/notte_summer/faces/100007_06_parts_c013.png"

        attribute sad2:
            "notte_summer_sad2_eyes"

        attribute shock:
            "notte_summer_shock_eyes"


    group mouth:

        pos (0.43066, 0.20410)

        attribute smile1 default:
            "notte_summer_smile1"

        attribute closed_smile1:
            "notte_summer_smile1_nottalking"

        attribute frown1:
            "notte_summer_frown1"

        attribute sweat_frown1:
            "notte_summer_sweat_frown1"

        attribute shout1:
            "notte_summer_shout1"

        attribute smile2:
            "notte_summer_smile2"

        attribute frown2:
            "notte_summer_frown2"

        attribute shout2:
            "notte_summer_shout2"


## EYE animations start here.

image notte_summer_relaxed_eyes:
    "images/notte_summer/faces/100007_06_parts_c000.png"
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
    "images/notte_summer/faces/100007_06_parts_c001.png"
    0.05
    repeat

image notte_summer_focused_eyes:
    "images/notte_summer/faces/100007_06_parts_c002.png"
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
    "images/notte_summer/faces/100007_06_parts_c003.png"
    0.05
    repeat

image notte_summer_relaxed2_eyes:
    "images/notte_summer/faces/100007_06_parts_c000.png"
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
    "images/notte_summer/faces/100007_06_parts_c008.png"
    0.05
    repeat

image notte_summer_sad_eyes:
    "images/notte_summer/faces/100007_06_parts_c009.png"
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
    "images/notte_summer/faces/100007_06_parts_c010.png"
    0.05
    repeat

image notte_summer_surprised_eyes:
    "images/notte_summer/faces/100007_06_parts_c011.png"
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
    "images/notte_summer/faces/100007_06_parts_c001.png"
    0.05
    repeat

image notte_summer_blush_eyes:
    "images/notte_summer/faces/100007_06_parts_c012.png"
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
    "images/notte_summer/faces/100007_06_parts_c013.png"
    0.05
    repeat

image notte_summer_sad2_eyes:
    "images/notte_summer/faces/100007_06_parts_c020.png"
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
    "images/notte_summer/faces/100007_06_parts_c021.png"
    0.05
    repeat

image notte_summer_shock_eyes:
    "images/notte_summer/faces/100007_06_parts_c022.png"
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
    "images/notte_summer/faces/100007_06_parts_c023.png"
    0.05
    repeat


# MOUTH animations start here.

image notte_summer_smile1_nottalking = "images/notte_summer/mouths/100007_06_parts_c004.png"

image notte_summer_smile1_talking:
    "images/notte_summer/mouths/100007_06_parts_c005.png"
    0.15
    "images/notte_summer/mouths/100007_06_parts_c004.png"
    0.15
    repeat

image notte_summer_smile1 = WhileSpeaking("snott", "notte_summer_smile1_talking", "notte_summer_smile1_nottalking")


image notte_summer_frown1_nottalking = "images/notte_summer/mouths/100007_06_parts_c006.png"

image notte_summer_frown1_talking:
    "images/notte_summer/mouths/100007_06_parts_c007.png"
    0.15
    "images/notte_summer/mouths/100007_06_parts_c006.png"
    0.15
    repeat

image notte_summer_frown1 = WhileSpeaking("snott", "notte_summer_frown1_talking", "notte_summer_frown1_nottalking")


image notte_summer_sweat_frown1_nottalking = "images/notte_summer/mouths/100007_06_parts_c014.png"

image notte_summer_sweat_frown1_talking:
    "images/notte_summer/mouths/100007_06_parts_c015.png"
    0.15
    "images/notte_summer/mouths/100007_06_parts_c014.png"
    0.15
    repeat

image notte_summer_sweat_frown1 = WhileSpeaking("snott", "notte_summer_sweat_frown1_talking", "notte_summer_sweat_frown1_nottalking")


image notte_summer_shout1_nottalking = "images/notte_summer/mouths/100007_06_parts_c016.png"

image notte_summer_shout1_talking:
    "images/notte_summer/mouths/100007_06_parts_c017.png"
    0.15
    "images/notte_summer/mouths/100007_06_parts_c016.png"
    0.15
    repeat

image notte_summer_shout1 = WhileSpeaking("snott", "notte_summer_shout1_talking", "notte_summer_shout1_nottalking")


image notte_summer_smile2_nottalking = "images/notte_summer/mouths/100007_06_parts_c018.png"

image notte_summer_smile2_talking:
    "images/notte_summer/mouths/100007_06_parts_c019.png"
    0.15
    "images/notte_summer/mouths/100007_06_parts_c018.png"
    0.15
    repeat

image notte_summer_smile2 = WhileSpeaking("snott", "notte_summer_smile2_talking", "notte_summer_smile2_nottalking")


image notte_summer_frown2_nottalking = "images/notte_summer/mouths/100007_06_parts_c025.png"

image notte_summer_frown2_talking:
    "images/notte_summer/mouths/100007_06_parts_c026.png"
    0.15
    "images/notte_summer/mouths/100007_06_parts_c025.png"
    0.15
    repeat

image notte_summer_frown2 = WhileSpeaking("snott", "notte_summer_frown2_talking", "notte_summer_frown2_nottalking")


image notte_summer_shout2_nottalking = "images/notte_summer/mouths/100007_06_parts_c029.png"

image notte_summer_shout2_talking:
    "images/notte_summer/mouths/100007_06_parts_c030.png"
    0.15
    "images/notte_summer/mouths/100007_06_parts_c029.png"
    0.15
    repeat

image notte_summer_shout2 = WhileSpeaking("snott", "notte_summer_shout2_talking", "notte_summer_shout2_nottalking")







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

label notteS_character_procedures:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image sky = "images/backgrounds/Sty_bg_0015_100_00.png"
    scene sky at middle
    image beach = "images/backgrounds/Sty_bg_0078_100_03_front.png"
    show beach at middle

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show notte_summer closed_relaxed smile1 with dissolve
    snott "Ahhhhh~"
    snott "Nothin' like chillin' out in the sun~\n(closed_relaxed smile1)"

    show notte_summer relaxed smile2
    snott "Oh, hey Euden!\n(relaxed smile2)"

    show notte_summer surprised frown1
    snott "Say, has Ranzal finished his grilling and stuff?\n(surprised frown1)"

    show notte_summer sad
    snott "Aw man! He's still not done?\n(sad)"

    show notte_summer closed_sad shout1
    snott "Because man am I starving!\n(closed_sad shout1)"

    show notte_summer shock frown1
    snott "It’s just tough work playing all day, ya know?\n(shock)"

    show notte_summer blush
    snott "You can't just go to the beach in a bikini and call it good!\n(blush)"

    show notte_summer frown2
    snott "Speaking of, we should get some swimsuits for my bigger forms!\n(frown2)"

    show notte_summer closed_blush smile1
    snott "Then I can splash around with everyone!\n(closed_blush)"

    show notte_summer sad frown2
    snott "I mean, I already can, but it’s basically always a wipeout for me."

    show notte_summer focused sweat_frown1
    snott "And let me tell you, fairy wings do NOT work great when covered in water!\n(focused sweat_frown1)"

    show notte_summer relaxed frown1
    snott "Oh, before I forget, do you want to see the sandcastle I made?"

    show notte_summer relaxed2 smile1
    snott "It should be right over here!\n(relaxed2)"

    show notte_summer smile2
    snott "Pretty sweet work, wouldn’t ya say?"

    show notte_summer focused
    snott "Now I can be the ruler of Castle Notte!"

    show notte_summer closed_relaxed2 smile1
    snott "It’s like the Halidom, but with seashells.\n(closed_relaxed2)"

    show notte_summer surprised shout2
    snott "Oh my- You even brought a flag?!\n(shout2)"

    show notte_summer sad2 smile1
    snott "Awwww~! You're too kind, Euden!\n(sad2)"

    show notte_summer closed_smile1
    snott "*It just wouldn't be a perfect vacation without you guys!*\n(closed_smile1)"



    hide notte_meta with dissolve

    # This goes back to script

    jump testfiles
