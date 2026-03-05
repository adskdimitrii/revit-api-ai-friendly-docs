# Rebar Splice Error Enumeration

Source: https://www.revitapidocs.com/2026/7ca33f19-516d-8e98-0b0e-4b0093a1771b.htm

---

| Rebar Splice Error Enumeration |
| --- |

Class that defines states for splicing a Rebar. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public enum RebarSpliceError
```

```
Public Enumeration RebarSpliceError
```

```
public enum class RebarSpliceError
```

```
type RebarSpliceError
```
![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Members 

| Member name | Value | Description |
| --- | --- | --- |
| InvalidLineOrLinePlaneNormal | 3 | The line length is zero or the line direction is parallel with the line plane normal. |
| InvalidRebar | 2 | Free Form rebars, or Shape Driven rebars that are Multiplanar, or have a shape that whose definition is RebarShapeDefinitionByArc, or rebars that are part of a group can't be spliced. |
| LineDoesNotIntersectRebarBoundingBox | 4 | The line doesn't intersect the rebar bounding box. |
| SpliceGeometryAlmostParallelToBarSegment | 8 | The plane formed by splice geometry is almost parallel to bar segment plane. |
| SpliceGeometryDoesNotIntersectAllTheBarsInTheSet | 7 | A plane obtained from splice geometry doesn't intersect all the bars in the set. |
| SpliceGeometryOnCrank | 9 | If the splice geometry is on a crank, the rebar can't be spliced with it. |
| SpliceGeometryOnHookOrFillet | 5 | If the splice geometry is on a hook or a fillet, the rebar can't be spliced with it. |
| Success | 0 | This will be is there is no error. |
| TooSmallSegments | 6 | One of the resulting segments is too small to apply the lap. |
| Unknown | 1 | There is an unexpected error. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
