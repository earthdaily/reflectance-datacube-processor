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

ARG EDS_API_URL
ARG EDS_AUTH_URL
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG INPUT_JSON_PATH
ARG GATEWAY_STAGE

# Check if .env exists, if it does, copy .env file
# Otherwise, set up environment variable from build arguments
RUN if [ ! -f .env ]; then \
    # cp .env /app/.env; \
    # echo "fic exist"; \
    # else \
    echo "fic doesn't exist"; \
    echo "EDS_API_URL=${EDS_API_URL}" >> .env; \
    echo "valeur EDS_API_URL=${EDS_API_URL}"; \
    echo "EDS_AUTH_URL=${EDS_AUTH_URL}" >> .env; \
    echo "AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}" >> .env; \
    echo "AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}" >> .env; \
    echo "INPUT_JSON_PATH=${INPUT_JSON_PATH}" >> .env; \
    echo "GATEWAY_STAGE=${GATEWAY_STAGE}" >> .env; \
    echo .env; \
    fi

# Intermediate stage to copy .env file if it exists
FROM base AS intermediate

# Copy .env file into the Docker image
COPY .env /app/ || true

# Final stage
FROM base

# Copy files from the intermediate stage
COPY --from=intermediate /app/.env /app/

COPY docker-entrypoint.sh /usr/local/bin/
RUN dos2unix /usr/local/bin/docker-entrypoint.sh
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

RUN chmod 644 api/api.py

ENTRYPOINT ["docker-entrypoint.sh"]