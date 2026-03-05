# Cable Size Get Cable Size Ids Method

Source: https://www.revitapidocs.com/2026/fc2452ad-5d22-9b36-4842-f6c8d6364068.htm

---

| Cable Size Get Cable Size Ids Method |
| --- |

Gets all the Cable Size ids in the given document, sorted by name. 
**Namespace:** [Autodesk.Revit.DB.Electrical](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static IList<ElementId> GetCableSizeIds(
	Document document
)
```

```
Public Shared Function GetCableSizeIds ( 
	document As Document
) As IList(Of ElementId)
```

```
public:
static IList<ElementId^>^ GetCableSizeIds(
	Document^ document
)
```

```
static member GetCableSizeIds : 
        document : Document -> IList<ElementId> 
```

#### Parameters

document [Document](../Autodesk.Revit.DB/Document-Class.md)
:   The document.

#### Return Value

IList [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md) 
All the Cable Size ids in this document. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | document is not a project document. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The document is in failure mode: an operation has failed,  and Revit requires the user to either cancel the operation  or fix the problem (usually by deleting certain elements). |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[CableSize Class](Cable-Size-Class.md) [Autodesk.Revit.DB.Electrical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md)
