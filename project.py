from tkinter import *
from PIL import ImageTk,Image 

def main():
    root = Tk()
    
    root.title("Project")
    root.geometry("300x630")
    
    canvas = Canvas(root,width = 300,height=630,bg = "WHITE",bd = 0)
    f1 = Frame(canvas,width = 300,height=150,bg = "BLUE",bd = 0).place(x = 0 ,y = 0)
    
    
    # Insert image
    
    
    photo = ImageTk.PhotoImage(file='C://Users//Akash rana//Desktop//front.png')

    canvas.create_image(0,0,anchor=NW,image=photo)
    canvas.pack()
    
    f2=Frame(f1,width=260,height=480,bg="WHITE",bd=4,relief=GROOVE).place(x=20,y=130)
    
    l1 = Label(f2,font=('arial',30,'bold'),text="DYKAA",fg = "BLUE").place(x = 75,y=140)
    l1 = Label(f2,font=('Times New Roman',36,'bold'),text="L O G I N",fg = "BLUE").place(x = 40,y=230)
    
    e1=Entry(f2,font=('arial',15),bd=8,insertwidth=1, justify = 'left').place(x=30,y=330)
    e1=Entry(f2,font=('arial',15),bd=8,insertwidth=1, justify = 'left').place(x=30,y=400)
    
  #  button = PhotoImage(file="C://Users//Akash rana//Pictures//Screenshots//login.jpeg")
    btn = Button(f2,text=login).place(x = 0,y=150)
    
    
    
    
    
       
    root.mainloop()
if __name__=="__main__":
    main()    