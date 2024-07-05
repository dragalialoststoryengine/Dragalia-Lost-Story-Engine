# Finni Character Procedures File UPDATED 1/1/2023

# Paste this file into a story if you want to use Finni.  These procedures animate Finni as a speaker.
# You'll also need to paste THIS line into your actual script above the script label whenever you're using Finni:

define fin = Character("Finni", callback=speaker("fin"))

# This program assumes that the following folders exist:
#     -"images/finni"
#     -"images/finni/faces"
#     -"images/finni/mouths"

# Finni dynamically blinks and, while speaking, also moves her mouth along with the text scroll.

# FUNCTIONS:

# *Making Finni appear*:
#  -->  show finni with dissolve 0.5
#       ("with dissolve 0.5" is optional but makes transitions cleaner)

# *Changing Finni's eyes*:
#  -->  show finni [keyword]
#  List of eye keywords:
#     -->  wink (the default option), angry, closed_angry, closed_focused, flinch, focused,
#           neutral, pained, closed_pained, relaxed, relaxed2, sad, shocked, surprised

# *Changing Finni's mouth*:
#  -->  show finni [keyword]
#  List of mouth keywords:
#     -->  smile1 (the default option), smile2, awkward1, closed_awkward1, grin1, closed_grin1,
#           frown1, closed_frown1, frown2, mouth_slightly_open, mutter1, closed_mutter1, pout1, shout1, open_shout1

# *Writing dialogue for Finni*:
#  --> fin "[Finni's line here]"

# *Making Finni disappear*:
#  --> hide finni with dissolve 0.5
#       ("with dissolve 0.5" is optional but makes transitions cleaner)




# # # # #




layeredimage finni:

    always "images/finni/finni_body.png"

    group face:

        pos (0.45215, 0.25879)

        attribute wink default:
            "finni_wink_eyes"

        attribute closed_focused:
            "images/finni/faces/110383_01_parts_c002.png"

        attribute focused:
            "finni_focused_eyes"

        attribute relaxed:
            "finni_relaxed_eyes"

        attribute flinch:
            "finni_flinch_eyes"

        attribute surprised:
            "finni_surprised_eyes"

        attribute sad:
            "finni_sad_eyes"

        attribute pained:
            "finni_pained_eyes"

        attribute closed_pained:
            "images/finni/faces/110383_01_parts_c026.png"

        attribute shocked:
            "finni_shocked_eyes"

        attribute relaxed2:
            "finni_relaxed2_eyes"

        attribute angry:
            "finni_angry_eyes"

        attribute closed_angry:
            "images/finni/faces/110383_01_parts_c038.png"

        attribute neutral:
            "finni_neutral_eyes"

    group mouth:

        pos (0.45215, 0.25879)

        attribute smile1 default:
            "finni_smile1"

        attribute frown1:
            "finni_frown1"

        attribute closed_frown1:
            "finni_frown1_nottalking"

        attribute smile2:
            "finni_smile2"

        attribute pout1:
            "finni_pout1"

        attribute frown2:
            "finni_frown2"

        attribute awkward1:
            "finni_awkward1"

        attribute open_awkward1:
            "images/finni/mouths/110383_01_parts_c024.png"

        attribute closed_awkward1:
            "finni_awkward1_nottalking"

        attribute mouth_slightly_open:
            "images/finni/mouths/110383_01_parts_c031.png"

        attribute shout1:
            "finni_shout1"

        attribute open_shout1:
            "images/finni/mouths/110383_01_parts_c042.png"

        attribute grin1:
            "finni_grin1"

        attribute closed_grin1:
            "finni_grin1_nottalking"

        attribute mutter1:
            "finni_mutter1"

        attribute closed_mutter1:
            "finni_mutter1_nottalking"


# Also a cropped version that can move

