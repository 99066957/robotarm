from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')
robotArm.speed = 4
# Jouw python instructies zet je vanaf hier:
for x in range(8):
    robotArm.moveRight()
for x in range(1,10):
    robotArm.grab()
    scan = robotArm.scan()
    if scan == "red":
        for o in range(x):
            robotArm.moveRight()
        robotArm.drop()
        for o in range(x):
            robotArm.moveLeft()
    else:
        robotArm.drop()
    robotArm.moveLeft()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()

        




























































# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
