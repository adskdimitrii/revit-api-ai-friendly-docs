# IFCParameter Template Get Or Create In Session Template Method

Source: https://www.revitapidocs.com/2026/ba19254e-78a9-b66a-e3cd-efe09de2a112.htm

---

| IFCParameter Template Get Or Create In Session Template Method |
| --- |

Gets the in\-session non\-serializable template or create new. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static IFCParameterTemplate GetOrCreateInSessionTemplate(
	Document document
)
```

```
Public Shared Function GetOrCreateInSessionTemplate ( 
	document As Document
) As IFCParameterTemplate
```

```
public:
static IFCParameterTemplate^ GetOrCreateInSessionTemplate(
	Document^ document
)
```

```
static member GetOrCreateInSessionTemplate : 
        document : Document -> IFCParameterTemplate 
```

#### Parameters

document [Document](Document-Class.md)
:   The document where created mapping template is saved.

#### Return Value

[IFCParameterTemplate](IFCParameter-Template-Class.md) 
The mapping template. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[IFCParameterTemplate Class](IFCParameter-Template-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
