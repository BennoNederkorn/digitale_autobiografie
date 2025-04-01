import tkinter as tk

class ErzaehlomatUI:
    def __init__(self, root):
        self.root = root
        self.root.attributes('-fullscreen', True)  # Vollbild
        self.root.configure(bg='beige')  # Hintergrundfarbe Weiß

        # Rahmen für Start und Stopp
        instructions_frame_recording = tk.Frame(
            root,
            bg="white",
            bd=2,
            relief="groove"
        )
        instructions_frame_recording.place(relx=0.2, rely=0.5, anchor="center", width=600, height=300)

        # Rahmen für Beenden
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
        self.question_label = tk.Label(
            root,
            text="Hallo! Das ist der Erzählomat",  # Startfrage
            font=("Arial", 40),  # Große Schrift
            bg="beige",
            fg="black",
            wraplength=800,
            justify="center"
        )
        self.question_label.place(relx=0.5, rely=0.2, anchor="center")

        # Anweisungen als Label
        start_label = tk.Label(
            root,
            text="Drücken Sie START, um Ihre Geschichte aufzunehmen.",  # Anweisung
            font=("Arial", 24),
            bg="white",
            fg="black",
            justify="center",
            wraplength=500
        )
        start_label.place(relx=0.2, rely=0.425, anchor="center")

        stop_label = tk.Label(
            root,
            text="Drücken Sie STOP, um zu stoppen",  # Anweisung
            font=("Arial", 24),
            bg="white",
            fg="black",
            justify="center",
            wraplength=500
        )
        stop_label.place(relx=0.2, rely=0.575, anchor="center")

        next_label = tk.Label(
            root,
            text="Drücken Sie NÄCHSTE FRAGE, um zur nächsten Frage zu gelangen.",  # Anweisung
            font=("Arial", 24),
            bg="white",
            fg="black",
            justify="center",
            wraplength=600
        )
        next_label.place(relx=0.8, rely=0.575, anchor="center")

        previous_label = tk.Label(
            root,
            text="Drücken Sie VORHERIGE FRAGE, um zur vorherigen Frage zu gelangen.",  # Anweisung
            font=("Arial", 24),
            bg="white",
            fg="black",
            justify="center",
            wraplength=600
        )
        previous_label.place(relx=0.8, rely=0.425, anchor="center")

        quit_label = tk.Label(
            root,
            text="Drücken Sie AUSSCHALTEN, um wann anders weiterzumachen.",  # Anweisung
            font=("Arial", 24),
            bg="white",
            fg="black",
            justify="center",
            wraplength=500
        )
        quit_label.place(relx=0.5, rely=0.8, anchor="center")

        #Currently recording functionality
        self.recording_label = tk.Label(
            root,
            text="Aufnahme läuft...",
            font=("Arial", 24),
            bg="white",
            fg="red",
            justify="center",
            wraplength=500
        )
        # Escape-Taste zum Beenden
        root.bind('<Escape>', lambda e: root.destroy())
    
    def show_frame(self, frame):
        """
        shows Frame if visible.
        If already visible its not shown again.
        """
        frame.place(relx=0.2, rely=0.5, anchor="center")

    def hide_frame(self, frame):
        """
        Hides Frame if visible.
        """
        if frame.winfo_ismapped():
            frame.place_forget()

    # Methode zum Aktualisieren der Frage
    def update_question(self, new_question):
        """
        Updates Label with new question.
        :param new_question: The new question to be displayed. Needs a string.
        :type new_question: str"
        """
        self.question_label.config(text=new_question)