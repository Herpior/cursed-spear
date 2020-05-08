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
    show erica happy at dual_left with moveinleft
    e "Sorry, I'm late."
    c "It's all right."
    c "I'm just happy that you are here."
    # some gpt2 generated pieces
    # "Is everything okay?" "Everything is just fine, so long as I don't find you here alone," Camellia says with a smile. "I'm not alone. I have you."
    # "Well, I'm glad to be here with you again." Erica replies. They hug, then Erica asks, "Do you want to go back to your bedroom?" Camellia replies with a smile.
    # "I had almost given up on recovery. It was only your inspirational words that pulled me out of my depression and into the back rooms of the guild. Without you, I know I would have become an alchemist again. I am absolutely indebted to you."
    c "I missed you so."
    e "Is everything okay?"
    e "You look a bit distraught."
    c "It's nothing."
    show erica questioning
    e "Really?"
    show camellia worried
    c "I really can't hide anything from you, can I."
    show camellia sad
    show erica normal
    c "You remember when my father told me he'd get me married to some rich merchant if I wouldn't stop declining the marriage offers?"
    c "Well, it seems he's found someone interested."
    show camellia cri
    c "The papers are already in order and the merchant is set to pick me up later this week."
    show erica mad
    e "What?"
    e "I'll go punch some sense into those idiots right away!"
    show camellia worried
    c "Wait, calm down."
    show camellia sad
    c "You know that won't solve anything."
    e "But that's so unfair."
    show erica normal
    e "Isn't there anything I can do?"
    show camellia normal at dual_right
    c "You can be with me."
    e "But are you going to just let them take you away?"
    c "I will let them see their mistake once the time comes."
    c "But enough of that, come closer."

    show erica lenny at kiss_left behind camellia
    show camellia nya_left at right
    with ease
    c "You're the only one I'd let take me away."
    show erica blush
    e "Oh Camellia."
    e "You're unfair too."
    show camellia flirt
    c "It runs in the family."
    show erica nyahaha
    e "Stop it, you'll make my heart burst."
    show camellia nya_left
    c "Just like that?"
    c "Even though we've gone further before?"
    show erica blush
    e "Every day is a new day."
    c "So you'll make me do this every day?"

    scene cg the_kiss at bg_transform
    e "m-mmh."
    e "Only if you stay with me."
    c "I won't let anything separate us."
    c "If only this moment could last for ever."
    e "To stay like this forever." # the monkey paw twists a finger
    e "I couldn't ask for more."



    j "Camellia, I looked for you everywhere, your father is looking for you."
    scene bg backyard at bg_transform
    show erica normal at kiss_to_left behind camellia
    show camellia shock at kiss_to_right

    show joe normal at left with moveinleft:
        zoom 0.6667
    play music "bgm/Persecuted, Belittled And Betrayed By The People #50.mp3" fadein 2 fadeout 2

    j "Wait, what are you doing?"
    show camellia shock_left
    j "I'll have you two come with me right this instant!"
    $renpy.suspend_rollback(True)
    c "Run!"
    hide camellia
    hide erica
    with moveoutright
    return

label running_into_the_forest:
    # The run away from the village
    # RPG style segment

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

    return

