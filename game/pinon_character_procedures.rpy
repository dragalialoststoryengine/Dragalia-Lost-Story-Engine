
    # Pinon Character Procedures File

    # Paste this file into a story if you want to use Pinon.  These procedures animate Pinon as a speaker.
    # You'll also need to paste THIS line into your actual script above the script label whenever you're using Pinon:

define pin = Character("Pinon", callback=speaker("pin"))

    # This program assumes that the following folders exist:
    #     -"images/pinon"
    #     -"images/pinon/faces"
    #     -"images/pinon/mouths"
    #     -"images/pinon/faces_bow"
    #     -"images/pinon/mouths_bow"

    # Pinon dynamically blinks and, while speaking, also moves her mouth along with the text scroll.



    # FUNCTIONS:

    # *Making Pinon appear*:
    #  -->  show pinon with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Pinon's eyes*:
    #  -->  show pinon [keyword]
    #  List of eye keywords:
    #     -->  focused (the default option), askance_blush, askance_cry(*), askance_sad, blank(*),
    #            closed_focused, furrowed, glow, glow2, neutral(*), relaxed, surprised
    #
    #    "(*) indicates a keyword for "NORMAL" Pinon that does not also exist for "BOW" Pinon!!!
    #    Do not actually include (*) in the code!!!

    # *Changing Pinon's mouth*:
    #  -->  show pinon [keyword]
    #  List of mouth keywords:
    #     -->  frown2 (the default option), frown1, frown3, blush_smile1,
    #            grimace1, mutter1, shout1, smile1, sweat_pout1(*), sweat_shout1, sweat_smile1(*)
    #
    #    "(*) indicates a keyword for "NORMAL" Pinon that does not also exist for "BOW" Pinon!!!
    #    Do not actually include (*) in the code!!!

    # *Writing dialogue for Pinon*:
    #  --> pin "[Pinon's line here]"

    # *Making Pinon disappear*:
    #  --> hide pinon with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # *Making Pinon (with a bow) appear*:
    #  -->  show pinon_bow with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Pinon (with a bow)'s body*:
    #  -->  show pinon_bow [keyword]
    #  List of body keywords:
    #     -->  bow (the default option), sigil

    # *Changing Pinon (with a bow)'s eyes*:
    #  -->  show pinon_bow [keyword]
    #  List of eye keywords:
    #     -->  focused (the default option), askance_blush, askance_sad,
    #            closed_focused, furrowed, glow, glow2, relaxed, surprised

    # *Changing Pinon (with a bow)'s mouth*:
    #  -->  show pinon_bow [keyword]
    #  List of mouth keywords:
    #     -->  frown2 (the default option), frown1, frown3, blush_smile1, 
    #            grimace1, mutter1, shout1, smile1, sweat_shout1

    # *Writing dialogue for Pinon (with a bow)*:
    #  --> pin "[Pinon's line here]"

    # *Making Pinon (with a bow) disappear*:
    #  --> hide pinon_bow with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)



    # # # # #


layeredimage pinon:

    always "images/pinon/pinon_body.png"

    group face:

        # 445/1024, 267/1024:
        pos (0.43457, 0.26074)

        attribute focused default:
            "pinon_focused_eyes"

        attribute closed_focused:
            "images/pinon/faces/110366_02_parts_c001.png"

        attribute glow:
            "pinon_glow_eyes"

        attribute relaxed:
            "pinon_relaxed_eyes"

        attribute furrowed:
            "pinon_furrowed_eyes"

        attribute surprised:
            "pinon_surprised_eyes"

        attribute askance_blush:
            "pinon_askance_blush_eyes"

        attribute askance_sad:
            "pinon_askance_sad_eyes"

        attribute glow2:
            "pinon_glow2_eyes"

        attribute neutral:
            "pinon_neutral_eyes"

        attribute blank:
            "pinon_blank_eyes"

        attribute askance_cry:
            "pinon_askance_cry_eyes"


    group mouth:

        pos (0.43457, 0.26074)

        attribute frown2 default:
            "pinon_frown2"

        attribute frown3:
            "pinon_frown3"

        attribute smile1:
            "pinon_smile1"

        attribute grimace1:
            "pinon_grimace1"

        attribute sweat_shout1:
            "pinon_sweat_shout1"

        attribute blush_smile1:
            "pinon_blush_smile1"
    
        attribute frown1:
            "pinon_frown1"
    
        attribute shout1:
            "pinon_shout1"
    
        attribute mutter1:
            "pinon_mutter1"
    
        attribute sweat_pout1:
            "pinon_sweat_pout1"
    
        attribute sweat_smile1:
            "pinon_sweat_smile1"




