# Curve Intersect Result Get Overlaps Method

Source: https://www.revitapidocs.com/2026/b13ac7b5-f11c-a701-df35-05e91357cc18.htm

---

| Curve Intersect Result Get Overlaps Method |
| --- |

Gets information about the points shared between the two curves. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public IList<CurveOverlapPoint> GetOverlaps()
```

```
Public Function GetOverlaps As IList(Of CurveOverlapPoint)
```

```
public:
IList<CurveOverlapPoint^>^ GetOverlaps()
```

```
member GetOverlaps : unit -> IList<CurveOverlapPoint> 
```

#### Return Value

IList [CurveOverlapPoint](Curve-Overlap-Point-Class.md) 
The list of CurveOverLapPoints corresponding to points of intersection and/or intervals of overlap for the two curves. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This CurveIntersectResult only contains simple output. Use CurveIntersectResultOption::Detailed to compute detailed output. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks A CurveOverlapPoint whose type is CurveOverlapPointType.Intersection indicates an individual
 point of transverse intersection. An interval of curve overlap is indicated by two consecutive
 points \-\- the start point of the interval (having Type CurveOverlapPointType.IntervalStart), immediately
 followed by the end point of the interval (having Type CurveOverlapPointType.IntervalEnd). 

An overlap interval may be degenerate, in which case it indicates that the two curves are arranged
 end\-to\-end with shared end points. The Overlaps of a CurveIntersectResult may contain a combination
 of one or more intersection points and/or overlap intervals. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[CurveIntersectResult Class](Curve-Intersect-Result-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
