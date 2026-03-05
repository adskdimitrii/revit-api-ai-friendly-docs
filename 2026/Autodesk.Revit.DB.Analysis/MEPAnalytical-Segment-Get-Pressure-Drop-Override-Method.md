# MEPAnalytical Segment Get Pressure Drop Override Method

Source: https://www.revitapidocs.com/2026/4cebbf48-584d-aeb2-167f-88e31afca0d9.htm

---

| MEPAnalytical Segment Get Pressure Drop Override Method |
| --- |

Gets the overidden value of pressuer drop, in kg/(ft\*s^2\). 
**Namespace:** [Autodesk.Revit.DB.Analysis](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public double GetPressureDropOverride()
```

```
Public Function GetPressureDropOverride As Double
```

```
public:
double GetPressureDropOverride()
```

```
member GetPressureDropOverride : unit -> float 
```

#### Return Value

Double 
The overridden value, or 0\.0 if the pressure drop is not overridden. Note that the value can be negative to indicate the pressure gain at the flow direction. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[MEPAnalyticalSegment Class](MEPAnalytical-Segment-Class.md) [Autodesk.Revit.DB.Analysis Namespace](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md)
