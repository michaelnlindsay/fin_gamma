FROM ubuntu:latest

ENV PATH=/opt/conda/bin:$PATH

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

RUN apt-get update && \
    apt-get install -y wget && \
    apt-get install -y bzip2 vim && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN wget https://repo.continuum.io/miniconda/Miniconda3-4.5.4-Linux-x86_64.sh -O /tmp/miniconda.sh

RUN /bin/bash /tmp/miniconda.sh -b -p /opt/conda && \
    rm /tmp/miniconda.sh && \
    echo "export PATH=/opt/conda/bin:$PATH" > /etc/profile.d/conda.sh

RUN conda update -y -n base conda

RUN conda env create -f environment.yml

#RUN source activate cta_data_pipeline

