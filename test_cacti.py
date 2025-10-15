from cacti import cacti_number 

@cacti_number 
def plat1():
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
  print(plot1())
  print(plot2())

if __name__ == "__main__":
  main()
