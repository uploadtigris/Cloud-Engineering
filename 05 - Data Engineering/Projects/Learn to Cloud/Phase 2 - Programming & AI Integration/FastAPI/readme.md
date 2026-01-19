Following the course [Python FastAPI Tutorial: Build a REST API in 15 Minutes](https://www.youtube.com/watch?v=iWS9ogMPOI0)

We need to install `fastapi`, a web framework for building APIs with Python && `uvicorn`, the server we will use to test and run our fastapi applications.

```bash
sudo apt install python3
```
```bash
# install the environment package for python
sudo apt install python3.12-venv
```
```bash
# create a virtual environment
python3 -m venv venv
```
```bash
# activate the environment
source venv/bin/activate
```bash
# install fastapi & uvicorn
pip install fastapi uvicorn
```
```bash
# deactivate the environment once done
deactivate
```
## Working with FastAPI

running uvicorn
```bash
uvicorn main:app --reload
```
sending request after the server has been started
```bash
curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:8000/items?item=apple'
```

retreiving items from python data structures
```bash
curl -X GET http://127.0.0.1:8000/items/0
```

## Raising errors
```bash
#incorporate error handling into the paths
@app.get("/items/{item_id}")
def get_item(item_id: int) -> str:
        if item_id < len(items):
                return items[item_id]
        else:
            raise HTTPException(status_code=404, detail=f'Item {item_id} not found')
```

## Sending payloads
```bash
# notice that the -d flag has you define the class values
curl -X POST -H "Content-Type: application/json" -d '{"text":"apple"}' 'http://127.0.0.1:8000/items'
```

## Response models
```bash
# a response model allows you to specify the model that your data will be in
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
        if item_id < len(items):
                return items[item_id]
        else:
            raise HTTPException(status_code=404, detail=f'Item {item_id} not found')
```

## Interactive Documentation
```
http://127.0.0.1:8000/docs#/
```