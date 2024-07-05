    # Laxi Character Procedures File

    # Paste this file into a story if you want to use Laxi.  These procedures animate Laxi as a speaker.

define lax = Character("Laxi", callback=speaker("lax"))

    # This program assumes that the following folders exist:
    #     -"images/laxi"
    #     -"images/laxi/faces"
    #     -"images/laxi/mouths"

    # Laxi dynamically blinks and, while speaking, also moves her mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Laxi appear*:
    #  -->  show laxi with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Laxi's eyes*:
    #  -->  show laxi [keyword]
    #  List of eye keywords:
    #     -->  relaxed (the default option), relaxed2, angry, flinch,
    #          focused, sad, surprised, unfocused,
    #          corrupt_angry, corrupt_focused

    # *Changing Laxi's mouth*:
    #  -->  show laxi [keyword]
    #  List of mouth keywords:
    #     -->  mutter1 (the default option), frown1, frown2, grimace1, grimace2,
    #          pout1, shout1, smile1

    # *Writing dialogue for Laxi*:
    #  --> lax "[Laxi's line here]"

    # *Making Laxi disappear*:
    #  --> hide laxi with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage laxi:

    always "images/laxi/laxi_body.png"

    group face:

        # 444/1028, 276/1028:
        pos (0.43191, 0.26848)

        attribute relaxed default:
            "laxi_relaxed_eyes"

        attribute focused:
            "laxi_focused_eyes"

        attribute relaxed2:
            "laxi_relaxed2_eyes"

        attribute flinch:
            "laxi_flinch_eyes"

        attribute surprised:
            "laxi_surprised_eyes"

        attribute unfocused:
            "laxi_unfocused_eyes"

        attribute sad:
            "laxi_sad_eyes"

        attribute corrupt_focused:
            "laxi_corrupt_focused_eyes"

        attribute angry:
            "laxi_angry_eyes"

        attribute corrupt_angry:
            "laxi_corrupt_angry_eyes"


    group mouth:

        pos (0.43191, 0.26848)

        attribute mutter1 default:
            "laxi_mutter1"

        attribute frown1:
            "laxi_frown1"

        attribute smile1:
            "laxi_smile1"

        attribute pout1:
            "laxi_pout1"

        attribute grimace1:
            "laxi_grimace1"

        attribute frown2:
            "laxi_frown2"

        attribute grimace2:
            "laxi_grimace2"

        attribute shout1:
            "laxi_shout1"




## EYE animations start here.

image laxi_relaxed_eyes:
    "images/laxi/faces/100032_01_parts_c000.png"
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
    "images/laxi/faces/100032_01_parts_c001.png"
    0.05
    repeat

image laxi_focused_eyes:
    "images/laxi/faces/100032_01_parts_c003.png"
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
    "images/laxi/faces/100032_01_parts_c004.png"
    0.05
    repeat

image laxi_relaxed2_eyes:
    "images/laxi/faces/100032_01_parts_c009.png"
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
    "images/laxi/faces/100032_01_parts_c010.png"
    0.05
    repeat

image laxi_flinch_eyes:
    "images/laxi/faces/100032_01_parts_c011.png"
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
    "images/laxi/faces/100032_01_parts_c012.png"
    0.05
    repeat

image laxi_surprised_eyes:
    "images/laxi/faces/100032_01_parts_c013.png"
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
    "images/laxi/faces/100032_01_parts_c014.png"
    0.05
    repeat

image laxi_unfocused_eyes:
    "images/laxi/faces/100032_01_parts_c015.png"
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
    "images/laxi/faces/100032_01_parts_c016.png"
    0.05
    repeat

image laxi_sad_eyes:
    "images/laxi/faces/100032_01_parts_c025.png"
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
    "images/laxi/faces/100032_01_parts_c026.png"
    0.05
    repeat

image laxi_corrupt_focused_eyes:
    "images/laxi/faces/100032_01_parts_c027.png"
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
    "images/laxi/faces/100032_01_parts_c028.png"
    0.05
    repeat

image laxi_angry_eyes:
    "images/laxi/faces/100032_01_parts_c029.png"
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
    "images/laxi/faces/100032_01_parts_c030.png"
    0.05
    repeat

