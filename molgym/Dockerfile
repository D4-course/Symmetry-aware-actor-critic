FROM python:3.8

WORKDIR /d4
COPY . /d4

RUN pip install torch-scatter==2.0.5 -f https://data.pyg.org/whl/torch-1.5.0+cu102.html

RUN pip --default-timeout=1000 install torch==1.5.1

RUN pip --default-timeout=1000 install -r requirements.txt

RUN pip install scine-sparrow

RUN pip install -e .

RUN pip install unicorn

RUN pip install fastapi uvicorn

RUN chmod +x /d4/entrypoint.sh

ENTRYPOINT /d4/entrypoint.sh
