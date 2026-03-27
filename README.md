# Network Anomaly Detection & Secure Model Deployment (MLSECOPS)

This project implements a network anomaly detection system using the NSL-KDD dataset and a Random Forest classifier. The project is designed from an AI Security / MLSECOPS perspective, demonstrating secure model handling, preprocessing consistency, model serialization risks, and model deployment via an API.

---

# Project Overview
The goal of this project is to build a machine learning-based intrusion detection system that can classify network traffic as normal or different types of attacks. The project also demonstrates the security risks associated with machine learning model serialization, transfer, and deployment.

This project covers:
- Network anomaly detection using Random Forest
- Data preprocessing and feature engineering
- Multi-class attack classification
- Model evaluation and performance metrics
- Model serialization using joblib
- Secure model upload to an API
- AI/ML security and model deserialization risks
- MLSECOPS workflow

---

# Machine Learning Pipeline
The network anomaly detection pipeline follows these steps:

NSL-KDD Dataset  
→ Data Preprocessing  
→ Binary Target Creation (Normal vs Attack)  
→ Multi-Class Attack Mapping  
→ One-Hot Encoding (protocol, service)  
→ Numeric Feature Selection  
→ Feature Combination  
→ Train / Validation / Test Split  
→ Random Forest Training  
→ Validation Evaluation  
→ Test Evaluation  
→ Confusion Matrix & Classification Report  
→ Model Serialization (joblib)  
→ Model Upload to API  

---

# Attack Categories
The model classifies traffic into the following categories:

| Label | Category |
|------|----------|
| 0 | Normal |
| 1 | DoS |
| 2 | Probe |
| 3 | Privilege Escalation |
| 4 | Access Attack |

This allows the model to detect anomalies and classify the type of attack.

---

# Model Training
The model used is a Random Forest Classifier, which is suitable for intrusion detection because it:
- Handles large datasets
- Works with encoded categorical and numeric features
- Is resistant to overfitting
- Captures nonlinear relationships
- Performs well on anomaly detection datasets

The model is evaluated using:
- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Classification Report

---

# Model Serialization & Security Risk
The trained model is saved using joblib:

joblib.dump(model, "network_anomaly_detection_model.joblib")

Joblib uses Python pickle internally, which introduces a security risk.

Security Warning:
Loading a malicious pickle/joblib file can execute arbitrary code on the system.  
Only load models from trusted sources.

This is known as:
- Model Deserialization Attack
- Pickle Remote Code Execution
- ML Model Supply Chain Attack

---

# Model Upload & API Interaction
The project includes a script that uploads the trained model to an API endpoint:

POST /api/upload

This simulates a real-world ML deployment scenario where models are uploaded and evaluated by a server. If model files are not validated properly, this can lead to security vulnerabilities.

---

# AI Security / MLSECOPS Perspective
This project demonstrates several AI security concepts:

1. Data Poisoning Risk  
   Attackers may manipulate training data to influence model behavior.

2. Model Deserialization Risk  
   Loading untrusted joblib/pickle models can lead to remote code execution.

3. Model Supply Chain Attacks  
   Attackers may upload malicious models to compromise ML systems.

4. Untrusted Input Handling  
   Uploaded models and network traffic data must be treated as untrusted input.

5. MLSECOPS Workflow  
   Secure training, storage, transfer, loading, and monitoring of ML models.

---

# Project Structure
Anomaly_Detection/
│
├── downloading_Loading_dataset.py
├── preprocessing_splitting.py
├── training_evaluation.py
├── Evaluate.py
├── network_anomaly_detection_model.joblib
├── requirements.txt
└── README.md

---

# Technologies Used
- Python
- Scikit-learn
- Pandas
- NumPy
- Seaborn
- Matplotlib
- Joblib
- Requests
- Random Forest
- NSL-KDD Dataset

---

# Conclusion
This project demonstrates how to build a machine learning-based network intrusion detection system and highlights the security risks associated with machine learning model serialization and deployment. From an AI security perspective, it shows how machine learning models can become attack vectors if secure loading and validation mechanisms are not implemented.

---

# Author
Darsh Dave
