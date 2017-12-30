import numpy as np
import cv2
import time
from keyr import key_check
from grab import grab_screen
from tin import PressKey,ReleaseKey,DIK_W,DIK_S,DIK_A,DIK_D
import os
    

def keys_op(keys):
	#[W,S,A,D,J,K,L]
    output = [0,0,0,0,0,0,0]
    if 'W' in keys:
        output[0]=1
    elif 'S' in keys:
        output[1]=1
    elif 'J' in keys:
        output[2]=1
    elif 'L' in keys:
        output[3]=1
    elif 'K' in keys:
        output[4]=1
    elif 'A' in keys:
        output[5]=1
    elif 'D' in keys:
        output[6]=1
    return output
	
file_name = './newnfsfinal3_data.npy'
if os.path.isfile(file_name):
    f=np.load(file_name)
    newtr_data=list(f)
else:
	print("file not found creating new data file")
	screen= np.array(grab_screen(region=(0,40,1027,800)))
	screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
	screen = cv2.resize(screen,(80,60))
	keys = key_check()
	output = keys_op(keys)
	data=([screen,output])
	np.save(file_name,data)
	f=np.load(file_name)
	newtr_data=list(f)
    
while(True):
	screen= np.array(grab_screen(region=(0,40,1027,800)))
	screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
	screen = cv2.resize(screen,(80,60))
	keys = key_check()
	output = keys_op(keys)
	newtr_data.append([screen,output])
	if(len(newtr_data)%500 == 0):
		print(len(newtr_data))
		np.save(file_name,newtr_data)
	cv2.imshow('window',screen)
	if cv2.waitKey(25) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
		break