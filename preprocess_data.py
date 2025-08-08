import pandas as pd
import numpy as np

def create_sample_data(num_samples=100):
    """Creates a sample pandas DataFrame."""
    data = {
        'id': range(num_samples),
        'feature_1': np.random.rand(num_samples),
        'feature_2': np.random.rand(num_samples) * 10,
        'category': np.random.choice(['A', 'B', 'C'], num_samples),
        'label': np.random.randint(0, 2, num_samples)
    }
    df = pd.DataFrame(data)
    return df

def clean_and_transform_data(df):
    """
    Performs a simple data cleaning and transformation step.
    - Removes rows where 'category' is 'A'.
    - Creates a new 'transformed_feature' column.
    """
    # Drop rows with a specific category
    df = df[df['category'] != 'A'].copy()

    # Create a new feature by combining existing features
    df['transformed_feature'] = df['feature_1'] * df['feature_2']

    return df
def check_data_quality(df):
    """
    Performs a basic data quality check.
    - Checks for null values and prints a summary.
    """
    print("--- Running Data Quality Check ---")
    null_counts = df.isnull().sum()
    if null_counts.sum() > 0:
        print("Warning: Missing values found in the following columns:")
        print(null_counts[null_counts > 0])
    else:
        print("No missing values found. Data quality is good.")
    print("--------------------------------")
    return df

def profile_data(df):
    """
    Generates and prints a basic statistical profile of the data.
    """
    print("\n--- Running Data Profile ---")
    print(df.describe())
    print("----------------------------")

    # Also, check the data types of each column
    print("\n--- Data Types ---")
    print(df.info())
    print("----------------------------")


if __name__ == '__main__':
    # Create a sample DataFrame
    df = create_sample_data()

    # Perform a cleaning and transformation step
    cleaned_df = clean_and_transform_data(df)

    # Perform a data quality check on the cleaned data
    check_data_quality(cleaned_df)
    # data information
    profile_data(cleaned_df)
    # Save the transformed data to a new CSV file
    output_path = 'cleaned_data.csv'
    cleaned_df.to_csv(output_path, index=False)
    
    print(f"Cleaned data successfully saved to {output_path}")
    