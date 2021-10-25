import threading
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import music_genre_prediction
import asyncio

song_filepath = ''

def do_prediction(async_loop, progressBar, predictionMessage, buttonPredict, buttonAfter):
    threading.Thread(target=_predict_thread, args=(async_loop, progressBar, predictionMessage, buttonPredict, buttonAfter)).start()

def _predict_thread(async_loop, progressBar, predictionMessage, buttonPredict, buttonAfter):
    async_loop.run_until_complete(predict_main(progressBar, predictionMessage, buttonPredict, buttonAfter))

def predict_main(progressBar, predictionMessage, buttonPredict, buttonAfter):
    buttonPredict["state"] = "disabled"
    buttonAfter["state"] = "disabled"
    progressBar.grid(row=4, column=1, columnspan=2)
    progressBar.start(10)
    
    asyncio.run(async_predict(music_genre_prediction.predict(song_filepath), predictionMessage))

    buttonPredict["state"] = "enable"
    buttonAfter["state"] = "enable"
    progressBar.grid_remove()

async def async_predict(predict_fun, predictionMessage):
    result = await prediction_string(predict_fun)
    predictionMessage.configure(text=f"Your song is predicted to be of a {result} genre.")
    predictionMessage.grid(row=3, column=1, columnspan=2)

async def prediction_string(predict_fun):
    return predict_fun

def open_file(button, buttonPredict, buttonAfter, successMessage, predictionMessage = None):
    file_path = askopenfile(mode='r', filetypes=[("Audio Files", ".wav .ogg"),   ("All Files", "*.*")])

    if file_path is not None:
        if predictionMessage != None:
            predictionMessage.grid_remove()
        button.grid_remove()

        file_name_short = file_path.name.split('/')[-1]
        successMessage.configure(text=f'You uploaded {file_name_short} successfully!')
        successMessage.grid(row=1, column=1, columnspan=2, pady=10)

        global song_filepath 
        song_filepath = file_path.name

        buttonPredict.grid(row=2, column=1, pady=20)
        buttonAfter.grid(row=2, column=2, pady=20)

# main funtion
def gui(async_loop):
    root = Tk()

    # Basic window options
    root.title("Music Genre Predictor")
    root.geometry("400x200")

    # Components initialization
    title = Label(root, text="Upload a song to check its genre")
    successMessage = Label(root, text='', foreground='green')
    predictionMessage = Label(root, text='')
    progressBar = Progressbar(root, orient=HORIZONTAL, length=200, mode='indeterminate')
    buttonPredict = Button(root, text="Predict the genre", command=lambda:do_prediction(async_loop, progressBar, predictionMessage, buttonPredict, buttonAfter))
    buttonAfter = Button(root, text="Choose another song", command=lambda:open_file(button, buttonPredict, buttonAfter, successMessage, predictionMessage))
    button = Button(root, text="Choose a song", command=lambda:open_file(button, buttonPredict, buttonAfter, successMessage))

    # Components setting
    title.grid(row=0, column=1, columnspan=2, pady=10)
    button.grid(row=2, column=1, columnspan=2)

    # root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure((0, 3), weight=1)
    root.mainloop()

if __name__ == '__main__':
    async_loop = asyncio.get_event_loop()
    gui(async_loop)