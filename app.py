import json

from spellchecker import SpellChecker

mailText = '{"objet" : "Support NETFLIX", "text": "Bonjour , Nous n\'avons pas pu autoriser votre paiement pour le prochain cycle de facturation de votre abonnement. Nous serions bien évidemment très heureux de vous compter à nouveau parmi nous. cliquez simplement sur, réactivez simplement votre abonnement pour profiter des meilleurs films et séries TV sans interruption. RÉACTIVER L\'ABONNEMENT. Nous sommes là pour vous aider. Pour plus d\'informations, consultez le Centre d\'aide ou contactez-nous. L\'équipe Netflix"}'


# parse json:
text = json.loads(mailText)


#Objet a corriger
#print(text["text"])
mail_text=text["text"]



new_text=str()
for i in range(0,len(mail_text),1):
    if (mail_text[i+1]!="'"):
        print(mail_text[i])
        # new_text+=mail_text[i]
print(new_text)

        


spell = SpellChecker(language='fr')
# print(spell.correction("bojour"))

l=mail_text.split()
print(l)

new_l=[]
for i in range (0,len(l),1):

    #print(spell.correction(l[i]))
    new_l.append(spell.correction(l[i]))


print (new_l)

print('{"score1": "15%", "scores2": "80%"}')
