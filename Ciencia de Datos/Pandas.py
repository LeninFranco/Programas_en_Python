import pandas as pd

#Crear un DataFrame a partir de listas
fbk = ['Facebook', 2449, True, 2006]    
twt = ['Twitter', 339, False, 2006]
ig = ['Instagram', 1000, True, 2010]
yt = ['YouTube', 2000, False, 2005]
lkn = ['LinkedIn', 663, False, 2003]
wsp = ['WhatsApp', 1600, True, 2009]

redes_sociales = [fbk, twt, ig, yt, lkn, wsp]

df_rs = pd.DataFrame(redes_sociales,columns=['Nombre','Usuarios','ES_Facebook','Año'])

#print(df_rs)

#Seleccionar elementos: loc vs iloc

#loc
#print(df_rs.loc[1,'Nombre'])

#iloc
#print(df_rs.iloc[3,3])

#Seleccionar columnas
#print(df_rs['Nombre'])
#print(df_rs[['Nombre','Año']])
#print(df_rs.Nombre)

#Seleccionar Fila
#print(df_rs.iloc[2])
#print(df_rs.iloc[[0,2,5]])

#Seleccionar Filas y Columnas
#print(df_rs.loc[[0,2,5],['Nombre','Año']])

#Filtrar por condicion
#print(df_rs[df_rs['Usuarios'] > 1500])

#Filtrar por condicion en cadenas de texto
#print(df_rs[df_rs['Nombre'].str.contains('book')])

#Ordenar de menor a mayor
#print(df_rs.sort_values('Nombre', ascending=True))

#Ordenar de mayor a menor
#print(df_rs.sort_values('Nombre', ascending=False))

#Filtrar por una condicion y filtrar columnas
print(df_rs[df_rs['Año'] < 2006][['Nombre','Usuarios']])

#Operaciones estadisticas
#print(df_rs['Usuarios'].sum())
#print(df_rs['Usuarios'].var())
#print(df_rs['Usuarios'].mean())

#Estadisticas completas
#print(df_rs.describe())