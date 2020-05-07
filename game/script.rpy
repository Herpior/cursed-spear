# The game should not be very long so the entirety of the script is written
# in this file.

# In this block we declare all the characters who have dialogue in the game

define c = Character("Camellia") # the cursed
define e = Character("Erica") # the survivor
define j = Character("Joe") # the prosecutor

init -4:

    default mood = ""
    image eri_mini = "erp [eri.dir][mood]"
    image cam_mini = "carp [cam.dir]"
    image joe_mini = "jorp [vil.dir]"

    image joe_copy_0 = "jorp [villagers[0].dir]"
    image joe_copy_1 = "jorp [villagers[1].dir]"
    image joe_copy_2 = "jorp [villagers[2].dir]"
    image joe_copy_3 = "jorp [villagers[3].dir]"
    image joe_copy_4 = "jorp [villagers[4].dir]"
    image joe_copy_5 = "jorp [villagers[5].dir]"
    image joe_copy_6 = "jorp [villagers[6].dir]"
    image joe_copy_7 = "jorp [villagers[7].dir]"
    image joe_copy_8 = "jorp [villagers[8].dir]"
    image joe_copy_9 = "jorp [villagers[9].dir]"
    image joe_copy_10 = "jorp [villagers[10].dir]"
    image joe_copy_11 = "jorp [villagers[11].dir]"
    image joe_copy_12 = "jorp [villagers[12].dir]"
    image joe_copy_13 = "jorp [villagers[13].dir]"
    image joe_copy_14 = "jorp [villagers[14].dir]"
    image joe_copy_15 = "jorp [villagers[15].dir]"
    image joe_copy_16 = "jorp [villagers[16].dir]"
    image joe_copy_17 = "jorp [villagers[17].dir]"

    image erp front:
        "eri_rpg front"
        #0.1
        #repeat
    image erp back:
        "eri_rpg back"
    image erp front_sad:
        "eri_rpg front_sad"
    image erp back_sad:
        "eri_rpg back"
    image erp front_spear:
        "eri_rpg front_spear"
    image erp back_spear:
        "eri_rpg back_spear"
        #0.1
        #repeat
    image erp front_angery = AnimationAt(["rpg/eri_rpg angery_0000.png", "rpg/eri_rpg angery_0001.png", "rpg/eri_rpg angery_0002.png", "rpg/eri_rpg angery_0003.png", "rpg/eri_rpg angery_0004.png", "rpg/eri_rpg angery_0005.png"])
    image erp back_angery = AnimationAt(["rpg/eri_rpg back_angery_0000.png", "rpg/eri_rpg back_angery_0001.png", "rpg/eri_rpg back_angery_0002.png", "rpg/eri_rpg back_angery_0003.png", "rpg/eri_rpg back_angery_0004.png", "rpg/eri_rpg back_angery_0005.png"])
    image erpx front_angery:
        "eri_rpg angery_0000"
        0.083
        "eri_rpg angery_0001"
        0.083
        "eri_rpg angery_0002"
        0.083
        "eri_rpg angery_0003"
        0.083
        "eri_rpg angery_0004"
        0.083
        "eri_rpg angery_0005"
        0.083
        repeat
    image erpx back_angery:
        "eri_rpg back_angery_0000"
        0.083
        "eri_rpg back_angery_0001"
        0.083
        "eri_rpg back_angery_0002"
        0.083
        "eri_rpg back_angery_0003"
        0.083
        "eri_rpg back_angery_0004"
        0.083
        "eri_rpg back_angery_0005"
        0.083
        repeat

    image carp front:
        "cam_rpg front"
    image carp back:
        "cam_rpg back"

    image jorp front:
        "joe_rpg front"
    image jorp back:
        "joe_rpg back"

transform charpos(x, y):
    xpos x
    ypos y
    xanchor 0.5
    yanchor 0.5

transform dual_right:
    xpos 0.7
    xanchor 0.5
    yanchor 1.0
    ypos 1.0
    zoom 0.6667


transform dual_left:
    xpos 0.3
    xanchor 0.5
    yanchor 1.0
    ypos 1.0
    zoom 0.6667

