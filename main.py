import tkinter as tk
from Carrier_Taskforce_Academy import start_carrier


def change(func):
    root.destroy()
    func()


def error():
    print("Not implemented yet!")


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Pinnacle Helldiver Training")
    frame = tk.Frame(root)
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.columnconfigure(2, weight=1)
    frame.columnconfigure(3, weight=1)
    frame.columnconfigure(4, weight=1)

    tk.Button(frame, text="LibertyFleet Academy: Navigating Seas of Freedom with Carrier Might", font=('Arial', 20),
              command=lambda: change(start_carrier)).grid(row=0, column=0, sticky=tk.W + tk.E)
    tk.Button(frame, text="AmericanOrbit College: Space Command & the Spirit of Liberty", font=('Arial', 20),
              command=lambda: change(error)).grid(row=1, column=0, sticky=tk.W + tk.E)
    tk.Button(frame, text="EagleTech Academy: Engineering & Patriotism United", font=('Arial', 20),
              command=lambda: change(error)).grid(row=2, column=0, sticky=tk.W + tk.E)
    tk.Button(frame, text="UnitedDefenders College: Strategic Sentries & Patriotic Precision", font=('Arial', 20),
              command=lambda: change(error)).grid(row=3, column=0, sticky=tk.W + tk.E)
    tk.Button(frame, text="ValorVault Training Center: Stockpiling Strength with Super Earth Pride", font=('Arial', 20),
              command=lambda: change(error)).grid(row=4, column=0, sticky=tk.W + tk.E)

    frame.pack()
    root.mainloop()
