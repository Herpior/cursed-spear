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

    image erp front:
        "eri_rpg front"
        #0.1
        #repeat
    image erp front_sad:
        "eri_rpg front_sad"
    image erp back:
        "eri_rpg back"
        #0.1
        #repeat
    image erp back_sad:
        "eri_rpg back"

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

    #show screen rpg_view("heart_of_light")
    scene heart_of_light
    #show eri_rpg
    $mouse_coords = MouseCoordinateContainer()
    show screen mouse_tracker()

    python:
        chars = [eri, cam]
        eri.x = 620.0
        eri.y = 600.0
        cam.x = 640.0
        cam.y = 64.0
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
    "test"

    return

label the_final_date:
    # The date that shows the relationship between the two characters and
    # ends up in them being found out
    scene bg backyard_simple
    show camellia normal at dual_right
    c "Ah, there you are!"
    show erica normal at dual_left with moveinleft
    e "Sorry, I'm late."
    c "It's all right."
    c "I'm just happy that you are here."

    #talking, stuff, kiss cg for good bye

    j "Camellia, where have you been, your father is looking for you."
    j "Wait, what are you doing?"
    j "I'll have you two come with me right this instant!"
    c "Run!"
    return

label running_into_the_forest:
    # The run away from the village
    # RPG style segment

    scene heart_of_light
    #show eri_rpg
    #show cam_rpg
    #show joe_rpg
    python:
        chars = [eri, cam, vil]
        vil.x = 620.0
        vil.y = 600.0
        cam.x = 640.0
        cam.y = 64.0
        eri.x = 720
        eri.y = 64
        mood = "_sad"
    while eri.x < 1000 and not caught:
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
    "test"
    return

label burnt_as_witches:
    # You are caught by the one who saw you
    # Bad end 1
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

    c "Look, let's hide in those ruins."

    scene heart_of_light
    show eri_rpg
    show cam_rpg
    show joe_rpg
    python:
        chars = [eri, cam, temple_trigger]
        cam.x = 200.0
        cam.y = 360.0
        eri.x = 328
        eri.y = 360
        temple_trigger.x = 640.0
        temple_trigger.y = 64.0
    while eri.surface_dist(temple_trigger) > 4:
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
    "test"
    return

label in_the_ruins:
    # You think you are safe
    # The cursed object is found and activated
    return

label the_confrontation:
    # The villagers have found you and are approaching the temple
    # RPG style segment
    python:
        chars = [eri, cam] + villagers
    return

label stabbed_to_death:
    # The villagers killed you
    # Bad End 2
    return

label on_the_run:
    # You run away from the villagers
    # A slightly less bad end?
    return

label enemy_of_the_state:
    # You killed people but let some of them escape
    # Now you are a fugitive sought by the entire nation
    # Bad End 3
    return

label a_massacre:
    # You massacred everyone
    # Bad End 4
    return
