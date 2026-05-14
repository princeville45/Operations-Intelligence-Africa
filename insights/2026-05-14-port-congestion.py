def estimate_delivery_lag(congestion_index, base_lead_time):
    """Estimates delivery delay based on port congestion levels (0.0 to 1.0)."""
    # Exponential lag model based on historical Apapa port data
    multiplier = 1 + (2.5 * (congestion_index ** 2))
    return round(base_lead_time * multiplier, 2)