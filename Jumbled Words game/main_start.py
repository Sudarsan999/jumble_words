from tkinter import *
import Database
def start_main_page():
    def start_game(args):
        main_window.destroy()
        if args == 1:
            from Options import Animals #Options is folder name where animals.py file is present
            Animals.main() # we are calling main function of animals.py file
        elif args == 2:
            from Options import Body_parts
            Body_parts.main()
        elif args == 3:
            from Options import Colour
            Colour.main()
        elif args == 4:
            from Options import Fruit
            Fruit.main()
        elif args == 5:
            from Options import Shapes
            Shapes.main()
        elif args == 6:
            from Options import Vegetable
            Vegetable.main()
        elif args == 7:
            from Options import Vehicles
            Vehicles.main()

    def option():

        lab_img1 = Button(
            main_window,
            image=img1, #back button logo
            bg='#e6fff5',
            border=5, #defualt value 1
            justify='center',
            command=back,
        )
        sel_btn1 = Button(
            text="Animals",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="green",
            cursor="hand2",
            command=lambda: start_game(1), #passing value 1 to function start_game
        )

        sel_btn2 = Button(
            text="Body parts",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="green",
            cursor="hand2",
            command=lambda: start_game(2),
        )

        sel_btn3 = Button(
            text="Colour",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="green",
            cursor="hand2",
            command=lambda: start_game(3),
        )

        sel_btn4 = Button(
            text="Fruits",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="green",
            cursor="hand2",
            command=lambda: start_game(4),
        )

        sel_btn5 = Button(
            text="Shapes",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="green",
            cursor="hand2",
            command=lambda: start_game(5),
        )

        sel_btn6 = Button(
            text="Vegetable",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="green",
            cursor="hand2",
            command=lambda: start_game(6),
        )

        sel_btn7 = Button(
            text="Vehicles",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="green",
            cursor="hand2",
            command=lambda: start_game(7),
        )
        lab_img1.grid(row=0, column=0, padx=40) #left space
        sel_btn1.grid(row=0, column=4, pady=(10, 0), padx=50, )
        sel_btn2.grid(row=1, column=4, pady=(10, 0), padx=50, )
        sel_btn3.grid(row=2, column=4, pady=(10, 0), padx=50, )
        sel_btn4.grid(row=3, column=4, pady=(10, 0), padx=50, )
        sel_btn5.grid(row=4, column=4, pady=(10, 0), padx=50, )
        sel_btn6.grid(row=5, column=4, pady=(10, 0), padx=50, )
        sel_btn7.grid(row=6, column=4, pady=(10, 0), padx=50, )

    def show_option():
        start_btn.destroy() #Removed start button

        lab_img.destroy() # Removed the logo as well
        option()
        
    def back():
    	main_window.destroy()
    	start_main_page()    	
    	

    main_window = Tk() # main_window ---> refers to tkinter package

    main_window.geometry("700x700+500+150") # geometry is the size of the game screen 700*700 (b*l) and 500 is x-axis , 150 is y-axis 
    main_window.resizable(0, 0) #To prevent resizing of window
    main_window.title("Jumbled Words Quiz") #game title
    main_window.configure(background="#e6fff5") #background colour of the game

    img0 = PhotoImage(file="logo1.png") #game logo image
    img1 = PhotoImage(file="back.png") #game back button image

#widgets of tkinter are label , button ...etc

    lab_img = Label(
        main_window,
        image=img0,
    )
    lab_img.pack(pady=(50, 50))  #pady is to provide space , 50 is top margin and 0 is bottom margin
    
    start_btn = Button(
        main_window,
        text="Start", #buttom text
        width=18, #buttom width
        borderwidth=8, #
        fg="#000000", #foreground 
        bg="green", #background
        font=("", 13), # 1st argument font style  2nd Parameter font size
        cursor="spider", #mouse cursor shape
        command=show_option,  #function calling
    )
    start_btn.pack(pady=(50, 20)) #pady is on y axis i.e top and bottom . 2. Padx is x-axis left and right
     
    
    main_window.mainloop()


start_main_page()
