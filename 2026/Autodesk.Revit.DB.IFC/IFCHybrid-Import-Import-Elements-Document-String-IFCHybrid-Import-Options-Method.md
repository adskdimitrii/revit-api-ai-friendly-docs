# IFCHybrid Import Import Elements(Document, String, IFCHybrid Import Options) Method

Source: https://www.revitapidocs.com/2026/63776046-0d92-771d-a123-615c33bd62c5.htm

---

| IFCHybrid Import Import Elements(Document, String, IFCHybrid Import Options) Method |
| --- |

Imports IFC Elements using AnyCAD. 
**Namespace:** [Autodesk.Revit.DB.IFC](../ungrouped/Autodesk.-Revit.-DB.-IFC-Namespace.md) 
**Assembly:** RevitAPIIFC (in RevitAPIIFC.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public IList<ElementId> ImportElements(
	Document doc,
	string file,
	IFCHybridImportOptions options
)
```

```
Public Function ImportElements ( 
	doc As Document,
	file As String,
	options As IFCHybridImportOptions
) As IList(Of ElementId)
```

```
public:
IList<ElementId^>^ ImportElements(
	Document^ doc, 
	String^ file, 
	IFCHybridImportOptions^ options
)
```

```
member ImportElements : 
        doc : Document * 
        file : string * 
        options : IFCHybridImportOptions -> IList<ElementId> 
```

#### Parameters

doc [Document](../Autodesk.Revit.DB/Document-Class.md)
:   Document to receive elements from the IFC file import.

file String
:   Full path of the file to import.

options [IFCHybridImportOptions](IFCHybrid-Import-Options-Class.md)
:   The hybrid import options.

#### Return Value

IList [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md) 
Returns an array of ElementIds representing created elements. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[IFCHybridImport Class](IFCHybrid-Import-Class.md) [ImportElements Overload](IFCHybrid-Import-Import-Elements-Method.md) [Autodesk.Revit.DB.IFC Namespace](../ungrouped/Autodesk.-Revit.-DB.-IFC-Namespace.md)
