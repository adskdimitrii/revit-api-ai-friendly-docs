# Structural Connection Handler Type Add Elements To Custom Connection Method

Source: https://www.revitapidocs.com/2026/4ce5c475-c74a-c5aa-0724-8df7c1a0cacb.htm

---

| Structural Connection Handler Type Add Elements To Custom Connection Method |
| --- |

**Note: This API is now obsolete.** 

  
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Prefer updateCustomConnectionType instead.")]
public static void AddElementsToCustomConnection(
	StructuralConnectionHandler structuralConnectionHandler,
	IList<Reference> references
)
```

```
<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Prefer updateCustomConnectionType instead.")>
Public Shared Sub AddElementsToCustomConnection ( 
	structuralConnectionHandler As StructuralConnectionHandler,
	references As IList(Of Reference)
)
```

```
public:
[ObsoleteAttribute(L"This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Prefer updateCustomConnectionType instead.")]
static void AddElementsToCustomConnection(
	StructuralConnectionHandler^ structuralConnectionHandler, 
	IList<Reference^>^ references
)
```

```
[<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Prefer updateCustomConnectionType instead.")>]
static member AddElementsToCustomConnection : 
        structuralConnectionHandler : StructuralConnectionHandler * 
        references : IList<Reference> -> unit 
```

#### Parameters

structuralConnectionHandler [StructuralConnectionHandler](78653026-36f1-6ab3-f2c0-728692c99b3c.htm)
references IList [Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[StructuralConnectionHandlerType Class](Structural-Connection-Handler-Type-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