label burnt_as_witches:
    # You are caught by the one who saw you
    # Bad end 1
    scene black with dissolve
    play music "bgm/When What Is Known As Self Is Lost #79.mp3" fadein 2 fadeout 2
    $renpy.suspend_rollback(False)
    "Joe captures you both."
    "You try to fight back but he is like wall of muscle."
    "You are thrown into a small room and separated from Camellia."

    "After staying in the room for what must have been days, you're finally brought out." #, you are finally brought back to the surface."
    #"Sun's last rays blind you when they reach your eyes."
    #"Once your eyes adjust to the light, the sight is breathtaking."
    #"Or would be, if not for the pile of wood brought to the center of the square."
    "You're led to the center of the town."
    "A pile of wood is waiting for you at the town square."
    "Being pulled closer towards the pile, you notice the figure of another woman already tied to one of the stakes in the center of the pile."
    e "Camellia!!"
    c "Erica? Ahh, I'm so sorry."
    c "Maybe I could had saved you if I'd done something differently."
    #c "I was hoping they would save at least you." #"I tried to make them at least let you go"
    "You are led to a pillar next to Camellia."
    e "At least we're together again."
    e "But how are you here? didn't the merchant..."
    "You're tied tight to the pillar."
    c "He got second thoughts once I almost ripped his face off."
    "The ropes dig into your already sore body."
    c "After hearing about that, my father got furious, telling he'd 'let me be with you' if that was what I so wanted."
    "More people from the village is gathering to watch."
    e "Meaning this?"
    e "What a twisted father you have."
    c "The worst part is how happy I felt that moment, even though I guessed what he was meaning."
    c "You must hate me now that you know everything."
    #"Well, it's not every day that there's an event going on in here."
    "The kindlings are set ablaze, the smell of smoke fills the air."
    e "I could never hate you."
    e "I love you from the bottom of my heart, now and forever."
    c "Oh Erica, I love you too."
    "As the fire spreads, the smog is making it harder to breathe."
    c "*cough* Let us meet again *coughcough* in our next lives."
    "The smell of burning flesh is awful but the pain creeping up your legs is worse."
    e "AAaAaaaAaargh."
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

    #$renpy.suspend_rollback(False)
    c "Look, let's hide in those ruins."
    #$renpy.suspend_rollback(True)

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
    return

label in_the_ruins:
    # You think you are safe
    # The cursed object is found and activated
    scene bg temple at bg_transform
    show camellia sad at dual_right
    show erica normal at dual_left
    $renpy.suspend_rollback(False)
    play music "bgm/Psychological Emotional Survival Of An Indignant Soul #69.mp3" fadein 2 fadeout 2
    c "They won't dare to come here."
    c "I've heard them call these ruins cursed before."
    show camellia sarcastic
    c "But considering all the things they believe, I would be surprised if there's anything dangerous in here."
    show camellia sad
    e "This place looks pretty grim."
    show erica questioning
    e "And what are we going to do now?"
    e "Can't we just go back and call it all a misunderstanding?"
    show camellia sarcastic
    c "Oh wouldn't that be just grand."
    c "'Yeah, we uhh.. were just talking about the weather, really closely, while hiding in the stables.'"
    show camellia sad
    c "And it's too late anyways."
    show erica normal
    e "I guess that's true."
    show camellia sadder
    c "To be honest, I don't know what should we do."
    show camellia sad_think
    c "If we go back, they'll just lock me up and we'd never see again."
    show camellia sadder_think
    c "If we stay here, we'll starve."
    show camellia sad
    c "Maybe we could escape the village if we stole horses."
    show camellia sad_think
    c "But what would we do then?"
    c "Live as bandits?"
    show erica mad
    e "Slow down a bit, will you."
    show erica happy
    e "Well get through this."
    show erica normal
    e "Somehow."
    show camellia relief
    c "Thanks. I needed to hear that."
    c "Uhh..."
    c "I need to rest a little."



    "You decide to explore the ruins to take off your mind from the situation."
    #hide erica with moveoutright
    scene bg temple at bg_transform
    with dissolve
    show erica normal at center with moveinleft
    "After a while, you come across a small room that's somehow preserved better than the rest of the ruins."
    "In there you find a stone stand."
    scene cg the_pendant at bg_transform
    "On the stand sits a fancy necklace glimmering in the faint moonlight."
    "How could there be a necklace this exquisite in ruins like these."
    "It would surely look great on Camellia."
    "You take the pendant from the pedestal."

    scene bg temple at bg_transform
    "very sad things happen"
    scene cg the_curse at bg_transform
    play music "bgm/The Abyss Known As Oneself #39.mp3" fadein 2 fadeout 2
    c "It hurts so much, help me Erica!"
    return

label the_confrontation:
    # The villagers have found you and are approaching the temple
    # RPG style segment
    $renpy.suspend_rollback(True)
    "hold down mouse button to slash with the spear."
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
    scene black with dissolve
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
