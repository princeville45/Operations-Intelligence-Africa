def calculate_route_cost_efficiency(fuel_cost, distance, load_utilization):
    """Calculates efficiency metric for logistics routes (Lagos-Ibadan-Kano)."""
    # Cost per unit-kilometer adjusted for load utilization
    cost_per_km = fuel_cost / 15 # assuming 15km/L average for heavy trucks
    efficiency_index = (distance * cost_per_km) / (load_utilization + 0.01)
    return round(efficiency_index, 2)