import tkinter as tk
import random

class NeuralNetwork:
    def __init__(self):
        self.weights = [[random.uniform(-1, 1), random.uniform(-1, 1)] for _ in range(2)]
        self.biases = [random.uniform(-1, 1) for _ in range(2)]
    
    def sigmoid(self, x):
        return 1 / (1 + pow(2.71828, -x))
    
    def feed_forward(self, inputs):
        output = [self.sigmoid(sum([inputs[j] * self.weights[i][j] for j in range(2)]) + self.biases[i]) for i in range(2)]
        return output.index(max(output))

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Shape Recognition")
        self.canvas = tk.Canvas(self.master, width=200, height=200, bg="white")
        self.canvas.pack()
        self.canvas.bind("<B1-Motion>", self.paint)
        self.classify_button = tk.Button(self.master, text="Classify", command=self.classify)
        self.classify_button.pack(side="left")
        self.correct_button = tk.Button(self.master, text="Correct", command=self.correct)
        self.correct_button.pack(side="left")
        self.incorrect_button = tk.Button(self.master, text="Incorrect", command=self.incorrect)
        self.incorrect_button.pack(side="left")
        self.nn = NeuralNetwork()
        self.inputs = []
    
    def paint(self, event):
        x, y = event.x, event.y
        self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="black")
        self.inputs.append([x/200, y/200])
    
    def classify(self):
        if self.inputs:
            output = self.nn.feed_forward([x for x in self.inputs[-1]])
            if output == 0:
                self.result = tk.Label(self.master, text="It's a circle!")
                self.result.pack()
            elif output == 1:
                self.result = tk.Label(self.master, text="It's a square!")
                self.result.pack()
        else:
            self.result = tk.Label(self.master, text="Please draw a shape!")
            self.result.pack()
    
    def correct(self):
        self.nn = NeuralNetwork()
        self.inputs = []
        self.canvas.delete("all")
        self.result.destroy()
    
    def incorrect(self):
        self.inputs = []
        self.canvas.delete("all")
        self.result.destroy()

root = tk.Tk()
app = App(root)
root.mainloop()
