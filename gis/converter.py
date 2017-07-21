#!/usr/bin/env python
# https://gis.stackexchange.com/questions/41180/gdal-doesn%C2%B4t-support-my-xyz-file
# xyz2tif.py
# convert gridded XYZ data (but without missing values) to GeoTIFF
# data looks like this:
"""
379528.00 4577221.00 -5.38
379529.00 4577221.00 -5.38
379530.00 4577221.00 -5.40
379531.00 4577221.00 -5.41
379515.00 4577222.00 -5.34
379516.00 4577222.00 -5.36
"""

from pylab import *
from osgeo import osr, gdal

# UTM ZONE 19, NAD83 data
# data = genfromtxt('/rps/bathy/muskegat/EW_Survey1.xyz')
data = genfromtxt('37709.xyz')
x = data[:, 0]
y = data[:, 1]
z = data[:, 2]

# find the extent and difference
xmin = min(x)
xmax = max(x)
ymin = min(y)
ymax = max(y)
mdx = abs(diff(x))
mdy = abs(diff(y))

# determine dx and dy from the median of all the non-zero difference values
dx = median(mdx[where(mdx > 0.0)[0]])
dy = median(mdy[where(mdy > 0.0)[0]])

# construct x,y,z of complete grid
xi = arange(xmin, xmax + dx, dx)
yi = arange(ymin, ymax + dy, dy)
zi = ones((len(yi), len(xi))) * NaN
shape(zi)

# calculate indices in full grid (zi) to stick the input z values
ix = numpy.round((x - xmin) / dx).astype(int)
iy = numpy.round((y - ymin) / dy).astype(int)
zi[iy, ix] = z

zi = flipud(zi)

# write as 32-bit GeoTIFF using GDAL
ny, nx = zi.shape
driver = gdal.GetDriverByName("GTiff")
ds = driver.Create('output.tif', nx, ny, 1, gdal.GDT_Float32)

# top left x, w-e pixel resolution, rotation, top left y, rotation, n-s pixel resolution
ds.SetGeoTransform([xmin, dx, 0, ymax, 0, dy])

# set the reference info
srs = osr.SpatialReference()

# UTM zone 19, North=1
srs.SetUTM(19, 1)
srs.SetWellKnownGeogCS('NAD83')
ds.SetProjection(srs.ExportToWkt())

# write the data to a single band
ds.GetRasterBand(1).WriteArray(zi)
# close
ds = None
