    # Lapis Character Procedures File

    # Paste this file into a story if you want to use Lapis.  These procedures animate Lapis as a speaker.

define lapi = Character("Lapis", callback=speaker("lapi"))

    # This program assumes that the following folders exist:
    #     -"images/lapis"
    #     -"images/lapis/faces"
    #     -"images/lapis/mouths"

    # Lapis dynamically blinks and, while speaking, also moves his mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Lapis appear*:
    #  -->  show lapis with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Lapis's eyes*:
    #  -->  show lapis [keyword]
    #  List of eye keywords:
    #     -->  neutral (default), angry, flinch, flinch2, focused, focused2, relaxed, sad, surprised, wink,
    #            closed_neutral

    # *Changing Lapis's mouth*:
    #  -->  show lapis [keyword]
    #  List of mouth keywords:
    #     -->  grin1 (default), grin2, grimace1, grimace2, grimace3, grimace4, mutter1, shout1, smile1, smile2
    #           grin1_closed

    # *Writing dialogue for Lapis*:
    #  --> lapi "[Lapis's line here]"

    # *Making Lapis disappear*:
    #  --> hide lapis with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage lapis:

    always "images/lapis/lapis_body.png"

    group face:

        # 452/1024, 238/1024:
        pos (0.441406, 0.2324219)

        attribute neutral default:
            "lapis_neutral_eyes"

        attribute closed_neutral:
            "images/lapis/faces/110370_01_parts_c001.png"

        attribute focused:
            "lapis_focused_eyes"

        attribute relaxed:
            "lapis_relaxed_eyes"

        attribute flinch:
            "lapis_flinch_eyes"
        
        attribute surprised:
            "lapis_surprised_eyes"
        
        attribute angry:
            "lapis_angry_eyes"

        attribute sad:
            "lapis_sad_eyes"

        attribute focused2:
            "lapis_focused2_eyes"

        attribute wink:
            "lapis_wink_eyes"

        attribute flinch2:
            "lapis_flinch2_eyes"




    group mouth:

        pos (0.441406, 0.2324219)

        attribute grin1 default:
            "lapis_grin1"

        attribute grin1_closed:
            "images/lapis/mouths/110370_01_parts_c005.png"

        attribute grimace1:
            "lapis_grimace1"

        attribute smile1:
            "lapis_smile1"

        attribute grimace2:
            "lapis_grimace2"
    
        attribute mutter1:
            "lapis_mutter1"

        attribute grin2:
            "lapis_grin2"

        attribute grimace3:
            "lapis_grimace3"

        attribute shout1:
            "lapis_shout1"        

        attribute smile2:
            "lapis_smile2"

        attribute grimace4:
            "lapis_grimace4"





## EYE animations start here.

image lapis_neutral_eyes:
    "images/lapis/faces/110370_01_parts_c000.png"
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
    "images/lapis/faces/110370_01_parts_c001.png"
    0.05
    repeat

image lapis_focused_eyes:
    "images/lapis/faces/110370_01_parts_c003.png"
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
    "images/lapis/faces/110370_01_parts_c004.png"
    0.05
    repeat

image lapis_relaxed_eyes:
    "images/lapis/faces/110370_01_parts_c013.png"
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
    "images/lapis/faces/110370_01_parts_c014.png"
    0.05
    repeat

image lapis_flinch_eyes:
    "images/lapis/faces/110370_01_parts_c015.png"
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
    "images/lapis/faces/110370_01_parts_c016.png"
    0.05
    repeat

image lapis_surprised_eyes:
    "images/lapis/faces/110370_01_parts_c017.png"
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
    "images/lapis/faces/110370_01_parts_c018.png"
    0.05
    repeat

image lapis_angry_eyes:
    "images/lapis/faces/110370_01_parts_c019.png"
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
    "images/lapis/faces/110370_01_parts_c020.png"
    0.05
    repeat

image lapis_sad_eyes:
    "images/lapis/faces/110370_01_parts_c029.png"
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
    "images/lapis/faces/110370_01_parts_c030.png"
    0.05
    repeat

image lapis_focused2_eyes:
    "images/lapis/faces/110370_01_parts_c031.png"
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
    "images/lapis/faces/110370_01_parts_c032.png"
    0.05
    repeat

image lapis_wink_eyes:
    "images/lapis/faces/110370_01_parts_c039.png"
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
    "images/lapis/faces/110370_01_parts_c040.png"
    0.05
    repeat

image lapis_flinch2_eyes:
    "images/lapis/faces/110370_01_parts_c041.png"
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
    "images/lapis/faces/110370_01_parts_c042.png"
    0.05
    repeat



# MOUTH animations start here.

image lapis_grin1_nottalking = "images/lapis/mouths/110370_01_parts_c005.png"

image lapis_grin1_talking:
    "images/lapis/mouths/110370_01_parts_c006.png"
    0.15
    "images/lapis/mouths/110370_01_parts_c005.png"
    0.15
    repeat

image lapis_grin1 = WhileSpeaking("lapi", "lapis_grin1_talking", "lapis_grin1_nottalking")


image lapis_grimace1_nottalking = "images/lapis/mouths/110370_01_parts_c011.png"

image lapis_grimace1_talking:
    "images/lapis/mouths/110370_01_parts_c012.png"
    0.15
    "images/lapis/mouths/110370_01_parts_c011.png"
    0.15
    repeat

image lapis_grimace1 = WhileSpeaking("lapi", "lapis_grimace1_talking", "lapis_grimace1_nottalking")


