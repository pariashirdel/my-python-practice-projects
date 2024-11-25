from random import randint
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry('500x300')
root.title('Magic Woosh Dice roller')
root.iconbitmap('static/icon.ico')


frames = []
delay = 0
frame_count = -1

def D4():
    rolling_window = Toplevel()
    rolling_window.title('rolling dice...')
    rolling_window.geometry('500x500')
    rolling_window.iconbitmap('static/icon.ico')
    
    
    def final_output():
        number = Toplevel()
        number.title('Woosh!')
        number.iconbitmap('static/icon.ico')
        
        background_image = Image.open("static/wooshcat.png")
        tk_image = ImageTk.PhotoImage(background_image)
        output_num = randint(1,4)
        
        label1 = Label(number, text=f"Whoosh! you got {output_num}", image= tk_image, compound='center')
        label1.grid(row=4 , column=0)
        label1.image = tk_image
        
    def gif_to_image():
        global delay
        
        
        file = Image.open("static/catdice.gif")
        
        for frame in range(file.n_frames):
            file.seek(frame)
            frames.append(file.copy())
        
        delay = file.info['duration']
        play_gif()
    
    def play_gif():
        global frame_count, current_frame
        
        if frame_count >= len(frames)-1 :
            frame_count = -1
        else:
            frame_count += 1
            
            current_frame = ImageTk.PhotoImage(frames[frame_count])
            gif_lb.config(image=current_frame)
            
            rolling_window.after(delay, play_gif)
    
    gif_lb = Label(rolling_window)
    gif_lb.pack(fill=BOTH)
    
    gif_to_image()
    
    rolling_window.after(4000, final_output)
    rolling_window.after(4000, rolling_window.destroy)
    


def D6():
    rolling_window = Toplevel()
    rolling_window.title('rolling dice...')
    rolling_window.geometry('500x500')
    rolling_window.iconbitmap('static/icon.ico')
    
    
    def final_output():
        number = Toplevel()
        number.title('Woosh!')
        number.iconbitmap('static/icon.ico')
        
        background_image = Image.open("static/wooshcat.png")
        tk_image = ImageTk.PhotoImage(background_image)
        output_num = randint(1,6)
        
        label1 = Label(number, text=f"Whoosh! you got {output_num}", image= tk_image, compound='center')
        label1.grid(row=4 , column=0)
        label1.image = tk_image
        
    def gif_to_image():
        global delay
        
        
        file = Image.open("static/catdice.gif")
        
        for frame in range(file.n_frames):
            file.seek(frame)
            frames.append(file.copy())
        
        delay = file.info['duration']
        play_gif()
    
    def play_gif():
        global frame_count, current_frame
        
        if frame_count >= len(frames)-1 :
            frame_count = -1
        else:
            frame_count += 1
            
            current_frame = ImageTk.PhotoImage(frames[frame_count])
            gif_lb.config(image=current_frame)
            
            rolling_window.after(delay, play_gif)
    
    gif_lb = Label(rolling_window)
    gif_lb.pack(fill=BOTH)
    
    gif_to_image()
    
    rolling_window.after(4000, final_output)
    rolling_window.after(4000, rolling_window.destroy)
    

def D8():
    rolling_window = Toplevel()
    rolling_window.title('rolling dice...')
    rolling_window.geometry('500x500')
    rolling_window.iconbitmap('static/icon.ico')
    
    
    def final_output():
        number = Toplevel()
        number.title('Woosh!')
        number.iconbitmap('static/icon.ico')
        
        background_image = Image.open("static/wooshcat.png")
        tk_image = ImageTk.PhotoImage(background_image)
        output_num = randint(1,8)
        
        label1 = Label(number, text=f"Whoosh! you got {output_num}", image= tk_image, compound='center')
        label1.grid(row=4 , column=0)
        label1.image = tk_image
        
    def gif_to_image():
        global delay
        
        
        file = Image.open("static/catdice.gif")
        
        for frame in range(file.n_frames):
            file.seek(frame)
            frames.append(file.copy())
        
        delay = file.info['duration']
        play_gif()
    
    def play_gif():
        global frame_count, current_frame
        
        if frame_count >= len(frames)-1 :
            frame_count = -1
        else:
            frame_count += 1
            
            current_frame = ImageTk.PhotoImage(frames[frame_count])
            gif_lb.config(image=current_frame)
            
            rolling_window.after(delay, play_gif)
    
    gif_lb = Label(rolling_window)
    gif_lb.pack(fill=BOTH)
    
    gif_to_image()
    
    rolling_window.after(4000, final_output)
    rolling_window.after(4000, rolling_window.destroy)
    

