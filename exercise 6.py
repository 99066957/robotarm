from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')


# Jouw python instructies zet je vanaf hier:
robotArm.speed = 5
for x in range(9):
    robotArm.moveRight()
for o in range(8):
    for x in range(2):
        robotArm.moveLeft()    
    robotArm.grab()
    for x in range(1):
        robotArm.moveRight()
        robotArm.drop()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()