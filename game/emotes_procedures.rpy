transform speechright_pos:
    pos (0.65, 0.15)

transform speechright_upperrightpos:
    pos (0.80, 0.075)

image angry_animation:
    "images/emotes/angry veins.png"
    # width 107/1028 = 0.10409, height 88/1028 = 0.08560


    # center moves from (0.65 + 0.10409/2, 0.15 + 0.08560/2) = (0.70205, 0.1928)
    # to (0.65 + 0.12/2, 0.15 + 0.12/2) = (0.71, 0.21)
    # SO:  I need to linear transform pos to -(0.71-0.70205, 0.21-0.1928) = (-0.00795, -0.0172)

    anchor (0.052045, 0.0428)

    linear 0.5 xysize (0.12, 0.12)
    # linear 0.5 pos (-0.00795, -0.0172)
    linear 0.5 xysize (0.10409, 0.08560)
    # linear 0.5 pos (0.0, 0.0)

    repeat

image bad_animation:
    "images/emotes/frustrated squiggle.png"

    linear 0.25 rotate 5
    linear 0.25 rotate -5


    repeat

image question_mark_animation:
    "images/emotes/question mark.png"

    rotate -60
    linear 0.25 rotate 0

    block:
        pause 1
        linear 0.2 rotate -30
        linear 0.2 rotate 10
        linear 0.05 rotate 0
        repeat 1000

image exclamation_point_animation:
    "images/emotes/exclamation point.png"

    # width 48/1028 = 0.046693, height 99/1028 = 0.096304
    anchor (0.052045, 0.0428)

    linear 0.25 xysize (0.0700395, 0.144456)
    # linear 0.5 pos (-0.00795, -0.0172)
    linear 0.25 xysize (0.046693, 0.096304)
    # linear 0.5 pos (0.0, 0.0)

    block:
        linear 0.5 xysize (0.0513623, 0.1059344)
        # linear 0.5 pos (-0.00795, -0.0172)
        linear 0.5 xysize (0.046693, 0.096304)
        # linear 0.5 pos (0.0, 0.0)
        repeat 1000

image note_animation:
    "images/emotes/music note smaller.png"

    linear 0.05 rotate -30
    linear 0.05 rotate 0
    linear 0.05 rotate -20
    linear 0.05 rotate 0
    linear 0.05 rotate -12
    linear 0.05 rotate 0
    linear 0.05 rotate -4
    linear 0.05 rotate 0
    pause 1
    repeat

image lightbulb_ray:
    "images/emotes/ray 1.png"
    
    pause 0.1
    alpha 0.0
    pause 0.1
    alpha 1.0

    pause 0.1
    alpha 0.0
    pause 0.1
    alpha 1.0

    pause 0.1
    alpha 0.0
    pause 0.1
    alpha 1.0

    pause 1

    repeat

image lightbulb_flicker:
    "images/emotes/lightbulb glow.png"
    alpha 0.0
    pause 0.1
    alpha 1.0
    pause 0.1
    alpha 0.0

    pause 0.1
    alpha 1.0
    pause 0.1
    alpha 0.0

    pause 0.1
    alpha 1.0
    pause 0.1
    alpha 0.0

    pause 1
    
    repeat


layeredimage lightbulb_animation:
    always "images/emotes/lightbulb.png"

    group flicker:

        attribute light_on default:
            "lightbulb_flicker"

    group ray_1:

        pos (-0.035, -0.055)
        rotate -30

        attribute lightbulb_ray default:
            "lightbulb_ray"

    group ray_2:

        pos (0.025, -0.06)

        attribute lightbulb_ray default:
            "lightbulb_ray"

    group ray_3:

        pos (0.05, -0.05)
        rotate 30

        attribute lightbulb_ray default:
            "lightbulb_ray"

image heart_animation:

    "images/emotes/heart.png"
    pos (-0.1, -0.1)
    xysize (0.1163, 0.1297)
    rotate -10

    parallel:
        linear 0.25 rotate 2
        linear 0.25 xysize (0.08463, 0.09436)
        linear 0.25 pos (0, 0)

    block:
        linear 0.4 rotate 8
        linear 0.4 rotate -8
        repeat 1000


image sweatdrop_a_moving:
    "images/emotes/sweat drop.png"

    ## rotate -2
    parallel:
        linear 0.4 pos (0.02, 0)
        # linear 0.4 rotate 2
    parallel:
        linear 0.2 pos (0.03, 0)
        linear 0.2 alpha 0.0
        # linear 0.2 rotate 3
    pos (-0.3, 0)
    # rotate -3
    parallel:
        linear 0.2 pos (0, 0)
        linear 0.2 alpha 1.1
        #linear 0.2 rotate -2

    repeat


image sweatdrop_b_moving:
    "images/emotes/sweat drop.png"
    xysize (0.06, 0.035)


    parallel:
        linear 0.4 pos (0.02, 0)
        # linear 0.4 rotate 2
    parallel:
        linear 0.2 pos (0.03, 0)
        linear 0.2 alpha 0.0
        # linear 0.2 rotate 3
    pos (-0.3, 0)
    # rotate -3
    parallel:
        linear 0.2 pos (0, 0)
        linear 0.2 alpha 1.1
        #linear 0.2 rotate -2

    repeat



layeredimage sweat_animation:
    always "sweatdrop_a_moving"

    group sweatdrop2:
        pos (0.01, 0.027)

        attribute sweatdrop_b default:
            rotate 30
            "sweatdrop_b_moving"



layeredimage speechright:
    always "images/emotes/speech bubble right.png"

    group emotion:

        attribute anger:
            pos (0.015, 0.02)
            "angry_animation"

        attribute bad:
            pos (-0.01, -0.01)
            "bad_animation"

        attribute question:
            pos (0.005, 0.001)
            "question_mark_animation"
        
        attribute exclamation:
            pos (0.053, 0.015)
            "exclamation_point_animation"

        attribute note:
            pos (0.01, 0.005)
            "note_animation"

        attribute lightbulb:
            pos (0.025, 0.0175)
            "lightbulb_animation"

        attribute heart:
            pos (0.005, 0.005)
            "heart_animation"

        attribute sweat:
            pos (0.025, 0.026)
            "sweat_animation"

label emotes_procedures:
    # This goes back to script

    scene halidom_hall with fade

    show euden with dissolve

    eud "Time to test some emotes!"

    show speechright anger at speechright_pos with dissolve
    play sound "audio/sound/anger.wav"
    eud "This should show an angry speech bubble on the right."

    show speechright bad
    play sound "audio/sound/bad.wav"
    eud "This should show a dissapointed speech bubble on the right."

    show speechright question
    play sound "audio/sound/question.wav"
    eud "This should show a question mark speech bubble on the right."
    
    show speechright exclamation
    play sound "audio/sound/exclamation.wav"
    eud "This should show an exclamation point speech bubble on the right."

    show speechright note
    play sound "audio/sound/note.wav"
    eud "This should show a music note speech bubble on the right."

    show speechright lightbulb
    play sound "audio/sound/inspiration.wav"
    eud "This should show a lightbulb speech bubble on the right."

    show speechright heart
    play sound "audio/sound/heart.wav"
    eud "This should show a heart speech bubble on the right."

    show speechright sweat
    play sound "audio/sound/sweat.wav"
    eud "This should show a sweat drop bubble on the right."

    jump othertestfiles