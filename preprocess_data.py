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

if __name__ == '__main__':
    # Create a sample DataFrame
    df = create_sample_data()

    # Perform a cleaning and transformation step
    cleaned_df = clean_and_transform_data(df)

    # Save the transformed data to a new CSV file
    output_path = 'cleaned_data.csv'
    cleaned_df.to_csv(output_path, index=False)

    print(f"Cleaned data successfully saved to {output_path}")