layeredimage pinon_bow:

    group body:
        attribute bow default:
            "images/pinon/pinon_body_bow.png"

        attribute sigil:
            "images/pinon/pinon_body_sigil.png"

    group face:

        # 468/1024, 276/1024:
        pos (0.45703, 0.26953)

        attribute focused default:
            "pinon_bow_focused_eyes"

        attribute closed_focused:
            "images/pinon/faces_bow/110366_01_parts_c001.png"

        attribute glow:
            "pinon_bow_glow_eyes"

        attribute relaxed:
            "pinon_bow_relaxed_eyes"

        attribute furrowed:
            "pinon_bow_furrowed_eyes"

        attribute surprised:
            "pinon_bow_surprised_eyes"

        attribute askance_blush:
            "pinon_bow_askance_blush_eyes"

        attribute askance_sad:
            "pinon_bow_askance_sad_eyes"

        attribute glow2:
            "pinon_bow_glow2_eyes"



    group mouth:

        pos (0.45703, 0.26953)

        attribute frown2 default:
            "pinon_bow_frown2"

        attribute frown3:
            "pinon_bow_frown3"

        attribute smile1:
            "pinon_bow_smile1"

        attribute grimace1:
            "pinon_bow_grimace1"

        attribute sweat_shout1:
            "pinon_bow_sweat_shout1"
        
        attribute blush_smile1:
            "pinon_bow_blush_smile1"

        attribute frown1:
            "pinon_bow_frown1"

        attribute shout1:
            "pinon_bow_shout1"

        attribute mutter1:
            "pinon_bow_mutter1"


## EYE animations start here.

image pinon_focused_eyes:
    "images/pinon/faces/110366_02_parts_c000.png"
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
    "images/pinon/faces/110366_02_parts_c001.png"
    0.05
    repeat

image pinon_bow_focused_eyes:
    "images/pinon/faces_bow/110366_01_parts_c000.png"
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
    "images/pinon/faces_bow/110366_01_parts_c001.png"
    0.05
    repeat


image pinon_glow_eyes:
    "images/pinon/faces/110366_02_parts_c002.png"
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
    "images/pinon/faces/110366_02_parts_c003.png"
    0.05
    repeat

image pinon_bow_glow_eyes:
    "images/pinon/faces_bow/110366_01_parts_c003.png"
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
    "images/pinon/faces_bow/110366_01_parts_c004.png"
    0.05
    repeat


image pinon_relaxed_eyes:
    "images/pinon/faces/110366_02_parts_c009.png"
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
    "images/pinon/faces/110366_02_parts_c010.png"
    0.05
    repeat

image pinon_bow_relaxed_eyes:
    "images/pinon/faces_bow/110366_01_parts_c010.png"
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
    "images/pinon/faces_bow/110366_01_parts_c011.png"
    0.05
    repeat


image pinon_furrowed_eyes:
    "images/pinon/faces/110366_02_parts_c011.png"
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
    "images/pinon/faces/110366_02_parts_c012.png"
    0.05
    repeat

image pinon_bow_furrowed_eyes:
    "images/pinon/faces_bow/110366_01_parts_c012.png"
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
    "images/pinon/faces_bow/110366_01_parts_c013.png"
    0.05
    repeat


image pinon_surprised_eyes:
    "images/pinon/faces/110366_02_parts_c013.png"
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
    "images/pinon/faces/110366_02_parts_c014.png"
    0.05
    repeat

image pinon_bow_surprised_eyes:
    "images/pinon/faces_bow/110366_01_parts_c014.png"
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
    "images/pinon/faces_bow/110366_01_parts_c015.png"
    0.05
    repeat


