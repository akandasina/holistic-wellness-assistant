import time

def breathing_exercise():
    print("Let's begin a short guided breathing exercise.")
    
    for _ in range(3):
        print("Breathe in... (4 seconds)")
        time.sleep(4)
        print("Hold... (4 seconds)")
        time.sleep(4)
        print("Breathe out... (6 seconds)")
        time.sleep(6)
    
    print("Well done! How do you feel now?")
  
if __name__ == "__main__":
    breathing_exercise()
