import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from shapely.ops import cascaded_union
from geovoronoi.plotting import subplot_for_map, plot_voronoi_polys_with_points_in_area
from geovoronoi import voronoi_regions_from_coords, points_to_coords
from tkinter import *
from tkinter import ttk

delegaciones= {
    0: "MILPA ALTA",
    1: "BENITO JUÁREZ",
    2: "GUSTAVO A. MADERO",
    3: "COYOACÁN",
    4: "MIGUEL HIDALGO",
    5: "MAGDALENA CONTRERAS",
    6: "TLÁHUAC",
    7: "AZCAPOTZALCO",
    8: "IZTACALCO",
    9: "ÁLVARO OBREGÓN",
    10: "XOCHIMILCO",
    11: "VENUSTIANO CARRANZA",
    12: "TLALPAN",
    13: "CUAJIMALPA",
    14: "CUAUHTÉMOC",
    15: "IZTAPALAPA"
}

df = pd.read_excel('MercadosFull.xlsx')

def getVoronoiMap(index_delegacion: int):
    ndf = df[df.DELEGACION.isin([delegaciones[index_delegacion]])]
    mercados = gpd.GeoDataFrame(ndf, geometry=gpd.points_from_xy(ndf.long, ndf.lat))
    mercados.crs = "EPSG:4326"
    alcaldias = gpd.read_file("alcaldias_cdmx.shp")
    alcaldia = alcaldias.drop([i for i in range(16) if i != index_delegacion],axis=0)
    alcaldia = alcaldia.to_crs(epsg=3395)
    gdf_proj = mercados.to_crs(alcaldia.crs)
    alcaldia_shape = cascaded_union(alcaldia.geometry)
    coords = points_to_coords(gdf_proj.geometry)
    pts, poly_to_pt_assignments = voronoi_regions_from_coords(coords, alcaldia_shape)
    fig, ax = subplot_for_map(figsize=(14.5,10))
    plot_voronoi_polys_with_points_in_area(ax, alcaldia_shape, pts, coords,  poly_to_pt_assignments, point_labels=gdf_proj.MERCADO.tolist())
    ax.set_title(f'Regiones de Voronoi los mercados de la delegación {delegaciones[index_delegacion]}')
    plt.tight_layout()
    plt.show()

def main():
    global combo1
    root = Tk()
    root.title("GENERADOR DE MAPAS CON VORONOI")
    root.geometry("400x200")
    ttk.Label(root, text="SELECCIONE UNA DELEGACIÓN DE LA CDMX").place(x=80, y=25)
    combo1 = ttk.Combobox(root, width=50, state='readonly')
    combo1.place(x=40, y=75)
    combo1['values'] = list(delegaciones.values())
    combo1.current(0)
    ttk.Button(root, command=lambda: getVoronoiMap(combo1.current()), text="GENERAR MAPA",width=53).place(x=40, y=125)
    root.mainloop()

if __name__ == "__main__":
    main()