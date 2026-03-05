# Rebar Reset Moved Bar Transform Method

Source: https://www.revitapidocs.com/2026/5e2e7166-d294-88a3-5b03-1d38ce930546.htm

---

| Rebar Reset Moved Bar Transform Method |
| --- |

Reset the transformation representing the movement of the bar relative to its default position along the distribution path.
 The moved bar transform will be set to Identity. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void ResetMovedBarTransform(
	int barPositionIndex
)
```

```
Public Sub ResetMovedBarTransform ( 
	barPositionIndex As Integer
)
```

```
public:
void ResetMovedBarTransform(
	int barPositionIndex
)
```

```
member ResetMovedBarTransform : 
        barPositionIndex : int -> unit 
```

#### Parameters

barPositionIndex Int32
:   The bar index.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | barPositionIndex should be in range \[ 0, NumberOfBarPositions\-1 ] and the bar at barPositionIndex should be included. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Rebar Class](Rebar-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
