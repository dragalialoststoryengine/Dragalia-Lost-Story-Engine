
transform three_steps_enter_left:
    # Duration = 1.35

    alpha 0.0
    xpos -0.5
    parallel:
        linear 0.4 alpha 0.1
        linear 0.4 xpos -0.33
    linear 0.05 ypos 0.01
    linear 0.05 ypos 0.0
    parallel:
        linear 0.4 alpha 0.5
        linear 0.4 xpos -0.166
    linear 0.05 ypos 0.01
    linear 0.05 ypos 0.0
    parallel:
        linear 0.4 alpha 1.0
        linear 0.4 xpos -0.0
    linear 0.05 ypos 0.01
    linear 0.05 ypos 0.0 

transform three_steps_enter_right:
    # Duration = 1.35

    alpha 0.0
    xpos 0.5
    parallel:
        linear 0.4 alpha 0.1
        linear 0.4 xpos 0.33
    linear 0.05 ypos 0.01
    linear 0.05 ypos 0.0
    parallel:
        linear 0.4 alpha 0.5
        linear 0.4 xpos 0.166
    linear 0.05 ypos 0.01
    linear 0.05 ypos 0.0
    parallel:
        linear 0.4 alpha 1.0
        linear 0.4 xpos 0.0
    linear 0.05 ypos 0.01
    linear 0.05 ypos 0.0 


transform fly_offscreen_left:

    alpha 1.0
    parallel:
        linear 0.5 xpos -1.0
        linear 0.25 alpha 0.0

transform fly_offscreen_right:

    alpha 1.0
    parallel:
        linear 0.5 xpos 1.0
        linear 0.25 alpha 0.0

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



label combat_animation_test:

        scene field_day with fade

        show berserker at three_steps_enter_right

        bers "Hrrrnngggh..."

        show berserker at fly_offscreen_left

        bers "Take that!"

        show berserker at three_steps_enter_left

        bers "I return."

        show berserker at fly_offscreen_right

        bers "And off I go again!!!"

        show berserker at three_steps_enter_right

        bers "I am back again!"


        show berserker at big_swing_clockwise

        bers "HRRAAAGH!!!"

        show berserker at thrust_forward

        bers "En garde!!!"

        show berserker at big_swing_counterclockwise

        bers "HRRAAAGH (again)!!!"

        hide berserker with dissolve

        jump othertestfiles


