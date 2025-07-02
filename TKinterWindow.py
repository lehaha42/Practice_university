import tkinter as tk


class TKinterWindow:

    def __init__(self, commonResource):
        self.resource = commonResource
        self.root = tk.Tk()
        self.root.title('Окно управления')
        self.root.geometry('320x320')

        button = tk.Button(self.root, text='поменять режим сетки', command=self.change_mode)
        button.grid(row=0, column=0)
        button = tk.Button(self.root, text='применить', command=self.update)
        button.grid(row=4, column=0)

        self.label1 = tk.Label(self.root, text=f'текущий режим: {['декартова', 'полярная'][self.resource.mode]}')
        self.label1.grid(row=0, column=1)

        label = tk.Label(self.root, text='формула: R = a*e^(b*t)')
        label.grid(row=1, column=0)
        label = tk.Label(self.root, text='a = ')
        label.grid(row=2, column=0)
        label = tk.Label(self.root, text='b = ')
        label.grid(row=3, column=0)

        self.entry1 = tk.Entry(self.root)
        self.entry1.grid(row=2, column=1)
        self.entry2 = tk.Entry(self.root)
        self.entry2.grid(row=3, column=1)

    def change_mode(self):
        self.resource.mode = 1 - self.resource.mode
        self.label1.configure(text=f'текущий режим: {['декартова', 'полярная'][self.resource.mode]}')

    def update(self):
        try:
            a = float(self.entry1.get())
            b = float(self.entry2.get())
            self.resource.a = a
            self.resource.b = b
        except Exception:
            pass

    def on_close(self):
        self.resource.terminate = True
        self.root.destroy()

    def run(self):
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        while not self.resource.terminate:
            self.root.update()
