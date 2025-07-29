"""
MCP Resources for kiteMCP server.
Contains market data and trading knowledge for LLM context.
"""

mcp = None

def set_mcp_instance(mcp_instance):
    """Set the MCP instance from the main server."""
    global mcp
    mcp = mcp_instance

def get_nifty50_data() -> str:
    """Get NIFTY 50 market data and key information."""
    return """
NIFTY 50 - India's Premier Stock Index

KEY INFORMATION:
- Index Type: Market capitalization weighted
- Constituents: 50 largest companies listed on NSE
- Base Year: 1995 (Base Value: 1000)
- Trading Hours: 9:15 AM - 3:30 PM IST

IMPORTANT LEVELS:
- Support: 19,000, 18,500, 18,000
- Resistance: 20,000, 20,500, 21,000
- Key Moving Averages: 20 EMA, 50 EMA, 200 EMA

TRADING CHARACTERISTICS:
- High liquidity options available
- Expiry: Last Thursday of every month
- Lot Size: 50 shares
- Tick Size: 0.05

Use this data for NIFTY options trading strategies.
"""

def get_banknifty_data() -> str:
    """Get Bank NIFTY market data and key information."""
    return """
BANK NIFTY - Banking Sector Index

KEY INFORMATION:
- Index Type: Market capitalization weighted
- Constituents: 12 largest banking stocks
- Base Year: 2003 (Base Value: 1000)
- Trading Hours: 9:15 AM - 3:30 PM IST

IMPORTANT LEVELS:
- Support: 44,000, 43,000, 42,000
- Resistance: 46,000, 47,000, 48,000
- Key Moving Averages: 20 EMA, 50 EMA, 200 EMA

TRADING CHARACTERISTICS:
- High volatility options available
- Expiry: Last Thursday of every month
- Lot Size: 25 shares
- Tick Size: 0.05

Use this data for Bank NIFTY options trading strategies.
"""

def get_options_basics() -> str:
    """Get fundamental options trading knowledge."""
    return """
OPTIONS TRADING BASICS

CALL OPTIONS:
- Right to buy at strike price
- Bullish strategy
- Limited risk (premium paid)
- Unlimited profit potential

PUT OPTIONS:
- Right to sell at strike price
- Bearish strategy
- Limited risk (premium paid)
- Profit potential up to strike price

KEY CONCEPTS:
- Strike Price: Price at which option can be exercised
- Premium: Price paid for the option
- Expiry: Date when option expires
- In-the-money: Option has intrinsic value
- Out-of-the-money: Option has no intrinsic value
- At-the-money: Strike price equals current market price

RISK MANAGEMENT:
- Never risk more than 2% of portfolio per trade
- Use stop losses for all positions
- Diversify across different strategies
- Monitor position sizing carefully
"""

def get_greeks_knowledge() -> str:
    """Get options Greeks knowledge for advanced trading."""
    return """
OPTIONS GREEKS - Risk Management Tools

DELTA:
- Measures directional risk
- Range: 0 to 1 for calls, -1 to 0 for puts
- At-the-money options: ~0.5 delta
- Deep in-the-money: ~1.0 delta
- Deep out-of-the-money: ~0.0 delta

GAMMA:
- Measures rate of change in delta
- Highest for at-the-money options
- Decreases as option moves in/out of money
- Important for delta-neutral strategies

THETA:
- Measures time decay
- Always negative (options lose value over time)
- Accelerates as expiration approaches
- Higher for at-the-money options

VEGA:
- Measures sensitivity to volatility changes
- Highest for at-the-money options
- Decreases as option moves in/out of money
- Important for volatility strategies

RHO:
- Measures sensitivity to interest rate changes
- Usually small impact on short-term options
- More significant for long-term options
"""

def register_resources():
    """Register all resources with decorators after mcp is set."""
    if mcp is None:
        raise RuntimeError("MCP instance not set. Call set_mcp_instance() first.")
    
    # Apply decorators to all resource functions
    mcp.resource("market://nifty50")(get_nifty50_data)
    mcp.resource("market://banknifty")(get_banknifty_data)
    mcp.resource("knowledge://options_basics")(get_options_basics)
    mcp.resource("knowledge://greeks")(get_greeks_knowledge) 