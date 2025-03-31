import tkinter as tk
from ui import ErzaehlomatUI

def main():
    # Hauptfenster erstellen
    root = tk.Tk()

    # UI-Instanz erstellen
    ui = ErzaehlomatUI(root)

    # Beispiel: Frage nach 3 Sekunden aktualisieren
    root.after(3000, lambda: ui.update_question("Was war Ihr schönstes Erlebnis?"))
    root.after(5000, lambda: ui.update_question("Was war Ihr nächst schöneres Erlebnis?"))

    # Hauptfenster starten
    root.mainloop()

if __name__ == "__main__":
    main()