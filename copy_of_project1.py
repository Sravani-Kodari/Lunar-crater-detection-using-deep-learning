# -*- coding: utf-8 -*-
"""Copy of project1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1h8b40lvZfsIJsabrdnnvaXW5dFB_AQed
"""

import os

!pip install gis

print(globals().get('GIS'))

import gis

from pathlib import Path

!pip install arcgis

from arcgis import gis

!pip install timm

!pip show timm

!pip install timm

!pip install --upgrade timm

from timm.models import helpers

from arcgis.learn import MaskRCNN, prepare_data

from arcgis import GIS

!pip install arcpy

!pip show arcpy

!pip install arcpy

gis=GIS()

craters_5_20km = gis.content.get('af240e45a3ca445b88d6ec19209d3bb5')
craters_5_20km

lunar_dem = gis.content.get('beae2f7947704c938eb957c6deb2fa2b')
lunar_dem

craters_more_than_20km = gis.content.get('36272e93ec4547abba495c797a4fb921')
craters_more_than_20km

inRaster = "Lunar DEM"
out_folder = "D:/data/lunar_craters_256px_128strd"
in_training = "craters"
image_chip_format = "TIFF"
tile_size_x = "256"
tile_size_y = "256"
stride_x= "128"
stride_y= "128"
output_nofeature_tiles= "ONLY_TILES_WITH_FEATURES"
metadata_format= "Labeled_Tiles"
start_index = 0
classvalue_field = "Classvalue"
buffer_radius = 0
in_mask_polygons = "MaskPolygon"
rotation_angle = 0
reference_system = "PIXEL_SPACE"
processing_mode = "PROCESS_AS_MOSAICKED_IMAGE"
blacken_around_feature = "NO_BLACKEN"

(inRaster, out_folder, in_training,
    image_chip_format,tile_size_x, tile_size_y, stride_x,
    stride_y,output_nofeature_tiles, metadata_format, start_index,
    classvalue_field, buffer_radius, in_mask_polygons, rotation_angle,
    reference_system, processing_mode, blacken_around_feature)

training_data = gis.content.get('0a4e2d4ad7bf41f6973c7e3434faf7d4')
training_data

filepath = training_data.download(file_name=training_data.name)

import zipfile
with zipfile.ZipFile(filepath, 'r') as zip_ref:
    zip_ref.extractall(Path(filepath).parent)

output_path = Path(os.path.join(os.path.splitext(filepath)[0]))

data = prepare_data(output_path, batch_size=8)

data.show_batch(rows=2)

model = MaskRCNN(data)

lr = model.lr_find()
lr

model.fit(100, lr, early_stopping=True)

model.save("moon_mrcnn_2", publish=True)

Published DLPK Item Id: 81e635734e1b4d558cd51e2cee44833a

WindowsPath('C:/Users/shi10484/AppData/Local/Temp/lunar_craters_detection_from_digital_elevation_models_using_deep_learning/models/moon_mrcnn_2')

model.show_results(rows=2, mask_threshold=0.7)

model.average_precision_score()

arcpy.ia.DetectObjectsUsingDeepLearning(in_raster="dem_for_inference", out_detected_objects=r"\\detected_craters", in_model_definition=r"\\models\moon_mrcnn_2\moon_mrcnn_2.dlpk", model_arguments ="padding 56;batch_size 4;threshold 0.6;return_bboxes False", run_nms="NMS", confidence_score_field="Confidence", class_value_field="Class", max_overlap_ratio=0, processing_mode="PROCESS_AS_MOSAICKED_IMAGE")

from arcgis.mapping import WebMap
## Area1 Craters
LunarArea1 = gis.content.get('1a76ed548cfc4e159d860ae253e5ecc3')
map1 = WebMap(LunarArea1)
map1

LunarArea2 = gis.content.get('2ce5ad91fab649c7982dde750cce3390')
map2 = WebMap(LunarArea2)
map2

!pip install arcGIS Pro
