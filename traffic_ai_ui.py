import tkinter as tk
import random

def optimize_traffic():
    # Simulated density data from camera feeds
    north_south_queue = random.randint(0, 100)
    east_west_queue = random.randint(0, 100)
    
    if north_south_queue > east_west_queue:
        status_label.config(text=f"North-South Density: {north_south_queue}%\nStatus: GREEN (North-South)", fg="green")
    else:
        status_label.config(text=f"East-West Density: {east_west_queue}%\nStatus: GREEN (East-West)", fg="green")

# Initialize UI
root = tk.Tk()
root.title("Adaptive Traffic Signal AI - Control Panel")
root.geometry("350x200")

tk.Label(root, text="AI Traffic Optimizer", font=("Arial", 14, "bold")).pack(pady=10)
status_label = tk.Label(root, text="System Ready. Waiting for camera feed...", font=("Arial", 11))
status_label.pack(pady=20)

tk.Button(root, text="Run Optimization Cycle", command=optimize_traffic, bg="#0078D7", fg="white").pack()

if __name__ == "__main__":
    root.mainloop()
