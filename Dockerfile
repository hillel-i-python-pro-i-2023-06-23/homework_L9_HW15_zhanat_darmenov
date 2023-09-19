
FROM python:3.11-slim

# Define environment variables
ENV PYTHONUNBUFFERED=1
ARG WORKDIR=/wd
ARG USER=user

# Set the working directory
WORKDIR ${WORKDIR}

# Create a system user and set permissions for the working directory
RUN useradd --system ${USER} && \
    chown --recursive ${USER} ${WORKDIR}

# Add the following lines to set permissions for the /wd/db directory
# RUN mkdir -p ${WORKDIR}/db && \
# RUN chown -R ${USER} ${WORKDIR} && \
#    chmod -R 755 ${WORKDIR}

# Install necessary system packages
RUN apt update && apt upgrade -y
RUN apt install -y curl

# Copy and install Python dependencies
COPY --chown=${USER} requirements.txt requirements.txt

RUN pip install --upgrade pip && \
    pip install --requirement requirements.txt

# Copy your application files
COPY --chown=${USER} . ./

# Set the user for running the application
USER ${USER}

# Set the Database Volume
# VOLUME ${WORKDIR}

# Define the entry point for your application
# ENTRYPOINT ["python", "main.py"]
ENTRYPOINT ["flask", "run", "--host=0.0.0.0", "--port=45000"]