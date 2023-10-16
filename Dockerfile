FROM continuumio/miniconda3
RUN conda create -n env python=3.10.12
RUN echo "source activate env" > ~/.bashrc
ENV PATH /opt/conda/envs/env/bin:$PATH
EXPOSE 80
RUN pip install --upgrade pip==23.1.2
RUN pip cache purge 

COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN pip cache purge; exit 0

COPY ./src .
COPY ./setup.py .
COPY ./.env .

ENTRYPOINT ["hypercorn", "main:app", "-b", "0.0.0.0:80", "--worker-class", "trio"]

