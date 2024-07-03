![Banner](https://dlmeqwbnyvguihvtcgat.supabase.co/storage/v1/object/public/eliteClub/DALL_E_2024_07_03_11.59.13___A_cyberpunk_themed_banner_image_showcasing__Handling_Null_Values_with_Python_._The_design_should_be_very_technical__classy__and_modern__featuring_futu.webp?t=2024-07-03T06%3A29%3A34.493Z)
# Melbourne Housing Data Cleaning

This project demonstrates various techniques for handling and cleaning data using the Melbourne Homes dataset from Kaggle. The dataset contains information about housing prices and attributes in Melbourne, Australia.

## Dataset

The dataset used in this project is labeled as `melb_data.csv` and is assumed to be located in the specified folder path. The dataset contains various attributes such as price, building area, address, and seller information.

## Data Cleaning Techniques

The following data cleaning techniques are applied in this project:

1. **Handling Null Values**:
   - **Removing Rows with Null Values**:
     - `data_dropRow`: Removes all rows with any null values.
     - `data_dropRowSpecific`: Removes rows with null values in specific columns (`Price` and `BuildingArea`).
   - **Removing Columns with Null Values**:
     - `data_dropCols`: Removes all columns with any null values.
     - `data_dropColsThreshold`: Removes columns with null values exceeding a specified threshold (50% in this case).
   - **Filling Null Values**:
     - `data_fillZero`: Fills all null values with zero.
     - `data_fillMean`: Fills null values in numeric columns with the mean of the respective columns.
     - `data_fillMedian`: Fills null values in numeric columns with the median of the respective columns.
   - **Interpolating Missing Values**:
     - `dataInterpolate`: Interpolates missing values.

2. **Data Cleaning**:
   - **Remove Duplicate Rows**:
     - `dataCleaned`: Removes duplicate rows from the dataset.
   - **Removing Unnecessary or High Cardinality Columns**:
     - `data_cleaned`: Removes columns `Address` and `SellerG` which are deemed unnecessary or have high cardinality.

## Prerequisites

- Python 3.x
- Pandas

## Installation

To install the required library, you can use pip:

```bash
pip install pandas
```

## Usage

1. Clone the repository or download the code.
2. Ensure the dataset `melb_data.csv` is located in the specified folder path.
3. Run the script to perform data cleaning.

```python
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
```
Made with ❤️ by [Arreyan Hamid](https://github.com/GriffinBlackbirdd)
For any inquiries or feedback, please contact [arreyanhamid@icloud.com](mailto:arreyanhamid@icloud.com).