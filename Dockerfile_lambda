FROM public.ecr.aws/lambda/python:3.11

RUN pip install --upgrade pip==22.0.4
RUN pip cache purge

# Copy function code
COPY ./src ${LAMBDA_TASK_ROOT}
# Install the function's dependencies using file requirements.txt
# from your project folder.
COPY requirements.txt ${LAMBDA_TASK_ROOT}
# Install the specified packages
RUN pip install -r requirements.txt
# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "api.api.handler" ]