import os
import audio_recorder
import transcription
import ollama

categories = {
    1: "Kindheit",
    2: "Jugend",
    3: "Familie",
    4: "Arbeit",
    5: "Prägendes",
    6: "Sonstiges"
}

def get_number() -> int:
    while True:
        try:
            selected = int(input("Bitte wähle eine Kategorie (1-6): "))
            if selected in categories:
                return selected
            else:
                print("Ungültige Kategorie. Bitte wähle eine Zahl zwischen 1 und 6.")
        except ValueError:
            print("Ungültige Eingabe. Bitte gib eine Zahl ein.")
    

def main():
    # Define the available categories


    # Initialize recording counts for each category
    recording_counts = {cat: 0 for cat in categories.keys()}

    # Greeting and category selection
    print("Hallo! Welche Geschichten willst Du heute erzählen?")
    for num, name in categories.items():
        print(f"{num}: {name}")

    current_category : int = get_number()

    # Main process loop
    while True:
        current_category_name = categories[current_category]
        print(f"\nAktuelle Kategorie: {current_category} - {current_category_name}")
        print("Optionen:")
        print("  s: Neue Aufnahme starten")
        print("  n: Zur nächsten Kategorie wechseln")
        print("  p: Zur vorherigen Kategorie wechseln")
        print("  q: Programm beenden")
        print("  f: Biographie abschließen")
        
        choice = input("Bitte wähle eine Option: ").strip().lower()

        if choice == 's':
            # Increase the recording count for the current category
            count = recording_counts[current_category] + 1
            
            # Define the recordings folder path
            output_path = os.path.join("C:/Users/marti/Documents/Programmieren/DigitaleAutobiografie/recordings")
            # Ensure the folder exists, if not, create it
            os.makedirs(output_path, exist_ok=True)
            
            # Check if a file with the same name exists and increment count accordingly
            while True:
                output_filename = f"{current_category}_{current_category_name}_{count}"
                file_path = os.path.join(output_path, output_filename + ".wav")
                if not os.path.exists(file_path):
                    break
                count += 1
            
            # Update the count for this category
            recording_counts[current_category] = count
            
            print(f"Aufnahme wird gespeichert als: {output_filename}.wav in {output_path}")
            # Start recording using the audio_recorder module
            audio_recorder.start_recording(output_path, output_filename)
            
        elif choice == 'n':
            if current_category < 6:
                current_category += 1
            else:
                print("Dies ist bereits die höchste Kategorie.")
        elif choice == 'p':
            if current_category > 1:
                current_category -= 1
            else:
                print("Dies ist bereits die niedrigste Kategorie.")
        elif choice == 'q':
            print("Aufzeichnungen gespeichert. Bis bald!")
            break
        
        elif choice == 'f':
            print("Aufzeichnungen abgeschlossen. Vielen Dank für die Geschichten! Deine Biographie wird jetzt erstellt.")
            
            # Transcribe recordings into text files
            recordings_folder = os.path.join("C:/Users/marti/Documents/Programmieren/DigitaleAutobiografie/recordings")
            transcribed_folder = os.path.join("C:/Users/marti/Documents/Programmieren/DigitaleAutobiografie/transcribed_recordings")
            os.makedirs(transcribed_folder, exist_ok=True)

            for file in os.listdir(recordings_folder):
                if file.lower().endswith(".wav"):
                    audio_file_path = os.path.join(recordings_folder, file)
                    base_name = os.path.splitext(file)[0]
                    print(f"Transcribing {file}...")
                    transcription.transcribe_audio(audio_file_path, transcribed_folder, base_name)

            # Merge text files per category into one large chapter text file and store in chapters folder
            chapters_folder = os.path.join("C:/Users/marti/Documents/Programmieren/DigitaleAutobiografie/chapters")
            os.makedirs(chapters_folder, exist_ok=True)

            for category in categories.keys():
                texts = []
                # Collect all text files in transcribed_folder that start with the category name (e.g., "Kindheit")
                for file in os.listdir(transcribed_folder):
                    if file.lower().endswith(".txt") and file.startswith(str(category)):
                        file_path = os.path.join(transcribed_folder, file)
                        with open(file_path, 'r', encoding='utf-8') as f:
                            texts.append(f.read())
                if texts:
                    full_text = "\n".join(texts)
                    chapter_output_path = os.path.join(chapters_folder, f"{category}_chapter.txt")
                    with open(chapter_output_path, 'w', encoding='utf-8') as file:
                        file.write(full_text)
                    print(f"Final chapter for {category} saved as {chapter_output_path}")
            
            #generate the biography using the ollama model
            client = ollama.Client()
            model = "S2C"

            for category in categories.keys():
                chapter_input_path = os.path.join(chapters_folder, f"{category}_chapter.txt")
                
                # Check if the chapter file exists
                if not os.path.exists(chapter_input_path):
                    print(f"Skipping {categories[category]}: Chapter file does not exist.")
                    continue  # Skip to the next category if the file doesn't exist

                with open(chapter_input_path, 'r', encoding='utf-8') as file:
                    chapter_text = file.read()
                    prompt = f"Hier ist das Kapitel über {categories[category]}: {chapter_text}"
                    
                    print(f"Prompt: {prompt}")
                    print(f"Generating response for {categories[category]}...")
                    # Send the query to the model
                    response = client.generate(model=model, prompt=prompt)

                    # Print the response from the model as debugging output
                    print(f"Response from Ollama for {categories[category]}:")
                    print(response.response)

                    # Save the response to a .txt file
                    output_file = os.path.join(chapters_folder, f"{categories[category]}_finalized.txt")
                    with open(output_file, 'w', encoding='utf-8') as file:
                        file.write(response.response)
                    print(f"Response saved to {output_file}")

            # Exit the main loop after processing
            print("Alle Kapitel wurden verarbeitet und gespeichert.")
            print("Das Programm wird jetzt beendet.")
            break
        else:
            print("Ungültige Option. Bitte wähle 's', 'n', 'p', 'q' oder 'f'.")

if __name__ == "__main__":
    main()