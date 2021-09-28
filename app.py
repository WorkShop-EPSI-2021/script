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

our_mail3 = '{"objet" : "Support NETFLIX", "text": Bonjour, Lors de votre dernier achat ,vous avez été averti par un message qui vous informe de l\'obligation d\'adhérer à la nouvelle réglementation   Concernant la fiabilité pour les achats par carte bancaire sur internet . la mise en place d\'un arrêt pour vos futurs achats. A ce jour, nous n\'avons pas reçu d\'adhésion de votre part et nous sommes au regret de vous informer que vous ne pouvez plus utiliser votre carte sur internet. Faites votre demande d\'adhésion en ligne en cliquant ici Crédit agricole ca Ce message est généré automatiquement, merci de ne pas y répondre, il ne pourra pas être lu.   Société Anonyme à Directoire et Conseil de Surveillance au capital de 4 046 407 595 euros Siège social et adresse postale : 115, rue de Sèvres  75 275 Paris Cedex 06 RCS Paris 421 100 645  Code APE 6419Z, intermédiaire d\'assurance, immatriculé à l\'ORIAS sous le n° 07 023 424"}'
Mail_ML(our_mail3)
