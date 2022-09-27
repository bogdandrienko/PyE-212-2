sudo apt update -y

sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev


rm -R python_app1

mkdir python_app1 && cd python_app1
python3 -m venv env && source env/bin/activate
pip install --upgrade pip
pip install kivy buildozer cython virtualenv
pip freeze > requirements.txt

pip3 install Cython==0.29.19 virtualenv  
export PATH=$PATH:~/.local/bin/

cd .. && cp main.py python_app1 && cd python_app1

buildozer init

buildozer -v android debug
