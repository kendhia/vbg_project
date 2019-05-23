import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB




clf = GaussianNB()
df = pd.read_csv("flights_reason_added.csv")
df = df.fillna(0)
X_train, x_test, Y_train, y_test = train_test_split(df, df["Reason"], test_size=0.1)
model = clf.fit(X_train, Y_train)
score = model.score(x_test, y_test)
print(score)
#predict_result = model.predict(x_test)