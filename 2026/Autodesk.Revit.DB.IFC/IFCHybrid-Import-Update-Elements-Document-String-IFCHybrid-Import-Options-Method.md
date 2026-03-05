# IFCHybrid Import Update Elements(Document, String, IFCHybrid Import Options) Method

Source: https://www.revitapidocs.com/2026/be5a0dc9-8c39-fdda-6555-b08ddf4864e1.htm

---

| IFCHybrid Import Update Elements(Document, String, IFCHybrid Import Options) Method |
| --- |

Updates IFC Elements using AnyCAD. 
**Namespace:** [Autodesk.Revit.DB.IFC](../ungrouped/Autodesk.-Revit.-DB.-IFC-Namespace.md) 
**Assembly:** RevitAPIIFC (in RevitAPIIFC.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public IList<ElementId> UpdateElements(
	Document doc,
	string file,
	IFCHybridImportOptions options
)
```

```
Public Function UpdateElements ( 
	doc As Document,
	file As String,
	options As IFCHybridImportOptions
) As IList(Of ElementId)
```

```
public:
IList<ElementId^>^ UpdateElements(
	Document^ doc, 
	String^ file, 
	IFCHybridImportOptions^ options
)
```

```
member UpdateElements : 
        doc : Document * 
        file : string * 
        options : IFCHybridImportOptions -> IList<ElementId> 
```

#### Parameters

doc [Document](../Autodesk.Revit.DB/Document-Class.md)
:   Document to receive elements from the IFC file update.

file String
:   Full path of the file to import.

options [IFCHybridImportOptions](IFCHybrid-Import-Options-Class.md)
:   The hybrid import options.

#### Return Value

IList [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md) 
Returns an array of ElementIds representing created or updated elements. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[IFCHybridImport Class](IFCHybrid-Import-Class.md) [UpdateElements Overload](IFCHybrid-Import-Update-Elements-Method.md) [Autodesk.Revit.DB.IFC Namespace](../ungrouped/Autodesk.-Revit.-DB.-IFC-Namespace.md)
