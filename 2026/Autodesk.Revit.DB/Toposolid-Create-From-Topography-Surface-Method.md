# Toposolid Create From Topography Surface Method

Source: https://www.revitapidocs.com/2026/662a7ccb-63b9-a106-1b3e-659af6a35c70.htm

---

| Toposolid Create From Topography Surface Method |
| --- |

Creates a Toposolid element from a host TopographySurface, and Toposolid sub\-divisions from its subregions. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static Toposolid CreateFromTopographySurface(
	Document document,
	ElementId hostSurfaceId,
	ElementId topoTypeId,
	ElementId levelId
)
```

```
Public Shared Function CreateFromTopographySurface ( 
	document As Document,
	hostSurfaceId As ElementId,
	topoTypeId As ElementId,
	levelId As ElementId
) As Toposolid
```

```
public:
static Toposolid^ CreateFromTopographySurface(
	Document^ document, 
	ElementId^ hostSurfaceId, 
	ElementId^ topoTypeId, 
	ElementId^ levelId
)
```

```
static member CreateFromTopographySurface : 
        document : Document * 
        hostSurfaceId : ElementId * 
        topoTypeId : ElementId * 
        levelId : ElementId -> Toposolid 
```

#### Parameters

document [Document](Document-Class.md)
:   The document in which the new Toposolid is created.

hostSurfaceId [ElementId](Element-Id-Class.md)
:   Id of the host TopogarphySurface element.

topoTypeId [ElementId](Element-Id-Class.md)
:   Id of the Toposolid type to be used by the new Toposolid.

levelId [ElementId](Element-Id-Class.md)
:   Id of the level on which the Toposolid is to be placed.

#### Return Value

[Toposolid](Toposolid-Class.md) 
A new Toposolid object within the project if successful. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Toposolid Class](Toposolid-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
