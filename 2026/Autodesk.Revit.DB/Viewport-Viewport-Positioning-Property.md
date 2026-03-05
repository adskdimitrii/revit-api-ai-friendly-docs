# Viewport Viewport Positioning Property

Source: https://www.revitapidocs.com/2026/f82b1639-99e0-6951-28d2-ece6c5b6bc25.htm

---

| Viewport Viewport Positioning Property |
| --- |

**Note: This API is now obsolete.** 

Specifies the method the viewport will be positioned on the sheet when swapped to another view. Default is set to ViewportPositioning::ViewportCenter. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This property is deprecated in Revit 2026 and may be removed in a future version of Revit. Please use ViewAnchor instead.")]
public ViewportPositioning ViewportPositioning { get; set; }
```

```
<ObsoleteAttribute("This property is deprecated in Revit 2026 and may be removed in a future version of Revit. Please use ViewAnchor instead.")>
Public Property ViewportPositioning As ViewportPositioning
	Get
	Set
```

```
public:
[ObsoleteAttribute(L"This property is deprecated in Revit 2026 and may be removed in a future version of Revit. Please use ViewAnchor instead.")]
property ViewportPositioning ViewportPositioning {
	ViewportPositioning get ();
	void set (ViewportPositioning value);
}
```

```
[<ObsoleteAttribute("This property is deprecated in Revit 2026 and may be removed in a future version of Revit. Please use ViewAnchor instead.")>]
member ViewportPositioning : ViewportPositioning with get, set
```

#### Property Value

[ViewportPositioning](Viewport-Positioning-Enumeration.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Viewport Class](Viewport-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
