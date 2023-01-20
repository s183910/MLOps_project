# Base image
FROM python:3.9-slim

# install python
RUN apt update && \
    apt install --no-install-recommends -y build-essential gcc && \
    apt clean && rm -rf /var/lib/apt/lists/*


COPY requirements.txt requirements.txt
COPY setup.py setup.py
COPY src/ src/

WORKDIR /
RUN mkdir models
RUN mkdir data
RUN mkdir .dvc
COPY .dvc/config /.dvc/config

RUN pip install -r requirements.txt --no-cache-dir
RUN pip install -U "dvc[gs]"
RUN dvc pull

ENTRYPOINT ["python", "-u", "src/models/train_model.py"]
