# IFCParameter Template List Names Method

Source: https://www.revitapidocs.com/2026/0fd791f7-994a-1dfb-659f-5e63de2fcee0.htm

---

| IFCParameter Template List Names Method |
| --- |

Returns a list of names of IFC export parameter mapping templates. 
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
:   The Revit document to retrieve names from.

#### Return Value

IList String 
The array of strings representing names of predefined setups. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[IFCParameterTemplate Class](IFCParameter-Template-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
