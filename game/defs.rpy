init -5 python:



    cam = RPGCharacter(speed = 5, radius = 52, img = "cam_mini")
    eri = RPGCharacter(speed = 4, radius = 52, img = "eri_mini")

    temple_trigger = RPGCharacter(speed = 0.0001, radius = 128)

    vil = RPGCharacter(speed = 2, radius = 32, img = "joe_mini")
    villagers = [RPGCharacter(speed = 2, radius = 52, img = "joe_mini") for i in range(20)]
    trees = []
