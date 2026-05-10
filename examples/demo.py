from core.intelligence_engine import IntelligenceEngine
import pandas as pd
import numpy as np

# 1. Generate Synthetic Depot Data (30 days, 5 products)
np.random.seed(42)
products = ['C-Way 75cl', 'C-Way 1.5L', 'Dispenser Jar', 'C-Way Cup', 'Ice Block']
data = []
for i in range(30):
    for p in products:
        data.append({
            'date': f'2026-05-{i+1:02d}',
            'product': p,
            'amount': np.random.randint(500, 5000)
        })

# 2. Initialize Engine
engine = IntelligenceEngine(data)

# 3. Run Intelligence Pipeline
engine.generate_full_report()
