def divisible_by_five_and_seven(x, y):
    return [i for i in range(x, y+1) if i % 5 == 0 and i % 7 != 0]


def base_converter(x, b):
    return bin(x)[2:] if b == 2 else oct(x)[2:] if b == 8 else hex(x)[2:] if b == 16 else str(x)


def perfect_squares(n):
    for i in range(1, n):
        if i ** 2 < n:
            yield i ** 2
            
            
def find_phrase(phrase, file):
    with open(file, 'r') as f:
        for line in f:
            if phrase in line:
                return True
    return False


def sum_column(file, column):
    with open(file, 'r') as f:
        for line in f:
            line = line.split(',')
            yield int(line[column])
