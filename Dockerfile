FROM pytorch/torchserve:latest
# copy model archive
USER root
WORKDIR /serving
COPY serving/ /serving
# WORKDIR /home/model-server/model-store/
RUN apt update -y && apt install awscli -y && apt-get update && pip install --upgrade pip
RUN pip3 install transformers==4.6.0
# run Torchserve upon running the container
CMD ["python3", "serve.py"]
# CMD ["torchserve", "--start", "--model-store /serving/model_store","--models model=model.mar" ,"--ts-config config.properties"]