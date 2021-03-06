```
sudo apt update
```

```
sudo apt install -y postgresql postgresql-contrib
```

```
nano /etc/postgresql/10/main/pg_hba.conf
```
ADD:
```
host    all             all              0.0.0.0/0              md5
host    all             all              ::/0                   md5
```

<!-- 
or maybe:
host all all 0.0.0.0/0 md5 -->

```
nano /etc/postgresql/10/main/postgresql.conf
listen_addresses = '*'
```

`/etc/init.d/postgresql restart`

```
sudo -u postgres psql
```

```
ALTER USER postgres PASSWORD 'newPassword';

```

```
CREATE DATABASE main WITH owner=postgres ENCODING = 'UTF-8' lc_collate = 'en_US.utf8' lc_ctype = 'en_US.utf8' template template0;
```

```
\q
reboot
```


<!-- sudo -i -u postgres -->

<!-- createuser --interactive -->

<!-- createdb admin -->
<!-- # reopen -->

<!-- passwd postgres -->

/etc/init.d/postgresql restart

## Set up and activate python environment

Install latest python:
```

python=python3.9
sudo apt-get install -y software-properties-common
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt-get update --ignore-missing
sudo apt install -y  $python-dev $python-venv
```

Download and install pip (package manager):
```
wget https://bootstrap.pypa.io/get-pip.py
$python get-pip.py
rm get-pip.py
```

Download Project and install requirements:
```
sudo apt update
apt install -y git
git clone https://github.com/pip-install-HSE/TeploEnergoHackathon
cd TeploEnergoHackathon
pip install -r requirements.txt
``` 

Create and activate python environment:
```
$python -m venv venv
source venv/bin/activate
```

## Set up .env variables

Сreate a .env file containing the bot configuration
```..env
DB_HOST = "0.0.0.0"
DB_USERNAME = "Sammy"
DB_PASSWORD = "qwerty123"
DB_PORT = "5432"
DB_NAME = "main_db"
```



