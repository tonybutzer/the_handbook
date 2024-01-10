import geopandas as gpd
from pystac_client import Client
from shapely.geometry import mapping
import pandas as pd

"""
Hi everyone,

We have finished the build, deployment, and checkout testing of our LSAA Tile Products release.  We would like for all of you to take a look before we make a public announcement about the release next Tuesday (after the USGS PDB discusses the release).  A few items of note:

1.	The production STAC Server is located at: https://landsatlook.usgs.gov/stac-server  (the ST STAC Server is still at: https://st-usgs-landsat-dds.qa-lsdsdpas.chs.usgs.gov/stac-server)
2.	This release has all new tile products in our public usgs-landsat-ard bucket, with requester pays turned on.
3.	This release has all newly generated STAC Records for all of our Tile products
4.	This release also has re-generated Scene STAC Records that have the double forward slash '//' fixed, which GA mentioned; also, we have fixed the missing ‘ST_B6.TIF’ asset for Landsat 7 Albers items, which Saeed mentioned (we are still working that update to the L7 tiles but should be done today).
5.	STAC Server was upgraded to 0.3.1.  Our internal version of STAC Browser was also updated.
6.	We switched over to a new SAT-API cluster for LandsatLook, and the records are now 1.0.0 compliant (had been 1.0.0-beta.2) and the asset keys have changed.  We are still generating a few final SAT-API records, but they should all be there sometime today.  GA had mentioned they could only get records up through July 23 recently, but they should all be in the new cluster. NOTE: SAT-API is just being kept around for LandsatLook. However, we plan to remove SAT-API and use STAC Server in the next LL release.  So, anyone still using SAT-API (I believe GA is) should make plans to switch over.
STAC-related items NOT in this release, but planned for the next STAC release in November:
1.	A geometric accuracy extension (Matt Hanson is working on a CARD4L extension for this)
2.	An SNS topic that will send the body of each new STAC record generated
"""

# functions

import hvplot.pandas


# User configurable settings

# plot size settings
frame_width = 600
frame_height = 600

# line width of polygons
line_width = 3

# plot polygons as lines on a slippy map with background tiles.
def plot_polygons(data, *args, **kwargs):
    return data.hvplot.paths(*args, geo=True, tiles='OSM', xaxis=None, yaxis=None,
                             frame_width=frame_width, frame_height=frame_height,
                             line_width=line_width, **kwargs)

class LTWGL:
    def __init__(self, platform, aoi, date_range, cloud_cover_threshold):
        print("Instantiate class LTWGL (Landsat)")
        print("CLOUD Threshold is", cloud_cover_threshold, "percent.")
        self.cloud_cover_threshold = cloud_cover_threshold
        self.aoi = aoi
        self.platform = platform
        self.date_range = date_range
        self.url = 'https://earth-search.aws.element84.com/v0'
        #self.url = 'https://landsatlook.usgs.gov/stac-server'
        #self.url = 'https://ibhoyw8md9.execute-api.us-west-2.amazonaws.com/prod'
        #self.url = 'https://landsatlook.usgs.gov/sat-api/stac'


        filename = self.aoi
        aoi_gpd = gpd.read_file(filename)

        geom = mapping(aoi_gpd.to_dict()['geometry'][0])
        # Search parameters
        self.params = {
            "collections":['landsat-8-l1-c1'],
            #"collections": ["landsat-c2l2-sr"],
            #"collections": ["sentinel-s2-l2a-cogs"],
            "intersects": geom,
            "datetime": date_range,
            "limit": 100,
            "query": [f'eo:cloud_cover<={cloud_cover_threshold}']
        }


    def __repr__(self):
        return(f"CLOUD Threshold is {self.cloud_cover_threshold} percent. \n platform={self.platform}."+
               f'date_range={self.date_range}')


    def show_map(self):
        # read in AOI as a GeoDataFrame

        filename = self.aoi
        aoi_gpd = gpd.read_file(filename)
        return(plot_polygons(aoi_gpd))
	
    
    def item_count(self):

        cat = Client.open(self.url)
        self.search = cat.search(**self.params)

        matched = self.search.matched()
        if matched is not None:
            self.items_dict = [i.to_dict() for i in self.search.items()]
            return(matched)
        else:
            return(0)

    def list_scenes(self):
        self.items = []
        for item in self.search.items():
            self.items.append(item)
            print(item.id)
            
    def df_meta_s(self,index):
        #print(self.items[0].properties)
        mdf = pd.DataFrame(self.items[index].properties)
        # datetime 	platform 	constellation 	instruments 	gsd 	view:off_nadir 	proj:epsg 	sentinel:utm_zone 	sentinel:latitude_band 	sentinel:grid_square 	sentinel:sequence 	sentinel:product_id 	sentinel:data_coverage 	eo:cloud_cover 	sentinel:valid_cloud_cover 	created 	updated--
        pruned_df = mdf[["datetime", "platform", 'instruments', 'gsd', 'eo:cloud_cover']]
        pruned_df.set_index('datetime', inplace=True)

        return(pruned_df)
    
    def df_asset_s(self,index):
        
        assets = pd.DataFrame.from_dict(self.items_dict[index]['assets'], orient='index')

        for f in ['href', 'alternate', 'file:checksum', 'proj:transform', 'rel']:
            if f in assets:
                del assets[f]
        #type 	title 	roles 	gsd 	eo:bands 	proj:shape

        return(assets)
