# Asif J — Data Scientist & AI/ML Engineer Portfolio

A modern, high-impact, and production-grade portfolio web application engineered with **Python Flask** and **Vanilla CSS (Dark Mode Glassmorphism)** to showcase machine learning, generative AI, deep learning, and predictive engineering work.

---

## 🌟 Key Features

1. **Dark Mode Glassmorphism & Neural Aesthetics**:
   - Deep obsidian/slate backdrop (`#080c14`) with glowing violet (`#8b5cf6`), cyber cyan (`#06b6d4`), and emerald accents.
   - Interactive ambient neural particle canvas with real-time mouse interaction.
   - Premium typography using Google Fonts (*Plus Jakarta Sans* & *JetBrains Mono*).

2. **Interactive Project Gallery & Deep-Dive Modals**:
   - Dynamic category filter tabs (*All Work*, *LLMs & NLP*, *Computer Vision*, *Predictive ML & Analytics*, *Bio & Deep Learning*).
   - Real-time search filter matching project titles, summaries, and tech tags.
   - Interactive Architecture modal with pipeline flows, key metrics, and engineering solutions.
   - Dedicated standalone case study URLs (`/project/<id>`).

3. **Live ML Inference Playground Simulator**:
   - Real interactive inference widget powered by the Flask backend (`/api/ml-inference`).
   - Interactive sliders for model complexity, sequence volatility, and Bayesian confidence thresholds.
   - Dynamic real-time latency calculations, class predictions, and calibrated softmax probability distributions.

4. **Career Timeline & Quantifiable Deliverables**:
   - Structured experience milestones highlighting production achievements, latency speedups, and business ROI.
   - Education and verified cloud & deep learning certifications.

5. **Print-Ready Executive CV / Resume View**:
   - Accessible via `/resume` or the Resume button.
   - Formatted for clean 1-click printing or exporting to PDF without website clutter.

6. **Working Contact System**:
   - AJAX-powered contact form with validation and instant feedback alerts.
   - One-click copy email button with toast notifications.

---

## 📂 Project Directory Structure

```
asif_portfolio/
│
├── app.py                  # Core Flask application, routing, and live ML inference API
├── portfolio_data.py       # Central data file (profile, metrics, projects, skills, timeline)
├── requirements.txt        # Python dependencies (Flask)
├── README.md               # Documentation & setup guide
│
├── static/
│   ├── css/
│   │   └── style.css       # Complete dark glassmorphism design system & responsive styling
│   ├── js/
│   │   └── main.js         # Particle canvas, filters, modals, live ML playground, form AJAX
│   ├── images/
│   │   ├── avatar.jpg            # Professional portrait
│   │   ├── project-llm.jpg       # CognitiveRAG neural architecture visual
│   │   ├── project-vision.jpg    # AuraVision perception & tracking visual
│   │   ├── project-predictive.jpg# AlphaQuant financial intelligence visual
│   │   └── project-genomics.jpg  # GeneFold biomolecular deep learning visual
│   └── docs/
│
└── templates/
    ├── base.html           # Master layout with SEO headers, navbar, modal, and footer
    ├── index.html          # Main portfolio showcase
    ├── project_detail.html # Standalone project deep-dive case study page
    ├── resume.html         # Executive print-ready CV / Resume view
    ├── 404.html            # High-tech 404 error page
    └── 500.html            # Server exception page
```

---

## 🚀 How to Run the Portfolio Locally

### 1. Prerequisites
- Python 3.9+ installed.

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Launch Flask Application
```bash
python app.py
```

Open your browser and navigate to:
```
http://127.0.0.1:5000
```

---

## ✏️ How to Customize Your Portfolio

All your personal and professional details are consolidated in **`portfolio_data.py`**:
- **`PROFILE`**: Update your name, title, bio, contact email, GitHub, and LinkedIn links.
- **`METRICS`**: Adjust your production metrics (models deployed, uptime, throughput).
- **`SKILLS`**: Add or modify skill categories, proficiencies, and tools.
- **`PROJECTS`**: Add your own project case studies, metrics, architectures, and repository URLs.
- **`EXPERIENCES`**: Update your career history, companies, and achievements.
- **`EDUCATION` & `CERTIFICATIONS`**: Add your degrees and certifications.
