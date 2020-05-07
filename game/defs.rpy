init -5 python:



    cam = RPGCharacter(speed = 7, radius = 32, img = "cam_mini")
    eri = RPGCharacter(speed = 6, radius = 32, img = "eri_mini")

    temple_trigger = RPGCharacter(speed = 0.0001, radius = 128)

    vil = RPGCharacter(speed = 2, radius = 32, img = "joe_mini")
    villagers = [RPGCharacter(speed = 2, radius = 32, img = "joe_copy_"+str(i)) for i in range(18)]
    trees = []
