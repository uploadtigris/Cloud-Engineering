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