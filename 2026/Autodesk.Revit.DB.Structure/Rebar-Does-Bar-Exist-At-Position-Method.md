# Rebar Does Bar Exist At Position Method

Source: https://www.revitapidocs.com/2026/f223b762-1ef9-bf37-29e3-202dd570edb8.htm

---

| Rebar Does Bar Exist At Position Method |
| --- |

Checks whether a bar is included at the specified position. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public bool DoesBarExistAtPosition(
	int barPosition
)
```

```
Public Function DoesBarExistAtPosition ( 
	barPosition As Integer
) As Boolean
```

```
public:
bool DoesBarExistAtPosition(
	int barPosition
)
```

```
member DoesBarExistAtPosition : 
        barPosition : int -> bool 
```

#### Parameters

barPosition Int32
:   A bar position index between 0 and NumberOfBarPositions\-1\.

#### Return Value

Boolean 
Returns true if the bar at the specified position is included, false otherwise. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | barPosition should be in range \[ 0, NumberOfBarPositions\-1 ] and the bar at barPosition should be included. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Rebar Class](Rebar-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
