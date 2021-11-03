from RobotArm import RobotArm

robotArm = RobotArm()
robotArm.randomLevel(1,7)
robotArm.speed  = 5
# Jouw python instructies zet je vanaf hier:
for i in range (0,7):
    robotArm.grab()
    color = robotArm.scan()
    if color == '':
        break
    for i  in range (0,i+1):
        robotArm.moveRight()
    robotArm.drop()
    for i  in range (0,i+1):
        robotArm.moveLeft()



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()  