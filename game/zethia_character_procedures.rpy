
    # Zethia Character Procedures File

    # Paste this file into a story if you want to use Notte.  These procedures animate Notte as a speaker.
    # You'll also need to paste THIS line into your actual script above the script label whenever you're using Notte:

define zeth = Character("Zethia", callback=speaker("zeth"))

    # This program assumes that the following folders exist:
    #     -"images/zethia"
    #     -"images/zethia/faces"
    #     -"images/zethia/mouths"

    # Zethia dynamically blinks and, while speaking, also moves her mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Zethia appear*:
    #  -->  show zethia with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Zethia's eyes*:
    #  -->  show zethia [keyword]
    #  List of eye keywords:
    #     -->  relaxed (default), relaxed2, angry, focused, grumpy, pained, sad, surprised,
    #          other_angry, other_angry2, other_focused, other_pained, other_relaxed
    #          closed_relaxed, closed_focused

    # *Changing Zethia's mouth*:
    #  -->  show zethia [keyword]
    #  List of mouth keywords:
    #     -->  small_smile1 (default), awkward1, frown1, frown2, grin1,
    #          mutter1, mutter2, pout1, pout2, shout1, smile1, smile2,
    #          closed_frown1, closed_smile1

    # *Writing dialogue for Zethia*:
    #  --> zeth "[Notte's line here]"

    # *Making Zethia disappear*:
    #  --> hide zethia with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage zethia:

    always "images/zethia/zethia_body.png"

    group face:

        # 447/1024, 250/1024:
        pos (0.43652, 0.24414)

        attribute relaxed default:
            "zethia_relaxed_eyes"

        attribute closed_relaxed:
            "images/zethia/faces/100009_01_parts_c001.png"

        attribute other_relaxed:
            "zethia_other_relaxed_eyes"

        attribute focused:
            "zethia_focused_eyes"

        attribute closed_focused:
            "images/zethia/faces/100009_01_parts_c005.png"

        attribute relaxed2:
            "zethia_relaxed2_eyes"

        attribute grumpy:
            "zethia_grumpy_eyes"

        attribute surprised:
            "zethia_surprised_eyes"

        attribute sad:
            "zethia_sad_eyes"

        attribute pained:
            "zethia_pained_eyes"

        attribute angry:
            "zethia_angry_eyes"

        attribute other_angry:
            "zethia_other_angry_eyes"

        attribute other_angry2:
            "zethia_other_angry2_eyes"

        attribute other_focused:
            "zethia_other_focused_eyes"

        attribute other_pained:
            "zethia_other_pained_eyes"


    group mouth:

        pos (0.43652, 0.24414)

        attribute small_smile1 default:
            "zethia_small_smile1"

        attribute smile1:
            "zethia_smile1"

        attribute closed_smile1:
            "zethia_smile1_nottalking"

        attribute frown1:
            "zethia_frown1"

        attribute closed_frown1:
            "zethia_frown1_nottalking"

        attribute awkward1:
            "zethia_awkward1"

        attribute frown2:
            "zethia_frown2"

        attribute smile2:
            "zethia_smile2"

        attribute pout1:
            "zethia_pout1"

        attribute shout1:
            "zethia_shout1"

        attribute mutter1:
            "zethia_mutter1"

        attribute grin1:
            "zethia_grin1"

        attribute mutter2:
            "zethia_mutter2"

        attribute pout2:
            "zethia_pout2"


## EYE animations start here.

image zethia_relaxed_eyes:
    "images/zethia/faces/100009_01_parts_c000.png"
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
    "images/zethia/faces/100009_01_parts_c001.png"
    0.05
    repeat

image zethia_other_relaxed_eyes:
    "images/zethia/faces/100009_01_parts_c002.png"
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
    "images/zethia/faces/100009_01_parts_c003.png"
    0.05
    repeat

image zethia_focused_eyes:
    "images/zethia/faces/100009_01_parts_c004.png"
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
    "images/zethia/faces/100009_01_parts_c005.png"
    0.05
    repeat

image zethia_relaxed2_eyes:
    "images/zethia/faces/100009_01_parts_c013.png"
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
    "images/zethia/faces/100009_01_parts_c014.png"
    0.05
    repeat

image zethia_grumpy_eyes:
    "images/zethia/faces/100009_01_parts_c015.png"
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
    "images/zethia/faces/100009_01_parts_c016.png"
    0.05
    repeat

image zethia_surprised_eyes:
    "images/zethia/faces/100009_01_parts_c017.png"
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
    "images/zethia/faces/100009_01_parts_c018.png"
    0.05
    repeat

image zethia_sad_eyes:
    "images/zethia/faces/100009_01_parts_c019.png"
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
    "images/zethia/faces/100009_01_parts_c020.png"
    0.05
    repeat

