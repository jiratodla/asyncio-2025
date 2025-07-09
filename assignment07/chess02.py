import time
from datetime import timedelta
import asyncio


speed = 100 # speed 
judit_time = 5/speed # time for Judit to make a move
opponent_time = 55/speed # time for the opponent to make a move
opponents = 24
move_pairs = 30

async def async_game(x):
        board_start_time = time.perf_counter()
        
        for i in range(move_pairs):
            time.sleep(judit_time)
            print(f"BOARD-{x+1} {i+1} Judit move with {int(judit_time*speed)} secs.")
            await asyncio.sleep(opponent_time)
            print(f"BOARD-{x+1} {i+1} Opponent move with {int(opponent_time*speed)} secs.")
        print(f"BOARD-{x+1} ->>>>>>>>>>>>>>>> Finished move in {(time.perf_counter() - board_start_time)*speed:.1f} secs.\n")
        return {
            'calculated_board_time': (time.perf_counter() - board_start_time )*speed
        }

async def main():
        tasks = []
        for i in range(opponents):
            tasks +=[async_game(i)]
        await asyncio.gather(*tasks)
        print(f" Board exhibition finished for {opponents} opponents in {timedelta(seconds=speed*round(time.perf_counter()-start_time))} hrs.")

if __name__ == "__main__":
    print(f"Number of game: {opponents} games.")
    print(f"Number of move: {move_pairs} pairs.")
    start_time = time.perf_counter()
    asyncio.run(main())
    print(f"finished in {round(time.perf_counter() - start_time)} secs.")