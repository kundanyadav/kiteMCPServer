"""
Demo MCP Server for Kite Trading Recommendation App
Provides mock data without requiring Kite Connect authentication.
Implements read-only methods based on Kite Connect API.
"""

from mcp.server.fastmcp import FastMCP
import datetime
from typing import Dict, Any, List
import random

# Initialize FastMCP server
mcp = FastMCP("kiteMCP-demo")

# Mock data generators
def generate_mock_portfolio() -> dict:
    """Generate comprehensive mock portfolio data."""
    return {
        "total_margin": 100000.0,
        "available_cash": 50000.0,
        "total_exposure": 150000.0,
        "positions": [
            {
                "symbol": "ICICIBANK",
                "quantity": 100,
                "average_price": 1500.0,
                "current_price": 1520.0,
                "pnl": 2000.0,
                "margin_used": 50000.0,
                "premium_collected": 5000.0,
                "rom": 10.0,
                "ssr": 5.0,
                "risk_indicator": 6,
                "reward_risk_ratio": 833.33,
                "position_type": "short",
                "expiry": "2024-08-29T00:00:00",
                "strike_price": 1460.0,
                "option_type": "PE"
            },
            {
                "symbol": "HDFCBANK",
                "quantity": 50,
                "average_price": 1800.0,
                "current_price": 1820.0,
                "pnl": 1000.0,
                "margin_used": 30000.0,
                "premium_collected": 3000.0,
                "rom": 10.0,
                "ssr": 3.0,
                "risk_indicator": 4,
                "reward_risk_ratio": 750.0,
                "position_type": "short",
                "expiry": "2024-08-29T00:00:00",
                "strike_price": 1750.0,
                "option_type": "PE"
            }
        ],
        "sector_exposure": {"Banking": 0.6, "IT": 0.4},
        "risk_score": 6.5
    }

def generate_mock_holdings() -> List[Dict]:
    """Generate mock holdings data."""
    return [
        {
            "tradingsymbol": "ICICIBANK",
            "exchange": "NSE",
            "isin": "INE090A01021",
            "quantity": 100,
            "t1_quantity": 0,
            "average_price": 1500.0,
            "last_price": 1520.0,
            "pnl": 2000.0,
            "product": "CNC"
        },
        {
            "tradingsymbol": "HDFCBANK",
            "exchange": "NSE",
            "isin": "INE040A01034",
            "quantity": 50,
            "t1_quantity": 0,
            "average_price": 1800.0,
            "last_price": 1820.0,
            "pnl": 1000.0,
            "product": "CNC"
        }
    ]

def generate_mock_positions() -> List[Dict]:
    """Generate mock positions data."""
    return [
        {
            "tradingsymbol": "ICICIBANK24AUG1460PE",
            "exchange": "NFO",
            "product": "MIS",
            "quantity": 100,
            "overnight_quantity": 0,
            "multiplier": 1,
            "average_price": 16.5,
            "last_price": 17.0,
            "unrealised": 50.0,
            "realised": 0.0,
            "buy_quantity": 0,
            "sell_quantity": 100,
            "buy_amount": 0.0,
            "sell_amount": 1650.0,
            "day_buy_quantity": 0,
            "day_sell_quantity": 100,
            "day_buy_amount": 0.0,
            "day_sell_amount": 1650.0
        }
    ]

def generate_mock_profile() -> Dict:
    """Generate mock user profile data."""
    return {
        "user_id": "XX0000",
        "user_name": "Demo User",
        "user_shortname": "Demo",
        "broker": "ZERODHA",
        "exchanges": ["NSE", "BSE", "NFO", "CDS"],
        "products": ["CNC", "MIS", "NRML"],
        "order_types": ["MARKET", "LIMIT", "SL", "SL-M"],
        "email": "demo@example.com",
        "mobile": "9876543210",
        "pan": "ABCDE1234F",
        "login_time": "2024-01-15 09:15:00"
    }

