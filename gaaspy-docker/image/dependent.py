import os
import re
import time
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pipe import select, where
from functools import partial
from typing import Union, Tuple
from functools import partial
from dataclasses import dataclass
import rasterio as rio
from rasterio.plot import show
from rasterio.mask import mask
from rasterio.profiles import Profile
from rasterio.enums import Resampling
from rasterio.coords import BoundingBox
from rasterio.warp import reproject, transform_bounds
import geopandas as gpd
from shapely.geometry import Polygon, LineString, MultiLineString, box
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

import logging


print("Hello are all these modules working")

