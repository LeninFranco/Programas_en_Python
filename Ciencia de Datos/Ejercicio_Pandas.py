import pandas as pd

df = pd.DataFrame({'Mes':['Enero','Febrero','Marzo','Abril'],'Ventas':[30500,35600,28300,33900],'Gastos':[22000,23400,18100,20700]})

#Balance de cada mes
df['Balance'] = df['Ventas'] - df['Gastos']
#print(df)

#Balance de los bimestre Enero-Febrero
meses = ['Enero','Febrero']
print(df[df['Mes'].isin(meses)]['Balance'].sum())