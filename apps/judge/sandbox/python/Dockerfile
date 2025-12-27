FROM python:3.11-slim

WORKDIR /sandbox

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir RestrictedPython==6.2

COPY runner.py /sandbox/runner.py

RUN useradd -m -u 1000 sandbox && chown -R sandbox:sandbox /sandbox
USER sandbox

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

CMD ["python", "/sandbox/runner.py"]