image pinon_askance_blush_eyes:
    "images/pinon/faces/110366_02_parts_c015.png"
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
    "images/pinon/faces/110366_02_parts_c016.png"
    0.05
    repeat

image pinon_bow_askance_blush_eyes:
    "images/pinon/faces_bow/110366_01_parts_c016.png"
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
    "images/pinon/faces_bow/110366_01_parts_c017.png"
    0.05
    repeat


image pinon_askance_sad_eyes:
    "images/pinon/faces/110366_02_parts_c025.png"
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
    "images/pinon/faces/110366_02_parts_c026.png"
    0.05
    repeat

image pinon_bow_askance_sad_eyes:
    "images/pinon/faces_bow/110366_01_parts_c026.png"
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
    "images/pinon/faces_bow/110366_01_parts_c027.png"
    0.05
    repeat


image pinon_glow2_eyes:
    "images/pinon/faces/110366_02_parts_c027.png"
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
    "images/pinon/faces/110366_02_parts_c028.png"
    0.05
    repeat

image pinon_bow_glow2_eyes:
    "images/pinon/faces_bow/110366_01_parts_c028.png"
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
    "images/pinon/faces_bow/110366_01_parts_c029.png"
    0.05
    repeat


#The following eye animations only apply to normal (non-combat) Pinon:

image pinon_neutral_eyes:
    "images/pinon/faces/110366_02_parts_c029.png"
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
    "images/pinon/faces/110366_02_parts_c030.png"
    0.05
    repeat

image pinon_blank_eyes:
    "images/pinon/faces/110366_02_parts_c037.png"
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
    "images/pinon/faces/110366_02_parts_c028.png"
    0.05
    repeat

image pinon_askance_cry_eyes:
    "images/pinon/faces/110366_02_parts_c038.png"
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
    "images/pinon/faces/110366_02_parts_c039.png"
    0.05
    repeat




# MOUTH animations start here.

image pinon_frown2_nottalking = "images/pinon/mouths/110366_02_parts_c004.png"

image pinon_frown2_talking:
    "images/pinon/mouths/110366_02_parts_c004.png"
    0.15
    "images/pinon/mouths/110366_02_parts_c005.png"
    0.15
    repeat

image pinon_frown2 = WhileSpeaking("pin", "pinon_frown2_talking", "pinon_frown2_nottalking")


image pinon_bow_frown2_nottalking = "images/pinon/mouths_bow/110366_01_parts_c005.png"

image pinon_bow_frown2_talking:
    "images/pinon/mouths_bow/110366_01_parts_c005.png"
    0.15
    "images/pinon/mouths_bow/110366_01_parts_c006.png"
    0.15
    repeat

image pinon_bow_frown2 = WhileSpeaking("pin", "pinon_bow_frown2_talking", "pinon_bow_frown2_nottalking")




image pinon_frown3_nottalking = "images/pinon/mouths/110366_02_parts_c007.png"

image pinon_frown3_talking:
    "images/pinon/mouths/110366_02_parts_c007.png"
    0.15
    "images/pinon/mouths/110366_02_parts_c008.png"
    0.15
    repeat

image pinon_frown3 = WhileSpeaking("pin", "pinon_frown3_talking", "pinon_frown3_nottalking")


image pinon_bow_frown3_nottalking = "images/pinon/mouths_bow/110366_01_parts_c008.png"

image pinon_bow_frown3_talking:
    "images/pinon/mouths_bow/110366_01_parts_c008.png"
    0.15
    "images/pinon/mouths_bow/110366_01_parts_c009.png"
    0.15
    repeat

image pinon_bow_frown3 = WhileSpeaking("pin", "pinon_bow_frown3_talking", "pinon_bow_frown3_nottalking")




image pinon_smile1_nottalking = "images/pinon/mouths/110366_02_parts_c017.png"

image pinon_smile1_talking:
    "images/pinon/mouths/110366_02_parts_c017.png"
    0.15
    "images/pinon/mouths/110366_02_parts_c018.png"
    0.15
    repeat

