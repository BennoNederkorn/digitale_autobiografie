# digitale_autobiografie

### create virtual environment on Raspberry Pi OS
python3 -m venv --system-site-packages erzaehlomat
source ./erzaehlomat/bin/activate

### installation on Linux
sudo apt-get install portaudio19-dev
pip install -r requirements.txt --timeout=120
curl -fsSL https://ollama.com/install.sh | sh
maybe not needed: sudo apt-get install python3-rpi.gpiovi

### start the programm
sudo python3 script/controller.py

### UI
change wayland to X11 inside the Raspberry Pi Software Configuration Tool
execute: sudo raspi-config -> Advanced Options -> switch from Wayland to X11

### AI
ollama create generate_question -f ./ollama/generate_question/models/Modelfile
ollama create profile -f ./ollama/generate_question/models/Modelfile