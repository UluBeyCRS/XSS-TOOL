git clone https://github.com/UluBeyCRS/XSS-TOOL.git

cd XSS-TOOL

# Kali Linux
sudo apt update

sudo apt install python3 python3-pip -y

pip3 install requests

chmod +x xss_tool.py

python3 xss_tool.py

# Termux
pkg update && pkg upgrade -y

pkg install python -y

pkg install python-pip -y

pip install requests

chmod +x xss_tool.py

python xss_tool.py
