# -*- coding: utf-8 -*-
"""
Generated by ArcGIS ModelBuilder and Christopher Grasteit on : 2021-12-10 11:00:17
"""
import arcpy
from sys import argv

def SyncRevisedCompletedOffshoreFC(Division_FC="Project_Area_Mission_Q4", Quarterly_FC="Offshore Quarters Revised - Share\\OffshoreCompletedRev_Q4"):  # SyncRevisedCompletedOffshoreFC

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = True

    Field_Map = "CIRCUITNAME \"Circuit Name\" true true false 50 Text 0 0,First,#,C:\\Users\\c5gr\\OneDrive - PGE\\Desktop\\Data\\OneVM\\StorageOfDivisions-Offshore\\InProcess\\Mission_Q4.gdb\\Project_Area_Mission_Q4,CIRCUITNAME,0,50;InPoly_FID \"InPoly_FID\" true true false 4 Long 0 0,First,#,C:\\Users\\c5gr\\OneDrive - PGE\\Desktop\\Data\\OneVM\\StorageOfDivisions-Offshore\\InProcess\\Mission_Q4.gdb\\Project_Area_Mission_Q4,InPoly_FID,-1,-1;SimPgnFlag \"SimPgnFlag\" true true false 2 Short 0 0,First,#,C:\\Users\\c5gr\\OneDrive - PGE\\Desktop\\Data\\OneVM\\StorageOfDivisions-Offshore\\InProcess\\Mission_Q4.gdb\\Project_Area_Mission_Q4,SimPgnFlag,-1,-1;MaxSimpTol \"MaxSimpTol\" true true false 8 Double 0 0,First,#,C:\\Users\\c5gr\\OneDrive - PGE\\Desktop\\Data\\OneVM\\StorageOfDivisions-Offshore\\InProcess\\Mission_Q4.gdb\\Project_Area_Mission_Q4,MaxSimpTol,-1,-1;MinSimpTol \"MinSimpTol\" true true false 8 Double 0 0,First,#,C:\\Users\\c5gr\\OneDrive - PGE\\Desktop\\Data\\OneVM\\StorageOfDivisions-Offshore\\InProcess\\Mission_Q4.gdb\\Project_Area_Mission_Q4,MinSimpTol,-1,-1;SmoPgnFlag \"SmoPgnFlag\" true true false 2 Short 0 0,First,#,C:\\Users\\c5gr\\OneDrive - PGE\\Desktop\\Data\\OneVM\\StorageOfDivisions-Offshore\\InProcess\\Mission_Q4.gdb\\Project_Area_Mission_Q4,SmoPgnFlag,-1,-1;ORIG_FID \"ORIG_FID\" true true false 4 Long 0 0,First,#,C:\\Users\\c5gr\\OneDrive - PGE\\Desktop\\Data\\OneVM\\StorageOfDivisions-Offshore\\InProcess\\Mission_Q4.gdb\\Project_Area_Mission_Q4,ORIG_FID,-1,-1;Project_ID \"Project ID\" true true false 4 Long 0 0,First,#,Project_Area_Mission_Q4,ProjectID,0,20;DivCode \"DivCode\" true true false 255 Text 0 0,First,#,C:\\Users\\c5gr\\OneDrive - PGE\\Desktop\\Data\\OneVM\\StorageOfDivisions-Offshore\\InProcess\\Mission_Q4.gdb\\Project_Area_Mission_Q4,DivCode,0,255;ProjectYear \"ProjectYear\" true true false 4 Long 0 0,First,#,C:\\Users\\c5gr\\OneDrive - PGE\\Desktop\\Data\\OneVM\\StorageOfDivisions-Offshore\\InProcess\\Mission_Q4.gdb\\Project_Area_Mission_Q4,ProjectYear,-1,-1"

    # Process: Append (Append) 
    OffshoreCompletedRev_Q4 = arcpy.Append_management(inputs=[Division_FC], target=Quarterly_FC, schema_type="NO_TEST", field_mapping=Field_Map, subtype="", expression="")[0]

if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(outputCoordinateSystem="PROJCS['NAD_1983_UTM_Zone_10N',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',1640416.666666667],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-123.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Foot_US',0.3048006096012192]]", scratchWorkspace=r"C:\Users\c5gr\OneDrive - PGE\Desktop\Data\OneVM\OneVMProcess.gdb", workspace=r"C:\Users\c5gr\OneDrive - PGE\Desktop\Data\OneVM\OneVMProcess.gdb"):
        SyncRevisedCompletedOffshoreFC(*argv[1:])
