# The game should not be very long so the entirety of the script is written
# in this file.

# In this block we declare all the characters who have dialogue in the game

define c = Character("Camellia", color = "#FF82C0") # the cursed
define e = Character("Erica", color = "#B5FFBE") # the survivor
define j = Character("Joe", color = "#3CDCCE") # the prosecutor
define vf = Character("Voice from outside", color = "#3CDCCE") # the prosecutor
define s1 = Character("Voice in Erica's head", color = "F30095")
define s = Character("Camellia", color = "F30095")

init -4:
    python:
        if persistent.choice_style is None:
            persistent.choice_style = "rpg"

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

transform sit:
    yanchor 1.0
    ypos 1.2

transform hori_shake_right:
    zoom 0.6667
    block:
        linear 0.16 xpos 0.69
        linear 0.16 xpos 0.75
        repeat


transform shake_right:
    zoom 0.6667
    parallel:
        yanchor 1.0
        block:
            choice:
                linear 0.1 ypos 1.0
            choice:
                linear 0.03 ypos 1.04
            choice:
                linear 0.06 ypos 1.06
            choice:
                linear 0.16 ypos 1.02
        block:
            choice:
                linear 0.2 ypos 1.2
            choice:
                linear 0.1 ypos 1.13
            choice:
                linear 0.06 ypos 1.15
            choice:
                linear 0.03 ypos 1.10
    parallel:
        block:
            choice:
                linear 0.09 xpos 0.67
            choice:
                linear 0.08 xpos 0.69
            choice:
                linear 0.07 xpos 0.7
            choice:
                linear 0.06 xpos 0.71
        block:
            choice:
                linear 0.09 xpos 0.78
            choice:
                linear 0.08 xpos 0.76
            choice:
                linear 0.07 xpos 0.74
            choice:
                linear 0.06 xpos 0.73
    repeat

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

    if persistent.choice_style == "rpg":
        call meeting_in_secret
    call the_final_date
    if persistent.choice_style == "rpg":
        call running_into_the_forest
    else:
        menu override_run:
            "Joe is chasing you."
            "Run to the forest":
                #block of code to run
                pass
            "Get caught":
                $caught = True

    if caught:
        jump burnt_as_witches

    if persistent.choice_style == "rpg":
        call running_into_the_ruins
    else:
        scene bg forest at bg_transform
        show camellia normal at dual_left
        c "Look, let's hide in those ruins."
    call in_the_ruins
    if persistent.choice_style == "rpg":
        call the_confrontation
    else:
        menu override_confront:
            "A large group of people is closing in on you."
            "Run Away":
                #block of code to run
                pass
            "Do nothing":
                $dead = True
            "Slash with Camellia":
                $killed = 6
                $alive = 12
                "Camellia pierces through the people like butter."
                menu override_massacre:
                    "The people are starting to flee from you."
                    "Keep on killing":
                        $alive = 0
                        $killed = 18
                    "Stop":
                        #block of code to run
                        pass

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


    return

