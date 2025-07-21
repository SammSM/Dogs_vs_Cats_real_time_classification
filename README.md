# Dogs_vs_Cats_real_time_classification
This project performs simple binary image classification to distinguish between dogs and cats. It processes whole images and outputs the predicted class.

To solve the binary classification task, a **Convolutional Neural Network** was designed. The CNN is built to work with grayscale images of size **128×128** and consists of the following layers:

- **Conv2D (64 filters)**: with ReLU activation for feature extraction
- **MaxPooling2D**: to reduce dimensionality
- **Conv2D (128 filters)**: deeper feature detection
- **MaxPooling2D**
- **Flatten**: to convert 2D features to 1D
- **Dense (64 units)**: fully connected layer with **L2 regularization**
- **Dropout (0.2)**: to prevent overfitting
- **Output Layer**: Dense with **sigmoid** activation to classify between cat (0) and dog (1)

An **early stopping** mechanism was also used during training to avoid overfitting and save the best-performing model as `dogs_vs_cats_h5.h5`.

## 📚 Libraries

- **TensorFlow / Keras** — Model building, training, saving, and loading.  
- **scikit-learn** — Utilities for train/test splitting and data shuffling.  
- **NumPy** — Data manipulation and numerical operations.  
- **OpenCV** — Image preprocessing: resizing, color conversion, and webcam handling.  
- **Matplotlib** — Visualizing images and plotting training loss/accuracy graphs.  
- **Pickle** — Saving/loading machine learning models (used cautiously for Keras models).  
- **Other Keras modules** — Layers, optimizers, callbacks (EarlyStopping).  

