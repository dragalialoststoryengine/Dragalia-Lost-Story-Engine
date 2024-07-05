
    # Valentine Chelsea Character Procedures File

    # Paste this file into a story if you want to use Chelsea's Valentine's Day alt.  These procedures animate VChelsea as a speaker.
    # You'll also need to paste THIS line into your actual script above the script label whenever you're using VChelsea:

define vchel = Character("Chelsea", callback=speaker("vchel"))

    # This program assumes that the following folders exist:
    #     -"images/chelsea_valentine"
    #     -"images/chelsea_valentine/faces"
    #     -"images/chelsea_valentine/mouths"

    # VChelsea dynamically blinks and, while speaking, also moves her mouth along with the text scroll.

    # FUNCTIONS:

    # *Making VChelsea appear*:
    #  -->  show vchelsea with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing VChelsea's eyes*:
    #  -->  show vchelsea [keyword]
    #  List of eye keywords:
    #     -->  relaxed (default), angry, blush, cry, flinch, focused, focused_closed
    #           neutral, serious, serious_closed, surprised, wide

    # *Changing VChelsea's mouth*:
    #  -->  show vchelsea [keyword]
    #  List of mouth keywords:
    #     -->  drool1 (default), drool2, frown1, frown2, mutter1, pout1,
    #          grimace1, shout1, smile1, smile2, smile3, smile4, smile5

    # *Writing dialogue for VChelsea*:
    #  --> vchel "[VChelsea's line here]"

    # *Making VChelsea disappear*:
    #  --> hide vchelsea with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage vchelsea:

    always "images/chelsea_valentine/chelsea_valentine_body.png"

    group face:

        # 443/1028, 265/1028:
        pos (0.43093, 0.25778)

        attribute relaxed default:
            "vchelsea_relaxed_eyes"

        attribute serious:
            "vchelsea_serious_eyes"

        attribute serious_closed:
            "vchelsea_serious_closed_eyes"

        attribute focused:
            "vchelsea_focused_eyes"

        attribute focused_closed:
            "vchelsea_focused_closed_eyes"

        attribute flinch:
            "vchelsea_flinch_eyes"

        attribute wide:
            "vchelsea_wide_eyes"

        attribute blush:
            "vchelsea_blush_eyes"

        attribute cry:
            "vchelsea_cry_eyes"

        attribute angry:
            "vchelsea_angry_eyes"

        attribute neutral:
            "vchelsea_neutral_eyes"

        attribute surprised:
            "vchelsea_surprised_eyes"

    group mouth:

        pos (0.43093, 0.25778)

        attribute drool1 default:
            "vchelsea_drool1"

        attribute smile1:
            "vchelsea_smile1"

        attribute smile2:
            "vchelsea_smile2"

        attribute smile3:
            "vchelsea_smile3"

        attribute smile4:
            "vchelsea_smile4"

        attribute grimace1:
            "vchelsea_grimace1"

        attribute frown1:
            "vchelsea_frown1"

        attribute drool2:
            "vchelsea_drool2"

        attribute frown2:
            "vchelsea_frown2"

        attribute shout1:
            "vchelsea_shout1"

        attribute mutter1:
            "vchelsea_mutter1"

        attribute pout1:
            "vchelsea_pout1"

        attribute smile5:
            "vchelsea_smile5"

## EYE animations start here.

image vchelsea_relaxed_eyes:
    "images/chelsea_valentine/faces/110342_03_parts_c000.png"
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
    "images/chelsea_valentine/faces/110342_03_parts_c001.png"
    0.05
    repeat

image vchelsea_serious_eyes:
    "images/chelsea_valentine/faces/110342_03_parts_c004.png"
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
    "images/chelsea_valentine/faces/110342_03_parts_c005.png"
    0.05
    repeat

image vchelsea_serious_closed_eyes:
    "images/chelsea_valentine/faces/110342_03_parts_c005.png"

image vchelsea_focused_eyes:
    "images/chelsea_valentine/faces/110342_03_parts_c014.png"
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
    "images/chelsea_valentine/faces/110342_03_parts_c015.png"
    0.05
    repeat

image vchelsea_focused_closed_eyes:
    "images/chelsea_valentine/faces/110342_03_parts_c015.png"

