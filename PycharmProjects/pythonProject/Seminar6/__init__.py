import time

'''Используется объектно-ориентированная парадигма. Класс содержит методы для  работы секундомера. 
Также создается экземпляр класса Stopwatch 
В цикле пользователь имеет возможность управлять секундомером.
'''

class Stopwatch:  'класс'
    def (self):  'конструктор класса'
        self.start_time = None  ' Время начала работы секундомера'
        self.bool_pause_time = False  ' Переменная, указывающая, находится ли секундомер в режиме паузы'
        self.pause_start_time = None  'Время начала постановки секундомера на паузу'
        self.total_paused_time = 0  ' Общее время на паузах'

    def start(self):  'включает секундомер '
        if not self.start_time:
            self.start_time = time.time()  'Запускаем секундомер'
        elif self.bool_pause_time:  'Если секундомер находится в режиме паузы'
            self.total_paused_time += time.time() - self.pause_start_time  'Учитываем время паузы'
            self.bool_pause_time = False  ' Выходим из режима паузы'

    def pause(self):  'ставим секундомер на паузу'
        if self.start_time and not self.bool_pause_time:  'Если секундомер запущен и не находится в режиме паузы'
            self.bool_pause_time = True  'Входим в режим паузы''
            self.pause_start_time = time.time()  ' Запоминаем время начала паузы'

    def resume(self):  ' возобновляем работу секуномера после паузы'
        if self.bool_pause_time:  'Если секундомер находится в режиме паузы'
            self.bool_pause_time = False  'Выходим из режима паузы'
            self.total_paused_time += time.time() - self.pause_start_time  'Учитываем время паузы'

    def stop(self):  'останавливаем секундомер и сбрасываем все переменные'
        self.start_time = None
        self.bool_pause_time = False
        self.pause_start_time = None
        self.total_paused_time = 0


def get_time(self):  'возвращаем время работы секундомера в секундах'
    if self.start_time:
        if self.bool_pause_time:  'исправленна ошибка'
            return self.pause_start_time - self.start_time - self.total_paused_time
        else:
            return time.time() - self.start_time - self.total_paused_time


def get_time_format(self):  'возвращаем время работы секундомера в формате "минуты:секунды"
    time = int(self.get_time())
    min = time // 60
    sec = time % 60
    return f"{min:02}: {sec:02}"


if __name__ == "__main__":  #
    name = Stopwatch()
    # выводятся доступные опции управления, и пользователь выбирает одну из них.
    while True:
        print("1 - start")
        print("2 - pause")
        print("3 - continue")
        print("4 - stop")
        print("5 - exit")

        choice = input("Choose number: ")
        if choice == "1":
            name.start()
        elif choice == "2":
            name.pause()
        elif choice == "3":
            name.resume()
        elif choice == "4":
            name.stop()
        elif choice == "5":
            print("Exit")
            break
    'После выхода из цикла выводится общее время работы секундомера'
    total = name.get_time_format()
    print("time", total)