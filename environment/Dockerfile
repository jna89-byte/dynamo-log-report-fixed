FROM public.ecr.aws/docker/library/python:3.13-slim-bookworm@sha256:01f42367a0a94ad4bc17111776fd66e3500c1d87c15bbd6055b7371d39c124fb

# Bake the verifier's dependencies into the single image, pinned.
# tests/test.sh installs nothing at verify time.
RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

# Pre-create the parent directory of the artifact the agent writes.
RUN mkdir -p /app
WORKDIR /app

# Input data only. Ground truth and the reference solution never enter this image.
COPY data/access.log /app/access.log
