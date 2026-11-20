# 🔢 Digit Recognizer (Kaggle) – CNN with TensorFlow

> **يا صاحبي الموضوع أسهل مما تتخيل، متقلقش!** 😄
> We teach a computer to look at a picture of a handwritten number and say which digit it is (0–9).

---

## 🧠 What is this project?

This project solves the **Digit Recognizer** competition on Kaggle.
We build a small **Convolutional Neural Network (CNN)** that reads handwritten digit images and predicts the number inside each one.

**Result:** ~**98.4% validation accuracy** after only 10 epochs.

---

## 📚 Simple Words (Glossary)

| Word | Easy explanation |
|------|------------------|
| **Kaggle** | A website where people practice data science and AI by solving real problems. |
| **Competition** | A problem on Kaggle with a goal. Everyone submits predictions and gets a score. Ours is *Digit Recognizer*. |
| **Dataset** | The data we get to work with (here: CSV files full of images saved as numbers). |
| **Train set** | Images **with** the correct answer (label). The model learns from it. |
| **Test set** | Images **without** answers. We predict them and submit to Kaggle. |
| **Label** | The correct answer for an image (the digit 0–9). |
| **Pixel** | One tiny dot of an image. Our images are 28×28 = **784 pixels**. Each has a value from 0 (black) to 255 (white). |
| **CNN** | A type of neural network that is great at understanding images. |
| **Epoch** | One full round where the model sees all the training images once. |
| **Validation split** | We hide 20% of the training data to check if the model really learned (not just memorized). |

> **ولا يهمك المصطلحات**، هتفهمها كلها مع الوقت وإنت بتشتغل. 💪

---

## 📦 Dataset

Downloaded from the Kaggle competition: **Digit Recognizer**
🔗 https://www.kaggle.com/competitions/digit-recognizer

| File | What's inside |
|------|---------------|
| `train.csv` | 42,000 images. Column `label` = the digit, other 784 columns = pixel values. |
| `test.csv` | 28,000 images (no label). We predict these. |
| `submission.csv` | Our output file that we upload to Kaggle. |

> ⚠️ The CSV files are **not uploaded to GitHub** because they are big. Download them from Kaggle (see below).

### Download with the Kaggle CLI

```bash
kaggle competitions download -c digit-recognizer
```

Then unzip it in the project folder.

---

## 🛠️ How it works (step by step)

1. **Load data** – read `train.csv` and `test.csv` with pandas.
2. **Split** – separate the images (`X_train`) from the answers (`y_train`).
3. **Look at the data** – plot 30 images to see what we're dealing with.
4. **Reshape** – turn each row of 784 numbers into a 28×28 image with 1 color channel.
5. **Normalize** – divide by 255 so values are between 0 and 1 (the model learns faster).
6. **One-hot encode labels** – for example, `3` becomes `[0,0,0,1,0,0,0,0,0,0]`.
7. **Build the CNN model** (below).
8. **Train** – 10 epochs, batch size 128, 20% validation.
9. **Predict** the test images.
10. **Create `submission.csv`** and upload it to Kaggle.

---

## 🏗️ Model Architecture

```
Input (28×28×1)
   ↓
Conv2D (64 filters, 3×3, ReLU)
   ↓
MaxPooling (2×2)
   ↓
Conv2D (32 filters, 3×3, ReLU)
   ↓
MaxPooling (2×2)
   ↓
Conv2D (16 filters, 3×3, ReLU)
   ↓
Flatten
   ↓
Dense (10 outputs, Softmax)   → probability for each digit 0–9
```

**Why this works (simple idea):**
- **Conv2D** = small "magnifying glasses" that find shapes (lines, curves, corners).
- **MaxPooling** = shrinks the image and keeps the important parts.
- **Flatten + Dense** = takes everything found and decides: "this looks like a 7".
- **Softmax** = gives a probability for each digit; we pick the highest one.

---

## 📈 Training Results

| Epoch | Train Accuracy | Validation Accuracy |
|-------|----------------|---------------------|
| 1 | 85.1% | 95.7% |
| 5 | 98.2% | 97.7% |
| 10 | 98.9% | **98.5%** |

Training and validation accuracy are close, so the model is **not overfitting**. 👍

---

## ▶️ How to Run

```bash
# 1. Clone the repo
git clone https://github.com/beshara997/Digit-Recognizer.git
cd Digit-Recognizer

# 2. (Optional) create a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows

# 3. Install libraries
pip install tensorflow pandas numpy matplotlib kaggle

# 4. Download the data from Kaggle
kaggle competitions download -c digit-recognizer

# 5. Run the notebook / script
```

The output file `submission.csv` is created in the project folder. Upload it on the competition page under **Submit Predictions**.

---

## 🧰 Tools Used

- Python 3.12
- TensorFlow / Keras
- Pandas & NumPy
- Matplotlib

---

## 🚀 Ideas to Improve the Score

- Add **Dropout** or **BatchNormalization**
- Use **Data Augmentation** (small rotations/shifts)
- Train for more epochs with **EarlyStopping**
- Try a deeper CNN

---

## ✍️ Author

**beshara997**

> **خطوة خطوة وهتوصل. الأهم إنك تفهم اللي بتعمله، مش بس تشغّل الكود!** 🔥
# Changes
| 2 | Add Dropout(0.5) after Flatten | 0.9840 | 0.0464 | val_loss improved ~24%, train acc dropped (dropout active in training) |
