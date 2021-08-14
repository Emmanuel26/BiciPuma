from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

def mapTut():

	m = Basemap(projection = 'mill',llcrnrlat=20,urcrnrlat=50,llcrnrlon=-130,urcrnrlon=-60,resolution='c')
	m.drawcoastlines()
	m.drawcountries()
	m.drawstates()
	m.fillcontinents(color='#04BAE3',lake_color='#FFFFFF')
	m.drawmapboundary(fill_color='FFFFFF')


	# Texas

	lat,lon = 29.7630556,-95.360556
	x,y = m(lon,lat)
	m.plot(x,y,'ro')

	lon,lat = -104.237, 40.125

	xpt, ypt = m(lon,lat)
	m.plot(xpt,ypt,'go')

	pls.title("Geo Plotting")
	plt.show()

mapTut()
