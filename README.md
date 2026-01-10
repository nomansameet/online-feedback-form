# 🚀 Online Feedback Collector - Complete Setup Guide

## 📖 Project Overview
A **full-stack feedback collection system** built with **Flask**, **SQLite**, and modern **HTML/CSS/JavaScript**. Users submit feedback via a responsive form, and admins view analytics, charts, and export data as CSV.

**✨ Features:**
- 📝 Professional feedback form (name, email, rating, comments)
- 📊 Admin dashboard with real-time statistics & charts
- 📥 One-click CSV export
- 📱 Fully responsive design
- 🔐 SQLite database (no external setup)

***

## 📋 Prerequisites
```
✅ Python 3.8+ installed
✅ Git installed (for GitHub)
✅ Web browser (Chrome/Firefox recommended)
✅ Code editor (VS Code recommended)
```

***

## 🛠️ Step-by-Step Setup

### **Step 1: Clone Repository**
```bash
git clone https://github.com/yourusername/online-feedback-collector.git
cd online-feedback-collector
```

### **Step 2: Create & Activate Virtual Environment**
```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate
# Activate (Mac/Linux)  
source venv/bin/activate
```
**✅ Success:** Terminal shows `(venv)`

### **Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 4: Verify Installation**
```bash
python -c "import flask; print('✅ Flask ready!')"
```

### **Step 5: Run Application**
```bash
python app.py
```

**✅ Expected Output:**
```
🚀 Server starting...
🌐 Form: http://127.0.0.1:5000/
📊 Dashboard: http://127.0.0.1:5000/admin-dashboard
 * Running on http://127.0.0.1:5000
```

### **Step 6: Test Application**
Open browser and visit:
```
📱 Feedback Form: http://127.0.0.1:5000/
📊 Admin Dashboard: http://127.0.0.1:5000/admin-dashboard
📥 API (JSON): http://127.0.0.1:5000/api/feedback
```

***

## 🎮 How to Use

1. **Submit Feedback:**
   - Fill form at `/` 
   - Submit → Data saves to database

2. **View Analytics:**
   - Visit `/admin-dashboard`
   - See total count, average rating, rating distribution chart
   - Click "Export CSV" to download data

3. **Stop Server:**
   - Press `Ctrl+C` in terminal

***

## 📂 Project Structure
```
online-feedback-collector/
├── app.py                 # Flask backend + routes
├── requirements.txt       # Python dependencies
├── feedback.db           # SQLite database (auto-created)
├── templates/            # HTML templates (Jinja2)
│   ├── base.html         # Layout template
│   ├── index.html        # Feedback form
│   └── admin.html        # Dashboard + charts
└── static/
    ├── css/
    │   └── style.css     # Professional modern styling
    └── js/
        └── script.js     # Form validation

***