image pinon_smile1 = WhileSpeaking("pin", "pinon_smile1_talking", "pinon_smile1_nottalking")


image pinon_bow_smile1_nottalking = "images/pinon/mouths_bow/110366_01_parts_c018.png"

image pinon_bow_smile1_talking:
    "images/pinon/mouths_bow/110366_01_parts_c018.png"
    0.15
    "images/pinon/mouths_bow/110366_01_parts_c019.png"
    0.15
    repeat

image pinon_bow_smile1 = WhileSpeaking("pin", "pinon_bow_smile1_talking", "pinon_bow_smile1_nottalking")



image pinon_grimace1_nottalking = "images/pinon/mouths/110366_02_parts_c019.png"

image pinon_grimace1_talking:
    "images/pinon/mouths/110366_02_parts_c019.png"
    0.15
    "images/pinon/mouths/110366_02_parts_c020.png"
    0.15
    repeat

image pinon_grimace1 = WhileSpeaking("pin", "pinon_grimace1_talking", "pinon_grimace1_nottalking")


image pinon_bow_grimace1_nottalking = "images/pinon/mouths_bow/110366_01_parts_c020.png"

image pinon_bow_grimace1_talking:
    "images/pinon/mouths_bow/110366_01_parts_c020.png"
    0.15
    "images/pinon/mouths_bow/110366_01_parts_c021.png"
    0.15
    repeat

image pinon_bow_grimace1 = WhileSpeaking("pin", "pinon_bow_grimace1_talking", "pinon_bow_grimace1_nottalking")



image pinon_sweat_shout1_nottalking = "images/pinon/mouths/110366_02_parts_c021.png"

image pinon_sweat_shout1_talking:
    "images/pinon/mouths/110366_02_parts_c021.png"
    0.15
    "images/pinon/mouths/110366_02_parts_c022.png"
    0.15
    repeat

image pinon_sweat_shout1 = WhileSpeaking("pin", "pinon_sweat_shout1_talking", "pinon_sweat_shout1_nottalking")


image pinon_bow_sweat_shout1_nottalking = "images/pinon/mouths_bow/110366_01_parts_c022.png"

image pinon_bow_sweat_shout1_talking:
    "images/pinon/mouths_bow/110366_01_parts_c022.png"
    0.15
    "images/pinon/mouths_bow/110366_01_parts_c023.png"
    0.15
    repeat

image pinon_bow_sweat_shout1 = WhileSpeaking("pin", "pinon_bow_sweat_shout1_talking", "pinon_bow_sweat_shout1_nottalking")



image pinon_blush_smile1_nottalking = "images/pinon/mouths/110366_02_parts_c023.png"

image pinon_blush_smile1_talking:
    "images/pinon/mouths/110366_02_parts_c023.png"
    0.15
    "images/pinon/mouths/110366_02_parts_c024.png"
    0.15
    repeat

image pinon_blush_smile1 = WhileSpeaking("pin", "pinon_blush_smile1_talking", "pinon_blush_smile1_nottalking")


image pinon_bow_blush_smile1_nottalking = "images/pinon/mouths_bow/110366_01_parts_c024.png"

image pinon_bow_blush_smile1_talking:
    "images/pinon/mouths_bow/110366_01_parts_c024.png"
    0.15
    "images/pinon/mouths_bow/110366_01_parts_c025.png"
    0.15
    repeat

image pinon_bow_blush_smile1 = WhileSpeaking("pin", "pinon_bow_blush_smile1_talking", "pinon_bow_blush_smile1_nottalking")




image pinon_frown1_nottalking = "images/pinon/mouths/110366_02_parts_c031.png"

image pinon_frown1_talking:
    "images/pinon/mouths/110366_02_parts_c031.png"
    0.15
    "images/pinon/mouths/110366_02_parts_c032.png"
    0.15
    repeat

image pinon_frown1 = WhileSpeaking("pin", "pinon_frown1_talking", "pinon_frown1_nottalking")


image pinon_bow_frown1_nottalking = "images/pinon/mouths_bow/110366_01_parts_c030.png"

