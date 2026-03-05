# Cable Type Set Cable Size Usable Method

Source: https://www.revitapidocs.com/2026/2a0a7f44-9dcf-584e-0270-e8fbbddee4d0.htm

---

| Cable Type Set Cable Size Usable Method |
| --- |

Marks the Cable Size can be used by this Cable Type. 
**Namespace:** [Autodesk.Revit.DB.Electrical](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetCableSizeUsable(
	ElementId cableSizeId,
	bool usable
)
```

```
Public Sub SetCableSizeUsable ( 
	cableSizeId As ElementId,
	usable As Boolean
)
```

```
public:
void SetCableSizeUsable(
	ElementId^ cableSizeId, 
	bool usable
)
```

```
member SetCableSizeUsable : 
        cableSizeId : ElementId * 
        usable : bool -> unit 
```

#### Parameters

cableSizeId [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
:   The Cable Size id.

usable Boolean
:   The Cable Size can be used by this Cable Type or not.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The id is not a Cable Size id. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[CableType Class](Cable-Type-Class.md) [Autodesk.Revit.DB.Electrical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md)
