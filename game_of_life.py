# Student ID: 260968896
# Brisnel Etou Bosseba

def is_valid_universe(universe_list):
    """ (list) -> bool
    Given a a 2D list (reprsenting a universe) the function checks if all the lists
    inside are of the same length, not empty and composed of 0s,1s.
    >>> a = [[1],[2],[3]]
    >>> is_valid_universe(a)
    False
    >>> list_2d = [[0,1,1],[0,1,1],[1,1,1]]
    >>> is_valid_universe(list_2d)
    True
    >>> bee = [[1,2,3],[0,2,1],[0,1,1]]
    >>> is_valid_universe(bee)
    False
    """
    valid_universe = False

    # set to the length of first list
    size_world = len(universe_list[0])
    
    for world_lists in universe_list:
        # check if 1D lists are lists and not empty
        if type(world_lists) == list and world_lists != []:
            # checks if all the list are all the same length
            if len(world_lists) == size_world:
                for values in world_lists:
                   # check if the values are composed of 0,1
                    if values in (0,1):
                        valid_universe = True
                    else:
                        return False
            else:
                return False
        else:
             return False
            
    return valid_universe
    
def universe_to_str(valid_uni):
    """ (list) -> str
    Given a valid representation of a universe the function returns
    the string reprsentation of it using stars for 1s and spaces for 0s
    
    >>> block =  [[0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0], \
                 [0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0]]
    >>> str_block = universe_to_str(block)
    >>> print(str_block)
    +------+
    |      |
    |   ** |
    | ***  |
    |      |
    +------+
    >>> block =  [[0, 0, 1, 0, 0], [1, 0, 0, 1, 1], \
                 [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]]
    >>> str_block = universe_to_str(block)
    >>> print(str_block)
    +-----+
    |  *  |
    |*  **|
    | *** |
    |     |
    +-----+
    >>> block =  [[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], \
                 [0, 1, 0, 1, 0], [0, 0, 1, 0, 0]]
    >>> str_block = universe_to_str(block)
    >>> print(str_block)
    +-----+
    |  *  |
    | * * |
    | * * |
    |  *  |
    +-----+
    """
    rgt_bar = '|'
    lft_bar = '|\n'
    
    #sets the number of dashes to the length of the inside
    #lists the 2D list
    first_line = '+' + '-' * len(valid_uni[0]) + '+\n'
    last_line = '+' + '-' * len(valid_uni[0]) + '+'
    string_rep = ''+first_line 
    
    
    for worlds in valid_uni:
        # loops through the each worlds and finds the index of all cells
        for i in range(len(worlds)):
            # checks if the cell is alive or not
            if worlds[i] == 0:
                living_cell = ' '
            # if it's make it a star
            else:
                living_cell = '*'
            
            # checks if we are at index 0
            if i == 0:
                string_rep += rgt_bar + living_cell
            #checks if we are at the last index
            elif i == len(worlds) -1:
                string_rep += living_cell + lft_bar
    
            else:
                 string_rep += living_cell
    
    return string_rep + last_line



def count_live_neighbors(universe, pos_x, pos_y):
    """ (list, int, int) -> num
    Given a valid universe and a position x and y which represent the location of
    a specific cell, the function will return the number of live neighbours.
    >>> universe_1 =  [[0, 0, 0, 0, 0, 0], \
                      [0, 0, 1, 1, 1, 0], \
                      [0, 1, 1, 1, 0, 0], \
                      [0, 0, 0, 0, 0, 0]]
    >>> count_live_neighbors(universe_1, 1, 3)
    4
    >>> universe =  [[0, 1, 0, 0, 0, 0], \
                    [0, 0, 1, 1, 1, 0], \
                    [0, 1, 1, 0, 0, 0], \
                    [0, 1, 0, 0, 0, 0]]
    >>> count_live_neighbors(universe, 0, 1)
    1
    >>> b =  [[0, 1, 0, 0, 1, 1], \
             [0, 0, 1, 1, 1, 1], \
             [0, 1, 1, 1, 1, 1], \
             [0, 1, 0, 1, 1, 1]]
    >>> count_live_neighbors(b, 2, 4)
    8
    """
    
    count_living_cells = 0
    
    for worlds in range(len(universe)):
        for location in range(len(universe[worlds])):
            # checks if at this location do we have a living cell
            if universe[worlds][location] == 1:
                # checks if we are in the world of the specified cell
                if worlds == pos_x:
                # checks if the location is one greater or less than specified cell
                        if location == pos_y + 1 or location == pos_y - 1 :
                            count_living_cells += 1
                            
                # checks if we are one world above or below the specified cell's world
                elif worlds == pos_x + 1 or worlds == pos_x -1 :
                        if location == pos_y:
                            count_living_cells += 1
                            
                        elif location == pos_y - 1 or location == pos_y + 1:
                            count_living_cells += 1
                        
    return count_living_cells
        

