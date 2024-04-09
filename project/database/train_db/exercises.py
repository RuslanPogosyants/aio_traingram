class Exercise:

    def __init__(self, name, description, set_repetition, url, musclegroups):
        self.name: str = name
        self.description: str = description
        self.set_repetition: str = set_repetition
        self.url: str = url
        self.musclegroups = musclegroups

    def __str__(self):
        return f'[{self.name}]({self.url}) - {self.description}\nПлан: {self.set_repetition}\nЗадействуется - {self.musclegroups}\n'

    def __repr__(self):
        return f'|[{self.name}]({self.url})|'


# Упражнения
PullUp = Exercise('Pull-Up', 'подтягивания', '2-4 рабочих подхода до отказа по 6-12 повторений', 'https://www.youtube.com/watch?v=eGo4IYlbE5g&ab_channel=Calisthenicmovement', 'спина, бицепс(косвенно)')
PushUp = Exercise('Push-Up', 'отжимания', '2-4 рабочих подхода до отказа по 15-20 повторений', 'https://www.youtube.com/watch?v=IODxDxX7oi4', 'грудь, трицепс(косвенно), передняя дельта(косвенно)')
Squat = Exercise('Squat', 'приседания', '2-4 рабочих подхода до отказа по 6-12 повторений', 'https://www.youtube.com/watch?v=ultWZbUMPL8', 'ноги: квадрицепсы, ягодицы')
Deadlift = Exercise('Deadlift', 'становая тяга', '2-4 рабочих подхода до отказа по 5-10 повторений', 'https://www.youtube.com/watch?v=ytGaGIn3SjE', 'спина, ноги')
BenchPress = Exercise('Bench Press', 'жим лежа на скамье', '2-4 рабочих подхода до отказа по 5-10 повторений', 'https://www.youtube.com/watch?v=4Y2ZdHCOXok&ab_channel=JeremyEthier', 'грудь, трицепс(косвенно), передняя дельта(косвенно)')
BarbellCurl = Exercise('Barbell Curl', 'подъем штанги на бицепс', '2-4 рабочих подхода до отказа по 8-12 повторений', 'https://www.youtube.com/watch?v=kwG2ipFRgfo', 'бицепс')
TricepExtension = Exercise('Tricep Extension', 'разгибание трицепса на блоке', '2-4 рабочих подхода до отказа по 8-12 повторений', 'https://www.youtube.com/watch?v=2-LAMcpzODU', 'трицепс')
Lunges = Exercise('Lunges', 'выпады со штангой', '2-4 рабочих подхода до отказа по 10-12 повторений на каждую ногу', 'https://www.youtube.com/watch?v=QOVaHwm-Q6U', 'ноги: квадрицепсы, ягодицы')
ShoulderPress = Exercise('Shoulder Press', 'жим штанги стоя', '2-4 рабочих подхода до отказа по 8-10 повторений', 'https://www.youtube.com/watch?v=QAQ64hK4Xxs&ab_channel=JeremyEthier', 'плечи, трицепс(косвенно)')
LegPress = Exercise('Leg Press', 'жим ногами в тренажере', '2-4 рабочих подхода до отказа по 10-12 повторений', 'https://www.youtube.com/watch?v=qCR9bN3G1t4&ab_channel=PureGym', 'ноги: квадрицепсы, ягодицы')
CableRow = Exercise('Cable Row', 'горизонтальная тяга в блоке', '2-4 рабочих подхода до отказа по 10-12 повторений', 'https://www.youtube.com/watch?v=GZbfZ033f74&ab_channel=ScottHermanFitness', 'спина, бицепс(косвенно)')
InclineBenchPress = Exercise('Incline Bench Press', 'жим лежа на наклонной скамье', '2-4 рабочих подхода до отказа по 6-10 повторений', 'https://www.youtube.com/watch?v=SrqOu55lrYU&ab_channel=ScottHermanFitness', 'грудь, трицепс(косвенно), передняя дельта(косвенно)')
HammerCurl = Exercise('Hammer Curl', 'подъем гантелей молотком на бицепс', '2-4 рабочих подхода до отказа по 10-12 повторений', 'https://www.youtube.com/watch?v=TwD-YGVP4Bk', 'бицепс: брахиалис')
ProneLegCurl = Exercise('Prone Leg Curl', 'сгибание ног в тренажере сидя', '2-4 рабочих подхода до отказа по 10-12 повторений', 'https://www.youtube.com/watch?v=vl5nUdE9mWM&ab_channel=PhysiqueDevelopment', 'ноги: задняя поверхность бедра, ягодицы')
PullDown = Exercise('Pull Down', 'тяга верхнего блока к груди', '2-4 рабочих подхода до отказа по 10-12 повторений', 'https://www.youtube.com/watch?v=trZQjegcRx0&ab_channel=MuscleandMotion', 'спина, бицепс(косвенно)')
DumbbellBenchPress = Exercise('Dumbbell Bench Press', 'жим гантелей лежа на плоской скамье', '2-4 рабочих подхода до отказа по 8-10 повторений', 'https://www.youtube.com/shorts/z6A4W5Dib28', 'грудь, трицепс(косвенно), передняя дельта(косвенно)')
PreacherCurl = Exercise('Preacher Curl', 'подъем гантели на бицепс на скамье Скотта', '2-4 рабочих подхода до отказа по 10-12 повторений', 'https://www.youtube.com/shorts/Htw-s61mOw0', 'бицепс')
FrenchPress = Exercise('French Press', 'разгибание рук с гантелями лежа на скамье с наклоном вниз', '2-4 рабочих подхода до отказа по 10-12 повторений', 'https://www.youtube.com/watch?v=JImgCWzCHwI&ab_channel=Howcast', 'трицепс')
RussianTwist = Exercise('Russian Twist', 'русский твист с отягощением', '2-4 рабочих подхода до отказа по 10-12 повторений', 'https://www.youtube.com/watch?v=pDTHSnoGoEc&ab_channel=ScottHermanFitness', 'пресс')
LegExtension = Exercise('Leg Extension', 'разгибание ног в тренажере', '2-4 рабочих подхода до отказа по 10-12 повторений', 'https://www.youtube.com/shorts/fP6uMgfwqOA', 'ноги: квадрицепсы')
LateralRaise = Exercise('Lateral Raise', 'разведение рук в стороны с гантелями', '2-4 рабочих подхода до отказа по 10-12 повторений', 'https://www.youtube.com/shorts/tx2_X7ORHeM', 'плечи: средние дельты')
UprightRow = Exercise('Upright Row', 'подтягивание штанги к подбородку', '2-4 рабочих подхода до отказа по 10-12 повторений', 'https://www.youtube.com/watch?v=nwkLwMRHMQo&ab_channel=JeffNippard', 'плечи: передние дельты')
SkullCrusher = Exercise('Skull Crusher', 'разгибание рук на скамье с гантелями или штангой', '2-4 рабочих подхода до отказа по 10-12 повторений', 'https://www.youtube.com/watch?v=d_KZxkY_0cM&ab_channel=ScottHermanFitness', 'трицепс')
BarbellBent_OverRow = Exercise('Barbell Bent-Over Row', 'тяга штанги в наклоне', '2-4 рабочих подхода до отказа по 6-10 повторений', 'https://www.youtube.com/watch?v=kBWAon7ItDw&ab_channel=JeremyEthier', 'спина, бицепс(косвенно)')
BulgarianSplitSquat = Exercise('Bulgarian Split Squat', 'болгарские выпады', '2-4 рабочих подхода до отказа по 8-12 повторений (каждая нога)', 'https://www.youtube.com/watch?v=2C-uNgKwPLE&ab_channel=ScottHermanFitness', 'ноги: квадрицепсы, ягодицы')
Dips = Exercise('Dips', 'отжимания на брусьях', '2-4 рабочих подхода до отказа по 6-12 повторений', 'https://www.youtube.com/watch?v=vi1-BOcj3cQ&ab_channel=ATHLEAN-X%E2%84%A2', 'грудь, трицепс')
RomanianDeadlift = Exercise('Romanian Deadlift', 'румынская тяга', '2-4 рабочих подхода до отказа по 6-10 повторений', 'https://www.youtube.com/watch?v=_oyxCn2iSjU&ab_channel=JeffNippard', 'ноги, задняя поверхность бедра, ягодицы')
ArnoldPress = Exercise('Arnold Press', 'жим Арнольда', '2-4 рабочих подхода до отказа по 8-10 повторений', 'https://www.youtube.com/watch?v=6Z15_WdXmVw&ab_channel=BuffDudes', 'плечи, трицепс(косвенно)')
SeatedLegCurl = Exercise('Seated Leg Curl', 'сгибание ног в тренажере сидя', '2-4 рабочих подхода до отказа по 8-12 повторений', 'https://www.youtube.com/shorts/HeNjxoJhyow', 'ноги: задняя поверхность бедра, ягодицы')
CloseGripBenchPress = Exercise('Close-Grip Bench Press', 'жим узким хватом', '2-4 рабочих подхода до отказа по 8-10 повторений', 'https://www.youtube.com/watch?v=vEUyEOVn3yM&ab_channel=BarBend', 'трицепс, грудь(косвенно)')
HangingLegRaise = Exercise('Hanging Leg Raise', 'подъем ног в висе на перекладине', '2-4 рабочих подхода до отказа по 10-20 повторений', 'https://www.youtube.com/watch?v=Pr1ieGZ5atk&ab_channel=ATHLEAN-X%E2%84%A2', 'пресс')
ReverseFly = Exercise('Reverse Fly', 'разведение рук в стороны на тренажере', '2-4 рабочих подхода до отказа по 10-12 повторений', 'https://www.youtube.com/watch?v=MOBQn99Z1T4&ab_channel=LukeHoffman', 'плечи: задняя дельта; верх спины')
InclineDumbbellPress = Exercise('Incline Dumbbell Press', 'жим гантелей лежа на наклонной скамье', '2-4 рабочих подхода до отказа по 8-10 повторений', 'https://www.youtube.com/watch?v=8iPEnn-ltC8&ab_channel=ScottHermanFitness', 'грудь, трицепс(косвенно), передняя дельта(косвенно)')
HammerStrengthRow = Exercise('Hammer Strength Row', 'тяга на тренажере Hammer Strength', '2-4 рабочих подхода до отказа по 10-12 повторений', 'https://www.youtube.com/watch?v=gy-_QDUgGi4&ab_channel=PlanetFitnessBeginner', 'спина, бицепс(косвенно)')
GluteBridge = Exercise('Glute Bridge', 'мостик для ягодиц', '2-4 рабочих подхода до отказа', 'https://www.youtube.com/watch?v=iRImeYTD2jU', 'ноги: задняя поверхность бедра, ягодицы')
Plank = Exercise('Plank', 'планка', '2-4 рабочих подхода до отказа', 'https://www.youtube.com/watch?v=ASdvN_XEl_c', 'пресс')
BoxJumps = Exercise('Box Jumps', 'прыжки на платформу (ящик)', '2-4 рабочих подхода до отказа', 'https://www.youtube.com/watch?v=aDZoErlL1LQ&ab_channel=MindPumpTV', 'кардио')
Running = Exercise('Running', "бег", '15-45 минут c пульсом 120-140', 'https://www.youtube.com/watch?v=_kGESn8ArrU&ab_channel=GlobalTriathlonNetwork', 'кардио')
JumpRope = Exercise('Jump Rope', 'прыгание на скакалке', '2-4 рабочих подхода до отказа по 1-2 минуты', 'https://www.youtube.com/watch?v=0CeGsg-1NaA&ab_channel=AustinDunham', 'кардио')
Cycling = Exercise('Cycling', 'велосипедная езда', '30-60 минут', 'https://goo.su/QziGe', 'кардио')
StairClimbing = Exercise('Stair Climbing', 'подъем по лестнице', '5-15 минут с пульсом 120-140', 'https://goo.su/QMsuO', 'кардио')
Swimming = Exercise('Swimming', 'плавание', '20-30 минут', 'https://goo.su/RFyi', 'кардио')
Burpees = Exercise('Burpees', 'берпи', '2-4 рабочих подхода до отказа', 'https://www.youtube.com/watch?v=JZQA08SlJnM', 'кардио')
ChestPressMachine = Exercise('Chest Press Machine', 'грудной жим на тренажере', '2-4 рабочих подхода до отказа по 8-12 повторений', 'https://www.youtube.com/watch?v=sqNwDkUU_Ps&ab_channel=PureGym', 'грудь, трицепс(косвенно), передняя дельта(косвенно)')
DeclineChestPress = Exercise('Decline chest press', 'жим лежа на скамье головой вниз', '2-4 рабочих подхода до отказа по 6-10 повторений', 'https://www.youtube.com/watch?v=0xRvl4Qv3ZY&ab_channel=MyTrainingApp', 'грудь, трицепс(косвенно)')
RestDay = Exercise('RestDay', 'день отдыха', 'восстанавливаться также важно, как и тренироваться', 'https://www.youtube.com/watch?v=4xqOc4hJu94&ab_channel=ATHLEAN-X%E2%84%A2', 'ничего')
Shrugs = Exercise('Shrugs', 'подъем на трапецию', '2-4 рабочих подхода до отказа по 6-12 повторений', 'https://www.youtube.com/watch?v=JEnhFC1AtHw&ab_channel=BPISports', 'трапеция')
StraightArmPulldown = Exercise('Straight-Arm Pulldown', 'тяга блока с прямыми руками стоя', '2-4 рабочих подхода до отказа по 8-12 повторений', 'https://www.youtube.com/watch?v=aD-mosukbIQ&ab_channel=OnnitAcademy', 'спина')
BehindTheBackCurl = Exercise('Behind-The-Back Curl', 'подъем на бицепс из-за спины', '2-4 рабочих подхода до отказа по 8-12 повторений', 'https://www.youtube.com/watch?v=Df0GjCkUh90&ab_channel=JimStoppani%2CPhD', 'бицепс')
MachineLateralRaise = Exercise('Machine Lateral Raise', 'разведение рук в стороны на тренажере', '2-4 рабочих подхода до отказа по 8-12 повторений', 'https://www.youtube.com/watch?v=0FUpcwj_1z4&ab_channel=AbawiFit', 'плечи: средние дельты')
TricepOverheadExtension = Exercise('Tricep Overhead Extension', 'разгибание трицепса над головой', '2-4 рабочих подхода до отказа по 8-12 повторений', 'https://www.youtube.com/shorts/OwKc1fLVD30', 'трицепс')
DumbbellBicepsCurl = Exercise('Dumbbell Biceps Curl', 'сгибание рук с гантелями на бицепс', '2-4 рабочих подхода до отказа по 8-12 повторений', 'https://www.youtube.com/watch?v=ykJmrZ5v0Oo&ab_channel=Howcast', 'бицепс')
HackSquat = Exercise('Hack Squat', 'присед на тренажере', '2-4 рабочих подхода до отказа 6-12 повторений', 'https://www.youtube.com/watch?v=0tn5K9NlCfo&ab_channel=Bodybuilding.com', 'ноги: квадрицепсы')
AbdominalCrunch = Exercise('Abdominal Crunch', 'скручивания', '2-4 рабочих подхода до отказа по 8-15 повторений', 'https://www.youtube.com/watch?v=fuPFq2EYswE&ab_channel=FitLifeFitness%2CAquaticsandPhysicalTherapy', 'пресс')
DumbbellShoulderPress = Exercise('Dumbbell Shoulder Press', 'жим гантелей на плечи', '2-4 рабочих подхода до отказа по 6-12 повторений', 'https://www.youtube.com/watch?v=qEwKCR5JCog&ab_channel=ScottHermanFitness', 'плечи, трицепс(косвенно)')

