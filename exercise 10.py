from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')
robotArm.speed = 5

# Jouw python instructies zet je vanaf hier:
for x in range(5):
    print(x)
    robotArm.grab()
    print(x)
    for o in range(9-(2*x)):
        robotArm.moveRight()
    robotArm.drop()
    for o in range(9-(2*x)-1):
        robotArm.moveLeft()
        




# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
