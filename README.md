# CloudForge Demo App

A small container-ready app for demonstrating the CloudForge deployment workflow.

## Endpoints
- `/` — responsive project landing page
- `/health` — health-check JSON
- `/api/info` — runtime information as JSON

## Deploy with CloudForge
1. Push these files to a GitHub repository.
2. Select the repository and `main` branch in CloudForge.
3. Confirm `Dockerfile` is in the repository root.
4. Start the deployment and inspect build logs.
5. When running, open the assigned app URL/port and check `/health`.

## Run locally with Docker
```bash
docker build -t cloudforge-demo .
docker run --rm -p 8000:8000 cloudforge-demo
```
Visit `http://localhost:8000`, `http://localhost:8000/health`, and `http://localhost:8000/api/info`.

## Run without Docker
```bash
python -m pip install -r requirements.txt
python -m uvicorn app:app --host 0.0.0.0 --port 8000
```

## Structure
- `app.py` — FastAPI application
- `Dockerfile` — container build and startup instructions
- `requirements.txt` — pinned Python dependencies
- `.dockerignore` — excludes local files from the build context
