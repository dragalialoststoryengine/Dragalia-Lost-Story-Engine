#Combat Transforms Here

transform trudge_in_left:
    # Duration = 1.35

    alpha 0.0
    xpos -0.5
    parallel:
        linear 0.7 alpha 0.1
    parallel:
        linear 0.7 xpos -0.33
    linear 0.05 ypos 0.01
    linear 0.05 ypos 0.0
    parallel:
        linear 0.7 alpha 0.5
    parallel:
        linear 0.7 xpos -0.166
    linear 0.05 ypos 0.01
    linear 0.05 ypos 0.0
    parallel:
        linear 0.7 alpha 1.0
    parallel:
        linear 0.7 xpos -0.0
    linear 0.05 ypos 0.01
    linear 0.05 ypos 0.0 

transform trudge_in_right:
    # Duration = 1.35

    alpha 0.0
    xpos 0.5
    parallel:
        linear 0.7 alpha 0.1
    parallel:
        linear 0.7 xpos 0.33
    linear 0.05 ypos 0.01
    linear 0.05 ypos 0.0
    parallel:
        linear 0.7 alpha 0.5
    parallel:
        linear 0.7 xpos 0.166
    linear 0.05 ypos 0.01
    linear 0.05 ypos 0.0
    parallel:
        linear 0.7 alpha 1.0
    parallel:
        linear 0.7 xpos 0.0
    linear 0.05 ypos 0.01
    linear 0.05 ypos 0.0 


transform lunge_out_left:

    alpha 1.0
    parallel:
        linear 0.5 xpos -1.0
    parallel:
        linear 0.25 alpha 0.0

transform lunge_out_right:

    alpha 1.0
    parallel:
        linear 0.5 xpos 1.0
    parallel:
        linear 0.25 alpha 0.0

transform lunge_in_left:

    xpos -1.0
    alpha 0.0

    linear 0.25 xpos -0.5

    parallel:
        linear 0.25 xpos 0.0
    parallel:
        linear 0.25 alpha 1.0

transform lunge_in_right:

    xpos 1.0
    alpha 0.0

    linear 0.25 xpos 0.5

    parallel:
        linear 0.25 xpos 0.0
    parallel:
        linear 0.25 alpha 1.0

transform big_swing_clockwise:

    alpha 1.0
    pos (0.0, 0.0)

    xysize (1.0, 1.0)

    #linear 2.0 pos (0, 0) knot (-0.1, 0.05) knot (0, 0.1) knot (0.1, 0.05) knot (0, 0)

    linear 1.0 pos (0.0, 0.0) knot (-0.8, 0.05) knot (0, 0.1) knot (0.8, 0.05)
    linear 1.0 pos (0.0, 0.0) knot (-0.8, 0.05) knot (0, 0.1) knot (0.8, 0.05)

transform big_swing_counterclockwise:

    alpha 1.0
    pos (0.0, 0.0)

    xysize (1.0, 1.0)

    #linear 2.0 pos (0, 0) knot (-0.1, 0.05) knot (0, 0.1) knot (0.1, 0.05) knot (0, 0)

    linear 1.0 pos (0.0, 0.0) knot (0.8, 0.05) knot (0, 0.1) knot (-0.8, 0.05)
    linear 1.0 pos (0.0, 0.0) knot (0.8, 0.05) knot (0, 0.1) knot (-0.8, 0.05)


transform thrust_forward:

    alpha 1.0
    xysize (1.0, 1.0)
    pos (0.0, 0.0)

    anchor (0.5, 0.5)
    pos (0.5, 0.5)

    linear 0.1 xysize (1.25, 1.25)
    linear 0.1 xysize (1.0, 1.0)

    anchor (0.0, 0.0)
    pos (0.0, 0.0)

transform hit_shake:

    linear 0.075 xpos (0.02)
    linear 0.15 xpos (-0.02)
    linear 0.075 xpos (0.0)





# Story transforms here:

transform walk_in_right:

    alpha 0.0
    pos (0.3, 0.0)

    parallel:
        linear 0.66 pos (0.1, 0.0)
    parallel:
        linear 0.66 alpha 1.0

    linear 0.33 pos (0.0, 0.0)

transform walk_in_left:

    alpha 0.0
    pos (-0.3, 0.0)

    parallel:
        linear 0.66 pos (-0.1, 0.0)
    parallel:
        linear 0.66 alpha 1.0

    linear 0.33 pos (0.0, 0.0)


transform walk_out_right:

    alpha 1.0
    pos (0.0, 0.0)

    linear 0.33 pos (0.1, 0.0)

    parallel:
        linear 0.66 pos (0.3, 0.0)
    parallel:
        linear 0.66 alpha 0.0

transform walk_out_left:

    alpha 1.0
    pos (0.0, 0.0)

    linear 0.33 pos (-0.1, 0.0)

    parallel:
        linear 0.66 pos (-0.3, 0.0)
    parallel:
        linear 0.66 alpha 0.0


transform agree_dip:

    linear 0.15 ypos (0.035)
    linear 0.15 ypos (0.0)

transform disagree_shake:

    linear 0.15 xpos (0.02)
    linear 0.3 xpos (-0.02)
    linear 0.15 xpos (0.0)


label animation_test_procedures:

    image library = "images/backgrounds/Sty_bg_0042_100_00.png"
    scene library at middle

    menu:

        "What animation procedures do you want to see?"

        "{color=#000000}Combat animation test.{/color}":
            jump combat_animation_test

        "{color=#000000}Story animation test.{/color}":
            jump story_animation_test

        "{color=#000000}Back to other test files.{/color}":
            jump othertestfiles


label combat_animation_test:

        scene field_day with fade

        show berserker at lunge_in_right

        bers "I will take this hit for you!!"

        show berserker at hit_shake

        bers "ARGH!"

        show berserker at lunge_out_right

        bers "It has been a while since I've faced a blow that great!"

        show berserker at trudge_in_right

        bers "Hrrrnngggh... I am injured but I can still fight!!"

        show berserker at big_swing_clockwise
        pause 2.0
        show berserker at thrust_forward

        bers "Take this, my foe!"

        show berserker at lunge_out_left

        bers "Look out!  The enemy strikes like lightning!"

        show berserker at trudge_in_left

        bers "Heh.  The enemy's movements are slowing."


        show berserker at big_swing_counterclockwise
        pause 2.0
        show berserker at thrust_forward

        bers "En garde!!!"

        hide berserker with dissolve

        jump animation_test_procedures



label story_animation_test:

        image halidom_hall_day = "images/backgrounds/Sty_bg_0024_100_00.png"
        scene halidom_hall_day with fade

        show berserker at walk_in_right

        bers "...Ah, good morning."

        show berserker at agree_dip

        bers "Yes, I am prepared for the fiend extermination mission. I simply must eat first."

        show berserker at walk_out_left

        bers "I'm actually heading to the kitchen right now."

        show berserker at walk_in_left

        bers "Ah, my apologies, the kitchen is actually this way."

        show berserker at disagree_shake

        bers "How embarassing.  You would think I would know the castle better by this point."

        show berserker at walk_out_right

        bers "This should be the way to go."

        hide berserker with dissolve

        jump animation_test_procedures