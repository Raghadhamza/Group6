**BIManalyst group6**

**Architecture specifically the Facade**

**The claim we are checking is facade transparency. In the report it is stated to be 37%**

**The report is CES_BLD_24_06_ARC and its on page 5.**

**Our script**
```python
# BIManalyst group 06
import ifcopenshell
from bonsai.bim.ifc import IfcStore
file = IfcStore.get_file()
things = file.by_type('IfcWindow')
print(len(things))

things1 = file.by_type('IfcPlate')
print("Plate"len(things1))

things2 = file.by_type('IfcCurtainWall')
print("Curtain walls", len(things2))

```

**The result**

#The script is looking at the length of windows which is zero, meaning windows is labeled elsewhere in the model. Therefore the script looks at Ifcplate to count the number of windows, and ifccurtainwall to count the number of plates. However, upon inspection the windows and plates are sometimes mislabeled, leading to the values being inaccurate.
#IfcCurtain wall outputs the plates on the facade while ifcplate outputs the windows on the facade, however the BIM model is not entirely accurate so some windows are placed in different areas therefore it is not possible to extract the exact numbers of windows to plates to find the glazing ratio. If we use the output values of IfcCurtainWall = 2818 and Ifcplate = 1509 then the facade transparency is 53.5% which is not the same as the report. The report states that the facade transparency is 37% this proves that the BIM model is not accurately labeled since the value extracted from there is 53.5%.
