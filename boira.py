import os
#Exercici2
def comptarParaules(text):
  textx=text.split()
  conp=0
  for p in textx:
    conp=conp+1
  return conp
  #TODO Heu de retornar el nombre de paraules que té un text
  #Com podeu detectar una paraula, que el separa les paraules?

def comptarFrases(text):
  conf=0
  for f in text:
    if f =='.':
      conf=conf+1
    elif f==':':
      conf=conf+1
    elif f==';':
      conf=conf+1
  return conf
def mitjanaParaulesPerFrase(text):
  p=int(comptarParaules(text))
  f=int(comptarFrases(text))
  mitjana=p/f
  return mitjana
#Exercici 3
def numeroParaulesComplexes(text):
  textx=text.split()
  conpc=0
  for p in textx:
    if len(p) >= 5:
      conpc=conpc+1
  return conpc
  #TODO Heu de retornar el nombre de paraules complexes que té el text
  #Són aquelles que tenen méés de cinc lletres

def percetantgeParaulesComplexes(text):
  p=int(comptarParaules(text))
  pc=int(mitjanaParaulesPerFrase(text))
  percentatge=(100*pc)/p
  return percentatge

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
print(comptarFrases(text))
print(mitjanaParaulesPerFrase(text))
print(numeroParaulesComplexes(text))
print((percetantgeParaulesComplexes(text)),('%'))

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


