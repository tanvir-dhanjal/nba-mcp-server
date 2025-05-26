# NBA MCP Server

A Model Context Protocol (MCP) server that provides access to NBA data. This server enables AI assistants to retrieve NBA information including teams, players, games, and box scores.

## Features

- Team information and rosters
- Player search and details
- Game data with filtering options
- Live and historical box scores

## Prerequisites

- Python 3.10+
- API key (get from provider)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/nba-mcp-server.git
cd nba-mcp-server
```

2. Install dependencies:
```bash
source .venv/bin/activate
pip install fastmcp balldontlie
```

3. Add your API key to `server.py`

## Usage

```bash
python server.py
```

## Available Tools

**Teams**
- `nba_teams()` - List all teams
- `nba_teams_details(team_id)` - Team details and roster

**Players**
- `nba_players()` - Search players with filters
- `get_player_by_id(player_id)` - Player details

**Games**
- `nba_games()` - Games with date/team filters
- `nba_game_by_id(game_id)` - Game details

**Box Scores**
- `nba_live_box_scores()` - Live scores
- `nba_box_scores_by_date(date)` - Scores by date

## Configuration

Update your API key:
```python
api = BalldontlieAPI(api_key="YOUR_API_KEY")
```

## License

MIT License