def get_next_gen_cell(universe, pos_x, pos_y):
    """ (list, in,int) -> num
    Given a universe and specific position of a cell,
    the function will determine if the cell will die or be alive
    on the next generation depending on the number of neighbours
    
    >>> uni = [[0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0], \
               [0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0]]
    >>> get_next_gen_cell(uni, 1, 2)
    1
    >>> uni = [[0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0], \
                [0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0]]
    >>> get_next_gen_cell(uni, 1, 3)
    0
    >>> a = [[0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0], \
            [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1]]
    >>> get_next_gen_cell(a, 0, 3)
    1
    """
    # gives us the type of the specified cell
    type_of_cell = universe[pos_x][pos_y]
    num_neighbours = count_live_neighbors(universe, pos_x, pos_y)
    
    # checks if we a living or dead cell
    if type_of_cell == 1:
        # checks if number of neighbours equal to 2,3
        if num_neighbours in (2,3):
            return 1
        else:
            return 0
    else:
        # checks if dead cell has 3 living neighbours
        if num_neighbours == 3:
            return 1
        else:
            return 0
        
def get_next_gen_universe(valid_universe):
    """ (list) -> list
    Given a valid universe (2D list) the function will return the
    next generation universe by replacing each current cells by their
    next generation cells.
    
    >>> uni = [[0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0], \
               [0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0]]
    >>> get_next_gen_universe(uni)
    [[0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0]]
    >>> uni = [[0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0], \
               [0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0], \
               [0, 0, 1, 0, 1, 0]]
    >>> next_gen = get_next_gen_universe(uni)
    >>> ans = [[0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 0, 0],\
    [0, 0, 0, 0, 0, 0]]
    >>> next_gen == ans
    True
    >>> a = [[0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 1, 0], \
            [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1]]
    >>> get_next_gen_universe(a)
    [[0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 1], [0, 1, 1, 0, 0, 1], [0, 0, 1, 1, 0, 1]]
    """
    next_gen_uni = []
    # make deep copy
    for lists in valid_universe:
        next_gen_uni += [lists[:]]
            
    for pos_x in range(len(valid_universe)):
        for pos_y in range(len(valid_universe[pos_x])):
            # at current location replace cell by next gen cell
            next_gen_uni[pos_x][pos_y] = get_next_gen_cell(valid_universe,pos_x, pos_y)
            
    return next_gen_uni


def get_n_generations(universe, num_gen):
    """ (list, int) -> list
    Given a valid universe (2D list) and an integer representing the number of
    generations to create, the function will return a list composed of string
    representation of the all the generations before it starts repeating.

    >>> a = get_n_generations([[1,1,0],[1,0,1]],5)
    >>> print(a[0])
    +---+
    |** |
    |* *|
    +---+
    >>> a = [[0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 1, 0], \
            [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1]]
    >>> g = get_n_generations(a, 5)
    >>> len(g)
    5
    >>> print(g[2])
    +------+
    |      |
    | *****|
    |     *|
    | **** |
    +------+
    >>> a = [[0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 1, 0], \
            [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1]]
    >>> g = get_n_generations(a, 5)
    >>> len(g)
    5
    >>> print(g[4])
    +------+
    |  *  *|
    |  *  *|
    |     *|
    |   ** |
    +------+
    >>> get_n_generations([[1,1,0],[1,0,1]],0)
    Traceback (most recent call last):
    ValueError: Please provide a number greater than 0
    >>> get_n_generations([[1,1,0],[1,0,1]],0)
    Traceback (most recent call last):
    ValueError: The universe provided is not valid
    >>> get_n_generations([[1,1,0],[1,0,1]],0)
    Traceback (most recent call last):
    TypeError: Please provide a list and an integer
    """
    total_gen_list = []
    string_rep = universe_to_str(universe)
    current_gen = universe
    
    if type(universe) == list and type(num_gen) == int:
        # checks for valid universe
        if is_valid_universe(universe):
            if num_gen > 0:
                while len(total_gen_list) < num_gen:
                    # checks if we do not have a repetition
                    if string_rep not in total_gen_list:
                        total_gen_list.append(string_rep)
                        # get new generation
                        new_gen = get_next_gen_universe(current_gen)
                        # get the string representation of new generation
                        string_rep = universe_to_str(new_gen)
                    
                        current_gen = new_gen
                    else:
                        break
            else:
                raise ValueError('Please provide a number greater than 0')
        else:
            raise ValueError('The universe provided is not valid')
    else:
        raise TypeError('Please Provide a list and an integer')

    return total_gen_list


        
        
        
        
