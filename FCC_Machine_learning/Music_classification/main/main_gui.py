import threading
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 
import time
import music_genre_prediction
import asyncio

loop = asyncio.get_event_loop()

song_filepath = ''

def _asyncio_thread(async_loop):
    async_loop.run_until_complete(main())

def do_tasks(async_loop):
    threading.Thread(target=_asyncio_thread, args=(async_loop,)).start()

def gui(async_loop):
    root = Tk()

    root.title("Music Genre Predictor")
    root.geometry("400x200")


    title = Label(root, text="Upload a song to check its genre")

    progressBar = Progressbar(root, orient=HORIZONTAL, length=100, mode='indeterminate')
    buttonPredict = Button(root, text="Predict the genre", command=lambda:predict(progressBar, root))
    buttonAfter = Button(root, text="Choose another song", command=lambda:open_file(button, root, buttonPredict, buttonAfter))
    button = Button(root, text="Choose a song", command=lambda:open_file(button, root, buttonPredict, buttonAfter))


    title.grid(row=0, column=0, columnspan=2)
    button.grid(row=2, column=0)

    root.mainloop()

def predict(progressBar, root):
    progressBar.grid(row=4, column=0, columnspan=2)
    progressBar.start(10)
    asyncio.run(main(music_genre_prediction.predict(song_filepath), root))
    progressBar.grid_remove()

async def main(predict_fun, root):
    result = await prediction_string(predict_fun)
    Label(root, text=f"Your song is predicted to be of a {result} genre.").grid(row=3, column=0, columnspan=2)

async def prediction_string(predict_fun):
    return predict_fun

def open_file(button, root, buttonPredict, buttonAfter):
    file_path = askopenfile(mode='r', filetypes=[("Audio Files", ".wav .ogg"),   ("All Files", "*.*")])
    if file_path is not None:
        button.grid_remove()
        Label(root, text='File Uploaded Successfully!', foreground='green').grid(row=1, columnspan=3, pady=10)
        global song_filepath 
        song_filepath = file_path.name
        buttonPredict.grid(row=2, column=0)
        buttonAfter.grid(row=2, column=1)


def uploadFiles(root):
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

if __name__ == '__main__':
    async_loop = asyncio.get_event_loop()
    gui(async_loop)