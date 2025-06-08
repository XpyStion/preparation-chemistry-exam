from enum import Enum

CHOICES = list[tuple[str, str]]


def wrap_db_choice(choices_sequence: tuple | list) -> CHOICES:
    return [(choice, choice.capitalize()) for choice in choices_sequence]


class StringEnum(str, Enum):

    def __str__(self) -> str:
        """Магический метод возвращения строкового представления.

        Returns:
            Строковое представление.
        """
        return str.__str__(self)

    def __iter__(self):
        """Магический метод возвращения итерационного представления.

        Returns:
            Итерационное представление.
        """
        return iter((value.value for value in self))
