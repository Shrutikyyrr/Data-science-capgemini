# Section 8 – Docker + Deployment

## Build and Run with Docker

```bash
# Build image
docker build -t student-api .

# Run container
docker run -p 8000:8000 student-api

# Run with custom env variables
docker run -p 8000:8000 -e APP_ENV=staging -e APP_VERSION=2.0.0 student-api
```

## Run with Docker Compose
```bash
docker-compose up --build
```

## Test it
```
GET http://localhost:8000/
GET http://localhost:8000/health
GET http://localhost:8000/students
```

---

## Environment Variables vs Virtual Environment vs Docker

### Environment Variables
- Key-value pairs passed to the app at runtime
- Used for secrets, config (DB URL, API keys, port)
- Set with `-e KEY=VALUE` in Docker or in `.env` file
- App reads them via `os.getenv("KEY", "default")`

### Virtual Environment (venv)
- Isolates Python packages per project on your local machine
- Prevents version conflicts between projects
- Only exists on your machine — not portable
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

### Docker
- Packages the entire app + OS + runtime + dependencies into one container
- Runs identically on any machine — "works on my machine" problem solved
- Portable, scalable, production-ready
- Heavier than venv but much more reliable for deployment

| Feature | venv | Docker |
|---------|------|--------|
| Isolation | Python packages only | Full OS + app |
| Portability | No | Yes |
| Production use | No | Yes |
| Setup complexity | Low | Medium |
