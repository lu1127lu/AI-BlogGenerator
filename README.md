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

## 1B 延伸（LLM 量化對話）
### 影片（Google Drive 公開連結）
| 片段 | 連結 |
|------|------|
| 1-installation | https://drive.google.com/file/d/1UllD5SE-KCQhvCImTDp3QDWifZHv0np8/view?usp=sharing |
| 2-implementation | https://drive.google.com/file/d/11HCjiVyS_ZmcYnH-u_agry12w7GnfBMc/view?usp=sharing |
| 3-testing | https://drive.google.com/file/d/1MYnJstUMj3mdIvXDiEXgDbshOdocAhBj/view?usp=sharing |
