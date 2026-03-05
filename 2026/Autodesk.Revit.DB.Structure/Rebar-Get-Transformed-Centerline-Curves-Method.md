# Rebar Get Transformed Centerline Curves Method

Source: https://www.revitapidocs.com/2026/650b9879-3378-77f8-65f0-efeb05daa399.htm

---

| Rebar Get Transformed Centerline Curves Method |
| --- |

A chain of curves representing the centerline of the rebar. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public IList<Curve> GetTransformedCenterlineCurves(
	bool adjustForSelfIntersection,
	bool suppressHooksAndCranks,
	bool suppressBendRadius,
	MultiplanarOption multiplanarOption,
	int barPositionIndex
)
```

```
Public Function GetTransformedCenterlineCurves ( 
	adjustForSelfIntersection As Boolean,
	suppressHooksAndCranks As Boolean,
	suppressBendRadius As Boolean,
	multiplanarOption As MultiplanarOption,
	barPositionIndex As Integer
) As IList(Of Curve)
```

```
public:
IList<Curve^>^ GetTransformedCenterlineCurves(
	bool adjustForSelfIntersection, 
	bool suppressHooksAndCranks, 
	bool suppressBendRadius, 
	MultiplanarOption multiplanarOption, 
	int barPositionIndex
)
```

```
member GetTransformedCenterlineCurves : 
        adjustForSelfIntersection : bool * 
        suppressHooksAndCranks : bool * 
        suppressBendRadius : bool * 
        multiplanarOption : MultiplanarOption * 
        barPositionIndex : int -> IList<Curve> 
```

#### Parameters

adjustForSelfIntersection Boolean
:   If the curves overlap, as in a planar stirrup, this parameter controls
 whether they should be adjusted to avoid intersection (as in fine views),
 or kept in a single plane for simplicity (as in coarse views).

suppressHooksAndCranks Boolean
:   Identifies if the chain will include hooks and the crank curves.

suppressBendRadius Boolean
:   Identifies if the connected chain will include unfilleted curves.

multiplanarOption [MultiplanarOption](37cc5a15-0771-41dd-4456-6820c7cef725.htm)
:   If the Rebar is a multi\-planar shape, this parameter controls whether to generate only
 the curves in the primary plane (IncludeOnlyPlanarCurves), or to generate all curves,
 (IncludeAllMultiplanarCurves) including the out\-of\-plane connector segments as well as
 multi\-planar copies of the primary plane curves.
 This argument is ignored for planar shapes.

barPositionIndex Int32
:   The bar index.

#### Return Value

IList [Curve](../Autodesk.Revit.DB/Curve-Class.md) 
The centerline curves or empty array if the curves cannot be computed because
 the parameters values are inconsistent
 with the constraints of the RebarShape definition. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | barPositionIndex should be in range \[ 0, NumberOfBarPositions\-1 ] and the bar at barPositionIndex should be included.  \-or\-  A value passed for an enumeration argument is not a member of that enumeration |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks This method will return the centerline curves for bar at barPositionIndex even if this bar isn't included.
 The curves are in the final position. The BarPositionTransform (representing the relative position of any individual bar in the set \- a translation along the distribution path)
 and MovedBarTransform (representing the movement of the bar relative to its default position along the distribution path) will be applied to the returned curves. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Rebar Class](Rebar-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
