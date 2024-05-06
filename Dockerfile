FROM continuumio/miniconda3:23.10.0-1
EXPOSE 80

RUN pip install --upgrade pip==22.0.4
RUN conda clean --all
RUN pip cache purge

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt
RUN pip cache purge; exit 0
RUN apt-get update && apt-get install -y dos2unix
COPY ./src .

# Check if .env exists, if it does, copy .env file
# Otherwise, set up environment variable from build arguments
RUN if [ -f .env ]; then \
    cp .env /app/.env; \
    else \
    echo "EDS_API_URL=${EDS_API_URL}" >> .env; \
    echo "EDS_AUTH_URL=${EDS_AUTH_URL}" >> .env; \
    echo "AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}" >> .env; \
    echo "AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}" >> .env; \
    echo "INPUT_JSON_PATH=${INPUT_JSON_PATH}" >> .env; \
    echo "GATEWAY_STAGE=${GATEWAY_STAGE}" >> .env; \
    cp .env /app/.env; \
    fi

COPY docker-entrypoint.sh /usr/local/bin/
RUN dos2unix /usr/local/bin/docker-entrypoint.sh
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

RUN chmod 644 api/api.py

ENTRYPOINT ["docker-entrypoint.sh"]