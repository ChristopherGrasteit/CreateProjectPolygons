# -*- coding: utf-8 -*-
"""
Generated by ArcGIS ModelBuilder on : 2021-10-06 11:49:54
"""
import arcpy
from sys import argv

def CalcValuesMakeAdjustments(project_area_polygon_northcoast="NewProcess FC (5)\\project_area_polygon_northcoast", Code_Block):  # CalcValuesMakeAdjustments

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False


    # Process: Calculate Field (Calculate Field) 
    project_area_polygon_kern = arcpy.CalculateField_management(in_table=project_area_polygon_northcoast, field="PROJECT_NAME", expression="!PROJECT_NAME!.rstrip(\"-\")", expression_type="PYTHON3", code_block="", field_type="TEXT")[0]

    # Process: Calculate Field (2) (Calculate Field) 
    project_area_polygon_northcoast_2_ = arcpy.CalculateField_management(in_table=project_area_polygon_kern, field="Div", expression="\"NC\"", expression_type="PYTHON3", code_block=Code_Block, field_type="TEXT")[0]

if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace=r"C:\Users\c5gr\OneDrive - PGE\Desktop\Data\VMGIS\VMGISPro\VMGISPro.gdb", workspace=r"C:\Users\c5gr\OneDrive - PGE\Desktop\Data\VMGIS\VMGISPro\VMGISPro.gdb"):
        CalcValuesMakeAdjustments(*argv[1:])
