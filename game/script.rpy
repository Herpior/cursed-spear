# The game should not be very long so the entirety of the script is written
# in this file.

# In this block we declare all the characters who have dialogue in the game

define c = Character("Camellia") # the cursed
define e = Character("Erica") # the survivor

default e_dir = "front"
image erp = "erp [e_dir]"

image erp front:
    "eri_rpg.png"
    0.1
    repeat

image erp back:
    "eri_rpg.png"
    0.1
    repeat

image erp left:
    "eri_rpg.png"
    0.1
    repeat

image erp right:
    xzoom -1
    "eri_rpg.png"
    0.1
    repeat

python:
    # initialize the variables necessary for the story
    # at least until the parts where they are edited are finished
    caught = false
    dead = false
    killed = 0
    alive = 100

# The game starts here.

label start:
    # the main flow of the story

    call meeting_in_secret
    call the_final_date
    call running_into_the_forest
    if caught:
        jump burned_as_witches
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
    show screen rpg_view("heart_of_light")

    python:
        chars = [eri, cam]
        eri.x = 640
        eri.y = 600
        cam.x = 640
        cam.y = 64
        while eri.surface_dist(cam) > 4:
            #renpy.show("eri_rpg", at_list=[Transform(pos=(eri.x, eri.y))])
            #renpy.show("cam_rpg", at_list=[Transform(pos=(cam.x, cam.y))])
            renpy.pause(0.016)
            WaitForInput()
            print(eri.dist(cam))
    "test"
    hide rpg_view
    return

label the_final_date:
    # The date that shows the relationship between the two characters and
    # ends up in them being found out
    c "Ah, there you are!"
    return

label running_into_the_forest:
    # The run away from the village
    # RPG style segment
    python:
        chars = [eri, cam, vil]
    return

label burned_as_witches:
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
