# Structural Connection Handler Type Remove Main Subelements From Custom Connection Method

Source: https://www.revitapidocs.com/2026/09882898-b699-9b91-742b-ea6bd75942a1.htm

---

| Structural Connection Handler Type Remove Main Subelements From Custom Connection Method |
| --- |

**Note: This API is now obsolete.** 

  
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Prefer updateCustomConnectionType instead.")]
public static void RemoveMainSubelementsFromCustomConnection(
	StructuralConnectionHandler structuralConnectionHandler,
	IList<Subelement> subelements
)
```

```
<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Prefer updateCustomConnectionType instead.")>
Public Shared Sub RemoveMainSubelementsFromCustomConnection ( 
	structuralConnectionHandler As StructuralConnectionHandler,
	subelements As IList(Of Subelement)
)
```

```
public:
[ObsoleteAttribute(L"This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Prefer updateCustomConnectionType instead.")]
static void RemoveMainSubelementsFromCustomConnection(
	StructuralConnectionHandler^ structuralConnectionHandler, 
	IList<Subelement^>^ subelements
)
```

```
[<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Prefer updateCustomConnectionType instead.")>]
static member RemoveMainSubelementsFromCustomConnection : 
        structuralConnectionHandler : StructuralConnectionHandler * 
        subelements : IList<Subelement> -> unit 
```

#### Parameters

structuralConnectionHandler [StructuralConnectionHandler](78653026-36f1-6ab3-f2c0-728692c99b3c.htm)
subelements IList [Subelement](../Autodesk.Revit.DB/Subelement-Class.md)

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[StructuralConnectionHandlerType Class](Structural-Connection-Handler-Type-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
