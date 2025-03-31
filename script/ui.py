import tkinter as tk

# Funktion zum Aktualisieren der Frage
def update_question(new_question):
    question_label.config(text=new_question)

# Hauptfenster erstellen
root = tk.Tk()
root.attributes('-fullscreen', True)  # Vollbild
root.configure(bg='white')  # Hintergrundfarbe Weiß

# Frage als Label
question_label = tk.Label(
    root,
    text="Wie lautet Ihre Lebensgeschichte?",  # Startfrage
    font=("Arial", 36),  # Große Schrift
    bg="white",
    fg="black",
    wraplength=800,
    justify="center"
)
question_label.pack(pady=50)

# Anweisungen als Label
instructions_label = tk.Label(
    root,
    text="Drücken Sie die Leertaste, um fortzufahren.",  # Anweisung
    font=("Arial", 24),
    bg="white",
    fg="black",
    justify="center"
)
instructions_label.pack(pady=20)

# Anweisungen als Label
instructions_label = tk.Label(
    root,
    text="Drücken Sie die Leertaste, um fortzufahren.",  # Anweisung
    font=("Arial", 24),
    bg="white",
    fg="black",
    justify="center"
)
instructions_label.pack(pady=20)

# Escape-Taste zum Beenden
root.bind('<Escape>', lambda e: root.destroy())

# Leertaste für nächste Frage
root.bind('<space>', lambda e: update_question("Was war Ihr schönstes Erlebnis?"))

# Hauptfenster starten
root.mainloop()