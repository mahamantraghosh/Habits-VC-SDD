import os

class HabitView:
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def show_header():
        print("="*40)
        print(" ENGINEER'S HABIT DASHBOARD v1.0 ".center(40, "="))
        print("="*40)

    @staticmethod
    def show_habits(habits):
        if not habits:
            print("\n[ No active protocols found ]\n")
            return

        print("\nID | STATUS | PROTOCOL | STREAK")
        print("-" * 40)
        for h in habits:
            h_id, name, is_done, streak = h
            status = "[X]" if is_done else "[ ]"
            print(f"{h_id:2} |  {status}   | {name[:15]:<15} | 🔥 {streak}")
        print("-" * 40)

    @staticmethod
    def show_menu():
        print("\nCommands:")
        print("1. Initialize New Protocol (Add)")
        print("2. Execute/Revert Protocol (Toggle)")
        print("3. Terminate Protocol (Delete)")
        print("4. Exit System")
        return input("\nEnter command number: ")

    @staticmethod
    def get_input(prompt):
        return input(prompt)