# IFCParameter Template Find By Name Method

Source: https://www.revitapidocs.com/2026/6530fe2a-a82c-fb84-bb16-144e99ac1429.htm

---

| IFCParameter Template Find By Name Method |
| --- |

Returns mapping template element by name. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static IFCParameterTemplate FindByName(
	Document document,
	string name
)
```

```
Public Shared Function FindByName ( 
	document As Document,
	name As String
) As IFCParameterTemplate
```

```
public:
static IFCParameterTemplate^ FindByName(
	Document^ document, 
	String^ name
)
```

```
static member FindByName : 
        document : Document * 
        name : string -> IFCParameterTemplate 
```

#### Parameters

document [Document](Document-Class.md)
:   The document to find the mapping template with the specified name.

name String
:   Name of the mapping template to find.

#### Return Value

[IFCParameterTemplate](IFCParameter-Template-Class.md) 
The mapping template element, or if not found. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[IFCParameterTemplate Class](IFCParameter-Template-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