image zethia_pained_eyes:
    "images/zethia/faces/100009_01_parts_c029.png"
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
    "images/zethia/faces/100009_01_parts_c030.png"
    0.05
    repeat

image zethia_angry_eyes:
    "images/zethia/faces/100009_01_parts_c031.png"
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
    "images/zethia/faces/100009_01_parts_c032.png"
    0.05
    repeat

image zethia_other_angry_eyes:
    "images/zethia/faces/100009_01_parts_c037.png"
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
    "images/zethia/faces/100009_01_parts_c038.png"
    0.05
    repeat

image zethia_other_angry2_eyes:
    "images/zethia/faces/100009_01_parts_c039.png"
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
    "images/zethia/faces/100009_01_parts_c040.png"
    0.05
    repeat

image zethia_other_focused_eyes:
    "images/zethia/faces/100009_01_parts_c041.png"
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
    "images/zethia/faces/100009_01_parts_c042.png"
    0.05
    repeat

image zethia_other_pained_eyes:
    "images/zethia/faces/100009_01_parts_c043.png"
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
    "images/zethia/faces/100009_01_parts_c044.png"
    0.05
    repeat





# MOUTH animations start here.

image zethia_small_smile1_nottalking = "images/zethia/mouths/100009_01_parts_c006.png"

image zethia_small_smile1_talking:
    "images/zethia/mouths/100009_01_parts_c007.png"
    0.15
    "images/zethia/mouths/100009_01_parts_c006.png"
    0.15
    repeat

image zethia_small_smile1 = WhileSpeaking("zeth", "zethia_small_smile1_talking", "zethia_small_smile1_nottalking")


image zethia_smile1_nottalking = "images/zethia/mouths/100009_01_parts_c009.png"

image zethia_smile1_talking:
    "images/zethia/mouths/100009_01_parts_c010.png"
    0.15
    "images/zethia/mouths/100009_01_parts_c009.png"
    0.15
    repeat

image zethia_smile1 = WhileSpeaking("zeth", "zethia_smile1_talking", "zethia_smile1_nottalking")


image zethia_frown1_nottalking = "images/zethia/mouths/100009_01_parts_c011.png"

image zethia_frown1_talking:
    "images/zethia/mouths/100009_01_parts_c012.png"
    0.15
    "images/zethia/mouths/100009_01_parts_c011.png"
    0.15
    repeat

image zethia_frown1 = WhileSpeaking("zeth", "zethia_frown1_talking", "zethia_frown1_nottalking")


# 021/022 are the same as 009/010, i.e. smile1


image zethia_awkward1_nottalking = "images/zethia/mouths/100009_01_parts_c023.png"

image zethia_awkward1_talking:
    "images/zethia/mouths/100009_01_parts_c024.png"
    0.15
    "images/zethia/mouths/100009_01_parts_c023.png"
    0.15
    repeat

image zethia_awkward1 = WhileSpeaking("zeth", "zethia_awkward1_talking", "zethia_awkward1_nottalking")


image zethia_frown2_nottalking = "images/zethia/mouths/100009_01_parts_c025.png"

image zethia_frown2_talking:
    "images/zethia/mouths/100009_01_parts_c026.png"
    0.15
    "images/zethia/mouths/100009_01_parts_c025.png"
    0.15
    repeat

image zethia_frown2 = WhileSpeaking("zeth", "zethia_frown2_talking", "zethia_frown2_nottalking")


image zethia_smile2_nottalking = "images/zethia/mouths/100009_01_parts_c027.png"

image zethia_smile2_talking:
    "images/zethia/mouths/100009_01_parts_c028.png"
    0.15
    "images/zethia/mouths/100009_01_parts_c027.png"
    0.15
    repeat

image zethia_smile2 = WhileSpeaking("zeth", "zethia_smile2_talking", "zethia_smile2_nottalking")


image zethia_pout1_nottalking = "images/zethia/mouths/100009_01_parts_c033.png"

image zethia_pout1_talking:
    "images/zethia/mouths/100009_01_parts_c034.png"
    0.15
    "images/zethia/mouths/100009_01_parts_c033.png"
    0.15
    repeat

image zethia_pout1 = WhileSpeaking("zeth", "zethia_pout1_talking", "zethia_pout1_nottalking")


image zethia_shout1_nottalking = "images/zethia/mouths/100009_01_parts_c035.png"

image zethia_shout1_talking:
    "images/zethia/mouths/100009_01_parts_c036.png"
    0.15
    "images/zethia/mouths/100009_01_parts_c035.png"
    0.15
    repeat

image zethia_shout1 = WhileSpeaking("zeth", "zethia_shout1_talking", "zethia_shout1_nottalking")



image zethia_mutter1_nottalking = "images/zethia/mouths/100009_01_parts_c045.png"

