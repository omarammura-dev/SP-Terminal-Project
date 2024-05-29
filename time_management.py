"""
Ömer Ammura - 234210074
Emad CheikhElichreh - 224210087
Mohammad nikpour -  234210005
Eldar Semnov - 224210122
"""

import random

class TimeManagement:
    def __init__(self):
        self.time = None
    def generate_random_clock(self):
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        self.time_of_day = f"{hour:02d}:{minute:02d}"
        return self.time_of_day