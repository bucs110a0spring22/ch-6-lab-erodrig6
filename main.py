import turtle 
def seq3np1(n):
    """
        Print the 3n+1 sequence from n, terminating when it reaches 1.
        args: n (int) starting value for 3n+1 sequence
        return: None
    """
    count = 0
    while(n != 1):
       
        if(n % 2) == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
        count += 1
    return count 
          # the last print is 1

def draw_line_graph(upper):
    '''
        Draws a line graph representing the number of iterations
        args: upper bound
        return: none
    '''
    bee = turtle.Turtle()
    bee.color('green')
    writer = turtle.Turtle()
    writer.color('purple')
    win = turtle.Screen()
    win.setworldcoordinates(0, 0, 10, 10)
    max_so_far = 0
    for i in range(1, upper + 1):
        result = seq3np1(i)
        if result > max_so_far:
            max_so_far = result
            win.setworldcoordinates(0, 0, i + 10, max_so_far + 10)
            bee.goto(i, max_so_far)
            writer.clear()
            message = 'Maximum so far:' + ' ' + str(i) + ' ,' + str(result)
            writer.goto(0, max_so_far)
            writer.write(message)

    win.exitonclick()

def main():
    upper = int(input('What is the upper bound of your range? Must be positive '))
    if upper < 0:
        exit()
    for start in range(1, upper + 1):
        print(start,':', seq3np1(start))
    draw_line_graph(upper)
main()
