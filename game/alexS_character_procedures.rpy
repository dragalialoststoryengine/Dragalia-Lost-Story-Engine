
    # Summer Alex Character Procedures File

    # Paste this file into a story if you want to use Notte.  These procedures animate Notte as a speaker.
    # You'll also need to paste THIS line into your actual script above the script label whenever you're using Notte:

define sale = Character("Alex", callback=speaker("sale"))

    # This program assumes that the following folders exist:
    #     -"images/alex_summer"
    #     -"images/alex_summer/faces"
    #     -"images/alex_summer/mouths"

    # "alex_summer_back" procedures are further down below, so you need to scroll!!


    # Summer Alex dynamically blinks and, while speaking, also moves her mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Summer Alex appear*:
    #  -->  show alex_summer with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Summer Alex's eyes*:
    #  -->  show alex_summer [keyword]
    #  List of eye keywords:
    #     -->  relaxed (default), relaxed2, closed_relax, angry, askance, blush, closed_blush,
    #          focused, closed_focused, happy, shock, squint, closed_squint, surprised, closed_happy,
    #          wistful, closed_wistful, glare, closed_glare

    # *Changing Summer Alex's mouth*:
    #  -->  show alex_summer [keyword]
    #  List of mouth keywords:
    #     -->  smile1 (default), smile2, smile3, duchenne1, mutter1, closed_mutter1, frown1, frown2,
    #          frown3, frown4, grimace1, pout1, shout1

    # *Writing dialogue for Summer Alex*:
    #  --> sale "[Summer Alex's line here]"

    # *Making Summer Alex disappear*:
    #  --> hide alex_summer with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage alex_summer:

    always "images/alex_summer/alex_summer_body.png"

    group face:

        # 440/1028, 246/1028:

        #slightly off now, try 422/1028, 247/1028
        pos (0.42969, 0.24023)

        attribute relaxed default:
            "alex_summer_relaxed_eyes"

        attribute closed_relaxed:
            "images/alex_summer/faces/100005_08_parts_c001.png"

        attribute focused:
            "alex_summer_focused_eyes"

        attribute closed_focused:
            "images/alex_summer/faces/100005_08_parts_c003.png"

        attribute happy:
            "alex_summer_happy_eyes"

        attribute closed_happy:
            "images/alex_summer/faces/100005_08_parts_c014.png"

        attribute angry:
            "alex_summer_angry_eyes"

        attribute surprised:
            "alex_summer_surprised_eyes"

        attribute wistful:
            "alex_summer_wistful_eyes"

        attribute closed_wistful:
            "images/alex_summer/faces/100005_08_parts_c020.png"

        attribute squint:
            "alex_summer_squint_eyes"

        attribute closed_squint:
            "images/alex_summer/faces/100005_08_parts_c030.png"

        attribute shock:
            "alex_summer_shock_eyes"

        attribute relaxed2:
            "alex_summer_relaxed2_eyes"

        attribute blush:
            "alex_summer_blush_eyes"

        attribute closed_blush:
            "images/alex_summer/faces/100005_08_parts_c042.png"

        attribute askance:
            "alex_summer_askance_eyes"

        attribute glare:
            "alex_summer_glare_eyes"

        attribute closed_glare:
            "images/alex_summer/faces/100005_08_parts_c046.png"


    group mouth:

        pos (0.42969, 0.24023)

        attribute smile1 default:
            "alex_summer_smile1"

        attribute duchenne1:
            "alex_summer_duchenne1"

        attribute mutter1:
            "alex_summer_mutter1"

        attribute closed_mutter1:
            "images/alex_summer/mouths/100005_08_parts_c004.png"

        attribute smile2:
            "alex_summer_smile2"

        attribute grimace1:
            "alex_summer_grimace1"

        attribute shout1:
            "alex_summer_shout1"

        attribute frown1:
            "alex_summer_frown1"

        attribute smile3:
            "alex_summer_smile3"

        attribute duchenne2:
            "alex_summer_duchenne2"

        attribute frown2:
            "alex_summer_frown2"

        attribute shout1:
            "alex_summer_shout1"

        attribute frown3:
            "alex_summer_frown3"

        attribute frown4:
            "alex_summer_frown4"

        attribute pout1:
            "alex_summer_pout1"


