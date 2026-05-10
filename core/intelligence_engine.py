import pandas as pd
import numpy as np

class IntelligenceEngine:
    """The centerpiece of the Operations Intelligence framework."""
    
    def __init__(self, data):
        if isinstance(data, list):
            self.df = pd.DataFrame(data)
        else:
            self.df = data

    def generate_revenue_report(self):
        """Calculates total revenue, growth, and per-product performance."""
        summary = self.df.groupby('product')['amount'].sum().sort_values(ascending=False)
        total = summary.sum()
        return {
            'total_revenue': total,
            'by_product': summary.to_dict()
        }

    def detect_anomalies(self):
        """Uses IQR and Z-score to flag operational anomalies."""
        data = self.df['amount']
        mean, std = data.mean(), data.std()
        z_scores = (data - mean) / std
        
        q1, q3 = data.quantile(0.25), data.quantile(0.75)
        iqr = q3 - q1
        
        flags = (np.abs(z_scores) > 3) | (data < q1 - 1.5*iqr) | (data > q3 + 1.5*iqr)
        return self.df[flags]

    def forecast_next_period(self, alpha=0.3):
        """Simple exponential smoothing for demand forecasting."""
        # Aggregate by date first
        daily = self.df.groupby('date')['amount'].sum().values
        forecast = daily[0]
        for val in daily:
            forecast = alpha * val + (1 - alpha) * forecast
        return forecast

    def segment_products(self):
        """ABC Analysis: A (Top 80%), B (Next 15%), C (Bottom 5%)."""
        summary = self.df.groupby('product')['amount'].sum().sort_values(ascending=False)
        cumulative = summary.cumsum() / summary.sum()
        
        def abc(val):
            if val <= 0.8: return 'A'
            if val <= 0.95: return 'B'
            return 'C'
            
        return cumulative.apply(abc).to_dict()

    def generate_full_report(self):
        """Executes all intelligence methods and prints a summary."""
        print("--- OPERATIONS INTELLIGENCE REPORT ---")
        rev = self.generate_revenue_report()
        print(f"Total Revenue: {rev['total_revenue']}")
        
        abc = self.segment_products()
        print(f"Product Segmentation (ABC): {abc}")
        
        anomalies = self.detect_anomalies()
        print(f"Anomalies Detected: {len(anomalies)} records flagged.")
        
        forecast = self.forecast_next_period()
        print(f"Projected Revenue (Next Period): {forecast:.2f}")
