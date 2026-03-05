# IFCCategory Template List Names Method

Source: https://www.revitapidocs.com/2026/0da28c8e-08d0-ad93-1f53-65b87008af93.htm

---

| IFCCategory Template List Names Method |
| --- |

Returns a list of names of IFC export mapping templates. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static IList<string> ListNames(
	Document document
)
```

```
Public Shared Function ListNames ( 
	document As Document
) As IList(Of String)
```

```
public:
static IList<String^>^ ListNames(
	Document^ document
)
```

```
static member ListNames : 
        document : Document -> IList<string> 
```

#### Parameters

document [Document](Document-Class.md)
:   A Revit document to retrieve names from.

#### Return Value

IList String 
An array of strings representing names of predefined setups. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[IFCCategoryTemplate Class](IFCCategory-Template-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
