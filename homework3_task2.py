from time import sleep
from functools import wraps
from typing import Any


def repeater(call_count: int, start_sleep_time: int, factor: int, border_sleep_time: int):
    def repeater_decorator(function):
        @wraps(function)
        def wrapper(*args: Any) -> None:
            t: int = start_sleep_time

            print(f"Количество запусков: {call_count}")
            print(f"Начало работы.")

            for i in range(1, call_count + 1):
                test_t: int = start_sleep_time * (factor ** i)

                if test_t < border_sleep_time and i != 1:
                    t = test_t
                elif test_t >= border_sleep_time:
                    t = border_sleep_time

                sleep(t)
                func_result: int = function(*args)

                print(f"Запуск номер {i}. Ожидание: {t} sec.", end=" ")
                print(f"Результат декорируемой функции = {func_result}")

            print("Конец работы.")
        return wrapper
    return repeater_decorator


@repeater(5, 1, 2, 16)
def func(number: int) -> int:
    return number + 1


if __name__ == "__main__":
    func(1)
