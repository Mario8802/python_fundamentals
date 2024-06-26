force_side_dictionary = {}
command = input()
while command != "Lumpawaroo":
    if "|" in command:
        force_side, force_user = command.split(" | ")
        user_is_part_of_the_force = False
        for value in force_side_dictionary.values():
            if force_user in value:
                user_is_part_of_the_force = True
                break
        if not user_is_part_of_the_force:
            if force_side not in force_side_dictionary.keys():
                force_side_dictionary[force_side] = []
            force_side_dictionary[force_side].append(force_user)
    elif "->" in command:
        force_user, force_side = command.split(" -> ")
        for value in force_side_dictionary.values():
            if force_user in value:
                value.remove(force_user)
                break
        if force_side not in force_side_dictionary.keys():
            force_side_dictionary[force_side] = []
        force_side_dictionary[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")
    command = input()
for force_side, force_users in force_side_dictionary.items():
    if len(force_users) > 0:
        print(f"Side: {force_side}, Members: {len(force_users)}")
        for force_user in force_users:
            print(f"! {force_user}")



# The force users struggle to remember which side is the different force users from because they switch them too often.
# So you are tasked to create a web application to manage their profiles.
# You should store information for every unique force user registered in the application.
# You will receive several input lines in one of the following formats:
# "{force_side} | {force_user}"
# "{force_user} -> {force_side}"
# The "force_user" and "force_side" are strings, containing any character.
# If you receive "force_side | force_user":
#     • If there is no such force user and no such force side -> create a new force side
# and add the force user to the corresponding side.
#     • Only if there is no such force user in any force side -> add the force user to the corresponding side.
#     • If there is such force user already -> skip the command and continue to the next operation.
# If you receive a "force_user -> force_side":
#     • If there is such force user already -> change their side.
#     • If there is no such force user in any force side -> add the force user to the corresponding force side.
#     • If there is no such force user and no such force side -> create new force side
# and add the force user to the corresponding side.
#     • Then you should print on the console: "{force_user} joins the {force_side} side!".
# You should end your program when you receive the command "Lumpawaroo". At that point,
# you should print each force side. For each side, print the force users.
# In case there are no force users on a side, you shouldn't print the side information.
# Input / Constraints
#     • The input comes in the form of commands in one of the formats specified above.
#     • The input ends when you receive the command "Lumpawaroo".
# Output
#     • As output for each force side, you must print all the force users.
#     • The output format is:
# "Side: {force_side}, Members: {force_users_count}
# ! {force_user1}

from flask import Flask, request, jsonify

app = Flask(__name__)
force_side_dictionary = {}

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    force_side = data.get('force_side')
    force_user = data.get('force_user')
    if force_side and force_user:
        if force_user not in force_side_dictionary.values():
            if force_side not in force_side_dictionary:
                force_side_dictionary[force_side] = []
            force_side_dictionary[force_side].append(force_user)
            return jsonify({'message': f"{force_user} joins the {force_side} side!"}), 200
        else:
            return jsonify({'message': 'User already exists.'}), 400
    else:
        return jsonify({'message': 'Missing force_side or force_user in request.'}), 400

@app.route('/change_side', methods=['POST'])
def change_side():
    data = request.json
    force_user = data.get('force_user')
    force_side = data.get('force_side')
    if force_user and force_side:
        for value in force_side_dictionary.values():
            if force_user in value:
                value.remove(force_user)
                break
        if force_side not in force_side_dictionary:
            force_side_dictionary[force_side] = []
        force_side_dictionary[force_side].append(force_user)
        return jsonify({'message': f"{force_user} joins the {force_side} side!"}), 200
    else:
        return jsonify({'message': 'Missing force_side or force_user in request.'}), 400

@app.route('/force_sides', methods=['GET'])
def get_force_sides():
    return jsonify(force_side_dictionary), 200

if __name__ == '__main__':
    app.run(debug=True)

===================================================================



class ForceManager:
    def __init__(self):
        self.force_side_dict = {}

    def add_user_to_side(self, force_side, force_user):
        if force_user not in [user for users in self.force_side_dict.values() for user in users]:
            if force_side not in self.force_side_dict:
                self.force_side_dict[force_side] = []
            self.force_side_dict[force_side].append(force_user)

    def change_user_side(self, force_user, force_side):
        for value in self.force_side_dict.values():
            if force_user in value:
                value.remove(force_user)
                break
        if force_side not in self.force_side_dict:
            self.force_side_dict[force_side] = []
        self.force_side_dict[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

    def print_force_sides(self):
        for force_side, force_users in self.force_side_dict.items():
            if force_users:
                print(f"Side: {force_side}, Members: {len(force_users)}")
                for force_user in force_users:
                    print(f"! {force_user}")

    def process_commands(self):
        command = input()

        while command != "Lumpawaroo":
            if "|" in command:
                force_side, force_user = command.split(" | ")
                self.add_user_to_side(force_side, force_user)
            elif "->" in command:
                force_user, force_side = command.split(" -> ")
                self.change_user_side(force_user, force_side)
            command = input()

        self.print_force_sides()

if __name__ == "__main__":
    force_manager = ForceManager()
    force_manager.process_commands()

