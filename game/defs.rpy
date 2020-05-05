init -5 python:



    cam = RPGCharacter(speed = 5, radius = 64, img = "cam_rpg")
    eri = RPGCharacter(speed = 4, radius = 64, img = "eri_rpg")

    vil = RPGCharacter()
    villagers = [RPGCharacter() for i in range(20)]
    trees = []