layeredimage finni_crop:

    always "images/finni/finni_body_crop.png"

    group face:
        # 465/1028, 163/1028

        pos (0.45233, 0.15856)

        attribute wink default:
            "finni_wink_eyes"

        attribute closed_focused:
            "images/finni/faces/110383_01_parts_c002.png"

        attribute focused:
            "finni_focused_eyes"

        attribute relaxed:
            "finni_relaxed_eyes"

        attribute flinch:
            "finni_flinch_eyes"

        attribute surprised:
            "finni_surprised_eyes"

        attribute sad:
            "finni_sad_eyes"

        attribute pained:
            "finni_pained_eyes"

        attribute closed_pained:
            "images/finni/faces/110383_01_parts_c026.png"

        attribute shocked:
            "finni_shocked_eyes"

        attribute relaxed2:
            "finni_relaxed2_eyes"

        attribute angry:
            "finni_angry_eyes"

        attribute closed_angry:
            "images/finni/faces/110383_01_parts_c038.png"

        attribute neutral:
            "finni_neutral_eyes"

    group mouth:

        pos (0.45233, 0.15856)

        attribute smile1 default:
            "finni_smile1"

        attribute frown1:
            "finni_frown1"

        attribute closed_frown1:
            "finni_frown1_nottalking"

        attribute smile2:
            "finni_smile2"

        attribute pout1:
            "finni_pout1"

        attribute frown2:
            "finni_frown2"

        attribute awkward1:
            "finni_awkward1"

        attribute open_awkward1:
            "images/finni/mouths/110383_01_parts_c024.png"

        attribute closed_awkward1:
            "finni_awkward1_nottalking"

        attribute mouth_slightly_open:
            "images/finni/mouths/110383_01_parts_c031.png"

        attribute shout1:
            "finni_shout1"

        attribute open_shout1:
            "images/finni/mouths/110383_01_parts_c042.png"

        attribute grin1:
            "finni_grin1"

        attribute closed_grin1:
            "finni_grin1_nottalking"

        attribute mutter1:
            "finni_mutter1"

        attribute closed_mutter1:
            "finni_mutter1_nottalking"



## EYE animations start here.

image finni_wink_eyes:
    "images/finni/faces/110383_01_parts_c000.png"
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
    "images/finni/faces/110383_01_parts_c001.png"
    0.05
    repeat

image finni_focused_eyes:
    "images/finni/faces/110383_01_parts_c003.png"
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
    "images/finni/faces/110383_01_parts_c004.png"
    0.05
    repeat

image finni_relaxed_eyes:
    "images/finni/faces/110383_01_parts_c009.png"
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
    "images/finni/faces/110383_01_parts_c010.png"
    0.05
    repeat

image finni_flinch_eyes:
    "images/finni/faces/110383_01_parts_c011.png"
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
    "images/finni/faces/110383_01_parts_c012.png"
    0.05
    repeat

image finni_surprised_eyes:
    "images/finni/faces/110383_01_parts_c013.png"
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
    "images/finni/faces/110383_01_parts_c014.png"
    0.05
    repeat

image finni_sad_eyes:
    "images/finni/faces/110383_01_parts_c015.png"
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
    "images/finni/faces/110383_01_parts_c016.png"
    0.05
    repeat

image finni_pained_eyes:
    "images/finni/faces/110383_01_parts_c025.png"
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
    "images/finni/faces/110383_01_parts_c026.png"
    0.05
    repeat

image finni_shocked_eyes:
    "images/finni/faces/110383_01_parts_c027.png"
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
    "images/finni/faces/110383_01_parts_c028.png"
    0.05
    repeat

image finni_relaxed2_eyes:
    "images/finni/faces/110383_01_parts_c029.png"
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
    "images/finni/faces/110383_01_parts_c030.png"
    0.05
    repeat

image finni_angry_eyes:
    "images/finni/faces/110383_01_parts_c037.png"
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
    "images/finni/faces/110383_01_parts_c038.png"
    0.05
    repeat

