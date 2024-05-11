data = input()
user_points = {}
language_submissions = {}

while data != 'exam finished':
    data = data.split('-')
    if data[1] == 'banned':
        user = data[0]
        del user_points[user]
    else:
        user, language, points = data
        points = int(points)
        if user in user_points:
            if user_points[user] < points:
                user_points[user] = points
        else:
            user_points[user] = points

        if language not in language_submissions:
            language_submissions[language] = 0
        language_submissions[language] += 1

    data = input()

print('Results:')
for user, points in user_points.items():
    print(f'{user} | {points}')
print('Submissions:')
for lang, submissions in language_submissions.items():
    print(f'{lang} - {submissions}')


class ExamManager:
    def __init__(self):
        self.user_points = {}
        self.language_submissions = {}

    def process_data(self, data):
        data = data.split('-')
        if data[1] == 'banned':
            user = data[0]
            del self.user_points[user]
        else:
            user, language, points = data
            points = int(points)
            if user in self.user_points:
                if self.user_points[user] < points:
                    self.user_points[user] = points
            else:
                self.user_points[user] = points

            if language not in self.language_submissions:
                self.language_submissions[language] = 0
            self.language_submissions[language] += 1

    def print_results(self):
        print('Results:')
        for user, points in self.user_points.items():
            print(f'{user} | {points}')

        print('Submissions:')
        for lang, submissions in self.language_submissions.items():
            print(f'{lang} - {submissions}')

    def process_exam_data(self):
        data = input()
        while data != 'exam finished':
            self.process_data(data)
            data = input()
        self.print_results()

if __name__ == "__main__":
    exam_manager = ExamManager()
    exam_manager.process_exam_data()
