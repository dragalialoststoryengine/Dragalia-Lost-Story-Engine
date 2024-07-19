
transform three_steps_enter_left:
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

    parallel:
        linear 0.5 xpos -1.0
        linear 0.25 alpha 0.0

transform fly_offscreen_right:

    parallel:
        linear 0.5 xpos 1.0
        linear 0.25 alpha 0.0



label combat_animation_test:

        scene field_day with fade

        show berserker at three_steps_enter_right

        bers "Hrrraaaagggh..."

        show berserker at fly_offscreen_left

        bers "Take that!"

        show berserker at three_steps_enter_left

        bers "I return."

        show berserker at fly_offscreen_right

        bers "And off I go again!!!"


        jump othertestfiles