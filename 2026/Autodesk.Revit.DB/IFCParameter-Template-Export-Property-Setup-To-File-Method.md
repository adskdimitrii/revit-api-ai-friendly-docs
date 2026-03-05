# IFCParameter Template Export Property Setup To File Method

Source: https://www.revitapidocs.com/2026/4b193a70-936e-6caa-5317-c41e29ae0f3e.htm

---

| IFCParameter Template Export Property Setup To File Method |
| --- |

Exports mapping information of the provided property setup to a text file. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void ExportPropertySetupToFile(
	PropertySetupType propertySetupType,
	string fileName
)
```

```
Public Sub ExportPropertySetupToFile ( 
	propertySetupType As PropertySetupType,
	fileName As String
)
```

```
public:
void ExportPropertySetupToFile(
	PropertySetupType propertySetupType, 
	String^ fileName
)
```

```
member ExportPropertySetupToFile : 
        propertySetupType : PropertySetupType * 
        fileName : string -> unit 
```

#### Parameters

propertySetupType [PropertySetupType](Property-Setup-Type-Enumeration.md)
:   The property setup type.

fileName String
:   The full text file name.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |
| [FileAccessException](187d56d7-0b37-699f-2abd-6ddebfa93f1e.htm) | Failed to access the text file. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[IFCParameterTemplate Class](IFCParameter-Template-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
