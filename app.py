from voice_analyse import VoiceAnalyzer
from input_data import InputParam
from fastapi import FastAPI
import uvicorn

app = FastAPI()
va = VoiceAnalyzer()


@app.post("/voice_analysis")
async def voice_analysis(param: InputParam):  # params: InputParams):
    return va.analyze(uuid=dict(param)['UUID'])


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8006)
