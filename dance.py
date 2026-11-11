import time
import os

frames = [
r"""
          O
         \|/
          |
         / \
        
       💃 DANCING 💃
""",

r"""
          O
         \| 
          |\
         /  \
        
       💃 DANCING 💃
""",

r"""
          O
         /|\
          |
         / \
        
       🕺 DANCING 🕺
""",

r"""
          O
          |\
         /|
        /  \
        
       🕺 DANCING 🕺
"""
]

while True:
    for frame in frames:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n" * 2)
        print(frame)
        time.sleep(0.25)

