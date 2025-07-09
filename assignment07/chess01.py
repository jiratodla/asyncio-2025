import time
from datetime import timedelta

speed = 10 # speed 
judit_time = 5/speed # time for Judit to make a move
opponent_time = 55/speed # time for the opponent to make a move
opponents = 24
move_pairs = 30

def game(x):
    # Simulate a chess game with Judit
    board_start_time = time.perf_counter()
    calcu_board = 0
    for i in range(move_pairs):
        time.sleep(judit_time)
        calcu_board = calcu_board + judit_time
        print(f"BOARD-{x+1} {i+1} Judit move with {int(judit_time*speed)} secs.")
        # Simulate opponent's move
        time.sleep(opponent_time)
        print(f"BOARD-{x+1} {i+1} Opponent move with {int(opponent_time*speed)} secs.")
        calcu_board = calcu_board + opponent_time
    print(f"BOARD-{x+1} ->>>>>>>>>>>>>>>> Finished move in {time.perf_counter() - board_start_time:.1f} secs.")
    print(f"BOARD-{x+1} ->>>>>>>>>>>>>>>> Total time: {calcu_board*speed:.1f} secs.(calculated)\n")
    return{
        'board_time': (time.perf_counter() - board_start_time)*speed,
        'calculated_time': calcu_board*speed
    }

if __name__ == '__main__':
    print(f"Number of game: {opponents} games.")
    print(f"Number of move: {move_pairs} pairs.")
    start_time = time.perf_counter()
    # Simulate multiple chess games
    board_times = 0
    calculated_board_times = 0
    for board in range(opponents):
        result = game(board)
        board_times += result['board_time']
        calculated_board_times += result['calculated_board_time']

    print(f"Board exhibition finished for {opponents} opponents in {timedelta(seconds=round(board_times))} hrs.")
    print(f"Board exhibition finished for {opponents} opponents in {timedelta(seconds=round(calculated_board_times))} hrs. (calculated)")
    print(f"finished in {round(time.perf_counter() - start_time)} secs.")

    