    # Lowen Character Procedures File

    # Paste this file into a story if you want to use Lowen.  These procedures animate Lowen as a speaker.

define low = Character("Lowen", callback=speaker("low"))

    # This program assumes that the following folders exist:
    #     -"images/lowen"
    #     -"images/lowen/faces"
    #     -"images/lowen/mouths"

    # Lowen dynamically blinks and, while speaking, also moves his mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Lowen appear*:
    #  -->  show lowen with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Lowen's eyes*:
    #  -->  show lowen [keyword]
    #  List of eye keywords:
    #     -->  neutral (the default option), neutral2, angry, flinch,
    #          focused, relaxed, sad, surprised, closed_neutral

    # *Changing Lowen's mouth*:
    #  -->  show lowen [keyword]
    #  List of mouth keywords:
    #     -->  smile1 (the default option), smile2, smile3, frown1, frown2, grimace1,
    #          mutter1, shout1, closed_frown1

    # *Writing dialogue for Lowen*:
    #  --> low "[Lowen's line here]"

    # *Making Lowen disappear*:
    #  --> hide lowen with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage lowen:

    always "images/lowen/lowen_body.png"

    group face:

        # 449/1024, 271/1024:
        pos (0.43848, 0.26465)

        attribute neutral default:
            "lowen_neutral_eyes"

        attribute closed_neutral:
            "images/lowen/faces/110257_01_parts_c001.png"

        attribute focused:
            "lowen_focused_eyes"

        attribute surprised:
            "lowen_surprised_eyes"
        
        attribute flinch:
            "lowen_flinch_eyes"
                
        attribute neutral2:
            "lowen_neutral2_eyes"
                        
        attribute relaxed:
            "lowen_relaxed_eyes"
                        
        attribute sad:
            "lowen_sad_eyes"
                        
        attribute angry:
            "lowen_angry_eyes"


    group mouth:

        pos (0.43848, 0.26465)

        attribute smile1 default:
            "lowen_smile1"

        attribute frown1:
            "lowen_frown1"
        
        attribute closed_frown1:
            "images/lowen/mouths/110257_01_parts_c007.png"
        
        attribute smile3:
            "lowen_smile3"
                    
        attribute grimace1:
            "lowen_grimace1"
        
        attribute frown2:
            "lowen_frown2"
                
        attribute smile2:
            "lowen_smile2"
                
        attribute mutter1:
            "lowen_mutter1"
                
        attribute shout1:
            "lowen_shout1"




## EYE animations start here.

image lowen_neutral_eyes:
    "images/lowen/faces/110257_01_parts_c000.png"
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
    "images/lowen/faces/110257_01_parts_c001.png"
    0.05
    repeat

image lowen_focused_eyes:
    "images/lowen/faces/110257_01_parts_c002.png"
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
    "images/lowen/faces/110257_01_parts_c003.png"
    0.05
    repeat

image lowen_surprised_eyes:
    "images/lowen/faces/110257_01_parts_c009.png"
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
    "images/lowen/faces/110257_01_parts_c010.png"
    0.05
    repeat

image lowen_flinch_eyes:
    "images/lowen/faces/110257_01_parts_c011.png"
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
    "images/lowen/faces/110257_01_parts_c012.png"
    0.05
    repeat

image lowen_neutral2_eyes:
    "images/lowen/faces/110257_01_parts_c013.png"
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
    "images/lowen/faces/110257_01_parts_c014.png"
    0.05
    repeat

image lowen_relaxed_eyes:
    "images/lowen/faces/110257_01_parts_c015.png"
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
    "images/lowen/faces/110257_01_parts_c016.png"
    0.05
    repeat

image lowen_sad_eyes:
    "images/lowen/faces/110257_01_parts_c025.png"
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
    "images/lowen/faces/110257_01_parts_c026.png"
    0.05
    repeat

image lowen_angry_eyes:
    "images/lowen/faces/110257_01_parts_c027.png"
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
    "images/lowen/faces/110257_01_parts_c028.png"
    0.05
    repeat





# MOUTH animations start here.

# Note:  'grimace's here are animated in reverse from usual (teeth not shown on resting).

image lowen_smile1_nottalking = "images/lowen/mouths/110257_01_parts_c004.png"

image lowen_smile1_talking:
    "images/lowen/mouths/110257_01_parts_c004.png"
    0.15
    "images/lowen/mouths/110257_01_parts_c005.png"
    0.15
    repeat

image lowen_smile1 = WhileSpeaking("low", "lowen_smile1_talking", "lowen_smile1_nottalking")


image lowen_frown1_nottalking = "images/lowen/mouths/110257_01_parts_c007.png"

