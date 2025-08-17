import pandas as pd
import logging
from typing import List

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CustomBinningStrategy:
    
    def __init__(self):
        
        self.bins = [0, 12, 24, 48, 72]
        self.labels = ['New', 'Intermediate', 'Established', 'Loyal']
        logging.info("Initialized tenure binning strategy")

    def bin_feature(self, df: pd.DataFrame, tenure_column: str = 'tenure') -> pd.DataFrame:
        
        try:
            # Create tenure groups using the predefined bins and labels
            df['tenure_group'] = pd.cut(
                df[tenure_column],
                bins=self.bins,
                labels=self.labels,
                right=True,
                include_lowest=True
            )
            
            logging.info(f"Successfully binned tenure into {len(self.labels)} categories")
            logging.info(f"Tenure group distribution:\n{df['tenure_group'].value_counts()}")
            
            # Drop original tenure column as done in the notebook
            df.drop(columns=[tenure_column], inplace=True)
            logging.info(f"Dropped original {tenure_column} column")
            
            return df
            
        except Exception as e:
            logging.error(f"Error during tenure binning: {str(e)}")
            raise

if __name__ == "__main__":
    # Example usage
    try:
        # Sample data
        df = pd.DataFrame({
            'tenure': [1, 15, 30, 50, 70]
        })
        
        print("Original Data:")
        print(df)
        
        # Create and apply tenure binning
        binner = CustomBinningStrategy()
        df = binner.bin_feature(df)
        
        print("\nData after tenure binning:")
        print(df)
        
    except Exception as e:
        logging.error(f"Error in example: {str(e)}")