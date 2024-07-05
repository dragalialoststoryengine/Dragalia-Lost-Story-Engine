    # Grace Character Procedures File

    # Paste this file into a story if you want to use Grace.  These procedures animate Grace as a speaker.

define gra = Character("Grace", callback=speaker("gra"))

    # This program assumes that the following folders exist:
    #     -"images/grace"
    #     -"images/grace/faces"
    #     -"images/grace/mouths"

    # Grace dynamically blinks and, while speaking, also moves her mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Grace appear*:
    #  -->  show grace with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Grace's eyes*:
    #  -->  show grace [keyword]
    #  List of eye keywords:
    #     -->  neutral (the default option), focused, relaxed, angry, angry2,
    #          surprised, sad, sad2, blank, closed_neutral, closed_focused

    # *Changing Grace's mouth*:
    #  -->  show grace [keyword]
    #  List of mouth keywords:
    #     -->  grimace1 (the default option), grimace2, frown1, frown2, frown3,
    #          smile1, smile2, smile3

    # *Writing dialogue for Grace*:
    #  --> gra "[Grace's line here]"

    # *Making Grace disappear*:
    #  --> hide grace with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage grace:

    always "images/grace/grace_body.png"

    group face:

        # 400/1028, 246/1028:
        pos (0.38911, 0.23930)

        attribute neutral default:
            "grace_neutral_eyes"

        attribute closed_neutral:
            "images/grace/faces/110059_01_parts_c001.png"

        attribute focused:
            "grace_focused_eyes"

        attribute closed_focused:
            "images/grace/faces/110059_01_parts_c005.png"

        attribute relaxed:
            "grace_relaxed_eyes"

        attribute angry:
            "grace_angry_eyes"

        attribute surprised:
            "grace_surprised_eyes"

        attribute sad:
            "grace_sad_eyes"

        attribute sad2:
            "grace_sad2_eyes"

        attribute blank:
            "grace_blank_eyes"

        attribute angry2:
            "grace_angry2_eyes"


    group mouth:

        pos (0.38911, 0.23930)

        attribute grimace1 default:
            "grace_grimace1"

        attribute frown1:
            "grace_frown1"

        attribute smile1:
            "grace_smile1"

        attribute frown2:
            "grace_frown2"

        attribute grimace2:
            "grace_grimace2"

        attribute smile2:
            "grace_smile2"

        attribute smile3:
            "grace_smile3"

        attribute frown3:
            "grace_frown3"



## EYE animations start here.

image grace_neutral_eyes:
    "images/grace/faces/110059_01_parts_c000.png"
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
    "images/grace/faces/110059_01_parts_c001.png"
    0.05
    repeat

image grace_focused_eyes:
    "images/grace/faces/110059_01_parts_c004.png"
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
    "images/grace/faces/110059_01_parts_c005.png"
    0.05
    repeat

image grace_relaxed_eyes:
    "images/grace/faces/110059_01_parts_c011.png"
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
    "images/grace/faces/110059_01_parts_c012.png"
    0.05
    repeat

image grace_angry_eyes:
    "images/grace/faces/110059_01_parts_c013.png"
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
    "images/grace/faces/110059_01_parts_c014.png"
    0.05
    repeat

image grace_surprised_eyes:
    "images/grace/faces/110059_01_parts_c015.png"
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
    "images/grace/faces/110059_01_parts_c016.png"
    0.05
    repeat

image grace_sad_eyes:
    "images/grace/faces/110059_01_parts_c017.png"
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
    "images/grace/faces/110059_01_parts_c018.png"
    0.05
    repeat

image grace_sad2_eyes:
    "images/grace/faces/110059_01_parts_c027.png"
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
    "images/grace/faces/110059_01_parts_c028.png"
    0.05
    repeat

image grace_blank_eyes:
    "images/grace/faces/110059_01_parts_c029.png"
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
    "images/grace/faces/110059_01_parts_c030.png"
    0.05
    repeat

image grace_angry2_eyes:
    "images/grace/faces/110059_01_parts_c031.png"
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
    "images/grace/faces/110059_01_parts_c032.png"
    0.05
    repeat


# MOUTH animations start here.

# Note:  'grimaces' here are animated in reverse from usual (teeth not shown on resting).

image grace_grimace1_nottalking = "images/grace/mouths/110059_01_parts_c006.png"

image grace_grimace1_talking:
    "images/grace/mouths/110059_01_parts_c006.png"
    0.15
    "images/grace/mouths/110059_01_parts_c007.png"
    0.15
    repeat

image grace_grimace1 = WhileSpeaking("gra", "grace_grimace1_talking", "grace_grimace1_nottalking")


image grace_frown1_nottalking = "images/grace/mouths/110059_01_parts_c008.png"

image grace_frown1_talking:
    "images/grace/mouths/110059_01_parts_c008.png"
    0.15
    "images/grace/mouths/110059_01_parts_c009.png"
    0.15
    repeat

image grace_frown1 = WhileSpeaking("gra", "grace_frown1_talking", "grace_frown1_nottalking")


image grace_smile1_nottalking = "images/grace/mouths/110059_01_parts_c019.png"

image grace_smile1_talking:
    "images/grace/mouths/110059_01_parts_c019.png"
    0.15
    "images/grace/mouths/110059_01_parts_c020.png"
    0.15
    repeat

image grace_smile1 = WhileSpeaking("gra", "grace_smile1_talking", "grace_smile1_nottalking")


image grace_frown2_nottalking = "images/grace/mouths/110059_01_parts_c021.png"

image grace_frown2_talking:
    "images/grace/mouths/110059_01_parts_c021.png"
    0.15
    "images/grace/mouths/110059_01_parts_c022.png"
    0.15
    repeat

