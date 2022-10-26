# loops 
# for una lista lunga , mi stampa gli elemeneti a capo.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
# for anche solo per una variabile , mi stampa le lettere ogni lettera a capo
for x in "banana":
  print(x)
#on l' istruzione break possiamo interrompere il ciclo prima che abbia eseguito il ciclo di tutti gli elementi
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#Esci dal ciclo quando x è "banana", ma questa volta la pausa viene prima della stampa: break mi dice quando interrompere 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
  #Con l' istruzione continue possiamo interrompere l'iterazione corrente del ciclo e continuare con la successiva:
  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
  #Per scorrere un insieme di codice un determinato numero di volte, possiamo usare la funzione range() ,restituisce una sequenza di numeri, a partire da 0 per impostazione predefinita, e incrementa di 1 (per impostazione predefinita) e termina con un numero specificato.for y in range(6):  print(y)
  #Nota che range(6) non è i valori da 0 a 6, ma i valori da 0 a 5.
  for x in range(6):
       print(x)
 # il print va dopo il for 
 #qui mi stampa da 2 a 5
for x in range(2, 6):
   print(x)   

print("per separare i numeri") 

#La funzione range() per impostazione predefinita incrementa la sequenza di 1, tuttavia è possibile specificare il valore di incremento aggiungendo un terzo parametro: range(2, 30, 3 ) :
for x in range(2, 30, 3):
  print(x)  # incrementa la sequanza di 3 

#La elseparola chiave in un forciclo specifica un blocco di codice da eseguire al termine del ciclo:
for x in range(6):
  print(x)
else:
  print("Finally finished!")
  # il elseblocco NON verrà eseguito se il ciclo viene interrotto da breakun'istruzione.

for x in range(6):
  if x == 3: break
  print(x)
else:
    print("Finally finished!") # non mi stampa il print , nota che il for e else devono stare allo stesso livello e il print deve stare più avanti.

#Un ciclo annidato è un ciclo all'interno di un ciclo.
# alle variabili x associa le variabili y 
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

# per creare dei loop incompleti e non voglio completare l'istruzione , metto pass cosi non sono obbligato a stamparli 
for x in [0, 1, 2]:
  pass

#  print va prima break e continue e dopo il for e else 