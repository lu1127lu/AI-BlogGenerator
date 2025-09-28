# Results - AI-BlogGenerator (Llama-2 7B-chat via Ollama)

## 模型與量化
- Meta Llama-2-7B-chat
- 8-bit 量化（load_in_8bit）
- 本地 Ollama 部署

## 樣本輸出
**Input:** renewable energy  
**Output:**  
"Renewable energy is transforming the way we power our world..."

## 觀察數據
- 平均生成時間：≈ 5 s（RTX 3060 6 GB）
- 文章長度：120-180 words
- 關鍵字命中率：100 %（unit-test assert 通過）

## 測試結果
✅ Unit test (length &gt; 50 & keyword) passed.