image laxi_corrupt_angry_eyes:
    "images/laxi/faces/100032_01_parts_c031.png"
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
    "images/laxi/faces/100032_01_parts_c032.png"
    0.05
    repeat



# MOUTH animations start here.

# Note:  'grimace's here are animated in reverse from usual (teeth not shown on resting).

image laxi_mutter1_nottalking = "images/laxi/mouths/100032_01_parts_c005.png"

image laxi_mutter1_talking:
    "images/laxi/mouths/100032_01_parts_c005.png"
    0.15
    "images/laxi/mouths/100032_01_parts_c006.png"
    0.15
    repeat

image laxi_mutter1 = WhileSpeaking("lax", "laxi_mutter1_talking", "laxi_mutter1_nottalking")


image laxi_frown1_nottalking = "images/laxi/mouths/100032_01_parts_c007.png"

image laxi_frown1_talking:
    "images/laxi/mouths/100032_01_parts_c007.png"
    0.15
    "images/laxi/mouths/100032_01_parts_c008.png"
    0.15
    repeat

image laxi_frown1 = WhileSpeaking("lax", "laxi_frown1_talking", "laxi_frown1_nottalking")


image laxi_smile1_nottalking = "images/laxi/mouths/100032_01_parts_c017.png"

image laxi_smile1_talking:
    "images/laxi/mouths/100032_01_parts_c018.png"
    0.15
    "images/laxi/mouths/100032_01_parts_c017.png"
    0.15
    repeat

image laxi_smile1 = WhileSpeaking("lax", "laxi_smile1_talking", "laxi_smile1_nottalking")


image laxi_pout1_nottalking = "images/laxi/mouths/100032_01_parts_c019.png"

image laxi_pout1_talking:
    "images/laxi/mouths/100032_01_parts_c020.png"
    0.15
    "images/laxi/mouths/100032_01_parts_c019.png"
    0.15
    repeat

image laxi_pout1 = WhileSpeaking("lax", "laxi_pout1_talking", "laxi_pout1_nottalking")


image laxi_grimace1_nottalking = "images/laxi/mouths/100032_01_parts_c021.png"

image laxi_grimace1_talking:
    "images/laxi/mouths/100032_01_parts_c022.png"
    0.15
    "images/laxi/mouths/100032_01_parts_c021.png"
    0.15
    repeat

image laxi_grimace1 = WhileSpeaking("lax", "laxi_grimace1_talking", "laxi_grimace1_nottalking")


image laxi_frown2_nottalking = "images/laxi/mouths/100032_01_parts_c023.png"

image laxi_frown2_talking:
    "images/laxi/mouths/100032_01_parts_c024.png"
    0.15
    "images/laxi/mouths/100032_01_parts_c023.png"
    0.15
    repeat

image laxi_frown2 = WhileSpeaking("lax", "laxi_frown2_talking", "laxi_frown2_nottalking")


image laxi_grimace2_nottalking = "images/laxi/mouths/100032_01_parts_c033.png"

image laxi_grimace2_talking:
    "images/laxi/mouths/100032_01_parts_c034.png"
    0.15
    "images/laxi/mouths/100032_01_parts_c033.png"
    0.15
    repeat

image laxi_grimace2 = WhileSpeaking("lax", "laxi_grimace2_talking", "laxi_grimace2_nottalking")


# 035/036 is the same as 007/008


image laxi_shout1_nottalking = "images/laxi/mouths/100032_01_parts_c037.png"

image laxi_shout1_talking:
    "images/laxi/mouths/100032_01_parts_c038.png"
    0.15
    "images/laxi/mouths/100032_01_parts_c037.png"
    0.15
    repeat

image laxi_shout1 = WhileSpeaking("lax", "laxi_shout1_talking", "laxi_shout1_nottalking")



# 039/040 is the same as 037/038




transform laxi_face_pos:
#    xalign 0.43191
#    yalign 0.26848

# was relative to laxi image, not the frame.  Need to add a fudge factor.
    xalign 0.500
    yalign 0.300






# The game starts here.

