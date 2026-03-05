# Viewport Positioning Enumeration

Source: https://www.revitapidocs.com/2026/ef1bc472-5074-ae92-0d7e-37367c03546b.htm

---

| Viewport Positioning Enumeration |
| --- |

**Note: This API is now obsolete.** 

An enumerated type listing of viewport positioning options on the sheet when swapped to another view. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This property is deprecated in Revit 2026 and may be removed in a future version of Revit. Please use ViewAnchor instead.")]
public enum ViewportPositioning
```

```
<ObsoleteAttribute("This property is deprecated in Revit 2026 and may be removed in a future version of Revit. Please use ViewAnchor instead.")>
Public Enumeration ViewportPositioning
```

```
[ObsoleteAttribute(L"This property is deprecated in Revit 2026 and may be removed in a future version of Revit. Please use ViewAnchor instead.")]
public enum class ViewportPositioning
```

```
[<ObsoleteAttribute("This property is deprecated in Revit 2026 and may be removed in a future version of Revit. Please use ViewAnchor instead.")>]
type ViewportPositioning
```
![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Members 

| Member name | Value | Description |
| --- | --- | --- |
| ViewOrigin | 1 | When swapping to another view, the viewport location will be based on the view origin. |
| ViewportCenter | 0 | When swapping to another view, the center of the viewport will be maintained. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
