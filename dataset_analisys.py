#import matplotlib.pyplot as plt
import pandas as pd
import pyreclab as prl
import find_sort as fs
#from sklearn import datasets, linear_model
#from sklearn.model_selection import train_test_split

df = pd.read_csv('training_data.txt.csv',
                sep=',',
                names = ['userID','itemID','styleID','rating','brewerID','timestamp'],
                header=0)

df_users = list(df['userID'])
df_items = list(df['itemID'])
df_ratings_u = list(df['rating'])
df_ratings_i = list(df['rating'])

#Buscamos usuarios e items con pocas repeticiones: Overshots en su peso en el test
#Quick sort

df_users = fs.quicksort(df_users)
      
smpl_user = list([0 for i in range(0,max(df_users)-1)])

for i in df_users: #Contamos las veces que aparece cada usuario
    try:
        smpl_user[i-1] += 1
    except IndexError:
        print('Index error ',i)

user_ovsh = []
for i in df_users: #Agregamos a la lista especial a los usuarios que tienen igual o menos de 3 elementos
    try:
        if smpl_user[i-1] <= 3:
            user_ovsh.append(i)
    except IndexError:
        print('Index error ',i)

print(len(user_ovsh))
