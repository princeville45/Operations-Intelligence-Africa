"""
Operations Intelligence Africa: Logistics ROI Optimization
Vibe: Territorial Mastery | Logic: Margin per Kilometer

In Nigeria, logistics is a game of friction. This script optimizes
route selection based on fuel costs, tolls, and security premiums.
"""

def calculate_route_roi(routes):
    """
    Selects the route with the highest Net Margin per Kilometer.
    """
    print("Optimizing African Logistics Corridor...")
    optimized_report = []
    
    for route in routes:
        revenue = route['cargo_value'] * route['margin_rate']
        operating_cost = (route['distance'] * route['fuel_price']) + route['tolls'] + route['security_cost']
        net_profit = revenue - operating_cost
        roi_per_km = net_profit / route['distance']
        
        optimized_report.append({
            "route_id": route['id'],
            "net_profit": round(net_profit, 2),
            "roi_per_km": round(roi_per_km, 2)
        })
    
    # Sort by ROI per KM
    return sorted(optimized_report, key=lambda x: x['roi_per_km'], reverse=True)

if __name__ == "__main__":
    nigeria_routes = [
        {"id": "Lagos-Ibadan", "distance": 130, "fuel_price": 650, "tolls": 2000, "security_cost": 0, "cargo_value": 500000, "margin_rate": 0.2},
        {"id": "Lagos-Benin", "distance": 320, "fuel_price": 650, "tolls": 5000, "security_cost": 15000, "cargo_value": 1200000, "margin_rate": 0.25}
    ]
    
    rankings = calculate_route_roi(nigeria_routes)
    for r in rankings:
        print(f"Route: {r['route_id']} | ROI/KM: {r['roi_per_km']} | Net: {r['net_profit']}")
