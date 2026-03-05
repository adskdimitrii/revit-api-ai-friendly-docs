# Rebar Hook Orientation Enumeration

Source: https://www.revitapidocs.com/2026/e8365754-0811-8d4e-864a-55bf34af3a87.htm

---

| Rebar Hook Orientation Enumeration |
| --- |

**Note: This API is now obsolete.** 

Orientation of a rebar hook relative to the path of the Rebar Shape. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This enumeration is deprecated in Revit 2026 and may be removed in a later version of Revit. You can use RebarTerminationOrientation enumeration instead.")]
public enum RebarHookOrientation
```

```
<ObsoleteAttribute("This enumeration is deprecated in Revit 2026 and may be removed in a later version of Revit. You can use RebarTerminationOrientation enumeration instead.")>
Public Enumeration RebarHookOrientation
```

```
[ObsoleteAttribute(L"This enumeration is deprecated in Revit 2026 and may be removed in a later version of Revit. You can use RebarTerminationOrientation enumeration instead.")]
public enum class RebarHookOrientation
```

```
[<ObsoleteAttribute("This enumeration is deprecated in Revit 2026 and may be removed in a later version of Revit. You can use RebarTerminationOrientation enumeration instead.")>]
type RebarHookOrientation
```
![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Members 

| Member name | Value | Description |
| --- | --- | --- |
| Left | 1 | Hook towards the left of a segment\-based shape (RebarShapeDefinitionBySegments), or to the  interior of an arc\-based shape (RebarShapeDefinitionByArc). |
| Right | \-1 | Hook towards the right of a segment\-based shape (RebarShapeDefinitionBySegments), or to the  exterior of an arc\-based shape (RebarShapeDefinitionByArc). |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
