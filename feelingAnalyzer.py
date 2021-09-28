import json
import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

class FeelingAnalyzer:        

    def myfun(self):
        return 1
        
    def loadModel(self, verbose):
        
        # Importing and reading the Dataset
        dataset_feeling_file = 'dataset_feeling.csv'
        feelings_messages = pd.read_csv(dataset_feeling_file)

        labels_feelings = feelings_messages.iloc[:, 1].values
        features_mailText = feelings_messages.iloc[:, 2].values

        # Representing Text in Numeric Form with TF-IDF
        vectorizer = TfidfVectorizer (
            max_features=2500, 
            # min_df=7, 
            # max_df=0.8,
            #stop_words=stopwords.words('french')
        )
        features_mailText = vectorizer.fit_transform(features_mailText).toarray()

        # Dividing Data into Training and Test Sets
        X_train, X_test, y_train, y_test = train_test_split(
            features_mailText, 
            labels_feelings, 
            test_size=0.2, 
            random_state=0
        )

        # Training the Model
        text_classifier = RandomForestClassifier(n_estimators=200, random_state=0)
        text_classifier.fit(X_train, y_train)

        # Making Predictions and Evaluating the Model
        predictions = text_classifier.predict(X_test)

        if (verbose):
            print('****** Confusion matrix ******\n', confusion_matrix(y_test,predictions))
            print('****** Classification report ******\n', classification_report(y_test,predictions))
        
        print("Model accuracy =", accuracy_score(y_test, predictions)*100, "%")

        return 1