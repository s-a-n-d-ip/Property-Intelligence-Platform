# 🏠 Property Intelligence Platform

An end-to-end **Machine Learning and Property Intelligence Platform** that combines **property price prediction, interactive analytics, geospatial property discovery, and similarity-based apartment recommendations** into a single application.

The project demonstrates the complete journey from raw property data and machine learning experimentation to a **multi-page application, Docker containerization, and cloud deployment on AWS EC2**.

---

## 🎥 Project Demo

A complete demonstration of the application is available below.

The demo shows:

- 🏠 Property price prediction
- 📊 Property analytics
- 📍 Location-based apartment search
- 📏 Radius-based nearby apartment discovery
- 🤝 Similar apartment recommendations
- ☁️ The application running in a deployed environment

**[▶️ Watch the Project Demo](./demo/property-intelligence-demo.mp4)**

---

## 🚀 Project Overview

The goal of this project was to build more than a traditional machine learning model.

The platform combines machine learning, analytics, geospatial processing, and recommendation functionality to create an interactive property intelligence application.

### Major Components

1. 🏠 Property Price Prediction
2. 📊 Property Analytics
3. 📍 Geospatial Property Search
4. 🏢 Nearby Apartment Discovery
5. 🤝 Similar Apartment Recommendation
6. 🧠 Machine Learning and Feature Engineering
7. 🐳 Dockerized Application
8. ☁️ AWS EC2 Deployment

### Overall System

```text
                         PROPERTY INTELLIGENCE PLATFORM
                                      │
             ┌────────────────────────┼────────────────────────┐
             │                        │                        │
             ▼                        ▼                        ▼
      Price Prediction            Analytics             Recommendations
             │                        │                        │
             ▼                        ▼                        ▼
       ML Pipeline             Property Insights       Location Selection
                                                              │
                                                              ▼
                                                        Radius Selection
                                                              │
                                                              ▼
                                                     Nearby Apartments
                                                              │
                                                              ▼
                                                     Select Apartment
                                                              │
                                                              ▼
                                                   Similarity Analysis
                                                              │
                                                              ▼
                                                    Similar Apartments
```

---

## ✨ Key Features

### 🏠 1. Property Price Prediction

The platform provides a machine learning-based property price prediction system.

Users can enter property characteristics such as:

- Location / Sector
- Property type
- Built-up area
- Number of bedrooms
- Number of bathrooms
- Other relevant property attributes

The application processes the input through the trained machine learning pipeline and returns an estimated property price.

### Prediction Workflow

```text
User Input
    │
    ▼
Input Processing
    │
    ▼
Feature Transformation
    │
    ▼
Trained ML Pipeline
    │
    ▼
Predicted Property Price
```

The final trained pipeline is stored as:

```text
artifacts/final_pipeline.pkl
```

---

### 📊 2. Property Analytics

The application contains a dedicated analytics page for exploring property-related information.

Users can interact with the available property information and obtain insights through visualizations and summaries.

The analytics functionality can be used to explore:

- Property distributions
- Property characteristics
- Location-related information
- Price-related patterns
- Market information
- Relationships between property attributes

The analytics page is implemented in:

```text
app/pages/analysis_App.py
```

Precomputed visualization-related information is stored in:

```text
artifacts/data_viz1.pkl
```

---

### 📍 3. Geospatial Property Search

The platform incorporates geographical information to enable location-aware property discovery.

Properties are associated with geographical coordinates such as:

```text
Latitude
Longitude
```

Users can select a location and specify a search radius.

The application then identifies apartments located within the selected geographic area.

### Geospatial Workflow

```text
Selected Location
       │
       ▼
Latitude + Longitude
       │
       ▼
Distance Calculation
       │
       ▼
Radius Filtering
       │
       ▼
Nearby Properties
```

The project contains a dedicated coordinate data directory:

```text
data/coordinates/
```

---

### 🏢 4. Nearby Apartment Discovery

The recommendation page allows users to select a location and radius to discover apartments nearby.

```text
Location → Selected Area
Radius   → User-defined Distance
```

The system searches the available property information and returns apartments within the selected geographic radius.

---

### 🤝 5. Similar Apartment Recommendation

After finding nearby apartments, the user can select a specific apartment.

The platform then uses the selected apartment as a reference point and identifies similar apartments around that location.

### Recommendation Workflow

```text
User Selects Location
        │
        ▼
User Selects Radius
        │
        ▼
Find Nearby Apartments
        │
        ▼
User Selects an Apartment
        │
        ▼
Analyze Selected Apartment
        │
        ▼
Similarity Analysis
        │
        ▼
Similar Apartments
        │
        ▼
Recommendations
```

The recommendation functionality uses precomputed similarity artifacts:

```text
artifacts/
├── cosine_sim1.pkl
├── cosine_sim2.pkl
└── cosine_sim3.pkl
```

