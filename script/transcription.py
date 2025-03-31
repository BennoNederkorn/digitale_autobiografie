from faster_whisper import WhisperModel

def transcribe_audio(audio_file_path, output_path, output_filename):
    model_size = "small"
    model = WhisperModel(model_size, device="cpu", compute_type="float32")

    segments, info = model.transcribe(audio_file_path, beam_size=5, vad_filter=True)
    print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

    output_file_path = f"{output_path}/{output_filename}.txt"

    with open(output_file_path, 'w', encoding='utf-8') as file:
        for segment in segments:
            file.write(f"{segment.text}\n")

    print(f"Transcription saved to {output_file_path}")