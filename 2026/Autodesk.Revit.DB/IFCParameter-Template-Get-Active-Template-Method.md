# IFCParameter Template Get Active Template Method

Source: https://www.revitapidocs.com/2026/132c18c5-70b3-41f6-b966-47aed0879ddf.htm

---

| IFCParameter Template Get Active Template Method |
| --- |

Gets the active mapping template element in the document. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static IFCParameterTemplate GetActiveTemplate(
	Document document
)
```

```
Public Shared Function GetActiveTemplate ( 
	document As Document
) As IFCParameterTemplate
```

```
public:
static IFCParameterTemplate^ GetActiveTemplate(
	Document^ document
)
```

```
static member GetActiveTemplate : 
        document : Document -> IFCParameterTemplate 
```

#### Parameters

document [Document](Document-Class.md)
:   The document to find the active mapping template.

#### Return Value

[IFCParameterTemplate](IFCParameter-Template-Class.md) 
The active mapping template, or if none. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks New documents have no active mapping template and it implies in\-session template usage. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[IFCParameterTemplate Class](IFCParameter-Template-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
