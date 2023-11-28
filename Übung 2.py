import uvicorn
from fastapi import FastAPI
from pyproj import Transformer

app = FastAPI()

lv95 = "EPSG:2056"
wgs84 = "EPSG:4326"

t1 = Transformer.from_crs(wgs84, lv95)
t2 = Transformer.from_crs(lv95, wgs84)

def format_coord(coord):
    # Format the coordinate to show at least 4 decimal places
    return "{:.4f}".format(coord)

@app.get("/wgs84lv95")
async def wgs84lv95(lat: float = 0, lng: float = 0):
    result = t1.transform(lat, lng)
    formatted_result = [format_coord(coord) for coord in result]
    return {"LV95-Koordinaten": formatted_result}

@app.get("/lv95wgs84")
async def lv95wgs84(lat: float = 0, lng: float = 0):
    result = t2.transform(lat, lng)
    formatted_result = [format_coord(coord) for coord in result]
    return {"WGS84-Koordinaten": formatted_result}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)


# http://localhost:8000/wgs84lv95?lat=46.8182&lng=8.2275
# http://localhost:8000/lv95wgs84?lat=2600000&lng=1200000