import pandas as pd
import plotly.express as px
import math


def plotMapa(vecf):

    coordenadas=pd.DataFrame(vecf)

    print(coordenadas)

    lencoordenadas=math.trunc(len(coordenadas)/2)
    lon_media=float(coordenadas.iloc[lencoordenadas,2])
    lat_media=float(coordenadas.iloc[lencoordenadas,1])
    coordenadas=pd.DataFrame(vecf)
    df = coordenadas
    fig = px.scatter_mapbox(df, lat="Latitud", lon="Longitud", color="Lugar",
                      color_continuous_scale=px.colors.cyclical.IceFire, zoom=14,animation_frame=coordenadas.Lugar, center=dict(lat=lat_media,lon=lon_media),
                      mapbox_style="carto-positron",title="Ruta Bicipuma")
    fig.show()
    df = coordenadas
    fig = px.scatter_mapbox(df, lat="Latitud", lon="Longitud", color="Lugar",
                      color_continuous_scale=px.colors.cyclical.IceFire, zoom=14, center=dict(lat=lat_media,lon=lon_media),
                      mapbox_style="carto-positron",title="Ruta Bicipuma")
    fig.show()
