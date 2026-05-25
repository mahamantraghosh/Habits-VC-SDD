import streamlit as st
import json
import os

# --- Configuration & Vibe ---
st.set_page_config(page_title="HabitForge Vibe", page_icon="🔥", layout="centered")
st.title("🔥 HabitForge Dashboard")
st.markdown("Vibe your way to consistency. Execute protocols to earn XP.")

DATA_FILE = "vibe_data.json"

# --- Data Management ---
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"xp": 0, "level": 1, "habits": []}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

data = load_data()

# --- Top Stats UI ---
col1, col2, col3 = st.columns(3)
col1.metric("Current Level", f"Lvl {data['level']}")
col2.metric("Total XP", f"{data['xp']} XP")
col3.metric("XP to Next Level", f"{100 - (data['xp'] % 100)}")

st.progress((data['xp'] % 100) / 100, text="Level Progress")
st.divider()

# --- Add New Habit ---
with st.form("add_habit_form", clear_on_submit=True):
    new_habit = st.text_input("Define a new protocol...")
    submitted = st.form_submit_button("Add Protocol")
    if submitted and new_habit:
        data["habits"].append({"text": new_habit, "done": False})
        save_data(data)
        st.rerun()

# --- Habit List ---
st.subheader("Active Protocols")
if not data["habits"]:
    st.info("No active protocols. Add one above!")

for idx, habit in enumerate(data["habits"]):
    colA, colB = st.columns([0.85, 0.15])
    
    with colA:
        # Checkbox for completing tasks
        is_done = st.checkbox(habit["text"], value=habit["done"], key=f"chk_{idx}")
        
        if is_done != habit["done"]:
            habit["done"] = is_done
            if is_done:
                data["xp"] += 25
                data["level"] = (data["xp"] // 100) + 1
                st.balloons() # The Vibe Animation!
                st.toast(f"Protocol complete! +25 XP")
            else:
                data["xp"] = max(0, data["xp"] - 25)
                data["level"] = (data["xp"] // 100) + 1
            save_data(data)
            st.rerun()
            
    with colB:
        # Delete button
        if st.button("❌", key=f"del_{idx}"):
            data["habits"].pop(idx)
            save_data(data)
            st.rerun()