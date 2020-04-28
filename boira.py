import os
#Exercici2
def comptarParaules(text):
  conp=0
  for p in text:
    conp=conp+1
  return conp
  #TODO Heu de retornar el nombre de paraules que té un text
  #Com podeu detectar una paraula, que el separa les paraules?

def comptarFrases(text):
  conf=0
  for f in text.readline('.'):
    conf+=conf+1
  return conf



#TODO Fer-ho al final de tot el 5.
#Exericic 5 llegir configuració

#Exercici 1

r=False
while r==False:

  nomFitxer = input("Entra el nom de l'arxiu que vols analitzar ")
  

  if (os.path.isfile('noticies/'+nomFitxer)):
      r=True
      print("És fitxer")
      nom=open('noticies/'+ nomFitxer ,'r')
      text=(nom.read())

  else:
      print("No és fitxer")
      r=False
 
print(text)

print(comptarParaules(text))


print("Gràcies!")

#TODO heu de completar el codi perquè la variable text tingui el contingut del fitxer

 

#Per provar exercici 2 i 3 podeu posar-vos print aquíí per comprovar si es compta béé paraules, si compta frases, si es fa la mitja i si es detecten les complexes.

#Exercici 4
#càlcul de la fórmula
index =0 

#TODO  Pinteu index per pantalla 


#TODO Classifiqueu exercici segons índex
# Digueu com és el text seguint la taula https://en.wikipedia.org/wiki/Gunning_fog_inde

#TODO
#Heu de tancar el fitxer


