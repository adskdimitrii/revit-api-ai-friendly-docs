# IFCParameter Template Import Property Setup From File Method

Source: https://www.revitapidocs.com/2026/b7fa7de9-9c18-252e-046c-ab1e3c39edda.htm

---

| IFCParameter Template Import Property Setup From File Method |
| --- |

Imports mapping information from a text file. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void ImportPropertySetupFromFile(
	string fileName
)
```

```
Public Sub ImportPropertySetupFromFile ( 
	fileName As String
)
```

```
public:
void ImportPropertySetupFromFile(
	String^ fileName
)
```

```
member ImportPropertySetupFromFile : 
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
