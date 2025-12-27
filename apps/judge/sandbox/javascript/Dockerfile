FROM node:18-alpine

WORKDIR /sandbox

COPY runner.js /sandbox/runner.js

RUN adduser -D sandbox && chown -R sandbox:sandbox /sandbox
USER sandbox

ENV NODE_ENV=production

CMD ["node", "/sandbox/runner.js"]
