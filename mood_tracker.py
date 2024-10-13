import tkinter as tk
from tkinter import messagebox, font
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from collections import Counter

# Mapping moods to values for graphing
mood_mapping = {
    "happy": 1, "sad": 0, "stressed": -1, 
    "excited": 2, "tired": -2, "anxious": -3,
    "lonely": -4, "frustrated": -5, "content": 3, "bored": -6
}

# Function for breathing exercises
def breathing_exercise():
    messagebox.showinfo("Breathing Exercise", "Let's begin a short guided breathing exercise.")
    root.after(1000, lambda: messagebox.showinfo("Breathe in", "Breathe in... (4 seconds)"))
    root.after(5000, lambda: messagebox.showinfo("Hold", "Hold... (4 seconds)"))
    root.after(9000, lambda: messagebox.showinfo("Breathe out", "Breathe out... (6 seconds)"))
    root.after(15000, lambda: messagebox.showinfo("Breathing Exercise", "Well done!"))

# Function to give wellness advice based on mood
def give_wellness_advice(mood):
    wellness_plan = {
        "happy": ["Share your joy or practice gratitude journaling.", "Try an energizing workout."],
        "sad": ["Listen to calming music or take a walk.", "Journal about one positive thing today."],
        "stressed": ["Take a break to breathe or stretch.", "Try progressive muscle relaxation."],
        "excited": ["Channel energy into a project or workout.", "Set goals to capitalize on excitement!"],
        "tired": ["Consider a short nap or gentle yoga.", "Rest is productive."],
        "anxious": ["Use grounding techniques like 5-4-3-2-1.", "Reframe anxious thoughts."],
        "lonely": ["Reach out to a friend or join an online group.", "Appreciate your positive qualities."],
        "frustrated": ["Engage in a creative outlet or workout.", "Focus on what you can control."],
        "content": ["Savor the moment—reflect on successes.", "Enjoy a relaxing activity."],
        "bored": ["Try something new like a hobby or recipe.", "Engage in a fun physical activity!"]
    }
    return wellness_plan.get(mood.lower(), ["Stay positive and take care!"])

# Function to track mood and offer wellness advice
def track_mood(mood):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('mood_log.txt', 'a') as f:
        f.write(f"{current_time} - {mood}\n")
    messagebox.showinfo("Mood Recorded", "Your mood has been recorded.")
    advice = give_wellness_advice(mood)
    advice_str = "\n".join(advice)
    messagebox.showinfo("Wellness Advice", f"Wellness advice:\n{advice_str}")
    if mood.lower() in ["stressed", "anxious", "frustrated"]:
        breathing_exercise()

# Function to visualize mood trends
def visualize_mood_trends():
    dates = []
    moods = []
    try:
        with open('mood_log.txt', 'r') as f:
            for line in f:
                date, mood = line.strip().split(' - ')
                dates.append(datetime.strptime(date, '%Y-%m-%d %H:%M:%S'))
                moods.append(mood)
        mood_values = [mood_mapping.get(mood.lower(), 0) for mood in moods]
        plt.figure(figsize=(10, 5))
        plt.plot(dates, mood_values, marker='o', linestyle='-', color='b', label='Mood Over Time')
        plt.xlabel('Date')
        plt.ylabel('Mood')
        plt.title('Mood Trends Over Time')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.yticks([-6, -5, -4, -3, -2, -1, 0, 1, 2, 3], 
                   ['Bored', 'Frustrated', 'Lonely', 'Anxious', 'Tired', 'Stressed', 'Sad', 'Happy', 'Excited', 'Content'])
        plt.legend()
        plt.tight_layout()
        plt.show()
    except FileNotFoundError:
        messagebox.showerror("Error", "No mood log found. Please record some moods first.")

# Function to show a weekly mood summary
def show_weekly_summary():
    moods = []
    today = datetime.now()
    one_week_ago = today - timedelta(days=7)
    try:
        with open('mood_log.txt', 'r') as f:
            for line in f:
                date, mood = line.strip().split(' - ')
                mood_date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
                if mood_date >= one_week_ago:
                    moods.append(mood)
        if moods:
            common_mood = Counter(moods).most_common(1)[0][0]
            messagebox.showinfo("Weekly Mood Summary", f"Your most common mood in the past week is: {common_mood}")
        else:
            messagebox.showinfo("Weekly Mood Summary", "No moods recorded in the past week.")
    except FileNotFoundError:
        messagebox.showerror("Error", "No mood log found. Please record some moods first.")

# GUI Setup
def submit_mood():
    mood = mood_var.get()
    if mood:
        track_mood(mood)
    else:
        messagebox.showerror("Error", "Please select a mood.")

# Create the main window
root = tk.Tk()
root.title("Holistic Wellness Assistant")
root.geometry('400x500')
root.configure(bg="#f0f8ff")

# Customize font
header_font = font.Font(family="Helvetica", size=16, weight="bold")
label_font = font.Font(family="Arial", size=12)

# Add a label and radio buttons for mood selection
tk.Label(root, text="How are you feeling today?", font=header_font, bg="#f0f8ff").pack(pady=10)
mood_var = tk.StringVar(value="")  # No button selected initially

# Add radio buttons for moods
for mood in ["Happy", "Sad", "Stressed", "Excited", "Tired", "Anxious", "Lonely", "Frustrated", "Content", "Bored"]:
    tk.Radiobutton(root, text=mood, variable=mood_var, value=mood.lower(), font=label_font, bg="#f0f8ff").pack(anchor=tk.W, padx=20)

# Add Submit button
submit_button = tk.Button(root, text="Submit Mood", command=submit_mood, font=label_font, bg="#87ceeb")
submit_button.pack(pady=10)

# Add button to visualize mood trends
visualize_button = tk.Button(root, text="Visualize Mood Trends", command=visualize_mood_trends, font=label_font, bg="#87ceeb")
visualize_button.pack(pady=10)

# Add button to show weekly summary
summary_button = tk.Button(root, text="Show Weekly Summary", command=show_weekly_summary, font=label_font, bg="#87ceeb")
summary_button.pack(pady=10)

# Run the GUI loop
root.mainloop()
