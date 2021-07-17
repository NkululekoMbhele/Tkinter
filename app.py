from tkinter import filedialog
from tkinter import *
from pytube import YouTube 


def download_video():
    link = url_input.get()
    
    SAVE_PATH = "./" #to_do 
    #link="https://www.youtube.com/watch?v=nC9dQOnUyao"
    try: 
        youtube = YouTube(link) 
    except: 
        result_label.config(text="Connection Error")
        print() #to handle exception 
    d_video = youtube.streams.get_highest_resolution()
    try: 
        # downloading the video 
        d_video.download() 
    except: 
        print() 
        result_label.config(text="Some Error!")
    print() 
    result_label.config(text='Task Completed!')
    

window = Tk()
window.title("Download Youtube Videos")
window.config(padx=20, pady=20)


url_input = Entry(width=20)
url_input.grid(column=1, row=1)

folder_selected = filedialog.askdirectory()



url_label = Label(text="Enter the video url")
url_label.grid(column=0, row=1)


result_label = Label(text="")
result_label.grid(column=2, row=2)


download_button = Button(text="Download", command=download_video)
download_button.grid(column=1, row=2)


window.mainloop()