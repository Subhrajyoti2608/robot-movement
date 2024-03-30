
from controller import Robot, Keyboard, Motion


robot = Robot()

timestep = 32

keyboard = Keyboard()

keyboard.enable(timestep)

forward = Motion("../../motions/Forwards50.motion")
backward = Motion("../../motions/Backwards.motion")
sideStepLeft = Motion("../../motions/SideStepLeft.motion")
sideStepRight = Motion("../../motions/SideStepRight.motion")
handeWave = Motion("../../motions/HandWave.motion")
shoot = Motion("../../motions/Shoot.motion")
standUp = Motion("../../motions/StandUpFromFront.motion")
turnLeft40 = Motion("../../motions/TurnLeft40.motion")
turnLeft60 = Motion("../../motions/TurnLeft60.motion")
turnLeft180 = Motion("../../motions/TurnLeft180.motion")
turnRight40 = Motion("../../motions/TurnRight40.motion")
turnRight60 = Motion("../../motions/TurnRight60.motion")

def startMotion(motion):
    motion.play()

def printMessages():
    print("Press up arrow key to move forward")
    print("Press down arrow key to move backward")
    print("Press left arrow key to move left")
    print("Press right arrow key to move right")
    print("Press a to wave the hand")
    print("Press b to shoot")
    print("Press c to sleep")

key = -1

printMessages()

while robot.step(timestep) != -1:
    key = keyboard.getKey()

    if key == Keyboard.LEFT:
        startMotion(sideStepLeft)
    elif key == Keyboard.RIGHT:
        startMotion(sideStepRight)
    elif key == Keyboard.UP:
        startMotion(forward)
    elif key == Keyboard.DOWN:
        startMotion(backward)
    elif key == 65:
        startMotion(handeWave)
    elif key == 66:
        startMotion(shoot)
    elif key == 67:
        startMotion(standUp)
    elif key == 68:
        startMotion(turnLeft40)
    elif key == 69:
        startMotion(turnLeft60)
    elif key == 70:
        startMotion(turnLeft180)
    
    
    
