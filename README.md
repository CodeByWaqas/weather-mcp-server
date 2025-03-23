# Weather MCP Server

A Modern Code Protocol (MCP) server that provides weather information using the OpenWeatherMap API.

## Features

- Real-time weather data retrieval
- Metric units for temperature
- Detailed weather information including:
  - Temperature
  - Humidity
  - Wind Speed
  - Sunrise/Sunset times
  - Weather description

## Prerequisites

- Python 3.12 or higher
- OpenWeatherMap API key

## Installation

1. Clone the repository
2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```
3. Install dependencies:
```bash
pip install -e .
```

## Setup Intructions

### Setup with Claude Desktop
```json
# claude_desktop_config.json
# Can find location through:
# Claude -> Settings -> Developer -> Edit Config
{
  "mcpServers": {
      "mcp-weather-project": {
          "command": "uv",
          "args": [
              "--directory",
              "/<absolute-path>/weather-mcp-server/src/resources",
              "run",
              "server.py"
          ],
          "env": {
            "WEATHER_API_KEY": "YOUR_API_KEY"
          }
      }
  }
}
```
## Local/Dev Setup Instructions
### Clone repo
`git clone https://github.com/CodeByWaqas/weather-mcp-server`
### Install dependencies
Install MCP server dependencies:
```bash
cd weather-mcp-server

# Create virtual environment and activate it
uv venv

source .venv/bin/activate # MacOS/Linux
# OR
.venv/Scripts/activate # Windows

# Install dependencies
uv add "mcp[cli]" python-dotenv requests httpx
```

## Configuration

1. Copy `src/resources/env.example` to `src/resources/.env`
2. Add your OpenWeatherMap API key to the `.env` file:
```
WEATHER_API_KEY=your_api_key_here
```

## Usage

Run the Claude Desktop and use LLM to retrieve weather info

## License

This project is licensed under the MIT License - see the LICENSE file for details.
