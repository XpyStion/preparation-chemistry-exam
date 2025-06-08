import random

from ...base.base.util import StringEnum


class PromptText(StringEnum):
    TASK_1_P1_PROMPT: str = '''
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
    TASK_2_P1_PROMPT: str = '''
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
    TASK_3_P1_PROMPT: str = '''
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
    TASK_4_P1_PROMPT: str = '''
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
    TASK_5_P1_PROMPT: str = '''
Дана формулировка задания:
"Среди предложенных формул веществ, расположенных в пронумерованных ячейках, выберите формулы:
А) кислой соли; Б) средней соли; В) амфотерного гидроксида.
1. Ni 2. CsOH 3. B(OH)3 4. AL(OH)3 5. HNO3 6. KAL(SO4)2 7.H2O 8. NaHCO3 9. Na2ZnO2
"

Напиши похожее задание за основу возьми шаблон формулировки
'''
    TASK_6_P1_PROMPT: str = 'Напиши задание по химиии из ЕГЭ'
    TASK_7_P1_PROMPT: str = 'Напиши задание по химиии из ЕГЭ'
    TASK_8_P1_PROMPT: str = 'Напиши задание по химиии из ЕГЭ'
    TASK_9_P1_PROMPT: str = 'Напиши задание по химиии из ЕГЭ'
    TASK_10_P1_PROMPT: str = 'Напиши задание по химиии из ЕГЭ'
    TASK_11_P1_PROMPT: str = 'Напиши задание по химиии из ЕГЭ'
    TASK_12_P1_PROMPT: str = 'Напиши задание по химиии из ЕГЭ'
    TASK_13_P1_PROMPT: str = 'Напиши задание по химиии из ЕГЭ'
    TASK_14_P1_PROMPT: str = 'Напиши задание по химиии из ЕГЭ'
    TASK_15_P1_PROMPT: str = 'Напиши задание по химиии из ЕГЭ'
    TASK_16_P1_PROMPT: str = 'Напиши задание по химиии из ЕГЭ'
    TASK_17_P1_PROMPT: str = 'Напиши задание по химиии из ЕГЭ'
    TASK_18_P1_PROMPT: str = 'Напиши задание по химиии из ЕГЭ'
    TASK_19_P1_PROMPT: str = 'Напиши задание по химиии из ЕГЭ'
    TASK_20_P1_PROMPT: str = 'Напиши задание по химиии из ЕГЭ'
    TASK_1_P2_PROMPT: str = '''
"Для выполнения задания используйте следующий перечень веществ: сульфит натрия, гипохлорит калия, иодид аммония, фосфат
кальция, оксид магния, разбавленная серная кислота. Допустимо использование водных растворов веществ.

Из предложенного перечня выберите вещества, между которыми возможна окислительно-восстановительная реакция, приводящая
к изменению цвета раствора, и запишите уравнение этой реакции. Составьте электронный баланс, укажите окислитель
и восстановитель."

Напиши похожее задание за основу возьми шаблон формулировки
'''
    TASK_2_P2_PROMPT: str = '''
"Для выполнения задания используйте следующий перечень веществ: сульфит натрия, гипохлорит калия, иодид аммония, фосфат
кальция, оксид магния, разбавленная серная кислота. Допустимо использование водных растворов веществ.

Из предложенного перечня веществ выберите вещества, между которыми возможна реакция ионного обмена, приводящая к
выделению газа. Запишите молекулярное, полное и сокращенное ионное уравнения реакции с участием выбранных веществ."

Напиши похожее задание за основу возьми шаблон формулировки
'''
    TASK_3_P2_PROMPT: str = '''
"Медь растворили в разбавленной азотной кислоте. К полученному раствору добавили избыток раствора аммиака, наблюдая
сначала образование осадка, а затем его полное растворение с образованием темно-синего раствора. Полученный раствор
обработали серной кислотой до появления характерной голубой окраски солей меди.

Запишите уравнения описанных реакций."

Напиши похожее задание за основу возьми шаблон формулировки
'''
    TASK_4_P2_PROMPT: str = '''
"Напишите уравнения реакций, с помощью которых можно осуществить следующие превращения:
CH4--(Cl2hv)-->X1-->бензольное кольцо вверху CH3--(HNO3 H2SO4 t)-->X2--(Fe2HCL)-->бензольное кольцо вверху CH3
внизу NH3+CL- --(AgNO3)-->X3

При написании уравнений реакций используйте структурные формулы органических веществ."

Напиши похожее задание за основу возьми шаблон формулировки
'''
    TASK_5_P2_PROMPT: str = '''
"Смесь цис- и транс-изомеров этиленового углеводорода общим объемом 1,568л (н.у.) пропустили через избыток
водного раствора перманганата калия, в результате образовался двухатомный спирт массой 6,30г.
Установите молекулярную формулу углеводорода, изобразите структурную формулу транс-изомера и напишите уравнение его
реакции с подкисленным раствором перманганата калия."

Напиши похожее задание за основу возьми шаблон формулировки
'''


