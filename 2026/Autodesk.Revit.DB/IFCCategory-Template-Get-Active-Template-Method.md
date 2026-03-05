# IFCCategory Template Get Active Template Method

Source: https://www.revitapidocs.com/2026/1e418c35-b6e5-4cbb-5ffc-98ab761edbce.htm

---

| IFCCategory Template Get Active Template Method |
| --- |

Gets the active mapping template element in the document. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static IFCCategoryTemplate GetActiveTemplate(
	Document document
)
```

```
Public Shared Function GetActiveTemplate ( 
	document As Document
) As IFCCategoryTemplate
```

```
public:
static IFCCategoryTemplate^ GetActiveTemplate(
	Document^ document
)
```

```
static member GetActiveTemplate : 
        document : Document -> IFCCategoryTemplate 
```

#### Parameters

document [Document](Document-Class.md)
:   The document to find the active mapping template.

#### Return Value

[IFCCategoryTemplate](IFCCategory-Template-Class.md) 
The active mapping template, or if none. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks New documents have no active mapping template and it implies in\-session template usage. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[IFCCategoryTemplate Class](IFCCategory-Template-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
