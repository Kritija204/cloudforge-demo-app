from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime, timezone
import os, socket

app = FastAPI(title="CloudForge Demo App", version="1.0.0")

@app.get("/", response_class=HTMLResponse)
def home():
    return """<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>CloudForge Demo</title>
<style>
*{box-sizing:border-box}body{margin:0;background:#090d17;color:#f4f6ff;font:16px/1.6 system-ui,Segoe UI,sans-serif}.wrap{max-width:1000px;margin:auto;padding:28px 22px}.top{display:flex;justify-content:space-between;align-items:center}.brand{font-weight:800;font-size:1.2rem}.pill{color:#83f0c2;border:1px solid #285c4a;background:#103327;padding:6px 12px;border-radius:30px;font-size:.8rem}.hero{padding:80px 0 48px}.eyebrow{color:#a89cff;text-transform:uppercase;letter-spacing:.16em;font-weight:800;font-size:.8rem}h1{font-size:clamp(2.8rem,7vw,5rem);line-height:1.04;letter-spacing:-.05em;margin:16px 0}.gradient{background:linear-gradient(90deg,#b8aaff,#7be9c0);color:transparent;background-clip:text}.lead{color:#a4b0c8;max-width:680px;font-size:1.1rem}.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}.card{padding:22px;border:1px solid #27334a;border-radius:17px;background:linear-gradient(145deg,#151d2d,#0e1420)}.card h2{font-size:1.05rem}.card p{color:#a4b0c8;font-size:.93rem}.checks{margin-top:38px;display:grid;grid-template-columns:repeat(2,1fr);gap:12px}.check{padding:14px;border:1px solid #27334a;border-radius:12px;color:#dce4f5}.check b{color:#58dfaa;margin-right:8px}a{color:#c3baff}.footer{border-top:1px solid #27334a;margin-top:44px;padding-top:20px;color:#9aa8c2;font-size:.85rem}@media(max-width:650px){.grid,.checks{grid-template-columns:1fr}.hero{padding-top:50px}}
</style></head><body><main class="wrap"><header class="top"><div class="brand">✦ CloudForge Demo</div><span class="pill">● Live app response</span></header><section class="hero"><div class="eyebrow">Deployment proof of concept</div><h1>From GitHub to <span class="gradient">running software.</span></h1><p class="lead">A container-ready demo that validates the CloudForge pipeline: repository cloning, Docker image building, container startup, and HTTP health checks.</p><p><a href="/health">Check health endpoint ↗</a> &nbsp;·&nbsp; <a href="/api/info">View runtime info ↗</a></p></section><section class="grid"><article class="card"><div>📦</div><h2>Container-ready</h2><p>Includes a Dockerfile and pinned Python dependencies for repeatable builds.</p></article><article class="card"><div>⚡</div><h2>Health endpoint</h2><p>A simple route confirms that the deployed service is responding.</p></article><article class="card"><div>🔎</div><h2>Runtime visibility</h2><p>Inspect the container hostname and server time using a JSON endpoint.</p></article></section><section class="checks"><div class="check"><b>✓</b>Git repository can be cloned</div><div class="check"><b>✓</b>Docker image can be built</div><div class="check"><b>✓</b>Container can start on port 8000</div><div class="check"><b>✓</b>HTTP routes return responses</div></section><footer class="footer">Built as a demonstration project for the CloudForge deployment platform.</footer></main></body></html>"""

@app.get("/health")
def health():
    return {"status":"ok","service":"cloudforge-demo","timestamp":datetime.now(timezone.utc).isoformat()}

@app.get("/api/info")
def info():
    return {"app":"CloudForge Demo","version":"1.0.0","status":"running","hostname":socket.gethostname(),"port":int(os.getenv("PORT","8000")),"timestamp_utc":datetime.now(timezone.utc).isoformat()}
