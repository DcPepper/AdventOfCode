data="""noop
addx 5
addx -2
noop
noop
addx 7
addx 15
addx -14
addx 2
addx 7
noop
addx -2
noop
addx 3
addx 4
noop
noop
addx 5
noop
noop
addx 1
addx 2
addx 5
addx -40
noop
addx 5
addx 2
addx 15
noop
addx -10
addx 3
noop
addx 2
addx -15
addx 20
addx -2
addx 2
addx 5
addx 3
addx -2
noop
noop
noop
addx 5
addx 2
addx 5
addx -38
addx 3
noop
addx 2
addx 5
noop
noop
addx -2
addx 5
addx 2
addx -2
noop
addx 7
noop
addx 10
addx -5
noop
noop
noop
addx -15
addx 22
addx 3
noop
noop
addx 2
addx -37
noop
noop
addx 13
addx -10
noop
addx -5
addx 10
addx 5
addx 2
addx -6
addx 11
addx -2
addx 2
addx 5
addx 3
noop
addx 3
addx -2
noop
addx 6
addx -22
addx 23
addx -38
noop
addx 7
noop
addx 5
noop
noop
noop
addx 9
addx -8
addx 2
addx 7
noop
noop
addx 2
addx -4
addx 5
addx 5
addx 2
addx -26
addx 31
noop
addx 3
noop
addx -40
addx 7
noop
noop
noop
noop
addx 2
addx 4
noop
addx -1
addx 5
noop
addx 1
noop
addx 2
addx 5
addx 2
noop
noop
noop
addx 5
addx 1
noop
addx 4
addx 3
noop
addx -24
noop"""

example="""addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

#Goal: https://adventofcode.com/2022/day/10

## Question 1 ##

def update(cycle_start,input,value):
    input = input.split(' ')
    if len(input) == 2:
        return cycle_start+2, value + int(input[1])
    else:
        return cycle_start+1, value


important_values = [20, 60, 100, 140, 180, 220]
important_result = []
curr_value = 1
curr_cycle = 0

def calculate_values (data_input, c_v = curr_value, c_c = curr_cycle):
    lines = data_input.split('\n')
    n = len(lines)
    i=0
    j=0
    
    while c_c < important_values[-1]:
        line = lines[i]
        new_cycle,new_value = update(c_c, line, c_v)
        if new_cycle >= important_values[j]:
            important_result.append(c_v)
            j+=1
        
        c_c, c_v = new_cycle, new_value
        i+=1
    
    return sum([a*b for a,b in zip(important_result, important_values)])

print(calculate_values(data))

## Question 2 ##

def drawing(draw, cycle_start, inputs, position):
    inputs = inputs.split(' ')
    if cycle_start%40 in [position-1, position, position+1]:
        draw+="#"
    else:
        draw+="."
    
    if len(inputs) == 2:
        cycle_start += 1
        if cycle_start%40 in [position-1, position, position+1]:
            draw+="#"
        else:
            draw+="."
        
        position+=int(inputs[1])
    
    return draw, cycle_start+1, position
        

def draw_me_a_word(data_input, c_v = curr_value, c_c=curr_cycle):
    draw=""
    lines = data_input.split('\n')
    n = len(lines)
    i=0
    while c_c<240:
        line = lines[i]
        draw, c_c, c_v = drawing(draw, c_c, line, c_v)
        i+=1
    
    print('\n'.join([draw[40*k:40*(k+1)] for k in range(6)]))

print(draw_me_a_word(data))