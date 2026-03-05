# Curve Overlap Point Type Enumeration

Source: https://www.revitapidocs.com/2026/cc6789d6-27a0-242a-3639-376183e7d5b7.htm

---

| Curve Overlap Point Type Enumeration |
| --- |

An enumeration characterizing a point shared by two curves. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public enum CurveOverlapPointType
```

```
Public Enumeration CurveOverlapPointType
```

```
public enum class CurveOverlapPointType
```

```
type CurveOverlapPointType
```
![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Members 

| Member name | Value | Description |
| --- | --- | --- |
| Intersection | 1 | The point marks a transverse intersection of the two curves. |
| IntervalEnd | 3 | The point marks the end of an interval over which the two curves overlap. |
| IntervalStart | 2 | The point marks the beginning of an interval over which the two curves overlap. |
| Uninitialized | 0 | The value is uninitialized. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