label the_final_date:
    # The date that shows the relationship between the two characters and
    # ends up in them being found out
    scene bg backyard at bg_transform
    show camellia normal at dual_right
    c "Ah, there you are!"
    $renpy.suspend_rollback(False)
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
    "Joe captures you both."
    $renpy.suspend_rollback(False)
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
    "Dead end."
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
    play music "bgm/Psychological Emotional Survival Of An Indignant Soul #69.mp3" fadein 2 fadeout 2
    c "They won't dare to come here."
    $renpy.suspend_rollback(False)
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
    show camellia sadder
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
    show camellia not_smiling
    c "I need to rest a little."
    show camellia at sit
    with ease

    "You decide to explore the ruins to take off your mind from the situation."
    #hide erica with moveoutright
    scene bg temple at bg_transform
    with dissolve
    show erica normal at center, bg_transform with moveinleft
    "After a while, you come across a small room that's preserved better than the rest of the ruins."
    "In there, you find a stone stand."
    scene cg the_pendant at bg_transform
    "On the stand sits a fancy necklace glimmering in the faint moonlight."
    "How could there be a necklace this exquisite in ruins like these."
    "Maybe it would cheer Camellia up."
    "You take the pendant from the pedestal."

    scene bg temple at bg_transform
    show camellia not_smiling at dual_right, sit
    show erica happy at dual_left with moveinright
    #"very sad things happen"
    e "Hey Camellia, look what I found."
    show erica at center with ease
    show camellia left
    "You show the necklace to Camellia."
    show camellia worried
    c "And that was just laying around here?"
    #c "That better not be cursed."
    show erica normal
    e "Yeah."
    show camellia left
    c "Wait, that might just be our ticket out of this."
    show camellia flirt
    c "We could sell that and get enough to start over in a city."
    show erica lenny
    e "Guess how I'd like it more right now?"
    show erica at kiss_left
    show camellia at dual_right
        #zoom 0.6667
    with ease
    e "You wearing it."
    show erica:
        xpos 0.6
    with ease
    #"You place the pendant on her neck."
    #show erica blush
    show camellia amulet_happy
    c "Oh Erica, that's so sweet."
    show erica happy
    e "I'm glad you cheered up."

    show camellia amulet_unwell:
        ypos 1.025
    with ease
    c "Hang on, I feel a bit unwell."
    show erica questioning
    e "From the necklace?"
    show erica normal
    e "I'll take it off right away."
    show erica at hori_shake_right
    "You try to remove the pendant but it's almost like glued to her now."
    show erica stumped
    "The more you try to pull it the more it seems to hurt."
    play music "bgm/The Abyss Known As Oneself #39.mp3" fadein 2 fadeout 2
    show camellia amulet_hurt at shake_right
    show erica afu at center
    with ease
    "Camellia is shaking in pain."
    scene cg the_curse at bg_transform
    c "It hurts so much, help me Erica!"
    "She begs with eyes bulging and her nose stretching."
    "You don't know what could you do but you try to hold her close."
    "Her flesh is shifting rapidly under your fingers."
    c "AAaAAAAAaaaaAA!"
    "..."
    "After several agonizing minutes, you're left holding only a spear."

    scene bg temple at bg_transform
    show erica_spear cry_soft at dual_right
    "The spear looks gruesome with it's flesh-like handle and eye and all."
    s1 "Oww, that hurt."
    show erica_spear surprised
    e "Camellia!?"
    e "You're alive?"
    s "I got through that somehow, I suppose."
    show erica_spear normal
    s "I don't think I can move my body though."
    s "How bad does it look?"
    show erica_spear avoiding_gaze
    e "It's... pretty bad."
    e "You're... you just..."
    show erica_spear cry_hard
    "You break into tears mid sentence"
    e "You just turned into a spear right in front of me!"
    show erica_spear cry_medium
    e "What have I done."
    e "I should had never touched that necklace."
    show erica_spear cry_hard
    e "If anyone should had suffered, it should had been me."
    e "You never did anything wrong, so why?"
    e "Why did it have to be you."
    s "Calm down, Erica."
    show erica_spear cry_soft
    s "Nobody is blaming you for anything."
    s "At least we're still together."
    s "Isn't that right?"
    show erica_spear cry_medium
    e "But.. But I made you go through all that pain."
    e "And you can't even move by yourself anymore."
    show erica_spear cry_hard
    e "Camellia!"
    s "Erica listen to me!"
    show erica_spear cry_medium
    s "It wasn't your fault."
    s "Nobody could had predicted that this would happen."
    show erica_spear cry_soft
    e "*sniff*"
    s "You can't keep on blaming yourself forever."
    s "Were in this together."
    # There should be more text in here that would show the conflict between blaming self,
    # your loved one being changed to something unrecognizable and gross-ish,
    # your loved one now being entirely dependent on you,
    # Camellia also being in an unstable state right now rather than trying to calm Erica like now happens in the text
    # And accepting it all.
    # Or maybe half of that should be after the next action scene
    # but I don't know how to write any of that even half properly

    # Will anyone see what I'm trying to convey here?
    # If you're reading this long comment here, did it make my intentions clearer or maybe even more unclear?
    # Writing is still too hard for me.
    # I don't want to hurt the characters too much because that would make me hurt too much in the process.
    # I've already hurt them so much but to make the characters more realistic or something, I'd need to make them
    # hurt each other even more, to maybe make it possible for them to eventually make up and make the
    # Endings more meaningful.

    vf "It came from over there!"
    vf "Everyone, come here! They're at the ruins!"

    show erica_spear surprised
    e "They found us already?"
    e "What do we do?"
    show erica_spear sad
    s "There are no right answers anymore."
    s "Trust your guts."
    s "Just don't let them catch us."


    return

label the_confrontation:
    # The villagers have found you and are approaching the temple
    # RPG style segment
    $renpy.suspend_rollback(True)
    "You can hold down mouse button to slash with Camellia."
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
    while alive > 0 and (eri.x < 1240 and eri.y < 690 and eri.x > 40) and not dead and not escapee:
        #renpy.show("eri_rpg", at_list=[Transform(pos=(eri.x, eri.y))])
        #renpy.show("cam_rpg", at_list=[Transform(pos=(cam.x, cam.y))])
        python:
            renpy.pause(0.016)
            eri.speed = 6 + (killed / 5.0)
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


            for char in villager_instance:
                if killed > 4 and killed < 12:
                    char.speed = 1
                else:
                    char.speed = 2
                if (killed > 8):
                        char.run_from(eri)
                        if char.x < 8 or char.x > 1272 or char.y > 712:
                            escapee = True
                else:
                        char.follow(eri)
            update()
    "..."
    return

