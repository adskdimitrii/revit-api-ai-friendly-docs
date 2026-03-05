# Structural Connection Handler Type Update Custom Connection Type Method

Source: https://www.revitapidocs.com/2026/bd060853-9bb7-9fa6-10aa-1aa5b86c8e5a.htm

---

| Structural Connection Handler Type Update Custom Connection Type Method |
| --- |

  
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static void UpdateCustomConnectionType(
	StructuralConnectionHandler structuralConnectionHandler,
	IList<Reference> addReferences,
	IList<Reference> removeReferences
)
```

```
Public Shared Sub UpdateCustomConnectionType ( 
	structuralConnectionHandler As StructuralConnectionHandler,
	addReferences As IList(Of Reference),
	removeReferences As IList(Of Reference)
)
```

```
public:
static void UpdateCustomConnectionType(
	StructuralConnectionHandler^ structuralConnectionHandler, 
	IList<Reference^>^ addReferences, 
	IList<Reference^>^ removeReferences
)
```

```
static member UpdateCustomConnectionType : 
        structuralConnectionHandler : StructuralConnectionHandler * 
        addReferences : IList<Reference> * 
        removeReferences : IList<Reference> -> unit 
```

#### Parameters

structuralConnectionHandler [StructuralConnectionHandler](78653026-36f1-6ab3-f2c0-728692c99b3c.htm)
addReferences IList [Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)
removeReferences IList [Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[StructuralConnectionHandlerType Class](Structural-Connection-Handler-Type-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