image vchelsea_flinch_eyes:
    "images/chelsea_valentine/faces/110342_03_parts_c016.png"
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
    "images/chelsea_valentine/faces/110342_03_parts_c017.png"
    0.05
    repeat

image vchelsea_wide_eyes:
    "images/chelsea_valentine/faces/110342_03_parts_c018.png"
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
    "images/chelsea_valentine/faces/110342_03_parts_c019.png"
    0.05
    repeat

image vchelsea_blush_eyes:
    "images/chelsea_valentine/faces/110342_03_parts_c020.png"
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
    "images/chelsea_valentine/faces/110342_03_parts_c021.png"
    0.05
    repeat

image vchelsea_cry_eyes:
    "images/chelsea_valentine/faces/110342_03_parts_c030.png"
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
    "images/chelsea_valentine/faces/110342_03_parts_c031.png"
    0.05
    repeat

image vchelsea_angry_eyes:
    "images/chelsea_valentine/faces/110342_03_parts_c032.png"
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
    "images/chelsea_valentine/faces/110342_03_parts_c033.png"
    0.05
    repeat

image vchelsea_neutral_eyes:
    "images/chelsea_valentine/faces/110342_03_parts_c040.png"
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
    "images/chelsea_valentine/faces/110342_03_parts_c041.png"
    0.05
    repeat

# 042 and 043 are the same as 000 / 001.

image vchelsea_surprised_eyes:
    "images/chelsea_valentine/faces/110342_03_parts_c044.png"
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
    "images/chelsea_valentine/faces/110342_03_parts_c045.png"
    0.05
    repeat


# MOUTH animations start here.

image vchelsea_drool1_nottalking = "images/chelsea_valentine/mouths/110342_03_parts_c007.png"

image vchelsea_drool1_talking:
    "images/chelsea_valentine/mouths/110342_03_parts_c007.png"
    0.15
    "images/chelsea_valentine/mouths/110342_03_parts_c006.png"
    0.15
    repeat

image vchelsea_drool1 = WhileSpeaking("vchel", "vchelsea_drool1_talking", "vchelsea_drool1_nottalking")


image vchelsea_smile1_nottalking = "images/chelsea_valentine/mouths/110342_03_parts_c008.png"

image vchelsea_smile1_talking:
    "images/chelsea_valentine/mouths/110342_03_parts_c009.png"
    0.15
    "images/chelsea_valentine/mouths/110342_03_parts_c008.png"
    0.15
    repeat

image vchelsea_smile1 = WhileSpeaking("vchel", "vchelsea_smile1_talking", "vchelsea_smile1_nottalking")


image vchelsea_smile2_nottalking = "images/chelsea_valentine/mouths/110342_03_parts_c010.png"

image vchelsea_smile2_talking:
    "images/chelsea_valentine/mouths/110342_03_parts_c011.png"
    0.15
    "images/chelsea_valentine/mouths/110342_03_parts_c010.png"
    0.15
    repeat

image vchelsea_smile2 = WhileSpeaking("vchel", "vchelsea_smile2_talking", "vchelsea_smile2_nottalking")


image vchelsea_smile3_nottalking = "images/chelsea_valentine/mouths/110342_03_parts_c012.png"

image vchelsea_smile3_talking:
    "images/chelsea_valentine/mouths/110342_03_parts_c013.png"
    0.15
    "images/chelsea_valentine/mouths/110342_03_parts_c012.png"
    0.15
    repeat

image vchelsea_smile3 = WhileSpeaking("vchel", "vchelsea_smile3_talking", "vchelsea_smile3_nottalking")


image vchelsea_smile4_nottalking = "images/chelsea_valentine/mouths/110342_03_parts_c022.png"

image vchelsea_smile4_talking:
    "images/chelsea_valentine/mouths/110342_03_parts_c023.png"
    0.15
    "images/chelsea_valentine/mouths/110342_03_parts_c022.png"
    0.15
    repeat

image vchelsea_smile4 = WhileSpeaking("vchel", "vchelsea_smile4_talking", "vchelsea_smile4_nottalking")


image vchelsea_grimace1_nottalking = "images/chelsea_valentine/mouths/110342_03_parts_c024.png"

