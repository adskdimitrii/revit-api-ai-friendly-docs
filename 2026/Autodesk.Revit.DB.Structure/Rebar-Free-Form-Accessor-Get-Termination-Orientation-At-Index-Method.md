# Rebar Free Form Accessor Get Termination Orientation At Index Method

Source: https://www.revitapidocs.com/2026/a0787bdd-9f85-ba13-3ef8-8fc1d7344db8.htm

---

| Rebar Free Form Accessor Get Termination Orientation At Index Method |
| --- |

Gets the termination's (e.g. hook, crank ) orientation that is applied to this Rebar at the bar with index barPositionIndex at the specified end. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public RebarTerminationOrientation GetTerminationOrientationAtIndex(
	int barPositionIndex,
	int end
)
```

```
Public Function GetTerminationOrientationAtIndex ( 
	barPositionIndex As Integer,
	end As Integer
) As RebarTerminationOrientation
```

```
public:
RebarTerminationOrientation GetTerminationOrientationAtIndex(
	int barPositionIndex, 
	int end
)
```

```
member GetTerminationOrientationAtIndex : 
        barPositionIndex : int * 
        end : int -> RebarTerminationOrientation 
```

#### Parameters

barPositionIndex Int32
:   An index between 0 and (NumberOfBarPositions\-1\).

end Int32
:   0 for the start termination, 1 for the end termination.

#### Return Value

[RebarTerminationOrientation](Rebar-Termination-Orientation-Enumeration.md) 
Returns the termination (e.g. hook, crank) orientation at the specified end. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | end must be 0 or 1\.  \-or\-  barPositionIndex is not in the range \[ 0, NumberOfBarPositions\-1 ]. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks If this Rebar has Workshop Instructions set to Straight will return the same value for all barPositionIndex between 0 and (NumberOfBarPositions\-1\). This value will be the same as Rebar.GetTerminationOrientation(int end). 

If this Rebar has Workshop Instructions set to Bent there are different cases: 

* All bars are matched exactly with a shape. In this case will return the same value for all barPositionIndex between 0 and (NumberOfBarPositions\-1\). This value will be the same as Rebar.GetTerminationOrientation(int end).
* All bars are matched in reversed order with a shape. In this case will return the same value for all barPositionIndex between 0 and (NumberOfBarPositions\-1\). This value will be the same as Rebar.GetTerminationOrientation(int end).
* Some bars are matched in reversed order and the others are matched exactly with a shape. In this case for bars that are matched reversed will return the termination's (hook, crank) orientation at the opposite end. For the others bars will return the same as Rebar.GetTerminationOrientation(int end).

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarFreeFormAccessor Class](Rebar-Free-Form-Accessor-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
