import random

from app.base.util import StringEnum


class PromptText(StringEnum):
    TASK_1_PROMPT = '''
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

class Prompt:

    @property
    def get_task_1_prompt(self):
        elements: dict = {
            1:'Be', 2:'F', 3:'Mg', 4:'Cl', 5:'O', 6:'Li', 7:'N', 8:'Al', 9:'S', 10:'Na'
        }
        random_elements = random.sample(list(elements.values()), k=3)
        data = {
            "element_1": random_elements[0],
            "element_2": random_elements[1],
            "element_3": random_elements[2],
        }
        return PromptText.TASK_1_PROMPT.format(**data)