image lowen_frown1_talking:
    "images/lowen/mouths/110257_01_parts_c007.png"
    0.15
    "images/lowen/mouths/110257_01_parts_c008.png"
    0.15
    repeat

image lowen_frown1 = WhileSpeaking("low", "lowen_frown1_talking", "lowen_frown1_nottalking")


image lowen_smile3_nottalking = "images/lowen/mouths/110257_01_parts_c017.png"

image lowen_smile3_talking:
    "images/lowen/mouths/110257_01_parts_c017.png"
    0.15
    "images/lowen/mouths/110257_01_parts_c018.png"
    0.15
    repeat

image lowen_smile3 = WhileSpeaking("low", "lowen_smile3_talking", "lowen_smile3_nottalking")


image lowen_grimace1_nottalking = "images/lowen/mouths/110257_01_parts_c019.png"

image lowen_grimace1_talking:
    "images/lowen/mouths/110257_01_parts_c019.png"
    0.15
    "images/lowen/mouths/110257_01_parts_c020.png"
    0.15
    repeat

image lowen_grimace1 = WhileSpeaking("low", "lowen_grimace1_talking", "lowen_grimace1_nottalking")


image lowen_frown2_nottalking = "images/lowen/mouths/110257_01_parts_c021.png"

image lowen_frown2_talking:
    "images/lowen/mouths/110257_01_parts_c021.png"
    0.15
    "images/lowen/mouths/110257_01_parts_c022.png"
    0.15
    repeat

image lowen_frown2 = WhileSpeaking("low", "lowen_frown2_talking", "lowen_frown2_nottalking")


image lowen_smile2_nottalking = "images/lowen/mouths/110257_01_parts_c023.png"

image lowen_smile2_talking:
    "images/lowen/mouths/110257_01_parts_c023.png"
    0.15
    "images/lowen/mouths/110257_01_parts_c024.png"
    0.15
    repeat

image lowen_smile2 = WhileSpeaking("low", "lowen_smile2_talking", "lowen_smile2_nottalking")


image lowen_mutter1_nottalking = "images/lowen/mouths/110257_01_parts_c029.png"

image lowen_mutter1_talking:
    "images/lowen/mouths/110257_01_parts_c029.png"
    0.15
    "images/lowen/mouths/110257_01_parts_c030.png"
    0.15
    repeat

image lowen_mutter1 = WhileSpeaking("low", "lowen_mutter1_talking", "lowen_mutter1_nottalking")


image lowen_shout1_nottalking = "images/lowen/mouths/110257_01_parts_c033.png"

image lowen_shout1_talking:
    "images/lowen/mouths/110257_01_parts_c033.png"
    0.15
    "images/lowen/mouths/110257_01_parts_c034.png"
    0.15
    repeat

image lowen_shout1 = WhileSpeaking("low", "lowen_shout1_talking", "lowen_shout1_nottalking")








# The game starts here.

label lowen_character_procedures:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image woodsday = "images/backgrounds/Sty_bg_0073_100_00.png"
    scene woodsday at middle

    show lowen with dissolve
    low "Hi!  Thanks for meeting me here."

    show lowen neutral smile1
    low "(neutral smile1) I know it's probably an odd request to meet me out here in private."

    show lowen neutral2 smile2
    low "(neutral2 smile2) But I thought you would be able to help me.  See... I want to be more mature."

    show lowen focused smile3
    low "(focused smile3) You're really cool, and you manage a lot of responsibilities around the Halidom."

    show lowen flinch frown1
    low "(flinch frown1) But it seems like all I ever do is get taken care of by Louise, and Garuda too."

    show lowen angry frown2
    low "(angry frown2) It frustrates me that they're so worried about me all the time, so..."

    show lowen sad grimace1
    low "(sad grimace1) ...well, I can't help thinking that maybe somehow it's my fault, and I'm acting too childish."

    show lowen relaxed mutter1
    low "(relaxed mutter1) So, well... I want to act more like you.  You know... responsible, and stuff."

    show lowen closed_neutral closed_frown1
    low "(closed_neutral closed_frown1) ........."

    show lowen surprised shout1
    low "(surprised shout1) Oh! So what you're saying is I should focus less on SEEMING responsible and more on BEING responsible?"

    show lowen flinch smile1
    low "...I suppose you're right.  If I'm really trying to mature, I need to stop worrying about how other people see me."

    show lowen smile2
    low "Instead, I should just focus on making good choices."

    show lowen neutral2 smile3
    low "Thanks a bunch!  You always have good advice."
    low "I hope someday I'll be chock-full of wisdom just like you!"

    hide lowen with dissolve


    # This goes back to script

    jump testfiles
