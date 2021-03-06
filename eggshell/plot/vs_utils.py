# encoding: utf8
from tempfile import mkstemp
import logging
# from matplotlib import use
# use('Agg')   # use this if no xserver is available
import numpy as np

from matplotlib import pyplot as plt
from matplotlib.patches import Polygon
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection

from cartopy import config as cartopy_config
import cartopy.feature as cfeature
from cartopy.util import add_cyclic_point
import re

# from matplotlib.colors import Normalize
# from cartopy import config as cartopy_config
# from cartopy.util import add_cyclic_point
# import cartopy.crs as ccrs
# from eggshell import utils
# from flyingpigeon import utils

LOGGER = logging.getLogger("PYWPS")

def fig2plot(fig, file_extension='png', output_dir='.', bbox_inches='tight', dpi=300, facecolor='w', edgecolor='k', figsize=(20, 10)):
    '''saving a matplotlib figure to a graphic

    :param fig: matplotlib figure object
    :param output_dir: directory of output plot
    :param file_extension: file file_extension (default='png')

    :return str: path to graphic
    '''

    _, graphic = mkstemp(dir=output_dir, suffix='.%s' % file_extension)
    fig.savefig(graphic, bbox_inches=bbox_inches, dpi=dpi, facecolor=facecolor, edgecolor=edgecolor, figsize=figsize)

    return graphic

# def plot_products(products, extend=[10, 20, 5, 15]):
#     """
#     plot the products extends of the search result
#
#     :param products: output of sentinel api search
#
#     :return graphic: map of extents
#     """
#
#
#     try:
#         fig = plt.figure(dpi=90, facecolor='w', edgecolor='k')
#         projection = ccrs.PlateCarree()
#         ax = plt.axes(projection=projection)
#         ax.set_extent(extend)
#         ax.stock_img()
#         ax.coastlines()
#         ax.add_feature(cfeature.BORDERS)
#
#         pat = re.compile(r'''(-*\d+\.\d+ -*\d+\.\d+);*''')
#
#         for key in products.keys():
#             polygon = str(products[key]['footprint'])
#
#             # s = 'POLYGON ((15.71888453311329 9.045763865974665,15.7018748825589 8.97110837227606,15.66795226563288 8.822558900399137,15.639498612331632 8.69721920092792,15.63428409805786 8.674303514900869,15.600477269179995 8.525798537094156,15.566734239298787 8.377334323160321,15.53315342410745 8.228822837291709,15.499521168391912 8.080353481086165,15.493321895031096 8.052970059354971,14.999818486685434 8.053569047879877,14.999818016115439 9.046743365203026,15.71888453311329 9.045763865974665))'
#             matches = pat.findall(polygon)
#             if matches:
#                 xy = np.array([map(float, m.split()) for m in matches])
#                 ax.add_patch(mpatches.Polygon(xy, closed=True,  transform=ccrs.PlateCarree(), alpha=0.4)) # color='coral'
#         # ccrs.Geodetic()
#
#         ax.gridlines(draw_labels=True,)
#         img = vs.fig2plot(fig, output_dir='.')
#     except:
#         LOGGER.debug('failed to plot EO products')
#         _, img = mkstemp(dir='.', prefix='dummy_', suffix='.png')
#
#     return img


# class MidpointNormalize(Normalize):
#     def __init__(self, vmin=None, vmax=None, midpoint=None, clip=False):
#         self.midpoint = midpoint
#         Normalize.__init__(self, vmin, vmax, clip)
#
#     def __call__(self, value, clip=None):
#         x, y = [self.vmin, self.midpoint, self.vmax], [0, 0.5, 1]
#         return np.ma.masked_array(np.interp(value, x, y))





