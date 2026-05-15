def calculate_fuel_surcharge(base_rate, current_diesel_price, fuel_threshold=500, fuel_factor=0.05):
    """Calculates fuel surcharge for logistics routes in Nigeria based on diesel volatility."""
    if current_diesel_price <= fuel_threshold: return 0
    excess = current_diesel_price - fuel_threshold
    return base_rate * (excess / fuel_threshold) * fuel_factor