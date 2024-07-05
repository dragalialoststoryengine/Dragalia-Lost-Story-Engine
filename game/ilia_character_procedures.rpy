
    # Ilia Character Procedures File

    # Paste this file into a story if you want to use Ilia.  These procedures animate Ilia as a speaker.
    # You'll also need to paste THIS line into your actual script above the script label whenever you're using Ilia:

define ili = Character("Ilia", callback=speaker("ili"))

    # This program assumes that the following folders exist:
    #     -"images/ilia"
    #     -"images/ilia/faces"
    #     -"images/ilia/mouths"

    # Ilia dynamically blinks and, while speaking, also moves her mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Ilia appear*:
    #  -->  show ilia with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Ilia's eyes*:
    #  -->  show ilia [keyword]
    #  List of eye keywords:
    #     -->  relaxed (default), angry, flinch, focused, sad, serious, surprised
    #

    # *Changing Ilia's mouth*:
    #  -->  show ilia [keyword]
    #  List of mouth keywords:
    #     -->  smile1 (default), smile2, smile3, frown1, frown2, frown3, frown4,
    #          grimace1, grimace2, grin1

    # *Writing dialogue for Ilia*:
    #  --> ili "[Ilia's line here]"

    # *Making Ilia disappear*:
    #  --> hide ilia with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage ilia:

    always "images/ilia/ilia_body.png"

    group face:

        # 333/1028, 281/1028:
        pos (0.32393, 0.27335)

        attribute relaxed default:
            "ilia_relaxed_eyes"

        attribute focused:
            "ilia_focused_eyes"

        attribute flinch:
            "ilia_flinch_eyes"

        attribute surprised:
            "ilia_surprised_eyes"

        attribute sad:
            "ilia_sad_eyes"

        attribute serious:
            "ilia_serious_eyes"

        attribute angry:
            "ilia_angry_eyes"

    group mouth:

        pos (0.32393, 0.27335)

        attribute smile1 default:
            "ilia_smile1"

        attribute frown1:
            "ilia_frown1"

        attribute smile2:
            "ilia_smile2"

        attribute frown2:
            "ilia_frown2"

        attribute grimace1:
            "ilia_grimace1"

        attribute grin1:
            "ilia_grin1"

        attribute frown3:
            "ilia_frown3"

        attribute smile3:
            "ilia_smile3"

        attribute grimace2:
            "ilia_grimace2"

        attribute frown4:
            "ilia_frown4"

## EYE animations start here.

image ilia_relaxed_eyes:
    "images/ilia/faces/110367_01_parts_c000.png"
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
    "images/ilia/faces/110367_01_parts_c001.png"
    0.05
    repeat

image ilia_focused_eyes:
    "images/ilia/faces/110367_01_parts_c003.png"
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
    "images/ilia/faces/110367_01_parts_c004.png"
    0.05
    repeat

image ilia_flinch_eyes:
    "images/ilia/faces/110367_01_parts_c010.png"
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
    "images/ilia/faces/110367_01_parts_c011.png"
    0.05
    repeat

image ilia_surprised_eyes:
    "images/ilia/faces/110367_01_parts_c012.png"
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
    "images/ilia/faces/110367_01_parts_c013.png"
    0.05
    repeat

image ilia_sad_eyes:
    "images/ilia/faces/110367_01_parts_c014.png"
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
    "images/ilia/faces/110367_01_parts_c015.png"
    0.05
    repeat

image ilia_serious_eyes:
    "images/ilia/faces/110367_01_parts_c024.png"
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
    "images/ilia/faces/110367_01_parts_c025.png"
    0.05
    repeat

image ilia_angry_eyes:
    "images/ilia/faces/110367_01_parts_c026.png"
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
    "images/ilia/faces/110367_01_parts_c027.png"
    0.05
    repeat

# MOUTH animations start here.

image ilia_smile1_nottalking = "images/ilia/mouths/110367_01_parts_c005.png"

image ilia_smile1_talking:
    "images/ilia/mouths/110367_01_parts_c006.png"
    0.15
    "images/ilia/mouths/110367_01_parts_c005.png"
    0.15
    repeat

image ilia_smile1 = WhileSpeaking("ili", "ilia_smile1_talking", "ilia_smile1_nottalking")


