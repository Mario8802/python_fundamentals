number_of_messages = int(input())
sms = ""
for _ in range(number_of_messages):
    number = int(input())

    if number == 88:
        sms = "Hello"
    elif number == 86:
        sms = "How are you?"
    elif number < 88:
        sms = "GREAT!"
    elif number > 88:
        sms = "Bye."
    print(sms)
