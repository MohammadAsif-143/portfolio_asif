"""
Portfolio configuration and professional data for Asif J - Data Scientist & AI/ML Engineer.
All data can be easily customized here.
"""

PROFILE = {
    "name": "Asif J",
    "title": "Data Scientist & AI/ML Engineer",
    "subtitle": "Specializing in Large Language Models, Deep Learning & High-Throughput Predictive Systems",
    "location": "Bangalore, India • Open to Worldwide Remote",
    "bio": (
        "I am a results-driven Data Scientist and Machine Learning Engineer passionate about "
        "transforming complex raw data into production-grade AI systems. With strong foundations "
        "in statistical learning, transformer architectures, and scalable MLOps pipelines, "
        "I engineer end-to-end intelligent applications that solve high-stakes business challenges."
    ),
    "status": "Available for High-Impact Roles",
    "email": "asif.datascience.ai@gmail.com",
    "github": "https://github.com",
    "linkedin": "https://linkedin.com",
    "kaggle": "https://kaggle.com",
    "huggingface": "https://huggingface.co",
    "avatar_image": "/static/images/avatar.jpg",
    "experience_years": "4+",
}

METRICS = [
    {
        "label": "Production Models Deployed",
        "value": 14,
        "suffix": "+",
        "detail": "Across fintech, healthcare & NLP domains"
    },
    {
        "label": "Pipeline Inference Uptime",
        "value": 99.9,
        "suffix": "%",
        "detail": "Zero-downtime automated CI/CD MLOps"
    },
    {
        "label": "Inference Latency Reduction",
        "value": 42,
        "suffix": "%",
        "detail": "Model pruning, quantization & ONNX runtime"
    },
    {
        "label": "Daily Data Ingested",
        "value": 2.8,
        "suffix": "TB",
        "detail": "Distributed stream & batch ETL pipelines"
    }
]

SKILL_CATEGORIES = [
    {
        "name": "Core Machine Learning & Deep Learning",
        "icon": "brain",
        "skills": [
            {"name": "PyTorch", "level": 95},
            {"name": "TensorFlow / Keras", "level": 90},
            {"name": "Scikit-Learn", "level": 98},
            {"name": "XGBoost / LightGBM", "level": 94},
            {"name": "Deep Neural Networks (CNN/RNN/LSTM)", "level": 92},
            {"name": "Statistical Hypothesis Testing", "level": 90}
        ]
    },
    {
        "name": "Generative AI & NLP",
        "icon": "sparkles",
        "skills": [
            {"name": "LLM Fine-Tuning (LoRA / QLoRA)", "level": 94},
            {"name": "RAG Systems (Retrieval-Augmented)", "level": 96},
            {"name": "Hugging Face Transformers", "level": 95},
            {"name": "Vector Databases (FAISS, Chroma, Milvus)", "level": 92},
            {"name": "LangChain & LlamaIndex", "level": 91},
            {"name": "Prompt Engineering & Evaluation", "level": 94}
        ]
    },
    {
        "name": "Computer Vision & Perception",
        "icon": "eye",
        "skills": [
            {"name": "YOLOv8 & Object Detection", "level": 90},
            {"name": "Semantic Segmentation", "level": 88},
            {"name": "OpenCV & Image Processing", "level": 92},
            {"name": "Model Quantization (ONNX / TensorRT)", "level": 86}
        ]
    },
    {
        "name": "Data Engineering & Analytics",
        "icon": "database",
        "skills": [
            {"name": "Python (Advanced)", "level": 98},
            {"name": "SQL & Query Optimization", "level": 95},
            {"name": "Pandas & Polars", "level": 96},
            {"name": "Apache Spark (PySpark)", "level": 87},
            {"name": "Feature Engineering & EDA", "level": 95},
            {"name": "Interactive Dashboards (Plotly/Streamlit)", "level": 92}
        ]
    },
    {
        "name": "MLOps, Cloud & Production Tools",
        "icon": "cloud",
        "skills": [
            {"name": "Flask & FastAPI Microservices", "level": 95},
            {"name": "Docker & Containerization", "level": 92},
            {"name": "MLflow & Experiment Tracking", "level": 90},
            {"name": "AWS (SageMaker, S3, Lambda, EC2)", "level": 88},
            {"name": "Git & Automated CI/CD Pipelines", "level": 94},
            {"name": "DVC (Data Version Control)", "level": 85}
        ]
    }
]

