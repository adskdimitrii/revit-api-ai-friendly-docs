# Rebar Set Bar Included Method

Source: https://www.revitapidocs.com/2026/b6bd8b08-36ab-ec51-a533-8c918b2fe42c.htm

---

| Rebar Set Bar Included Method |
| --- |

Sets if the bar at the desired index is included or not. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetBarIncluded(
	bool include,
	int barPositionIndex
)
```

```
Public Sub SetBarIncluded ( 
	include As Boolean,
	barPositionIndex As Integer
)
```

```
public:
void SetBarIncluded(
	bool include, 
	int barPositionIndex
)
```

```
member SetBarIncluded : 
        include : bool * 
        barPositionIndex : int -> unit 
```

#### Parameters

include Boolean
:   True to include the bar, false to exclude the bar.

barPositionIndex Int32
:   The bar index.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | barPositionIndex should be in range \[ 0, NumberOfBarPositions\-1 ] and the bar at barPositionIndex should be included. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Rebar Class](Rebar-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