label laxi_character_procedures:

    # I'd like to use the ▷ and ◁ characters but Ren'py rejects it in dialogue for some reason.


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image drawbridgeday = "images/backgrounds/Sty_bg_0017_100_00.png"
    scene drawbridgeday at middle

    show laxi with dissolve
    lax "Greetings.  You may be wondering why I summoned you here."
    lax "Allow me to explain.  The reason pertains to a disagreement between m--\n\n>>It's because Laxi's unfriendly!<<"
    lax "Ahem.  Mascula believes that my current expressional algortithms lack a siginificant enough variation.\n\n>>Laxi, you act all emotionless! It would help us if you showed more empathy.<<"
    lax "I do not understand your insistance on the matter, Mascula.  Information in conversation is conveyed via a series of verbal phonemes."
    lax "Facial expressions are merely aethetic and secondary.\n\n>>Laxi, it's about tone and subtext...<<"
    lax "...Regardless, I suppose you see the extent of the conflict.\n\n>>Anyway, that's how it is!<<"
    lax "Therefore, I would ask you to evaluate a subset of my facial expressions and tell me whether you think they are sufficient for conveying information."
    lax "That will hopefully put Mascula's complaints to rest.\n\n>>Hey, they're completely valid complaints!  Even Luca gets weirded out by it!<<"
    lax "...(ahem) Silence is required for optimal experimental conditions.\n\n>>Yeah, yeah, whatever...<<"

    show laxi relaxed mutter1
    lax "These are my 'relaxed' and 'mutter1' settings.\n\n>>This makes us look unfeeling and cold, Laxi!<<"

    show laxi relaxed2 frown1
    lax "...These are my 'relaxed2' and 'frown1' settings.\n\n>>Oh come on, this is basically the same face!<<"

    show laxi angry frown2
    lax "(ahem) THESE are my 'angry' and 'frown2' settings.  Which are starting to describe my current emotional state.\n\n>>Oh cool, so there ARE some emotions you can express!  Too bad they're mean ones!!!<<"

    show laxi flinch grimace1
    lax "Suppressing Mascula.  Ngh... These... are my 'flinch' and 'grimace1'... settings..."

    show laxi focused grimace2
    lax "These... are... my... 'focused'... and... 'grimace2'... sett-  sett..."

    show laxi corrupt_focused pout1
    lax "--SETT--SETT--SETT-----CORRUPTION DETECTED.  DE-DEFAULTING TO 'corrupt_focused' AND 'pout1' SETTINGS\n\n>>Oh no!!  Laxi forcibly suppressed my influcence, but that caused her to become corrupted again!!<<"

    show laxi corrupt_angry shout1
    lax "CORRUPTION AT 83 PERCENT; SWITCHING TO 'corrupt_angry' AND 'shout1' SETTINGS.\n\n>>Ok, I'm going to try to forcibly reboot Laxi!  Let's hope this works...!!!<<"

    show laxi unfocused mutter1
    lax "Corruption... termination protocols initiated...  ...defaulting to 'mutter1' mouth.  Recalibrating optical cameras.  Initiating 'unfocused' protocol for maintenance.\n\n>>Whew, I think it worked!<<"

    show laxi surprised
    lax "...Mascula?  What happened?  I'm feeling very disoriented and 'surprised'...\n\n>>You became recorrupted when you tried to forcibly suppress me...<<"

    show laxi sad
    lax "('sad')>>I'm sorry Laxi, I shouldn't have been complaining so much.  I know you want to connect with people too, but I should let you do it at your own pace...<<"
    lax "No, I am also at fault, Mascula.  I know that you have sacrificed much to keep me stable and I should not shut you out just to make a point.  We almost hurt people thanks to my recklessness."

    show laxi sad smile1
    lax ">>Maybe we should call a truce for now.  Besides, I think we've honestly had enough \"emotions\" for one day...<<\n\nThank you, Mascula.  Engaging 'smile1' protocol to demonstrate gratitude."

    show laxi surprised
    lax ">>Hey, that's right!  You got it!  I think a smile looks good on us.<<\n\nPerhaps you are right.  I concur."

    hide laxi with dissolve


    # This goes back to script

    jump testfiles
