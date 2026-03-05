# Conductor Material Get Conductor Material Ids Method

Source: https://www.revitapidocs.com/2026/df578b29-16e9-6d64-e33a-30178c75e509.htm

---

| Conductor Material Get Conductor Material Ids Method |
| --- |

Gets all the Conductor Material ids in the given document, sorted by name. 
**Namespace:** [Autodesk.Revit.DB.Electrical](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static IList<ElementId> GetConductorMaterialIds(
	Document document
)
```

```
Public Shared Function GetConductorMaterialIds ( 
	document As Document
) As IList(Of ElementId)
```

```
public:
static IList<ElementId^>^ GetConductorMaterialIds(
	Document^ document
)
```

```
static member GetConductorMaterialIds : 
        document : Document -> IList<ElementId> 
```

#### Parameters

document [Document](../Autodesk.Revit.DB/Document-Class.md)
:   The document.

#### Return Value

IList [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md) 
All the Conductor Material ids in this document. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | document is not a project document. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The document is in failure mode: an operation has failed,  and Revit requires the user to either cancel the operation  or fix the problem (usually by deleting certain elements). |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[ConductorMaterial Class](Conductor-Material-Class.md) [Autodesk.Revit.DB.Electrical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md)
