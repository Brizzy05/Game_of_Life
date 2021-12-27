import turtle
import game_of_life as gm
import time

n = 20
size = 32
COLOR = (5,4,41)

class Grid():
    def __init__(self, x=0, y=0, idx=0, color=0, val=0):
        # contains grid object
        self.pos_x = x
        self.pos_y = y
        self.index = idx
        self.color = color
        self.value = val
        if color != 0:
            self.draw()
        
    
    def __str__(self):
        return f'x:{self.pos_x}, y:{self.pos_y}, index:{self.index}, color:{self.color}, value:{self.value}'
    
    def change_val(self, gr):
        if gr.value == 0:
            gr.value = 1
        else:
            gr.value = 0
        
            
    
    def draw(self):
        if self.value == 1:
            self.color = 'white'
        else:
            self.color = COLOR
        
        bob.penup()
        
        bob.goto(self.pos_x, self.pos_y)
        
        bob.fillcolor(self.color)
        bob.begin_fill()
        bob.pendown()
        
        for i in range(4):
            bob.forward(size)
            bob.right(90)
            
        bob.end_fill()
        bob.penup()
    
    
    @staticmethod
    def draw_life(next_gen, grid_lst):
        
        for i in range(len(grid_lst)):
            for j in range(len(grid_lst)):
                grid = grid_lst[i][j]
                cell_type = next_gen[i][j]
                
                grid.value = cell_type
                grid.draw()
        
        
        
            
        
                
        
        

turtle.setup(700,700)

bob = turtle.Turtle(visible=False)
bob.color('white')
bob.penup()
bob.goto(-320, 320)
bob.write("Press 'Enter' to generate life and 'Space' to reset", align= 'left', font=('Courier', 15, 'bold'))
bob.width(2)
bob.pencolor('grey')
bob.speed(0)

wn = turtle.Screen()
wn.title('Game of Life')

turtle.colormode(255)
wn.bgcolor(COLOR)

wn.tracer(0)
bob.pendown()


      
def create_obj():
    grid_lst = []
    x = -320
    y = 320
    for i in range(n):
        grid_lst.append([])
        for j in range(n):
            grid = Grid(x, y, (j,i), COLOR, 0)
            grid_lst[i].append(grid)
            
            if x < 320 - size:
                x += size
            else:
                x = -320
        y -= size
    return grid_lst


def gen_lst(grid_lst):
        
        val_lst = []
        
        for i in range(len(grid_lst)):
            val_lst.append([])
            for j in range(len(grid_lst)):
                val_lst[i].append(grid_lst[i][j].value)
                  
        return val_lst
    

def click_listner(x, y):
    indx_x = int((x + 320) // 32)
    indx_y = int((-y + 320) // 32)
    
    for i in range(len(grid_objs)):
        for j in range(len(grid_objs)):
            grid = grid_objs[i][j]
            if (indx_x, indx_y) == grid.index:
                grid.change_val(grid)
                grid.draw()
    
def reset():
    global game_on
    game_on = False
    for lst in grid_objs:
        for grid in lst:
            grid.value = 0
            grid.draw()


def gen_life():
    lst_life = gen_lst(grid_objs)
    next_gen = gm.get_next_gen_universe(lst_life)
    Grid.draw_life(next_gen, grid_objs)
    wn.update()
    time.sleep(0.5)
    
def start_life():
    global game_on
    game_on = True
    while game_on:
        gen_life()

grid_objs = create_obj()



turtle.listen()
wn.update()
game_on = False


turtle.onscreenclick(click_listner, 1)
turtle.onkey(start_life, 'Return')
turtle.onkey(reset, 'space')



wn.mainloop()