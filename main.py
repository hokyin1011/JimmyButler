from nba_api.stats.static import players
player_dic=players.get_players()

butler = [player for player in player_dic if player["full_name"]== 'Jimmy Butler'][0]
butler_id = butler['id']

from nba_api.stats.static import teams
team_dict = teams.get_teams()
MH = [team for team in team_dict if team['full_name']=='Miami Heat']

from nba_api.stats.endpoints import playergamelog 

gamelog_butler = playergamelog.PlayerGameLog(player_id='202710', season='2023')
gamelog_butler_df = gamelog_butler.get_data_frames()[0]