The recommendation interface is implemented in:

```text
app/pages/Recommend_Appartments.py
```

---

## 🧠 Machine Learning Workflow

```text
Raw Property Data
       │
       ▼
Data Cleaning
       │
       ▼
Exploratory Data Analysis
       │
       ▼
Feature Engineering
       │
       ▼
Feature Selection
       │
       ▼
Model Training
       │
       ▼
Hyperparameter Optimization
       │
       ▼
Model Evaluation
       │
       ▼
Final ML Pipeline
       │
       ▼
Model Serialization
```

---

## ⚙️ Hyperparameter Optimization with Optuna

**Optuna** was used for hyperparameter optimization during model development.

Instead of relying entirely on manually selected parameters, Optuna was used to systematically search for better-performing hyperparameter combinations.

### Optimization Workflow

```text
Model
  │
  ▼
Optuna Optimization
  │
  ├── Trial 1
  ├── Trial 2
  ├── Trial 3
  ├── ...
  └── Trial N
        │
        ▼
Best Hyperparameters
        │
        ▼
Final Model
```

---

## 🧩 Feature Engineering

Feature engineering was performed to transform raw property information into useful features for machine learning and downstream analysis.

The project separates different stages of the data processing workflow:

```text
data/
├── raw/
├── interim/
├── cleaned/
├── feature_engineered/
├── feature_selection/
├── merged/
└── coordinates/
```

The feature engineering workflow includes:

- Cleaning property attributes
- Processing numerical features
- Processing categorical features
- Creating derived features
- Preparing location-related information
- Selecting useful features
- Preparing data for machine learning
- Preparing data for analytics and recommendations

---

## 🧠 Word2Vec

**Word2Vec** was incorporated into the project for vector-based representation and similarity-related processing.

```text
Property / Location Information
          │
          ▼
       Word2Vec
          │
          ▼
Vector Representation
          │
          ▼
Similarity Analysis
          │
          ▼
Similar Properties
```

The project also contains:

```text
artifacts/WordCloud_feature_text.pkl
```

---

## 🗺️ Geospatial Analysis

The geospatial component enables the platform to work with real-world property locations.

Property coordinates are used for:

- Location-based property discovery
- Radius-based searches
- Nearby apartment identification
- Geographic visualization
- Location-aware recommendations

---

## 📈 Similarity and Recommendation System

The recommendation component combines property information, location information, and similarity calculations.

Precomputed similarity artifacts are stored in:

```text
artifacts/
├── cosine_sim1.pkl
├── cosine_sim2.pkl
└── cosine_sim3.pkl
```

### Recommendation Workflow

```text
Nearby Properties
       │
       ▼
User Selects Property
       │
       ▼
Property Representation
       │
       ▼
Similarity Analysis
       │
       ▼
Rank Similar Properties
       │
       ▼
Recommended Apartments
```

---

## 🏗️ Application Architecture

```text
                         USER
                           │
                           ▼
                  ┌─────────────────┐
                  │   Streamlit UI  │
                  └────────┬────────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
 Price Prediction       Analytics       Recommendations
        │                  │                  │
        ▼                  ▼                  ▼
 ML Pipeline          Analytics Data     Geospatial Search
                                             │
                                             ▼
                                      Nearby Apartments
                                             │
                                             ▼
                                      Select Apartment
                                             │
                                             ▼
                                      Similarity Analysis
                                             │
                                             ▼
                                        Recommendations
```

---

## 🖥️ Application Pages

### Home

```text
app/Home.py
```

Main entry point of the Streamlit application.

### Price Prediction

```text
app/pages/price_predictor.py
```

Provides the property price prediction interface.

### Analytics

```text
app/pages/analysis_App.py
```

Provides interactive property analytics and data insights.

### Apartment Recommendations

```text
app/pages/Recommend_Appartments.py
```

Provides:

- Location selection
- Radius selection
- Nearby apartment discovery
- Apartment selection
- Similar apartment recommendations

---

## 🔌 API

The project also contains an API component:

```text
app/api.py
```

The API provides a separate interface for programmatic interaction with application functionality.

---

## 📦 Model and Application Artifacts

```text
artifacts/
│
├── cosine_sim1.pkl
├── cosine_sim2.pkl
├── cosine_sim3.pkl
├── data_viz1.pkl
├── final_pipeline.pkl
├── location_df.pkl
└── WordCloud_feature_text.pkl
```

| Artifact | Purpose |
|---|---|
| `final_pipeline.pkl` | Trained machine learning preprocessing and prediction pipeline |
| `cosine_sim1.pkl` | Similarity information used by the recommendation system |
| `cosine_sim2.pkl` | Similarity information based on feature used by the recommendation system |
| `cosine_sim3.pkl` | Similarity information based on distance used by the recommendation system |
| `location_df.pkl` | Location/property information used by the application |
| `data_viz1.pkl` | Precomputed data used for analytics and visualization |
| `WordCloud_feature_text.pkl` | Text data used for word-cloud functionality |

