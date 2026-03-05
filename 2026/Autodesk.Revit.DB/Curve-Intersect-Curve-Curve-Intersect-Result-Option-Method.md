# Curve Intersect(Curve, Curve Intersect Result Option) Method

Source: https://www.revitapidocs.com/2026/ed77380e-8b47-bc2c-1651-ebb342310391.htm

---

| Curve Intersect(Curve, Curve Intersect Result Option) Method |
| --- |

Calculates the intersection of this curve with the specified curve. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public CurveIntersectResult Intersect(
	Curve curve,
	CurveIntersectResultOption option
)
```

```
Public Function Intersect ( 
	curve As Curve,
	option As CurveIntersectResultOption
) As CurveIntersectResult
```

```
public:
CurveIntersectResult^ Intersect(
	Curve^ curve, 
	CurveIntersectResultOption option
)
```

```
member Intersect : 
        curve : Curve * 
        option : CurveIntersectResultOption -> CurveIntersectResult 
```

#### Parameters

curve [Curve](Curve-Class.md)
:   The specified curve to intersect with this curve.

option [CurveIntersectResultOption](Curve-Intersect-Result-Option-Enumeration.md)
:   Specifies the amount of information to return in the [CurveIntersectResult](Curve-Intersect-Result-Class.md) .

#### Return Value

[CurveIntersectResult](Curve-Intersect-Result-Class.md) 
The [CurveIntersectResult](Curve-Intersect-Result-Class.md) describing the geometric relationship of the two curves. This will contain at least a SetComparisonResult and, if requested, 
a list of [CurveOverlapPoint](Curve-Overlap-Point-Class.md) s specifying where the two curves overlap or intersect. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | The specified curve is . |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Failed to calculate the intersection. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The [CurveIntersectResultOption](Curve-Intersect-Result-Option-Enumeration.md) passed to this method determines the amount of information that will be calculated and returned: * CurveIntersectResultOption.Simple \- Calculate only the geometric relationship between the two curves, as indicated by a SetComparisonResult value.
* CurveIntersectResultOption.Detailed \- Calculate the geometric relationship between the two curves, along with any points or intervals of overlap. 
This option may result in additional computations being performed compared to CurveIntersectResultOption.Simple.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Curve Class](Curve-Class.md) [Intersect Overload](Curve-Intersect-Method.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
