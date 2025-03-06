import pandas as pd

def clean_data(file_path):
    """Cleans a CSV file by handling missing values and duplicates."""
    try:
        # Load the dataset
        df = pd.read_csv(file_path)
        print("Original Data:")
        print(df.head())
        
        # Remove duplicates
        df.drop_duplicates(inplace=True)
        
        # Fill missing values with the column mean (for numeric columns)
        for col in df.select_dtypes(include=['number']).columns:
            df[col].fillna(df[col].mean(), inplace=True)
        
        # Fill missing values with the most common value (for categorical columns)
        for col in df.select_dtypes(include=['object']).columns:
            df[col].fillna(df[col].mode()[0], inplace=True)
        
        print("Cleaned Data:")
        print(df.head())
        
        # Save the cleaned data
        cleaned_file_path = "cleaned_" + file_path
        df.to_csv(cleaned_file_path, index=False)
        print(f"Cleaned data saved as {cleaned_file_path}")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    file_path = input("Enter the CSV file path: ")
    clean_data(file_path)
