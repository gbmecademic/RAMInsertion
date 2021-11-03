from forceFunctions import FindSurface, MoveThread, ClickDetection
from mecademicpy.robot import Robot
from NetFT import Sensor
from queue import Queue
from time import sleep

sleep(5)

sensor = Sensor('192.168.0.101')
q = Queue()
robot = Robot()

#fs = FindSurface(1, 'FindSurface', 1, sensor, q, 15)
cd = ClickDetection(1, 'Click', 2, sensor, q, 80, 5)
move = MoveThread(2, 'Move', 2, robot, q)
move.connect()
move.move_settings(speed=3)

print("Moving to point 1")
robot.MoveJoints(111.038,35.027,32.493,-1.526,23.191,21.365)

print('Starting Thread')
#fs.start()
cd.start()
move.start()

while q.empty():
    sleep(1)

print(q.get())

cd.join()
move.join()

with q.mutex:
    q.queue.clear()

print("Moving to point 2")
robot.MoveJoints(79.054,32.841,36.759,-2.497,20.697,-9.687)

cd = ClickDetection(1, 'Click', 2, sensor, q, 80, 8)
move = MoveThread(2, 'Move', 2, robot, q)
move.move_settings(speed=3)

print('Starting Thread')
#fs.start()
cd.start()
move.start()

while q.empty():
    sleep(1)

print(q.get())



sleep(3)
robot.Disconnect()