## EYE animations start here.

image alex_summer_relaxed_eyes:
    "images/alex_summer/faces/100005_08_parts_c000.png"
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
    "images/alex_summer/faces/100005_08_parts_c001.png"
    0.05
    repeat

image alex_summer_focused_eyes:
    "images/alex_summer/faces/100005_08_parts_c004.png"
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
    "images/alex_summer/faces/100005_08_parts_c005.png"
    0.05
    repeat

image alex_summer_happy_eyes:
    "images/alex_summer/faces/100005_08_parts_c013.png"
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
    "images/alex_summer/faces/100005_08_parts_c014.png"
    0.05
    repeat

image alex_summer_angry_eyes:
    "images/alex_summer/faces/100005_08_parts_c015.png"
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
    "images/alex_summer/faces/100005_08_parts_c016.png"
    0.05
    repeat

image alex_summer_surprised_eyes:
    "images/alex_summer/faces/100005_08_parts_c017.png"
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
    "images/alex_summer/faces/100005_08_parts_c018.png"
    0.05
    repeat

image alex_summer_wistful_eyes:
    "images/alex_summer/faces/100005_08_parts_c019.png"
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
    "images/alex_summer/faces/100005_08_parts_c020.png"
    0.05
    repeat

image alex_summer_squint_eyes:
    "images/alex_summer/faces/100005_08_parts_c029.png"
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
    "images/alex_summer/faces/100005_08_parts_c030.png"
    0.05
    repeat

image alex_summer_shock_eyes:
    "images/alex_summer/faces/100005_08_parts_c031.png"
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
    "images/alex_summer/faces/100005_08_parts_c032.png"
    0.05
    repeat

image alex_summer_relaxed2_eyes:
    "images/alex_summer/faces/100005_08_parts_c033.png"
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
    "images/alex_summer/faces/100005_08_parts_c034.png"
    0.05
    repeat

image alex_summer_blush_eyes:
    "images/alex_summer/faces/100005_08_parts_c041.png"
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
    "images/alex_summer/faces/100005_08_parts_c042.png"
    0.05
    repeat

image alex_summer_askance_eyes:
    "images/alex_summer/faces/100005_08_parts_c043.png"
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
    "images/alex_summer/faces/100005_08_parts_c044.png"
    0.05
    repeat

image alex_summer_glare_eyes:
    "images/alex_summer/faces/100005_08_parts_c045.png"
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
    "images/alex_summer/faces/100005_08_parts_c046.png"
    0.05
    repeat




# MOUTH animations start here.

image alex_summer_smile1_nottalking = "images/alex_summer/mouths/100005_08_parts_c006.png"

image alex_summer_smile1_talking:
    "images/alex_summer/mouths/100005_08_parts_c007.png"
    0.15
    "images/alex_summer/mouths/100005_08_parts_c006.png"
    0.15
    repeat

image alex_summer_smile1 = WhileSpeaking("sale", "alex_summer_smile1_talking", "alex_summer_smile1_nottalking")


image alex_summer_duchenne1_nottalking = "images/alex_summer/mouths/100005_08_parts_c007.png"

image alex_summer_duchenne1_talking:
    "images/alex_summer/mouths/100005_08_parts_c006.png"
    0.15
    "images/alex_summer/mouths/100005_08_parts_c007.png"
    0.15
    repeat

image alex_summer_duchenne1 = WhileSpeaking("sale", "alex_summer_duchenne1_talking", "alex_summer_duchenne1_nottalking")


image alex_summer_mutter1_nottalking = "images/alex_summer/mouths/100005_08_parts_c011.png"

image alex_summer_mutter1_talking:
    "images/alex_summer/mouths/100005_08_parts_c012.png"
    0.15
    "images/alex_summer/mouths/100005_08_parts_c011.png"
    0.15
    repeat

