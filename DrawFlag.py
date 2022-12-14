'''
Function Name: draw_USA_flag
Function description: the purpose of this function is to use turtle to draw the USA flag and Olypmic Rings on a screen.
This function intergates codes from the sample_files and combines draw_square(), draw_six_stars_rows(),
draw_five_stars_rows(), and draw_stripes() into a big function.
@param: none
@return: none    
'''
import turtle
import time
import print_me_first
def draw_USA_flag():
    # create a screen
    screen = turtle.getscreen()
    # set background color of screen
    screen.bgcolor("white")
    # set tile of screen

    screen.title("CNET-142-01 USA Flag")
    turtle.bgpic('usa.png')

    mypen = turtle.Turtle()
    mypen.speed(1000000)
    # set the cursor/turtle speed. Higher value, faster is the turtle
    mypen.penup()
    # decide the shape of cursor/turtle
    mypen.shape("turtle")

    # flag height to width ratio is 1:1.9
    flag_height = 250
    flag_width = 475

    # starting points
    # start from the first quardant, half of flag width and half of flag height
    start_x = -237
    start_y = 125

    # For red and white stripes (total 13 stripes in flag), each strip width will be flag_height/13 = 19.2 approx
    stripe_height = flag_height/13
    stripe_width = flag_width

    # length of one arm of star
    star_size = 10

    #starting point of stripes
    flag_x = start_x
    flag_y = start_y

 #it will draw 12 strips in red and white. 
    for stripe in range(0,6):
        for color in ['red','white']:
            mypen.goto(flag_x,flag_y) 
            mypen.pendown()
            mypen.color(color)
            mypen.begin_fill()
            mypen.forward(stripe_width) 
            mypen.right(90)
            mypen.forward(stripe_height)
            mypen.right(90)
            mypen.forward(stripe_width)
            mypen.right(90)
            mypen.forward(stripe_height)
            mypen.right(90)
            mypen.end_fill()
            mypen.penup()
            flag_y = flag_y - stripe_height
            
    # create last red stripe  
    mypen.goto(flag_x,flag_y)
    mypen.pendown()
    mypen.color('red')
    mypen.begin_fill()
    mypen.forward(stripe_width)
    mypen.right(90)
    mypen.forward(stripe_height)
    mypen.right(90)
    mypen.forward(stripe_width)
    mypen.right(90)
    mypen.forward(stripe_height)
    mypen.right(90)
    mypen.end_fill()
    mypen.penup()
    flag_y = flag_y - stripe_height

    # this function create navy color square
    # height = 7/13 of flag_height
    # width = 0.76 * flag_height
    # check references section for these values

    #starting point of the squre
    square_x = start_x
    square_y = start_y

    square_height = (7/13) * flag_height
    square_width = (0.76) * flag_height

    square_height = (7/13) * flag_height
    square_width = (0.76) * flag_height

    mypen.goto(square_x,square_y)
    mypen.pendown()
    mypen.color('navy')
    mypen.begin_fill()
    mypen.forward(square_width)
    mypen.right(90)
    mypen.forward(square_height)
    mypen.right(90)
    mypen.forward(square_width)
    mypen.right(90)
    mypen.forward(square_height)
    mypen.right(90)
    mypen.end_fill()
    mypen.penup()

    #draw 6 stars row
    gap_between_stars = 30
    gap_between_lines = stripe_height + 6
    stars_y = 112
    # create 4 rows of stars
    for row in range(0,5) :
        stars_x = -222
        # create 6 stars in each row
        for star in range (0,6) :
            mypen.goto(stars_x,stars_y)
            mypen.setheading(0)
            mypen.pendown()
            mypen.begin_fill()
            mypen.color('white')
            for turn in range(0,5) :
                mypen.forward(star_size)
                mypen.right(144)
                mypen.forward(star_size)
                mypen.right(144)
            mypen.end_fill()
            mypen.penup()
            stars_x = stars_x + gap_between_stars
        stars_y = stars_y - gap_between_lines

    #draw 5 stars row

    gap_between_stars = 30
    gap_between_lines = stripe_height + 6
    stars_y = 100
    # create 4 rows of stars
    for row in range(0,4) :
        stars_x = -206
        # create 5 stars in each row
        for star in range (0,5) :
            mypen.goto(stars_x,stars_y)
            mypen.setheading(0)
            mypen.pendown()
            mypen.begin_fill()
            mypen.color('white')
            for turn in range(0,5) :
                mypen.forward(star_size)
                mypen.right(144)
                mypen.forward(star_size)
                mypen.right(144)
            mypen.end_fill()
            mypen.penup()
            stars_x = stars_x + gap_between_stars
        stars_y = stars_y - gap_between_lines

    #writing title
    title_x = 0
    title_y = 230
    mypen.penup()
    mypen.goto(title_x, title_y)
    mypen.pendown()
    mypen.pencolor("blue")
    mypen.write("USA", align="center", font=("Helvetica",60,"bold"))
    mypen.penup()
    title_x = 0
    title_y = 160
    mypen.goto(title_x, title_y)
    mypen.pendown()
    mypen.write("OLYMPIC TEAM", align="center", font=("Helvetica",60,"bold"))
    #Drawing rings
    RADIUS = 70
    STARTING_POINT_X = -180
    STARTING_POINT_Y = -300
    x = STARTING_POINT_X
    y = STARTING_POINT_Y
    HSHIFT = 90
    VSHIFT = 80

    ring_index = 0
    for ring_color in ['navy','orange','black','green','red']:
        color = ring_color
        mypen.hideturtle()
        mypen.pensize(10)
        mypen.pencolor(ring_color) 
        mypen.penup() # when penup is set, drawing is disabled when move the cursor
        mypen.goto(x, y) # move the cursor to (x, y)
        mypen.pendown() #when pendown is setup, drawing is enabled
        mypen.circle(RADIUS) # draw a circle
        if ring_index %2 == 0: #it will draw an upper ring if the index is odd
            x+= HSHIFT
            y-= VSHIFT
        if ring_index %2 == 1: #it will draw a lower ring if the index is even
            x+= HSHIFT
            y+= VSHIFT
        ring_index += 1

    #write personal info
    x = 250
    y = -400
    #getting personal info from the print me first function
    info = print_me_first.printinfo()
    #write them in blue
    mypen.pencolor('blue')
    mypen.penup()
    mypen.goto(x,y) #go to the proper location
    mypen.write(info)
        
    turtle.hideturtle()
    # keep holding the screen until closed manually
    screen.mainloop()
