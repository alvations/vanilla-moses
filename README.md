# vanillia-moses

Install
====

```
sudo apt-get install g++ git subversion automake libtool zlib1g-dev libboost-all-dev libbz2-dev liblzma-dev python-dev graphviz libgoogle-perftools-dev
git clone https://github.com/alvations/vanilla-moses.git
cd vanilla-moses
python3 install_moses.py
```

Download Data
====

```
cd vanilla-moses
nohup python3 get_data.py &
```

Train Model
====