image alex_summer_mutter1 = WhileSpeaking("sale", "alex_summer_mutter1_talking", "alex_summer_mutter1_nottalking")


image alex_summer_smile2_nottalking = "images/alex_summer/mouths/100005_08_parts_c021.png"

image alex_summer_smile2_talking:
    "images/alex_summer/mouths/100005_08_parts_c022.png"
    0.15
    "images/alex_summer/mouths/100005_08_parts_c021.png"
    0.15
    repeat

image alex_summer_smile2 = WhileSpeaking("sale", "alex_summer_smile2_talking", "alex_summer_smile2_nottalking")


image alex_summer_grimace1_nottalking = "images/alex_summer/mouths/100005_08_parts_c023.png"

image alex_summer_grimace1_talking:
    "images/alex_summer/mouths/100005_08_parts_c024.png"
    0.15
    "images/alex_summer/mouths/100005_08_parts_c023.png"
    0.15
    repeat

image alex_summer_grimace1 = WhileSpeaking("sale", "alex_summer_grimace1_talking", "alex_summer_grimace1_nottalking")


image alex_summer_frown1_nottalking = "images/alex_summer/mouths/100005_08_parts_c025.png"

image alex_summer_frown1_talking:
    "images/alex_summer/mouths/100005_08_parts_c026.png"
    0.15
    "images/alex_summer/mouths/100005_08_parts_c025.png"
    0.15
    repeat

image alex_summer_frown1 = WhileSpeaking("sale", "alex_summer_frown1_talking", "alex_summer_frown1_nottalking")


image alex_summer_smile3_nottalking = "images/alex_summer/mouths/100005_08_parts_c027.png"

image alex_summer_smile3_talking:
    "images/alex_summer/mouths/100005_08_parts_c028.png"
    0.15
    "images/alex_summer/mouths/100005_08_parts_c027.png"
    0.15
    repeat

image alex_summer_smile3 = WhileSpeaking("sale", "alex_summer_smile3_talking", "alex_summer_smile3_nottalking")


image alex_summer_duchenne2_nottalking = "images/alex_summer/mouths/100005_08_parts_c028.png"

image alex_summer_duchenne2_talking:
    "images/alex_summer/mouths/100005_08_parts_c027.png"
    0.15
    "images/alex_summer/mouths/100005_08_parts_c028.png"
    0.15
    repeat

image alex_summer_duchenne2 = WhileSpeaking("sale", "alex_summer_duchenne2_talking", "alex_summer_duchenne2_nottalking")


image alex_summer_frown2_nottalking = "images/alex_summer/mouths/100005_08_parts_c035.png"

image alex_summer_frown2_talking:
    "images/alex_summer/mouths/100005_08_parts_c036.png"
    0.15
    "images/alex_summer/mouths/100005_08_parts_c035.png"
    0.15
    repeat

image alex_summer_frown2 = WhileSpeaking("sale", "alex_summer_frown2_talking", "alex_summer_frown2_nottalking")


image alex_summer_shout1_nottalking = "images/alex_summer/mouths/100005_08_parts_c037.png"

image alex_summer_shout1_talking:
    "images/alex_summer/mouths/100005_08_parts_c038.png"
    0.15
    "images/alex_summer/mouths/100005_08_parts_c037.png"
    0.15
    repeat

image alex_summer_shout1 = WhileSpeaking("sale", "alex_summer_shout1_talking", "alex_summer_shout1_nottalking")


image alex_summer_frown3_nottalking = "images/alex_summer/mouths/100005_08_parts_c039.png"

image alex_summer_frown3_talking:
    "images/alex_summer/mouths/100005_08_parts_c040.png"
    0.15
    "images/alex_summer/mouths/100005_08_parts_c039.png"
    0.15
    repeat

image alex_summer_frown3 = WhileSpeaking("sale", "alex_summer_frown3_talking", "alex_summer_frown3_nottalking")


