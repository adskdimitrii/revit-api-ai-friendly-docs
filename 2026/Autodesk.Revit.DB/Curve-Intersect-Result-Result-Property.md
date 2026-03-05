# Curve Intersect Result Result Property

Source: https://www.revitapidocs.com/2026/d2cb3dc8-7648-f8ac-627e-4e16d1f4d4bf.htm

---

| Curve Intersect Result Result Property |
| --- |

The classification of intersection or overlap between the two curves. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public SetComparisonResult Result { get; }
```

```
Public ReadOnly Property Result As SetComparisonResult
	Get
```

```
public:
property SetComparisonResult Result {
	SetComparisonResult get ();
}
```

```
member Result : SetComparisonResult with get
```

#### Property Value

[SetComparisonResult](Set-Comparison-Result-Enumeration.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks SetComparisonResult.Overlap \- One or more intersections or overlapping intervals were encountered. 

SetComparisonResult.Subset \- The curve used to invoke the intersection check is a bound curve whose bounded interval is entirely within the curve passed as an argument. 

SetComparisonResult.Superset \- The bounded input curve is entirely within the curve used to invoke the intersection check. 

SetComparisonResult.Disjoint \- There is no intersection or overlap found between the two curves. 

SetComparisonResult.Equal \- The two curves are identical. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[CurveIntersectResult Class](Curve-Intersect-Result-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
