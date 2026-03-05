# Cable Size Get Cable Size Method

Source: https://www.revitapidocs.com/2026/a03be136-fec3-9b70-0e53-ad2a799dbd4b.htm

---

| Cable Size Get Cable Size Method |
| --- |

Gets the Cable Size data by given Cable Size id. 
**Namespace:** [Autodesk.Revit.DB.Electrical](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static CableSize GetCableSize(
	Document document,
	ElementId cableSizeId
)
```

```
Public Shared Function GetCableSize ( 
	document As Document,
	cableSizeId As ElementId
) As CableSize
```

```
public:
static CableSize^ GetCableSize(
	Document^ document, 
	ElementId^ cableSizeId
)
```

```
static member GetCableSize : 
        document : Document * 
        cableSizeId : ElementId -> CableSize 
```

#### Parameters

document [Document](../Autodesk.Revit.DB/Document-Class.md)
:   The document.

cableSizeId [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
:   The Cable Size id.

#### Return Value

[CableSize](Cable-Size-Class.md) 
The Cable Size data. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | document is not a project document. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The document is in failure mode: an operation has failed,  and Revit requires the user to either cancel the operation  or fix the problem (usually by deleting certain elements). |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[CableSize Class](Cable-Size-Class.md) [Autodesk.Revit.DB.Electrical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md)
