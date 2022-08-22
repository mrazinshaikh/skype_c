## Setup

### Install python3 or greater

### Create env

```sh
python3 -m venv venv

source venv/bin/activate 
```

### Install dependencies

```sh
pip3 install -r requirements.txt
```

## Usage

### API

Hit POST  `/`  with name and message in request body.

To startup api server in local run `uvicorn app:app --reload` and for production run on `uvicorn app:app --host 0.0.0.0 --port 80`

### Standalone file

To run file as standalone run `python3 main.py NAME --message`

# Docker setup 

## Build docker container

```sh
docker-composer build
```

## Start docker container

```sh
docker-compose up
```

- This will start api server on port 8005 of host machine