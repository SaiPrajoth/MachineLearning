# IRIS Flower Data Prediction

**Table of Contents:**

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Credits](#credits)

## Overview

Welcome to the IRIS Flower Data Prediction project! This project is a simple web application that uses a machine learning logistic regression model to predict the species of an IRIS flower based on its sepal and petal measurements. Whether you're a developer or someone curious about machine learning, this project will help you understand the process.

The project consists of the following components:
- A Flask web application for user interaction
- A trained logistic regression model for predictions
- An HTML template for the web interface
- Custom CSS for styling

## Prerequisites

Before you start, make sure you have the following installed on your machine:
- Python
- Flask
- scikit-learn
- pandas
- matplotlib
- Bootstrap (CSS framework)

You can install these dependencies using `pip`, Python's package manager.

```bash
pip install flask scikit-learn pandas matplotlib
```

## Getting Started

1. Clone this repository to your local machine.

2. Open your terminal and navigate to the project directory.

3. Make sure you have the IRIS dataset CSV file (`Iris.csv`) in the project directory. You can obtain this dataset from various sources online.

4. Train the logistic regression model by running the `LogisticRegressionII.py` script. This will read the dataset, preprocess it, and save the trained model as 'model.pkl'.

```bash
python LogisticRegressionII.py
```

5. With the model trained, you can start the web application by running `app.py`.

```bash
python app.py
```

The app should be running at `http://127.0.0.1:5000/`. Open your web browser and navigate to this URL.

## Usage

1. In your web browser, you will see a simple form that asks for sepal and petal measurements.

2. Enter the measurements for the IRIS flower you want to predict and click the "Submit" button.

3. The web application will use the trained logistic regression model to predict the flower's species based on the provided measurements.

4. The prediction result will be displayed on the page.

## Project Structure

- `app.py`: The Flask web application.
- `LogisticRegressionII.py`: The script for training the logistic regression model and saving it.
- `templates/frontend.html`: The HTML template for the web page.
- `frontend.css`: Custom CSS for styling the web page.
- `Iris.csv`: The dataset for training the model.

## Credits

- This project uses Flask for creating the web application.
- The logistic regression model is implemented using scikit-learn.
- Bootstrap is used for styling the web page.

Enjoy exploring the world of machine learning with the IRIS Flower Data Prediction project! If you have any questions or run into any issues, please feel free to reach out for assistance.
