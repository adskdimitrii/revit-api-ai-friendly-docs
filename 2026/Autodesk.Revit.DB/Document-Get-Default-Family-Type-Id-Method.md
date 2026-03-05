# Document Get Default Family Type Id Method

Source: https://www.revitapidocs.com/2026/34d20683-dfea-b1f8-14cf-750611b218ed.htm

---

| Document Get Default Family Type Id Method |
| --- |

Gets the default family type id with the given family category id. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public ElementId GetDefaultFamilyTypeId(
	ElementId familyCategoryId
)
```

```
Public Function GetDefaultFamilyTypeId ( 
	familyCategoryId As ElementId
) As ElementId
```

```
public:
ElementId^ GetDefaultFamilyTypeId(
	ElementId^ familyCategoryId
)
```

```
member GetDefaultFamilyTypeId : 
        familyCategoryId : ElementId -> ElementId 
```

#### Parameters

familyCategoryId [ElementId](Element-Id-Class.md)
:   The family category id.

#### Return Value

[ElementId](Element-Id-Class.md) 
The default family type id. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | familyCategoryId is not a built in category or parameter Element ID. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Document Class](Document-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
