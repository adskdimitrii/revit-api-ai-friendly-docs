# Curve Intersect(Curve, Intersection Result Array ) Method

Source: https://www.revitapidocs.com/2026/51961478-fb36-e00b-2d1b-7db27b0a09e6.htm

---

| Curve Intersect(Curve, Intersection Result Array ) Method |
| --- |

**Note: This API is now obsolete.** 

Calculates the intersection of this curve with the specified curve and returns the intersection results. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Use the new Curve.Intersect method with CurveIntersectResultOption.Detailed. Note also that the updated method has improved handling of certain edge cases.")]
public SetComparisonResult Intersect(
	Curve curve,
	out IntersectionResultArray resultArray
)
```

```
<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Use the new Curve.Intersect method with CurveIntersectResultOption.Detailed. Note also that the updated method has improved handling of certain edge cases.")>
Public Function Intersect ( 
	curve As Curve,
	<OutAttribute> ByRef resultArray As IntersectionResultArray
) As SetComparisonResult
```

```
public:
[ObsoleteAttribute(L"This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Use the new Curve.Intersect method with CurveIntersectResultOption.Detailed. Note also that the updated method has improved handling of certain edge cases.")]
SetComparisonResult Intersect(
	Curve^ curve, 
	[OutAttribute] IntersectionResultArray^% resultArray
)
```

```
[<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Use the new Curve.Intersect method with CurveIntersectResultOption.Detailed. Note also that the updated method has improved handling of certain edge cases.")>]
member Intersect : 
        curve : Curve * 
        resultArray : IntersectionResultArray byref -> SetComparisonResult 
```

#### Parameters

curve [Curve](Curve-Class.md)
:   The specified curve to intersect with this curve.

resultArray [IntersectionResultArray](4742c1e8-0566-73c6-de42-04d98a503dfc.htm)
:   Provides more information about the intersection.

#### Return Value

[SetComparisonResult](Set-Comparison-Result-Enumeration.md) 
* SetComparisonResult.Overlap \- One or more intersections were encountered. The output argument has the details.
* SetComparisonResult.Subset \- The inputs are parallel lines with only one common intersection point, or 
the curve used to invoke the intersection check is a line entirely within the unbound line passed as argument curve.
If the former, the output argument has the details of the intersection point.
* SetComparisonResult.Superset \- The input curve is entirely within the unbound line used to invoke the intersection check.
* SetComparisonResult.Disjoint \- There is no intersection found between the two curves.
* SetComparisonResult.Equal \- The two curves are identical.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the specified curve is . |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when failed to calculate the intersection. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The array of the intersection results contains one entry for each point where curves intersect.
The following is the meaning of IntersectionResult members: * XYZPoint is the evaluated intersection point
* UVPoint.U is the unnormalized parameter on this curve (use ComputeNormalizedParameter to compute the normalized value).
* UVPoint.V is the unnormalized parameter on the specified curve (use ComputeNormalizedParameter to compute the normalized value).

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Curve Class](Curve-Class.md) [Intersect Overload](Curve-Intersect-Method.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
