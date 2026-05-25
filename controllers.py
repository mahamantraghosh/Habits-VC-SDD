class HabitController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        while True:
            self.view.clear_screen()
            self.view.show_header()
            habits = self.model.get_all_habits()
            self.view.show_habits(habits)
            
            choice = self.view.show_menu()

            if choice == '1':
                name = self.view.get_input("Enter protocol name: ")
                if name:
                    self.model.add_habit(name)
            elif choice == '2':
                try:
                    h_id = int(self.view.get_input("Enter ID to toggle: "))
                    self.model.toggle_habit(h_id)
                except ValueError:
                    pass
            elif choice == '3':
                try:
                    h_id = int(self.view.get_input("Enter ID to delete: "))
                    self.model.delete_habit(h_id)
                except ValueError:
                    pass
            elif choice == '4':
                self.view.clear_screen()
                print("Exiting System. Goodbye.")
                break