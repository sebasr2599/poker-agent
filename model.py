from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np

# todo, method to transform from card type to array
class Tree:
    def __init__(self):
        columns = ["S1", "C1", "S2", "C2", "S3",
                   "C3", "S4", "C4", "S5", "C5", "Class"]

        df = pd.read_csv('poker-hand-training-true.data', names=columns)
        # print(df.head())

        # shuffle data
        df = df.sample(frac=1).reset_index(drop=True)

        my_df_y = df["Class"]
        del df["Class"]
        my_df_x = df.copy()

        # x_train,y_train =  train_test_split(my_df_x, my_df_y)

        self.d_tree = DecisionTreeClassifier(max_depth=9)
        # self.d_tree.fit(x_train, y_train)
        self.d_tree.fit(my_df_x.values, my_df_y.values)
        # y_pred_dt = d_tree.predict(x_test)
        # print("tree score", accuracy_score(y_test, y_pred_dt))
    # Recive the n number of cards, and return the best ranking hand except 0

    def predict(self, cardsList):
       # the data should be encoded already
       # do a switch case of the list len 5,6,7
        listLen = len(cardsList)//2
        print(listLen)

        if listLen == 5:
            print("list of 5 cards")
            ls = np.array(cardsList)
            ls = ls.reshape(1, -1)
            pred = self.d_tree.predict(ls)
            print(f'the prediction for this hand is {pred}')
            return np.min(pred[np.nonzero(pred)]) 
        elif listLen == 6:
            print("list of 6 cards")
            arr = self.permamut_6(cardsList)
            pred = self.d_tree.predict(arr)
            return np.min(pred[np.nonzero(pred)])  
        return 0

    def permamut_6(self, arr):
        combi = []
        aux = arr.copy()
        combi.append(arr[:10])
        last = len(arr)
        # print(combi)
        # print(f'last: {last}')
        # check for your own cards and the rest
        for i in range(5, last-2, +2):
            # print(f'i: {aux[i]}, i+1: {aux[i-1]}')
            aux2 = aux.copy()
            temp = aux[last-1]
            aux[last-1] = aux[i]
            aux[i] = temp

            temp = aux[last-2]
            aux[last-2] = aux[i-1]
            aux[i-1] = temp

            # print(f'current arr: {aux}')
            combi.append(aux[:10])

            aux = aux2.copy()
        # print(combi)
        return combi


# data set reading
# no label encoding needed
# divide into x and y

"""
Convert to object with method to convert cards to input and predict
Maybe do a support vector machine that works the same?


"""
