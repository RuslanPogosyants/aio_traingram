from project.database.train_db.training_days import *


def photo_into_bytes(path):
    with open(path, 'rb') as f:
        return f.read()


class Split:

    def __init__(self, name, description, photo_path, days):
        self.name: str = name
        self.description: str = description
        self.photo_in_bytes: bytes = photo_into_bytes(photo_path)
        self.days: list[TrainDay] = days

    def __str__(self):
        split_days = '\n'.join([str(day) for day in self.days])
        return f"{self.name} - {self.description}\n{split_days}\n"

    def __repr__(self):
        split_days = '\n'.join([repr(day) for day in self.days])
        return f"{self.name} - {self.description}\n{split_days}\n"


push_pull_legs = Split(name='Push-Pull-Legs', description='Тренировочный план Push-Pull-Legs (также известный как PPL) - это методика тренировок, которая разделяет упражнения на три основные группы: Push (толчки), Pull (тяги) и Legs (ноги). Каждая группа упражнений ориентирована на определенные мышечные группы и функциональные движения.',
                       photo_path=r'C:\Users\Ruslan\PycharmProjects\workoutgram\project\database\train_db\Photo\PPL.jpg',
                       days=[ChestDay, RelaxDay, BackDay, HIITDay, RelaxDay, LegDay])

upper_lower = Split(name='UpperLowerSplit', description='UpperLowerSplit – это сплит, разделяющий тренировки на Верхнюю часть тела (Upper) и Нижнюю часть тела (Lower). Позволяет эффективно развивать мышечную массу, силу и выносливость, обеспечивая всесторонний прогресс вашего физического состояния.',
                    photo_path=r'C:\Users\Ruslan\PycharmProjects\workoutgram\project\database\train_db\Photo\UL.jpg',
                    days=[BackDay, RelaxDay, LegDay, ChestDay, RelaxDay, CardioDay, ArmDay, RelaxDay, LegDay])

full_body = Split(name='FullBody', description='FullBody сплит - программа тренировок для всего тела, включающая упражнения на все группы мышц. Позволяет эффективно развивать мышечную массу, силу и выносливость, обеспечивая всесторонний прогресс вашего физического состояния.',
                  photo_path=r'C:\Users\Ruslan\PycharmProjects\workoutgram\project\database\train_db\Photo\FB.jpg',
                  days=[FullBodyDay, RelaxDay, ArmDay, RelaxDay, HIITDay, RelaxDay, FullBodyDay, RelaxDay, CardioDay, RelaxDay])

split_list = [push_pull_legs, upper_lower, full_body]


if __name__ == '__main__':
    for split in split_list:
        print(split.name + '\n' + split.description + '\n')

    for split in split_list:
        print(repr(split))
