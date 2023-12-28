from joblib import load
import pandas as pd
from datetime import datetime
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
from pydantic import BaseModel
from mangum import Mangum
import pytz

app=FastAPI()
handler = Mangum(app)

# 모델 로드
model_path = "models/model.joblib"
model = load(model_path)

def predict_angles(day, hour, minute, month):
    data = pd.DataFrame([[day, hour, minute, month]], columns=['day', 'hour', 'minute', 'month'])
    angles = model.predict(data)
    angle_h = angles[0][0]
    angle_v = angles[0][1]
    return angle_h, angle_v

def get_time():
    # 한국 시간대로 현재 시간 가져오기
    timestamp = datetime.now(pytz.timezone('Asia/Seoul'))
        # 각 필드 추출 및 소수점 셋째자리까지 반올림
    day = round(timestamp.day / 31, 3)
    hour = round((timestamp.hour - 8) / 11, 3)
    minute = round(timestamp.minute / 60, 3)
    month = round(timestamp.month / 12, 3)
    return timestamp.strftime('%Y-%m-%d %H:%M:%S'), day, hour, minute, month


@app.get('/')
def my_function(tick: int):
    if tick == 1:
        timestamp, day, hour, minute, month = get_time()
        angle_h, angle_v = predict_angles(day, hour, minute, month)
        return JSONResponse({
            "timestamp": timestamp,
            "day": day, "hour": hour, "minute": minute, "month": month,
            "angle_h": angle_h, "angle_v": angle_v
        })

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
