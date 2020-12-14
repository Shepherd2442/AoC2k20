from utils import FileUtils
import numpy as np

class Ferry:
    def __init__(self, seat_layout):
        self.layout = seat_layout
        self.shape = ({'x': len(seat_layout[0]), 'y': len(seat_layout)})
    
    def get_num_of_occupied(self):
        return "".join(self.layout).count("#")

    def get_adjacent_seats(self, x, y):
        adjacent_seats = []
        directions = [{'x': -1, 'y':  1},{'x':  0, 'y':  1},{'x':  1, 'y':  1},
                      {'x':  1, 'y':  0},                   {'x':  1, 'y': -1},
                      {'x':  0, 'y': -1},{'x': -1, 'y': -1},{'x': -1, 'y':  0}]
        valid_dirs = list(filter(lambda dir: (0 <= x + dir['x'] < self.shape['x']) &
                                             (0 <= y + dir['y'] < self.shape['y']), directions))
        adjacent_seats = [self.layout[y + v_dir['y']][x + v_dir['x']] for v_dir in valid_dirs]
        # Any seat - comment out for part 1
        if (self.layout[y][x] in ["#", "L"]):
            for idx, seat in enumerate(adjacent_seats):
                if seat == '.':
                    adjacent_seats[idx] = self.get_seat_in_direction(x, y, direction=valid_dirs[idx])
        return adjacent_seats

    def get_seat_in_direction(self, x, y, direction):
        new_x, new_y = x + direction['x'], y + direction['y']
        if new_x < 0 or new_x >= self.shape['x'] or new_y < 0 or new_y >= self.shape['y']:
            return '.'
        seat_canditate = self.layout[new_y][new_x]
        while seat_canditate not in ["#", "L"]:
            return self.get_seat_in_direction(new_x, new_y, direction)
        return seat_canditate

    def run_iteration(self, n_times=1, max_occupied=4):
        for _ in range(n_times):
            new_layout = self.layout[:] # Deep copy
            for ix, iy in np.ndindex(self.shape['x'], self.shape['y']):
                seat = self.layout[iy][ix]
                if (seat == 'L') & ('#' not in self.get_adjacent_seats(ix, iy)):
                    new_layout[iy] =  new_layout[iy][:ix] + '#' + new_layout[iy][ix + 1:]
                elif (seat == '#') & (self.get_adjacent_seats(ix, iy).count('#') >= max_occupied):
                    new_layout[iy] =  new_layout[iy][:ix] + 'L' + new_layout[iy][ix + 1:]
            self.layout = new_layout
        return self.layout

    def stabilize_layout(self, max_occupied=4):
        layouts = [None, self.layout]
        while layouts[-1] != layouts[-2]:
            layouts.append(self.run_iteration(max_occupied=max_occupied))

    def __str__(self):
        return '\n'.join(self.layout)

if __name__ == "__main__":
    ferry = Ferry(FileUtils.input())
    ferry.stabilize_layout(max_occupied=5)
    print(ferry.get_num_of_occupied())
    print(ferry)