# Exporter IFC Get Family Instance Assembly Offset Method

Source: https://www.revitapidocs.com/2026/14122a4d-1aa3-36ff-f781-8617cf06a8dd.htm

---

| Exporter IFC Get Family Instance Assembly Offset Method |
| --- |

Obtains Translation to adjust Family Instance within an Assembly, based on Family Symbol origin change. 
**Namespace:** [Autodesk.Revit.DB.IFC](../ungrouped/Autodesk.-Revit.-DB.-IFC-Namespace.md) 
**Assembly:** RevitAPIIFC (in RevitAPIIFC.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public XYZ GetFamilyInstanceAssemblyOffset(
	FamilyInstance familyInstance
)
```

```
Public Function GetFamilyInstanceAssemblyOffset ( 
	familyInstance As FamilyInstance
) As XYZ
```

```
public:
XYZ^ GetFamilyInstanceAssemblyOffset(
	FamilyInstance^ familyInstance
)
```

```
member GetFamilyInstanceAssemblyOffset : 
        familyInstance : FamilyInstance -> XYZ 
```

#### Parameters

familyInstance [FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.htm)
:   The family instance.

#### Return Value

[XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm) 
Translation for Family Instance. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[ExporterIFC Class](Exporter-IFC-Class.md) [Autodesk.Revit.DB.IFC Namespace](../ungrouped/Autodesk.-Revit.-DB.-IFC-Namespace.md)
