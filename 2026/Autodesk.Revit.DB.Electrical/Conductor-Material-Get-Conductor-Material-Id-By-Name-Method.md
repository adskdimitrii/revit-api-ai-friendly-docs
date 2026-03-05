# Conductor Material Get Conductor Material Id By Name Method

Source: https://www.revitapidocs.com/2026/1119b7c5-fde3-65db-4685-b12c7eb61775.htm

---

| Conductor Material Get Conductor Material Id By Name Method |
| --- |

Gets the Conductor Material id by given Conductor Material name. 
**Namespace:** [Autodesk.Revit.DB.Electrical](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static ElementId GetConductorMaterialIdByName(
	Document document,
	string name
)
```

```
Public Shared Function GetConductorMaterialIdByName ( 
	document As Document,
	name As String
) As ElementId
```

```
public:
static ElementId^ GetConductorMaterialIdByName(
	Document^ document, 
	String^ name
)
```

```
static member GetConductorMaterialIdByName : 
        document : Document * 
        name : string -> ElementId 
```

#### Parameters

document [Document](../Autodesk.Revit.DB/Document-Class.md)
:   The document.

name String
:   The Conductor Material name.

#### Return Value

[ElementId](../Autodesk.Revit.DB/Element-Id-Class.md) 
The Conductor Material id. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | document is not a project document.  \-or\-  name cannot include prohibited characters, such as "{, }, \[, ], \|, ;, less\-than sign, greater\-than sign, ?, \`, \~".  \-or\-  name is an empty string. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The document is in failure mode: an operation has failed,  and Revit requires the user to either cancel the operation  or fix the problem (usually by deleting certain elements). |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[ConductorMaterial Class](Conductor-Material-Class.md) [Autodesk.Revit.DB.Electrical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md)
