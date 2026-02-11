import pandas as pd
from sklearn.utils import resample
import os

def balance_job_data():
    # Load the raw job market data
    if not os.path.exists('data/raw_market_data.csv'):
        print("Error: raw_market_data.csv not found. Run data_generation.py first.")
        return

    df = pd.read_csv('data/raw_market_data.csv')
    
    print("--- Original Region Distribution ---")
    print(df['Region'].value_counts())
    
    # We want to balance the regions so smaller hubs like Jaffna/Galle 
    # have enough data for the forecasting model
    
    # Identify the majority class (Colombo) and minority classes
    df_colombo = df[df.Region == 'Colombo']
    df_others = df[df.Region != 'Colombo']
    
    # Upsample the smaller regions to match a higher count (e.g., 400 per region)
    # This addresses the 'target_size' error from your previous run
    balanced_list = [df_colombo]
    
    for region in ['Kandy', 'Galle', 'Jaffna']:
        df_region = df[df.Region == region]
        df_region_upsampled = resample(df_region, 
                                       replace=True,     # sample with replacement
                                       n_samples=400,    # Fixed parameter name
                                       random_state=42) 
        balanced_list.append(df_region_upsampled)
    
    # Combine back into one dataframe
    df_balanced = pd.concat(balanced_list)
    
    # Save the cleaned dataset for Power BI
    os.makedirs('data', exist_ok=True)
    df_balanced.to_csv('data/balanced_market_data.csv', index=False)
    
    print("\n--- Balanced Region Distribution ---")
    print(df_balanced['Region'].value_counts())
    print("\nBalanced data saved to data/balanced_market_data.csv")

if __name__ == "__main__":
    balance_job_data()