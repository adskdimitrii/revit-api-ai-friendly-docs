# IFCParameter Template Create Method

Source: https://www.revitapidocs.com/2026/8812ffd9-ff0a-8a1c-a9f3-44757e967df9.htm

---

| IFCParameter Template Create Method |
| --- |

Create an IFC parameter mapping template with default values. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static IFCParameterTemplate Create(
	Document document,
	string name
)
```

```
Public Shared Function Create ( 
	document As Document,
	name As String
) As IFCParameterTemplate
```

```
public:
static IFCParameterTemplate^ Create(
	Document^ document, 
	String^ name
)
```

```
static member Create : 
        document : Document * 
        name : string -> IFCParameterTemplate 
```

#### Parameters

document [Document](Document-Class.md)
:   The document where created mapping template is saved.

name String
:   The name specified to this mapping template.

#### Return Value

[IFCParameterTemplate](IFCParameter-Template-Class.md) 
The new mapping template instance. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The name already exists. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[IFCParameterTemplate Class](IFCParameter-Template-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
