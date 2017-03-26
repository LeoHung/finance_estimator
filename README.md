# Finance Estimator

![demo](demo/taiwan_50.png?raw=true "Demo")
![demo](demo/tsmc.png?raw=true "Demo")

## 免責聲明:

本專案提供的數據只供參考，概不構成財務意見，並且不對您的投資結果負責。

## 目的:

根據過往資料以及使用者的投資組合，以隨機模式模擬未來總資產成長趨勢。

## 使用方式：

- 請先安裝 numpy 和 matplotlib。或者可以用pip 讀取 requirments 安裝套件表 (如下指令)

pip install -r requirments

- 執行 main.py

python taiwan_50_main.py
python tsmc_main.py

## Demo:

main.py 會產生 50 條模擬的總資產成長圖，x軸為週期，y軸為資產總額，曲線估
計三年內資產總額量及其可能性。

模擬曲線數越集中的範圍，代表其預測機率越高。

目前提供兩個投資組合案例：(1)每個月購買一萬的台灣銀行定存，以及將
一萬元投入元大50 ETF。 (2) 每個月購買一萬的台灣銀行定存，以及購買一萬元
台積電股票。週期以月為單位。


## 資料來源：

台灣銀行新臺幣存(放)款牌告利率 (http://rate.bot.com.tw/twd?Lang=zh-TW)
Yahoo Finance. (http://finance.yahoo.com/quote/0050.TW?ltr=1)