def generate_mock_quote(symbol: str) -> Dict:
    """Generate mock quote data."""
    base_price = random.uniform(1000, 2000)
    change = random.uniform(-50, 50)
    return {
        symbol: {
            "instrument_token": random.randint(1000000, 9999999),
            "last_price": base_price,
            "last_quantity": random.randint(100, 1000),
            "last_trade_time": datetime.datetime.now().isoformat(),
            "change": change,
            "net_change": change,
            "oi": random.randint(10000, 100000),
            "oi_day_high": random.randint(10000, 100000),
            "oi_day_low": random.randint(10000, 100000),
            "lower_circuit_limit": base_price * 0.9,
            "upper_circuit_limit": base_price * 1.1,
            "ohlc": {
                "open": base_price - random.uniform(10, 50),
                "high": base_price + random.uniform(10, 50),
                "low": base_price - random.uniform(10, 50),
                "close": base_price
            },
            "depth": {
                "buy": [
                    {"quantity": random.randint(100, 1000), "price": base_price - 1},
                    {"quantity": random.randint(100, 1000), "price": base_price - 2}
                ],
                "sell": [
                    {"quantity": random.randint(100, 1000), "price": base_price + 1},
                    {"quantity": random.randint(100, 1000), "price": base_price + 2}
                ]
            }
        }
    }

def generate_mock_ltp(symbol: str) -> Dict:
    """Generate mock last traded price data."""
    return {
        symbol: {
            "instrument_token": random.randint(1000000, 9999999),
            "last_price": random.uniform(1000, 2000)
        }
    }

def generate_mock_ohlc(symbol: str, interval: str = "day") -> Dict:
    """Generate mock OHLC data."""
    base_price = random.uniform(1000, 2000)
    return {
        "symbol": symbol,
        "interval": interval,
        "data": [
            {
                "date": (datetime.datetime.now() - datetime.timedelta(days=i)).strftime("%Y-%m-%d"),
                "open": base_price + random.uniform(-50, 50),
                "high": base_price + random.uniform(0, 100),
                "low": base_price - random.uniform(0, 100),
                "close": base_price + random.uniform(-30, 30),
                "volume": random.randint(100000, 1000000)
            }
            for i in range(30, 0, -1)
        ]
    }

def generate_mock_historical_data(symbol: str, from_date: str, to_date: str) -> List[Dict]:
    """Generate mock historical data."""
    base_price = random.uniform(1000, 2000)
    return [
        {
            "date": (datetime.datetime.now() - datetime.timedelta(days=i)).strftime("%Y-%m-%d"),
            "open": base_price + random.uniform(-50, 50),
            "high": base_price + random.uniform(0, 100),
            "low": base_price - random.uniform(0, 100),
            "close": base_price + random.uniform(-30, 30),
            "volume": random.randint(100000, 1000000)
        }
        for i in range(30, 0, -1)
    ]

def generate_mock_instruments() -> List[Dict]:
    """Generate mock instruments data."""
    return [
        {
            "instrument_token": 128000256,
            "tradingsymbol": "ICICIBANK",
            "name": "ICICI Bank Limited",
            "last_price": 1520.0,
            "expiry": "",
            "strike": 0.0,
            "tick_size": 0.05,
            "lot_size": 1,
            "instrument_type": "EQ",
            "segment": "NSE",
            "exchange": "NSE"
        },
        {
            "instrument_token": 128000257,
            "tradingsymbol": "HDFCBANK",
            "name": "HDFC Bank Limited",
            "last_price": 1820.0,
            "expiry": "",
            "strike": 0.0,
            "tick_size": 0.05,
            "lot_size": 1,
            "instrument_type": "EQ",
            "segment": "NSE",
            "exchange": "NSE"
        }
    ]

def generate_mock_orders() -> List[Dict]:
    """Generate mock orders data."""
    return [
        {
            "order_id": "240115000000001",
            "tradingsymbol": "ICICIBANK",
            "exchange": "NSE",
            "transaction_type": "SELL",
            "quantity": 100,
            "price": 1520.0,
            "order_type": "LIMIT",
            "product": "MIS",
            "validity": "DAY",
            "disclosed_quantity": 0,
            "trigger_price": 0,
            "is_amo": False,
            "order_timestamp": "2024-01-15 09:15:00",
            "exchange_timestamp": "2024-01-15 09:15:01",
            "status": "COMPLETE",
            "status_message": "Order completed successfully",
            "order_source": "API"
        }
    ]

