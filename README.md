# **Mobile-Phone-Classification**

[View the app on Hugging Face](https://huggingface.co/spaces/Sashi1922/SmartPriceTag)

Predicting the price range of mobile phones based on their features is crucial for **market analysis**, **competitive pricing**, and **customer segmentation**. This project leverages machine learning techniques to classify mobile phones into different price categories based on their specifications.

## 📊 **Dataset Overview**

The dataset consists of approximately 2,000 entries, each representing a mobile phone with various features that influence its pricing. These features include battery power, RAM, internal memory, camera specifications, screen resolution, processor speed, and more. The goal of the model is to classify mobile phones into different price ranges based on these attributes.

The target variable categorizes mobile phones into four price segments:

- **0** – Low-cost  
- **1** – Medium-cost  
- **2** – High-cost  
- **3** – Very high-cost  

This classification helps in understanding how different features contribute to the pricing of mobile devices.

## 🏗️ **Model Development**

To identify the best-performing model, multiple classification algorithms were evaluated using key performance metrics, including **accuracy**, **precision**, **recall**, and **F1-score**. After thorough analysis, the **Decision Tree model** emerged as the most effective choice, demonstrating a strong balance across all evaluation criteria. This model was selected based on its ability to accurately classify mobile phones into their respective price ranges while maintaining a high recall and precision, ensuring reliable predictions.

## 🛠️ **Tech Stack & Tools**
- **Python** (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)
- **Machine Learning Algorithms**
- **Feature Engineering & Data Preprocessing**
- **Streamlit** for deployment
- **Pickle** for model serialization

## 🌐 **Model Deployment**
The trained model is deployed using **Streamlit**, allowing users to input mobile phone specifications and predict the price category!

## 📌 **Author:** Sashini Shayamindi  
*Machine Learning enthusiast*
