image dragonyule_cake = "images/items/dragonyule_cake.png"
image dragonyule_present = "images/items/dragonyule_present.png"
image hyper_bolt = "images/items/hyper_bolt.png"

transform item_pos:
    xalign 0.2
    yalign 0.2

transform item_pos2:
    xalign 0.8
    yalign 0.2



label item_procedures:

    scene black with fade

    show dragonyule_present at item_pos with dissolve

    "This is a Dragonyule Present.  It was from the first Dragonyule event and was a rare drop to exchange for items from the event store."

    hide dragonyule_present with dissolve
    show dragonyule_cake at item_pos with dissolve

    "This is a Dragonyule Cake.  It was from the first Dragonyule event and could be given as a gift to dragons to raise their friendship."

    hide dragonyule_cake with dissolve
    show hyper_bolt at item_pos with dissolve

    "This is a Hyper Bolt item.  It was from the Megaman crossover event."

    hide hyper_bolt with dissolve

    jump othertestfiles
