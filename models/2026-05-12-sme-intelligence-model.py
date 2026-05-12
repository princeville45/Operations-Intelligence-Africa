"""
Informal Market Intelligence Model
Author: Irem Victor Chinonso | Statistical Business Architect
Date: 2026-05-12
Repo: Operations-Intelligence-Africa

Models the revenue structure and operational efficiency of
informal/SME businesses in sub-Saharan Africa.
Benchmarks performance against informal sector norms
and provides actionable operational intelligence.
"""

import pandas as pd
import numpy as np


SECTOR_BENCHMARKS = {
    "Wholesale/Retail": {
        "gross_margin_pct": 18.0,
        "inventory_turnover": 8.5,
        "daily_revenue_ngn": 45000,
        "opex_ratio": 0.22
    },
    "Food & Beverage": {
        "gross_margin_pct": 28.0,
        "inventory_turnover": 12.0,
        "daily_revenue_ngn": 25000,
        "opex_ratio": 0.35
    },
    "Transport & Logistics": {
        "gross_margin_pct": 22.0,
        "inventory_turnover": None,
        "daily_revenue_ngn": 30000,
        "opex_ratio": 0.40
    }
}


def generate_business_snapshot(sector="Wholesale/Retail"):
    """Simulate a real business's monthly operational data."""
    np.random.seed(13)
    bench = SECTOR_BENCHMARKS[sector]

    return {
        "sector": sector,
        "monthly_revenue_ngn": round(bench["daily_revenue_ngn"] * 26 * np.random.uniform(0.85, 1.15), 2),
        "cogs_ngn": round(bench["daily_revenue_ngn"] * 26 * (1 - bench["gross_margin_pct"] / 100) * np.random.uniform(0.9, 1.1), 2),
        "monthly_opex_ngn": round(bench["daily_revenue_ngn"] * 26 * bench["opex_ratio"] * np.random.uniform(0.8, 1.2), 2),
        "avg_inventory_value_ngn": round(np.random.uniform(80000, 250000), 2),
        "credit_sales_pct": round(np.random.uniform(15, 45), 1),
        "cash_collected_pct": round(np.random.uniform(70, 95), 1),
        "staff_count": np.random.randint(1, 8),
        "working_days": 26
    }


def compute_operational_kpis(snapshot):
    """Derive key operational KPIs from snapshot."""
    rev = snapshot["monthly_revenue_ngn"]
    cogs = snapshot["cogs_ngn"]
    opex = snapshot["monthly_opex_ngn"]
    inv = snapshot["avg_inventory_value_ngn"]

    gross_profit = rev - cogs
    gross_margin = round(gross_profit / rev * 100, 2) if rev else 0
    net_profit = gross_profit - opex
    net_margin = round(net_profit / rev * 100, 2) if rev else 0
    inv_turnover = round(cogs / inv, 2) if inv else None
    daily_revenue = round(rev / snapshot["working_days"], 2)
    revenue_per_staff = round(rev / snapshot["staff_count"], 2)

    return {
        "gross_profit_ngn": round(gross_profit, 2),
        "gross_margin_pct": gross_margin,
        "net_profit_ngn": round(net_profit, 2),
        "net_margin_pct": net_margin,
        "inventory_turnover": inv_turnover,
        "daily_revenue_ngn": daily_revenue,
        "revenue_per_staff_ngn": revenue_per_staff,
        "cash_conversion": snapshot["cash_collected_pct"]
    }


def benchmark_analysis(kpis, sector):
    """Compare KPIs against sector benchmarks."""
    bench = SECTOR_BENCHMARKS[sector]
    report = []

    checks = [
        ("Gross Margin (%)", kpis["gross_margin_pct"], bench["gross_margin_pct"], "higher is better"),
        ("Daily Revenue (NGN)", kpis["daily_revenue_ngn"], bench["daily_revenue_ngn"], "higher is better"),
    ]
    if kpis["inventory_turnover"] and bench["inventory_turnover"]:
        checks.append(("Inventory Turnover", kpis["inventory_turnover"], bench["inventory_turnover"], "higher is better"))

    for label, actual, target, direction in checks:
        gap = round(actual - target, 2)
        status = "ABOVE BENCHMARK" if gap >= 0 else "BELOW BENCHMARK"
        report.append({"metric": label, "actual": actual, "benchmark": target, "gap": gap, "status": status})

    return pd.DataFrame(report)


def run_intelligence():
    print("=" * 60)
    print("OPERATIONS INTELLIGENCE: AFRICA SME MODEL")
    print("Operations Intelligence Africa | Irem Victor Chinonso")
    print("=" * 60)

    sector = "Wholesale/Retail"
    snapshot = generate_business_snapshot(sector)
    kpis = compute_operational_kpis(snapshot)
    bench_df = benchmark_analysis(kpis, sector)

    print(f"\nSector: {sector}")
    print(f"Monthly Revenue: ₦{snapshot['monthly_revenue_ngn']:,.0f}")
    print(f"COGS:            ₦{snapshot['cogs_ngn']:,.0f}")
    print(f"OpEx:            ₦{snapshot['monthly_opex_ngn']:,.0f}")
    print(f"Staff Count:     {snapshot['staff_count']}")

    print("\n--- OPERATIONAL KPIs ---")
    for key, val in kpis.items():
        print(f"  {key:<35} {val}")

    print("\n--- BENCHMARK ANALYSIS ---")
    print(bench_df.to_string(index=False))

    print("\n--- INTELLIGENCE SIGNALS ---")
    for _, row in bench_df.iterrows():
        if row["status"] == "BELOW BENCHMARK":
            print(f"  IMPROVE: {row['metric']} is {abs(row['gap']):.2f} units below sector average.")
        else:
            print(f"  STRONG:  {row['metric']} outperforms the sector by {row['gap']:.2f} units.")

    print("\nAnalysis complete.")


if __name__ == "__main__":
    run_intelligence()
