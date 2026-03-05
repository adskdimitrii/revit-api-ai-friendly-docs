# IFCHybrid Import Import Elements(Document, String) Method

Source: https://www.revitapidocs.com/2026/7d0a704f-1f57-ffe4-8853-a2326dfaf88d.htm

---

| IFCHybrid Import Import Elements(Document, String) Method |
| --- |

**Note: This API is now obsolete.** 

Imports IFC Elements using AnyCAD. 
**Namespace:** [Autodesk.Revit.DB.IFC](../ungrouped/Autodesk.-Revit.-DB.-IFC-Namespace.md) 
**Assembly:** RevitAPIIFC (in RevitAPIIFC.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This is deprecated in Revit 2026.  Please use the importElements function with the IFCHybridImportOptions.")]
public IList<ElementId> ImportElements(
	Document doc,
	string file
)
```

```
<ObsoleteAttribute("This is deprecated in Revit 2026.  Please use the importElements function with the IFCHybridImportOptions.")>
Public Function ImportElements ( 
	doc As Document,
	file As String
) As IList(Of ElementId)
```

```
public:
[ObsoleteAttribute(L"This is deprecated in Revit 2026.  Please use the importElements function with the IFCHybridImportOptions.")]
IList<ElementId^>^ ImportElements(
	Document^ doc, 
	String^ file
)
```

```
[<ObsoleteAttribute("This is deprecated in Revit 2026.  Please use the importElements function with the IFCHybridImportOptions.")>]
member ImportElements : 
        doc : Document * 
        file : string -> IList<ElementId> 
```

#### Parameters

doc [Document](../Autodesk.Revit.DB/Document-Class.md)
:   Document to receive elements from the IFC file import.

file String
:   Full path of the file to import.

#### Return Value

IList [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md) 
Returns an array of ElementIds representing created elements. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[IFCHybridImport Class](IFCHybrid-Import-Class.md) [ImportElements Overload](IFCHybrid-Import-Import-Elements-Method.md) [Autodesk.Revit.DB.IFC Namespace](../ungrouped/Autodesk.-Revit.-DB.-IFC-Namespace.md)
