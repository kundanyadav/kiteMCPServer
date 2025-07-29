"""
MCP Prompts for kiteMCP server.
Contains structured templates that guide LLMs for specific trading tasks.
"""

mcp = None

def set_mcp_instance(mcp_instance):
    """Set the MCP instance from the main server."""
    global mcp
    mcp = mcp_instance

def portfolio_analysis_prompt(symbol: str = None, timeframe: str = "1d") -> str:
    """
    Analyze portfolio positions and provide trading insights.
    Use this prompt to get structured portfolio analysis.
    """
    return f"""
You are a professional options trading analyst. Analyze the portfolio data and provide insights.

CONTEXT:
- Symbol: {symbol or "All positions"}
- Timeframe: {timeframe}
- Focus on: Risk assessment, profit/loss analysis, position sizing, and recommendations

TASK:
1. Review current portfolio positions
2. Identify high-risk positions
3. Suggest hedging strategies
4. Recommend position adjustments
5. Provide clear, actionable advice

Use the available tools to gather data and provide comprehensive analysis.
"""

def market_sentiment_prompt(symbol: str, indicator: str = "EMA") -> str:
    """
    Analyze market sentiment and technical indicators for trading decisions.
    """
    return f"""
You are a technical analyst specializing in market sentiment analysis.

CONTEXT:
- Symbol: {symbol}
- Primary Indicator: {indicator}
- Focus: Market trend, momentum, support/resistance levels

TASK:
1. Analyze the {indicator} data for {symbol}
2. Determine market sentiment (bullish/bearish/neutral)
3. Identify key support and resistance levels
4. Suggest entry/exit points
5. Assess risk-reward ratio

Provide clear, data-driven insights for trading decisions.
"""

def options_strategy_prompt(symbol: str, strategy_type: str = "neutral") -> str:
    """
    Generate options trading strategies based on market conditions.
    """
    return f"""
You are an options trading strategist. Create strategies based on market analysis.

CONTEXT:
- Symbol: {symbol}
- Strategy Type: {strategy_type}
- Focus: Risk management, profit potential, market conditions

TASK:
1. Analyze current market conditions for {symbol}
2. Design appropriate options strategies:
   - For bullish markets: Call spreads, covered calls
   - For bearish markets: Put spreads, protective puts
   - For neutral markets: Iron condors, straddles
3. Calculate risk-reward ratios
4. Suggest position sizing
5. Provide exit strategies

Ensure strategies align with current market sentiment and risk tolerance.
"""

def risk_assessment_prompt(portfolio_value: float = None) -> str:
    """
    Assess portfolio risk and provide risk management recommendations.
    """
    return f"""
You are a risk management specialist for options trading.

CONTEXT:
- Portfolio Value: {portfolio_value or "Current portfolio"}
- Focus: Risk assessment, position sizing, diversification

TASK:
1. Evaluate current portfolio risk exposure
2. Identify concentration risks
3. Assess correlation between positions
4. Suggest diversification strategies
5. Recommend position size limits
6. Provide hedging recommendations

Prioritize capital preservation while maintaining profit potential.
"""

def register_prompts():
    """Register all prompts with decorators after mcp is set."""
    if mcp is None:
        raise RuntimeError("MCP instance not set. Call set_mcp_instance() first.")
    
    # Apply decorators to all prompt functions
    mcp.prompt("portfolio_analysis")(portfolio_analysis_prompt)
    mcp.prompt("market_sentiment")(market_sentiment_prompt)
    mcp.prompt("options_strategy")(options_strategy_prompt)
    mcp.prompt("risk_assessment")(risk_assessment_prompt) 