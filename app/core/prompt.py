import random

from app.base.util import StringEnum


class PromptText(StringEnum):
    TASK_ONE_PROMPT: str = '''
Дана формулировка задания:
"Для выполнения заданий 1−3 используйте следующий ряд химических элементов:
1. {element_1}
2. F
3. Mg
4. {element_2}
5. {element_3}
Ответом в заданиях 1−3 является последовательность цифр, под которыми указаны химические элементы в данном ряду.
Определите, какие из указанных элементов образуют положительный или отрицательный ион с электронной конфигурацией неона.
Запишите в поле ответа номера выбранных элементов в порядке возрастания."

Напиши похожее задание за основу возьми шаблон формулировки
'''
    TASK_TWO_PROMPT: str = '''
Дана формулировка задания:
"Для выполнения заданий 1−3 используйте следующий ряд химических элементов:

1. {element_1}
2. {element_2}
3. {element_3}
4. {element_4}
5. {element_5}
Ответом в заданиях 1−3 является последовательность цифр, под которыми указаны химические элементы в данном ряду.
Выберите три элемента, которые в Периодической системе находятся в одной группе, и расположите эти элементы в порядке
уменьшения электроотрицательности. Запишите в поле ответа номера выбранных элементов в нужной последовательности."

Напиши похожее задание за основу возьми шаблон формулировки
'''
    TASK_THREE_PROMPT: str = '''
Дана формулировка задания:
"Для выполнения заданий 1−3 используйте следующий ряд химических элементов:

1. {element_1}
2. {element_2}
3. {element_3}
4. {element_4}
5. {element_5}
Ответом в заданиях 1−3 является последовательность цифр, под которыми указаны химические элементы в данном ряду.

Выберите два элемента, которые в соединениях могут иметь степень окисления −2. Запишите в поле ответа номера выбранных
элементов в порядке возрастания."

Напиши похожее задание за основу возьми шаблон формулировки
'''
    TASK_FOUR_PROMPT: str = '''
Дана формулировка задания:
"Из предложенного перечня выберите два вещества, кристаллическая решетка которых такая же, как и у сахарозы.

1. Ацетат натрия.
2. Этанол.
3. Оксид кремния.
4. Углекислый газ.
5. Ртуть.
Запишите в поле ответа номера выбранных веществ."

Напиши похожее задание за основу возьми шаблон формулировки
'''
    TASK_FIVE_PROMPT: str = '''
Дана формулировка задания:
"Среди предложенных формул веществ, расположенных в пронумерованных ячейках, выберите формулы:
А) кислой соли; Б) средней соли; В) амфотерного гидроксида.
1. Ni 2. CsOH 3. B(OH)3 4. AL(OH)3 5. HNO3 6. KAL(SO4)2 7.H2O 8. NaHCO3 9. Na2ZnO2
"

Напиши похожее задание за основу возьми шаблон формулировки
'''
    TASK_SIX_PROMPT: str = ''
    TASK_SEVEN_PROMPT: str = ''
    TASK_EIGHT_PROMPT: str = ''
    TASK_NINE_PROMPT: str = ''
    TASK_TEN_PROMPT: str = ''
    TASK_ELEVEN_PROMPT: str = ''
    TASK_TWELVE_PROMPT: str = ''


class Prompt:
    ELEMENTS: dict = {
        1: 'Be', 2: 'F', 3: 'Mg', 4: 'Cl', 5: 'O', 6: 'Li', 7: 'N', 8: 'Al', 9: 'S', 10: 'Na'
    }

    @property
    def get_task_one_prompt(self) -> str:
        random_elements = random.sample(list(self.ELEMENTS.values()), k=3)
        data = {
            "element_1": random_elements[0],
            "element_2": random_elements[1],
            "element_3": random_elements[2],
        }
        return PromptText.TASK_ONE_PROMPT.format(**data)

    @property
    def get_task_two_prompt(self) -> str:
        random_elements = random.sample(list(self.ELEMENTS.values()), k=5)
        data = {
            "element_1": random_elements[0],
            "element_2": random_elements[1],
            "element_3": random_elements[2],
            "element_4": random_elements[3],
            "element_5": random_elements[4],
        }
        return PromptText.TASK_TWO_PROMPT.format(**data)

    @property
    def get_task_three_prompt(self) -> str:
        random_elements = random.sample(list(self.ELEMENTS.values()), k=5)
        data = {
            "element_1": random_elements[0],
            "element_2": random_elements[1],
            "element_3": random_elements[2],
            "element_4": random_elements[3],
            "element_5": random_elements[4],
        }
        return PromptText.TASK_THREE_PROMPT.format(**data)

    @property
    def get_task_four_prompt(self) -> str:
        return PromptText.TASK_FOUR_PROMPT

    @property
    def get_task_five_prompt(self) -> str:
        return PromptText.TASK_FIVE_PROMPT

    @property
    def get_task_six_prompt(self) -> str:
        return 'Напиши задание по химиии из ЕГЭ'

    @property
    def get_task_seven_prompt(self) -> str:
        return 'Напиши задание по химиии из ЕГЭ'

    @property
    def get_task_eight_prompt(self) -> str:
        return 'Напиши задание по химиии из ЕГЭ'

    @property
    def get_task_nine_prompt(self) -> str:
        return 'Напиши задание по химиии из ЕГЭ'

    @property
    def get_task_ten_prompt(self) -> str:
        return 'Напиши задание по химиии из ЕГЭ'

    @property
    def get_task_twelve_prompt(self) -> str:
        return 'Напиши задание по химиии из ЕГЭ'