image ilia_frown1_nottalking = "images/ilia/mouths/110367_01_parts_c008.png"

image ilia_frown1_talking:
    "images/ilia/mouths/110367_01_parts_c009.png"
    0.15
    "images/ilia/mouths/110367_01_parts_c008.png"
    0.15
    repeat

image ilia_frown1 = WhileSpeaking("ili", "ilia_frown1_talking", "ilia_frown1_nottalking")


image ilia_smile2_nottalking = "images/ilia/mouths/110367_01_parts_c016.png"

image ilia_smile2_talking:
    "images/ilia/mouths/110367_01_parts_c017.png"
    0.15
    "images/ilia/mouths/110367_01_parts_c016.png"
    0.15
    repeat

image ilia_smile2 = WhileSpeaking("ili", "ilia_smile2_talking", "ilia_smile2_nottalking")


image ilia_frown2_nottalking = "images/ilia/mouths/110367_01_parts_c018.png"

image ilia_frown2_talking:
    "images/ilia/mouths/110367_01_parts_c019.png"
    0.15
    "images/ilia/mouths/110367_01_parts_c018.png"
    0.15
    repeat

image ilia_frown2 = WhileSpeaking("ili", "ilia_frown2_talking", "ilia_frown2_nottalking")


image ilia_grimace1_nottalking = "images/ilia/mouths/110367_01_parts_c020.png"

image ilia_grimace1_talking:
    "images/ilia/mouths/110367_01_parts_c021.png"
    0.15
    "images/ilia/mouths/110367_01_parts_c020.png"
    0.15
    repeat

image ilia_grimace1 = WhileSpeaking("ili", "ilia_grimace1_talking", "ilia_grimace1_nottalking")


image ilia_grin1_nottalking = "images/ilia/mouths/110367_01_parts_c022.png"

image ilia_grin1_talking:
    "images/ilia/mouths/110367_01_parts_c023.png"
    0.15
    "images/ilia/mouths/110367_01_parts_c022.png"
    0.15
    repeat

image ilia_grin1 = WhileSpeaking("ili", "ilia_grin1_talking", "ilia_grin1_nottalking")


image ilia_frown3_nottalking = "images/ilia/mouths/110367_01_parts_c028.png"

image ilia_frown3_talking:
    "images/ilia/mouths/110367_01_parts_c029.png"
    0.15
    "images/ilia/mouths/110367_01_parts_c028.png"
    0.15
    repeat

image ilia_frown3 = WhileSpeaking("ili", "ilia_frown3_talking", "ilia_frown3_nottalking")


image ilia_smile3_nottalking = "images/ilia/mouths/110367_01_parts_c030.png"

image ilia_smile3_talking:
    "images/ilia/mouths/110367_01_parts_c031.png"
    0.15
    "images/ilia/mouths/110367_01_parts_c030.png"
    0.15
    repeat

image ilia_smile3 = WhileSpeaking("ili", "ilia_smile3_talking", "ilia_smile3_nottalking")


image ilia_grimace2_nottalking = "images/ilia/mouths/110367_01_parts_c032.png"

image ilia_grimace2_talking:
    "images/ilia/mouths/110367_01_parts_c033.png"
    0.15
    "images/ilia/mouths/110367_01_parts_c032.png"
    0.15
    repeat

image ilia_grimace2 = WhileSpeaking("ili", "ilia_grimace2_talking", "ilia_grimace2_nottalking")


image ilia_frown4_nottalking = "images/ilia/mouths/110367_01_parts_c034.png"

image ilia_frown4_talking:
    "images/ilia/mouths/110367_01_parts_c035.png"
    0.15
    "images/ilia/mouths/110367_01_parts_c034.png"
    0.15
    repeat

image ilia_frown4 = WhileSpeaking("ili", "ilia_frown4_talking", "ilia_frown4_nottalking")

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

