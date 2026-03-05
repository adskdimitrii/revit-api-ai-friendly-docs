# IFCParameter Template Copy Template Method

Source: https://www.revitapidocs.com/2026/aff8f057-a229-be04-5a91-3b5873e4d458.htm

---

| IFCParameter Template Copy Template Method |
| --- |

Create copy of mapping template with new name. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public IFCParameterTemplate CopyTemplate(
	Document document,
	string copyTemplateName
)
```

```
Public Function CopyTemplate ( 
	document As Document,
	copyTemplateName As String
) As IFCParameterTemplate
```

```
public:
IFCParameterTemplate^ CopyTemplate(
	Document^ document, 
	String^ copyTemplateName
)
```

```
member CopyTemplate : 
        document : Document * 
        copyTemplateName : string -> IFCParameterTemplate 
```

#### Parameters

document [Document](Document-Class.md)
:   The Revit document to save the copied template.

copyTemplateName String
:   The name for copied template name.

#### Return Value

[IFCParameterTemplate](IFCParameter-Template-Class.md) 
The copied mapping template element. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The name already exists. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Failed to create IFCParameterTemplate element. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The copied template is saved in the document passed as parameter.
 Passing the same document as the source template's document will create a new template in the same document.
 The active template of the document remains unchanged. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[IFCParameterTemplate Class](IFCParameter-Template-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
