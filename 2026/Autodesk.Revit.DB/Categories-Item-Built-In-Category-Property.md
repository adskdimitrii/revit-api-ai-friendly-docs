# Categories Item(Built In Category) Property

Source: https://www.revitapidocs.com/2026/562ddcba-8f15-7421-e7a5-6968ccef7b10.htm

---

| Categories Item(Built In Category) Property |
| --- |

Retrieves a category object corresponding to a BuiltInCategory id. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public virtual Category this[
	BuiltInCategory categoryId
] { get; }
```

```
Public Overridable ReadOnly Property Item ( 
	categoryId As BuiltInCategory
) As Category
	Get
```

```
public:
virtual property Category^ Item[BuiltInCategory categoryId] {
	Category^ get (BuiltInCategory categoryId);
}
```

```
abstract Item : Category with get
override Item : Category with get
```

#### Parameters

categoryId [BuiltInCategory](Built-In-Category-Enumeration.md)

#### Property Value

[Category](d390ecf6-e5db-d7c1-d7f2-766c0686e975.htm) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks Unlike the method that obtains categories by name, this routine will obtain
the handle even of built\-in subcategories.
Since 2016 it is advised to use either Category.​​​GetCategory(​Document, ​BuiltIn​Category)
or Category.​​​GetCategory(​Document,​ ElementId)​ from [Category](d390ecf6-e5db-d7c1-d7f2-766c0686e975.htm) class. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Categories Class](6708af38-6a62-ead0-88ff-c68bedd88ffe.htm) [Item Overload](c87c1b7c-55e8-0900-ee0a-f7e2fee0cd73.htm) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
