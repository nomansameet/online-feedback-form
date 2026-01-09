from flask import Flask, render_template, request, redirect, url_for, jsonify, send_file
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import csv
import io
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'echo': False}

# Fix: Initialize DB properly
db = SQLAlchemy(app)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.Text, nullable=True)
    date_submitted = db.Column(db.DateTime, default=datetime.utcnow)

# Fix: Proper DB initialization with error handling
@app.cli.command()
def init_db():
    with app.app_context():
        db.create_all()
    print("Database initialized!")

@app.route('/', endpoint='home')
def home():
    return render_template('index.html')

@app.route('/submit-feedback', methods=['POST'], endpoint='submit_feedback')
def submit_feedback():
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    rating = request.form.get('rating')
    comments = request.form.get('comments', '').strip()

    if not name or not email or not rating:
        print(f"Missing data: name={name}, email={email}, rating={rating}")
        return redirect(url_for('home'))

    try:
        fb = Feedback(name=name, email=email, rating=int(rating), comments=comments)
        db.session.add(fb)
        db.session.commit()
        print(f"Feedback saved: {name}")
    except Exception as e:
        print(f"Database error: {e}")
        db.session.rollback()
        return redirect(url_for('home'))

    return redirect(url_for('home'))

@app.route('/admin-dashboard', endpoint='admin_dashboard')
def admin_dashboard():
    try:
        feedbacks = Feedback.query.order_by(Feedback.date_submitted.desc()).all()
        total = len(feedbacks)
        avg_rating = round(sum(f.rating for f in feedbacks) / total, 2) if total > 0 else 0

        rating_counts = {str(i): 0 for i in range(1, 6)}
        for f in feedbacks:
            rating_counts[str(f.rating)] += 1

        return render_template('admin.html', feedbacks=feedbacks, total=total, 
                             avg_rating=avg_rating, rating_counts=rating_counts)
    except Exception as e:
        print(f"Dashboard error: {e}")
        return "Error loading dashboard", 500

@app.route('/api/feedback', endpoint='api_feedback')
def api_feedback():
    feedbacks = Feedback.query.order_by(Feedback.date_submitted.desc()).all()
    data = [{'id': f.id, 'name': f.name, 'email': f.email, 'rating': f.rating, 
             'comments': f.comments, 'date_submitted': f.date_submitted.isoformat()} 
            for f in feedbacks]
    return jsonify(data)

@app.route('/export-csv', endpoint='export_csv')
def export_csv():
    feedbacks = Feedback.query.order_by(Feedback.date_submitted.desc()).all()
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['id', 'name', 'email', 'rating', 'comments', 'date_submitted'])
    for f in feedbacks:
        writer.writerow([f.id, f.name, f.email, f.rating, f.comments,
                        f.date_submitted.strftime('%Y-%m-%d %H:%M:%S')])
    output.seek(0)
    return send_file(io.BytesIO(output.getvalue().encode()), mimetype='text/csv',
                    as_attachment=True, download_name='feedback.csv')

# Fix: Initialize DB on startup
def init_database():
    with app.app_context():
        db.create_all()
        print("✅ Database ready!")

if __name__ == '__main__':
    print("🚀 Starting Flask app...")
    init_database()
    print("🌐 Open: http://127.0.0.1:5000/")
    app.run(debug=True, host='127.0.0.1', port=5000)
