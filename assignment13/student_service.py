from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import httpx
import requests
import os
import folium
from dotenv import load_dotenv
from fastapi.responses import HTMLResponse
load_dotenv()
SERVICE_REGISTRY_URL = os.getenv("SERVICE_REGISTRY_URL", "http://127.0.0.1:9000")
app = FastAPI(title="Weather Map API")
DEFALUT_CITY = os.getenv("CITY")
API_KEY = os.getenv("OWM_API_KEY")
STUDENT_NAME = os.getenv("STUDENT_NAME")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.get("/weather_map/{city}", response_class=HTMLResponse)
def weather_map(city: str):
    if not API_KEY:
        raise HTTPException(status_code=500, detail="API Key not found")

    # เรียก API
    params = {"q": city, "appid": API_KEY, "units": "metric", "lang": "th"}
    response = requests.get(BASE_URL, params=params)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="City not found")

    data = response.json()
    lat = data["coord"]["lat"]
    lon = data["coord"]["lon"]
    weather_desc = data["weather"][0]["description"]
    temp = data["main"]["temp"]

    # สร้าง Folium Map
    m = folium.Map(location=[lat, lon], zoom_start=10)
    folium.Marker([lat, lon],
                  popup=f"{city}: {weather_desc}, {temp}°C",
                  tooltip=f"{city} info:").add_to(m)

    # คืนค่า HTML เต็ม
    return HTMLResponse(content=m.get_root().render())

@app.get("/aggregate_map", response_class=HTMLResponse)
async def aggregate_map():
    """
    ดึง weather จากทุก service แล้วสร้างแผนที่ Folium รวม
    """
    async with httpx.AsyncClient(timeout=5.0) as client:
        try:
            response = await client.get(f"{SERVICE_REGISTRY_URL}/services")
            response.raise_for_status()
            services = response.json()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Service Registry Error: {e}")

        # สร้างแผนที่เริ่มต้น (ตรงกลางประเทศไทย)
        m = folium.Map(location=[13.75, 100.5], zoom_start=6)
        added = False

        for service_name, service in services.items():
            url = service["url"]
            try:
                r = await client.get(f"{url}/weather")
                r.raise_for_status()
                data = r.json()

                city = data.get("city", service_name)
                lat = data.get("lat")
                lon = data.get("lon")
                temp = data.get("temperature")
                condition = data.get("condition")

                if lat and lon:
                    folium.Marker(
                        location=[lat, lon],
                        popup=f"{city}: {condition}, {temp}°C",
                        tooltip=city,
                        icon=folium.Icon(color="blue", icon="cloud")
                    ).add_to(m)
                    added = True
            except Exception as e:
                print(f"Error calling {url}/weather: {e}")

        if not added:
            folium.Marker(
                location=[13.75, 100.5],
                popup="No weather data found",
                icon=folium.Icon(color="red", icon="exclamation-sign")
            ).add_to(m)

        return m.get_root().render()
@app.post("/register_self")
async def register_self():
    service_info = {
        "name": STUDENT_NAME,
        "url": SERVICE_REGISTRY_URL,
        "city": DEFALUT_CITY
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{SERVICE_REGISTRY_URL}/register", json=service_info)
        return response.json()

@app.put("/update_self")
async def update_self():
    service_info = {
        "name": STUDENT_NAME,
        "url": SERVICE_REGISTRY_URL,
        "city": DEFALUT_CITY
    }
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{SERVICE_REGISTRY_URL}/update", json=service_info)
        return response.json()

@app.delete("/unregister_self")
async def unregister_self():
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{SERVICE_REGISTRY_URL}/unregister/{STUDENT_NAME}")
        return response.json()