# Rebar Get Moved Bar Transform Method

Source: https://www.revitapidocs.com/2026/8db286b5-f16e-2367-7e1f-de58fe5a84b8.htm

---

| Rebar Get Moved Bar Transform Method |
| --- |

Returns a transform representing the movement of the bar relative to its default position along the distribution path. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public Transform GetMovedBarTransform(
	int barPositionIndex
)
```

```
Public Function GetMovedBarTransform ( 
	barPositionIndex As Integer
) As Transform
```

```
public:
Transform^ GetMovedBarTransform(
	int barPositionIndex
)
```

```
member GetMovedBarTransform : 
        barPositionIndex : int -> Transform 
```

#### Parameters

barPositionIndex Int32
:   The bar index.

#### Return Value

[Transform](58dd01c8-b3fc-7142-e4f3-c524079a282d.htm) 
The transform representing the movement of the bar relative to its default position along the distribution path. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | barPositionIndex should be in range \[ 0, NumberOfBarPositions\-1 ] and the bar at barPositionIndex should be included. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Rebar Class](Rebar-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
