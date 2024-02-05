import time
from collections import deque
import os

class PathFinding:
    def __init__(self):
        self.start_time = time.time()
        self.find = False
        self.player = 'P'
        self.wall = "#"
        self.finish = "F"
        self.attempt = "+"
        self.player_color = '\033[92m'
        self.wall_color = '\033[94m'
        self.finish_color = '\033[91m'

        self.player_pos = (9, 1)
        self.finish_pos = (5, 9)
        
        self.visited = []
        self.moves = -1
        self.path = []
        self.queue = deque()

        self.generate_map()

    def generate_map(self):
        self.map = [
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", " ", "#", "#", " ", " ", "#", "#", " ", " ", "#"],
            ["#", " ", "#", " ", " ", " ", " ", "#", " ", " ", "#"],
            ["#", " ", " ", " ", "#", "#", " ", " ", " ", " ", "#"],
            ["#", " ", "#", "#", "#", "#", "#", "#", " ", " ", "#"],
            ["#", " ", "#", "#", " ", "#", " ", " ", " ", " ", "#"],
            ["#", " ", " ", "#", " ", "#", " ", "#", "#", " ", "#"],
            ["#", " ", " ", "#", " ", "#", " ", " ", "#", " ", "#"],
            ["#", " ", " ", "#", "#", "#", "#", " ", "#", " ", "#"],
            ["#", " ", " ", " ", " ", " ", " ", " ", "#", " ", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
        ]

        self.map[self.player_pos[0]][self.player_pos[1]] = self.player
        self.map[self.finish_pos[0]][self.finish_pos[1]] = self.finish
        
        for e in self.queue:
            self.map[e[0][0]][e[0][1]] = self.attempt
        for p in self.path:
            self.map[p[0]][p[1]] = self.player

        if len(self.queue) == 0:
            self.queue.append([self.player_pos, [], 0])


    def draw_map(self):
        for i, row in enumerate(self.map):
            for j, value in enumerate(row):
                prefix = ""
                sufix = '\033[0m'
                if value == self.player:
                    prefix = self.player_color
                    self.player_pos = (i, j)
                elif value == self.wall:
                    prefix = self.wall_color
                elif value == self.finish:
                    prefix = self.finish_color
                elif value == self.attempt:
                    prefix = self.player_color
                print(prefix + value + sufix, end=" ")
            print()
        print()

    
    def find_neighbors(self):
        self.neighbors = []
        for el in self.queue:
            x, y = el[0]
            path = el[1]
            moves = el[2]
            
            if self.map[x + 1][y] != "#":
                pos = (x + 1, y)
                self.check_neighbor(pos, path, moves)
            if self.map[x - 1][y] != "#":
                pos = (x - 1, y)
                self.check_neighbor(pos, path, moves)
            if self.map[x][y + 1] != "#":
                pos = (x, y + 1)
                self.check_neighbor(pos, path, moves)
            if self.map[x][y - 1] != "#":
                pos = (x, y - 1)
                self.check_neighbor(pos, path, moves)
        for neighbor in self.neighbors:
            self.queue.append(neighbor)
        self.queue.popleft()
        

    def check_neighbor(self, pos, path, moves):
        if self.map[pos[0]][pos[1]] == self.finish:
            self.find = True
            self.path = path
            self.moves = moves + 1
            self.queue.clear
            return
        if pos not in self.visited:
            new_path = path + [pos]
            self.neighbors.append((pos, new_path, moves + 1))
            self.visited.append(pos)


def main():
    path_finding = PathFinding()
    
    while not path_finding.find:
        path_finding.draw_map()
        path_finding.find_neighbors()
        path_finding.generate_map()
    path_finding.draw_map()
    print(f"Reached final goal within {path_finding.moves} steps and {round((time.time() - path_finding.start_time) * 1000, 2)}ms")

if __name__ == "__main__":
    main()
