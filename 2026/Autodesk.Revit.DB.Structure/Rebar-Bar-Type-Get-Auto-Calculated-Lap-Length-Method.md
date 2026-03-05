# Rebar Bar Type Get Auto Calculated Lap Length Method

Source: https://www.revitapidocs.com/2026/cec3b77b-eea8-7a64-4cdb-2d3f6cdce6ec.htm

---

| Rebar Bar Type Get Auto Calculated Lap Length Method |
| --- |

Identifies if the lap length is auto calculated for the specified Rebar Splice Type. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public bool GetAutoCalculatedLapLength(
	ElementId rebarSpliceTypeId
)
```

```
Public Function GetAutoCalculatedLapLength ( 
	rebarSpliceTypeId As ElementId
) As Boolean
```

```
public:
bool GetAutoCalculatedLapLength(
	ElementId^ rebarSpliceTypeId
)
```

```
member GetAutoCalculatedLapLength : 
        rebarSpliceTypeId : ElementId -> bool 
```

#### Parameters

rebarSpliceTypeId [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
:   The Rebar Splice Type id.
 Interactions with Rebar Splice Types can be done with the functions in [RebarSpliceTypeUtils](98b9e51e-cd97-954d-4a31-a5189696b27e.htm) .

#### Return Value

Boolean 
Returns true if the lap length is auto calculated for the specified Rebar Bar Type and Rebar Splice Type, false otherwise. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The rebarSpliceTypeId doesn't represent a valid Rebar Splice Type. It should be an ElementType of BuiltInCategory.OST\_RebarSpliceType category. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks If it is auto calculated, lap length value is computed based on the formula: lap length multiplier (found in splice type) \* bar nominal diameter. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarBarType Class](Rebar-Bar-Type-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
