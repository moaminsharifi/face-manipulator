
# Face-Manipulator 
## Running the app

### Run with CLI
```bash
usage: face_manipulator.py [-h] -i image file path -t [-100-100]

optional arguments:
  -h, --help            show this help message and exit
  -i image file path, --image image file path
                        image file path ex: selfie_image_path.[jpg|png]
  -t [-100-100], --threshold [-100-100]
                        threshold of change nose or left eye
```
#### example:
```bash
python face_manipulator.py -t 100 -i tests/assets/front.jpg
```
### import as python packages
#### install package
```bash
pip install -e .
```
#### import package
```python
face_manipulator
```
### setup ENV and install packages
best way is create isolate environment with python virtualenv
```bash
virtualenv -p python3 venv
source venv/bin/activate
```
Next install python packages with `pip`

```bash
pip install -r requirements.txt
```

if want to test app install `pytest` with
```bash
pip install pytest
```
then run 
```bash
pytest
```