transform kiss_left:
    xpos 0.67
    xanchor 0.5
    yanchor 1.0
    ypos 1.0
    zoom 0.6667

transform kiss_to_left:
    xpos 0.72
    xanchor 0.5
    yanchor 1.0
    ypos 1.0
    zoom 0.6667
    ease 0.3 xpos 0.67

transform kiss_to_right:
    xpos 0.75
    xanchor 0.5
    yanchor 1.0
    ypos 1.0
    zoom 0.6667
    ease 0.3 xpos 0.8


transform rot(angel):
    rotate angel

transform bg_transform:
    zoom 0.6667

# The game starts here.

label start:

    python:
        # initialize the variables necessary for the story
        # at least until the parts where they are edited are finished
        caught = False
        dead = False
        killed = 0
        alive = 100

    # the main flow of the story
    e "I need to hurry!"
    play music "bgm/The Fragile Bliss Founded On Secrecy #74.mp3" fadein 2 fadeout 2

    call meeting_in_secret
    call the_final_date
    call running_into_the_forest
    if caught:
        jump burnt_as_witches
    call running_into_the_ruins
    call in_the_ruins
    call the_confrontation
    if dead:
        jump stabbed_to_death
    if killed == 0:
        jump on_the_run
    if alive == 0:
        jump a_massacre
    jump enemy_of_the_state

    # just leave the return here in case the jump would return back here
    # or something, idk, it isn't really necessary
    return

label meeting_in_secret:
    # Where you meet your girlfriend
    # RPG style segment

    $renpy.suspend_rollback(True)
    #show screen rpg_view("heart_of_light")
    scene bg rpg_backyard at bg_transform
    #show eri_rpg

    python:
        chars = [eri, cam]
        eri.x = 620.0
        eri.y = 600.0
        cam.x = 700.0
        cam.y = 54.0
        cam.dir = "front"
        mood = ""
    while eri.surface_dist(cam) > 4:
        #renpy.show("eri_rpg", at_list=[Transform(pos=(eri.x, eri.y))])
        #renpy.show("cam_rpg", at_list=[Transform(pos=(cam.x, cam.y))])
        python:
            renpy.pause(0.016)
            WaitForInput()
            #print(eri.dist(cam))
            update()


    $renpy.suspend_rollback(False)
    return

label the_final_date:
    # The date that shows the relationship between the two characters and
    # ends up in them being found out
    scene bg backyard at bg_transform
    show camellia normal at dual_right
    c "Ah, there you are!"
    show erica normal at dual_left with moveinleft
    e "Sorry, I'm late."
    c "It's all right."
    c "I'm just happy that you are here."

    show erica at kiss_left behind camellia
    show camellia at right
    with ease
    e "I missed you so."
    c ""

    scene cg the_kiss at bg_transform
    e "I wish we could stay like this forever." # the monkey paw twists a finger



    j "Camellia, where have you been, your father is looking for you."
    scene bg backyard at bg_transform
    show erica normal at kiss_to_left behind camellia
    show camellia normal at kiss_to_right

    show joe normal at left with moveinleft:
        zoom 0.6667
    play music "bgm/Persecuted, Belittled And Betrayed By The People #50.mp3" fadein 2 fadeout 2

    j "Wait, what are you doing?"
    j "I'll have you two come with me right this instant!"
    c "Run!"
    hide camellia
    hide erica
    with moveoutright
    return

label running_into_the_forest:
    # The run away from the village
    # RPG style segment

    $renpy.suspend_rollback(True)
    scene bg rpg_backyard at bg_transform

    #show eri_rpg
    #show cam_rpg
    #show joe_rpg
    python:
        chars = [eri, cam, vil]
        vil.x = 620.0
        vil.y = 600.0
        cam.x = 680.0
        cam.y = 64.0
        eri.x = 760
        eri.y = 64
        mood = "_sad"
        caught = False
    while eri.x < 1140 and not caught:
        #renpy.show("eri_rpg", at_list=[Transform(pos=(eri.x, eri.y))])
        #renpy.show("cam_rpg", at_list=[Transform(pos=(cam.x, cam.y))])
        python:
            renpy.pause(0.016)
            WaitForInput()
            cam.follow(eri)
            vil.follow(cam)
            if (vil.surface_dist(cam) < 1 or vil.surface_dist(eri) < 1):
                caught = True
            #print(eri.dist(cam))
            update()

    $renpy.suspend_rollback(False)
    return

