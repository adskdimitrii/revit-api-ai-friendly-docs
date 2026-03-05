# IFCParameter Template Is Valid Name Method

Source: https://www.revitapidocs.com/2026/5de6e241-684c-0bf8-1196-3220bba3edd0.htm

---

| IFCParameter Template Is Valid Name Method |
| --- |

Returns result that the proposed name is valid and not exist in the specified document. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static bool IsValidName(
	Document document,
	string name
)
```

```
Public Shared Function IsValidName ( 
	document As Document,
	name As String
) As Boolean
```

```
public:
static bool IsValidName(
	Document^ document, 
	String^ name
)
```

```
static member IsValidName : 
        document : Document * 
        name : string -> bool 
```

#### Parameters

document [Document](Document-Class.md)
:   The document to check

name String
:   The name to check.

#### Return Value

Boolean 
Whether or not the name is valid. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks Name can't contains following characters, such as { } \[ ] \| ; \< \> ? \` \~ \\ : \\r \\n \\f \\t \\v.
 Name can't be blank.
 If true, the name is valid and not exist in specified document.
 If false, the name is not a valid name which means it does not exist in specified document. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[IFCParameterTemplate Class](IFCParameter-Template-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
