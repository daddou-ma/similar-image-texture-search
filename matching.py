#!/usr/bin/env python
#imports
import sys
import os
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from image import Image
from csvhandler import CSVFile
from distance import Distance
from tkinter import filedialog

database = CSVFile.load_from_csv('images/images.csv')

if len(sys.argv) >=2:
    filename = sys.argv[1]
else:
    filename = filedialog.askopenfilename() # sys.argv[0]

request_image = Image(filename)
request_vector = request_image.get_features_vector()

rows = []
for index, row in database.iterrows():
    rows.append(Distance.distance(request_vector, list(row[1:5])))

database['distance'] = rows
database = database.sort_values(by=['distance'], ascending=True)
print(database['distance'])

similars = database.head(4)[1:4].apply(lambda row: {'img': Image(row['0']), 'distance': round(row['distance'], 2)}, axis=1)

similar1, similar2, similar3 = map(lambda item: Image.get_preview_image(item['img'], item['distance']), similars)

top = np.hstack((Image.get_preview_image(request_image, 0), similar1))
bottom = np.hstack((similar2, similar3))
result = np.vstack((top, bottom))


cv2.imshow('similars', result)

#numpy_vertical = np.vstack((image, grey_3_channel))

cv2.waitKey()