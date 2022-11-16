# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import tkinter as tk
import pyttsx3

# Setup TTS Engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# Read Aloud / TTS
def read_aloud(text):
    engine.say(text)
    engine.runAndWait()


def main():
    # Main window
    root = tk.Tk()
    root.title("Read2Me")

    # Build GUI
    # Setup window dimensions
    window_width = 300
    window_height = 150

    # Get screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Find the center point
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    # Set position of window to the center of the screen
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    # Text Label
    label = tk.Label(root, text="Paste the text you would to have read to you.")
    label.pack(padx=10, pady=10)
    # Input Field
    input_field = tk.Entry(root)
    input_field.pack(padx=10, pady=10)
    input_field.bind('<Return>', lambda: read_aloud(input_field.get()))

    # Submit Field
    submit_button = tk.Button(root, text="Start", command=lambda: read_aloud(input_field.get()))
    submit_button.pack(padx=10, pady=10)

    # Keep window running
    root.mainloop()


if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
