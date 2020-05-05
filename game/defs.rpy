init -5 python:



    cam = RPGCharacter(speed = 5, radius = 64, img = "cam_rpg")
    eri = RPGCharacter(speed = 4, radius = 64, img = "eri_rpg")

    temple_trigger = RPGCharacter(speed = 0.0001, radius = 128)

    vil = RPGCharacter(speed = 2, radius = 32, img = "joe_rpg")
    villagers = [RPGCharacter() for i in range(20)]
    trees = []
