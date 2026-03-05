# Rebar Free Form Accessor Get Crank Type Id At Index Method

Source: https://www.revitapidocs.com/2026/73de7bb6-46fc-bfae-60c0-fdce7ed6c31d.htm

---

| Rebar Free Form Accessor Get Crank Type Id At Index Method |
| --- |

Gets the id of the Rebar Crank Type that is applied to this Rebar at the bar with index barPositionIndex at the specified end. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public ElementId GetCrankTypeIdAtIndex(
	int barPositionIndex,
	int end
)
```

```
Public Function GetCrankTypeIdAtIndex ( 
	barPositionIndex As Integer,
	end As Integer
) As ElementId
```

```
public:
ElementId^ GetCrankTypeIdAtIndex(
	int barPositionIndex, 
	int end
)
```

```
member GetCrankTypeIdAtIndex : 
        barPositionIndex : int * 
        end : int -> ElementId 
```

#### Parameters

barPositionIndex Int32
:   An index between 0 and (NumberOfBarPositions\-1\).

end Int32
:   0 for the start hook, 1 for the end crank.

#### Return Value

[ElementId](../Autodesk.Revit.DB/Element-Id-Class.md) 
The id of a Rebar Crank Type, or invalidElementId if the rebar has no crank at the specified end. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | end must be 0 or 1\.  \-or\-  barPositionIndex is not in the range \[ 0, NumberOfBarPositions\-1 ]. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks If this Rebar has Workshop Instructions set to Straight will return the same value for all barPositionIndex between 0 and (NumberOfBarPositions\-1\). This value will be the same as Rebar.GetCrankTypeId(int end). 

If this Rebar has Workshop Instructions set to Bent there are different cases: 

* All bars are matched exactly with a shape. In this case will return the same value for all barPositionIndex between 0 and (NumberOfBarPositions\-1\). This value will be the same as Rebar.GetCrankTypeId(int end).
* All bars are matched in reversed order with a shape. In this case will return the same value for all barPositionIndex between 0 and (NumberOfBarPositions\-1\). This value will be the same as Rebar.GetCrankTypeId(int end).
* Some bars are matched in reversed order and the others are matched exactly with a shape. In this case for bars that are matched reversed will return the id of the Rebar Crank Type at the opposite end. For the others bars will return the same as Rebar.GetCrankTypeId(int end).

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarFreeFormAccessor Class](Rebar-Free-Form-Accessor-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
