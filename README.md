## .env使用
1. 安裝python-dotenv。
2. 在專案根目錄放.env，並寫入需使用之資訊。
3. 參考`demo_env`的寫法將`.env`之資訊讀入程式。

此範例專案為了展示方便，將.env加入版控。正常情況應該要gitignore。

## Pool
參考`demo_pool`

## ML專案架構
建議使用`python -m`比較方便，例如執行：
```
python -m pipe.proc
```
這樣在`pipe/proc.py`可以成功引用另一子資料夾`src`內的`foo.py`的函數`foo`。直接使用`python pipe/proc.py`會無法成功import。要成功import需要多做
```
export PYTHONPATH="${PYTHONPATH}:<your-project-path>" 
```