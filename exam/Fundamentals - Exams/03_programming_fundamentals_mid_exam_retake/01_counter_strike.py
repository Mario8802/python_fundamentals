health = int(input())
command = input()
win_games = 0

while command != 'End of battle':
    distance_to_reach_an_enemy = int(command)

    if health < distance_to_reach_an_enemy:
        print(f'Not enough energy! Game ends with {win_games} won battles and {health} energy')
        break

    health -= distance_to_reach_an_enemy
    win_games += 1

    if win_games % 3 == 0:
        health += win_games

    command = input()

if command == 'End of battle':
    print(f'Won battles: {win_games}. Energy left: {health}')