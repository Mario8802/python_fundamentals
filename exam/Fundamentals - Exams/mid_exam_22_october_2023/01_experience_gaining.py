

needed_experience = float(input())
battles = int(input())
experience = 0
experience_gained = False

for battle in range(1, battles + 1):
    experience_per_battle = float(input())

    if battle % 3 == 0:
        experience_per_battle += experience_per_battle * 0.15

    if battle % 5 == 0:
        experience_per_battle -= experience_per_battle * 0.10

    experience += experience_per_battle

    if experience >= needed_experience:
        experience_gained = True
        break

if experience_gained:
    print(f"Player successfully collected his needed experience for {battle} battles.")
else:
    print(f"Player was not able to collect the needed experience, {abs(experience-needed_experience):.2f} more needed.")