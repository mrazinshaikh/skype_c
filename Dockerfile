FROM ubuntu:20.04

WORKDIR /var/www/html

COPY . /var/www/html/

RUN apt-get update

RUN apt-get install -y pip \
    python \ 
    python3.8-venv

RUN python3 -m venv venv

# RUN source venv/bin/activate
RUN /bin/bash -c "source /var/www/html/venv/bin/activate"    

RUN pip3 install -r requirements.txt

ENTRYPOINT ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]


EXPOSE 8000