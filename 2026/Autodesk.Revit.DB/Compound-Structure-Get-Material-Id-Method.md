# Compound Structure Get Material Id Method

Source: https://www.revitapidocs.com/2026/f5d0da40-935f-f18b-13e0-c4e5d8d8aca9.htm

---

| Compound Structure Get Material Id Method |
| --- |

Retrieves the material element id of a specified layer. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public ElementId GetMaterialId(
	int layerIdx
)
```

```
Public Function GetMaterialId ( 
	layerIdx As Integer
) As ElementId
```

```
public:
ElementId^ GetMaterialId(
	int layerIdx
)
```

```
member GetMaterialId : 
        layerIdx : int -> ElementId 
```

#### Parameters

layerIdx Int32
:   Index of a layer in the CompoundStructure. The layer index is zero based. It counts from the exterior of wall and from the top of roofs, floors and ceilings.

#### Return Value

[ElementId](Element-Id-Class.md) 
The material element id. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The layer index is out of range. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[CompoundStructure Class](Compound-Structure-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
