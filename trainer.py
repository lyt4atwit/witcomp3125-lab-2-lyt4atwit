
from sklearn.linear_model import LinearRegression
from joblib import dump
import pandas as pd

def main():
    data = pd.read_csv("pong_data.csv")

    # separate features and outcomes
    X = data.drop('paddle_direction', axis=1)
    y = data['paddle_direction']

    # train 
    model = LinearRegression()
    
    # fit
    model.fit(X, y)
    
    # save 
    dump(model, 'pongAI.joblib')

if __name__=="__main__":
    # call the main function
    main()