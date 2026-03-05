# Compound Structure Set Deck Embedding Type Method

Source: https://www.revitapidocs.com/2026/2f291187-825d-fb60-cd4a-33280dce91e4.htm

---

| Compound Structure Set Deck Embedding Type Method |
| --- |

Sets the deck embedding type to use for the specified structural deck. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetDeckEmbeddingType(
	int layerIdx,
	StructDeckEmbeddingType embedType
)
```

```
Public Sub SetDeckEmbeddingType ( 
	layerIdx As Integer,
	embedType As StructDeckEmbeddingType
)
```

```
public:
void SetDeckEmbeddingType(
	int layerIdx, 
	StructDeckEmbeddingType embedType
)
```

```
member SetDeckEmbeddingType : 
        layerIdx : int * 
        embedType : StructDeckEmbeddingType -> unit 
```

#### Parameters

layerIdx Int32
:   Index of a layer in the CompoundStructure. The layer index is zero based. It counts from the exterior of wall and from the top of roofs, floors and ceilings.

embedType [StructDeckEmbeddingType](2cc96ee3-bb7b-26e8-271c-25975dbc9fc4.htm)
:   The embedding type to be used by the specified layer if it is a structural deck.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The layer is not a structural deck. |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The layer index is out of range.  \-or\-  A value passed for an enumeration argument is not a member of that enumeration |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[CompoundStructure Class](Compound-Structure-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
