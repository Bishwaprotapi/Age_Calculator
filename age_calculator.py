import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import sys
import os

class AgeCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Age Calculator")
        self.root.geometry("500x400")
        self.root.configure(bg="#2C3E50")
        self.root.resizable(False, False)

        # Create and pack widgets
        self.create_widgets()

    def create_widgets(self):
        # Main Container
        main_frame = tk.Frame(self.root, bg="#2C3E50", padx=20, pady=20)
        main_frame.pack(expand=True, fill="both")

        # Title Label with decorative line
        title_frame = tk.Frame(main_frame, bg="#2C3E50")
        title_frame.pack(fill="x", pady=(0, 20))

        title_label = tk.Label(
            title_frame,
            text="Age Calculator",
            font=("Helvetica", 24, "bold"),
            bg="#2C3E50",
            fg="#ECF0F1"
        )
        title_label.pack()

        # Decorative line
        separator = ttk.Separator(main_frame, orient='horizontal')
        separator.pack(fill='x', pady=(0, 20))

        # Input Container
        input_frame = tk.Frame(main_frame, bg="#34495E", padx=30, pady=20)
        input_frame.pack(fill="x", padx=20)

        # Birth Date Label and Entry
        date_label = tk.Label(
            input_frame,
            text="Enter Birth Date (DD/MM/YYYY)",
            bg="#34495E",
            fg="#ECF0F1",
            font=("Helvetica", 12)
        )
        date_label.pack()
        
        # Style the entry widget
        self.birth_date_entry = tk.Entry(
            input_frame,
            font=("Helvetica", 14),
            width=15,
            justify='center',
            bg="#ECF0F1",
            fg="#2C3E50",
            insertbackground="#2C3E50"
        )
        self.birth_date_entry.pack(pady=10)

        # Calculate Button with hover effect
        self.calculate_button = tk.Button(
            main_frame,
            text="Calculate Age",
            command=self.calculate_age,
            font=("Helvetica", 12, "bold"),
            bg="#3498DB",
            fg="white",
            padx=30,
            pady=10,
            border=0,
            cursor="hand2"
        )
        self.calculate_button.pack(pady=20)
        self.bind_hover_events()

        # Result Frame
        result_frame = tk.Frame(main_frame, bg="#34495E", padx=20, pady=15)
        result_frame.pack(fill="x", padx=20)

        self.result_label = tk.Label(
            result_frame,
            text="Your age will appear here",
            font=("Helvetica", 12),
            bg="#34495E",
            fg="#ECF0F1",
            wraplength=400
        )
        self.result_label.pack()

    def bind_hover_events(self):
        self.calculate_button.bind("<Enter>", self.on_enter)
        self.calculate_button.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self.calculate_button.config(bg="#2980B9")

    def on_leave(self, e):
        self.calculate_button.config(bg="#3498DB")

    def calculate_age(self):
        try:
            birth_date = self.birth_date_entry.get()
            birth_date = datetime.strptime(birth_date, "%d/%m/%Y")
            today = datetime.now()
            
            age = today.year - birth_date.year - (
                (today.month, today.day) < (birth_date.month, birth_date.day)
            )
            
            months = today.month - birth_date.month
            if months < 0:
                months += 12
            
            days = today.day - birth_date.day
            if days < 0:
                days += 30
                
            result_text = f"""
Age: {age} Years, {months} Months, {days} Days
Born: {birth_date.strftime('%d %B %Y')}
Today: {today.strftime('%d %B %Y')}
            """
            self.result_label.config(text=result_text)
            
        except ValueError:
            messagebox.showerror(
                "Invalid Date",
                "Please enter date in correct format (DD/MM/YYYY)"
            )

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = AgeCalculator(root)
    root.mainloop() 