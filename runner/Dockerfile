FROM mrlindsay/ctadp:main

ENV PATH=/opt/conda/bin:$PATH

# Set the working directory
WORKDIR /pipeline

# Copy the current directory contents into the container
COPY . /pipeline


# Specify the command to run the Python script
CMD "init.sh"