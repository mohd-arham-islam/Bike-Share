# Bike Share Demand Prediction
This project aims to predict the demand for rental bikes using a comprehensive dataset that includes hourly bike rental counts and corresponding weather conditions. The goal is to employ regression analysis techniques to accurately forecast the required number of bikes for each hour, thus enhancing the user experience and mobility convenience provided by rental bike providers.

![image](https://github.com/mohd-arham-islam/Bike-Share/assets/111959286/4ad471ed-849c-4ae2-9949-41cd9e043eb4)

## Exploratory Data Analysis (EDA)
During the exploratory phase of the project, several insightful visualizations were created to better understand the dataset:

### Monthly Bike Rental Variation
A bar chart depicting the variation of rented bike counts monthwise revealed interesting patterns. The lowest bike rental counts were observed during the winter months (December to February), while the highest counts were in June. This highlights a clear seasonal trend, with demand peaking during the warmer summer months.

![image](https://github.com/mohd-arham-islam/Bike-Share/assets/111959286/0c8d67a5-ab93-41a9-a57c-303322b705a0)


### Weekly Variations in Bike Rentals
Analyzing the day-wise variation in rented bikes showed consistent counts from Monday to Friday, with a slight dip on weekends. This suggests a potential relationship between bike availability and weekday versus weekend demand. Remarkably, the minimal variation between the highest and lowest bike rentals throughout the week indicates stable demand patterns, aiding effective planning for rental bike providers.

![image](https://github.com/mohd-arham-islam/Bike-Share/assets/111959286/2cc0079d-7aa7-445b-a3bb-e5dfc138033b)


### Hourly Fluctuations in Bike Rentals
Hourly fluctuations were visualized through a line chart, revealing two prominent peaks at 8 am and 6 pm. These peaks align with typical office commuting hours, indicating a strong correlation between bike rentals and work schedules. The lowest rental counts occurred at 4 am, while the highest were at 6 pm. These insights further emphasize the importance of understanding daily routines when forecasting bike demand.

![image](https://github.com/mohd-arham-islam/Bike-Share/assets/111959286/b7ea167f-508d-4dad-9617-5bba9763c722)


### Seasonal Fluctuations
A pie chart demonstrated the distribution of rented bikes across the four seasons. Summer stood out with the highest percentage (37%) of rentals, followed by autumn (29%), spring (26%), and winter (7.9%). This data underscores the popularity of bike rentals during the pleasant summer months and the lower demand during colder winters. Seasonal trends like these are crucial for anticipating and preparing for shifts in demand.

![image](https://github.com/mohd-arham-islam/Bike-Share/assets/111959286/e6e2304e-4108-43e9-b99f-6c29ffd774b3)

### Distribution of Rented Bikes by Temperature
The histogram illustrating the distribution of rented bikes by temperature revealed significant insights. Bike rentals showed an upward trend as temperatures increased, peaking around 25°C. This indicates that mild temperatures are most favorable for bike rentals, while extreme cold or hot weather conditions lead to decreased demand. This observation highlights the pivotal role of temperature in influencing bike rental trends.

![image](https://github.com/mohd-arham-islam/Bike-Share/assets/111959286/9af7f1ab-7680-450d-ac56-d6804b0c1834)


## Feature Engineering
In the feature engineering phase, less important columns such as 'Dew point temperature(°C)', 'Solar Radiation (MJ/m2)', and 'Visibility (10m)' were dropped. Additionally, rainfall and snowfall were combined into a single column named "precipitation," streamlining the dataset and enhancing model efficiency.

## Model Building
For the model building process, two regression algorithms were implemented:

* **Random Forest Regressor:** This algorithm yielded an R-squared score of approximately **0.854**, indicating a decent level of predictive accuracy.

* **XGBoost Regressor:** Utilizing the XGBoost algorithm, along with hyperparameter tuning through Grid Search, resulted in a significantly improved R-squared score of around **0.913**. This suggests that the XGBoost model outperforms the Random Forest Regressor in predicting bike rental demand.

## Flask Application for Model Deployment
To provide easy access to the trained model's predictions, a Flask application was developed. The web interface allows users to input relevant parameters and receive accurate bike count predictions in real-time. This integration of regression analysis, model deployment, and user interaction empowers rental bike providers to make informed decisions and optimize resource management effectively.

![image](https://github.com/mohd-arham-islam/Bike-Share/assets/111959286/20497980-1131-450f-97aa-4d776ea54e80)


By leveraging these insights, feature engineering techniques, and advanced regression models, this project offers a comprehensive solution for predicting bike rental demand, enhancing the overall user experience, and enabling more efficient resource allocation for rental bike providers.
