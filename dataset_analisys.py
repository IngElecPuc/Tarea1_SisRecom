import matplotlib.pyplot as plt
import pandas as pd
import pyreclab as prl
import numpy as np
import find_sort as fs
#from sklearn import datasets, linear_model
#from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold

df = pd.read_csv('training_data.txt.csv',
                sep=',',
                names = ['userID','itemID','styleID','rating','brewerID','timestamp'],
                header=0)

#Falta eliminar los repetidos, pares (userID, itemID) que se repiten en la base de datos

df_users = list(df['userID'])
df_items = list(df['itemID'])
df_ratings = list(df['rating'])

df_users_r = list([[df_users[i],df_ratings[i]] for i in range(0,len(df_users)-1)])
df_items_r = list([[df_items[i],df_ratings[i]] for i in range(0,len(df_items)-1)])
#Buscamos usuarios e items con pocas repeticiones: Overshots en su peso en el test

smpl_users = list([0 for i in range(max(df_users))])
smpl_items = list([0 for i in range(max(df_items))])

for i in df_users: #Contamos las veces que aparece cada usuario
    smpl_users[i-1] += 1

for i in df_items: #E item
    smpl_items[i-1] += 1
#Algunas estadísticas
print("Minimo de repeticiones de usuarios " + str(min(smpl_users)))
print("Máximo de repeticiones de usuarios " + str(max(smpl_users)))
print("Moda en las repeticiones de usuarios " + str(np.argmax(np.bincount(smpl_users))))#Moda
print("Promedio de repeticiones de usuarios " + str(np.mean(smpl_users)))
print("Varianza de repeticiones de usuarios " + str(np.var(smpl_users)))
print("Minimo de repeticiones de items " + str(min(smpl_items)))
print("Máximo de repeticiones de items " + str(max(smpl_items)))
print("Moda en las repeticiones de items " + str(np.argmax(np.bincount(smpl_items))))#Moda
print("Promedio de repeticiones de items " + str(np.mean(smpl_items)))
print("Varianza de repeticiones de items " + str(np.var(smpl_items)))

users_ovsh = []
items_ovsh = []

for i in df_users: 
    if smpl_users[i-1] == 1:#Agregamos a la lista especial a los usuarios que tienen 1 elemento (moda)
        users_ovsh.append(i)
    elif smpl_users[i-1] == 0:#Eliminamos los usuarios que no están en la lista
        print("Usuario fuera de la lista")
        smpl_users.pop(i-1)

for i in df_items: 
    if smpl_items[i-1] == 1:#Agregamos a la lista especial a los items que tienen 1 elemento (moda)
        items_ovsh.append(i)
    elif smpl_items[i-1] == 0:#Eliminamos los items que no están en la lista
        print("Item fuera de la lista")
        smpl_items.pop(i-1)

kf = KFold(n_splits = 4, shuffle = True, random_state = None)
result = next(kf.split(df), None)

train = df.iloc[result[0]]
test =  df.iloc[result[1]]

train.head()
test.head()
#Falta eliminar los repetidos
df_users_ord = df_users_r.sort()
#df_items_ord = fs.quicksort(df_items)
#df_users_pd = df['userID']
#hist_users = df_users_pd.hist(bin=3)
#print(hist_users)

plt.figure()
hist = plt.hist(df_users,bins=30)
plt.show()

print(hist)