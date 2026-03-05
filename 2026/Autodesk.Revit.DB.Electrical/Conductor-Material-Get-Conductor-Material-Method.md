# Conductor Material Get Conductor Material Method

Source: https://www.revitapidocs.com/2026/e94e5e9d-0302-5c6f-2b7f-6eb0d18de312.htm

---

| Conductor Material Get Conductor Material Method |
| --- |

Gets the Conductor Material data by given Conductor Material id. 
**Namespace:** [Autodesk.Revit.DB.Electrical](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static ConductorMaterial GetConductorMaterial(
	Document document,
	ElementId conductorMaterialId
)
```

```
Public Shared Function GetConductorMaterial ( 
	document As Document,
	conductorMaterialId As ElementId
) As ConductorMaterial
```

```
public:
static ConductorMaterial^ GetConductorMaterial(
	Document^ document, 
	ElementId^ conductorMaterialId
)
```

```
static member GetConductorMaterial : 
        document : Document * 
        conductorMaterialId : ElementId -> ConductorMaterial 
```

#### Parameters

document [Document](../Autodesk.Revit.DB/Document-Class.md)
:   The document.

conductorMaterialId [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
:   The Conductor Material id.

#### Return Value

[ConductorMaterial](Conductor-Material-Class.md) 
The Conductor Material data. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | document is not a project document.  \-or\-  The id is not a Conductor Material id. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The document is in failure mode: an operation has failed,  and Revit requires the user to either cancel the operation  or fix the problem (usually by deleting certain elements). |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[ConductorMaterial Class](Conductor-Material-Class.md) [Autodesk.Revit.DB.Electrical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md)
