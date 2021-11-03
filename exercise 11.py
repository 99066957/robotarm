from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')
robotArm.speed = 5
# Jouw python instructies zet je vanaf hier:
for i in range(8):
    robotArm.moveRight()
for x in range(9):
    robotArm.grab()
    scan = robotArm.scan()
    if scan == "red":
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
        robotArm.moveLeft()
    else:
        robotArm.grab()
        robotArm.drop()
        robotArm.moveLeft()






# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()