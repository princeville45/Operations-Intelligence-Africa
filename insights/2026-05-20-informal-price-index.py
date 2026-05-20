def index_informal_market_prices(market_data):
    """Calculates a weighted price index for commodities across regional markets (e.g., Mile 12, Bodija)."""
    # market_data: list of {'market': str, 'commodity': str, 'price': float, 'weight': float}
    total_weighted_price = sum(item['price'] * item['weight'] for item in market_data)
    total_weight = sum(item['weight'] for item in market_data)
    if total_weight == 0: return 0
    return round(total_weighted_price / total_weight, 2)