image finni_neutral_eyes:
    "images/finni/faces/110383_01_parts_c039.png"
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
    "images/finni/faces/110383_01_parts_c040.png"
    0.05
    repeat



# MOUTH animations start here.

image finni_smile1_nottalking = "images/finni/mouths/110383_01_parts_c005.png"

image finni_smile1_talking:
    "images/finni/mouths/110383_01_parts_c005.png"
    0.15
    "images/finni/mouths/110383_01_parts_c006.png"
    0.15
    repeat

image finni_smile1 = WhileSpeaking("fin", "finni_smile1_talking", "finni_smile1_nottalking")


image finni_frown1_nottalking = "images/finni/mouths/110383_01_parts_c007.png"

image finni_frown1_talking:
    "images/finni/mouths/110383_01_parts_c007.png"
    0.15
    "images/finni/mouths/110383_01_parts_c008.png"
    0.15
    repeat

image finni_frown1 = WhileSpeaking("fin", "finni_frown1_talking", "finni_frown1_nottalking")


image finni_smile2_nottalking = "images/finni/mouths/110383_01_parts_c017.png"

image finni_smile2_talking:
    "images/finni/mouths/110383_01_parts_c017.png"
    0.15
    "images/finni/mouths/110383_01_parts_c018.png"
    0.15
    repeat

image finni_smile2 = WhileSpeaking("fin", "finni_smile2_talking", "finni_smile2_nottalking")


image finni_pout1_nottalking = "images/finni/mouths/110383_01_parts_c019.png"

image finni_pout1_talking:
    "images/finni/mouths/110383_01_parts_c019.png"
    0.15
    "images/finni/mouths/110383_01_parts_c020.png"
    0.15
    repeat

image finni_pout1 = WhileSpeaking("fin", "finni_pout1_talking", "finni_pout1_nottalking")


image finni_frown2_nottalking = "images/finni/mouths/110383_01_parts_c021.png"

image finni_frown2_talking:
    "images/finni/mouths/110383_01_parts_c021.png"
    0.15
    "images/finni/mouths/110383_01_parts_c022.png"
    0.15
    repeat

image finni_frown2 = WhileSpeaking("fin", "finni_frown2_talking", "finni_frown2_nottalking")


image finni_awkward1_nottalking = "images/finni/mouths/110383_01_parts_c023.png"

image finni_awkward1_talking:
    "images/finni/mouths/110383_01_parts_c023.png"
    0.15
    "images/finni/mouths/110383_01_parts_c024.png"
    0.15
    repeat

image finni_awkward1 = WhileSpeaking("fin", "finni_awkward1_talking", "finni_awkward1_nottalking")



image finni_shout1_nottalking = "images/finni/mouths/110383_01_parts_c032.png"

image finni_shout1_talking:
    "images/finni/mouths/110383_01_parts_c032.png"
    0.15
    "images/finni/mouths/110383_01_parts_c033.png"
    0.15
    repeat

image finni_shout1 = WhileSpeaking("fin", "finni_shout1_talking", "finni_shout1_nottalking")


# 034/035, formerly smile3, is the same as 005/006 smile1


# 041/042, which i initially called frown5, are identical to 032/033, originally called frown4 and now shout1.


image finni_grin1_nottalking = "images/finni/mouths/110383_01_parts_c043.png"

image finni_grin1_talking:
    "images/finni/mouths/110383_01_parts_c043.png"
    0.15
    "images/finni/mouths/110383_01_parts_c044.png"
    0.15
    repeat

image finni_grin1 = WhileSpeaking("fin", "finni_grin1_talking", "finni_grin1_nottalking")


image finni_mutter1_nottalking = "images/finni/mouths/110383_01_parts_c045.png"

image finni_mutter1_talking:
    "images/finni/mouths/110383_01_parts_c045.png"
    0.15
    "images/finni/mouths/110383_01_parts_c046.png"
    0.15
    repeat

image finni_mutter1 = WhileSpeaking("fin", "finni_mutter1_talking", "finni_mutter1_nottalking")



