from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 
import time
import music_genre_prediction_test
import asyncio

loop = asyncio.get_event_loop()

root = Tk()
root.title("Music Genre Predictor")
root.geometry("400x200")

song_filepath = ''

title = Label(root, text="Upload a song to check its genre")

buttonPredict = Button(root, text="Predict the genre", command=lambda:predict())
button = Button(root, text="Choose a song", command=lambda:open_file())
buttonAfter = Button(root, text="Choose another song", command=lambda:open_file())

progressBar = Progressbar(root, orient=HORIZONTAL, length=100, mode='indeterminate')

title.grid(row=0, column=0, columnspan=2)
button.grid(row=2, column=0)

def predict():
    progressBar.grid(row=4, column=0, columnspan=2)
    progressBar.start(10)
    asyncio.run(main(music_genre_prediction_test.predict(song_filepath)))
    progressBar.grid_remove()

async def main(predict_fun):
    result = await prediction_string(predict_fun)
    Label(root, text=f"Your song is predicted to be of a {result} genre.").grid(row=3, column=0, columnspan=2)

async def prediction_string(predict_fun):
    return predict_fun

def open_file():
    file_path = askopenfile(mode='r', filetypes=[("Audio Files", ".wav .ogg"),   ("All Files", "*.*")])
    if file_path is not None:
        button.grid_remove()
        Label(root, text='File Uploaded Successfully!', foreground='green').grid(row=1, columnspan=3, pady=10)
        global song_filepath 
        song_filepath = file_path.name
        buttonPredict.grid(row=2, column=0)
        buttonAfter.grid(row=2, column=1)


def uploadFiles():
    pb1 = Progressbar(
        root, 
        orient=HORIZONTAL, 
        length=300, 
        mode='determinate'
        )
    pb1.grid(row=1, columnspan=3, pady=20)
    for i in range(5):
        root.update_idletasks()
        pb1['value'] += 20
        time.sleep(1)
    pb1.destroy()
    Label(root, text='File Uploaded Successfully!', foreground='green').grid(row=1, columnspan=3, pady=10)


root.mainloop()