image vchelsea_grimace1_talking:
    "images/chelsea_valentine/mouths/110342_03_parts_c025.png"
    0.15
    "images/chelsea_valentine/mouths/110342_03_parts_c024.png"
    0.15
    repeat

image vchelsea_grimace1 = WhileSpeaking("vchel", "vchelsea_grimace1_talking", "vchelsea_grimace1_nottalking")


image vchelsea_frown1_nottalking = "images/chelsea_valentine/mouths/110342_03_parts_c026.png"

image vchelsea_frown1_talking:
    "images/chelsea_valentine/mouths/110342_03_parts_c027.png"
    0.15
    "images/chelsea_valentine/mouths/110342_03_parts_c026.png"
    0.15
    repeat

image vchelsea_frown1 = WhileSpeaking("vchel", "vchelsea_frown1_talking", "vchelsea_frown1_nottalking")


image vchelsea_drool2_nottalking = "images/chelsea_valentine/mouths/110342_03_parts_c029.png"

image vchelsea_drool2_talking:
    "images/chelsea_valentine/mouths/110342_03_parts_c029.png"
    0.15
    "images/chelsea_valentine/mouths/110342_03_parts_c028.png"
    0.15
    repeat

image vchelsea_drool2 = WhileSpeaking("vchel", "vchelsea_drool2_talking", "vchelsea_drool2_nottalking")


image vchelsea_frown2_nottalking = "images/chelsea_valentine/mouths/110342_03_parts_c034.png"

image vchelsea_frown2_talking:
    "images/chelsea_valentine/mouths/110342_03_parts_c035.png"
    0.15
    "images/chelsea_valentine/mouths/110342_03_parts_c034.png"
    0.15
    repeat

image vchelsea_frown2 = WhileSpeaking("vchel", "vchelsea_frown2_talking", "vchelsea_frown2_nottalking")


image vchelsea_shout1_nottalking = "images/chelsea_valentine/mouths/110342_03_parts_c036.png"

image vchelsea_shout1_talking:
    "images/chelsea_valentine/mouths/110342_03_parts_c037.png"
    0.15
    "images/chelsea_valentine/mouths/110342_03_parts_c036.png"
    0.15
    repeat

image vchelsea_shout1 = WhileSpeaking("vchel", "vchelsea_shout1_talking", "vchelsea_shout1_nottalking")

# 038 / 039 are the same as 010 / 011.  Deleted.

image vchelsea_mutter1_nottalking = "images/chelsea_valentine/mouths/110342_03_parts_c046.png"

image vchelsea_mutter1_talking:
    "images/chelsea_valentine/mouths/110342_03_parts_c046.png"
    0.15
    "images/chelsea_valentine/mouths/110342_03_parts_c047.png"
    0.15
    repeat

image vchelsea_mutter1 = WhileSpeaking("vchel", "vchelsea_mutter1_talking", "vchelsea_mutter1_nottalking")


image vchelsea_pout1_nottalking = "images/chelsea_valentine/mouths/110342_03_parts_c048.png"

image vchelsea_pout1_talking:
    "images/chelsea_valentine/mouths/110342_03_parts_c049.png"
    0.15
    "images/chelsea_valentine/mouths/110342_03_parts_c048.png"
    0.15
    repeat

image vchelsea_pout1 = WhileSpeaking("vchel", "vchelsea_pout1_talking", "vchelsea_pout1_nottalking")


image vchelsea_smile5_nottalking = "images/chelsea_valentine/mouths/110342_03_parts_c050.png"

image vchelsea_smile5_talking:
    "images/chelsea_valentine/mouths/110342_03_parts_c051.png"
    0.15
    "images/chelsea_valentine/mouths/110342_03_parts_c050.png"
    0.15
    repeat

image vchelsea_smile5 = WhileSpeaking("vchel", "vchelsea_smile5_talking", "vchelsea_smile5_nottalking")


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

