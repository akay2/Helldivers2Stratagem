import random
import time
import tkinter as tk


class Carrier:
    eagle_strafing_run = ["Strafing Run", 'w', 'd', 'd']  # 100%
    eagle_airstrike = ["Airstrike", 'w', 'd', 's', 'd']  # 100%
    eagle_cluster_bomb = ["Cluster Bombs", 'w', 'd', 's', 's', 'd']  # 100%
    eagle_napalm = ["Napalm Airstrike", 'w', 'd', 's', 'w']  # 50%
    eagle_rockets = ["Rocket Pods", 'w', 'd', 'w', 'a']  # 100%
    eagle_500kg = ["500KG BOMB", 'w', 'd', 's', 's', 's']  # 100%
    eagle_options = [eagle_strafing_run, eagle_airstrike, eagle_cluster_bomb, eagle_napalm, eagle_rockets, eagle_500kg]

    def __init__(self):
        self.next = self.eagle_options[random.randint(0, len(self.eagle_options) - 1)]

    def re_roll(self):
        self.next = self.eagle_options[random.randint(0, len(self.eagle_options) - 1)]

    def get_image(self):
        match self.next[0]:
            case "Strafing Run":
                return 0
            case "Airstrike":
                return 1
            case "Cluster Bombs":
                return 2
            case "Napalm Airstrike":
                return 3
            case "Rocket Pods":
                return 4
            case "500KG BOMB":
                return 5


def letter_to_index(letter):
    match letter:
        case 'w':
            return 0
        case 's':
            return 1
        case 'a':
            return 2
        case 'd':
            return 3


class Windows:

    def __init__(self):
        self.images = []
        self.label_images = []
        self.width = 400
        self.height = 250
        self.x_off = 0
        self.y_off = 0
        self.root = None
        self.labels = []
        self.current_idx = 0
        self.carrier = Carrier()
        self.create_root()

    def create_root(self):
        if self.root is not None:
            self.root.destroy()
        self.root = tk.Tk()
        self.root.bind("<w>", self.pressed)
        self.root.bind("<s>", self.pressed)
        self.root.bind("<a>", self.pressed)
        self.root.bind("<d>", self.pressed)
        self.root.bind("<W>", self.pressed)
        self.root.bind("<S>", self.pressed)
        self.root.bind("<A>", self.pressed)
        self.root.bind("<D>", self.pressed)
        self.images = [tk.PhotoImage(file="images/empty.png"), tk.PhotoImage(file="images/empty.png"),
                       tk.PhotoImage(file="images/empty.png"), tk.PhotoImage(file="images/empty.png"),
                       tk.PhotoImage(file="images/empty.png")]
        self.label_images = [tk.PhotoImage(file="images/strafe.png"),
                             tk.PhotoImage(file="images/airstrike.png"),
                             tk.PhotoImage(file="images/cluster.png"),
                             tk.PhotoImage(file="images/napalm.png"),
                             tk.PhotoImage(file="images/rockets.png"),
                             tk.PhotoImage(file="images/500kg.png")]
        self.x_off = (self.root.winfo_screenwidth() - self.width) // 2
        self.y_off = (self.root.winfo_screenheight() - self.height) // 2
        self.root.geometry(f"{self.width}x{self.height}+{self.x_off}+{self.y_off}")
        tk.Label(self.root, text=self.carrier.next[0], font=('Arial', 20)).pack(pady=5)
        tk.Label(self.root, image=self.label_images[self.carrier.get_image()]).pack(pady=5)

        self.labels = []
        frame = tk.Frame(self.root)
        for i in range(len(self.carrier.next) - 1):
            label = tk.Label(frame, image=self.images[i])
            label.grid(row=0, column=i)
            self.labels.append(label)
        frame.pack(pady=5)

        btnframe = tk.Frame(self.root)
        tk.Button(btnframe, text="End me", font=('Arial', 20), command=self.root.destroy).grid(row=0, column=0)
        btnframe.pack(pady=5)

        self.root.title("Carrier Taskforce Academy")
        self.root.focus_force()

    def green_re_roll(self):
        for i in range(len(self.carrier.next) - 1):
            match self.carrier.next[i + 1]:
                case 'w':
                    path = "images/w_g.png"
                case 'd':
                    path = "images/d_g.png"
                case 's':
                    path = "images/s_g.png"
                case 'a':
                    path = "images/a_g.png"
            self.images[i] = tk.PhotoImage(file=path)
        for i in range(len(self.labels)):
            self.labels[i].config(image=self.images[i])
        self.root.after(50, self.re_roll)

    def get_window(self):
        return self.root

    def re_roll(self):
        self.carrier.re_roll()
        self.current_idx = 0
        self.create_root()

    def shake_window(self):
        x0, y0 = self.root.winfo_x(), self.root.winfo_y()
        amp = 5
        freq = 2

        for _ in range(freq):
            self.root.geometry(f"+{x0 + amp}+{y0}")
            self.root.update()
            time.sleep(0.02)
            self.root.geometry(f"+{x0 - amp}+{y0}")
            self.root.update()
            time.sleep(0.02)
        self.root.geometry(f"+{x0}+{y0}")

    def pressed(self, event):
        # <KeyPress event send_event=True state=Mod1 keysym=w keycode=87 char='w' x=287 y=107>
        c = event.char.lower()
        if c == self.carrier.next[self.current_idx + 1]:
            self.images[self.current_idx] = tk.PhotoImage(file="images/" + c + ".png")
            self.labels[self.current_idx].config(image=self.images[self.current_idx])
            self.current_idx += 1
            if self.current_idx >= len(self.carrier.next) - 1:
                self.green_re_roll()
        else:
            self.current_idx = 0
            for i in range(len(self.images)):
                self.images[i] = tk.PhotoImage(file="images/empty.png")
            for i in range(len(self.labels)):
                self.labels[i].config(image=self.images[i])
            self.shake_window()


def start_carrier():
    w = Windows()
    root = w.get_window()
    root.mainloop()


if __name__ == '__main__':
    start_carrier()