label stabbed_to_death:
    # The villagers killed you
    # Bad End 2
    scene black with dissolve
    play music "bgm/When What Is Known As Self Is Lost #79.mp3" fadein 2 fadeout 2
    $renpy.suspend_rollback(False)
    "Seeing camellias new form must have spooked them as they don't even try to catch you."
    "Instead they just ruthlessly kill you when they get near enough."
    "You got killed."
    "They later disposed of Camellia by burning her."
    "Or at least tried to, I don't know how to destroy a demonic spear."
    "It must still have hurt a lot."
    "Not that you'd know that, being dead and all."
    "Dead end."
    return

label on_the_run:
    # You run away from the villagers
    # A slightly less bad end?
    scene cg the_escape at bg_transform
    play music "bgm/Perseverance In The Face Of Extreme Moral And Social Weakness #42.mp3" fadein 2 fadeout 2
    $renpy.suspend_rollback(False)
    "You run away with tears rolling off your cheeks."
    "You manage to evade the villagers and get out of the town."
    "After running for hours, your lungs burning and muscles aching, you finally collapse from exhaustion and fall asleep."
    #"you're sure you are no longer being followed,
    "Once you wake up, you wrap Camellia in cloth and start walking."

    "..."
    "You travel through the country doing odd jobs to survive."
    "Never staying long in one place to keep your secret safe."
    # This cg looks totally out of place in here but I can't think of anything better either and at least it uses the cg
    # would be a shame not to use the cg if I've drawn it already.
    scene cg the_kiss_end at bg_transform
    "Only when no one else is looking, can you be with Camellia"
    "You're still risking everything every second you spend with her."
    "But you'd rather die than be separated from her."

    "Peaceful end."
    return

label enemy_of_the_state:
    # You killed people but let some of them escape
    # Now you are a fugitive sought by the entire nation
    # Bad End 3
    scene cg the_monster at bg_transform
    play music "bgm/When What Is Known As Self Is Lost #79.mp3" fadein 2 fadeout 2
    $renpy.suspend_rollback(False)
    "The remaining villagers run away in fear."
    j "M-monster!!"
    "You look at your hands stained in blood."
    "What have you done?"
    "Not only did you hurt your beloved."
    "You also killed your neighbours, people you knew."
    "Camellia is covered in blood."
    "How did it come to this?"
    #e "Oh dear."
    #e "..."
    #s ""
    #scene cg the_kiss_end_blood at bg_transform
    #e "I love you, Camellia."
    # There is a cg for kissing bloody spear Camellia but I just can't find a way to make it work with the story
    # it's a shame to not use it since it already exists but what can I do..
    "..."

    "You end up being chased by the law enforcement."
    "They are generally easy to avoid as long as you stay away from larger cities and settlements."
    "You live your life poaching and foraging in the woods, with an occasional robbery here and there."
    "The small cabin is cozy and with no visitors, you have a lot of time to talk with Camellia."
    "There's always shortage of food and Camellia needs a sip of blood every now and then to stay sane."
    "Luckily it seems that animal blood works as well."
    "And like that, the days pass along."

    "Outlaw end."
    return

label a_massacre:
    # You massacred everyone
    scene cg the_massacre at bg_transform
    play music "bgm/When What Is Known As Self Is Lost #79.mp3" fadein 2 fadeout 2
    # it's easy to accidentally click through the first line, so add a line that can be safely skipped.
    $renpy.suspend_rollback(False)
    "One by one you strike through the people chasing you."
    "Even as they begin to flee, you won't let a single one of them escape."
    #"You kill everyone, not letting a single one of them escape."
    "The rush of the chase makes you forget you even knew the people."
    #"Every hit invigorates you and makes you stronger"
    "..."

    "Several months later."
    "You're walking through a battlefield."
    "The ground is littered with bodies."
    "They are not killed by you, well, not all of them, at the very least."
    "You joined a group of mercenaries not long after the events at your home village."
    "Growing stronger with every battle, you've come to be held as a human weapon of sorts."
    "A reaper of the battlefields."
    "The matters of the court could not interest you less, as long as you get to draw blood."
    "You've mostly forgotten what life was before the curse."
    "Camellia's words ring in your head."
    "They are the only thing you need."
    "That's the only thing you can remember clearly."

    "Violent end."
    # Bad End 4
    return