image pinon_bow_frown1_talking:
    "images/pinon/mouths_bow/110366_01_parts_c030.png"
    0.15
    "images/pinon/mouths_bow/110366_01_parts_c031.png"
    0.15
    repeat

image pinon_bow_frown1 = WhileSpeaking("pin", "pinon_bow_frown1_talking", "pinon_bow_frown1_nottalking")




image pinon_shout1_nottalking = "images/pinon/mouths/110366_02_parts_c033.png"

image pinon_shout1_talking:
    "images/pinon/mouths/110366_02_parts_c033.png"
    0.15
    "images/pinon/mouths/110366_02_parts_c034.png"
    0.15
    repeat

image pinon_shout1 = WhileSpeaking("pin", "pinon_shout1_talking", "pinon_shout1_nottalking")


image pinon_bow_shout1_nottalking = "images/pinon/mouths_bow/110366_01_parts_c034.png"

image pinon_bow_shout1_talking:
    "images/pinon/mouths_bow/110366_01_parts_c034.png"
    0.15
    "images/pinon/mouths_bow/110366_01_parts_c035.png"
    0.15
    repeat

image pinon_bow_shout1 = WhileSpeaking("pin", "pinon_bow_shout1_talking", "pinon_bow_shout1_nottalking")




image pinon_mutter1_nottalking = "images/pinon/mouths/110366_02_parts_c035.png"

image pinon_mutter1_talking:
    "images/pinon/mouths/110366_02_parts_c035.png"
    0.15
    "images/pinon/mouths/110366_02_parts_c036.png"
    0.15
    repeat

image pinon_mutter1 = WhileSpeaking("pin", "pinon_mutter1_talking", "pinon_mutter1_nottalking")


image pinon_bow_mutter1_nottalking = "images/pinon/mouths_bow/110366_01_parts_c032.png"

image pinon_bow_mutter1_talking:
    "images/pinon/mouths_bow/110366_01_parts_c032.png"
    0.15
    "images/pinon/mouths_bow/110366_01_parts_c033.png"
    0.15
    repeat

image pinon_bow_mutter1 = WhileSpeaking("pin", "pinon_bow_mutter1_talking", "pinon_bow_mutter1_nottalking")



#The following mouth animations only apply to normal (non-combat) Pinon:

image pinon_sweat_pout1_nottalking = "images/pinon/mouths/110366_02_parts_c040.png"

image pinon_sweat_pout1_talking:
    "images/pinon/mouths/110366_02_parts_c040.png"
    0.15
    "images/pinon/mouths/110366_02_parts_c041.png"
    0.15
    repeat

image pinon_sweat_pout1 = WhileSpeaking("pin", "pinon_sweat_pout1_talking", "pinon_sweat_pout1_nottalking")



image pinon_sweat_smile1_nottalking = "images/pinon/mouths/110366_02_parts_c042.png"

image pinon_sweat_smile1_talking:
    "images/pinon/mouths/110366_02_parts_c042.png"
    0.15
    "images/pinon/mouths/110366_02_parts_c043.png"
    0.15
    repeat

image pinon_sweat_smile1 = WhileSpeaking("pin", "pinon_sweat_smile1_talking", "pinon_sweat_smile1_nottalking")






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

