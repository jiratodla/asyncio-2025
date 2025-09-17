from fastapi import FastAPI, HTTPException, BackgroundTasks
import asyncio
import random

app = FastAPI(title="Asynchronous Rocket Launcher")

async def launch_rocket(student_id: str, time_to_target: float):
    print(f"Rocket {student_id} launched! ETA: {time_to_target:.2f} seconds")
    await asyncio.sleep(time_to_target)
    print(f"Rocket {student_id} reached destination after {time_to_target:.2f} seconds")

@app.get("/fire/{student_id}")
async def fire_rocket(student_id: str, background_tasks: BackgroundTasks):
    # ตรวจสอบ student_id ต้องเป็น 10 หลัก และเป็นตัวเลขทั้งหมด
    if len(student_id) != 10 or not student_id.isdigit():
        raise HTTPException(status_code=400, detail="student_id must be 10 digits")

    # สุ่มเวลาจรวดบิน 1-2 วินาที
    time_to_target = random.uniform(1, 2)

    # สร้าง background task ยิง rocket แบบไม่บล็อก
    background_tasks.add_task(launch_rocket, student_id, time_to_target)

    # ส่ง response พร้อมเวลาจรวดบิน
    return {
        "message": f"Rocket {student_id} fired!",
        "time_to_target": round(time_to_target, 2)

    }
