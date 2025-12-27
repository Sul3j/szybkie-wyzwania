FROM mcr.microsoft.com/dotnet/sdk:8.0-alpine

WORKDIR /sandbox

RUN dotnet tool install -g dotnet-script

ENV PATH="${PATH}:/root/.dotnet/tools"

COPY runner.cs /sandbox/runner.cs

RUN adduser -D sandbox && chown -R sandbox:sandbox /sandbox

CMD ["dotnet", "script", "/sandbox/runner.cs"]
