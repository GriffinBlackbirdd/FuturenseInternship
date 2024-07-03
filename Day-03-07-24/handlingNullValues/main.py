'''
I will be using the Melbourne Homes dataset from Kaggle - https://www.kaggle.com/datasets/dansbecker/melbourne-housing-snapshot,
@author: Arreyan Hamid
'''
import pandas as pd
import os


FOLDER_PATH = "E:\\futurense\\FuturenseInternship\\Day-03-07-24\\handlingNullValues"
dataPath = os.path.join(FOLDER_PATH, "melb_data.csv")
data = pd.read_csv(dataPath)

numeric_cols = data.select_dtypes(include='number').columns

# Handling null values
# 1. Removing Rows with Null Values
data_dropRow = data.dropna()
data_dropRowSpecific = data.dropna(subset=['Price', 'BuildingArea'])

# 2. Removing Columns with Null Values
data_dropCols = data.dropna(axis=1, how='any')
threshold = len(data) * 0.5
data_dropColsThreshold = data.dropna(axis=1, thresh=threshold)

# 3. Filling Null Values
data_fillZero = data.fillna(0)
data_fillMean = data.copy()
data_fillMean[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].mean())
data_fillMedian = data.copy()
data_fillMedian[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].median())

# 4. Interpolating Missing Values
dataInterpolate = data.interpolate()

# Data Cleaning
# Remove duplicate rows
dataCleaned = data.drop_duplicates()

# Removing columns that are unnecessary or have high cardinality
data_cleaned = dataCleaned.drop(['Address', 'SellerG'], axis=1)

final_data_path = os.path.join(FOLDER_PATH, "melb_dataCleaned.csv")
data_cleaned.to_csv(final_data_path, index=False)
