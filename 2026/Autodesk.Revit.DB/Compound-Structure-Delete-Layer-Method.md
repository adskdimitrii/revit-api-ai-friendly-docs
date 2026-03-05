# Compound Structure Delete Layer Method

Source: https://www.revitapidocs.com/2026/64688e23-2d51-b072-35db-8e5b74e95804.htm

---

| Compound Structure Delete Layer Method |
| --- |

Deletes the specified layer from this CompoundStructure. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public bool DeleteLayer(
	int layerIdx
)
```

```
Public Function DeleteLayer ( 
	layerIdx As Integer
) As Boolean
```

```
public:
bool DeleteLayer(
	int layerIdx
)
```

```
member DeleteLayer : 
        layerIdx : int -> bool 
```

#### Parameters

layerIdx Int32
:   Index of a layer in the CompoundStructure. The layer index is zero based. It counts from the exterior of wall and from the top of roofs, floors and ceilings.

#### Return Value

Boolean 
True if the layer was successfully deleted, and false otherwise. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The layer cannot be deleted. |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The layer index is out of range. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks For a vertically compound structure, a layer
 may only be deleted if it is not associated to a region, or else it is associated to exactly one simple
 region, which will also be deleted. Regions associated to layers with index greater than layerIdx will
 have their associated layer indices decremented by one. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[CompoundStructure Class](Compound-Structure-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
