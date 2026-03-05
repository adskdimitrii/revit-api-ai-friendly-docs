# Insulation Material Get Insulation Material Method

Source: https://www.revitapidocs.com/2026/e1996b65-d4f5-88ea-313a-77e4d106f25e.htm

---

| Insulation Material Get Insulation Material Method |
| --- |

Gets the Conductor Insulation Material data by given Conductor Insulation Material id. 
**Namespace:** [Autodesk.Revit.DB.Electrical](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static InsulationMaterial GetInsulationMaterial(
	Document document,
	ElementId insulationMaterialId
)
```

```
Public Shared Function GetInsulationMaterial ( 
	document As Document,
	insulationMaterialId As ElementId
) As InsulationMaterial
```

```
public:
static InsulationMaterial^ GetInsulationMaterial(
	Document^ document, 
	ElementId^ insulationMaterialId
)
```

```
static member GetInsulationMaterial : 
        document : Document * 
        insulationMaterialId : ElementId -> InsulationMaterial 
```

#### Parameters

document [Document](../Autodesk.Revit.DB/Document-Class.md)
:   The document.

insulationMaterialId [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
:   The Conductor Insulation Material id.

#### Return Value

[InsulationMaterial](Insulation-Material-Class.md) 
The Conductor Insulation Material data. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | document is not a project document.  \-or\-  The id is not a Conductor Insulation Material id. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The document is in failure mode: an operation has failed,  and Revit requires the user to either cancel the operation  or fix the problem (usually by deleting certain elements). |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[InsulationMaterial Class](Insulation-Material-Class.md) [Autodesk.Revit.DB.Electrical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md)
