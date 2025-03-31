import tkinter as tk

# Funktion zum Aktualisieren der Frage
def update_question(new_question):
    question_label.config(text=new_question)

# Hauptfenster erstellen
root = tk.Tk()
root.attributes('-fullscreen', True)  # Vollbild
root.configure(bg='beige')  # Hintergrundfarbe Weiß

# Rahmen für Start und Stopp
instructions_frame_recording = tk.Frame(
    root,
    bg="white",
    bd=2,
    relief="groove"
)
instructions_frame_recording.place(relx=0.2, rely=0.5, anchor="center", width=600, height=300)

#Rahmen für Beenden

instructions_frame_quit = tk.Frame(
    root,
    bg="white",
    bd=2,
    relief="groove"
)
instructions_frame_quit.place(relx=0.5, rely=0.8, anchor="center", width=600, height=100)


# Rahmen für die Anweisungen
instructions_frame_move = tk.Frame(
    root,
    bg="white",
    bd=2,
    relief="groove"
)
instructions_frame_move.place(relx=0.8, rely=0.5, anchor="center", width=600, height=300)



# Frage als Label
question_label = tk.Label(
    root,
    text="Hallo! Das ist der Erzählomat",  # Startfrage
    font=("Arial", 40),  # Große Schrift
    bg="beige",
    fg="black",
    wraplength=800,
    justify="center"
)
question_label.place(relx=0.5, rely=0.2, anchor="center")

# Anweisungen als Label
start_label = tk.Label(
    root,
    text="Drücken Sie Start, um Ihre Geschichte aufzunehmen.",  # Anweisung
    font=("Arial", 24),
    bg="white",
    fg="black",
    justify="center",
    wraplength=500
)
start_label.place(relx=0.2, rely=0.4, anchor="center")

# Anweisungen als Label
stop_label = tk.Label(
    root,
    text="Drücken Sie Stop, um die Aufnahme zu beenden.",  # Anweisung
    font=("Arial", 24),
    bg="white",
    fg="black",
    justify="center",
    wraplength=500
)
stop_label.place(relx=0.2, rely=0.6, anchor="center")

next_label = tk.Label(
    root,
    text="Drücken Sie Nächste Frage, um zur nächsten Frage zu gelangen.",  # Anweisung
    font=("Arial", 24),
    bg="white",
    fg="black",
    justify="center",
    wraplength=500
)
next_label.place(relx=0.8, rely=0.6, anchor="center")

previous_label = tk.Label(
    root,
    text="Drücken Sie Vorherige Frage, um zur vorherigen Frage zu gelangen.",  # Anweisung
    font=("Arial", 24),
    bg="white",
    fg="black",
    justify="center",
    wraplength=500
)
previous_label.place(relx=0.8, rely=0.4, anchor="center")

quit_label = tk.Label(
    root,
    text="Drücken Sie Ausschalten, um wann anders weiterzumachen.",  # Anweisung
    font=("Arial", 24),
    bg="white",
    fg="black",
    justify="center",
    wraplength=500
)
quit_label.place(relx=0.5, rely=0.8, anchor="center")

# Escape-Taste zum Beenden
root.bind('<Escape>', lambda e: root.destroy())

# Leertaste für nächste Frage
root.bind('<space>', lambda e: update_question("Was war Ihr schönstes Erlebnis?"))

# Hauptfenster starten
root.mainloop()