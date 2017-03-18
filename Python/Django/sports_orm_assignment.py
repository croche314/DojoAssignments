#...all leagues in the Atlantic region
leagues =  League.objects.filter(name__contains='Atlantic')
# all teams based in Dallas
teams =  Team.objects.filter(location__contains='Dallas')
# all teams called the Raptors
teams =  Team.objects.filter(team_name='Raptors')
# all teams whose location includes 'City'
teams =  Team.objects.filter(location__contains='City')
# all teams whose names begin with 'T'
teams =  Team.objects.filter(location__startswith='T')
# all teams, ordered alphabetically by location
teams =  Team.objects.order_by('location')
# all teams, ordered by team name in reverse alphabetical order
teams =  Team.objects.order_by('-team_name')
# every player with last name 'Cooper'
players =  Player.objects.filter(last_name__contains='Cooper')
# every player with last name 'Cooper', except for 'Joshua'
players =  Player.objects.filter(last_name='Cooper').exclude(first_name='Joshua')
# all players with first name 'Alexander' OR first name 'Wyatt'
players =  Player.objects.filter(first_name='Alexander')|Player.objects.filter(first_name='Wyatt')
