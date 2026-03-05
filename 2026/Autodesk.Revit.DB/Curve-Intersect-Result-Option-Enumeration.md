# Curve Intersect Result Option Enumeration

Source: https://www.revitapidocs.com/2026/31d5fc16-a446-f1df-81ec-bbf142d809e5.htm

---

| Curve Intersect Result Option Enumeration |
| --- |

Specifies how much information will be computed and returned when calculating intersection of Curves. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public enum CurveIntersectResultOption
```

```
Public Enumeration CurveIntersectResultOption
```

```
public enum class CurveIntersectResultOption
```

```
type CurveIntersectResultOption
```
![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Members 

| Member name | Value | Description |
| --- | --- | --- |
| Detailed | 1 | Return overlap points and intervals, in addition to the intersection's classification.  Note: selecting this option may cause additional calculations to be performed when determining the curve intersection. |
| Simple | 0 | Only return the SetComparisonResult classifying the type of intersection (or lack thereof). |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
