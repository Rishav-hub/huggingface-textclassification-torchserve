FROM pytorch/torchserve:latest

# install dependencies
RUN pip3 install transformers==4.6.0

# copy model archive
COPY model_store/ /home/model-server/model-store/

# WORKDIR /home/model-server/model-store/

# run Torchserve upon running the container
CMD ["torchserve", "--start", "--model-store /home/model-server/model-store/","--models my_model=BERTTokenClassification.mar" ,"--ts-config config.properties"]