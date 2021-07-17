from tkinter import filedialog
from tkinter import *
from pytube import YouTube 


 #to_do 

def download_video():
    link = url_input.get()
    
    try: 
        youtube = YouTube(link) 
    except: 
        result_label.config(text="Connection Error")
        print() #to handle exception 
    d_video = youtube.streams.get_highest_resolution()
    try: 
        # downloading the video 
        d_video.download(file_path.cget("text")) 
    except: 
        print() 
        result_label.config(text="Some Error!")
    print() 
    result_label.config(text='Task Completed!')


SAVE_PATH = ""

def choose_folder():
    SAVE_PATH = str(filedialog.askdirectory())
    file_path.config(text=SAVE_PATH)
    
window = Tk()
window.title("Download Youtube Videos")
window.config(width=300, height=300, padx=100, pady=100)



url_input = Entry(width=50)
url_input.grid(column=1, row=0)


url_label = Label(text="Enter the video url: ", pady=20)
url_label.grid(column=0, row=0)

url_label = Label(text="File path: ")
url_label.grid(column=0, row=1)

download_button = Button(text="Browse", command=choose_folder)
download_button.grid(column=2, row=1)

file_path = Label(text="./", pady=20)
file_path.grid(column=1, row=1)

result_label = Label(text="", pady=20)
result_label.grid(column=1, row=3)


download_button = Button(text="Download", command=download_video)
download_button.grid(column=1, row=2)
window.mainloop()