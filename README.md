# 🎨 Cartoonify an Image with OpenCV + Flask

Transform your photos into cartoon-style art using Python, OpenCV, and Flask!

| Normal Image                                                   | Cartoonify Image                                               |
|----------------------------------------------------------------|----------------------------------------------------------------|
| ![test2](https://github.com/user-attachments/assets/2b632be3-4119-48f9-8a27-3384f0e95c59)  | ![cartoon_test2](https://github.com/user-attachments/assets/0b7ce7b5-c62b-4688-99b1-7638b93367f5)     |
---

## 📌 Features

- 📤 Upload any photo
- 🧠 Apply cartoon filter using OpenCV
- 📥 Download the cartoonified image
- 🖥️ Simple, responsive web interface

---

## 🧰 Tech Stack

| Layer     | Technology          |
|-----------|---------------------|
| Backend   | Flask (Python)      |
| Image FX  | OpenCV              |
| Frontend  | HTML, CSS, JS       |
| Template  | Jinja2              |

---

## 📁 Project Structure

```
cartoonify-image/
│
├── backend/
│ ├── app.py # Flask app
│ ├── cartoonify.py # Image processing logic
│
├── static/
│ ├── uploads/ # Uploaded images
│ ├── results/ # Processed cartoon images
│
├── templates/
│ └── index.html # Main UI
│
├── venv/ # Python virtual environment
├── requirements.txt # Dependencies
└── README.md
```

---

## 🚀 Setup Instructions

### 1. Clone the Repo

```
git clone https://github.com/yourusername/cartoonify-image.git
cd cartoonify-image
```
2. Create Virtual Environment
```
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```
3. Install Dependencies
```
pip install -r requirements.txt
```
4. Run the App
```
cd backend
python app.py
```
Visit: http://127.0.0.1:5000 in your browser 🚀





