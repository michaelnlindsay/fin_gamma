FROM continuumio/miniconda3:4.6.14
ARG GAMMALIB

ENV GAMMALIB='/usr/local/gamma'

COPY . .

RUN conda config --append channels conda-forge

RUN conda config --append channels cta-observatory

RUN conda install --yes ctools


#ENTRYPOINT ["tini", "-g", "--"]

# Run app.py when the container launches
CMD ["python", "./app.py"]