label ilia_character_procedures:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image cottage = "images/backgrounds/Sty_bg_0059_100_00.png"
    scene cottage at middle

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    show ilia with dissolve
    ili "Hey, Mordecai!  I've been thinking about the problem you brought up earlier."

    show ilia focused grin1
    ili "When you told me that you had no idea what to do with your facial muscles since you just got them... yeah, that was a good point..."

    show ilia flinch smile1
    ili "It was kind of a lot to expect you to get the whole concept of 'human expressions' when even the concept of EMOTIONS is foreign to you..."

    show ilia relaxed
    ili "But... that's why I've decided to show you the ropes!"

    ili "See, humans have an entire portion of their brain that's entirely devoted to interpreting other people's emotions."
    ili "Since other people's emotions determine their actions a lot of the time, you could call it a survival instinct."
    ili "But, see, you're from another world, so you haven't needed to know any of that before."

    show ilia focused
    ili "Anyway, my thought is that I can show you how a bunch of different emotions look on MY face and tell you what they mean!"
    ili "That way, when you see somebody else making an expression, you'll have a point of reference to work off of."
    ili "Make sense?  Not really?  Well, I think it's worth a shot, so... here goes!"

    show ilia relaxed smile1
    ili "Ok, so right now, i'm pretty relaxed and content.  You can see my eyebrows are relaxed, and I also have a smile (smile1)."

    show ilia serious frown1
    ili "But if something came up that was concerning or warranted my attention, my eyebrows might get more focused, and I'd have a small frown (frown1) like this."

    show ilia flinch grimace1
    ili "Ok, now, let's say that I got injured or I had some internal pain.  My eyes would flinch like this, and I'd frown with my teeth, which is called a grimace (grimace1)."

    show ilia surprised frown2
    ili "'Is pain an emotion?' Oh, huh.  That's a good question.  I suppose it depends..."

    show ilia smile1
    ili "Oh!  Wait, this is a good opportunity!"

    show ilia surprised frown2
    ili "Did you see how when you asked that question, I didn't know the answer right away?  That's called being surprised, so my eyebrows went up and I frowned (frown2), but... in a different way?"

    show ilia sad
    ili "But there's a lot of other emotions, too.  For instance, when someone's sad, the corners of their eyes might droop, and they might frown (frown3) more obviously."

    show ilia grin1
    ili "They might try to hide it with a grin or something too (grin1), but it'll still be obvious from their eyes."

    show ilia surprised smile2
    ili "...'Do *I* ever hide my sadness?'  Uh... well, I dunno what to tell you... hahaha..."
    ili "...'Can smiles (smile2) be fake too?'  Look, this wasn't exactly supposed to be an interrogation of my emotions..."

    show ilia serious frown3
    ili "Oh.  Wait.  I want to show you something important."
    ili "...This expression?  I guess you could call it 'serious.'  With a frown (frown3), of course."
    ili "But Mordecai, I just thought of something you really should know."
    ili "Now, even though Meene and I have been kind to you, it doesn't mean that all people will treat you the same day."
    ili "So you need to be able to tell when people are in an agitated or hostile frame of mind.  Otherwise, you could wind up in danger."

    show ilia angry grimace2
    ili "When someone's angry, their eybrows come down like this.  And they may raise their voice or grimace (grimace2)."

    show ilia frown4
    ili "But even if it's just a small frown (frown4), some people can still have hostile intent, you can see it in their eyes."

    show ilia serious
    ili "If you run into someone who's looking at you like that, it could mean that they want to do harm to you."
    ili "So if that happens, I want you to be careful.  Get out of the situation if you can, or turn to somebody in the situation you can trust."

    show ilia surprised
    ili "'What if I'm the one who becomes angry?'  You're worried about becoming angry yourself."

    show ilia relaxed smile1
    ili "Well... I don't think that's very likely, since you're a really gentle person.  But in a situation like that..."

    show ilia sad
    ili "I guess you could... try to focus on WHY you're angry?  If you get angry and act impulsively, you could do something you regret."
    ili "But... if you get angry at me, or other people... well, I'd be sad, but I wouldn't be afraid of you.  I really care about you, Mordecai."

    show ilia relaxed grin1
    ili "Well... that's enough of that depressing topic for now!  Why don't we focus on studying up on some alchemy for now?  I've got a really cool idea for a design..."

    show ilia surprised grimace1
    ili "'What does DEPRESSING look like now?'  ...Oh boy, I think I unintentionally opened a huge can of worms here..."

    show ilia smile2
    ili "Ahahahaha...  Hoo boy..."


    hide ilia with dissolve

    # This goes back to script

    jump testfiles
