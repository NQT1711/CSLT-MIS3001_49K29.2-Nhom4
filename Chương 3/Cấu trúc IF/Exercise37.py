num_sides = int(input('The number of sides: '))
if 2 < num_sides < 11:
    if num_sides == 3:
        print('That shape is triangle')
    elif num_sides == 4:
        print('That shape is quadrilateral')
    elif num_sides == 5:
        print('That shape is pentagon')
    elif num_sides == 6:
        print('That shape is hexagon')
    elif num_sides == 7:
        print('That shape is heptagon')
    elif num_sides == 8:
        print('That shape is octagon')
    elif num_sides == 9:
        print('That shape is nonagon')
    elif num_sides == 10:
        print('That shape is decagon')
else:
    print('the shape cannot be determined')
