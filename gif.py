import tkinter as tk
from PIL import Image, ImageTk


rolling_window =tk.Tk()
rolling_window.title('rolling dice...')
rolling_window.geometry('500x500')
rolling_window.iconbitmap('static/icon.ico')

frames = []
delay = 0

def gif_to_image():
    global delay
    
    
    file = Image.open("static/catdice.gif")
    
    for frame in range(file.n_frames):
        file.seek(frame)
        frames.append(file.copy())
    
    delay = file.info['duration']
    play_gif()

frame_count = -1

def play_gif():
    global frame_count, current_frame
    
    if frame_count >= len(frames)-1 :
        rolling_window.destroy
    else:
        frame_count += 1
        
        current_frame = ImageTk.PhotoImage(frames[frame_count])
        gif_lb.config(image=current_frame)
        
        rolling_window.after(delay, play_gif)


gif_lb = tk.Label(rolling_window)
gif_lb.pack(fill=tk.BOTH)


if __name__ == "__main__":
    gif_to_image()
    rolling_window.mainloop()
    