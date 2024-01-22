import argparse
from trainingstimer_core import grumfundler


import time
import sys
import os

# Exercise data
exercises = [
    {"Activity": "Stretching", "Time": 10, "A": "Gentle Full Body Stretch", "B": "Yoga Poses"},
    {"Activity": "Bodyweight Circuit Training", "Time": 20, "A": "Push-Ups", "B": "Squats", "C": "Lunges", "D": "Planks"},
    {"Activity": "Stair Climbing", "Time": 15, "A": "Basic Step Up", "B": "Side Step Up", "C": "Step Up with Knee Lift"},
    {"Activity": "Jump Rope (Imaginary)", "Time": 15, "A": "Basic Jump", "B": "High Knees", "C": "Double Under (Imaginary)"},
    {"Activity": "Meditation and Breathing", "Time": 10, "A": "Guided Deep Breathing", "B": "Mindfulness Meditation"}
]

def beep():
    # System beep. Replace with a sound file if needed.
    print("\a") 

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1

def run_exercises(exercises):
    for exercise in exercises:
        total_time = exercise["Time"] * 60  # Convert minutes to seconds
        segments = total_time // 300  # Number of 5-minute segments

        print(f"\n{exercise['Activity']}")
        for i in range(1, segments + 1):
            segment_time = 300  # 5 minutes in seconds
            element = exercise.get(chr(64 + i), "Rest")  # Get the exercise element (A, B, C, D) or Rest
            print(f"{element} - Segment {i}")
            countdown(segment_time)
            beep()  # Sound at the end of each segment

        remaining_time = total_time % 300
        if remaining_time > 0:
            print("Final Stretch")
            countdown(remaining_time)
            beep()

def main():
    parser = argparse.ArgumentParser(description='Grumfundler')
    parser.add_argument('-g', '--grumfundler', default="Hello World!", help='Grumfundler')
    parser.add_argument('-d', '--dockertest', action='store_true', help='Run in Docker')
    args = parser.parse_args()

    if args.dockertest:
        print('Running in Docker')
        print(f'cwd: {os.getcwd()}')
        print(f'args: {args}')
        print(f'env: {os.environ}')
        return

    if args.grumfundler is not None or args.grumfundler != '':
        gf = grumfundler.Grumfundler(args.grumfundler)
        print(f'x: {gf}')
        return

    run_exercises(exercises)

if __name__ == "__main__":
    main()