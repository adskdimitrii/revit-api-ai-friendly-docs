# IFCParameter Template Import From File Method

Source: https://www.revitapidocs.com/2026/04832b89-171a-3b4a-8d41-070365cdf090.htm

---

| IFCParameter Template Import From File Method |
| --- |

Import mapping template from a text file. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static IFCParameterTemplate ImportFromFile(
	Document document,
	string fileName,
	string templateName
)
```

```
Public Shared Function ImportFromFile ( 
	document As Document,
	fileName As String,
	templateName As String
) As IFCParameterTemplate
```

```
public:
static IFCParameterTemplate^ ImportFromFile(
	Document^ document, 
	String^ fileName, 
	String^ templateName
)
```

```
static member ImportFromFile : 
        document : Document * 
        fileName : string * 
        templateName : string -> IFCParameterTemplate 
```

#### Parameters

document [Document](Document-Class.md)
:   The Revit document.

fileName String
:   The full text file name.

templateName String
:   The mapping template name.

#### Return Value

[IFCParameterTemplate](IFCParameter-Template-Class.md) 
The mapping template element. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The name already exists. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [FileAccessException](187d56d7-0b37-699f-2abd-6ddebfa93f1e.htm) | Failed to access the text file. |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Failed to create IFCParameterTemplate. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The imported template is saved in the document passed as parameter.
 The active template of the document remains unchanged. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[IFCParameterTemplate Class](IFCParameter-Template-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
