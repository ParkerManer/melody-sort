import tkinter as tk
import random
import time
import subprocess
from pydub.playback import play  # Import the play function
from tone_generator import play_tone, generate_tone

# Function to perform Bubble Sort
def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                update_visualization(data, [j, j+1])  # Highlight the bars being compared
                note = data[j]  # Use the value of data[j] to determine the note to play
                note2 = data[j+1]
                duration = 0.03  # Set the duration for the note (in seconds)
                play_tone(note, duration*2/3)  # Play the generated tone
                play_tone(note2, duration/3)
                update_visualization(data, [j, j+1], highlight=False)  # Remove the highlight

# Function to update the visualization (same as before)
def update_visualization(data, highlighted_indices=None, highlight=True):
    canvas.delete("all")
    bar_width = canvas_width / len(data)
    
    for i, height in enumerate(data):
        x1, y1, x2, y2 = i * bar_width, canvas_height, (i + 1) * bar_width, canvas_height - height
        if highlighted_indices and i in highlighted_indices:
            fill_color = "lightblue" if highlight else "blue"
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
# Define the frequencies of natural notes across middle five octaves (C4 to B8)
note_frequencies = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 523.25, 587.33, 659.26, 698.46, 783.99, 880.00, 987.77, 1046.50, 1174.66, 1318.51, 1396.91, 1567.98, 1760.00, 1975.53, 2093.00, 2349.32, 2637.02, 2793.83]
freqdownoct = [freq / 4  for freq in note_frequencies]
# Generate a random list of natural note frequencies from C4 to B8
num_notes = 20  # Adjust the number of notes as needed
data = random.sample(freqdownoct, num_notes)


# Create a button to start sorting
start_button = tk.Button(root, text="Start Sorting", command=lambda: bubble_sort(data))
start_button.pack()

root.mainloop()
