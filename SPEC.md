# Specification: Terminal Habit Tracker (Python MVC)

## 1. Architecture
* **Model (`models.py`):** Handles SQLite3 database connections and data logic.
* **View (`views.py`):** Handles terminal output, ASCII formatting, and rendering menus.
* **Controller (`controllers.py`):** Handles the main application loop and user input routing.

## 2. Database Schema (SQLite3)
Table: `habits`
Columns: `id` (INTEGER PK), `name` (TEXT), `is_done` (BOOLEAN), `streak` (INTEGER)