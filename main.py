from tkinter import Tk, Frame, Label, Entry, Button, messagebox, PhotoImage

class SimpleyServeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simpley Serve")
        self.root.geometry("400x500")

        # Load image as GIF (Tkinter supports GIF natively)
        try:
            self.image = PhotoImage(file="SimplyServe_resized.gif")  # ← MUST be .gif!
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
        title_label = Label(main_frame, text="Simpley Serve", font=("Arial", 18, "bold"), 
                                )
        title_label.grid(row=1, column=0, columnspan=2, pady=(0, 20))

        # Username
        Label(main_frame, text="Username:", font=("Arial", 12) ).grid(
            row=3, column=0, sticky="w", pady=5)
        self.username_entry = Entry(main_frame, font=("Arial", 12), width=25)
        self.username_entry.grid(row=3, column=1, pady=5)

        # Password
        Label(main_frame, text="Password:", font=("Arial", 12) ).grid(
            row=2, column=0, sticky="w", pady=5)
        self.password_entry = Entry(main_frame, font=("Arial", 12), width=25, show="*")
        self.password_entry.grid(row=2, column=1, pady=5)

        # Buttons
        Button(main_frame, text="Login", font=("Arial", 12, "bold"),
               width=15, command=self.login).grid(row=4, column=0, pady=15, padx=5)
        Button(main_frame, text="Sign Up", font=("Arial", 12, "bold"),
               width=15, command=self.sign_up).grid(row=4, column=1, pady=15, padx=5)

        # Footer
        Label(main_frame, text="© 2025 Simpley Serve. All rights reserved.",
              font=("Arial", 9) ).grid(
            row=5, column=0, columnspan=2, pady=(30, 0))

    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        if not username or not password:
            messagebox.showwarning("Login Failed", "Please enter both username and password.")
            return
        messagebox.showinfo("Success", f"Logged in as {username}!")
        print(f"[DEBUG] Login: {username}")

    def sign_up(self):
        messagebox.showinfo("Sign Up", "Sign-up feature coming soon!")
        print("[DEBUG] Sign-up clicked")


def main():
    root = Tk()
    app = SimpleyServeApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
