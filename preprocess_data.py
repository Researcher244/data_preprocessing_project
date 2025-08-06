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

if __name__ == '__main__':
    # Create a sample DataFrame
    df = create_sample_data()

    # Save the data to a CSV file
    output_path = 'sample_data.csv'
    df.to_csv(output_path, index=False)

    print(f"Sample data successfully saved to {output_path}")