muscle_group = {
    'Грудь': (BenchPress, InclineBenchPress, ChestPressMachine, InclineDumbbellPress, DumbbellBenchPress, Dips, PushUp, DeclineChestPress),
    'Спина': (PullUp, Deadlift, PullDown, CableRow, BarbellBent_OverRow, StraightArmPulldown, Shrugs, HammerStrengthRow),
    'Ноги': (Squat, HackSquat, Lunges, LegPress, BulgarianSplitSquat, LegExtension, SeatedLegCurl, RomanianDeadlift, ProneLegCurl, GluteBridge, BoxJumps),
    'Бицепс': (BarbellCurl, DumbbellBicepsCurl, HammerCurl, PreacherCurl, BehindTheBackCurl),
    'Трицепс': (TricepExtension, TricepOverheadExtension, FrenchPress, SkullCrusher, Dips, CloseGripBenchPress),
    'Плечи': (ShoulderPress, DumbbellShoulderPress, LateralRaise, UprightRow, ArnoldPress, ReverseFly, MachineLateralRaise),
    'Пресс': (AbdominalCrunch, HangingLegRaise, RussianTwist, Plank),
    'Кардио': (Running, JumpRope, Cycling, StairClimbing, Swimming, Burpees)
}


if __name__ == '__main__':
    for muscle, exercises in muscle_group.items():
        print(muscle, *[repr(exercise) for exercise in exercises])

    print('\n\n', muscle_group['Грудь'][0])


