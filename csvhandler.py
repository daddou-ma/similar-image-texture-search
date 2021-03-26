import os
import numpy as np
import pandas as pd

class CSVFile:
    # Get All jpg files in images folder
    @staticmethod
    def save_to_csv(data, filename):
        df = pd.DataFrame(data, columns = list(range(0, 5)))

        # Save DataFrame to a csv file
        df.to_csv(filename)


    # Open an Image
    @staticmethod
    def load_from_csv(filename):
        return pd.read_csv(filename, index_col=0)