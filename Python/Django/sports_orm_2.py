# all teams in the Atlantic Soccer Conference
	these_teams = Team.objects.filter(league__name='Atlantic Soccer Conference')
# all (current) players on the Boston Penguins
	these_players = Player.objects.filter(curr_team__location='Boston').filter(curr_team__team_name='Penguins')
# all (current) players in the International Collegiate Baseball Conference
	these_players = Player.objects.filter(curr_team__league__name='International Collegiate Baseball Conference')
# all (current) players in the American Conference of Amateur Football with last name "Lopez"
	these_players = Player.objects.filter(last_name='Lopez').filter(curr_team__league__name='American Conference of Amateur Football')
# all football players
	these_players = Player.objects.filter(curr_team__league__sport='Football')
# all teams with a (current) player named "Sophia"
	teams = Team.objects.filter(curr_players__first_name='Sophia')
# all leagues with a (current) player named "Sophia"
	leagues = League.objects.filter(teams__curr_players__first_name='Sophia')
# everyone with the last name "Flores" who DOESN'T (currently) play for the Washington Roughriders
	players = Player.objects.filter(last_name='Flores').exclude(curr_team__location='Washington')
