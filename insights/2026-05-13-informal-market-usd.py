def index_informal_prices(prices_ngn, usd_rate):
    # Normalizing informal market pricing to USD for inflation tracking
    return [p / usd_rate for p in prices_ngn]