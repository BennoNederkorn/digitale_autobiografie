# digitale_autobiografie

### create virtual environment
python3 -m venv erzaehlomat
source ./erzaehlomat/bin/activate

### installation on Linux
maybe not needed: sudo apt-get install python3-rpi.gpiovi
curl -fsSL https://ollama.com/install.sh | sh
pip install -r requirements.txt --timeout=120

### start the programm
python3 script/controller.py