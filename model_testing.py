import numpy as np
from grabscreen import grab_screen
import cv2
import time
from directkeys import PressKey,ReleaseKey, W, A, S, D
from alexnet import alexnet
from getkeys import key_check

WIDTH = 160
HEIGHT = 120
LR = 1e-3
EPOCHS = 10
MODEL_NAME = 'pygta5-car-fast-{}-{}-{}-epochs-300K-data.model'.format(LR, 'alexnetv2',EPOCHS)

t_time = 0.09
def acc():
	PressKey(DIK_W)

def left():
	PressKey(DIK_J)
	
def right():
	PressKey(DIK_L)

def rev():
	PressKey(DIK_S)
	
def nit():
	PressKey(DIK_K)
	
def tech1():
	PressKey(DIK_A)
	
def tech2():
	PressKey(DIK_D)
print("Loading the Model")	
model=alexnet(WIDTH,HEIGHT,LR)
model.load(MODEL_NAME)
print(MODEL_NAME+"  loaded succesfully")
def main():
		paused=False 
		while True:
			if paused==False:
				screen= np.array(grab_screen(region=(0,40,1027,800)))
				screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
				screen = cv2.resize(screen,(80,60))
				prediction=model.predict([screen.reshape(WIDTH,HEIGHT,1)])[0]
				moves=list(np.around(prediction))
				print(moves)
				if moves==[1,0,0,0,0,0,0]:
					acc()
				elif moves==[0,1,0,0,0,0,0]:
					rev()
				elif moves==[0,0,1,0,0,0,0]:
					left()
				elif moves==[0,0,0,1,0,0,0]:
					right()
				elif moves==[0,0,0,0,1,0,0]:
					nit()
				elif moves==[0,0,0,0,0,1,0]:
					tech1()
				elif moves==[0,0,0,0,0,0,1]:
					tech2()
			keys=key_check()
			if 'P' in keys:
				if paused:
					paused=False
					time.sleep(0.5)
				else:
					paused=True
					ReleaseKey(DIK_W)
					ReleaseKey(DIK_A)
					ReleaseKey(DIK_D)
					ReleaseKey(DIK_J)
					ReleaseKey(DIK_K)
					ReleaseKey(DIK_L)
					ReleaseKey(DIK_S)
					time.sleep(0.5)
					
					
main()
