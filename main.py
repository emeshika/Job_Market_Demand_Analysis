from scripts.data_generation import generate_job_market_data
from scripts.data_balancing import balance_job_data
from scripts.forecasting_model import run_job_demand_forecast

def main():
    print("--- Starting Market Demand Project Workflow ---")
    generate_job_market_data()
    balance_job_data()
    forecast = run_job_demand_forecast()
    print("Workflow Complete. Ready for Power BI import.")

if __name__ == "__main__":
    main()