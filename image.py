import os
import math
import cv2
import numpy as np
from skimage.feature import greycomatrix

class Image:
    angles = (0, np.pi/4, np.pi/2, 3*np.pi/4)

    def __init__(self, imagepath):
        self.imagepath = imagepath
        self.image = Image.load_image(imagepath)
        self.grey = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.reduced = [[((pixel * 8) // 256) for pixel in line] for line in self.grey]

    def get_comatrix(self, angle):
        #return greycomatrix(self.reduced, [1], [angle], 8, symmetric=True, normed=True)
        return greycomatrix(self.reduced, [1], [angle], 8, normed=True)
    
    def get_features_vector(self):
        matrices = list(map(self.get_comatrix, Image.angles))
        energy_mean = np.array(list(map(Image.comatrix_energy, matrices))).mean()
        inertia_mean = np.array(list(map(Image.comatrix_inertia, matrices))).mean()
        entropy_mean = np.array(list(map(Image.comatrix_entropy, matrices))).mean()
        momentdi_mean = np.array(list(map(Image.comatrix_momentdi, matrices))).mean()

        return (energy_mean, inertia_mean, entropy_mean, momentdi_mean)

    def get_full_vector(self):
        return  (self.imagepath, ) + self.get_features_vector()

    @staticmethod
    def comatrix_energy(matrix):
        result = 0
        for line in matrix:
            for p in line:
                result = result + p**2
                
        return result

    @staticmethod
    def comatrix_inertia(comatrix):
        result = 0
        for i, line in enumerate(comatrix):
            for j, p in enumerate(line):
                result = result + p * (i - j)**2
                
        return result

    @staticmethod
    def comatrix_entropy(comatrix):
        result = 0
        for line in comatrix:
            for p in line:
                result = result + p * math.log2(p if p else 1)
                
        return result

    @staticmethod
    def comatrix_momentdi(comatrix):
        result = 0
        for i, line in enumerate(comatrix):
            for j, p in enumerate(line):
                result = result + (1  / (1 + (i - j)**2)) * p
                
        return result
    
    # Get All jpg files in images folder
    @staticmethod
    def get_all_images_in_folder(foldername):
        filenames = []
        for  filename in  [x for x in os.listdir(foldername) if x.endswith(".jpg")]: 
            path = './' + foldername + '/' + filename
            filenames.append(path)
        return filenames

    # Open an Image
    @staticmethod
    def load_image(imagepath):
        image = cv2.imread(imagepath)
        return image

    @staticmethod
    def get_preview_image(image, distance):
        result = cv2.resize(image.image,(480, 360))
        result = cv2.rectangle(result, (10, 320), (470, 350), (255, 255, 255), cv2.FILLED)
        result = cv2.putText(result, ('Distance : ' +str(distance)) if distance != 0 else 'Request', (20, 340), cv2.FONT_HERSHEY_COMPLEX, 0.5, (192, 54, 62), 1, cv2.LINE_AA)
        return result
