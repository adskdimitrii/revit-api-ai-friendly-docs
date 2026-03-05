# MEPAnalytical Segment Is Segment Overridable Method

Source: https://www.revitapidocs.com/2026/6aa780fb-000d-13d2-d027-0f8d071daff6.htm

---

| MEPAnalytical Segment Is Segment Overridable Method |
| --- |

Verifies if the segment can be overridden (e.g., the pressure drop of the pump and curve segments are calculated from the network and cannot be overridden). 
**Namespace:** [Autodesk.Revit.DB.Analysis](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public bool IsSegmentOverridable()
```

```
Public Function IsSegmentOverridable As Boolean
```

```
public:
bool IsSegmentOverridable()
```

```
member IsSegmentOverridable : unit -> bool 
```

#### Return Value

Boolean 
True if the segment can be overridden for the loss coefficient or pressure drop, false if the segment cannot be overriden. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[MEPAnalyticalSegment Class](MEPAnalytical-Segment-Class.md) [Autodesk.Revit.DB.Analysis Namespace](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md)