# def plot_extend(resource, file_extension='png'):
#     """
#     plots the extend (domain) of the values stored in a netCDF file:
#
#     :parm resource: path to netCDF file
#     :param file_extension: file format of the graphic. if file_extension=None a matplotlib figure will be returned
#
#     :return graphic: graphic in specified format
#     """
#     import matplotlib.patches as mpatches
#     lats, lons = utils.get_coordinates(resource, unrotate=True)
#
#     # box_top = 45
#     # x, y = [-20, -20, 45, 45, -44], [-45, box_top, box_top, -45, -45]
#
#     xy = np.array([[np.min(lons), np.min(lats)],
#                    [np.max(lons), np.min(lats)],
#                    [np.max(lons), np.max(lats)],
#                    [np.min(lons), np.max(lats)]])
#
#     fig = plt.figure(figsize=(20, 10), dpi=600, facecolor='w', edgecolor='k')
#     projection = ccrs.Robinson()
#
#     #  ccrs.Orthographic(central_longitude=np.mean(xy[:, 0]),
#     #  central_latitude=np.mean(xy[:, 1]),
#     #  globe=None)  # Robinson()
#
#     ax = plt.axes(projection=projection)
#     ax.stock_img()
#     ax.coastlines()
#     ax.add_patch(mpatches.Polygon(xy, closed=True,  transform=ccrs.PlateCarree(), color='coral', alpha=0.6))
#     # ccrs.Geodetic()
#     ax.gridlines()
#     plt.show()
#
#     if file_extension is None:
#         map_graphic = fig
#     else:
#         map_graphic = fig2plot(fig=fig, file_extension=file_extension)
#     plt.close()
#
#     return map_graphic