PROJECTS = [
    {
        "id": "cognitiverag-llm-knowledge-graph",
        "title": "CognitiveRAG: Enterprise Multi-Modal Knowledge Engine",
        "category": "nlp",
        "category_name": "Generative AI & NLP",
        "summary": "Hybrid retrieval-augmented generation engine integrating vector dense search with hierarchical graph reasoning for complex enterprise document synthesis.",
        "image": "/static/images/project-llm.jpg",
        "metrics": "94.2% Context Retrieval Accuracy • 3.2x Latency Speedup",
        "tags": ["Python", "PyTorch", "Hugging Face", "LangChain", "ChromaDB", "FastAPI", "Docker"],
        "highlights": [
            "Engineered hybrid search fusing BM25 sparse keyword ranking with dense cosine similarity embeddings.",
            "Incorporated re-ranking using Cross-Encoders, boosting relevant answer precision by 28%.",
            "Deployed streaming response pipeline with sub-450ms time-to-first-token using asynchronous FastAPI and vLLM.",
            "Integrated hallucination detection guardrails with semantic confidence scoring."
        ],
        "architecture": "Raw Multi-Format Docs → Semantic Chunking → Hybrid Vector/Graph Index → Contextual Query Expansion → Cross-Encoder Re-ranker → LLM Synthesizer",
        "dataset": "Enterprise Financial Disclosures & SEC 10-K Filings (over 850,000 paragraphs)",
        "tech_stack": "Python 3.11, PyTorch, Transformers, LangChain, FAISS, Milvus, Flask/FastAPI, Docker",
        "github_url": "https://github.com",
        "demo_url": "https://demo.example.com/cognitiverag",
        "featured": True
    },
    {
        "id": "auravision-edge-perception",
        "title": "AuraVision: Autonomous Video Perception & Anomaly Detector",
        "category": "vision",
        "category_name": "Computer Vision",
        "summary": "Real-time edge multi-camera surveillance and mobility perception system performing multi-class tracking, semantic segmentation, and anomaly classification at 60 FPS.",
        "image": "/static/images/project-vision.jpg",
        "metrics": "60 FPS on Edge Hardware • 98.1% Mean Average Precision (mAP@50)",
        "tags": ["PyTorch", "YOLOv8", "DeepSORT", "OpenCV", "TensorRT", "CUDA", "Flask"],
        "highlights": [
            "Trained and fine-tuned customized YOLOv8 perception models on edge scenarios with mixed lighting conditions.",
            "Converted models to TensorRT FP16 precision, reducing memory footprint by 58% while maintaining 98.1% mAP.",
            "Implemented DeepSORT multi-object tracking with trajectory vector prediction and dwell-time anomaly triggers.",
            "Engineered low-latency WebRTC and RTSP streaming pipeline with Flask API control layer."
        ],
        "architecture": "RTSP Video Stream → Frame Extraction Queue → TensorRT YOLOv8 Tensor Engine → DeepSORT Kalman Tracker → Spatial Anomaly Engine → Live Telemetry Dashboard",
        "dataset": "Custom Multi-Weather Urban Mobility Dataset (140,000 annotated camera frames)",
        "tech_stack": "Python, PyTorch, YOLOv8, OpenCV, DeepSORT, NVIDIA TensorRT, Flask, WebSocket",
        "github_url": "https://github.com",
        "demo_url": "https://demo.example.com/auravision",
        "featured": True
    },
    {
        "id": "alphaquant-algorithmic-forecasting",
        "title": "AlphaQuant: High-Throughput Quantitative Forecasting Engine",
        "category": "predictive",
        "category_name": "Predictive ML & Analytics",
        "summary": "End-to-end algorithmic risk forecasting platform utilizing Temporal Fusion Transformers and ensemble gradient boosting for multi-horizon asset prediction.",
        "image": "/static/images/project-predictive.jpg",
        "metrics": "0.0321 Validation Loss • 0.941 AUC-ROC • Sub-12ms Inference",
        "tags": ["Python", "XGBoost", "LightGBM", "PyTorch Forecasting", "Polars", "MLflow", "AWS"],
        "highlights": [
            "Built distributed feature engineering pipelines using Polars & PySpark, reducing processing time by 75% over legacy Pandas.",
            "Developed Temporal Fusion Transformer (TFT) with interpretable multi-head attention weights for macro factor attribution.",
            "Implemented automated walk-forward cross-validation preventing lookahead data leakage in financial time-series.",
            "Configured continuous model drift detection in MLflow, triggering automated retraining pipelines."
        ],
        "architecture": "Live Market Feeds → Polars Feature Store → Rolling Window Normalizer → TFT & XGBoost Ensemble → Monte Carlo Risk Simulator → REST API",
        "dataset": "10-Year High Frequency Tick & Macroeconomic Multi-Asset Time Series (4.2B data points)",
        "tech_stack": "Python, PyTorch Forecasting, LightGBM, Polars, Scikit-Learn, MLflow, AWS S3",
        "github_url": "https://github.com",
        "demo_url": "https://demo.example.com/alphaquant",
        "featured": True
    },
    {
        "id": "genefold-biomedical-ai",
        "title": "GeneFold-AI: 3D Biomolecular Structure & Sequence Deep Learning",
        "category": "bio",
        "category_name": "Deep Learning & Life Sciences",
        "summary": "Deep learning research suite for predicting 3D macromolecular structures, gene variant calling, and amino acid binding affinity scores.",
        "image": "/static/images/project-genomics.jpg",
        "metrics": "94.7% Folding Confidence (pLDDT) • 3D Interactive WebGL Rendering",
        "tags": ["Python", "Geometric Deep Learning", "PyTorch Geometric", "BioPython", "Three.js", "Docker"],
        "highlights": [
            "Implemented equivariant graph neural networks (EGNNs) modeling 3D spatial rotational and translational invariances.",
            "Constructed automated sequence parsing pipelines for FASTA, PDB, and genomic variant call files (VCF).",
            "Designed interactive 3D molecular viewer integrated with real-time residue confidence heatmaps.",
            "Benchmarked against standard CASP datasets with superior convergence rate."
        ],
        "architecture": "FASTA/MSA Sequence → Multiple Sequence Alignment Embeddings → Equivariant GNN → 3D Coordinate Recovery → Refinement & Confidence Scoring",
        "dataset": "Protein Data Bank (PDB) & UniProt Curated Sequences (over 180,000 structures)",
        "tech_stack": "Python, PyTorch Geometric, NetworkX, BioPython, NumPy, Flask, WebGL",
        "github_url": "https://github.com",
        "demo_url": "https://demo.example.com/genefold",
        "featured": True
    },
    {
        "id": "neurosentinel-fraud-stream",
        "title": "NeuroSentinel: Real-Time Fraud & Anomaly Stream Intelligence",
        "category": "predictive",
        "category_name": "Predictive ML & Analytics",
        "summary": "Streaming transaction intelligence platform detecting zero-day fraud rings with real-time Graph Neural Networks and Isolation Forests.",
        "image": "/static/images/project-predictive.jpg",
        "metrics": "99.2% True Positive Rate • 4.8M Daily Transactions • <15ms Latency",
        "tags": ["Python", "Graph Neural Networks", "Kafka", "Scikit-Learn", "Redis", "Docker"],
        "highlights": [
            "Constructed dynamic graph embeddings identifying money-mule collusion rings across transaction networks.",
            "Integrated Redis feature store caching sub-second user behavioral aggregations.",
            "Achieved 99.2% detection rate while cutting false customer purchase declines by 34%."
        ],
        "architecture": "Kafka Event Stream → Real-time Redis Feature Lookups → Dynamic GNN Inference → Threshold Decision Engine → Alert Webhook",
        "dataset": "Anonymized Multi-Institution Financial Transaction Stream (50M+ events)",
        "tech_stack": "Python, PyTorch, PyG, Apache Kafka, Redis, Scikit-Learn, Docker",
        "github_url": "https://github.com",
        "demo_url": "https://demo.example.com/neurosentinel",
        "featured": False
    }
]

