# Finance Estimator

![demo](estimation.jpg?raw=true "Demo")

## 免責聲明:

本專案提供的數據只供參考，概不構成財務意見，並且不對您的投資結果負責。

## 目的:

根據過往資料以及使用者的投資組合，以隨機模式模擬未來總資產成長趨勢。

## 使用方式：

- 請先安裝 numpy 和 matplotlib
pip install -r requirments

- 執行 main.py
python main.py

## Demo:

main.py 提供一個非常簡單的投資組合：每個月購買一萬的台灣銀行定存，以及將
一萬元投入元大50 ETF。main.py 會產生 50 條模擬的總資產成長圖，以估計三年
後資產總額及其可能性。模擬曲線數越集中的範圍，代表其預測機率越高。