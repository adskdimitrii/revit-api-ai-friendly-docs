# Compound Structure Is Layer Valid Method

Source: https://www.revitapidocs.com/2026/820dfece-50bc-df1c-4078-7ae07bdc35ca.htm

---

| Compound Structure Is Layer Valid Method |
| --- |

Verifies that the data in this layer is internally consistent. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public bool IsLayerValid(
	int layerIdx,
	CompoundStructureLayer layer
)
```

```
Public Function IsLayerValid ( 
	layerIdx As Integer,
	layer As CompoundStructureLayer
) As Boolean
```

```
public:
bool IsLayerValid(
	int layerIdx, 
	CompoundStructureLayer^ layer
)
```

```
member IsLayerValid : 
        layerIdx : int * 
        layer : CompoundStructureLayer -> bool 
```

#### Parameters

layerIdx Int32
:   Index of a layer in the CompoundStructure. The layer index is zero based. It counts from the exterior of wall and from the top of roofs, floors and ceilings.

layer [CompoundStructureLayer](Compound-Structure-Layer-Class.md)
:   The layer to be set.

#### Return Value

Boolean 
True if the layer is internally consistent, false if the layer is not internally consistent. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks If the layer function is not Membrane or StructuralDeck, the width must be greater than zero.
 If the layer function is not StructuralDeck, then the deck embedding type must be Invalid, and the deck profile id must be InvalidElementId.
 The priority must be valid to match the function. Refer to [IsValidLayerPriority(Int32, Int32\)](Compound-Structure-Is-Valid-Layer-Priority-Method.md) . ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[CompoundStructure Class](Compound-Structure-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
