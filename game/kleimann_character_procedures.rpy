    # Kleimann Character Procedures File

    # Paste this file into a story if you want to use Karl.  These procedures animate Karl as a speaker.

define klei = Character("Kleimann", callback=speaker("klei"))

    # This program assumes that the following folders exist:
    #     -"images/kleimann"
    #     -"images/kleimann/faces"
    #     -"images/kleimann/mouths"

    # Kleimann dynamically blinks and, while speaking, also moves his mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Kleimann appear*:
    #  -->  show kleimann with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Kleimann's eyes*:
    #  -->  show kleimann [keyword]
    #  List of eye keywords:
    #     -->  neutral (default), cry, dark, focused, glow, shadow, surprised

    # *Changing Kleimann's mouth*:
    #  -->  show kleimann [keyword]
    #  List of mouth keywords:
    #     -->  grin1 (default), grin2, frown1, grimace1, grimace2, grimace3,
    #           mutter1, shout1, frown1_closed

    # *Writing dialogue for Kleimann*:
    #  --> klei "[Kleimann's line here]"

    # *Making Kleimann disappear*:
    #  --> hide kleimann with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage kleimann:

    always "images/kleimann/kleimann_body.png"

    group face:

        # 448/1024, 265/1024:
        pos (0.4375, 0.25879)

        attribute neutral default:
            "kleimann_neutral_eyes"

        attribute focused:
            "kleimann_focused_eyes"

        attribute cry:
            "kleimann_cry_eyes"

        attribute surprised:
            "kleimann_surprised_eyes"

        attribute glow:
            "kleimann_glow_eyes"

        attribute shadow:
            "kleimann_shadow_eyes"

        attribute dark:
            "kleimann_dark_eyes"



    group mouth:

        pos (0.4375, 0.25879)

        attribute grin1 default:
            "kleimann_grin1"

        attribute frown1_closed:
            "images/kleimann/mouths/110051_01_parts_c008.png"

        attribute frown1:
            "kleimann_frown1"

        attribute grin2:
            "kleimann_grin2"

        attribute grimace3:
            "kleimann_grimace3"

        attribute grimace2:
            "kleimann_grimace2"

        attribute mutter1:
            "kleimann_mutter1"

        attribute grimace1:
            "kleimann_grimace1"

        attribute shout1:
            "kleimann_shout1"



## EYE animations start here.

image kleimann_neutral_eyes:
    "images/kleimann/faces/110051_01_parts_c000.png"
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
    "images/kleimann/faces/110051_01_parts_c001.png"
    0.05
    repeat

image kleimann_focused_eyes:
    "images/kleimann/faces/110051_01_parts_c002.png"
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
    "images/kleimann/faces/110051_01_parts_c003.png"
    0.05
    repeat

image kleimann_cry_eyes:
    "images/kleimann/faces/110051_01_parts_c010.png"
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
    "images/kleimann/faces/110051_01_parts_c011.png"
    0.05
    repeat

image kleimann_surprised_eyes:
    "images/kleimann/faces/110051_01_parts_c012.png"
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
    "images/kleimann/faces/110051_01_parts_c013.png"
    0.05
    repeat

image kleimann_glow_eyes:
    "images/kleimann/faces/110051_01_parts_c014.png"
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
    "images/kleimann/faces/110051_01_parts_c001.png"
    0.05
    repeat

image kleimann_shadow_eyes:
    "images/kleimann/faces/110051_01_parts_c015.png"
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
    "images/kleimann/faces/110051_01_parts_c016.png"
    0.05
    repeat

image kleimann_dark_eyes:
    "images/kleimann/faces/110051_01_parts_c025.png"
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
    "images/kleimann/faces/110051_01_parts_c026.png"
    0.05
    repeat


# MOUTH animations start here.

image kleimann_grin1_nottalking = "images/kleimann/mouths/110051_01_parts_c004.png"

image kleimann_grin1_talking:
    "images/kleimann/mouths/110051_01_parts_c005.png"
    0.15
    "images/kleimann/mouths/110051_01_parts_c004.png"
    0.15
    repeat

image kleimann_grin1 = WhileSpeaking("klei", "kleimann_grin1_talking", "kleimann_grin1_nottalking")


image kleimann_frown1_nottalking = "images/kleimann/mouths/110051_01_parts_c008.png"

image kleimann_frown1_talking:
    "images/kleimann/mouths/110051_01_parts_c009.png"
    0.15
    "images/kleimann/mouths/110051_01_parts_c008.png"
    0.15
    repeat

image kleimann_frown1 = WhileSpeaking("klei", "kleimann_frown1_talking", "kleimann_frown1_nottalking")


image kleimann_grin2_nottalking = "images/kleimann/mouths/110051_01_parts_c017.png"