# def plot_polygons(regions, file_extension='png'):
#     """
#     extract the polygon coordinate and plot it on a worldmap
#
#     :param regions: list of ISO abreviations for polygons
#
#     :return png: map_graphic.png
#     """
#
#     from cartopy.io.shapereader import Reader
#     from cartopy.feature import ShapelyFeature
#     from numpy import mean, append
#
#     import eggshell.config
#     # from flyingpigeon import config
#     DIR_SHP = config.shapefiles_path()
#
#     if type(regions) == str:
#         regions = list([regions])
#
#     fname = join(DIR_SHP, "countries.shp")
#     geos = Reader(fname).geometries()
#     records = Reader(fname).records()
#     central_latitude = []
#     central_longitude = []
#
#     for r in records:
#         geo = geos.next()
#         if r.attributes['ISO_A3'] in regions:
#             x, y = geo.centroid.coords.xy
#             central_longitude.append(x[0])
#             central_latitude.append(y[0])
#
#     fig = plt.figure(figsize=(20, 10))
#     projection = ccrs.Orthographic(central_longitude=mean(central_longitude),
#                                    central_latitude=mean(central_latitude),
#                                    globe=None)  # Robinson()
#     ax = plt.axes(projection=projection)
#
#     geos = Reader(fname).geometries()
#     records = Reader(fname).records()
#
#     for r in records:
#         geo = geos.next()
#         if r.attributes['ISO_A3'] in regions:
#             shape_feature = ShapelyFeature(geo, ccrs.PlateCarree(), edgecolor='black', color='coral')
#             ax.add_feature(shape_feature)
#     ax.coastlines()
#     ax.gridlines()
#     ax.stock_img()
#     # ax.set_global()
#     map_graphic = fig2plot(fig=fig, file_extension=file_extension)
#     plt.close()
#
#     return map_graphic
#
#
#
#
# def spaghetti(resouces, variable=None, title=None, file_extension='png'):
#     """
#     creates a png file containing the appropriate spaghetti plot as a field mean of the values.
#
#     :param resouces: list of files containing the same variable
#     :param variable: variable to be visualised. If None (default), variable will be detected
#     :param title: string to be used as title
#
#     :retruns str: path to png file
#     """
#     from eggshell.general.calculation import fieldmean
#
#     try:
#         fig = plt.figure(figsize=(20, 10), dpi=600, facecolor='w', edgecolor='k')
#         LOGGER.debug('Start visualisation spaghetti plot')
#
#         # === prepare invironment
#         if type(resouces) != list:
#             resouces = [resouces]
#         if variable is None:
#             variable = utils.get_variable(resouces[0])
#         if title is None:
#             title = "Field mean of %s " % variable
#
#         LOGGER.info('plot values preparation done')
#     except:
#         msg = "plot values preparation failed"
#         LOGGER.exception(msg)
#         raise Exception(msg)
#     try:
#         for c, nc in enumerate(resouces):
#             # get timestapms
#             try:
#                 dt = utils.get_time(nc)  # [datetime.strptime(elem, '%Y-%m-%d') for elem in strDate[0]]
#                 ts = fieldmean(nc)
#                 plt.plot(dt, ts)
#                 # fig.line( dt,ts )
#             except Exception as e:
#                 msg = "spaghetti plot failed for {} : {}".format(nc, e)
#                 LOGGER.exception(msg)
#
#         plt.title(title, fontsize=20)
#         plt.grid()
#
#         output_png = fig2plot(fig=fig, file_extension=file_extension)
#
#         plt.close()
#         LOGGER.info('timeseries spaghetti plot done for %s with %s lines.' % (variable, c))
#     except Exception as e:
#         msg = 'matplotlib spaghetti plot failed: {}'.format(e)
#         LOGGER.exception(msg)
#     return output_png
#
#
# def uncertainty(resouces, variable=None, ylim=None, title=None, file_extension='png', window=None):
#     """
#     creates a png file containing the appropriate uncertainty plot.
#
#     :param resouces: list of files containing the same variable
#     :param variable: variable to be visualised. If None (default), variable will be detected
#     :param title: string to be used as title
#     :param window: windowsize of the rolling mean
#
#     :returns str: path/to/file.png
#     """
#     LOGGER.debug('Start visualisation uncertainty plot')
#
#     import pandas as pd
#     import numpy as np
#     from os.path import basename
#     from eggshell.general.utils import get_time, sort_by_filename
#     from eggshell.general.calculation import fieldmean
#     from eggshell.general.metadata import get_frequency
#     #
#     # from flyingpigeon.utils import get_time, sort_by_filename
#     # from flyingpigeon.calculation import fieldmean
#     # from flyingpigeon.metadata import get_frequency
#
#     # === prepare invironment
#     if type(resouces) == str:
#         resouces = list([resouces])
#     if variable is None:
#         variable = utils.get_variable(resouces[0])
#     if title is None:
#         title = "Field mean of %s " % variable
#
#     try:
#         fig = plt.figure(figsize=(20, 10), facecolor='w', edgecolor='k')  # dpi=600,
#         #  variable = utils.get_variable(resouces[0])
#         df = pd.DataFrame()
#
#         LOGGER.info('variable %s found in resources.' % variable)
#         datasets = sort_by_filename(resouces, historical_concatination=True)
#
#         for key in datasets.keys():
#             try:
#                 data = fieldmean(datasets[key])  # get_values(f)
#                 ts = get_time(datasets[key])
#                 ds = pd.Series(data=data, index=ts, name=key)
#                 # ds_yr = ds.resample('12M', ).mean()   # yearly mean loffset='6M'
#                 df[key] = ds
#
#             except Exception:
#                 LOGGER.exception('failed to calculate timeseries for %s ' % (key))
#
#         frq = get_frequency(resouces[0])
#
#         if window is None:
#             if frq == 'day':
#                 window = 10951
#             elif frq == 'man':
#                 window = 359
#             elif frq == 'sem':
#                 window = 119
#             elif frq == 'yr':
#                 window = 30
#             else:
#                 LOGGER.debug('frequency %s is not included' % frq)
#                 window = 30
#
#         if len(df.index.values) >= window * 2:
#             # TODO: calculate windowsize according to timestapms (day,mon,yr ... with get_frequency)
#             df_smooth = df.rolling(window=window, center=True).mean()
#             LOGGER.info('rolling mean calculated for all input data')
#         else:
#             df_smooth = df
#             LOGGER.debug('timeseries too short for moving mean')
#             fig.text(0.95, 0.05, '!!! timeseries too short for moving mean over 30years !!!',
#                      fontsize=20, color='red',
#                      ha='right', va='bottom', alpha=0.5)
#
#         try:
#             rmean = df_smooth.quantile([0.5], axis=1,)  # df_smooth.median(axis=1)
#             # skipna=False  quantile([0.5], axis=1, numeric_only=False )
#             q05 = df_smooth.quantile([0.10], axis=1,)  # numeric_only=False)
#             q33 = df_smooth.quantile([0.33], axis=1,)  # numeric_only=False)
#             q66 = df_smooth.quantile([0.66], axis=1, )  # numeric_only=False)
#             q95 = df_smooth.quantile([0.90], axis=1, )  # numeric_only=False)
#             LOGGER.info('quantile calculated for all input data')
#         except Exception:
#             LOGGER.exception('failed to calculate quantiles')
#
#         try:
#             plt.fill_between(df_smooth.index.values, np.squeeze(q05.values), np.squeeze(q95.values),
#                              alpha=0.5, color='grey')
#             plt.fill_between(df_smooth.index.values, np.squeeze(q33.values), np.squeeze(q66.values),
#                              alpha=0.5, color='grey')
#
#             plt.plot(df_smooth.index.values, np.squeeze(rmean.values), c='r', lw=3)
#
#             plt.xlim(min(df.index.values), max(df.index.values))
#             plt.ylim(ylim)
#             plt.title(title, fontsize=20)
#             plt.grid()  # .grid_line_alpha=0.3
#
#             output_png = fig2plot(fig=fig, file_extension=file_extension)
#             plt.close()
#             LOGGER.debug('timeseries uncertainty plot done for %s' % variable)
#         except Exception as err:
#             raise Exception('failed to calculate quantiles. %s' % err.message)
#     except Exception:
#         LOGGER.exception('uncertainty plot failed for %s.' % variable)
#         _, output_png = mkstemp(dir='.', suffix='.png')
#     return output_png
#
#
# def map_robustness(signal, high_agreement_mask, low_agreement_mask,
#                    variable=None, cmap='seismic', title=None,
#                    file_extension='png'):
#     """
#     generates a graphic for the output of the ensembleRobustness process for a lat/long file.
#
#     :param signal: netCDF file containing the signal difference over time
#     :param highagreement:
#     :param lowagreement:
#     :param variable:
#     :param cmap: default='seismic',
#     :param title: default='Model agreement of signal'
#     :returns str: path/to/file.png
#     """
#     # from flyingpigeon import utils
#     from eggshell.general import utils
#     from numpy import mean, ma
#
#     if variable is None:
#         variable = utils.get_variable(signal)
#
#     try:
#         var_signal = utils.get_values(signal)
#         mask_l = utils.get_values(low_agreement_mask)
#         mask_h = utils.get_values(high_agreement_mask)
#
#         # mask_l = ma.masked_where(low < 0.5, low)
#         # mask_h = ma.masked_where(high < 0.5, high)
#         # mask_l[mask_l == 0] = np.nan
#         # mask_h[mask_h == 0] = np.nan
#
#         LOGGER.info('data loaded')
#
#         lats, lons = utils.get_coordinates(signal, unrotate=True)
#
#         if len(lats.shape) == 1:
#             cyclic_var, cyclic_lons = add_cyclic_point(var_signal, coord=lons)
#             mask_l, cyclic_lons = add_cyclic_point(mask_l, coord=lons)
#             mask_h, cyclic_lons = add_cyclic_point(mask_h, coord=lons)
#
#             lons = cyclic_lons.data
#             var_signal = cyclic_var
#
#         LOGGER.info('lat lon loaded')
#
#         minval = round(np.nanmin(var_signal))
#         maxval = round(np.nanmax(var_signal)+.5)
#
#         LOGGER.info('prepared data for plotting')
#     except:
#         msg = 'failed to get data for plotting'
#         LOGGER.exception(msg)
#         raise Exception(msg)
#
#     try:
#         fig = plt.figure(facecolor='w', edgecolor='k')
#
#         ax = plt.axes(projection=ccrs.Robinson(central_longitude=int(mean(lons))))
#         norm = MidpointNormalize(midpoint=0)
#
#         cs = plt.contourf(lons, lats, var_signal, 60, norm=norm, transform=ccrs.PlateCarree(),
#                           cmap=cmap, interpolation='nearest')
#
#         cl = plt.contourf(lons, lats, mask_l, 1, transform=ccrs.PlateCarree(), colors='none', hatches=[None, '/'])
#         ch = plt.contourf(lons, lats, mask_h, 1, transform=ccrs.PlateCarree(), colors='none', hatches=[None, '.'])
#         # artists, labels = ch.legend_elements()
#         # plt.legend(artists, labels, handleheight=2)
#         # plt.clim(minval,maxval)
#         ax.coastlines()
#         ax.gridlines()
#         # ax.set_global()
#
#         if title is None:
#             plt.title('%s with Agreement' % variable)
#         else:
#             plt.title(title)
#         plt.colorbar(cs)
#
#         plt.annotate('// = low model ensemble agreement', (0, 0), (0, -10),
#                      xycoords='axes fraction', textcoords='offset points', va='top')
#         plt.annotate('..  = high model ensemble agreement', (0, 0), (0, -20),
#                      xycoords='axes fraction', textcoords='offset points', va='top')
#
#         graphic = fig2plot(fig=fig, file_extension=file_extension)
#         plt.close()
#
#         LOGGER.info('Plot created and figure saved')
#     except:
#         msg = 'failed to plot graphic'
#         LOGGER.exception(msg)
#
#     return graphic
#
#
# def concat_images(images, orientation='v'):
#     """
#     concatenation of images.
#
#     :param images: list of images
#     :param orientation: vertical ('v' default) or horizontal ('h') concatenation
#
#     :return string: path to image
#     """
#     from PIL import Image
#     import sys
#
#     LOGGER.debug('Images to be concatinated: %s' % images)
#
#     if len(images) > 1:
#         try:
#             images_existing = [img for img in images if os.path.exists(img)]
#             open_images = map(Image.open, images_existing)
#             w = max(i.size[0] for i in open_images)
#             h = max(i.size[1] for i in open_images)
#             nr = len(open_images)
#             if orientation == 'v':
#                 result = Image.new("RGB", (w, h * nr))
#                 # p = nr # h / len(images)
#                 for i in range(len(open_images)):
#                     oi = open_images[i]
#                     cw = oi.size[0]
#                     ch = oi.size[1]
#                     cp = h * i
#                     box = [0, cp, cw, ch+cp]
#                     result.paste(oi, box=box)
#
#             if orientation == 'h':
#                 result = Image.new("RGB", (w * nr, h))
#                 # p = nr # h / len(images)
#                 for i in range(len(open_images)):
#                     oi = open_images[i]
#
#                     cw = oi.size[0]
#                     ch = oi.size[1]
#                     cp = w * i
#                     box = [cp, 0, cw+cp, ch]
#                     result.paste(oi, box=box)
#
#             ip, image = mkstemp(dir='.', suffix='.png')
#             result.save(image)
#         except:
#             LOGGER.exception('failed to concat images')
#             _, image = mkstemp(dir='.', suffix='.png')
#             result = Image.new("RGB", (50, 50))
#             result.save(image)
#     elif len(images) == 1:
#         image = images[0]
#     else:
#         LOGGER.exception('No concatable number of images: %s, Dummy will be produced' % len(images))
#         _, image = mkstemp(dir='.', suffix='.png')
#         result = Image.new("RGB", (50, 50))
#         result.save(image)
#     return image
#
#
# def pdfmerge(pdfs):
#     """
#     merge a list of pdfs
#
#     :param pdfs: list of pdf files
#
#     :retun str: merged pdf
#     """
#     from PyPDF2 import PdfFileMerger
#
#     # pdfs = ['file1.pdf', 'file2.pdf', 'file3.pdf', 'file4.pdf']
#     try:
#         merger = PdfFileMerger()
#         for pdf in pdfs:
#             merger.append(pdf)
#         _, mergedpdf = mkstemp(dir='.', suffix='.pdf')
#         merger.write(mergedpdf)
#     except:
#         LOGGER.excetion('failed to merge pdfs')
#         _, mergedpdf = mkstemp(dir='.', suffix='.pdf')
#
#     return mergedpdf