---

## 📂 Project Structure

```text
Property-Intelligence-Platform/
│
├── .vscode/
│   └── settings.json
│
├── app/
│   ├── pages/
│   │   ├── analysis_App.py
│   │   ├── price_predictor.py
│   │   └── Recommend_Appartments.py
│   ├── api.py
│   ├── Home.py
│   └── house_price_app.py
│
├── artifacts/
│   ├── cosine_sim1.pkl
│   ├── cosine_sim2.pkl
│   ├── cosine_sim3.pkl
│   ├── data_viz1.pkl
│   ├── final_pipeline.pkl
│   ├── location_df.pkl
│   └── WordCloud_feature_text.pkl
│
├── data/
│   ├── cleaned/
│   ├── coordinates/
│   ├── feature_engineered/
│   ├── feature_selection/
│   ├── interim/
│   ├── merged/
│   └── raw/
│
├── demo/
│   └── property-intelligence-demo.mp4
│
├── notebooks/
│   └── ...
│
├── reports/
│   └── ...
│
├── src/
│   └── ...
│
├── .dockerignore
├── .gitignore
├── Dockerfile
├── main.py
├── README.md
├── requirements.txt
├── requirements-lock.txt
└── start.sh
```

> `property-platform-env/` is a local virtual environment and should not be committed to GitHub.

---

## 🛠️ Technology Stack

### Programming
- Python

### Data Processing
- Pandas
- NumPy

### Machine Learning
- Scikit-learn
- Optuna
- Word2Vec

### Visualization & Analytics
- Streamlit
- Matplotlib
- Seaborn
- Geospatial visualization tools

### Application
- Streamlit
- Python API

### Deployment
- Docker
- Ubuntu/Linux
- AWS EC2

### Development & Version Control
- Git
- GitHub
- VS Code

---

## 🔄 End-to-End Project Workflow

```text
                         RAW PROPERTY DATA
                                │
                                ▼
                         DATA INGESTION
                                │
                                ▼
                         DATA VALIDATION
                                │
                                ▼
                          DATA CLEANING
                                │
                                ▼
                     EXPLORATORY ANALYSIS
                                │
                                ▼
                      FEATURE ENGINEERING
                                │
                                ▼
                       FEATURE SELECTION
                                │
                                ▼
                       MODEL DEVELOPMENT
                                │
                                ▼
                 OPTUNA HYPERPARAMETER OPTIMIZATION
                                │
                                ▼
                         MODEL EVALUATION
                                │
                                ▼
                       FINAL ML PIPELINE
                                │
                                ▼
                       MODEL SERIALIZATION
                                │
                                ▼
                     APPLICATION DEVELOPMENT
                                │
              ┌─────────────────┼─────────────────┐
              │                 │                 │
              ▼                 ▼                 ▼
       Price Prediction      Analytics      Recommendations
                                                   │
                                      ┌────────────┴────────────┐
                                      │                         │
                                      ▼                         ▼
                               Geospatial Search          Similarity
                                      │                    Analysis
                                      ▼                         │
                               Nearby Apartments              │
                                      │                         │
                                      └────────────┬────────────┘
                                                   ▼
                                          User Recommendations
                                                   │
                                                   ▼
                                                Docker
                                                   │
                                                   ▼
                                               AWS EC2
```

---

## 🐳 Dockerization

The application was containerized using Docker to provide a consistent and reproducible runtime environment.

### Build the Docker Image

```bash
docker build -t property-intelligence .
```

### Run the Container

```bash
docker run -d -p 8501:8501 property-intelligence
```

### Check Running Containers

```bash
docker ps
```

### View Container Logs

```bash
docker logs <container_name>
```

---

## ☁️ AWS EC2 Deployment

The Dockerized application was successfully deployed and tested on an **AWS EC2 Ubuntu instance**.

### Deployment Architecture

```text
                         AWS CLOUD
                            │
                            ▼
                    ┌───────────────┐
                    │     EC2       │
                    │    Ubuntu     │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │ Docker Engine │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │    Docker     │
                    │   Container   │
                    └───────┬───────┘
                            │
                            ▼
                Property Intelligence
                    Application
```

### Deployment Workflow

```text
Local Application
       │
       ▼
Docker Build
       │
       ▼
Docker Image
       │
       ▼
AWS EC2
       │
       ▼
Docker Engine
       │
       ▼
Running Container
       │
       ▼
Application Testing
```

The deployed application was accessed through the browser and tested after the container was started on the EC2 instance.

> The AWS deployment was hosted temporarily for testing and demonstration purposes. The cloud resources may be taken down after validation to avoid unnecessary ongoing infrastructure costs.

