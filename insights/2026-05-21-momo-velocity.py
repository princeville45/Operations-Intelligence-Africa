def calculate_momo_velocity(transactions_df):
    """Calculates the velocity of Mobile Money (MoMo) transactions for regional agents."""
    # Velocity = Total Transaction Volume / Unique Agents active
    total_volume = transactions_df['amount'].sum()
    active_agents = transactions_df['agent_id'].nunique()
    if active_agents == 0: return 0
    return round(total_volume / active_agents, 2)