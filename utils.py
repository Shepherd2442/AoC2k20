import sys

class FileUtils:
    @staticmethod
    def input():
        with open(sys.argv[1], 'r') as file:
            lines = [int(line.rstrip()) for line in file]
        return lines