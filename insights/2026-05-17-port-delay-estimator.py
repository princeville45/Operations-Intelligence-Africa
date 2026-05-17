def estimate_lagos_port_delay(vessel_count, weather_status='Clear'):
    """Estimates delay at Apapa/Tin Can ports based on vessel queue and conditions."""
    base_delay_days = vessel_count / 5
    if weather_status == 'Rainy':
        base_delay_days *= 1.5
    return round(base_delay_days, 1)