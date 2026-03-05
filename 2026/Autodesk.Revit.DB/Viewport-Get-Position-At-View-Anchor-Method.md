# Viewport Get Position At View Anchor Method

Source: https://www.revitapidocs.com/2026/e5c279a1-b4e1-4bb2-6e62-2ba971bb16ae.htm

---

| Viewport Get Position At View Anchor Method |
| --- |

Gets the position coordinates at the ViewAnchor. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public XYZ GetPositionAtViewAnchor(
	ViewAnchor viewAnchor
)
```

```
Public Function GetPositionAtViewAnchor ( 
	viewAnchor As ViewAnchor
) As XYZ
```

```
public:
XYZ^ GetPositionAtViewAnchor(
	ViewAnchor viewAnchor
)
```

```
member GetPositionAtViewAnchor : 
        viewAnchor : ViewAnchor -> XYZ 
```

#### Parameters

viewAnchor [ViewAnchor](View-Anchor-Enumeration.md)
:   The viewAnchor at which the position is requested.

#### Return Value

[XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm) 
The position at the ViewAnchor. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given value of viewAnchor cannot be applied to this Viewport. |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Viewport Class](Viewport-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
