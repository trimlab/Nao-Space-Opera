#!/usr/bin/python

'''	Spring 2016 Child-Robot Theater 
	Space Opera - Laser gun shooting motion for Nao '''

# Modified Choregraphe bezier export in Python.
import argparse
from naoqi import ALProxy

def main(robotIP, PORT=9559):
	names = list()
	times = list()
	keys = list()

	names.append("HeadPitch")
	times.append([1, 1.48, 1.96])
	keys.append([[-0.14117, [3, -0.333333, 0], [3, 0.16, 0]], [-0.14117, [3, -0.16, 0], [3, 0.16, 0]], [-0.14117, [3, -0.16, 0], [3, 0, 0]]])

	names.append("HeadYaw")
	times.append([1, 1.48, 1.96])
	keys.append([[-0.0107799, [3, -0.333333, 0], [3, 0.16, 0]], [-0.0107799, [3, -0.16, 0], [3, 0.16, 0]], [-0.0107799, [3, -0.16, 0], [3, 0, 0]]])

	names.append("LAnklePitch")
	times.append([1, 1.48, 1.96])
	keys.append([[0.0889301, [3, -0.333333, 0], [3, 0.16, 0]], [0.0889301, [3, -0.16, 0], [3, 0.16, 0]], [0.0889301, [3, -0.16, 0], [3, 0, 0]]])

	names.append("LAnkleRoll")
	times.append([1, 1.48, 1.96])
	keys.append([[-0.122678, [3, -0.333333, 0], [3, 0.16, 0]], [-0.122678, [3, -0.16, 0], [3, 0.16, 0]], [-0.122678, [3, -0.16, 0], [3, 0, 0]]])

	names.append("LElbowRoll")
	times.append([1, 1.48, 1.96])
	keys.append([[-0.427944, [3, -0.333333, 0], [3, 0.16, 0]], [-0.427944, [3, -0.16, 0], [3, 0.16, 0]], [-0.427944, [3, -0.16, 0], [3, 0, 0]]])

	names.append("LElbowYaw")
	times.append([1, 1.48, 1.96])
	keys.append([[-1.18736, [3, -0.333333, 0], [3, 0.16, 0]], [-1.18736, [3, -0.16, 0], [3, 0.16, 0]], [-1.18736, [3, -0.16, 0], [3, 0, 0]]])

	names.append("LHand")
	times.append([1, 1.48, 1.96])
	keys.append([[0.2896, [3, -0.333333, 0], [3, 0.16, 0]], [0.2896, [3, -0.16, 0], [3, 0.16, 0]], [0.2896, [3, -0.16, 0], [3, 0, 0]]])

	names.append("LHipPitch")
	times.append([1, 1.48, 1.96])
	keys.append([[0.121228, [3, -0.333333, 0], [3, 0.16, 0]], [0.121228, [3, -0.16, 0], [3, 0.16, 0]], [0.131966, [3, -0.16, 0], [3, 0, 0]]])

	names.append("LHipRoll")
	times.append([1, 1.48, 1.96])
	keys.append([[0.0966839, [3, -0.333333, 0], [3, 0.16, 0]], [0.0966839, [3, -0.16, 0], [3, 0.16, 0]], [0.0966839, [3, -0.16, 0], [3, 0, 0]]])

	names.append("LHipYawPitch")
	times.append([1, 1.48, 1.96])
	keys.append([[-0.1733, [3, -0.333333, 0], [3, 0.16, 0]], [-0.1733, [3, -0.16, 0], [3, 0.16, 0]], [-0.1733, [3, -0.16, 0], [3, 0, 0]]])

	names.append("LKneePitch")
	times.append([1, 1.48, 1.96])
	keys.append([[-0.0874801, [3, -0.333333, 0], [3, 0.16, 0]], [-0.0874801, [3, -0.16, 0], [3, 0.16, 0]], [-0.0874801, [3, -0.16, 0], [3, 0, 0]]])

	names.append("LShoulderPitch")
	times.append([1, 1.48, 1.96])
	keys.append([[1.44805, [3, -0.333333, 0], [3, 0.16, 0]], [1.44805, [3, -0.16, 0], [3, 0.16, 0]], [1.47413, [3, -0.16, 0], [3, 0, 0]]])

	names.append("LShoulderRoll")
	times.append([1, 1.48, 1.96])
	keys.append([[0.199378, [3, -0.333333, 0], [3, 0.16, 0]], [0.199378, [3, -0.16, 0], [3, 0.16, 0]], [0.06592, [3, -0.16, 0], [3, 0, 0]]])

	names.append("LWristYaw")
	times.append([1, 1.48, 1.96])
	keys.append([[0.122678, [3, -0.333333, 0], [3, 0.16, 0]], [0.122678, [3, -0.16, 0], [3, 0.16, 0]], [0.122678, [3, -0.16, 0], [3, 0, 0]]])

	names.append("RAnklePitch")
	times.append([1, 1.48, 1.96])
	keys.append([[0.0859461, [3, -0.333333, 0], [3, 0.16, 0]], [0.0859461, [3, -0.16, 0], [3, 0.16, 0]], [0.0859461, [3, -0.16, 0], [3, 0, 0]]])

	names.append("RAnkleRoll")
	times.append([1, 1.48, 1.96])
	keys.append([[0.121228, [3, -0.333333, 0], [3, 0.16, 0]], [0.121228, [3, -0.16, 0], [3, 0.16, 0]], [0.121228, [3, -0.16, 0], [3, 0, 0]]])

	names.append("RElbowRoll")
	times.append([1, 1.48, 1.96])
	keys.append([[0.414222, [3, -0.333333, 0], [3, 0.16, 0]], [0.596768, [3, -0.16, 0], [3, 0.16, 0]], [0.382009, [3, -0.16, 0], [3, 0, 0]]])

	names.append("RElbowYaw")
	times.append([1, 1.48, 1.96])
	keys.append([[1.19188, [3, -0.333333, 0], [3, 0.16, 0]], [1.18881, [3, -0.16, 0], [3, 0.16, 0]], [1.2471, [3, -0.16, 0], [3, 0, 0]]])

	names.append("RHand")
	times.append([1, 1.48, 1.96])
	keys.append([[0.3992, [3, -0.333333, 0], [3, 0.16, 0]], [0.3992, [3, -0.16, 0], [3, 0.16, 0]], [0.3992, [3, -0.16, 0], [3, 0, 0]]])

	names.append("RHipPitch")
	times.append([1, 1.48, 1.96])
	keys.append([[0.131882, [3, -0.333333, 0], [3, 0.16, 0]], [0.131882, [3, -0.16, 0], [3, 0.16, 0]], [0.131882, [3, -0.16, 0], [3, 0, 0]]])

	names.append("RHipRoll")
	times.append([1, 1.48, 1.96])
	keys.append([[-0.0966001, [3, -0.333333, 0], [3, 0.16, 0]], [-0.0966001, [3, -0.16, 0], [3, 0.16, 0]], [-0.0966001, [3, -0.16, 0], [3, 0, 0]]])

	names.append("RHipYawPitch")
	times.append([1, 1.48, 1.96])
	keys.append([[-0.1733, [3, -0.333333, 0], [3, 0.16, 0]], [-0.1733, [3, -0.16, 0], [3, 0.16, 0]], [-0.1733, [3, -0.16, 0], [3, 0, 0]]])

	names.append("RKneePitch")
	times.append([1, 1.48, 1.96])
	keys.append([[-0.0858622, [3, -0.333333, 0], [3, 0.16, 0]], [-0.0858622, [3, -0.16, 0], [3, 0.16, 0]], [-0.0858622, [3, -0.16, 0], [3, 0, 0]]])

	names.append("RShoulderPitch")
	times.append([1, 1.48, 1.96])
	keys.append([[0.949588, [3, -0.333333, 0], [3, 0.16, 0]], [0.271559, [3, -0.16, 0.111981], [3, 0.16, -0.111981]], [0.159578, [3, -0.16, 0], [3, 0, 0]]])

	names.append("RShoulderRoll")
	times.append([1, 1.48, 1.96])
	keys.append([[-0.131966, [3, -0.333333, 0], [3, 0.16, 0]], [-0.0951499, [3, -0.16, -0.036816], [3, 0.16, 0.036816]], [0.144154, [3, -0.16, 0], [3, 0, 0]]])

	names.append("RWristYaw")
	times.append([1, 1.48, 1.96])
	keys.append([[0.091998, [3, -0.333333, 0], [3, 0.16, 0]], [0.021434, [3, -0.16, 0], [3, 0.16, 0]], [0.493905, [3, -0.16, 0], [3, 0, 0]]])

	try:
	  motion = ALProxy("ALMotion", robotIP, PORT)
	  motion.angleInterpolationBezier(names, times, keys)
	except BaseException, err:
	  print err

if __name__ == '__main__':
	
	parser = argparse.ArgumentParser()
	parser.add_argument("--ip", type=str, default="127.0.0.1", 
		help="Robot ip address")
	parser.add_argument("--port", type=int, default=9559,
		help="Robot port number")

	args = parser.parse_args()
	
	main(args.ip, args.port)
