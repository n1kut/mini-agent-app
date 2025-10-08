from fastapi import FastAPI
app = FastAPI(title="Mini Agent")

# Маршрут HTTP GET /
@app.get("/")
def root():
    # Любой словарь Python автоматически сериализуется в JSON.
    return {"ok": True, "service": "Mini Agent", "lesson": 1}