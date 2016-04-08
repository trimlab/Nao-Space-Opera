#!/usr/bin/python

'''	Spring 2016 Child-Robot Theater 
	Space Opera - Second lines for Nao '''

import argparse
from naoqi import ALProxy

def main(robotIP, PORT=9559):
	
	animatedSpeechProxy = ALProxy("ALAnimatedSpeech", robotIP, PORT)

	configuration = {"bodyLanguageMode":"contextual"}

	lines = "^start(animations/Stand/Gestures/YouKnowWhat_1) \
		He wants to rule over all humans and robots."	
	
	animatedSpeechProxy.say(lines)

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument("--ip", type=str, default="127.0.0.1", 
		help="Robot ip address")
	parser.add_argument("--port", type=int, default=9559,
		help="Robot port number")

	args = parser.parse_args()
	
	main(args.ip, args.port)