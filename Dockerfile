FROM python:3.11-slim

WORKDIR /app

# System deps for torch/pillow wheels
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
COPY scripts/ ./scripts/

ENV PYTHONPATH=/app/src
EXPOSE 8000

CMD ["uvicorn", "multimodal_assistant.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
