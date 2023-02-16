'''
Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. 
Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. За один ход можно забрать
не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход.
 Сколько конфет нужно взять первому игроку,
 чтобы забрать все конфеты у своего конкурента?

	a) Добавьте игру против бота
	b) Подумайте как наделить бота ""интеллектом""
'''
from random import randint

# Реализовано два варианта игры - против соперника и против компьютера
# с "интеллектом"


def select_game():
    global player2
    print("Выберите вариант игры: ")
    game_variant = input(
        "\tИграть вдвоём:'1' Играть против компьютера:'2' -> ")
    if game_variant == "2":
        player2 = "Компьютер" 
    draw_lots()
    
def draw_lots():
    global player2
    print("Определим кто первый. Кинем монетку\n")
    coin = randint(0, 1)
    if coin:
        print(f"Первым ходит {player1}")
        player_bot(player1)
    else:
        print(f"Первым ходит {player2}")
        player_bot(player2)


def player_bot(player):
    global total_candies        
    if player == "Компьютер":
        if total_candies % 29 != 0:
            take_candy = total_candies % 29
        else:
            take_candy = randint(1, 28)            
        print(f"\n{player}. Всего {total_candies}. {player} берёт {take_candy} конфет.")            
    else:
        take_candy = int(input(f"\n{player}. Всего {total_candies} конфет. Сколько конфет возьмёте? -> "))
        while take_candy > 28 or take_candy < 1 or take_candy > total_candies:
            take_candy = int(input("Не жульничайте! Сколько возьмёте конфет? -> "))
    total_candies = total_candies - take_candy    
    print(f"Осталось {total_candies} конфет")
    if total_candies <= 0:
        print(f"{player} победил!")
        return
    if player == player1:
        player_bot(player2)
    else:
        player_bot(player1)

total_candies = 160
player1 = "Игрок 1"
player2 = "Игрок 2"

select_game()

