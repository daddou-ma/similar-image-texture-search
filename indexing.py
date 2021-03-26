#!/usr/bin/env python

import sys
import os
from image import Image
from csvhandler import CSVFile
from progress import map_with_progress

folderpath = 'images'

# Get Images Histograms as list
print('[Step 1: Loading Images in \'{folderpath}\*.jpg folder]'.format(folderpath=folderpath))
images = list(map_with_progress(lambda path: Image(path), Image.get_all_images_in_folder(folderpath)))

print('[Step 2: Calculating Feature Vector for each Image]')
data = list(map_with_progress(lambda image: image.get_full_vector(), images))

# Save DataFrame to a csv file
print('[Step 3: Saving to CSV File \'{name}/{name}.csv\']'.format(name=folderpath))
CSVFile.save_to_csv(data, '{name}/{name}.csv'.format(name=folderpath))
