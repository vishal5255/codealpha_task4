#codealpha #codealpha_internship
=============================
 Data Cleaning with Python
===========================

## Introduction
This project is a simple Data Cleaning Script that processes CSV files to remove errors and inconsistencies. It helps clean datasets by handling missing values and removing duplicate records.

I have created a raw file (only for testing purpose) or you can test this on your own data.
==============
How It Works
================
1. **Loads a CSV file** using `pandas`.
2. **Removes duplicate rows** to ensure unique data.
3. **Handles missing values**:
   - For **numerical columns**, missing values are replaced with the column mean.
   - For **categorical columns**, missing values are filled with the most common value.
4. **Saves  the cleaned data** to a new CSV file (by creating a new .csv file automatically).

=====================
## Functionality
=======================
- Automatically **removes duplicates**.
- Fills  missing values using **smart imputation**.
- Works with both **numerical and categorical data**.
  -Saves the cleaned dataset as a new file with a `cleaned_` prefix.

=================
## How to Use
==============
1. **Install pandas** if not already installed:
   pip install pandas
   
2. **Run the script**:
   python data_cleaning.py
   
4. **Enter the CSV file name** (e.g., `sample_data.csv`).

5. The cleaned file will be saved as **`cleaned_sample_data.csv`**.

## Thanks
Special thanks to the #CodeAlpha team for their support in this project! 🚀
#codealpha #code_alpha
#internship