image zethia_mutter1_talking:
    "images/zethia/mouths/100009_01_parts_c046.png"
    0.15
    "images/zethia/mouths/100009_01_parts_c045.png"
    0.15
    repeat

image zethia_mutter1 = WhileSpeaking("zeth", "zethia_mutter1_talking", "zethia_mutter1_nottalking")



image zethia_grin1_nottalking = "images/zethia/mouths/100009_01_parts_c047.png"

image zethia_grin1_talking:
    "images/zethia/mouths/100009_01_parts_c048.png"
    0.15
    "images/zethia/mouths/100009_01_parts_c047.png"
    0.15
    repeat

image zethia_grin1 = WhileSpeaking("zeth", "zethia_grin1_talking", "zethia_grin1_nottalking")


image zethia_mutter2_nottalking = "images/zethia/mouths/100009_01_parts_c049.png"

image zethia_mutter2_talking:
    "images/zethia/mouths/100009_01_parts_c050.png"
    0.15
    "images/zethia/mouths/100009_01_parts_c049.png"
    0.15
    repeat

image zethia_mutter2 = WhileSpeaking("zeth", "zethia_mutter2_talking", "zethia_mutter2_nottalking")


image zethia_pout2_nottalking = "images/zethia/mouths/100009_01_parts_c051.png"

image zethia_pout2_talking:
    "images/zethia/mouths/100009_01_parts_c052.png"
    0.15
    "images/zethia/mouths/100009_01_parts_c051.png"
    0.15
    repeat

image zethia_pout2 = WhileSpeaking("zeth", "zethia_pout2_talking", "zethia_pout2_nottalking")



# The game starts here.

label zethia_character_procedures:


    image forest_grotto_day = "images/backgrounds/Sty_bg_0074_100_00.png"
    scene forest_grotto_day


    show zethia with dissolve
    zeth "Wow, this forest grotto is even more beautiful than I could have ever imagined!"

    show zethia relaxed small_smile1
    zeth "(relaxed small_smile1) I came here to check on the Lambentree, but being here in solutude surrounded by the blessings of mana is so invigorating!  I've never even seen some of these plants before."

    show zethia surprised frown1
    zeth "(surprised frown1) Oh?"

    show zethia focused mutter1
    zeth "(focused mutter1) My reflection looks so out of place here... and... there's something different in my eyes..."

    show zethia other_angry grin1 with fade
    zeth "(other_angry grin1) Indeed.  You should know it well, my sweet Auspex.  You will never be able to fully purge my influence from you."

    show zethia angry shout1
    zeth "(angry shout1) ...The Other!!  Oh no!  Why are you emerging now from within me?"

    show zethia other_pained smile1
    zeth "(other_pained smile1) Surely that's not a real question?  I should think it obvious that the Lambentree amplifies all mana--including mine."

    show zethia pained frown2
    zeth "(pained frown2) Of course... but I must not allow this!  You cannot be permitted back into the world, even as a shadow of your former self within me."

    show zethia other_relaxed awkward1
    zeth "(other_relaxed awkward1) I don't understand why you're talking about this like you have a choice in the matter.  As long as hatred exists in the world, so too will I."

    show zethia grumpy pout1
    zeth "(grumpy pout1) That may be true, but that doesn't mean I'll continue to let you have free reign over my body!  Haaaaah!"

    image white = "images/backgrounds/white.png"
    show white with dissolve
    show zethia other_angry2 pout2
    hide white with fade

    zeth "(other_angry2 pout2) Tsk.  Crystallizing the ambient mana of prayer and coating your entire body with it?  What an annoying little barrier you've managed to construct."

    show zethia angry mutter1
    zeth "(angry mutter1) That's right.  Had enough yet, or do you need me to unleash the full power of an Auspex on you?"

    show zethia other_relaxed mutter2
    zeth "(other_relaxed mutter2) (sigh) I suppose I'd rather not deal with such an annoyance.  Besides, I never intended this to be the moment of my escape anyway."

    show zethia other_focused grin1
    zeth "(other_focused grin1) I just wanted to have a little chat with you, sweet little Auspex.  After all, I'll always live inside you, so I have all the time in the world..."

    show zethia closed_focused closed_frown1
    zeth "(closed_focused closed_frown1) ..."

    show zethia sad frown1
    zeth "(sad frown1) ...I think I've contained him.  For now."

    show zethia pained smile2
    zeth "(pained smile2) And here I thought I could take a break from my troubles...  I suppose it really will be a long road ahead for me..."

    show zethia closed_relaxed frown1
    zeth "(closed_relaxed frown1) ...Well, staying here won't do me much good.  I should leave here before the mana density here triggers another attack."

    hide zethia with dissolve

    hide zethia with dissolve


    # This goes back to script

    jump testfiles
