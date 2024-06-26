class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []

while True:
    command = input()

    if command == 'Stop':
        break

    sender, receiver, content = command.split()
    email = Email(sender, receiver, content)
    emails.append(email)

indices = list(map(int, input().split(', ')))
for x in indices:
    emails[x].send()

for email in emails:
    print(email.get_info())



===================================================================================




class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
line = input()

while line != "Stop":
    sender, receiver, content = line.split()
    email = Email(sender, receiver, content)
    emails.append(email)
    line = input()

send_emails = [int(x) for x in input().split(', ')]

for idx in send_emails:
    emails[idx].send()

for email in emails:
    print(email.get_info())
