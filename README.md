# Gemini Health App 🍎🤖

A Streamlit-powered web application that uses **Google Gemini** to analyze images of food and provide detailed calorie estimations. Upload an image of your meal and get a breakdown of each item’s calorie content instantly!

---

## ✨ Features

- Upload food images (JPG, JPEG, PNG)
- Automatically identify food items using Gemini AI
- Get a detailed calorie breakdown per item
- Interactive, user-friendly interface with Streamlit

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/gemini-health-app.git
cd gemini-health-app
```

### 2. Install the dependencies

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
```

Then install the required packages:

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables

Create a `.env` file in the root directory and add your **Google Gemini API key**:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

> You can get access to the Gemini API via Google’s developer platform.

---

## 🧠 How It Works

1. Upload an image of a meal.
2. The app sends the image and a detailed prompt to the Gemini model.
3. Gemini returns a list of detected food items with estimated calorie values.
4. The app displays the response in a clean format.

---

## 🖼️ Example Output

```
1. Grilled Chicken - 250 calories  
2. Steamed Broccoli - 55 calories  
3. Brown Rice - 216 calories  
```

---

## 📦 Project Structure

```
.
├── app.py               # Main Streamlit application
├── requirements.txt     # Python dependencies
└── .env                 # Environment variables (not committed)
```

---

## 🔐 Disclaimer

This application provides approximate calorie values and is not a substitute for professional dietary advice.

---

## 🛠 Built With

- [Streamlit](https://streamlit.io/)
- [Google Gemini API](https://ai.google.dev/)
- [Python](https://www.python.org/)

---

## 📬 Contact

Have questions or want to contribute? Reach out at [koushikyerra3@gmail.com] or open an issue.
