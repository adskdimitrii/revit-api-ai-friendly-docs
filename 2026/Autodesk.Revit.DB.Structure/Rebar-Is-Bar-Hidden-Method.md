# Rebar Is Bar Hidden Method

Source: https://www.revitapidocs.com/2026/d066eb29-243b-bcc9-2468-c5df0f255a13.htm

---

| Rebar Is Bar Hidden Method |
| --- |

Identifies if a given bar in this rebar set is hidden in this view. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public bool IsBarHidden(
	View view,
	int barIndex
)
```

```
Public Function IsBarHidden ( 
	view As View,
	barIndex As Integer
) As Boolean
```

```
public:
bool IsBarHidden(
	View^ view, 
	int barIndex
)
```

```
member IsBarHidden : 
        view : View * 
        barIndex : int -> bool 
```

#### Parameters

view [View](../Autodesk.Revit.DB/View-Class.md)
:   The view.

barIndex Int32
:   The index of the bar from this rebar set.

#### Return Value

Boolean 
True if the bar is hidden in this view, false otherwise. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | barIndex should be in range \[ 0, NumberOfBarPositions\-1 ] and the bar at barIndex should be included. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Rebar Class](Rebar-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
