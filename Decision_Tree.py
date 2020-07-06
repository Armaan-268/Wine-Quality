# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def main():
    # Importing the dataset
    data = pd.read_csv('new_dataset.csv')
    x_train = data.iloc[:,:-1].values
    y_train = data.iloc[:,-1].values
    
    # Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size = 0.2, random_state = 0)
    
    #Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc_x = StandardScaler()
    sc_y = StandardScaler()
    x_train = sc_x.fit_transform(x_train)
    x_test = sc_x.transform(x_test)
    
    # Training the Decision Tree Classification model on the Training set
    from sklearn.tree import DecisionTreeClassifier
    classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
    classifier.fit(x_train, y_train)

    # Predicting the Test set results
    y_pred = classifier.predict(x_test)
    
    # Making the Confusion Matrix
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(y_test, y_pred)
    print(cm)
    
    # Writing Predictions in a file:
    df = pd.DataFrame(y_pred)
    df.to_csv('Y_Pred_DT.csv',index=False)
        
    # Plot
    slices = []
    s = set(y_pred)
    l = list(s)
    for j in l:
        temp = []
        for  i in range (1,len(y_pred)):
            if y_pred[i] == j:
                temp.append(y_pred[i])
                #total = sum(temp)
        slices.append(len(temp))
    quality = ['Bad Wine','Good Wine']
    color= ['r','c']
    plt.pie(slices,labels=quality,colors=color,shadow=False,autopct='%1.2f%%',radius=1,startangle=90)
    plt.title('Percentage of Good Wine')
    plt.show()
    
    # Plot 2
    slices = []
    s = set(y_pred)
    l = list(s)
    yes = []
    no = []
    for  i in range (0,len(y_pred)):
        if y_pred[i] == y_test[i]:
            yes.append(y_pred[i])
        else:
            no.append(y_pred[i])
    slices.append(len(no))
    slices.append(len(yes))
    quality = ['Incorrect','Correct']
    color= ['r','c']
    plt.pie(slices,labels=quality,colors=color,explode=(0.2,0),shadow=False,autopct='%1.2f%%',radius=1,startangle=0)
    plt.title('Predictions')
    plt.show()
if __name__ == "__main__":
    main()