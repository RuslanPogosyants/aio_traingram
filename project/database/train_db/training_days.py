from .exercises import *


class TrainDay:
    def __init__(self, name, exercises=None):
        if exercises is None:
            exercises = []
        self.name: str = name
        self.exercises: list[Exercise] = exercises

    def __str__(self):
        exercises = '\n'.join([str(exercise) for exercise in self.exercises])
        return f"{self.name:^20}\n{str(exercises)}\n"

    def __repr__(self):
        exercises = '\n'.join([repr(exercise) for exercise in self.exercises])
        return f'|{self.name}|\n{exercises}'


LegDay = TrainDay("День Ног", [Squat, HackSquat, Lunges, LegPress, BulgarianSplitSquat, LegExtension, SeatedLegCurl, RomanianDeadlift, ProneLegCurl, GluteBridge, BoxJumps])
ChestDay = TrainDay("День Груди", [BenchPress, InclineBenchPress, ChestPressMachine, InclineDumbbellPress, DumbbellBenchPress, Dips, PushUp, ])
HIITDay = TrainDay("Высокоинтенсивная Тренировка", [Running, JumpRope, Burpees, Lunges, Squat, Deadlift])
CardioDay = TrainDay("Кардио", [Running, JumpRope, Cycling, StairClimbing, Swimming, Burpees])
ArmDay = TrainDay("День Рук", [BarbellCurl, DumbbellBicepsCurl, HammerCurl, PreacherCurl, BehindTheBackCurl, TricepExtension, TricepOverheadExtension, FrenchPress, SkullCrusher, Dips, CloseGripBenchPress])
BackDay = TrainDay("День Спины", [PullUp, Deadlift, PullDown, CableRow, BarbellBent_OverRow, StraightArmPulldown, Shrugs, HammerStrengthRow])
FullBodyDay = TrainDay("День Тренировки Всего Тела", [Squat, Deadlift, BenchPress, PullUp, ShoulderPress, Lunges, BarbellCurl, TricepExtension])
RelaxDay = TrainDay('Сегодня вы можете отдохнуть! Восстанавливайтесь!', [])

WorkoutDays = [LegDay, ChestDay, HIITDay, CardioDay, ArmDay, BackDay, FullBodyDay, RelaxDay]

if __name__ == '__main__':
    for day in WorkoutDays:
        print(day)

    for day in WorkoutDays:
        print(repr(day))
