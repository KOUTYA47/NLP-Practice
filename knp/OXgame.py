import math
import random
import numpy as np
from time import sleep
import matplotlib.pyplot as plt
from IPython.display import clear_output

# プレイヤの入力を受け付ける関数
def get_player_input(play_area, player_turn):
    choosable_area = [str(area) for area in play_area if type(area) is int]

    # 入力待ち
    while(True):
        player_input = input('Choose a number >')
        if player_input in choosable_area:
            player_input = int(player_input)
            break
        else:
            print('Wrong input!\nChoose a number from {}'.format(choosable_area))
    
    # player_turn=1: 先手，player_turn=2: 後手
    if player_turn == 1:
        play_area[play_area.index(player_input)] = '○'
    elif player_turn == 2:
        play_area[play_area.index(player_input)] = '×'
    
    return play_area, player_input

# ゲーム画面を表示する関数
def show_play(play_area):
    clear_output()
    plt.figure(figsize=(6, 6))
    plt.plot()
    plt.xticks([0, 5, 10, 15])
    plt.yticks([0, 5, 10, 15])
    plt.tick_params(labelbottom='off', bottom='off')
    plt.tick_params(labelleft='off', left='off')
    plt.xlim(0, 15)
    plt.ylim(0, 15)

    x_pos = [2.5, 7.5, 12.5]
    y_pos = [2.5, 7.5, 12.5]

    markers = ['$' + str(marker) + '$' for marker in play_area]

    marker_count = 0
    for y in reversed(y_pos):
        for x in x_pos:
            if markers[marker_count] == '$○$':
                color = 'r'
            elif markers[marker_count] == '$×$':
                color = 'k'
            else:
                color = 'b'
            plt.plot(x, y, marker=markers[marker_count], 
                     markersize=30, color=color)
            marker_count += 1
    plt.show()

# ゲーム終了と勝敗を判定する関数
def judge(play_area, inputter):
    end_flg = 0
    winner = 'Nobody'
    first_list = [0, 3, 6, 0, 1, 2, 0, 2]
    second_list = [1, 4, 7, 3, 4, 5, 4, 4]
    third_list = [2, 5, 8, 6, 7, 8, 8, 6]
    for first, second, third in zip(first_list, second_list, third_list):
        if play_area[first] == play_area[second] and play_area[first] == play_area[third]:
            winner = inputter
            end_flg = 1
            break
    choosable_area = [str(area) for area in play_area if type(area) is int]
    if len(choosable_area) == 0:
        end_flg = 1
    return winner, end_flg

# プレイヤとランダムAIのゲームを実行する関数
def player_vs_randomAI(first_inputter):
    inputter1 = 'YOU'
    inputter2 = 'AI'

    play_area = list(range(1, 10))
    show_play(play_area)
    inputter_count = first_inputter
    end_flg = 0
    while True:
        if (inputter_count % 2) == 1:
            print('Your turn!')
            play_area, player_input = get_player_input(play_area, first_inputter)
            show_play(play_area)
            winner, end_flg = judge(play_area, inputter1)
            if end_flg:
                break
        elif (inputter_count % 2) == 0:
            print('AI\'s turn!')
            play_area, ai_input = get_ai_input(play_area, first_inputter, mode=0)
            show_play(play_area)
            winner, end_flg = judge(play_area, inputter2)
            if end_flg:
                break
        inputter_count += 1
    print('{} win!!!'.format(winner))

player_vs_randomAI(1) # 1: プレイヤ先手，2: プレイヤ後手

