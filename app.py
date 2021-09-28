import json
from spellchecker import SpellChecker


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


    print('{"Erreur":'+ str(count_errors)+'}')




our_mail1 = '{"objet" : "Support NETFLIX", "text": "Bonjour , Nous n\'avons pas pu autoriser votre paiement pour le prochain cycle de facturation de votre abonnement. Nous serions bien évidemment très heureux de vous compter à nouveau parmi nous. cliquez simplement sur, réactivez simplement votre abonnement pour profiter des meilleurs films et séries TV sans interruption. RÉACTIVER L\'ABONNEMENT. Nous sommes là pour vous aider. Pour plus d\'informations, consultez le Centre d\'aide ou contactez-nous. L\'équipe Netflix"}'
Mail_ML(our_mail1)

our_mail2 = '{"objet" : "Support NETFLIX", "text": "Souhaitez-vous garder votre compte Disney ? Nous venons de détecter que votre moyen de paiement n\'est plus valide. Sans nouvelle source de paiement de votre part, votre abonnement sera résilié et vous serez facturé 29.99 conformément à la Loi sur la consommation adoptée en Février 2014. Configuration de paiement Nous suivre Facebook Twitter Link Pour plus d\'informations, Veuillez consulter notre Centre d\'aide.  2021 Disney et toutes ses entités associées. Tous droits réservés"}'
Mail_ML(our_mail2)

our_mail3 = '{"objet" : "Support NETFLIX", "text":   Toutes nos félicitations ! Vous avez été sélectionné pour participer à cette enquete. Cela ne prend qu\'une minute et vous obtenez un prix fantastique : le nouveau scooter électrique Xiaomi Mi! OBTENEZ LE MAINTENANT Chaque jour, nous sélectionnons au hasard 10 utilisateurs pour avoir la chance de gagner de superbes prix. Le prix d\'aujourd\'hui est un nouveau scooter électrique Xiaomi Mi! 10 heureux gagnants vont uniquement à ceux qui vivent en France! Cette enquête vise à améliorer le service à nos utilisateurs. Dépêchez-vous, le nombre de lots que vous pouvez gagner est limité! "}'
Mail_ML(our_mail3)