label chelseaV_character_procedures:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image bedroom = "images/backgrounds/Sty_bg_0049_100_00.png"
    scene bedroom at middle

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    show vchelsea with dissolve

    vchel "AAAAAAAH!!! I'm SO excited for my Valentine's date with Luccy!!!"

    show vchelsea surprised
    show vchelsea frown2

    vchel "Oh.  But sometimes when Luccy sees my face, he runs away."
    vchel "I'd better make sure I can control my facial expressions so I can be exactly what Luccy wants."

    show vchelsea blush
    show vchelsea drool2

    vchel "And then he'll be MINE FOREVER AND WE'LL GET MARRIED AND HAVE TWELVE BEAUTIFUL CHILDREN!!!"

    show vchelsea focused_closed
    show vchelsea frown4

    vchel "...No, no, cool it, Chelsea, this is exactly the kind of thing that scares Luccy away."
    vchel "I need to make sure I'm the perfect girl for Luccy.  The only thing that matters is his happiness."

    show vchelsea focused

    vchel "Ok, I can do this.  Time to visualize the situation and practice my face in the mirror."

    show vchelsea relaxed
    show vchelsea smile1

    vchel "I meet Luccy and I greet him with a relaxed expression and a smile (smile1)."

    show vchelsea flinch
    show vchelsea grimace1

    vchel "No, no, that's not right!  I'm gonna look like a brick!"
    vchel "...Oh no!  Just look at me!  I'm flinching (flinch) and grimacing (grimace1) just thinking about it!!"

    show vchelsea focused_closed

    vchel "Calm down, calm down... I gotta focus (focused_closed)!"

    show vchelsea focused

    vchel "Ok, I'm totally focused now."

    show vchelsea wide
    show vchelsea smile2

    vchel "Ok, Chelsea... let's go for wider (wide) eyes and a bigger smile (smile2)."
    vchel "That looks pretty good... right?"

    show vchelsea serious
    show vchelsea frown1

    vchel "No, no... I can do better.  It's time for me to get serious."
    vchel "All the frowns (frown1) in the world would be worth it to have the perfect expression."

    show vchelsea neutral
    show vchelsea smile3

    vchel "Ok, let's go for a more neutral expression and a more understated smile (smile3)."
    vchel "'Hello, Luccy, it's a pleasure to see you this fine day.'"

    show vchelsea blush
    show vchelsea drool1

    vchel "That could be cool!  Ahhh, he'd think of me as a sophisticated young lady!!!"
    vchel "I'm blushing (blush) and drooling (drool1) just thinking about it!!!"

    show vchelsea drool2

    vchel "Aaaaaahhhhhhh!!! Luccyyyy, I'm all yours!!!"
    vchel "I'm drooling (drool2), you say??  Then maybe you could wipe it off with a KISSS!!!"

    show vchelsea surprised
    show vchelsea shout1

    vchel "No!!  No!!!  Bad, me!  This is exactly the problem!!!"
    vchel "Aaaaah, and I lost the face, too!!!  Now I just look surprised and grimacing (shout1)!"

    show vchelsea angry
    show vchelsea frown2

    vchel "I'm such an idiot!!!  I can't do anything right!!!  This should be so easy!!!"
    vchel "Aaaaugh, I'm so angry and all I can do is frown (frown2)!!"

    show vchelsea cry
    show vchelsea mutter1

    vchel "Aaaaaagh.... That's right, I've got a huge frown (mutter1) on my face... and look at me, I'm even crying (cry)..."

    show vchelsea pout1

    vchel "Look at my disgusting face... Luccy would never want to be with someone who frowns (pout1) like this."
    vchel "I'm totally hopeless... why did I think this could work?"

    show vchelsea serious_closed
    show vchelsea frown3

    vchel "...No.  I know I'm hopeless.  But that's why I need to trust in Luccy."
    vchel "If I can just be serious (serious_closed) about it, then it becomes really obvious."
    vchel "If Luccy were the kind of person who would hate me because of my face, I wouldn't love him the way I do."

    show vchelsea smile4

    vchel "Yes... Just thinking about the kind of person Luccy is is enough to make me smile (smile4)."

    show vchelsea smile5

    vchel "And... if I trust my feelings and I trust him..."

    show vchelsea focused

    vchel "...then I don't have to worry about it.  The perfect smile (smile5) will come from my heart."

    show vchelsea focused_closed

    vchel "..."

    show vchelsea serious

    vchel "Alright.  I'm ready to face him now.  Watch out, Luccy!  I'm determined to share my feelings with you."

    hide vchelsea with dissolve

    # This goes back to script

    jump testfiles
