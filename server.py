# server.py
from fastmcp import FastMCP
from balldontlie import BalldontlieAPI

from typing import Optional, List

api = BalldontlieAPI(api_key="d0ee7bf2-957c-49c4-a411-abbf8c707431")
mcp = FastMCP("NBA Score Server")

@mcp.tool()
def nba_teams () -> dict:
    """
    Retrieve a list of all NBA teams.
    """
    return api.nba.teams.list()

@mcp.tool()
def nba_teams_details (team_id: int) -> dict:
    """
    Retrieve detailed information about a specific NBA team, including roster.
    """
    return api.nba.teams.get(team_id)

@mcp.tool()
def nba_players(
    search: Optional[str] = None,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    team_ids: Optional[List[int]] = None,
    player_ids: Optional[List[int]] = None,
) -> dict:
    """
    Retrieves a list of NBA players. Supports filtering by name, team ID, player ID, and pagination options.
    """
    try:
        return api.nba.players.list(
            search=search,
            first_name=first_name,
            last_name=last_name,
            team_ids=team_ids,
            player_ids=player_ids,
        )
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_player_by_id(player_id: int) -> dict:
    """
    Retrieves details of a specific NBA player by their unique ID.
    """
    try:
        return api.nba.players.get(player_id)
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def nba_games(
    dates: Optional[List[str]] = None,
    seasons: Optional[List[int]] = None,
    team_ids: Optional[List[int]] = None,
    postseason: Optional[bool] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
) -> dict:
    """
    Retrieves NBA games with support for pagination, filtering by date, season, team, and whether it's postseason.
    """
    try:
        return api.nba.games.list(
            dates=dates,
            seasons=seasons,
            team_ids=team_ids,
            postseason=postseason,
            start_date=start_date,
            end_date=end_date,
        )
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def nba_game_by_id(game_id: int) -> dict:
    """
    Retrieve details of a specific NBA game by its ID.
    """
    try:
        return api.nba.games.get(game_id)
    except Exception as e:
        return {"error": str(e)}
    
@mcp.tool()
def nba_live_box_scores() -> dict:
    """
    Retrieve all live NBA box scores.
    """
    try:
        return api.nba.box_scores.get_live()
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def nba_box_scores_by_date(date: str) -> dict:
    """
    Retrieve all NBA box scores for a specific date.
    """
    try:
        return api.nba.box_scores.get_by_date(date=date)
    except Exception as e:
        return {"error": str(e)}
    
if __name__ == "__main__":
    mcp.run()