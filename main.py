import tkinter as tk
import random
import time
# random change
# Function to perform Bubble Sort
def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                update_visualization(data)
                time.sleep(0.1)

# Function to update the visualization
def update_visualization(data):
    canvas.delete("all")
    bar_width = canvas_width / len(data)
    for i, height in enumerate(data):
        x1, y1, x2, y2 = i * bar_width, canvas_height, (i + 1) * bar_width, canvas_height - height
        canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
    root.update()

# Create the main window
root = tk.Tk()
root.title("Melody-Sort Visualization")

canvas_width = 800
canvas_height = 400

canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# Generate random data to sort
data = [random.randint(10, 300) for _ in range(50)]

# Create a button to start sorting
start_button = tk.Button(root, text="Start Sorting", command=lambda: bubble_sort(data))
start_button.pack()

root.mainloop()
