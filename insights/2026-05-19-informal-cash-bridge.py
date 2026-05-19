def calculate_cash_to_digital_bridge(cash_volume, bridge_fee_pct):
    """Calculates the net digital liquidity for informal traders after bridging fees."""
    # Fees usually represent the cost of converting paper cash to digital wallet balances
    fee = cash_volume * (bridge_fee_pct / 100)
    net_liquidity = cash_volume - fee
    return round(net_liquidity, 2)