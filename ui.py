import tkinter as tk
from tkinter import messagebox
from main import run_all_algorithms
from utils import get_summary
import matplotlib.pyplot as plt

current_results = {}
def show_graph(results):
    if not results:
        messagebox.showwarning("No Data", "Run algorithms first!")
        return

    algos = list(results.keys())
    times = [results[a]["time"] for a in algos]
    comparisons = [results[a]["comparisons"] for a in algos]

    plt.figure()

    plt.subplot(1, 2, 1)
    plt.bar(algos, times)
    plt.title("Time Comparison")
    plt.xlabel("Algorithms")
    plt.ylabel("Execution Time(sec)")

    plt.subplot(1, 2, 2)
    plt.bar(algos, comparisons)
    plt.title("No of Comparisons")
    plt.xlabel("Algorithms")
    plt.ylabel("Comparisons Count")

    plt.tight_layout()
    plt.show()


def run_algorithms():
    global current_results
    text = text_entry.get()
    pattern = pattern_entry.get()
    if not text or not pattern:
        messagebox.showwarning("Input Error", "Enter both text and pattern!")
        return
    results = run_all_algorithms(text, pattern)
    current_results = results
    for box in [naive_box, kmp_box, bm_box, analysis_box]:
        box.config(state="normal")
        box.delete(1.0, tk.END)
    for algo, res in results.items():
        content = (
            f"Matches: {res['matches']}\n"
            f"Comparisons: {res['comparisons']}\n"
            f"Time: {res['time']:.8f} sec\n"
        )
        if algo == "Naive":
            naive_box.insert(tk.END, content)
        elif algo == "KMP":
            kmp_box.insert(tk.END, content)
        else:
            bm_box.insert(tk.END, content)
    
    summary = get_summary(results)

    fastest = ", ".join(summary["fastest"])
    least = ", ".join(summary["least_comparisons"])

    analysis_box.insert(tk.END, f"🏆 Fastest: {fastest}\n\n", "center")
    analysis_box.insert(tk.END, f"🧠 Least Comparisons: {least}\n", "center")
    for box in [naive_box, kmp_box, bm_box, analysis_box]:
        box.config(state="disabled")


root = tk.Tk()
root.title("String Matching Visualizer 🚀")
root.geometry("900x650")
root.configure(bg="#000000")  # Pure black


tk.Label(root, text="String Matching Visualizer",
         font=("Segoe UI", 18, "bold"),
         bg="#000000", fg="#7e7e29").pack(pady=10)


input_frame = tk.Frame(root, bg="#000000")
input_frame.pack()
tk.Label(input_frame, text="Text:", fg="white", bg="#000000").grid(row=0, column=0)
text_entry = tk.Entry(input_frame, width=60, bg="#111111", fg="white")
text_entry.grid(row=0, column=1, padx=10, pady=5)
tk.Label(input_frame, text="Pattern:", fg="white", bg="#000000").grid(row=1, column=0)
pattern_entry = tk.Entry(input_frame, width=60, bg="#111111", fg="white")
pattern_entry.grid(row=1, column=1, padx=10, pady=5)


tk.Button(root, text="Run Comparison",
          command=run_algorithms,
          bg="#7e7e29", fg="black",
          font=("Segoe UI", 11, "bold")).pack(pady=10)


box_frame = tk.Frame(root, bg="#000000")
box_frame.pack(pady=5)
def create_box(title):
    frame = tk.Frame(box_frame, bg="#111111", padx=5, pady=5)
    tk.Label(frame, text=title, bg="#111111", fg="#417a9b", font=("Segoe UI", 12, "bold")).pack()
    text_box = tk.Text(frame,width=25, height=7, bg="#000000", fg="#7e7e29", font=("Consolas", 10))
    text_box.pack()

    return frame, text_box


naive_frame, naive_box = create_box("Naive")
kmp_frame, kmp_box = create_box("KMP")
bm_frame, bm_box = create_box("Boyer-Moore")

naive_frame.grid(row=0, column=0, padx=10)
kmp_frame.grid(row=0, column=1, padx=10)
bm_frame.grid(row=0, column=2, padx=10)

analysis_frame = tk.Frame(root, bg="#111111", padx=5, pady=5)
analysis_frame.pack(pady=5)

tk.Label(analysis_frame, text="📊 Analysis", bg="#111111", fg="#7e7e29",font=("Segoe UI", 13, "bold")).pack()

analysis_box = tk.Text(analysis_frame, width=85, height=10, bg="#000000", fg="#417a9b", font=("Consolas", 11))
analysis_box.pack(pady=5)

tk.Button(analysis_frame, text="Show Graph 📊", command=lambda: show_graph(current_results), bg="#0080ff", fg="white", font=("Segoe UI", 10, "bold")).pack(pady=5)


root.mainloop()
