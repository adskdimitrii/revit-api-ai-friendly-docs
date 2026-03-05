# Curve Intersect(Curve) Method

Source: https://www.revitapidocs.com/2026/90e86110-9bce-6e43-c18a-4d67380008bb.htm

---

| Curve Intersect(Curve) Method |
| --- |

**Note: This API is now obsolete.** 

Calculates the intersection of this curve with the specified curve. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Use the new Curve.Intersect method with CurveIntersectResultOption.Simple. Note also that the updated method has improved handling of certain edge cases.")]
public SetComparisonResult Intersect(
	Curve curve
)
```

```
<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Use the new Curve.Intersect method with CurveIntersectResultOption.Simple. Note also that the updated method has improved handling of certain edge cases.")>
Public Function Intersect ( 
	curve As Curve
) As SetComparisonResult
```

```
public:
[ObsoleteAttribute(L"This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Use the new Curve.Intersect method with CurveIntersectResultOption.Simple. Note also that the updated method has improved handling of certain edge cases.")]
SetComparisonResult Intersect(
	Curve^ curve
)
```

```
[<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Use the new Curve.Intersect method with CurveIntersectResultOption.Simple. Note also that the updated method has improved handling of certain edge cases.")>]
member Intersect : 
        curve : Curve -> SetComparisonResult 
```

#### Parameters

curve [Curve](Curve-Class.md)
:   The specified curve to intersect with this curve.

#### Return Value

[SetComparisonResult](Set-Comparison-Result-Enumeration.md) 
* SetComparisonResult.Overlap \- One or more intersections were encountered.
* SetComparisonResult.Subset \- The inputs are parallel lines with only one common intersection point, or 
the curve used to invoke the intersection check is a line entirely within the unbound line passed as argument curve.
* SetComparisonResult.Superset \- The input curve is entirely within the unbound line used to invoke the intersection check.
* SetComparisonResult.Disjoint \- There is no intersection found between the two curves.
* SetComparisonResult.Equal \- The two curves are identical.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | The specified curve is . |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Failed to calculate the intersection. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Curve Class](Curve-Class.md) [Intersect Overload](Curve-Intersect-Method.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
