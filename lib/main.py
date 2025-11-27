from tkinter import Tk, Frame, Label, Entry, Button, messagebox, PhotoImage

class SimpleyServeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simpley Serve")
        self.root.geometry("300x400")

            # Load image
        try:
            self.image = PhotoImage(file="SimplyServe_resized.png")  
        except Exception as e:
            print(f"[ERROR] Could not load image: {e}")
            self.image = None

        main_frame = Frame(root , padx=20, pady=20)
        main_frame.pack(expand=True, fill="both")

        # Display logo if loaded
        if self.image:
            logo_label = Label(main_frame, image=self.image )
            logo_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Title
        title_label = Label(main_frame, text="Simpley Serve")
        title_label.grid(row=1, column=0, columnspan=2, pady=(0, 20))

        # Username
        Label(main_frame, text="Username:").grid(
            row=2, column=0, sticky="w", pady=5)
        self.username_entry = Entry(main_frame, width=25)
        self.username_entry.grid(row=2, column=1, pady=5)

        # Password
        Label(main_frame, text="Password:").grid(
            row=3, column=0, sticky="w", pady=5)
        self.password_entry = Entry(main_frame, width=25, show="*")
        self.password_entry.grid(row=3, column=1, pady=5)

        # Buttons
        Button(main_frame, text="Login", 
               width=15).grid(row=4, column=0, pady=15, padx=5)
        Button(main_frame, text="Sign Up",
               width=15).grid(row=4, column=1, pady=15, padx=5)


def main():
    root = Tk()
    app = SimpleyServeApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()