def generate_mock_trades() -> List[Dict]:
    """Generate mock trades data."""
    return [
        {
            "trade_id": "240115000000001",
            "order_id": "240115000000001",
            "tradingsymbol": "ICICIBANK",
            "exchange": "NSE",
            "transaction_type": "SELL",
            "quantity": 100,
            "price": 1520.0,
            "trade_timestamp": "2024-01-15 09:15:01",
            "trade_source": "API"
        }
    ]

def generate_mock_margins() -> Dict:
    """Generate mock margins data."""
    return {
        "equity": {
            "enabled": True,
            "net": 100000.0,
            "available": {
                "cash": 50000.0,
                "intraday_payin": 0.0,
                "collateral": 0.0,
                "adhoc_margin": 0.0,
                "notional": 0.0,
                "span": 0.0,
                "exposure": 0.0,
                "breakup": {
                    "trading_member_obligation": 0.0,
                    "trading_member_obligation_span": 0.0,
                    "trading_member_obligation_exposure": 0.0,
                    "trading_member_obligation_additional": 0.0,
                    "trading_member_obligation_adhoc": 0.0,
                    "trading_member_obligation_notional": 0.0,
                    "trading_member_obligation_total": 0.0,
                    "trading_member_obligation_utilised": 0.0,
                    "trading_member_obligation_available": 0.0
                }
            },
            "used": {
                "payin": 0.0,
                "payout": 0.0,
                "span": 0.0,
                "exposure": 0.0,
                "adhoc_margin": 0.0,
                "notional": 0.0,
                "breakup": {
                    "trading_member_obligation_span": 0.0,
                    "trading_member_obligation_exposure": 0.0,
                    "trading_member_obligation_additional": 0.0,
                    "trading_member_obligation_adhoc": 0.0,
                    "trading_member_obligation_notional": 0.0,
                    "trading_member_obligation_total": 0.0
                }
            }
        }
    }

def generate_mock_order_margins(order_params: Dict) -> Dict:
    """Generate mock order margins calculation."""
    return {
        "total": 50000.0,
        "additional": 0.0,
        "exchanges": {
            "NSE": {
                "total": 50000.0,
                "additional": 0.0
            }
        }
    }

# Portfolio & Holdings Methods
@mcp.tool()
def get_portfolio_tool() -> dict:
    """Get current portfolio data with positions, holdings, and margins."""
    return generate_mock_portfolio()

@mcp.tool()
def get_holdings_tool() -> List[Dict]:
    """Get current holdings with P&L information."""
    return generate_mock_holdings()

@mcp.tool()
def get_positions_tool() -> List[Dict]:
    """Get current positions with risk metrics."""
    return generate_mock_positions()

@mcp.tool()
def get_profile_tool() -> Dict:
    """Get user profile and account details."""
    return generate_mock_profile()

# Market Data Methods
@mcp.tool()
def get_quote_tool(symbol: str) -> Dict:
    """Get real-time quote for a symbol."""
    return generate_mock_quote(symbol)

@mcp.tool()
def get_ltp_tool(symbol: str) -> Dict:
    """Get last traded price for a symbol."""
    return generate_mock_ltp(symbol)

@mcp.tool()
def get_ohlc_tool(symbol: str, interval: str = "day") -> Dict:
    """Get OHLC data for a symbol."""
    return generate_mock_ohlc(symbol, interval)

@mcp.tool()
def get_historical_data_tool(symbol: str, from_date: str, to_date: str) -> List[Dict]:
    """Get historical data for a symbol."""
    return generate_mock_historical_data(symbol, from_date, to_date)

@mcp.tool()
def get_instruments_tool() -> List[Dict]:
    """Get all available instruments."""
    return generate_mock_instruments()

# Order History Methods (Read-Only)
@mcp.tool()
def get_orders_tool() -> List[Dict]:
    """Get order history (read-only)."""
    return generate_mock_orders()

@mcp.tool()
def get_trades_tool() -> List[Dict]:
    """Get trade history (read-only)."""
    return generate_mock_trades()

@mcp.tool()
def get_order_history_tool(order_id: str) -> Dict:
    """Get specific order details (read-only)."""
    orders = generate_mock_orders()
    for order in orders:
        if order["order_id"] == order_id:
            return order
    return {"error": "Order not found"}

