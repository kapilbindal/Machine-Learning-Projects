import numpy as np
import cv2
import os
from PIL import Image
import matplotlib.image as mpimg

def distance(x1,x2):
	return np.sqrt(sum((x1-x2)**2))

def knn(train,test,k=5):
	dist = []
	m = train.shape[0]
	for i in range(m):
		ix = train[i, :-1]
		iy = train[i, -1]
		d = distance(test,ix)
		dist.append([d,iy])

	dk = sorted(dist, key=lambda x: x[0])[:k]
	labels = np.array(dk)[:, -1]
	output = np.unique(labels, return_counts=True)
	index = np.argmax(output[1])
	return output[0][index]

face_data = []
dataset_path = './images/'
labels = []

class_id = 0
names = {}
for fx in os.listdir(dataset_path):
	##print(fx)
	for f in os.listdir(dataset_path+fx):
		if(f.endswith('.jpg')):
			names[class_id] = fx
			##print("Loaded "+f)
			img = Image.open(dataset_path+fx+'/'+f)
			arr = np.array(img)
			##print(arr.shape)
			#data_item = np.load(dataset_path+fx)
			face_data.append(arr)
			target = class_id*np.ones((arr.shape[0],))
			class_id += 1
			labels.append(target)
face_data = np.array(face_data)
face_dataset = np.concatenate(face_data,axis=0)
##print(face_dataset.shape)
face_dataset = face_dataset[:,0]
face_labels = np.concatenate(labels,axis=0).reshape((-1,1))
print(face_dataset.shape)
print(face_labels.shape)

trainset = np.concatenate((face_dataset,face_labels),axis=1)
print(trainset.shape)