label pinon_character_procedures:


    image courtyard_sunset = "images/backgrounds/Sty_bg_0027_200_00.png"
    scene courtyard_sunset at middle


    show pinon with dissolve
    pin "O-Oh!  Hello.  You have caught me in the midst of my training."
    hide pinon with dissolve
    show pinon_bow with dissolve
    pin "I raise and lower my bow until the motion is fluid and seamless."
    hide pinon_bow with dissolve

    show pinon focused frown2 with dissolve
    pin "(focused frown2) I should not stop halfway through my routine, but you may talk to me if you need to."
    hide pinon with dissolve
    show pinon_bow focused frown2 with dissolve
    pin "(focused frown2) As an apostle, I need to be able to multitask, and this allows me to exercise my mind and body."
    hide pinon_bow with dissolve

    show pinon glow frown1 with dissolve
    pin "(glow frown1) So, please fill me in about the situation on your mind."
    hide pinon with dissolve
    show pinon_bow glow frown1 with dissolve
    pin "(glow frown1) The relationship between the apostles and the Halidom is important, so I will do my part to maintain it."
    hide pinon_bow with dissolve

    show pinon glow2 frown3 with dissolve
    pin "(glow2 frown3) ...I understand.  If you really suspect that the sighting could have been a demon, I ought to get involved."
    hide pinon with dissolve
    show pinon_bow glow2 frown3 with dissolve
    pin "(glow2 frown3) As the most recent addition to the apostles, this will be a good opportunity to demonstrate my capability."
    hide pinon_bow with dissolve

    show pinon furrowed grimace1 with dissolve
    pin "(furrowed grimace1) ...Nevin says he wants to partner with me on this?  I have a sinking feeling about this..."
    hide pinon with dissolve
    show pinon_bow furrowed grimace1 with dissolve
    pin "(furrowed grimace1) There is a chance he will offload the heavy lifting to me while he investigates in the background..."
    hide pinon_bow with dissolve

    show pinon askance_blush blush_smile1 with dissolve
    pin "(askance_blush blush_smile1) O-Oh, thank you, I appreciate the vote of confidence!  B-But I should not speak badly about my senior, sorry...!"
    hide pinon with dissolve
    show pinon_bow askance_blush blush_smile1 with dissolve
    pin "(askance_blush blush_smile1) Nevin IS a highly capable apostle!  He is able to relax because he can handle situations even without his full effort."
    hide pinon_bow with dissolve

    show pinon askance_sad mutter1 with dissolve
    pin "(askance_sad mutter1) I cannot help but wonder... if I have to put in this much effort just to equal his level of success..."
    hide pinon with dissolve
    show pinon_bow askance_sad mutter1 with dissolve
    pin "(askance_sad mutter1) ...perhaps... the skill gap between us is one that I will not ever cross..."
    hide pinon_bow with dissolve

    show pinon surprised sweat_shout1 with dissolve
    pin "(surprised sweat_shout1) Th-That is not to say that I have given up!  That is why I am putting in all this training!"
    hide pinon with dissolve
    show pinon_bow surprised shout1 with dissolve
    pin "(surprised sweat_shout1) But wait... you think that my potential may be being limited by burnout?"
    hide pinon_bow with dissolve

    show pinon closed_focused shout1 with dissolve
    pin "(closed_focused shout1) Argh!  So are you saying that Nevin's skill stems from the fact that he is always well-rested?!"
    hide pinon with dissolve
    show pinon_bow closed_focused shout1 with dissolve
    pin "(closed_focused shout1) I... I suppose that I HAVE felt rather exhausted lately, given how hard I have been pushing myself!"

    show pinon_bow relaxed smile1
    pin "(relaxed smile1) In that case, perhaps I should file for a vacation once this current matter is dealt with."
    hide pinon_bow with dissolve
    show pinon relaxed smile1
    pin "(relaxed smile1) I must admit, now that you have proposed the idea, I already feel the stress leaving my body."

    show pinon blank sweat_pout1
    pin "(blank sweat_pout1) WH-WHAT DO YOU MEAN, \"NEVIN IS RUBBING OFF ON ME?!?\""

    show pinon askance_cry
    pin "(askance_cry) Y-You had better not tell him I said that, do you hear me?!?"
    pin "I can hear him making fun of me already! \"Seems like soon you're gonna be lazier than your Papa Bear\" or some nonsense!"

    show pinon neutral sweat_smile1
    pin "(neutral sweat_smile1) S-Seriously, let us just keep this between us, ok?"
    pin "Ha ha... ha ha......"

    hide pinon with dissolve

    show pinon_bow bow surprised sweat_shout1 with dissolve
    pin "(bow) N-NEVIN?!?  HOW LONG HAVE YOU BEEN LURKING THERE?!?"

    show pinon_bow sigil glow2
    pin "(sigil) TH-THAT'S IT!!!  I WILL NOT TAKE ANY MORE OF YOUR RIBBING!!!  SIGIL, RELEASE!!!"
    hide pinon_bow with dissolve


    # This goes back to script

    jump testfiles
