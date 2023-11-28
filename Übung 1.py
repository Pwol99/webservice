# Aufgabe 1:
# Schreiben Sie einen Webservice welcher als Eingabe den Gemeindenamen nimmt 
# und als Ausgabe sämtliche Attribute dieser Gemeinde im Datensatz 
# PLZO_CSV_LV95.csv
import uvicorn
from fastapi import FastAPI

app = FastAPI()
d = {}

file = open("PLZO_CSV_LV95.csv", encoding="utf-8")
next(file)

for line in file:
    data = line.strip().split(";")
    ortschaftname = data[0]
    plz = data[1]
    zusatzziffer = data[2]
    gemeindename = data[3] 
    bfsnr = data[4]
    kanton = data[5]
    e_koordinate = data[6]
    n_koordinate = data[7]
    sprache = data[8]  

    d[ortschaftname] = { 
        "ortschaftsname": ortschaftname,
        "plz": plz,
        "zusatzziffer": zusatzziffer,
        "gemeindename": gemeindename,
        "bfsnr": bfsnr,
        "kantonskuerzel": kanton,
        "E": e_koordinate,
        "N": n_koordinate,
        "Sprache": sprache
    }

file.close()

@app.get("/search")
async def search(ortschaftname: str):  
    if ortschaftname in d:
        return d[ortschaftname]
    else:
        return {"error": "not found"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)