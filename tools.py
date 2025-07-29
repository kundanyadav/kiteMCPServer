"""
MCP Tools for kiteMCP server.
Contains all trading-related functions that can be called by the agent/LLM.
"""

import datetime
from typing import Dict, Any

# Global kite instance (will be set by main server)
kite = None
mcp = None

def set_kite_instance(kite_instance):
    """Set the kite instance from the main server."""
    global kite
    kite = kite_instance

def set_mcp_instance(mcp_instance):
    """Set the MCP instance from the main server."""
    global mcp
    mcp = mcp_instance

def get_portfolio() -> dict:
    """Get my current portfolio positions."""
    if not kite:
        return {"error": "Kite Connect not authenticated. Please restart the server."}
    try:
        return kite.positions()
    except Exception as e:
        return {"error": str(e)}

def get_market_indicators(symbol: str) -> dict:
    """Fetch the 20-day EMA for a symbol."""
    if not kite:
        return {"error": "Kite Connect not authenticated. Please restart the server."}
    try:
        to_date = datetime.datetime.now()
        from_date = to_date - datetime.timedelta(days=30)
        ltp = kite.ltp([symbol])
        instrument_token = ltp[symbol]['instrument_token']
        data = kite.historical_data(
            instrument_token=instrument_token,
            from_date=from_date,
            to_date=to_date,
            interval="day"
        )
        closes = [candle['close'] for candle in data]
        ema = None
        period = 20
        if len(closes) >= period:
            k = 2 / (period + 1)
            ema = closes[0]
            for price in closes[1:]:
                ema = price * k + ema * (1 - k)
        return {
            "symbol": symbol,
            "ema_20": ema,
            "close_prices": closes
        }
    except Exception as e:
        return {"error": str(e)}

def get_option_chain(symbol: str) -> dict:
    """Get option chain data for a symbol."""
    if not kite:
        return {"error": "Kite Connect not authenticated. Please restart the server."}
    try:
        # Get instrument info
        instruments = kite.instruments("NFO")
        # Filter for the symbol
        symbol_instruments = [i for i in instruments if i['name'] == symbol]
        return {
            "symbol": symbol,
            "instruments": symbol_instruments[:10]  # Limit to first 10 for demo
        }
    except Exception as e:
        return {"error": str(e)}

def get_quote(symbol: str) -> dict:
    """Get latest quote for a symbol."""
    if not kite:
        return {"error": "Kite Connect not authenticated. Please restart the server."}
    try:
        quote = kite.ltp([symbol])
        return quote
    except Exception as e:
        return {"error": str(e)}

def get_news(symbol: str) -> dict:
    """Get the latest news for a symbol (stub)."""
    return {"symbol": symbol, "news": ["Sample news headline for " + symbol]}

def get_sentiment(symbol: str = None) -> dict:
    """Get the current market or symbol sentiment (stub)."""
    return {"symbol": symbol or "market", "sentiment": "neutral"}

def register_tools():
    """Register all tools with decorators after mcp is set."""
    if mcp is None:
        raise RuntimeError("MCP instance not set. Call set_mcp_instance() first.")
    
    # Apply decorators to all tool functions
    mcp.tool()(get_portfolio)
    mcp.tool()(get_market_indicators)
    mcp.tool()(get_option_chain)
    mcp.tool()(get_quote)
    mcp.tool()(get_news)
    mcp.tool()(get_sentiment) 