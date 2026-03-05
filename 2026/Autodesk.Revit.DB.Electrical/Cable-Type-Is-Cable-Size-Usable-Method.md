# Cable Type Is Cable Size Usable Method

Source: https://www.revitapidocs.com/2026/8488b8a0-1bf8-bf15-9c4f-3326b95d5fd1.htm

---

| Cable Type Is Cable Size Usable Method |
| --- |

Checks whether the Cable Size can be used by this Cable Type or not. 
**Namespace:** [Autodesk.Revit.DB.Electrical](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public bool IsCableSizeUsable(
	ElementId cableSizeId
)
```

```
Public Function IsCableSizeUsable ( 
	cableSizeId As ElementId
) As Boolean
```

```
public:
bool IsCableSizeUsable(
	ElementId^ cableSizeId
)
```

```
member IsCableSizeUsable : 
        cableSizeId : ElementId -> bool 
```

#### Parameters

cableSizeId [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
:   The Cable Size id.

#### Return Value

Boolean 
True if the Cable Size can be used by this Cable Type. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The id is not a Cable Size id. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[CableType Class](Cable-Type-Class.md) [Autodesk.Revit.DB.Electrical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md)
