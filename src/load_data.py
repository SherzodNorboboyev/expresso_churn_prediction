import pandas as pd
from typing import Optional
from pathlib import Path

def load_data(path: str) -> Optional[pd.DataFrame]:
    '''
    Load a dataset from a CSV file into a pandas DataFrame.

    Args:
        path (str): Path to the CSV file.

    Returns:
        Optional[pd.DataFrame]: The loaded DataFrame if successful, 
        otherwise None.
    '''
    df = None
    csv_path = Path(path)
    if (csv_path is None):
        print("File doesn't exist")
        return None
    try:
        df = pd.read_csv(csv_path)
        print(f"Loaded dataset with shape {df.shape} from {csv_path}")
        return df
    except pd.errors.EmptyDataError:
        print(f"Error: The file {csv_path} is empty.")
    except pd.errors.ParserError as e:
        print(f"Error: Could not parse {csv_path}: {e}")
    except Exception as e:
        print(f"Unexpected error while loading {csv_path}: {e}")
    
    return None
