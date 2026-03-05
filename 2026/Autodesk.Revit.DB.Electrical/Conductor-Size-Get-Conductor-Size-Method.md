# Conductor Size Get Conductor Size Method

Source: https://www.revitapidocs.com/2026/cee6bfc3-50f9-c0b7-d4e1-9fd01d36c8d3.htm

---

| Conductor Size Get Conductor Size Method |
| --- |

Gets the Conductor Size data by given Conductor Size id. 
**Namespace:** [Autodesk.Revit.DB.Electrical](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static ConductorSize GetConductorSize(
	Document document,
	ElementId conductorSizeId
)
```

```
Public Shared Function GetConductorSize ( 
	document As Document,
	conductorSizeId As ElementId
) As ConductorSize
```

```
public:
static ConductorSize^ GetConductorSize(
	Document^ document, 
	ElementId^ conductorSizeId
)
```

```
static member GetConductorSize : 
        document : Document * 
        conductorSizeId : ElementId -> ConductorSize 
```

#### Parameters

document [Document](../Autodesk.Revit.DB/Document-Class.md)
:   The document.

conductorSizeId [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
:   The Conductor Size id.

#### Return Value

[ConductorSize](Conductor-Size-Class.md) 
The Conductor Size data. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | document is not a project document.  \-or\-  The id is not a Conductor Size id. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The document is in failure mode: an operation has failed,  and Revit requires the user to either cancel the operation  or fix the problem (usually by deleting certain elements). |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[ConductorSize Class](Conductor-Size-Class.md) [Autodesk.Revit.DB.Electrical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md)
