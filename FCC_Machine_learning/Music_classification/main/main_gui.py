import threading
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import music_genre_prediction
import asyncio

song_filepath = ''

def do_prediction(async_loop, progressBar, root):
    threading.Thread(target=_predict_thread, args=(async_loop, progressBar, root)).start()

def _predict_thread(async_loop, progressBar, root):
    async_loop.run_until_complete(predict_main(progressBar, root))

def predict_main(progressBar, root):
    progressBar.grid(row=4, column=0, columnspan=2)
    progressBar.start(10)
    asyncio.run(async_predict(music_genre_prediction.predict(song_filepath), root))
    progressBar.grid_remove()

async def async_predict(predict_fun, root):
    result = await prediction_string(predict_fun)
    Label(root, text=f"Your song is predicted to be of a {result} genre.").grid(row=3, column=0, columnspan=2)

async def prediction_string(predict_fun):
    return predict_fun

def open_file(button, buttonPredict, buttonAfter, successMessage):
    file_path = askopenfile(mode='r', filetypes=[("Audio Files", ".wav .ogg"),   ("All Files", "*.*")])
    if file_path is not None:
        button.grid_remove()
        file_name_short = file_path.name.split('/')[-1]
        successMessage.configure(text=f'You uploaded {file_name_short} successfully!')
        successMessage.grid(row=1, columnspan=3, pady=10)
        global song_filepath 
        song_filepath = file_path.name
        buttonPredict.grid(row=2, column=0)
        buttonAfter.grid(row=2, column=1)

# main funtion
def gui(async_loop):
    root = Tk()

    # Basic window options
    root.title("Music Genre Predictor")
    root.geometry("400x200")

    # Components initialization
    title = Label(root, text="Upload a song to check its genre")
    successMessage = Label(root, text='File uploaded successfully', foreground='green')
    progressBar = Progressbar(root, orient=HORIZONTAL, length=100, mode='indeterminate')
    buttonPredict = Button(root, text="Predict the genre", command=lambda:do_prediction(async_loop, progressBar, root))
    buttonAfter = Button(root, text="Choose another song", command=lambda:open_file(button, buttonPredict, buttonAfter, successMessage))
    button = Button(root, text="Choose a song", command=lambda:open_file(button, buttonPredict, buttonAfter, successMessage))

    # Components setting
    title.grid(row=0, column=0, columnspan=2)
    button.grid(row=2, column=0)

    root.mainloop()

if __name__ == '__main__':
    async_loop = asyncio.get_event_loop()
    gui(async_loop)