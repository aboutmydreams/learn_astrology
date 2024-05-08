import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part, FinishReason
import vertexai.preview.generative_models as generative_models

# pip install --upgrade google-cloud-aiplatform
# gcloud auth application-default login
def generate():
  vertexai.init(project="celestial-shore-422306-h9", location="us-central1")
  model = GenerativeModel("gemini-1.5-pro-preview-0409")
  responses = model.generate_content(
      [image1, text1],
      generation_config=generation_config,
      safety_settings=safety_settings,
      stream=True,
  )

  for response in responses:
    print(response.text, end="")

image1 = Part.from_data(
    mime_type="image/jpeg",
    data=base64.b64decode("""iVBOR"""))
text1 = """帮我写一段 python 代码，利用下面的 md 表格数据绘制出这样的图

）
## 星座与身体部位对应表

| 星座 | 日期 | 主宰行星 | 元素 | 模式 | 相关身体部位 |
|---|---|---|---|---|---|
| 白羊座 ♈ | 3.21-4.20 | 火星 | 火 | 开创 | 头、面部、头骨、肾上腺素 |
| 金牛座 ♉ | 4.21-5.21 | 金星 | 土 | 固定 | 嗓子、喉咙、肩膀和上臂 |
| 双子座 ♊ | 5.22-6.21 | 水星 | 风 | 变动 | 前臂、手腕、手、手指、肺 |
| 巨蟹座 ♋ | 6.22-7.22 | 月亮 | 水 | 开创 | 胸部、乳房、胃 |
| 狮子座 ♌ | 7.23-8.23 | 太阳 | 火 | 固定 | 心脏、脊柱中段 |
| 处女座 ♍ | 8.24-9.23 | 水星 | 土 | 变动 | 下腹部、肠 |
| 天秤座 ♎ | 9.24-10.23 | 金星 | 风 | 开创 | 后背下部、肾和膀胱 |
| 天蝎座 ♏ | 10.24-11.22 | 冥王星 & 火星 | 水 | 固定 | 性器官、荷尔蒙 |
| 射手座 ♐ | 11.23-12.21 | 木星 | 火 | 变动 | 臀部和大腿 |
| 摩羯座 ♑ | 12.22-1.20 | 土星 | 土 | 开创 | 牙齿、膝盖、骨骼 |
| 水瓶座 ♒ | 1.21-2.19 | 天王星 & 土星 | 风 | 固定 | 循环系统、脚踝和小腿 |
| 双鱼座 ♓ | 2.20-3.20 | 海王星 & 木星 | 水 | 变动 | 脚、松果体 |"""

generation_config = {
    "max_output_tokens": 8192,
    "temperature": 1,
    "top_p": 0.95,
}

safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}

generate()