image lapis_smile1_nottalking = "images/lapis/mouths/110370_01_parts_c021.png"

image lapis_smile1_talking:
    "images/lapis/mouths/110370_01_parts_c022.png"
    0.15
    "images/lapis/mouths/110370_01_parts_c021.png"
    0.15
    repeat

image lapis_smile1 = WhileSpeaking("lapi", "lapis_smile1_talking", "lapis_smile1_nottalking")


image lapis_grimace2_nottalking = "images/lapis/mouths/110370_01_parts_c023.png"

image lapis_grimace2_talking:
    "images/lapis/mouths/110370_01_parts_c024.png"
    0.15
    "images/lapis/mouths/110370_01_parts_c023.png"
    0.15
    repeat

image lapis_grimace2 = WhileSpeaking("lapi", "lapis_grimace2_talking", "lapis_grimace2_nottalking")


image lapis_mutter1_nottalking = "images/lapis/mouths/110370_01_parts_c025.png"

image lapis_mutter1_talking:
    "images/lapis/mouths/110370_01_parts_c026.png"
    0.15
    "images/lapis/mouths/110370_01_parts_c025.png"
    0.15
    repeat

image lapis_mutter1 = WhileSpeaking("lapi", "lapis_mutter1_talking", "lapis_mutter1_nottalking")


image lapis_grin2_nottalking = "images/lapis/mouths/110370_01_parts_c027.png"

image lapis_grin2_talking:
    "images/lapis/mouths/110370_01_parts_c028.png"
    0.15
    "images/lapis/mouths/110370_01_parts_c027.png"
    0.15
    repeat

image lapis_grin2 = WhileSpeaking("lapi", "lapis_grin2_talking", "lapis_grin2_nottalking")


image lapis_grimace3_nottalking = "images/lapis/mouths/110370_01_parts_c033.png"

image lapis_grimace3_talking:
    "images/lapis/mouths/110370_01_parts_c034.png"
    0.15
    "images/lapis/mouths/110370_01_parts_c033.png"
    0.15
    repeat

image lapis_grimace3 = WhileSpeaking("lapi", "lapis_grimace3_talking", "lapis_grimace3_nottalking")


image lapis_shout1_nottalking = "images/lapis/mouths/110370_01_parts_c035.png"

image lapis_shout1_talking:
    "images/lapis/mouths/110370_01_parts_c036.png"
    0.15
    "images/lapis/mouths/110370_01_parts_c035.png"
    0.15
    repeat

image lapis_shout1 = WhileSpeaking("lapi", "lapis_shout1_talking", "lapis_shout1_nottalking")


image lapis_smile2_nottalking = "images/lapis/mouths/110370_01_parts_c043.png"

image lapis_smile2_talking:
    "images/lapis/mouths/110370_01_parts_c044.png"
    0.15
    "images/lapis/mouths/110370_01_parts_c043.png"
    0.15
    repeat

image lapis_smile2 = WhileSpeaking("lapi", "lapis_smile2_talking", "lapis_smile2_nottalking")


image lapis_grimace4_nottalking = "images/lapis/mouths/110370_01_parts_c045.png"

image lapis_grimace4_talking:
    "images/lapis/mouths/110370_01_parts_c046.png"
    0.15
    "images/lapis/mouths/110370_01_parts_c045.png"
    0.15
    repeat

image lapis_grimace4 = WhileSpeaking("lapi", "lapis_grimace4_talking", "lapis_grimace4_nottalking")






# The test file script starts here.

label lapis_character_procedures:

    image city_neighborhood_night = "images/backgrounds/Sty_bg_0086_300_00.png"
    scene city_neighborhood_night with fade

    show lapis with dissolve
    lapi "Ah, if it isn't the seventh scion.  Out for a stroll, or were you just dying to see moi again?"

    show lapis neutral grin1
    lapi "(neutral grin1) I'm impressed that you managed to anticipate my escape route. And in record time, no less!"

    show lapis surprised grimace1
    lapi "(surprised grimace1) It seems you've brought quite the welcoming party with you as well."

    show lapis angry grin2
    lapi "(angry grin2) A large group of armed warriors is certainly ONE way to make a lady feel welcome."

    show lapis flinch grimace2
    lapi "(flinch grimace2) I'm wounded.  Are you really that against returning art to its proper place?"

    show lapis sad mutter1
    lapi "(sad mutter1) You and I are fundamentally similar.  We both dedicate our life to righting wrongs.  I was hoping we could find common ground."

    show lapis closed_neutral grin1_closed
    lapi "(closed_neutral grin1_closed) ..."

    show lapis focused grimace3
    lapi "(focused grimace3) ...I see.  Disappointing, but I'm glad there are people like you in the world who use your authority for good."

    show lapis focused2 grimace4
    lapi "(focused2 grimace4) It's a shame that you and I will have to part on bad terms again, though.  And it's an even bigger shame that I'll have to do this..."

    show lapis flinch2 shout1
    lapi "(flinch2 shout1) ...GUAAAARDS!!!  HELP!!!!  MERCENARIES ARE ASSAULTING ME!!!"

    show lapis wink smile1
    lapi "(wink smile1) Well, that ought to keep you occupied for a while.  Meanwhile, I think I'll take my chances with this manhole."

    show lapis relaxed smile2
    lapi "(relaxed smile2) After all, it's the job of the Blue Rose to make an impossible escape possible.  Adieu!"

    show lapis at fall_down
    pause 0.75
    
    hide lapis with dissolve


    # This goes back to script

    jump testfiles
