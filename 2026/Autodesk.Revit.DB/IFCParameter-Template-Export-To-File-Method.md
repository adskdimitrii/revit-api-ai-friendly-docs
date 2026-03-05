# IFCParameter Template Export To File Method

Source: https://www.revitapidocs.com/2026/c329302b-92c6-93ae-b8e4-fcf4b76422be.htm

---

| IFCParameter Template Export To File Method |
| --- |

Export mapping template to a text file. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void ExportToFile(
	string fileName
)
```

```
Public Sub ExportToFile ( 
	fileName As String
)
```

```
public:
void ExportToFile(
	String^ fileName
)
```

```
member ExportToFile : 
        fileName : string -> unit 
```

#### Parameters

fileName String
:   The full text file name.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [FileAccessException](187d56d7-0b37-699f-2abd-6ddebfa93f1e.htm) | Failed to access the text file. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[IFCParameterTemplate Class](IFCParameter-Template-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
