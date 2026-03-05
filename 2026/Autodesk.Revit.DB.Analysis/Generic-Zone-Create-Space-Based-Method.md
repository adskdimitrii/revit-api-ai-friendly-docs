# Generic Zone Create Space Based Method

Source: https://www.revitapidocs.com/2026/db52b16e-3f63-9f89-64d4-7e15d2fcf909.htm

---

| Generic Zone Create Space Based Method |
| --- |

  
**Namespace:** [Autodesk.Revit.DB.Analysis](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static GenericZone CreateSpaceBased(
	Document doc,
	ElementId typeId,
	string name,
	GenericZoneDomainData domainData,
	ElementId levelId,
	ISet<ElementId> spaceIds
)
```

```
Public Shared Function CreateSpaceBased ( 
	doc As Document,
	typeId As ElementId,
	name As String,
	domainData As GenericZoneDomainData,
	levelId As ElementId,
	spaceIds As ISet(Of ElementId)
) As GenericZone
```

```
public:
static GenericZone^ CreateSpaceBased(
	Document^ doc, 
	ElementId^ typeId, 
	String^ name, 
	GenericZoneDomainData^ domainData, 
	ElementId^ levelId, 
	ISet<ElementId^>^ spaceIds
)
```

```
static member CreateSpaceBased : 
        doc : Document * 
        typeId : ElementId * 
        name : string * 
        domainData : GenericZoneDomainData * 
        levelId : ElementId * 
        spaceIds : ISet<ElementId> -> GenericZone 
```

#### Parameters

doc [Document](../Autodesk.Revit.DB/Document-Class.md)
typeId [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
name String
domainData [GenericZoneDomainData](c2c91032-f21e-f0b7-0c3b-73e720f42d68.htm)
levelId [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
spaceIds ISet [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)

#### Return Value

[GenericZone](Generic-Zone-Class.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[GenericZone Class](Generic-Zone-Class.md) [Autodesk.Revit.DB.Analysis Namespace](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md)
