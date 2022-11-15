from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np

class tree:
    def __init__(self):
        columns = ["S1","C1","S2","C2","S3","C3","S4","C4","S5","C5","Class"]

        df = pd.read_csv('poker-hand-training-true.data', names=columns)
        # print(df.head())

        # shuffle data
        df = df.sample(frac=1).reset_index(drop=True)
        
        my_df_y = df["Class"]
        del df["Class"]
        my_df_x = df.copy()

        # x_train,y_train =  train_test_split(my_df_x, my_df_y)

        self.d_tree = DecisionTreeClassifier(max_depth = 9)
        # self.d_tree.fit(x_train, y_train)
        self.d_tree.fit(my_df_x, my_df_y)
        # y_pred_dt = d_tree.predict(x_test)
        # print("tree score", accuracy_score(y_test, y_pred_dt))
    # Recive the n number of cards, and return the best ranking hand except 0
    def predict(self,cardsList):
       # the data should be encoded already
       # do a switch case of the list len 5,6,7
        listLen = len(cardsList)//2
        print(listLen)
        ls = np.array(cardsList).reshape(1,-1)
        if listLen == 5:
           print("list of 5 cards")
           pred = self.d_tree.predict(cardsList)
           print(f'the prediction for this hand is {pred}')
           return pred 
        elif listLen == 6: 
           print("list of 6 cards")
        elif listLen == 7: 
           print("list of 7 cards")
        return 0

# data set reading 
# no label encoding needed
# divide into x and y

"""
Convert to object with method to convert cards to input and predict
Maybe do a support vector machine that works the same?


"""
