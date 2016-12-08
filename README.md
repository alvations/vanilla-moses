# vanillia-moses

Install
====

```
sudo apt-get update
sudo apt-get install g++ git subversion automake libtool zlib1g-dev libboost-all-dev libbz2-dev liblzma-dev python-dev graphviz libgoogle-perftools-dev
sudo apt-get install gcc make
sudo apt-get install python3-dev python3-pip
sudo pip3 install beautifulsoup4

git clone https://github.com/alvations/vanilla-moses.git
cd vanilla-moses
python3 install_moses.py

python3 install_clustercat.py
```

When the above commands ends with the line `this is a small house`, Moses has been installed properly.

Download Data
====

To download WMT open data for specific languages (`cs`, `de`, `fi`, `fr`, `ru`):

```
cd vanilla-moses
nohup python3 get_data.py de &
```

To download all WMT open data:

```
cd vanilla-moses
nohup python3 get_data.py &
```

It'll be downloading 50 GB of data, it might take 4-5 hours depending on Moses' file server.
When finished a directory named `wmt-data` will pop up in your home directory.

Train Model
====



