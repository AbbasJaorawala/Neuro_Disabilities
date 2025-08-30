import pandas as pd
import numpy as np

def clean_data(df):
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Fill missing values
    df = df.fillna(method='ffill')
    
    return df

def transform_data(df):
    # Example transformation: Convert categorical variables to dummy variables
    df = pd.get_dummies(df, drop_first=True)
    
    return df

def prepare_data(file_path):
    # Load data
    df = pd.read_csv(file_path)
    
    # Clean and transform data
    df = clean_data(df)
    df = transform_data(df)
    
    return df

def save_processed_data(df, output_path):
    # Save the processed DataFrame to a CSV file
    df.to_csv(output_path, index=False)