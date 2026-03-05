# Compound Structure Get Layer Priority Method

Source: https://www.revitapidocs.com/2026/baf83c54-c9a8-9d99-6729-3695bfa9c423.htm

---

| Compound Structure Get Layer Priority Method |
| --- |

Retrieves the priority of the specified layer.
 Index of a layer in the CompoundStructure. The layer index is zero based. It counts from the exterior of wall and from the top of roofs, floors and ceilings. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public int GetLayerPriority(
	int layerIdx
)
```

```
Public Function GetLayerPriority ( 
	layerIdx As Integer
) As Integer
```

```
public:
int GetLayerPriority(
	int layerIdx
)
```

```
member GetLayerPriority : 
        layerIdx : int -> int 
```

#### Parameters

layerIdx Int32

#### Return Value

Int32 ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The layer index is out of range. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[CompoundStructure Class](Compound-Structure-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
