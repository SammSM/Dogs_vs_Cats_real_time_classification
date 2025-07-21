# Dogs_vs_Cats_real_time_classification
This project performs simple binary image classification to distinguish between dogs and cats. It processes whole images and outputs the predicted class.

To solve the binary classification task, a **Convolutional Neural Network** was designed.

## 📚 Libraries

- **TensorFlow / Keras** — Model building, training, saving, and loading.
- **scikit-learn** — Utilities for train/test splitting and data shuffling.
- **NumPy** — Data manipulation.
- **OpenCV** — Image preprocessing: resizing, color conversion, and webcam handling.  
- **Matplotlib** — Visualizing images and plotting training loss/accuracy graphs.
- **Pickle** — Saving/loading ML models.
- **Other Keras modules** — Layers, optimizers, callbacks (EarlyStopping).  

## 🛠️ Setup guide

### 1. Clone the repository
Open your environment and clone the repository
```bash
https://github.com/SammSM/Dogs_vs_Cats_real_time_classification.git
```
### 2. Change to Dogs_vs_Cats_real_time_classification directory
```bash
cd Dogs_vs_Cats_real_time_classification
```

### 4. Create a virtual environment and activate it

- #### Create a virtual environment
On Windows:
```bash
python -m venv venv
```
On macOS / Linux:
```bash
python3 -m venv venv
```
- #### Activate the virtual environment
On Windows:
```bash
venv\Scripts\activate
```
On macOS / Linux:
```bash
source venv/bin/activate
```

### 5. Install PIP package manager for Python
```bash
py -m pip install --upgrade pip
```
#### Or
```bash
python -m pip install --upgrade pip
```

### 6. Install requirements
```bash
pip install -r requirements.txt
```

## ⚙️ How to run it
Open command line and enter:
```bash
py -m live_camera.py
```
To close the camera press 'q'.
