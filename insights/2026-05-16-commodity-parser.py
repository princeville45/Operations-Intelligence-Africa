import re

def parse_commodity_prices(raw_text):
    """Parses unstructured SMS/Chat market price updates for commodities in Nigeria."""
    # Matches patterns like 'Maize: 45,000 NGN/Bag'
    pattern = r'(\w+):\s*([\d,]+)\s*NGN'
    matches = re.findall(pattern, raw_text)
    return {item: float(price.replace(',', '')) for item, price in matches}