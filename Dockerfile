FROM python:3.11

ENV PYTHONUNBUFFERED=1

ARG WORKDIR=/wd
ARG USER=user

WORKDIR ${WORKDIR}

RUN useradd --system ${USER} && \
    chown --recursive ${USER} ${WORKDIR}

RUN apt update && apt upgrade -y
RUN apt install -y curl

COPY --chown=${USER} requirements.txt requirements.txt

RUN pip install --upgrade pip && \
    pip install --requirement requirements.txt

COPY --chown=${USER} app/main.py main.py
COPY --chown=${USER} app/sqlite_manager.py sqlite_manager.py

USER ${USER}

VOLUME ${WORKDIR}/db

EXPOSE 45000/tcp

ENTRYPOINT ["python", "main.py"]
