team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
team_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']

players = input().split()
game_over = False

for player in players:
    if player in team_a:
        team_a.remove(player)
    elif player in team_b:
        team_b.remove(player)
    if len(team_a) < 7 or len(team_b) < 7:
        game_over = True
        break
print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if game_over:
    print("Game was terminated")


==================================================================================================

team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

cards = input().split()
for card in cards:
    team, player = card.split('-')
    player = int(player)

    if team == "A" and player in team_a:
        team_a.remove(player)
    elif team == "B" and player in team_b:
        team_b.remove(player)

    if len(team_a) < 7 or len(team_b) < 7:
        print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
        print("Game was terminated")
        break

if len(team_a) >= 7 and len(team_b) >= 7:
    print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")



==================================================================================================

team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
team_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']

cards = input().split()
game_over = False

for player in cards:
    if player in team_a:
        team_a.remove(player)

    elif player in team_b:
        team_b.remove(player)

    if len(team_a) < 7 or len(team_b) < 7:
        game_over = True
        break
print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if game_over:
    print("Game was terminated")
