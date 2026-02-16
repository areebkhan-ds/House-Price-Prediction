House Price Prediction
Overview

This project focuses on predicting house prices using machine learning techniques. The objective is to build a predictive model that can estimate the selling price of a house based on its features. The model is evaluated based on accuracy and can assist real estate agents, buyers, and sellers in making data-driven decisions.

Dataset and Features

The dataset contains 21,613 records and 21 features:

Column	Description
id	Unique identifier for each house
date	Date of sale
price	Sale price of the house (target variable)
bedrooms	Number of bedrooms
bathrooms	Number of bathrooms
sqft_living	Square footage of living space
sqft_lot	Square footage of the lot
floors	Number of floors
waterfront	Presence of waterfront property (0 = No, 1 = Yes)
view	Quality of view
condition	Condition of the house
grade	Overall grade of the house based on construction and design
sqft_above	Square footage of house apart from basement
sqft_basement	Square footage of basement
yr_built	Year the house was built
yr_renovated	Year the house was renovated (0 if never renovated)
zipcode	ZIP code of the house
lat	Latitude coordinate
long	Longitude coordinate
sqft_living15	Average square footage of living space of 15 nearest neighbors
sqft_lot15	Average lot size of 15 nearest neighbors

Note: All features are complete with no missing values.

Methodology

Since only accuracy is computed, the model evaluation is based solely on accuracy score. No additional metrics or feature engineering have been applied in this version.

Data Preprocessing

Basic data cleaning

Feature selection includes all columns except id and date

Model

A single regression model was trained to predict price

Performance is evaluated using accuracy (coefficient of determination or R² score)

Results

The trained model achieved an accuracy of Linear Regression Score: 0.70260409319793
Forest Regression Score: 0.8535704027007335]

Note: Accuracy is the only evaluation metric used in this project.

Installation

To run the project locally:

# Clone the repository
git clone https://github.com/areebkhan-ds/house-price-prediction.git
cd house-price-prediction

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run the notebook
jupyter notebook

Dependencies

Python >= 3.8

pandas, numpy

scikit-learn

Jupyter Notebook

Author

Areeb Khan – Data Science Enthusiast & Machine Learning Developer
GitHub Profile
