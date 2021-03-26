import os
import numpy as np
import pandas as pd

class Distance:
    # Get All jpg files in images folder
    @staticmethod
    def distance(vector1, vector2):
        nv1 = np.array(vector1)
        nv2 = np.array(vector2)
        result = np.sum(np.absolute(((nv1 - nv2) / nv1))) / 4
        return result