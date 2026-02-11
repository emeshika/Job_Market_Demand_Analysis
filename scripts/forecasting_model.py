import pandas as pd
import numpy as np
from statsmodels.tsa.holtwinters import ExponentialSmoothing

def run_job_demand_forecast():
    # Load the balanced data
    df = pd.read_csv('data/balanced_market_data.csv', parse_dates=['Post_Date'])
    
    # Aggregate daily applicant trends to see demand velocity
    df_daily = df.groupby(df['Post_Date'].dt.date)['Applicant_Count'].sum()
    
    # Build the Time Series Model
    model = ExponentialSmoothing(df_daily, trend='add', seasonal=None)
    model_fit = model.fit()
    
    # Generate Forecast for next 30 days
    forecast = model_fit.forecast(30)
    
    # Scenario Analysis: Best Case (+20%) / Worst Case (-20%)
    print("--- Market Demand Scenario Analysis ---")
    print(f"Most Likely (Predicted): {forecast.sum():.0f} applicants")
    print(f"Best Case (High Growth): {forecast.sum() * 1.2:.0f} applicants")
    print(f"Worst Case (Economic Downturn): {forecast.sum() * 0.8:.0f} applicants")
    
    return forecast

if __name__ == "__main__":
    run_job_demand_forecast()