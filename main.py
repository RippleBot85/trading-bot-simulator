from fastapi import FastAPI
import simulate  # Assicura che questo abbia la funzione run_bot()

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Bot attivo!"}

@app.get("/ping")
def ping():
    simulate.run_bot()
    return {"status": "ok", "detail": "Simulazione eseguita"}
