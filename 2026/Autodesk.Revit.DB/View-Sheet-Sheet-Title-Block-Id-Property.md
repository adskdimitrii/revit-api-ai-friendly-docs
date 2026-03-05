# View Sheet Sheet Title Block Id Property

Source: https://www.revitapidocs.com/2026/c866285c-67c2-5536-cbf5-169c31247ab8.htm

---

| View Sheet Sheet Title Block Id Property |
| --- |

The Id of the title block this sheet is associated with. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public ElementId SheetTitleBlockId { get; set; }
```

```
Public Property SheetTitleBlockId As ElementId
	Get
	Set
```

```
public:
property ElementId^ SheetTitleBlockId {
	ElementId^ get ();
	void set (ElementId^ value);
}
```

```
member SheetTitleBlockId : ElementId with get, set
```

#### Property Value

[ElementId](Element-Id-Class.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[ViewSheet Class](View-Sheet-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