image kleimann_grin2_talking:
    "images/kleimann/mouths/110051_01_parts_c018.png"
    0.15
    "images/kleimann/mouths/110051_01_parts_c017.png"
    0.15
    repeat

image kleimann_grin2 = WhileSpeaking("klei", "kleimann_grin2_talking", "kleimann_grin2_nottalking")


image kleimann_grimace3_nottalking = "images/kleimann/mouths/110051_01_parts_c019.png"

image kleimann_grimace3_talking:
    "images/kleimann/mouths/110051_01_parts_c020.png"
    0.15
    "images/kleimann/mouths/110051_01_parts_c019.png"
    0.15
    repeat

image kleimann_grimace3 = WhileSpeaking("klei", "kleimann_grimace3_talking", "kleimann_grimace3_nottalking")


image kleimann_grimace2_nottalking = "images/kleimann/mouths/110051_01_parts_c021.png"

image kleimann_grimace2_talking:
    "images/kleimann/mouths/110051_01_parts_c022.png"
    0.15
    "images/kleimann/mouths/110051_01_parts_c021.png"
    0.15
    repeat

image kleimann_grimace2 = WhileSpeaking("klei", "kleimann_grimace2_talking", "kleimann_grimace2_nottalking")


image kleimann_mutter1_nottalking = "images/kleimann/mouths/110051_01_parts_c023.png"

image kleimann_mutter1_talking:
    "images/kleimann/mouths/110051_01_parts_c024.png"
    0.15
    "images/kleimann/mouths/110051_01_parts_c023.png"
    0.15
    repeat

image kleimann_mutter1 = WhileSpeaking("klei", "kleimann_mutter1_talking", "kleimann_mutter1_nottalking")


image kleimann_grimace1_nottalking = "images/kleimann/mouths/110051_01_parts_c027.png"

image kleimann_grimace1_talking:
    "images/kleimann/mouths/110051_01_parts_c028.png"
    0.15
    "images/kleimann/mouths/110051_01_parts_c027.png"
    0.15
    repeat

image kleimann_grimace1 = WhileSpeaking("klei", "kleimann_grimace1_talking", "kleimann_grimace1_nottalking")


image kleimann_shout1_nottalking = "images/kleimann/mouths/110051_01_parts_c031.png"

image kleimann_shout1_talking:
    "images/kleimann/mouths/110051_01_parts_c032.png"
    0.15
    "images/kleimann/mouths/110051_01_parts_c031.png"
    0.15
    repeat

image kleimann_shout1 = WhileSpeaking("klei", "kleimann_shout1_talking", "kleimann_shout1_nottalking")



# The test file script starts here.

label kleimann_character_procedures:

    image laboratory = "images/backgrounds/Sty_bg_0103_100_00.png"
    scene laboratory with fade

    show kleimann with dissolve
    klei "Aha!  Welcome, my valuable assistant!  Back for another foray into the natural sciences?"

    show kleimann neutral grin1
    klei "(neutral grin1) You know, it's been quite a while since you've stopped in to lend me a hand."

    show kleimann cry grin2
    klei "(cry grin2) Just now, I was considering conjuring up some fiends again just to get you back in here in a huff.  Whee-ha-ha-hoo!"

    show kleimann focused frown1
    klei "(focused frown1) Well, no matter.  You're here now.  See, I've actually been dealing with a small conundrum, and I could use assistance."

    show kleimann shadow grimace1
    klei "(shadow grimace1) As you know, the ultimate goal of my research is to find out where souls sacrificed in rituals go."
    klei "To that end, I've been developing a hypothesis that the sacrificial process has parallels to the mana circles involved in empowering human abilities."

    show kleimann neutral grimace2
    klei "(grimace2) To that end, I want to sacrifice high-quality dragon parts in a magic ritual to imitate the sacrifice of a soul!"

    show kleimann dark mutter1
    klei "(dark mutter1) I would collect these samples myself, but a certain {i}someone{/i} has forbidden me from the endeavor after my most recent attempt."

    image high_shadowwyrms_horn = "images/items/high shadowwyrm's horn.png"
    show high_shadowwyrms_horn at item_pos with dissolve

    show kleimann glow frown1_closed
    klei "(glow frown1_closed) ..."

    show kleimann glow grimace3
    klei "(grimace3) ...What?  Could that be... a horn fragment of the High Shadowwyrm??"

    show kleimann surprised shout1
    klei "(shout1) How did you even obtain this?!  This is the kind of sample I could only dream of collecting!!"

    hide high_shadowwyrms_horn with dissolve

    show kleimann cry grin2
    klei "Whee-ha-ha-hoo!!  Excellent work, my assistant!  I knew there was a reason I chose you to work with me!!!"
    show kleimann surprised
    klei "We must put this sample to work at once!!!  Come, come!!!  Let me prep the sample while you fetch the ritual chalk and candles..."


    hide kleimann with dissolve


    # This goes back to script

    jump testfiles
