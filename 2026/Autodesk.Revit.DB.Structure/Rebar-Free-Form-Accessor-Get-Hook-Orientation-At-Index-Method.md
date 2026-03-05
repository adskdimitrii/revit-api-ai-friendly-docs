# Rebar Free Form Accessor Get Hook Orientation At Index Method

Source: https://www.revitapidocs.com/2026/c2292cbe-0b87-0105-6937-5caaae22955d.htm

---

| Rebar Free Form Accessor Get Hook Orientation At Index Method |
| --- |

**Note: This API is now obsolete.** 

Gets the termination's orientation that is applied to this Rebar at the bar with index barPositionIndex at the specified end.
 The orientation it's the same for both hook and crank. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarFreeFormAccessor.GetTerminationOrientationAtIndex instead.")]
public RebarHookOrientation GetHookOrientationAtIndex(
	int barPositionIndex,
	int end
)
```

```
<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarFreeFormAccessor.GetTerminationOrientationAtIndex instead.")>
Public Function GetHookOrientationAtIndex ( 
	barPositionIndex As Integer,
	end As Integer
) As RebarHookOrientation
```

```
public:
[ObsoleteAttribute(L"This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarFreeFormAccessor.GetTerminationOrientationAtIndex instead.")]
RebarHookOrientation GetHookOrientationAtIndex(
	int barPositionIndex, 
	int end
)
```

```
[<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarFreeFormAccessor.GetTerminationOrientationAtIndex instead.")>]
member GetHookOrientationAtIndex : 
        barPositionIndex : int * 
        end : int -> RebarHookOrientation 
```

#### Parameters

barPositionIndex Int32
:   An index between 0 and (NumberOfBarPositions\-1\).

end Int32
:   0 for the start hook, 1 for the end hook.

#### Return Value

[RebarHookOrientation](Rebar-Hook-Orientation-Enumeration.md) 
Returns the hook orientation at the specified end. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | end must be 0 or 1\.  \-or\-  barPositionIndex is not in the range \[ 0, NumberOfBarPositions\-1 ]. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks If this Rebar has Workshop Instructions set to Straight will return the same value for all barPositionIndex between 0 and (NumberOfBarPositions\-1\). This value will be the same as Rebar.GetHookOrientation(int end). 

If this Rebar has Workshop Instructions set to Bent there are different cases: 

* All bars are matched exactly with a shape. In this case will return the same value for all barPositionIndex between 0 and (NumberOfBarPositions\-1\). This value will be the same as Rebar.GetHookOrientation(int end).
* All bars are matched in reversed order with a shape. In this case will return the same value for all barPositionIndex between 0 and (NumberOfBarPositions\-1\). This value will be the same as Rebar.GetHookOrientation(int end).
* Some bars are matched in reversed order and the others are matched exactly with a shape. In this case for bars that are matched reversed will return the hook orientation at the opposite end. For the others bars will return the same as Rebar.GetHookOrientation(int end).

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarFreeFormAccessor Class](Rebar-Free-Form-Accessor-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
