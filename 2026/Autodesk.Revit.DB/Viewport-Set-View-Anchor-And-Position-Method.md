# Viewport Set View Anchor And Position Method

Source: https://www.revitapidocs.com/2026/d4ad4603-33b8-2c4f-b7e5-2c012a80d932.htm

---

| Viewport Set View Anchor And Position Method |
| --- |

Sets the ViewAnchor and position to Viewport. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetViewAnchorAndPosition(
	ViewAnchor viewAnchor,
	XYZ position
)
```

```
Public Sub SetViewAnchorAndPosition ( 
	viewAnchor As ViewAnchor,
	position As XYZ
)
```

```
public:
void SetViewAnchorAndPosition(
	ViewAnchor viewAnchor, 
	XYZ^ position
)
```

```
member SetViewAnchorAndPosition : 
        viewAnchor : ViewAnchor * 
        position : XYZ -> unit 
```

#### Parameters

viewAnchor [ViewAnchor](View-Anchor-Enumeration.md)
:   The viewAnchor to be assigned.

position [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)
:   The position to be assigned.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given value of viewAnchor cannot be applied to this Viewport. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Viewport Class](Viewport-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
