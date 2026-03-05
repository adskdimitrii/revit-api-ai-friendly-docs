# Generic Zone Create Method

Source: https://www.revitapidocs.com/2026/2af51757-c003-cd4f-25de-82e0d5964824.htm

---

| Generic Zone Create Method |
| --- |

**Note: This API is now obsolete.** 

  
**Namespace:** [Autodesk.Revit.DB.Analysis](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Prefer createSketchBased instead.")]
public static GenericZone Create(
	Document doc,
	string name,
	GenericZoneDomainData domainData,
	ElementId levelId,
	IList<CurveLoop> curveLoops
)
```

```
<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Prefer createSketchBased instead.")>
Public Shared Function Create ( 
	doc As Document,
	name As String,
	domainData As GenericZoneDomainData,
	levelId As ElementId,
	curveLoops As IList(Of CurveLoop)
) As GenericZone
```

```
public:
[ObsoleteAttribute(L"This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Prefer createSketchBased instead.")]
static GenericZone^ Create(
	Document^ doc, 
	String^ name, 
	GenericZoneDomainData^ domainData, 
	ElementId^ levelId, 
	IList<CurveLoop^>^ curveLoops
)
```

```
[<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Prefer createSketchBased instead.")>]
static member Create : 
        doc : Document * 
        name : string * 
        domainData : GenericZoneDomainData * 
        levelId : ElementId * 
        curveLoops : IList<CurveLoop> -> GenericZone 
```

#### Parameters

doc [Document](../Autodesk.Revit.DB/Document-Class.md)
name String
domainData [GenericZoneDomainData](c2c91032-f21e-f0b7-0c3b-73e720f42d68.htm)
levelId [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
curveLoops IList [CurveLoop](84824924-cb89-9e20-de6e-3461f429dfd6.htm)

#### Return Value

[GenericZone](Generic-Zone-Class.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[GenericZone Class](Generic-Zone-Class.md) [Autodesk.Revit.DB.Analysis Namespace](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md)
