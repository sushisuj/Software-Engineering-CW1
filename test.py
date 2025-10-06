from tkinter import Tk, Frame, Button, Label, StringVar, Toplevel, Entry

class HealthApp:
    
    def __init__(self, smart_home):
        self.smart_home = smart_home

        self.win = Tk()
        self.win.title("Smart Home Control")

        self.main_frame = Frame(self.win)
        self.main_frame.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
        )

        self.new_device_type = StringVar()

        self.device_widgets = []

    def create_widgets(self):
        # Create a new frame (box)
        self.box_frame = Frame(self.main_frame, borderwidth=2, relief="solid")
        self.box_frame.grid(row=1, column=0, padx=10, pady=10)

        # Add a button inside the frame
        self.box_button = Button(self.box_frame, text="Click Me", command=self.on_button_click)
        self.box_button.pack(padx=5, pady=5)

    def on_button_click(self):
        print("Button inside the box clicked!")

    def run(self):
        self.create_widgets()
        self.win.mainloop()

if __name__ == "__main__":
    app = SmartHomeApp(smart_home=None)
    app.run()