label burnt_as_witches:
    # You are caught by the one who saw you
    # Bad end 1
    scene black
    play music "bgm/When What Is Known As Self Is Lost #79.mp3" fadein 2 fadeout 2
    "After staying in the jail for a week, you are finally brought back to the surface."
    "Sun's last rays blind you when they reach your eyes."
    "Once your eyes adjust to the light, the sight is breathtaking."
    "Or would be, if not for the pile of wood brought to the center of the square."
    "Being pulled closer towards the pile, you notice the figure of another woman, already tied to one of the pillars in the center of the pile."
    e "Camellia!!"
    c "Erica? Oh no."
    #c "I was hoping they would save at least you." #"I tried to make them at least let you go"
    "You are led to a pillar next to Camellia."
    e "At least we're together again."
    "You're tied tight to the pillar."
    "The ropes dig into your already sore body."
    "More people from the village is gathering to watch."
    #"Well, it's not every day that there's an event going on in here."
    "The kindlings are set ablaze, the smell of smoke fills the air."
    "As the fire spreads, the smog is making it harder to breathe."
    "The smell of burning flesh is awful but the pain creeping up your legs is worse."
    "With flames licking your body, every breath you take hits with searing pain in your lungs."
    "Not long after, the world turns to black and the pain becomes just a ghost."
    "A memory in the ocean of time."
    "You died, by the way."
    "As did Camellia."
    "Was this really all you could do?"
    return

label running_into_the_ruins:
    # The run away from the village
    # RPG style segment
    scene bg forest at bg_transform
    show camellia normal at dual_left
    c "Look, let's hide in those ruins."

    $renpy.suspend_rollback(True)
    scene bg rpg_temple at bg_transform
    python:
        chars = [eri, cam]
        cam.x = 200.0
        cam.y = 360.0
        eri.x = 328
        eri.y = 360
        mood = "_sad"
        temple_trigger.x = 640.0
        temple_trigger.y = 64.0
    while eri.y > 80 or eri.x < 200 or eri.x > 900:
        #renpy.show("eri_rpg", at_list=[Transform(pos=(eri.x, eri.y))])
        #renpy.show("cam_rpg", at_list=[Transform(pos=(cam.x, cam.y))])
        python:
            renpy.pause(0.016)
            WaitForInput()
            cam.follow(eri)
            update()
    $renpy.suspend_rollback(False)
    return

label in_the_ruins:
    # You think you are safe
    # The cursed object is found and activated
    scene bg temple at bg_transform
    show camellia normal at dual_right
    show erica normal at dual_left
    play music "bgm/Psychological Emotional Survival Of An Indignant Soul #69.mp3" fadein 2 fadeout 2
    c ""
    scene cg the_pendant at bg_transform
    "very sad things happen"
    scene cg the_curse at bg_transform
    play music "bgm/The Abyss Known As Oneself #39.mp3" fadein 2 fadeout 2
    c "It hurts so much, help me Erica!"
    return

