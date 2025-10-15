from cacti import cacti_number

@cacti_number
def plot1():
    return [
        [1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0]
    ]

@cacti_number
def plot2():
    return [
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [1, 0, 1, 0, 0, 1]
    ]

def main():
    print(plot1())  # expected: 4
    print(plot2())  # expected: 1

if __name__ == "__main__":
    main()
