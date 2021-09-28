import json
import pandas as pd
from spellchecker import SpellChecker
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

our_mail = '{"objet" : "Support NETFLIX", "text": "Bonjour , Nous n\'avons pas pu autoriser votre paiement pour le prochain cycle de facturation de votre abonnement. Nous serions bien évidemment très heureux de vous compter à nouveau parmi nous. cliquez simplement sur, réactivez simplement votre abonnement pour profiter des meilleurs films et séries TV sans interruption. RÉACTIVER L\'ABONNEMENT. Nous sommes là pour vous aider. Pour plus d\'informations, consultez le Centre d\'aide ou contactez-nous. L\'équipe Netflix"}'


def Mail_ML (mail_recup):

    '''
    La fonction prends en paramètre un Json avec ce que l'on récupère de l'utilisateur 

    Elle rends un json avec les scores calculés pendant le machine learning sur la probabilité que le mail soit un faux 

    On prends en compte :

        - Les fautes d'orthographes présentent dans le mail 
    '''
    # parse json:
    text = json.loads(mail_recup)


    #Objet a corriger
    corps_mail=text["text"]

    new_str=""
    foundForbiddenChar = False
    for i in range(0, len(corps_mail)-1, 1):
        # end of corps_mail
        if (i+1 == len(corps_mail)):
            new_str = new_str + corps_mail[i]
           
        if (corps_mail[i+1]!="'" and corps_mail[i+1]!=","):
            if not foundForbiddenChar :
                new_str += corps_mail[i]
                foundForbiddenChar = False
            else :
                foundForbiddenChar = False
        else :
            foundForbiddenChar = True


    # print(new_str)

        

    spell = SpellChecker(language='fr')
    # print(spell.correction("bojour"))

    all_words=new_str.split()

    corrected_all_words=[]
    for i in range (0,len(all_words),1):

        #print(spell.correction(l[i]))
        corrected_all_words.append(spell.correction(all_words[i]))


    # print (corrected_all_words)

    count_errors=0
    for i in range (0,len(corrected_all_words),1):
        if (corrected_all_words[i]!=all_words[i]):
            count_errors+=1

    print ("Il y a " + str(count_errors) + " erreurs")


    """
        Analyse de sentiments
    """
    dataset_feeling_file = 'dataset_feeling.csv'
    feelings_messages = pd.read_csv(dataset_feeling_file)

    labels_feelings = feelings_messages.iloc[:, 1].values
    features_mailText = feelings_messages.iloc[:, 2].values

    vectorizer = TfidfVectorizer (
        max_features=2500, 
        # min_df=7, 
        # max_df=0.8,
        #stop_words=stopwords.words('french')
    )


    features_mailText = vectorizer.fit_transform(features_mailText).toarray()

    X_train, X_test, y_train, y_test = train_test_split(
        features_mailText, 
        labels_feelings, 
        test_size=0.2, 
        random_state=0
    )

    text_classifier = RandomForestClassifier(n_estimators=200, random_state=0)
    text_classifier.fit(X_train, y_train)

    predictions = text_classifier.predict(X_test)


    print(confusion_matrix(y_test,predictions))
    print(classification_report(y_test,predictions))
    print("Model accuracy =", accuracy_score(y_test, predictions)*100, " %")


    print('{"score1": "15%", "scores2": "80%"}')



Mail_ML(our_mail)