---

## 🔐 Security

Sensitive credentials and infrastructure secrets should never be committed to the repository.

Never commit:

- AWS private keys
- `.pem` files
- AWS access keys
- AWS secret keys
- API keys
- Authentication tokens
- Passwords
- `.env` files
- Database credentials

Example `.gitignore` entries:

```gitignore
.venv/
venv/
property-platform-env/
__pycache__/
*.pyc
.env
*.pem
*.key
```

---

## 🧪 Testing and Validation

### Machine Learning

- Data preprocessing validation
- Feature engineering validation
- Feature selection
- Model evaluation
- Hyperparameter optimization
- Final pipeline validation

### Application

- Application startup
- User input handling
- Price prediction
- Analytics functionality
- Location search
- Radius filtering
- Apartment selection
- Similar-property recommendations

### Deployment

- Docker image creation
- Docker container startup
- Container status verification
- Container log inspection
- Cloud-hosted application testing

---

## 🎯 Project Objectives

1. Build an end-to-end property price prediction system.
2. Develop a reusable machine learning pipeline.
3. Apply hyperparameter optimization using Optuna.
4. Build an interactive property analytics platform.
5. Integrate geographical information into the application.
6. Implement radius-based nearby property discovery.
7. Build a similarity-based property recommendation system.
8. Incorporate Word2Vec into the similarity workflow.
9. Build a multi-page Streamlit application.
10. Package the application using Docker.
11. Deploy and test the containerized application on AWS EC2.

---

## 💡 Engineering Highlights

### Machine Learning
- End-to-end preprocessing pipeline
- Feature engineering
- Feature selection
- Model evaluation
- Optuna hyperparameter optimization
- Model serialization

### Recommendation System
- Property similarity analysis
- Cosine similarity
- Word2Vec-based representation
- Location-aware recommendations

### Geospatial System
- Property coordinates
- Latitude/longitude processing
- Radius-based search
- Nearby property discovery
- Geographic visualization

### Application Engineering
- Multi-page Streamlit application
- Price prediction interface
- Analytics interface
- Recommendation interface
- API component
- Serialized application artifacts

### Deployment
- Docker containerization
- Linux/Ubuntu environment
- AWS EC2 deployment
- Cloud-based application testing

---

## 📚 Key Learnings

This project helped me understand the complete journey from machine learning experimentation to application deployment.

The major concepts explored were:

- Data preprocessing
- Feature engineering
- Feature selection
- Machine learning pipelines
- Hyperparameter optimization
- Model serialization
- Word embeddings
- Similarity analysis
- Recommendation systems
- Geospatial search
- Data visualization
- Interactive dashboards
- Streamlit application development
- API development
- Docker
- Linux server administration
- AWS EC2
- Cloud deployment

A major objective was to understand the difference between:

```text
ML Experiment
      │
      ▼
Trained Model
```

and:

```text
ML Model
   │
   ▼
Reusable Pipeline
   │
   ▼
Application
   │
   ▼
Docker Container
   │
   ▼
Cloud Deployment
```

---

## 🚧 Future Improvements

Potential improvements include:

- CI/CD using GitHub Actions
- Automated unit and integration testing
- Model monitoring
- Application monitoring
- Model versioning
- Centralized model/artifact storage
- HTTPS and custom domain
- Authentication and authorization
- Improved recommendation algorithms
- More advanced geospatial filtering
- Improved similarity metrics
- Production-grade API architecture
- Scalable cloud infrastructure
- Automated Docker image builds and deployment
- Cloud-based logging and monitoring

---

## 📌 Deployment Status

The application has been **Dockerized and successfully deployed and tested on AWS EC2**.

The cloud deployment was intended for testing, learning, and demonstration purposes and may be taken down after validation to avoid unnecessary infrastructure costs.

The project remains reproducible through the source code, Docker configuration, dependency files, and serialized artifacts maintained in the repository.

---

## 👨‍💻 Author

### Sandip Ghosh

**Machine Learning | Python | MLOps | Docker | AWS**

---

## ⭐ Project Highlights

```text
✓ End-to-End Machine Learning Pipeline
✓ Property Price Prediction
✓ Optuna Hyperparameter Optimization
✓ Feature Engineering
✓ Feature Selection
✓ Word2Vec
✓ Property Similarity Analysis
✓ Cosine Similarity
✓ Geospatial Property Search
✓ Radius-Based Apartment Discovery
✓ Similar Apartment Recommendation
✓ Interactive Property Analytics
✓ Multi-Page Streamlit Application
✓ API Component
✓ Model Serialization
✓ Docker Containerization
✓ AWS EC2 Deployment
✓ Linux Deployment
✓ Reproducible Environment
```

---

## 📜 License

This project is intended for educational, portfolio, and demonstration purposes.