def D10():
    rolling_window = Toplevel()
    rolling_window.title('rolling dice...')
    rolling_window.geometry('500x500')
    rolling_window.iconbitmap('static/icon.ico')
    
    
    def final_output():
        number = Toplevel()
        number.title('Woosh!')
        number.iconbitmap('static/icon.ico')
        
        background_image = Image.open("static/wooshcat.png")
        tk_image = ImageTk.PhotoImage(background_image)
        output_num = randint(1,12)
        
        label1 = Label(number, text=f"Whoosh! you got {output_num}", image= tk_image, compound='center')
        label1.grid(row=4 , column=0)
        label1.image = tk_image
        
    def gif_to_image():
        global delay
        
        
        file = Image.open("static/catdice.gif")
        
        for frame in range(file.n_frames):
            file.seek(frame)
            frames.append(file.copy())
        
        delay = file.info['duration']
        play_gif()
    
    def play_gif():
        global frame_count, current_frame
        
        if frame_count >= len(frames)-1 :
            frame_count = -1
        else:
            frame_count += 1
            
            current_frame = ImageTk.PhotoImage(frames[frame_count])
            gif_lb.config(image=current_frame)
            
            rolling_window.after(delay, play_gif)
    
    gif_lb = Label(rolling_window)
    gif_lb.pack(fill=BOTH)
    
    gif_to_image()
    
    rolling_window.after(4000, final_output)
    rolling_window.after(4000, rolling_window.destroy)
    
def D12():
    rolling_window = Toplevel()
    rolling_window.title('rolling dice...')
    rolling_window.geometry('500x500')
    rolling_window.iconbitmap('static/icon.ico')
    
    
    def final_output():
        number = Toplevel()
        number.title('Woosh!')
        number.iconbitmap('static/icon.ico')
        
        background_image = Image.open("static/wooshcat.png")
        tk_image = ImageTk.PhotoImage(background_image)
        output_num = randint(1,4)
        
        label1 = Label(number, text=f"Whoosh! you got {output_num}", image= tk_image, compound='center')
        label1.grid(row=4 , column=0)
        label1.image = tk_image
        
    def gif_to_image():
        global delay
        
        
        file = Image.open("static/catdice.gif")
        
        for frame in range(file.n_frames):
            file.seek(frame)
            frames.append(file.copy())
        
        delay = file.info['duration']
        play_gif()
    
    def play_gif():
        global frame_count, current_frame
        
        if frame_count >= len(frames)-1 :
            frame_count = -1
        else:
            frame_count += 1
            
            current_frame = ImageTk.PhotoImage(frames[frame_count])
            gif_lb.config(image=current_frame)
            
            rolling_window.after(delay, play_gif)
    
    gif_lb = Label(rolling_window)
    gif_lb.pack(fill=BOTH)
    
    gif_to_image()
    
    rolling_window.after(4000, final_output)
    rolling_window.after(4000, rolling_window.destroy)
    

def D20():
    rolling_window = Toplevel()
    rolling_window.title('rolling dice...')
    rolling_window.geometry('500x500')
    rolling_window.iconbitmap('static/icon.ico')
    
    
    def final_output():
        number = Toplevel()
        number.title('Woosh!')
        number.iconbitmap('static/icon.ico')
        
        background_image = Image.open("static/wooshcat.png")
        tk_image = ImageTk.PhotoImage(background_image)
        output_num = randint(1,20)
        
        label1 = Label(number, text=f"Whoosh! you got {output_num}", image= tk_image, compound='center')
        label1.grid(row=4 , column=0)
        label1.image = tk_image
        
    def gif_to_image():
        global delay
        
        
        file = Image.open("static/catdice.gif")
        
        for frame in range(file.n_frames):
            file.seek(frame)
            frames.append(file.copy())
        
        delay = file.info['duration']
        play_gif()
    
    def play_gif():
        global frame_count, current_frame
        
        if frame_count >= len(frames)-1 :
            frame_count = -1
        else:
            frame_count += 1
            
            current_frame = ImageTk.PhotoImage(frames[frame_count])
            gif_lb.config(image=current_frame)
            
            rolling_window.after(delay, play_gif)
    
    gif_lb = Label(rolling_window)
    gif_lb.pack(fill=BOTH)
    
    gif_to_image()
    
    rolling_window.after(4000, final_output)
    rolling_window.after(4000, rolling_window.destroy)
    




button_D4 = Button(root, text='roll a D4', command=D4)
button_D4.pack()

button_D6 = Button(root, text='roll a D6', command=D6)
button_D6.pack()

button_D8 = Button(root, text='roll a D8', command=D8)
button_D8.pack()

button_D10 = Button(root, text='roll a D10', command=D10)
button_D10.pack()

button_D12 = Button(root, text='roll a D12', command=D12)
button_D12.pack()

button_D20 = Button(root, text='roll a D20', command=D20)
button_D20.pack()



root.mainloop()