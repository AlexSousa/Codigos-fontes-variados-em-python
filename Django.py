from tkinter import *
from downloader import *


from teste.download import download_video

window = Tk()
window.title('youtube')
window.geometry("500x200")
window.resizable(0, 0)

title = Label(window, text='youtube', font=('Arial', 25), fg='Blue')
title.pack()
msg = Label(window, text='', font=('Arial,15'))
entry_url = Entry(window, width=60, justify='center')
entry_url.insert(0, "Enter the url")
entry_url.pack()
entry_url.focus_set()

entry_name_video = Entry(window, width=60, justify='center')
entry_name_video.insert(0, 'Enter the name video')
entry_name_video.pack()


def click_button():
    url = entry_url.get()
    name_video = entry_name_video.get()

    if download_video(url, name_video):
        msg['fg'] = 'Green'
        msg['text'] = 'Download feito Com Sucesso'

    else:
        msg['fg'] = 'Red'
        msg['text'] = 'Ocorreu alguma Falha'


btn = Button(window, text='Download now', width=20, command=click_button)
btn.pack()

window.mainloop()
