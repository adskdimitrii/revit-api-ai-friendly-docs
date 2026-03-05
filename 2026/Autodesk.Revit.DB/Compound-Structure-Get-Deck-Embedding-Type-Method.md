# Compound Structure Get Deck Embedding Type Method

Source: https://www.revitapidocs.com/2026/bb52f22b-39b0-72ae-cb2f-4504eac02e9d.htm

---

| Compound Structure Get Deck Embedding Type Method |
| --- |

Retrieves the deck embedding type used for the specified structural deck. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public StructDeckEmbeddingType GetDeckEmbeddingType(
	int layerIdx
)
```

```
Public Function GetDeckEmbeddingType ( 
	layerIdx As Integer
) As StructDeckEmbeddingType
```

```
public:
StructDeckEmbeddingType GetDeckEmbeddingType(
	int layerIdx
)
```

```
member GetDeckEmbeddingType : 
        layerIdx : int -> StructDeckEmbeddingType 
```

#### Parameters

layerIdx Int32
:   Index of a layer in the CompoundStructure. The layer index is zero based. It counts from the exterior of wall and from the top of roofs, floors and ceilings.

#### Return Value

[StructDeckEmbeddingType](2cc96ee3-bb7b-26e8-271c-25975dbc9fc4.htm) 
The embedding type of the structural deck associated to the specified layer. Invalid if it is not a structural deck. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The layer index is out of range. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[CompoundStructure Class](Compound-Structure-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
