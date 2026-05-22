def analyze_port_lead_time(vessel_logs):
    """Calculates lead time inflation due to Apapa/Tin Can port congestion."""
    # vessel_logs: list of {'vessel_id': str, 'arrival': datetime, 'berth': datetime}
    lead_times = [(log['berth'] - log['arrival']).total_seconds() / 3600 for log in vessel_logs]
    avg_wait_hours = sum(lead_times) / len(lead_times) if lead_times else 0
    congestion_index = avg_wait_hours / 24.0 # normalized to days
    return round(avg_wait_hours, 2), round(congestion_index, 2)