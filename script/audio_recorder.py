import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

# Recording settings
samplerate = 48000 # 44100  # Sample rate in Hz
audio_data = []
recording = False  # Flag to track recording state

def diagnostic_info():
    """Print diagnostic information about the audio input device."""
    default_device = sd.default.device[0]  # Index of the default input device
    device_info = sd.query_devices(default_device)  # Get device details
    print(f"Using audio input device: {device_info['name']}")
    print(f"Sample rate: {device_info['default_samplerate']} Hz")
    print(f"Channels: {device_info['max_input_channels']}")
    print("Press 's' to start recording and 'e' to stop.")

def callback(indata, frames, time, status):
    if status:
        print(status)
    audio_data.append(indata.copy())

def start_recording(output_path, output_filename):
    """Start recording audio and save it to the specified path."""
    global recording, audio_data
    if not recording:
        print("Recording started... Press 'e' to stop.")
        audio_data = []  # Reset data
        recording = True
        try:
            with sd.InputStream(device=4, samplerate=samplerate, channels=1, callback=callback, dtype='int16'):
                print("Press Ctrl+C to stop recording.")
            while True: pass
        except KeyboardInterrupt:
            print("Recording stopped with Ctrl+C.")

        stop_recording(output_path, output_filename)

def stop_recording(output_path, output_filename):
    """Stop recording and save the audio data to a file."""
    global recording
    if recording:
        recording = False
        print("Recording stopped.")

        # Convert list to numpy array and save
        audio_data_np = np.concatenate(audio_data, axis=0)
        filename = f"{output_path}/{output_filename}.wav"
        wav.write(filename, samplerate, audio_data_np)
        print(f"Saved as {filename}")