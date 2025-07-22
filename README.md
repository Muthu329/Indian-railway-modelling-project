
🚆 Railway Accident Risk Analytics & Modeling in India (1902–2024)

📊 End-to-End Data Science Project | By [Muthuraj]


---

🧠 Overview

This project aims to analyze and model railway accidents in India using a combination of historical records, environmental data, human error reports, maintenance schedules, and geospatial railway data. The goal is to extract actionable insights, identify accident risk factors, and build predictive models to enhance railway safety and inform future decision-making.


---

📁 Datasets Used

File	Description

Indian_Railways_Accidents_Dataset_1902_2024.xlsx	Historical accident records
Environmental_Factors.csv	Weather and environmental data
Historical_Weather.csv	Supplementary weather data
Human_Error_Factors.csv	Reports on human-caused incidents
Maintenance_Schedules_Log.csv	Rail inspection and maintenance logs
hotosm_ind_railways_lines.csv	Railway line geospatial data
hotosm_ind_railways_points.csv	Railway station/location data



---

🔧 Tech Stack

Language: Python

Environment: Google Colab

Libraries: pandas, numpy, matplotlib, seaborn, sklearn, datetime, geopandas



---

📌 Project Workflow

1. 🧹 Data Cleaning

Removed missing values

Handled outliers and inconsistencies

Converted date columns to datetime objects

Merged datasets using keys like station names and dates


2. 📊 Exploratory Data Analysis (EDA)

Visualized accident frequency, seasonality, type trends

Mapped high-risk zones using geospatial plots

Correlated human error and weather to incident spikes


3. ⚙️ Feature Engineering

Created accident severity scores

Merged weather and maintenance features into a unified timeline

Encoded categorical features


4. 🤖 Predictive Modeling

Built models to predict accident likelihood

Decision Tree

Random Forest


Evaluated using accuracy and confusion matrix


5. 📈 Insights & Business Impact

Identified top accident contributors

Visualized when and where accidents are most likely to occur

Recommended predictive maintenance windows



---

✅ Conclusion

This data science project successfully integrates multi-source datasets to:

Uncover root causes of rail accidents

Highlight patterns by season, region, and operation

Predict risk with ~80% model accuracy

Offer a foundation for real-time alert systems