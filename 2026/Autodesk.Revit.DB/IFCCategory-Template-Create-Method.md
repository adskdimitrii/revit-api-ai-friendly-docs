# IFCCategory Template Create Method

Source: https://www.revitapidocs.com/2026/ba0e5b7b-0cd9-5e96-3d67-65251bfa9071.htm

---

| IFCCategory Template Create Method |
| --- |

Create a IFC category mapping template with default values. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static IFCCategoryTemplate Create(
	Document document,
	string name
)
```

```
Public Shared Function Create ( 
	document As Document,
	name As String
) As IFCCategoryTemplate
```

```
public:
static IFCCategoryTemplate^ Create(
	Document^ document, 
	String^ name
)
```

```
static member Create : 
        document : Document * 
        name : string -> IFCCategoryTemplate 
```

#### Parameters

document [Document](Document-Class.md)
:   Document where created mapping template is saved.

name String
:   The name specified to this mapping template.

#### Return Value

[IFCCategoryTemplate](IFCCategory-Template-Class.md) 
The new mapping template instance. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The name already exists. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[IFCCategoryTemplate Class](IFCCategory-Template-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
