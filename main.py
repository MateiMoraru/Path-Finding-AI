import curses
from curses import wrapper

class PathFinding:
    def __init__(self):
        self.generate_map()
        self.player = 'P'
        self.wall = "#"
        self.finish = "F"
        self.player_color = '\033[92m'
        self.wall_color = '\033[94m'
        self.finish_color = '\033[91m'

    def generate_map(self):
        self.map = [
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", " ", "#", "#", " ", " ", "F", " ", " ", " ", "#"],
            ["#", " ", "#", " ", " ", " ", " ", " ", " ", " ", "#"],
            ["#", " ", " ", " ", "#", "#", " ", " ", " ", " ", "#"],
            ["#", " ", "#", "#", "#", "#", "#", "#", " ", " ", "#"],
            ["#", " ", "#", "#", " ", "#", " ", " ", " ", " ", "#"],
            ["#", " ", " ", "#", " ", "#", " ", " ", " ", " ", "#"],
            ["#", " ", " ", "#", " ", "#", " ", " ", " ", " ", "#"],
            ["#", " ", " ", "#", "#", "#", "#", " ", "#", " ", "#"],
            ["#", "P", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
        ]


    def draw_map(self):
        for i, row in enumerate(self.map):
            for j, value in enumerate(row):
                prefix = ""
                sufix = '\033[0m'
                if value == self.player:
                    prefix = self.player_color
                elif value == self.wall:
                    prefix = self.wall_color
                elif value == self.finish:
                    prefix = self.finish_color
                print(prefix + value + sufix, end=" ")
            print()


def main():
    path_finding = PathFinding()
    
    path_finding.draw_map()

if __name__ == "__main__":
    main()
