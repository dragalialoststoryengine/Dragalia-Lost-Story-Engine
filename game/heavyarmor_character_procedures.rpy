    # Heavy Armor Character Procedures File

    # Paste this file into a story if you want to use a heavily armored character.  These procedures animate heavily armored characters as a speaker.



# In the past, Dyrenell generals / officers would have their own speaker and would usually be heavily armored soldiers.

define arm_guard = Character ("Armored Guard", callback=speaker("arm_guard"))

define gen_gen = Character("General", callback=speaker("gen_gen"))

define gen_off = Character("Officer", callback=speaker("gen_off"))


define alb_gen = Character("Alberian General", callback=speaker("alb_gen"))

define alb_off = Character("Alberian Officer", callback=speaker("alb_off"))


define nalb_gen = Character("New Alberian General", callback=speaker("nalb_gen"))

define nalb_off = Character("New Alberian Officer", callback=speaker("nalb_off"))


define dyre_gen = Character("Dyrenell General", callback=speaker("dyre_gen"))

define dyre_off = Character("Dyrenell Officer", callback=speaker("dyre_off"))


# Saboa, one of Prince Emile's guards, is a recurring character that gets his own speaker and image (same as dyrenell heavy armor 3)

define sabo = Character("Saboa", callback=speaker("sabo"))





    # This program assumes that the following folders exist:
    #     -"images/soldiers/heavy armor"

    # Heavily armored soldiers has no image procedures.

    # FUNCTIONS:

    # *Making a heavily armored soldier appear*:
    #  -->  show heavyarmor with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing the heavily armored soldier's appearance*:
    #  -->  show heavyarmor [keyword]
    #
    #       Keywords:  alberia (default), new_alberia, dyrenell, dyrenell_blue



    # *Writing dialogue for these characters*:
    #  --> arm_guard "[Armored Guard's line here]"
    #  --> gen_gen "[General's line here]"
    #  --> gen_off "[Officer's line here]"
    #  --> alb_gen "[Alberian General's line here]"
    #  --> alb_off "[Alberian Officer's line here]"
    #  --> nalb_gen "[New Alberian General's line here]"
    #  --> nalb_off "[New Alberian Officer's line here]"
    #  --> dyre_gen "[Dyrenell General's line here]"
    #  --> dyre_off "[Dyrenell Officer's line here]"
    #  --> sabo "[Saboa's line here]"

    # *Making the heavily armored soldier disappear disappear*:
    #  --> hide heavyarmor with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage heavyarmor:

    group affiliation:

        attribute generic default:
            "images/soldiers/heavy armor/heavy_armor_1_body.png"

        attribute alberia:
            "images/soldiers/heavy armor/heavy_armor_2_body.png"

        attribute dyrenell:
            "images/soldiers/heavy armor/heavy_armor_3_body.png"

        attribute dyrenell_blue:
            "images/soldiers/heavy armor/heavy_armor_5_body.png"



image saboa = "images/soldiers/heavy armor/heavy_armor_3_body.png"




# The game starts here.

label heavyarmor_character_procedures:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image capitol = "images/backgrounds/Sty_bg_0005_100_00.png"
    scene capitol with fade

    show heavyarmor with dissolve
    arm_guard "Armored guard, reporting for duty! (arm_guard speaker)"

    show heavyarmor generic
    gen_off "(generic) Volunteer heavy armor unit officer, reporting for duty! (gen_off speaker)"

    show heavyarmor generic
    gen_gen "Volunteer heavy armor unit general, reporting for duty!  (gen_gen speaker)"

    show heavyarmor alberia
    alb_off "(alberia) Alberian heavy armor unit officer, reporting for duty!  (alb_off speaker)"

    alb_gen "Alberian heavy armor unit general, reporting for duty!  (alb_gen speaker)"

    nalb_off "New Alberian heavy armor unit officer, reporting for duty!  (nalb_off speaker)"

    nalb_gen "New Alberian heavy armor unit general, reporting for duty!  (nalb_gen speaker)"

    show heavyarmor dyrenell
    dyre_off "(dyrenell) Dyrenell heavy armor unit officer, reporting for duty!  (dyre_off speaker)"

    show heavyarmor dyrenell_blue
    dyre_gen "(dyrenell_blue) Dyrenell heavy armor unit general, reporting for duty!  (dyre_gen speaker)"

    hide heavyarmor with dissolve

    show saboa with dissolve
    sabo "Officer Saboa, reporting for duty, sir!  We must protect Prince Emile at all costs!!! (sabo speaker)"

    hide saboa with dissolve


    # This goes back to script

    jump npctestfiles
