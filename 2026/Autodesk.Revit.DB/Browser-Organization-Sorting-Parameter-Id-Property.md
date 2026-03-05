# Browser Organization Sorting Parameter Id Property

Source: https://www.revitapidocs.com/2026/f709abcf-baa3-085c-4fdd-8ab09ee976b8.htm

---

| Browser Organization Sorting Parameter Id Property |
| --- |

**Note: This API is now obsolete.** 

The Id of the parameter used to determine the sorting order of items in the browser. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This property is deprecated in Revit 2026 and may be removed in a later version of Revit. We suggest you use the 'getSortingParameterIdPath' method instead.")]
public ElementId SortingParameterId { get; }
```

```
<ObsoleteAttribute("This property is deprecated in Revit 2026 and may be removed in a later version of Revit. We suggest you use the 'getSortingParameterIdPath' method instead.")>
Public ReadOnly Property SortingParameterId As ElementId
	Get
```

```
public:
[ObsoleteAttribute(L"This property is deprecated in Revit 2026 and may be removed in a later version of Revit. We suggest you use the 'getSortingParameterIdPath' method instead.")]
property ElementId^ SortingParameterId {
	ElementId^ get ();
}
```

```
[<ObsoleteAttribute("This property is deprecated in Revit 2026 and may be removed in a later version of Revit. We suggest you use the 'getSortingParameterIdPath' method instead.")>]
member SortingParameterId : ElementId with get
```

#### Property Value

[ElementId](Element-Id-Class.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[BrowserOrganization Class](Browser-Organization-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
