import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
df = pd.read_csv("../data/house_data.csv")
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df.drop(['date','id'], axis=1, inplace=True)
plt.figure(figsize=(16,10))
sns.heatmap(df.corr(), annot=True)
plt.show()
sns.histplot(df['price'])
plt.show()
sns.scatterplot(x = 'sqft_living', y = 'price', data = df)
plt.show()
X = df.drop('price', axis=1)
y = df['price']
X_train,X_test,y_train,y_test = train_test_split(X,y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train,y_train)
model1 = RandomForestRegressor()
model1.fit(X_train, y_train)
model_pred = model.predict(X_test)
model1_pred = model1.predict(X_test)

accuracy = r2_score(y_test, model_pred)
accuracy1 = r2_score(y_test, model1_pred)

print('Linear Regression Score:', accuracy)
print('Forest Regression Score:', accur
