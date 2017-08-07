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


folder = "./photos/training"
if __name__ == "__main__":
	pool = PoolImages(folder)