image alex_summer_frown4_nottalking = "images/alex_summer/mouths/100005_08_parts_c049.png"

image alex_summer_frown4_talking:
    "images/alex_summer/mouths/100005_08_parts_c050.png"
    0.15
    "images/alex_summer/mouths/100005_08_parts_c049.png"
    0.15
    repeat

image alex_summer_frown4 = WhileSpeaking("sale", "alex_summer_frown4_talking", "alex_summer_frown4_nottalking")


image alex_summer_pout1_nottalking = "images/alex_summer/mouths/100005_08_parts_c051.png"

image alex_summer_pout1_talking:
    "images/alex_summer/mouths/100005_08_parts_c052.png"
    0.15
    "images/alex_summer/mouths/100005_08_parts_c051.png"
    0.15
    repeat

image alex_summer_pout1 = WhileSpeaking("sale", "alex_summer_pout1_talking", "alex_summer_pout1_nottalking")









# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

transform alex_summer_back_pos:
    #118, 180 ->> 118/1028 ?

    # no, try (118 + (770/2))/1028
    xalign 0.48930
    yalign 1.0

transform alex_summer_back_ambush_pos:
    xalign 0.0
    yalign 1.0

transform alex_summer_back_ambush_to_regular:
    xalign 0.0
    yalign 1.0
    linear 1.0 xalign 0.48930 yalign 1.0








# The game starts here.

label alexS_character_procedures:


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

    show alex_summer with dissolve
    sale "Ah! It’s nice to be out on the beach again!"

    show alex_summer wistful smile3
    sale "(wistful smile3) It’s funny. I remember that I used to not be all about this."

    show alex_summer relaxed2 smile2
    sale "(relaxed2 smile2) But hey, that’s what I have to thank you for, Elisanne."

    show alex_summer happy smile3
    sale "(happy) I don’t feel I say it enough, but I’m just so grateful to be with you."

    show alex_summer angry grimace1
    sale "(angry grimace1) You helped me get out of something so abhorrent, I feel angry just remembering it…"

    show alex_summer closed_happy duchenne1
    sale "(closed_happy duchenne1) I can only hope to always be yours."

    show alex_summer squint frown4
    sale "(squint frown4) Sorry, just feeling a bit introspective is all."

    show alex_summer smile1
    sale "(smile1) Let’s just have some fun while we’re here!"

    show alex_summer askance pout1
    sale "(askance pout1) You know, just… preferably without as many townsfolk vying for our attention."

    show alex_summer relaxed2 duchenne1
    sale "(relaxed2) What say you? Should we do something out in the sea first?"

    show alex_summer closed_relaxed smile3
    sale "(closed_relaxed) I mean, I would love to just go out there with you, hand in hand~."

    show alex_summer shock shout1
    sale "(shock shout1) Oh, sorry! I didn’t mean to surprise you like that!"

    show alex_summer askance frown2
    sale "(frown2) *sigh*\nIt’s just… when I’m around you…"

    show alex_summer focused frown1
    sale "(focused frown1) I can’t describe it. I feel like I’m without words."

    show alex_summer relaxed mutter1
    sale "(relaxed mutter1) You just help me feel more complete when you’re around."

    show alex_summer smile2
    sale "The entire reason I’m even wearing this is because you yourself thought it was beautiful!"

    show alex_summer askance frown3
    sale "(frown3) Or, \"cute,\" to use your own words."

    show alex_summer wistful
    sale "I guess this is just my way of saying…"

    show alex_summer happy smile2
    sale "... that we should make this day last forever!"

    show alex_summer glare duchenne1
    sale "(glare) *You are my everything, Elisanne.*"

    show alex_summer blush duchenne2
    sale "(blush duchenne2) *Thank you for teaching me how to love again, Elly~. And for giving me the chance to love you again.*"

    show alex_summer surprised frown2
    sale "..."

    show alex_summer relaxed frown3
    sale "Assuming I said that out loud, just know that I support you and His Majesty no matter what."


    hide alex_summer with dissolve

    # This goes back to script

    jump testfiles
