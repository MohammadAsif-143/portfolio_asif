import os
import time
import math
import random
from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, send_from_directory, make_response
from portfolio_data import PROFILE, METRICS, SKILL_CATEGORIES, PROJECTS, EXPERIENCES, EDUCATION, CERTIFICATIONS

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'asif-portfolio-secret-key-2026')


@app.context_processor
def inject_globals():
    """Make profile data, projects, and current year accessible to all templates."""
    return {
        'profile': PROFILE,
        'projects': PROJECTS,
        'current_year': 2026
    }


@app.route('/')
def index():
    """Render the main high-impact portfolio showcase."""
    # Group categories for filter buttons
    categories = [
        {"id": "all", "label": "All Work", "count": len(PROJECTS)},
        {"id": "nlp", "label": "LLMs & NLP", "count": len([p for p in PROJECTS if p['category'] == 'nlp'])},
        {"id": "vision", "label": "Computer Vision", "count": len([p for p in PROJECTS if p['category'] == 'vision'])},
        {"id": "predictive", "label": "Predictive ML & Analytics", "count": len([p for p in PROJECTS if p['category'] == 'predictive'])},
        {"id": "bio", "label": "Bio & Deep Learning", "count": len([p for p in PROJECTS if p['category'] == 'bio'])},
    ]

    return render_template(
        'index.html',
        profile=PROFILE,
        metrics=METRICS,
        categories=categories,
        skills=SKILL_CATEGORIES,
        projects=PROJECTS,
        experiences=EXPERIENCES,
        education=EDUCATION,
        certifications=CERTIFICATIONS
    )


@app.route('/project/<project_id>')
def project_detail(project_id):
    """Render a dedicated deep-dive page for a specific project."""
    project = next((p for p in PROJECTS if p['id'] == project_id), None)
    if not project:
        flash(f"Project '{project_id}' not found.", "warning")
        return redirect(url_for('index'))

    # Related projects
    related_projects = [p for p in PROJECTS if p['id'] != project_id and (p['category'] == project['category'] or p.get('featured'))][:2]

    return render_template('project_detail.html', project=project, related=related_projects)


@app.route('/api/projects')
def api_projects():
    """API endpoint to get filtered projects."""
    category = request.args.get('category', 'all')
    search = request.args.get('q', '').strip().lower()

    filtered = PROJECTS
    if category != 'all':
        filtered = [p for p in filtered if p['category'] == category]

    if search:
        filtered = [
            p for p in filtered
            if search in p['title'].lower()
            or search in p['summary'].lower()
            or any(search in tag.lower() for tag in p['tags'])
        ]

    return jsonify({"status": "success", "count": len(filtered), "projects": filtered})


@app.route('/api/predict', methods=['GET', 'POST'])
@app.route('/api/ml-inference', methods=['POST'])
def ml_inference():
    """
    Live interactive ML inference playground simulator.
    Demonstrates Flask REST capabilities, latency calculation,
    probabilistic calibration, and feature attribution.
    """
    start_time = time.time()
    data = request.get_json(silent=True) or request.form.to_dict()

    task_type = data.get('task', 'risk_classification')
    input_text = data.get('text', '').strip()
    feature_a = float(data.get('feature_a', 75))  # Transaction Volume / Model Depth
    feature_b = float(data.get('feature_b', 45))  # Volatility / Sequence Length
    feature_c = float(data.get('feature_c', 90))  # Confidence / Threshold

    # Calculate deterministic simulated inference
    # Softmax probability modeling
    z1 = (feature_a * 0.03) + (feature_b * 0.02) - (feature_c * 0.025)
    z2 = -(feature_a * 0.015) + (feature_b * 0.035) + 0.5
    z3 = 0.8 - (feature_b * 0.01)

    exp_z = [math.exp(min(max(z, -10), 10)) for z in [z1, z2, z3]]
    sum_exp = sum(exp_z)
    probs = [round(e / sum_exp, 4) for e in exp_z]

    # Map classes based on task
    if task_type == 'nlp_sentiment':
        classes = ["Positive Sentiment", "Neutral / Ambiguous", "Critical / Urgent"]
        predicted_idx = probs.index(max(probs))
        pred_label = classes[predicted_idx]
    elif task_type == 'anomaly_detection':
        classes = ["Normal Baseline", "Statistical Anomaly", "Critical Risk Pattern"]
        predicted_idx = probs.index(max(probs))
        pred_label = classes[predicted_idx]
    else:  # risk_classification
        classes = ["Low Risk / High Confidence", "Medium Variance", "High Risk / Review Needed"]
        predicted_idx = probs.index(max(probs))
        pred_label = classes[predicted_idx]

    inference_ms = round((time.time() - start_time) * 1000 + random.uniform(8.5, 14.2), 2)

    return jsonify({
        "status": "success",
        "task": task_type,
        "prediction": pred_label,
        "confidence": round(probs[predicted_idx] * 100, 1),
        "probabilities": {
            classes[0]: round(probs[0] * 100, 1),
            classes[1]: round(probs[1] * 100, 1),
            classes[2]: round(probs[2] * 100, 1)
        },
        "feature_attributions": {
            "Normalized Input Weight": round(min(1.0, feature_a / 100), 2),
            "Sequence Volatility Factor": round(min(1.0, feature_b / 100), 2),
            "Prior Bayesian Calibration": round(min(1.0, feature_c / 100), 2)
        },
        "latency_ms": inference_ms,
        "model_architecture": "Ensemble Transformer + Gradient Boosted Calibration"
    })


@app.route('/contact', methods=['POST'])
def contact():
    """Handle contact form submissions with validation and user feedback."""
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    subject = request.form.get('subject', 'General Inquiry').strip()
    message = request.form.get('message', '').strip()

    if not name or not email or not message:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.is_json:
            return jsonify({"status": "error", "message": "Please fill in all required fields."}), 400
        flash("Please fill in all required fields.", "error")
        return redirect(url_for('index') + '#contact')

    # Basic email verification check
    if '@' not in email or '.' not in email:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.is_json:
            return jsonify({"status": "error", "message": "Please enter a valid email address."}), 400
        flash("Please enter a valid email address.", "error")
        return redirect(url_for('index') + '#contact')

    # In production, send via SendGrid, SMTP, or webhook
    # For now, return pleasant interactive confirmation
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.is_json:
        return jsonify({
            "status": "success",
            "message": f"Thank you, {name}! Your message has been received. I will get back to you within 24 hours."
        })

    flash(f"Thank you, {name}! Your message has been received. I will respond to {email} promptly.", "success")
    return redirect(url_for('index') + '#contact')


@app.route('/resume/download')
def download_resume():
    """Provide a clean resume download or preview."""
    resume_path = os.path.join(app.root_path, 'static', 'docs', 'Asif_J_Data_Scientist_Resume.pdf')
    if os.path.exists(resume_path):
        return send_from_directory(
            os.path.join(app.root_path, 'static', 'docs'),
            'Asif_J_Data_Scientist_Resume.pdf',
            as_attachment=True
        )
    # If PDF isn't compiled, render an executive print-ready view
    return redirect(url_for('resume_view'))


@app.route('/resume')
def resume_view():
    """Print-ready executive CV / Resume page for recruiters."""
    return render_template(
        'resume.html',
        profile=PROFILE,
        metrics=METRICS,
        skills=SKILL_CATEGORIES,
        projects=PROJECTS,
        experiences=EXPERIENCES,
        education=EDUCATION,
        certifications=CERTIFICATIONS
    )


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


if __name__ == '__main__':
    # Run locally with debug mode
    app.run(host='127.0.0.1', port=5000, debug=True)
