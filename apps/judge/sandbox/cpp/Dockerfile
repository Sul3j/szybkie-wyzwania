FROM gcc:11-bullseye

WORKDIR /sandbox

RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -u 1000 sandbox && chown -R sandbox:sandbox /sandbox
USER sandbox

CMD ["/bin/sh"]