label the_confrontation:
    # The villagers have found you and are approaching the temple
    # RPG style segment
    "hold down mouse button to slash with the spear."
    $renpy.suspend_rollback(True)
    scene bg rpg_temple at bg_transform
    play music "bgm/Negotiating The Boundary Between Self And World #85.mp3" fadein 2 fadeout 2
    #show screen mouse_tracker(mouse_down)
    python:
        villager_instance = villagers[:]
        villager_instance[0].x = 196
        villager_instance[0].y = 642
        villager_instance[1].x = 263
        villager_instance[1].y = 666
        villager_instance[2].x = 289
        villager_instance[2].y = 634
        villager_instance[3].x = 325
        villager_instance[3].y = 682
        villager_instance[4].x = 384
        villager_instance[4].y = 633
        villager_instance[5].x = 486
        villager_instance[5].y = 652
        villager_instance[6].x = 521
        villager_instance[6].y = 629
        villager_instance[7].x = 559
        villager_instance[7].y = 690
        villager_instance[8].x = 582
        villager_instance[8].y = 630
        villager_instance[9].x = 632
        villager_instance[9].y = 651
        villager_instance[10].x = 693
        villager_instance[10].y = 643
        villager_instance[11].x = 724
        villager_instance[11].y = 684
        villager_instance[12].x = 760
        villager_instance[12].y = 653
        villager_instance[13].x = 826
        villager_instance[13].y = 613
        villager_instance[14].x = 842
        villager_instance[14].y = 653

        villager_instance[15].x = 103
        villager_instance[15].y = 369
        villager_instance[16].x = 125
        villager_instance[16].y = 481
        villager_instance[17].x = 96
        villager_instance[17].y = 531
        chars = [eri] + villager_instance
        eri.x = 480.0
        eri.y = 96.0
        mood = "_spear"
        dead = False
        alive = len(villager_instance)
        killed = 0
        escapee = False
    while alive > 0 and eri.x < 1140 and not dead and not escapee:
        #renpy.show("eri_rpg", at_list=[Transform(pos=(eri.x, eri.y))])
        #renpy.show("cam_rpg", at_list=[Transform(pos=(cam.x, cam.y))])
        python:
            renpy.pause(0.016)
            WaitForInput()
            mouse_down = isMousePressed()
            if mouse_down:
                mood = "_angery"
                deaths = check_deaths(eri, villager_instance)
                for dead_vil in deaths:
                    killed += 1
                    alive -= 1
                    #hack_swap = villager_instance[-1]
                    villager_instance.remove(dead_vil)
                    chars.remove(dead_vil)
                    renpy.hide(dead_vil.img)
                    renpy.show("splat_rpg", tag = "splat_"+str(killed), at_list = [rot(dead_vil.dir_to(eri)), charpos(int(dead_vil.x), int(dead_vil.y))])
                    #dead_vil.x = hack_swap.x
                    #dead_vil.y = hack_swap.y
            elif eri in chars:
                mood = "_spear"
                for villager in villager_instance:
                    if eri.surface_dist(villager) < 2:
                        dead = True
                        chars.remove(eri)
                        renpy.hide(eri.img)
                        renpy.show("splat_rpg", tag = "splat_"+str(killed), at_list = [rot(eri.dir_to(villager)), charpos(int(eri.x), int(eri.y))])
                        renpy.pause(0.2)

            if (killed > 5):
                for char in villager_instance:
                    char.run_from(eri)
                    if char.x < 8 or char.x > 1272 or char.y > 712:
                        escapee = True
            else:
                for char in villager_instance:
                    char.follow(eri)
            update()

    $renpy.suspend_rollback(False)
    return

label stabbed_to_death:
    # The villagers killed you
    # Bad End 2
    scene black with fadein
    play music "bgm/When What Is Known As Self Is Lost #79.mp3" fadein 2 fadeout 2
    "You got killed"
    return

label on_the_run:
    # You run away from the villagers
    # A slightly less bad end?
    scene cg the_escape at bg_transform
    play music "bgm/Perseverance In The Face Of Extreme Moral And Social Weakness #42.mp3" fadein 2 fadeout 2
    "You ran away"
    return

label enemy_of_the_state:
    # You killed people but let some of them escape
    # Now you are a fugitive sought by the entire nation
    # Bad End 3
    scene cg the_monster at bg_transform
    play music "bgm/When What Is Known As Self Is Lost #79.mp3" fadein 2 fadeout 2
    "The remaining villagers run away."
    return

label a_massacre:
    # You massacred everyone
    scene cg the_massacre at bg_transform
    play music "bgm/When What Is Known As Self Is Lost #79.mp3" fadein 2 fadeout 2
    "..." # it's easy to accidentally click through the first line, so add a line that can be safely skipped.
    "You killed everyone"
    # Bad End 4
    return
