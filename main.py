# class ChessBoard:
#     def init(self):
#         self.size = 8 #размер

#     def valid_position(self, position):
#         return 1 <= position[0] <= 8 and 1 <= position[1] <= 8 #проверка позиц

#     def queen_move(self, start, end): #проверкаа хода фезя
#         if not self.valid_position(start) or not self.valid_position(end):
#             raise ValueError("Одна или две позиции не на доске")
#         elif start == end:
#             return False 

#         same_row = start[0] == end[0]
#         same_column = start[1] == end[1]
#         same_diagonal = abs(start[0] - end[0]) == abs(start[1] - end[1])

#         return same_row or same_column or same_diagonal

#     def horse_move(self, start, end): #проверка хода коня
#         if not self.valid_position(start) or not self.valid_position(end):
#             raise ValueError("Одна или обе позиции находятся вне доски")
#         elif start == end:
#             return False

#         row_diff = abs(start[0] - end[0])
#         col_diff = abs(start[1] - end[1])

#         return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)


# board = ChessBoard()
# try:
#     start_pos = (2, 2)
#     end_pos = (8, 8)
#     print(f"Ферзь может перейти с {start_pos} на {end_pos}: {board.queen_move(start_pos, end_pos)}")
# except ValueError as z:
#     print(f"Ошибка: {z}")


# try:
#     start_pos = (1, 1)
#     end_pos = (2, 3)
#     print(f"Конь может перейти с {start_pos} на {end_pos}: {board.horse_move(start_pos, end_pos)}")
# except ValueError as e:
#     print(f"Ошибка: {e}")







# def plus_two():
#     try:
#         num = 2
#         number = int(input("Введите число: "))
#         return(f"Сумма чисел: {num + number}")
#     except:
#         return("Ожидаемый тип данных — число!")

# a = plus_two()
# print(a)




try:
    list = ['red', 12, ('res', 45, 3), True]
    index = list[int(input("Введите номер индекса: "))]
    print(f"Элемент переменной list: {index}")
except IndexError:
    print("Данный индекс не найден")
except ValueError:
    print("Вы ввели не число!")
print("\nПоиск индекса завершен")