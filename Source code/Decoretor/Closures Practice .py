


                    # Function returning Function closures / first class function practice

def to_power(x):
    def cal_power(n):
        return n**x
    return cal_power
  # with this function you can do two thing one square and two is cube

square = to_power(2)
print(square(5))        # --> returning square

cube = to_power(3)      # ---> returning Cube
print(cube(10))
