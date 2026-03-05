# IFCProperty Mapping Info Revit Property Id Property

Source: https://www.revitapidocs.com/2026/c74edf77-98cf-cc32-9347-51ac63ea75b9.htm

---

| IFCProperty Mapping Info Revit Property Id Property |
| --- |

The Revit property id. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public ElementId RevitPropertyId { get; set; }
```

```
Public Property RevitPropertyId As ElementId
	Get
	Set
```

```
public:
property ElementId^ RevitPropertyId {
	ElementId^ get ();
	void set (ElementId^ value);
}
```

```
member RevitPropertyId : ElementId with get, set
```

#### Property Value

[ElementId](Element-Id-Class.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[IFCPropertyMappingInfo Class](IFCProperty-Mapping-Info-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
