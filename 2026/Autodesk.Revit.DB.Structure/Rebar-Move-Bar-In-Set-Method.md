# Rebar Move Bar In Set Method

Source: https://www.revitapidocs.com/2026/f1ff60b3-7882-c352-e03c-a00208993e04.htm

---

| Rebar Move Bar In Set Method |
| --- |

This method applies the transformation matrix to the rebar bar at the desired position in the rebar set.
 If the bar was already moved, the method will concatenate the transformation matrix with the existing movement. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void MoveBarInSet(
	int barPositionIndex,
	Transform moveTransform
)
```

```
Public Sub MoveBarInSet ( 
	barPositionIndex As Integer,
	moveTransform As Transform
)
```

```
public:
void MoveBarInSet(
	int barPositionIndex, 
	Transform^ moveTransform
)
```

```
member MoveBarInSet : 
        barPositionIndex : int * 
        moveTransform : Transform -> unit 
```

#### Parameters

barPositionIndex Int32
:   The bar index of the rebar to apply the transformation.

moveTransform [Transform](58dd01c8-b3fc-7142-e4f3-c524079a282d.htm)
:   The transformation matrix to apply to the specified rebar bar.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | barPositionIndex should be in range \[ 0, NumberOfBarPositions\-1 ] and the bar at barPositionIndex should be included.  \-or\-  moveTransform is not conformal. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Rebar Class](Rebar-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
