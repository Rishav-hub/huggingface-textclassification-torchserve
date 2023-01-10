FROM pytorch/torchserve:latest
# copy model archive
USER root
COPY serving/ /serving/
# WORKDIR /home/model-server/model-store/
RUN apt update -y && apt install awscli -y && apt-get update && pip install --upgrade pip
RUN pip3 install transformers==4.6.0
# run Torchserve upon running the container
WORKDIR /serving/
CMD ["python3", "serve.py"]
# CMD ["torchserve", "--start", "--model-store /home/model-server/model-store/model_store","--models my_model=model.mar" ,"--ts-config config.properties"]