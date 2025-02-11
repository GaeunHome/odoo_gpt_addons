# 在 Odoo 平台使用 OpenAI API 並將回應輸出

使用 `text-davinci-003` 模型，而非 `gpt-3.5-turbo`。程式碼只需參照 `controllers.py`，其餘檔案尚未使用。

## 設置指南

1. **API Key 設定**  
   在 `controllers.py` 中輸入您的 API Key，並將該文件放置於其他的 addons 路徑中。

2. **查看模型回應**  
   只需透過網址即可查看模型的回應。

## 操作步驟

1. **激活**  
   根據其他的 addons 檔案路徑，輸入以下網址格式：
   ```
   http://<您的域名或IP地址>/<指定的路徑>/?prompt=你的問題
   ```
   這將在網頁上輸出模型的回應。

2. **備註**  
   有關於 `<指定的路徑>` 可在 `controllers.py` 的第 7 行進行設定。
