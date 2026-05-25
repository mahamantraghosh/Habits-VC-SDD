import customtkinter as ctk
from models import HabitModel

# --- System Settings for the "Vibe" ---
ctk.set_appearance_mode("dark")  # Forces Dark Mode
ctk.set_default_color_theme("blue")  # Modern blue accents

class HabitApp(ctk.CTk):
    def __init__(self, model):
        super().__init__()
        self.model = model

        # Window Setup
        self.title("HabitForge | Pure Python Enterprise")
        self.geometry("550x700")
        self.resizable(False, False)

        # Header Frame
        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.pack(pady=20, padx=20, fill="x")

        self.title_label = ctk.CTkLabel(
            self.header_frame, 
            text="HabitForge Protocol", 
            font=ctk.CTkFont(size=32, weight="bold")
        )
        self.title_label.pack()

        self.subtitle_label = ctk.CTkLabel(
            self.header_frame, 
            text="Native Python Desktop Edition", 
            font=ctk.CTkFont(size=14), 
            text_color="gray"
        )
        self.subtitle_label.pack()

        # Input Frame
        self.input_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.input_frame.pack(pady=10, padx=20, fill="x")

        self.habit_entry = ctk.CTkEntry(
            self.input_frame, 
            placeholder_text="Initialize new protocol...",
            height=40,
            font=ctk.CTkFont(size=14)
        )
        self.habit_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        
        # Bind the Enter key to the add button
        self.habit_entry.bind("<Return>", lambda event: self.add_habit())

        self.add_btn = ctk.CTkButton(
            self.input_frame, 
            text="Execute", 
            height=40,
            width=100,
            font=ctk.CTkFont(weight="bold"),
            command=self.add_habit
        )
        self.add_btn.pack(side="right")

        # Scrollable List Frame
        self.scrollable_frame = ctk.CTkScrollableFrame(self, corner_radius=15)
        self.scrollable_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Initial Render
        self.refresh_ui()

    def refresh_ui(self):
        # Clear existing items in the scrollable frame
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        # Fetch fresh data from SQLite Database
        habits = self.model.get_all_habits()

        if not habits:
            empty_label = ctk.CTkLabel(
                self.scrollable_frame, 
                text="No active protocols found.", 
                text_color="gray",
                font=ctk.CTkFont(slant="italic")
            )
            empty_label.pack(pady=20)
            return

        # Render each habit
        for h_id, name, is_done, streak in habits:
            row_frame = ctk.CTkFrame(self.scrollable_frame, corner_radius=10)
            row_frame.pack(fill="x", pady=5, padx=5)

            # Left side: Checkbox
            checkbox_var = ctk.IntVar(value=is_done)
            checkbox = ctk.CTkCheckBox(
                row_frame, 
                text=name,
                variable=checkbox_var,
                font=ctk.CTkFont(size=16, overstrike=(is_done == 1)),
                text_color="gray" if is_done else "white",
                command=lambda hid=h_id: self.toggle_habit(hid)
            )
            checkbox.pack(side="left", pady=15, padx=15)

            # Right side: Streak & Delete Button
            if streak > 0:
                streak_label = ctk.CTkLabel(
                    row_frame, 
                    text=f"🔥 {streak}", 
                    text_color="#f97316",
                    font=ctk.CTkFont(weight="bold")
                )
                streak_label.pack(side="left", padx=10)

            delete_btn = ctk.CTkButton(
                row_frame, 
                text="✕", 
                width=30, 
                height=30,
                fg_color="#ef4444", 
                hover_color="#b91c1c",
                command=lambda hid=h_id: self.delete_habit(hid)
            )
            delete_btn.pack(side="right", pady=10, padx=10)

    # --- Controller Actions ---
    def add_habit(self):
        habit_name = self.habit_entry.get().strip()
        if habit_name:
            self.model.add_habit(habit_name)
            self.habit_entry.delete(0, 'end')
            self.refresh_ui()

    def toggle_habit(self, habit_id):
        self.model.toggle_habit(habit_id)
        self.refresh_ui()

    def delete_habit(self, habit_id):
        self.model.delete_habit(habit_id)
        self.refresh_ui()

if __name__ == "__main__":
    # Boot up the Model and pass it to the App
    db_model = HabitModel()
    app = HabitApp(db_model)
    app.mainloop()