EXPERIENCES = [
    {
        "role": "Senior Data Scientist / Machine Learning Lead",
        "company": "Apex Intelligent Systems",
        "period": "2023 - Present",
        "location": "Bangalore, India",
        "type": "Full-time",
        "description": "Leading the core applied AI team developing enterprise LLM applications, predictive modeling infrastructure, and production ML pipelines.",
        "achievements": [
            "Architected and deployed enterprise-grade RAG and LLM systems serving 100,000+ daily employee queries with 94%+ answer relevance.",
            "Optimized deep learning training clusters on AWS SageMaker, cutting GPU infrastructure compute bills by 32%.",
            "Designed automated model governance and drift detection pipelines via MLflow and Prometheus, achieving 99.9% inference reliability.",
            "Mentored team of 5 junior data scientists and engineers in best software practices, PyTorch optimization, and CI/CD."
        ],
        "technologies": ["Python", "PyTorch", "LLMs", "LangChain", "AWS SageMaker", "Docker", "MLflow", "FastAPI"]
    },
    {
        "role": "Machine Learning Engineer",
        "company": "DataSphere Analytics Lab",
        "period": "2021 - 2023",
        "location": "Bangalore, India",
        "type": "Full-time",
        "description": "Developed high-scale predictive algorithms, computer vision models, and streaming data analytics solutions for global clients.",
        "achievements": [
            "Constructed an automated churn prediction and lifetime value forecasting engine that increased customer retention by 18%.",
            "Built edge-compatible computer vision models using YOLO and OpenCV, deployed on embedded hardware with ONNX runtime.",
            "Engineered distributed feature pipelines with Apache Spark and PostgreSQL, speeding up ETL batch runs by 4x.",
            "Created reusable Python data science libraries for statistical testing and automated exploratory data analysis."
        ],
        "technologies": ["Python", "Scikit-Learn", "TensorFlow", "YOLO", "PySpark", "PostgreSQL", "Flask", "Git"]
    },
    {
        "role": "Data Science Associate",
        "company": "Cognitive Insights Tech",
        "period": "2020 - 2021",
        "location": "Hyderabad, India",
        "type": "Full-time",
        "description": "Collaborated with cross-functional product and engineering teams on statistical data modeling, hypothesis testing, and executive reporting.",
        "achievements": [
            "Conducted exploratory data analysis on 10M+ transactional rows, discovering key user behavior clusters via unsupervised K-Means.",
            "Built interactive executive dashboards using Streamlit and Plotly, enabling C-suite decision-makers to track real-time KPIs.",
            "Standardized data cleaning and outlier detection modules, reducing missing data discrepancies by 45%."
        ],
        "technologies": ["Python", "Pandas", "NumPy", "SQL", "Scikit-Learn", "Streamlit", "Plotly", "Matplotlib"]
    }
]

EDUCATION = [
    {
        "degree": "Bachelor of Technology in Computer Science & Engineering",
        "institution": "National Institute of Technology",
        "period": "2016 - 2020",
        "grade": "First Class with Distinction",
        "details": "Specialized coursework in Machine Learning, Probability & Statistics, Data Structures & Algorithms, Database Management."
    }
]

CERTIFICATIONS = [
    {
        "title": "AWS Certified Machine Learning – Specialty",
        "issuer": "Amazon Web Services",
        "year": "2023",
        "badge": "AWS ML"
    },
    {
        "title": "Deep Learning Specialization",
        "issuer": "DeepLearning.AI (Andrew Ng)",
        "year": "2022",
        "badge": "DL Specialization"
    },
    {
        "title": "Natural Language Processing with Transformers",
        "issuer": "Hugging Face",
        "year": "2023",
        "badge": "Hugging Face"
    }
]
