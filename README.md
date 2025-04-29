# End-to-End Fraud Detection System with Vertex AI

## Project Overview
This project aims to build a fraud detection model for credit card transactions and deploy it into production using Google Cloud's Vertex AI services.

## Dataset
- Source: Kaggle Credit Card Fraud Detection Dataset
- Description: 284,807 transactions, 492 frauds (0.172% of all transactions).

## Goals
- Build a supervised learning model to detect fraudulent transactions.
- Deploy the model to a live API using Vertex AI.
- Build a minimal FastAPI server to serve predictions.

## Technologies
- Python
- Scikit-learn
- XGBoost
- Vertex AI
- FastAPI
- GCP Storage, BigQuery (optional)

## Folder Structure
- `/data`: raw and processed data
- `/notebooks`: exploration and training notebooks
- `/src`: data processing and model scripts
- `/deployment/api_app`: API server code
- `/vertex_ai`: GCP deployment notebooks

## Author
[Your Name]
