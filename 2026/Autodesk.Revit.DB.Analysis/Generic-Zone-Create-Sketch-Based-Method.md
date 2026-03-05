# Generic Zone Create Sketch Based Method

Source: https://www.revitapidocs.com/2026/29d77d56-9e59-4d7b-7804-7bb1df60e111.htm

---

| Generic Zone Create Sketch Based Method |
| --- |

  
**Namespace:** [Autodesk.Revit.DB.Analysis](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static GenericZone CreateSketchBased(
	Document doc,
	ElementId typeId,
	string name,
	GenericZoneDomainData domainData,
	ElementId levelId,
	IList<CurveLoop> curveLoops
)
```

```
Public Shared Function CreateSketchBased ( 
	doc As Document,
	typeId As ElementId,
	name As String,
	domainData As GenericZoneDomainData,
	levelId As ElementId,
	curveLoops As IList(Of CurveLoop)
) As GenericZone
```

```
public:
static GenericZone^ CreateSketchBased(
	Document^ doc, 
	ElementId^ typeId, 
	String^ name, 
	GenericZoneDomainData^ domainData, 
	ElementId^ levelId, 
	IList<CurveLoop^>^ curveLoops
)
```

```
static member CreateSketchBased : 
        doc : Document * 
        typeId : ElementId * 
        name : string * 
        domainData : GenericZoneDomainData * 
        levelId : ElementId * 
        curveLoops : IList<CurveLoop> -> GenericZone 
```

#### Parameters

doc [Document](../Autodesk.Revit.DB/Document-Class.md)
typeId [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
name String
domainData [GenericZoneDomainData](c2c91032-f21e-f0b7-0c3b-73e720f42d68.htm)
levelId [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
curveLoops IList [CurveLoop](84824924-cb89-9e20-de6e-3461f429dfd6.htm)

#### Return Value

[GenericZone](Generic-Zone-Class.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[GenericZone Class](Generic-Zone-Class.md) [Autodesk.Revit.DB.Analysis Namespace](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md)
