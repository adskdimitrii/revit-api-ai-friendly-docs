# IFCCategory Template Get Or Create In Session Template Method

Source: https://www.revitapidocs.com/2026/62b8adbe-dcd0-aac0-2d0e-a44e10af0013.htm

---

| IFCCategory Template Get Or Create In Session Template Method |
| --- |

Gets the in\-session non\-serializable template or create new. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static IFCCategoryTemplate GetOrCreateInSessionTemplate(
	Document document
)
```

```
Public Shared Function GetOrCreateInSessionTemplate ( 
	document As Document
) As IFCCategoryTemplate
```

```
public:
static IFCCategoryTemplate^ GetOrCreateInSessionTemplate(
	Document^ document
)
```

```
static member GetOrCreateInSessionTemplate : 
        document : Document -> IFCCategoryTemplate 
```

#### Parameters

document [Document](Document-Class.md)
:   The document to find the in\-session mapping template.

#### Return Value

[IFCCategoryTemplate](IFCCategory-Template-Class.md) 
The mapping template, or if failed to create. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[IFCCategoryTemplate Class](IFCCategory-Template-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
