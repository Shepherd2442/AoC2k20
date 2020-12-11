from utils import FileUtils
import math

def get_inner_interval(interval, lower=True):
    minimum, maximum = interval
    new_bound = math.floor(abs(maximum - minimum) / 2)
    if lower:
        maximum = new_bound + minimum
    else:
        minimum = new_bound + minimum + 1
    return (minimum, maximum)

def get_seat(boarding_pass, rows=(0, 127), columns=(0, 7)):
    switcher = {
        "F": (get_inner_interval(rows), columns),
        "B": (get_inner_interval(rows, lower=False), columns),
        "L": (rows, get_inner_interval(columns)),
        "R": (rows, get_inner_interval(columns, lower=False)),
    }
    if len(boarding_pass) > 0:
        arguments = switcher.get(boarding_pass[0])
        return get_seat(boarding_pass[1:], *arguments)
    # At this point lower and upper is the same
    return (rows[0], columns[0])

def get_seat_id(seat):
    return seat[0] * 8 + seat[1]

def get_my_seat_id(seat_list):
    missing_seats = []
    for row in range(128):
        for column in range(8):
            if (row, column) not in seat_list:
                missing_seats.append((row, column))
    seat_list_ids = [get_seat_id(seat) for seat in seat_list]
    for seat in missing_seats:
        seat_id = get_seat_id(seat)
        if seat_id + 1 in seat_list_ids and seat_id - 1 in seat_list_ids:
            return seat_id

if __name__ == "__main__":
    seats = [get_seat(boarding_pass) for boarding_pass in FileUtils.input()]
    print("Part_1:", max([get_seat_id(seat) for seat in seats]) )
    print("Part_2:", get_my_seat_id(seats))