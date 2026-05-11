import pandas as pd
import datetime

def structure_informal_market_survey(survey_data):
    """
    Structures raw informal market survey data into a statistical summary.
    survey_data: list of dicts with 'vendor_id', 'product', 'price', 'demand_signal' (1-5)
    """
    df = pd.DataFrame(survey_data)
    df['collected_at'] = datetime.datetime.now().strftime("%Y-%m-%d")
    
    summary = df.groupby('product').agg({
        'price': ['mean', 'min', 'max', 'std'],
        'demand_signal': 'mean',
        'vendor_id': 'count'
    }).reset_index()
    
    summary.columns = ['product', 'avg_price', 'min_price', 'max_price', 'price_volatility', 'avg_demand', 'vendor_count']
    return df, summary

if __name__ == "__main__":
    # Sample data from an Ife market survey
    raw_data = [
        {"vendor_id": "V01", "product": "Pure Water Sachet", "price": 50, "demand_signal": 5},
        {"vendor_id": "V02", "product": "Pure Water Sachet", "price": 60, "demand_signal": 4},
        {"vendor_id": "V03", "product": "Table Water 75cl", "price": 150, "demand_signal": 3},
        {"vendor_id": "V04", "product": "Table Water 75cl", "price": 120, "demand_signal": 4},
        {"vendor_id": "V05", "product": "Yam (Large)", "price": 3500, "demand_signal": 2},
    ]
    
    clean_df, stats = structure_informal_market_survey(raw_data)
    print("--- Nigeria Informal Market Statistical Summary ---")
    print(stats)
