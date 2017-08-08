import PIL,os
from PIL import Image
import numpy as np
from scipy import linalg as LA


class PoolImages():
	def __init__(self,directory):
		self.full_file_paths = self.get_filepaths(directory)
		print("number of example:",len(self.full_file_paths))
		self.images=[]
		self.SetImagesFromFolder()
		self.imsize = len(self.images[0])
		self.Nimages = len(self.images)
		self.Avimages = []
		self.CalcAverage()
		self.diffimages = [0 for i in range(self.Nimages)]
		self.CalcDiffImagesAv()
		self.uvecs = [[0.0 for j in range(self.images)] for i in range(self.Nimages)]
		self.CalcEgienvectors()

	def get_filepaths(self,directory):
		file_paths = []
		for root,directories,files in os.walk(directory):
			for filename in files:
				filepath = os.path.join(root,filename)
				file_paths.append(filepath)
		return file_paths

	def SetImagesFromFolder(self):
		for f in self.full_file_paths:
			im = Image.open(f).convert('L')
			pix = im.load()
			w = im.size[0]
			h = im.size[1]
			for i in range(w):
				for j in range(h):
					imagetmp.append(pix[i,j])
			print(imagetmp)
			self.images.append(imagetmp)

	def CalcAverage(self):
		for i in range(self.imsize):
			tmpvalue = sum(row[i] for row in self.images)
			self.Avimages.append(tmpvalue/self.Nimages)

	def CalcDiffImagesAv(self):
		for i  in range(self.Nimages):
			tmpdiff = []
			for j in range(self.imsize):
				tmpdiff.append(-self.Avimages[i]+self.images[i][j])
			self.diffimages[i] = tmpdiff

	def CalcEigenvectors():
		L = [[0 for i in range(self.Nimages)] for j in range(self.Nimages)]
		for i in range(self.Nimages):
			for j in range(self.Nimages):
				L[i][j] = np.dot(self.diffimages[i],self.diffimages[j])
		evals,evecs=LA.eig(L)
		for i in range(self.Nimages):
			for j in range(self.Nimages):
				self.uvecs[i] = list(map(lambda x,y:x+evecs[i][j]*y,self.uvecs[i],self.diffimages[j]))


class CheckImage():
	def __init__(self,FILENAME,directory):
		self.imagetest = []
		self.GetImages(FILENAME)
		self.poolims = PoolImages(directory)
		self.utest = [0 for i in range(self.poolims.Nimages)]
		self.uvecs = self.poolims.uvecs
		self.Avim = self.poolims.Avimages
		self.CalcProjectionIm()


	def GetImage(self,filename):
		imtest = Image.open(filename).convert("L")
		pixtest = imtest.load()
		w = imtest.size[0]
		h = imtest.size[1]
		for i in range(w):
			for j in range(h):
				self.imagetest.append(pixtest[i,j])

	def CalcProjectionIm(self):
		for i in range(self.poolims.Nimages):
			




folder = "./photos/training"
if __name__ == "__main__":
	pool = PoolImages(folder)

