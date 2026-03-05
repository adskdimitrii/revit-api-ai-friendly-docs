# Rebar Bar Type Get Auto Calculated Stagger Length Method

Source: https://www.revitapidocs.com/2026/016b3925-9e16-8268-2a61-01a55af96baf.htm

---

| Rebar Bar Type Get Auto Calculated Stagger Length Method |
| --- |

Identifies if the stagger length is auto calculated for the specified Rebar Splice Type. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public bool GetAutoCalculatedStaggerLength(
	ElementId rebarSpliceTypeId
)
```

```
Public Function GetAutoCalculatedStaggerLength ( 
	rebarSpliceTypeId As ElementId
) As Boolean
```

```
public:
bool GetAutoCalculatedStaggerLength(
	ElementId^ rebarSpliceTypeId
)
```

```
member GetAutoCalculatedStaggerLength : 
        rebarSpliceTypeId : ElementId -> bool 
```

#### Parameters

rebarSpliceTypeId [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
:   The Rebar Splice Type id.
 Interactions with Rebar Splice Types can be done with the functions in [RebarSpliceTypeUtils](98b9e51e-cd97-954d-4a31-a5189696b27e.htm) .

#### Return Value

Boolean 
Returns true if the stagger length is auto calculated for the specified Rebar Bar Type and Rebar Splice Type, false otherwise. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The rebarSpliceTypeId doesn't represent a valid Rebar Splice Type. It should be an ElementType of BuiltInCategory.OST\_RebarSpliceType category. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks If it is auto calculated, stagger length value is computed based on the formula: stagger length multiplier (found in splice type) \* lap length. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarBarType Class](Rebar-Bar-Type-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
