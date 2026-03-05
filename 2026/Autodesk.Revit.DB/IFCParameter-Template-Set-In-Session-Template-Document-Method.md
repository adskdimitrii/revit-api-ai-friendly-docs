# IFCParameter Template Set In Session Template Document Method

Source: https://www.revitapidocs.com/2026/6792865b-e40c-044c-164b-de5f3c1088b3.htm

---

| IFCParameter Template Set In Session Template Document Method |
| --- |

Set document for in\-session template. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetInSessionTemplateDocument(
	Document document
)
```

```
Public Sub SetInSessionTemplateDocument ( 
	document As Document
)
```

```
public:
void SetInSessionTemplateDocument(
	Document^ document
)
```

```
member SetInSessionTemplateDocument : 
        document : Document -> unit 
```

#### Parameters

document [Document](Document-Class.md)
:   The Revit document.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The template is not an is\-session. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The document is used for non built\-in parameters mapping. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[IFCParameterTemplate Class](IFCParameter-Template-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
