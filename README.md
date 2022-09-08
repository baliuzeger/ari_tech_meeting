## .env使用
1. 安裝python-dotenv。
2. 在專案根目錄放.env，並寫入需使用之資訊。
3. 參考`demo_env`的寫法將`.env`之資訊讀入程式。

此範例專案為了展示方便，將.env加入版控。正常情況應該要gitignore。

## Pool
參考`demo_pool`

## ML專案架構
### python -m
建議使用`python -m`比較方便，例如執行：
```
python -m pipe.proc
```
這樣在`pipe/proc.py`可以成功引用另一子資料夾`src`內的`foo.py`的函數`foo`。直接使用以下：

```python pipe/proc.py```

會無法成功import。要成功import需要多做
```
export PYTHONPATH="${PYTHONPATH}:<your-project-path>" 
```

### srs, pipe & config
可參考本專案`src`（pipeline的單一步驟）和`pipe`（連串步驟的pipeline）等資料夾內的寫法，在`src`和`pipe`下個放一個`config.py`，分別給「跑單一步驟」和「跑pipeline」時使用，這樣就可以同時給這兩種情境套用不同的參數。執行單一步驟用`python -m src.foo`，執行pipeline用`python -m pipe.proc`。