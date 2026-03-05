# IFCParameter Template Constructor

Source: https://www.revitapidocs.com/2026/abc5725d-1ce6-ad2c-83f6-79eb31666dc1.htm

---

| IFCParameter Template Constructor |
| --- |

Custom constructor for this element. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public IFCParameterTemplate(
	Document document
)
```

```
Public Sub New ( 
	document As Document
)
```

```
public:
IFCParameterTemplate(
	Document^ document
)
```

```
new : 
        document : Document -> IFCParameterTemplate
```

#### Parameters

document [Document](Document-Class.md)
:   The document where created template is saved.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[IFCParameterTemplate Class](IFCParameter-Template-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
