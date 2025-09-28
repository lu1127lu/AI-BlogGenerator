# AI-BlogGenerator - Llama-2 via Ollama  
學號：p2202956 & p2215793　組員：Chloe & Winnie

## 一、環境安裝（一鍵）
```bash
git clone https://github.com/lu1127lu/AI-BlogGenerator.git
cd AI_BlogGenerator
python -m venv llm_env
# Windows
llm_env\Scripts\activate
# macOS/Linux
source llm_env/bin/activate
pip install -r requirements.txt
ollama pull llama2:7b


## 執行與測試

```bash
# 1. 互動生成
python app_ollama.py

# 2. 單元測試
python test_app_ollama.py


## 影片
| 片段 | 連結 |
|------|------|
| 1-installation | https://youtu.be/BE0jZ5aDQ1E |
| 2-implementation | https://youtu.be/ozkGyI9pkcs |
| 3-testing | https://youtu.be/RGARQdDrqQU |