image grace_frown2 = WhileSpeaking("gra", "grace_frown2_talking", "grace_frown2_nottalking")


image grace_grimace2_nottalking = "images/grace/mouths/110059_01_parts_c023.png"

image grace_grimace2_talking:
    "images/grace/mouths/110059_01_parts_c023.png"
    0.15
    "images/grace/mouths/110059_01_parts_c024.png"
    0.15
    repeat

image grace_grimace2 = WhileSpeaking("gra", "grace_grimace2_talking", "grace_grimace2_nottalking")


image grace_smile2_nottalking = "images/grace/mouths/110059_01_parts_c025.png"

image grace_smile2_talking:
    "images/grace/mouths/110059_01_parts_c025.png"
    0.15
    "images/grace/mouths/110059_01_parts_c026.png"
    0.15
    repeat

image grace_smile2 = WhileSpeaking("gra", "grace_smile2_talking", "grace_smile2_nottalking")


image grace_smile3_nottalking = "images/grace/mouths/110059_01_parts_c034.png"

image grace_smile3_talking:
    "images/grace/mouths/110059_01_parts_c034.png"
    0.15
    "images/grace/mouths/110059_01_parts_c035.png"
    0.15
    repeat

image grace_smile3 = WhileSpeaking("gra", "grace_smile3_talking", "grace_smile3_nottalking")


# 036 and 037 are identical to 006 and 007.

image grace_frown3_nottalking = "images/grace/mouths/110059_01_parts_c038.png"

image grace_frown3_talking:
    "images/grace/mouths/110059_01_parts_c038.png"
    0.15
    "images/grace/mouths/110059_01_parts_c039.png"
    0.15
    repeat

image grace_frown3 = WhileSpeaking("gra", "grace_frown3_talking", "grace_frown3_nottalking")


# 040 and 041 are identical to 036 and 037



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

label grace_character_procedures:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image chapelday = "images/backgrounds/Sty_bg_0013_100_00.png"
    scene chapelday at middle

    show grace with dissolve
    gra "Oh... hello there.  I was just saying a prayer for my late husband."
    gra "...No, no.  Please, stay.  Actually, there is something I could use your help with."
    gra "You see..."

    gra "...Let me start with a brief story.  As you know, my husband and I were very happy together for a long time."

    show grace smile3
    gra "Believe it or not, I was actually a really joyful person.  My husband always used to say that my smile could brighten the entire room."

    show grace -smile3
    gra "However, things became very stressful for us when we first planned to defect from the Syndicate."
    gra "I was really anxious all the time, and... something my husband said back then has been on my mind lately."
    gra "He took me by the hand, and said, 'My dear, you look like you've forgotten how to smile.  If we can't even save your own heart, we can't hope to save our patients.  Please, be at ease, with me at least.'"
    gra "I... was annoyed at the time, and after his death, those words felt like a bitter cruelty to me."
    gra "After all, how could I smile in a world without him?"
    gra "And yet... when I pray for my husband, I sometimes feel as though he is pained by the suffering on my face."
    gra "I will never stop feeling sorrow and grief, but... I also do not wish to worry him."
    gra "After all, if he feels I have still 'forgotten how to smile,' surely he will never be at peace."
    gra "..."
    gra "...All this is to say... I wish to practice smiling, so that I can give some comfort to my husband in the next life."
    gra "Normally I would do this by myself, but I fear that I am no longer a good gauge of my own sincerity.  I feel as though an outside opinion may, therefore, be in order."
    gra "Would you please assist me in this endeavor?"
    gra "...Thank you, it means quite a lot to me."

    show grace neutral
    gra "This is my normal, neutral expression (neutral). Let me start by moving my eyes a little.  After all, I've heard that a smile starts with the eyes."

    show grace focused
    gra "This is a more focused face.  I want to convey my dedication to this endeavor with my eyes."

    show grace relaxed
    gra "Now I am attempting to convey a relaxed expression."

    show grace angry
    gra "This is more of an angry expression."

    show grace angry2
    gra "And a second angry expression (angry2)"

    show grace surprised
    gra "Let me now attempt to make a surprised face."

    show grace sad
    gra "Oh, this is hopeless.  Even now my endeavors feel foolish and sad (sad)."

    show grace sad2
    gra "If my husband sees me like this, he'll simply be distraught... (sad2)"

    show grace blank
    gra "Perhaps it would simply be better to wipe away all my emotions... (blank)"

    show grace surprised
    gra "...You think I should continue?"

    show grace focused
    gra "...You're right, of course.  I can't let my grief prevent me from doing this... for my husband's sake."

    show grace -focused
    gra "Very well.  If you believe I should proceed, I'll focus on my mouth muscles next."

    show grace grimace1
    gra "I know that the way I usually talk (grimace1) is very restrained and can make people uncomfortable."

    show grace grimace2
    gra "But... can I really smile?  A grimace (grimace2) like this feels more appropriate for how I feel."

    show grace frown1
    gra "...No, even if I feel like this... even if I must frown (frown1), I will continue."

    show grace frown2
    gra "I will simply exhaust every way I can frown (frown2) until my face has no choice."

    show grace frown3
    gra "...Yes, no more frowning (frown3).  I will attempt to smile."

    show grace smile1
    gra "Here I go!  (smile1)"

    show grace smile2
    gra "Or this one?"

    show grace smile3
    gra "...Although I fear I am far away from achieving a sincere smile... I feel at peace enough for this expression to feel genuine (smile 3)."
    gra "Thank you for your help and support.  I feel a little bit closer to my husband now, and you were the one who made that possible."
    gra "Perhaps once my quest to eliminate the Syndicate is over, I shall join you with a real smile on my face."

    hide grace with dissolve


    # This goes back to script

    jump testfiles
