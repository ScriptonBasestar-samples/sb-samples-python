Faust kafka
===========

## Install

### Ubuntu20

```bash
pip install pipenv
libgflags-dev
sudo apt-get install libgflags-dev libsnappy-dev zlib1g-dev libbz2-dev liblz4-dev libzstd-dev
apt install librocksdb-dev build-essential
#git clone https://github.com/facebook/rocksdb.git
#cd rocksdb/
#make all
#DEBUG_LEVEL=0 make shared_lib install-shared
#ssibal.. ubuntu error nam

pipenv install
```

### Manjaro

```bash
pip install pipenv
#sudo pacman -S rocksdb
pipenv install
```

## Run

### SetUp

```bash
docker run --rm -d -p 9093:9093 kafka
```

### App

코드 직접 실행은 안된다\
celery처럼. 파라미터를 미리 정의해서 전달하면 되긴되는데\
좀 쨔증나게 실행시켜야함
```bash
faust main worker -l info
```

## REF

~