class Prompt:
    ELEMENTS: dict = {
        1: 'Be', 2: 'F', 3: 'Mg', 4: 'Cl', 5: 'O', 6: 'Li', 7: 'N', 8: 'Al', 9: 'S', 10: 'Na'
    }

    @property
    def get_task_1_p1_prompt(self) -> str:
        random_elements = random.sample(list(self.ELEMENTS.values()), k=3)
        data = {
            "element_1": random_elements[0],
            "element_2": random_elements[1],
            "element_3": random_elements[2],
        }
        return PromptText.TASK_1_P1_PROMPT.format(**data)

    @property
    def get_task_2_p1_prompt(self) -> str:
        random_elements = random.sample(list(self.ELEMENTS.values()), k=5)
        data = {
            "element_1": random_elements[0],
            "element_2": random_elements[1],
            "element_3": random_elements[2],
            "element_4": random_elements[3],
            "element_5": random_elements[4],
        }
        return PromptText.TASK_2_P1_PROMPT.format(**data)

    @property
    def get_task_3_p1_prompt(self) -> str:
        random_elements = random.sample(list(self.ELEMENTS.values()), k=5)
        data = {
            "element_1": random_elements[0],
            "element_2": random_elements[1],
            "element_3": random_elements[2],
            "element_4": random_elements[3],
            "element_5": random_elements[4],
        }
        return PromptText.TASK_3_P1_PROMPT.format(**data)

    @property
    def get_task_4_p1_prompt(self) -> str:
        return PromptText.TASK_4_P1_PROMPT

    @property
    def get_task_5_p1_prompt(self) -> str:
        return PromptText.TASK_5_P1_PROMPT

    @property
    def get_task_6_p1_prompt(self) -> str:
        return PromptText.TASK_6_P1_PROMPT

    @property
    def get_task_7_p1_prompt(self) -> str:
        return PromptText.TASK_7_P1_PROMPT

    @property
    def get_task_8_p1_prompt(self) -> str:
        return PromptText.TASK_8_P1_PROMPT

    @property
    def get_task_9_p1_prompt(self) -> str:
        return PromptText.TASK_9_P1_PROMPT

    @property
    def get_task_10_p1_prompt(self) -> str:
        return PromptText.TASK_10_P1_PROMPT

    @property
    def get_task_11_p1_prompt(self) -> str:
        return PromptText.TASK_11_P1_PROMPT

    @property
    def get_task_12_p1_prompt(self) -> str:
        return PromptText.TASK_12_P1_PROMPT

    @property
    def get_task_13_p1_prompt(self) -> str:
        return PromptText.TASK_13_P1_PROMPT

    @property
    def get_task_14_p1_prompt(self) -> str:
        return PromptText.TASK_14_P1_PROMPT

    @property
    def get_task_15_p1_prompt(self) -> str:
        return PromptText.TASK_15_P1_PROMPT

    @property
    def get_task_16_p1_prompt(self) -> str:
        return PromptText.TASK_16_P1_PROMPT

    @property
    def get_task_17_p1_prompt(self) -> str:
        return PromptText.TASK_17_P1_PROMPT

    @property
    def get_task_18_p1_prompt(self) -> str:
        return PromptText.TASK_18_P1_PROMPT

    @property
    def get_task_19_p1_prompt(self) -> str:
        return PromptText.TASK_19_P1_PROMPT

    @property
    def get_task_20_p1_prompt(self) -> str:
        return PromptText.TASK_20_P1_PROMPT

    @property
    def get_task_1_p2_prompt(self) -> str:
        return PromptText.TASK_1_P2_PROMPT

    @property
    def get_task_2_p2_prompt(self) -> str:
        return PromptText.TASK_2_P2_PROMPT

    @property
    def get_task_3_p2_prompt(self) -> str:
        return PromptText.TASK_3_P2_PROMPT

    @property
    def get_task_4_p2_prompt(self) -> str:
        return PromptText.TASK_4_P2_PROMPT

    @property
    def get_task_5_p2_prompt(self) -> str:
        return PromptText.TASK_5_P2_PROMPT
