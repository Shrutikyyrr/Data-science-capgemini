# ── Stage 1: Base image ───────────────────────────────────────────────────────
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy and install dependencies first (layer caching — faster rebuilds)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# ── Environment Variables (can be overridden at runtime with -e flag) ─────────
ENV APP_ENV=production
ENV APP_VERSION=1.0.0
ENV PORT=8000

# Run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
