# IFCCategory Template Get Mapping Info By Id Method

Source: https://www.revitapidocs.com/2026/9304b014-4d75-7ace-6a31-bea372c9f5d7.htm

---

| IFCCategory Template Get Mapping Info By Id Method |
| --- |

Gets a copy of IFC mapping info by category id. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public ExportIFCCategoryInfo GetMappingInfoById(
	Document document,
	ElementId categoryId,
	CustomSubCategoryId customSubCategoryId
)
```

```
Public Function GetMappingInfoById ( 
	document As Document,
	categoryId As ElementId,
	customSubCategoryId As CustomSubCategoryId
) As ExportIFCCategoryInfo
```

```
public:
ExportIFCCategoryInfo^ GetMappingInfoById(
	Document^ document, 
	ElementId^ categoryId, 
	CustomSubCategoryId customSubCategoryId
)
```

```
member GetMappingInfoById : 
        document : Document * 
        categoryId : ElementId * 
        customSubCategoryId : CustomSubCategoryId -> ExportIFCCategoryInfo 
```

#### Parameters

document [Document](Document-Class.md)
:   A Revit document.

categoryId [ElementId](Element-Id-Class.md)
:   The category id.

customSubCategoryId [CustomSubCategoryId](b92e5bf8-0a3d-b22f-bd2a-a75a21312c73.htm)
:   The custom subcategory id.

#### Return Value

[ExportIFCCategoryInfo](Export-IFCCategory-Info-Class.md) 
Return the info for this category. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[IFCCategoryTemplate Class](IFCCategory-Template-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
