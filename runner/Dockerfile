FROM mrlindsay/ctadp:main

SHELL ["/bin/bash", "-c"]

# Set the working directory
WORKDIR /pipeline

# Copy the current directory contents into the container
COPY . /pipeline

# Activate conda environment
RUN "source activate cta_data_pipeline"

# Specify the command to run the Python script
CMD ["python", "script.py"]