@mcp.tool()
def get_order_trades_tool(order_id: str) -> List[Dict]:
    """Get trades for specific order (read-only)."""
    trades = generate_mock_trades()
    return [trade for trade in trades if trade["order_id"] == order_id]

# Risk & Margin Methods (Read-Only)
@mcp.tool()
def get_margins_tool() -> Dict:
    """Get current margin information (read-only)."""
    return generate_mock_margins()

@mcp.tool()
def get_order_margins_tool(order_params: Dict) -> Dict:
    """Get order margin calculation (simulation only, read-only)."""
    return generate_mock_order_margins(order_params)

@mcp.tool()
def get_risk_metrics_tool() -> Dict:
    """Get portfolio risk metrics (read-only)."""
    return {
        "total_exposure": 150000.0,
        "margin_used": 100000.0,
        "available_margin": 50000.0,
        "risk_score": 6.5,
        "var_95": 5000.0,
        "max_loss": 10000.0,
        "sector_exposure": {
            "Banking": 0.6,
            "IT": 0.4
        },
        "position_concentration": {
            "ICICIBANK": 0.4,
            "HDFCBANK": 0.3
        }
    }

@mcp.tool()
def get_basket_margins_tool(instruments: List[str]) -> Dict:
    """Get basket margin calculation (simulation only, read-only)."""
    return {
        "total_margin": 75000.0,
        "additional_margin": 0.0,
        "breakup": {
            "span": 50000.0,
            "exposure": 25000.0,
            "additional": 0.0
        }
    }

# Real-time Data Methods (Read-Only)
@mcp.tool()
def subscribe_tool(instruments: List[str]) -> Dict:
    """Subscribe to real-time data (read-only)."""
    return {
        "status": "subscribed",
        "instruments": instruments,
        "message": "Successfully subscribed to real-time data"
    }

@mcp.tool()
def unsubscribe_tool(instruments: List[str]) -> Dict:
    """Unsubscribe from real-time data (read-only)."""
    return {
        "status": "unsubscribed",
        "instruments": instruments,
        "message": "Successfully unsubscribed from real-time data"
    }

@mcp.tool()
def get_streaming_data_tool() -> Dict:
    """Get real-time market data (read-only)."""
    return {
        "timestamp": datetime.datetime.now().isoformat(),
        "data": {
            "ICICIBANK": {
                "last_price": 1520.0,
                "change": 20.0,
                "volume": 1000000
            },
            "HDFCBANK": {
                "last_price": 1820.0,
                "change": 15.0,
                "volume": 800000
            }
        }
    }

# Additional Analysis Methods
@mcp.tool()
def get_market_indicators_tool(symbol: str) -> Dict:
    """Get market indicators for analysis."""
    return {
        "symbol": symbol,
        "current_price": 1520.0,
        "ema_20": 1500.0,
        "sma_50": 1480.0,
        "rsi": 65.0,
        "macd": {
            "macd": 5.0,
            "signal": 3.0,
            "histogram": 2.0
        },
        "volume": 1000000,
        "change_percent": 1.32
    }

@mcp.tool()
def get_option_chain_tool(symbol: str) -> Dict:
    """Get option chain data for analysis."""
    return {
        "symbol": symbol,
        "instruments": [
            {
                "symbol": f"{symbol}24AUG1460PE",
                "option_type": "PE",
                "strike_price": 1460.0,
                "premium": 16.5,
                "margin_required": 50000.0,
                "bid_price": 16.05,
                "ask_price": 17.10,
                "expiry": "2024-08-29",
                "lot_size": 100,
                "oi": 5000,
                "volume": 1000
            },
            {
                "symbol": f"{symbol}24AUG1580CE",
                "option_type": "CE",
                "strike_price": 1580.0,
                "premium": 12.5,
                "margin_required": 45000.0,
                "bid_price": 12.05,
                "ask_price": 13.10,
                "expiry": "2024-08-29",
                "lot_size": 100,
                "oi": 3000,
                "volume": 800
            }
        ]
    }

if __name__ == "__main__":
    print("Starting kiteMCP Demo Server...")
    print("This server provides mock data for demonstration purposes.")
    print("No Kite Connect authentication required.")
    print("All methods are READ-ONLY - no order execution capabilities.")
    print("Server will run on stdio transport.")
    print("-" * 50)
    
    # Start the server
    mcp.run(transport='stdio') 