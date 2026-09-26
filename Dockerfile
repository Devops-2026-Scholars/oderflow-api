# Stage 1: Build Dependencies 
FROM python:3.11-slim AS builder 
WORKDIR /app 
RUN apt-get update && apt-get install -y --no-install-recommends gcc libpq-dev && rm -rf /var/lib/ apt/lists/* 
COPY requirements.txt . 
RUN pip install --user --no-cache-dir -r requirements.txt 

# Stage 2: Hardened Runtime 
FROM python:3.11-slim AS runner 
WORKDIR /app 

# Create non-root system user 
RUN addgroup --system appgroup && adduser --system --group appuser 

COPY --from=builder /root/.local /home/appuser/.local 
COPY app/ ./app/ 

ENV PATH=/home/appuser/.local/bin:$PATH     PYTHONUNBUFFERED=1 

USER appuser 
EXPOSE 8000 

HEALTHCHECK --interval=30s --timeout=3s --retries=3   CMD curl -f http://localhost:8000/health || exit 1 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]