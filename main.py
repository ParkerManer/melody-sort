import tkinter as tk
import random
import time
import subprocess
from pydub.playback import play  # Import the play function
from music_generator import MusicGenerator  # Import the MusicGenerator class

# Create an instance of the MusicGenerator class
music_generator = MusicGenerator()

# Function to perform Bubble Sort
def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                update_visualization(data, [j, j+1])  # Highlight the bars being compared
                note = data[j]  # Use the value of data[j] to determine the note to play
                sound = music_generator.generate_tone(note)  # Generate the note dynamically
                
                # Redirect ffmpeg's stderr to /dev/null on macOS
                devnull = open('/dev/null', 'w')
                play(sound)
                devnull.close()
                
                time.sleep(0.01)
                update_visualization(data, [j, j+1], highlight=False)  # Remove the highlight

# Function to update the visualization (same as before)
def update_visualization(data, highlighted_indices=None, highlight=True):
    canvas.delete("all")
    bar_width = canvas_width / len(data)
    
    for i, height in enumerate(data):
        x1, y1, x2, y2 = i * bar_width, canvas_height, (i + 1) * bar_width, canvas_height - height
        if highlighted_indices and i in highlighted_indices:
            fill_color = "red" if highlight else "blue"
        else:
            fill_color = "blue"
        canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color)
    root.update()

# Create the main window
root = tk.Tk()
root.title("Melody-Sort Visualization")

canvas_width = 400
canvas_height = 400

canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# Generate random data to sort
data = [random.randint(10, 300) for _ in range(50)]

# Create a button to start sorting
start_button = tk.Button(root, text="Start Sorting", command=lambda: bubble_sort(data))
start_button.pack()

root.mainloop()
