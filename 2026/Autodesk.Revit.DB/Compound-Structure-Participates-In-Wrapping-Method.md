# Compound Structure Participates In Wrapping Method

Source: https://www.revitapidocs.com/2026/06cfa919-0839-7771-2ff1-02c43465daad.htm

---

| Compound Structure Participates In Wrapping Method |
| --- |

Identifies if a layer is included in wrapping at inserts and ends. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public bool ParticipatesInWrapping(
	int layerIdx
)
```

```
Public Function ParticipatesInWrapping ( 
	layerIdx As Integer
) As Boolean
```

```
public:
bool ParticipatesInWrapping(
	int layerIdx
)
```

```
member ParticipatesInWrapping : 
        layerIdx : int -> bool 
```

#### Parameters

layerIdx Int32
:   Index of a layer in the CompoundStructure. The layer index is zero based. It counts from the exterior of wall and from the top of roofs, floors and ceilings.

#### Return Value

Boolean 
If true, then the layer participates in wrapping at inserts and openings. If false, the layer will not
 participate in wrapping. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The layer index is out of range. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks This method applies only to interior and exterior shell layers. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[CompoundStructure Class](Compound-Structure-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
