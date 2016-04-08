#!/usr/bin/python

'''	Spring 2016 Child-Robot Theater 
	Space Opera - First lines for Nao '''

import argparse
from naoqi import ALProxy

def main(robotIP, PORT=9559):
	
	animatedSpeechProxy = ALProxy("ALAnimatedSpeech", robotIP, PORT)

	configuration = {"bodyLanguageMode":"contextual"}

	lines = "I am Nao ^wait(animations/Stand/Gestures/Hey_1), \
		leader of the Freedom Fighters. \
		These are my friends. Joining our fight for freedom is a dinosaur, \
		stranded outside his time ^wait(animations/Stand/Gestures/You_4)  - Pleo!"

	animatedSpeechProxy.say(lines)

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument("--ip", type=str, default="127.0.0.1", 
		help="Robot ip address")
	parser.add_argument("--port", type=int, default=9559,
		help="Robot port number")

	args = parser.parse_args()
	
	main(args.ip, args.port)