transform finni_crop_pos:
    xalign 0.0
    yalign 0.99805

transform finni_crop_shake:
    xalign 0.0
    yalign 0.99805
    linear 0.1 xalign 0.005 yalign 0.99805
    linear 0.1 xalign 0.0 yalign 0.99805
    repeat

transform finni_crop_leap_right:
    xalign 0.0
    yalign 0.99805
    linear 0.25 xalign 1.0 yalign 0.99805

transform finni_crop_leap_left:
    xalign 1.0
    yalign 0.99805
    linear 0.25 xalign 0.0 yalign 0.99805

transform finni_crop_right:
    xalign 1.0 yalign 0.99805

transform finni_crop_move_right:
    xalign 0.0
    yalign 0.99805
    linear 1.5 xalign 1.0 yalign 0.99805



label finni_character_procedures:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image sky = "images/backgrounds/Sty_bg_0015_100_00.png"
    scene sky at middle
    image village = "images/backgrounds/Sty_bg_0015_100_04_front.png"
    show village at middle



    show finni at middle with dissolve
    fin "Hey everyone!"
    show finni_crop at finni_crop_pos

    # These display lines of dialogue.

    fin "Ok, so I've just undergone a major emote programming restructure (as of 1/1/2023), so I need to make sure everything works under this new format."
    hide finni_crop
    fin "Hopefully this restructure will make the emote interface more standardized, more descriptive and easier to use."
    fin "The quick brown fox jumps over the lazy dog.  The quick brown fox jumps over the lazy dog.  The quick brown fox jumps over the lazy dog."

    show finni wink smile1
    fin "Activating 'wink' and 'smile1' protocols.  Testing for code instabilities... verifying test data.  Seeking external validation."

    show finni angry smile2
    fin "Activating 'angry' and 'smile2' protocols.  Testing for code instabilities... verifying test data.  Seeking external validation."

    show finni closed_focused awkward1
    fin "Activating 'closed_focused' and 'awkward1' protocols.  Testing for code instabilities... verifying test data.  Seeking external validation."

    show finni flinch closed_awkward1
    fin "Activating 'flinch' and 'closed_awkard1' protocols.  Testing for code instabilities... verifying test data.  Seeking external validation."

    show finni focused grin1
    fin "Activating 'focused' and 'grin1' protocols.  Testing for code instabilities... verifying test data.  Seeking external validation."

    show finni neutral frown1
    fin "Activating 'neutral' and 'frown1' protocols.  Testing for code instabilities... verifying test data.  Seeking external validation."

    show finni pained frown2
    fin "Activating 'pained' and 'frown2' protocols.  Testing for code instabilities... verifying test data.  Seeking external validation."

    show finni relaxed mouth_slightly_open
    fin "Activating 'relaxed' and 'mouth_slightly_open' protocols.  Testing for code instabilities... verifying test data.  Seeking external validation."

    show finni relaxed2 mutter1
    fin "Activating 'relaxed2' and 'mutter1' protocols.  Testing for code instabilities... verifying test data.  Seeking external validation."

    show finni sad pout1
    fin "Activating 'sad' and 'pout1' protocols.  Testing for code instabilities... verifying test data.  Seeking external validation."

    show finni shock shout1
    fin "Activating 'shock' and 'shout1' protocols.  Testing for code instabilities... verifying test data.  Seeking external validation."

    show finni surprised closed_mutter1
    fin "Activating 'surprised' and 'closed_mutter1' protocols.  Testing for code instabilities... verifying test data.  Seeking external validation."

    show finni closed_frown1
    fin "Activating 'closed_frown1' protocols.  Testing for code instabilities... verifying test data.  Seeking external validation."

    show finni wink smile1
    fin "Ok, I think that's everything!  If you got this far without crashing, I guess we can chalk this up as a success!!"

    hide finni with dissolve

    # This goes back to script

    jump testfiles
