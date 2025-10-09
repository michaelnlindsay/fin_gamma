FROM ubuntu:latest

# Add conda library to path
ENV PATH=/opt/conda/bin:$PATH

# Set shell top bash for source command
SHELL ["/bin/bash", "-c"]

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
    echo "export PATH=/opt/conda/bin:$PATH" > /etc/profile.d/conda.sh \

RUN #conda update -y -n base conda

RUN ls -l /app/ && \
    pwd

RUN conda env create -f /app/environment.yml

RUN source activate cta_data_pipeline

