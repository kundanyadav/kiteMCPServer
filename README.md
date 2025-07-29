# kiteMCP Server

## Overview
This directory contains the MCP (Model Context Protocol) server that securely connects to the Kite Connect API and exposes safe trading tools, prompts, and resources for LLM/agent use.

## Files
- `mcp_server.py` - Main MCP server implementation
- `tools.py` - Trading tools exposed to the agent/LLM
- `prompts.py` - Structured prompt templates
- `resources.py` - Market data and trading knowledge resources
- `requirements.txt` - Python dependencies
- `README.md` - This file

## Quick Start
```bash
cd MCPServer
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python mcp_server.py
```

## Features
- Secure authentication with Kite Connect API
- Tools for portfolio analysis, market indicators, option chains
- Structured prompts for LLM guidance
- Market data and trading knowledge resources
- No secrets exposed to agent/LLM

## Security
- API keys and tokens handled only at server startup
- Only safe, post-authenticated tools exposed
- Single-user, single-session design 