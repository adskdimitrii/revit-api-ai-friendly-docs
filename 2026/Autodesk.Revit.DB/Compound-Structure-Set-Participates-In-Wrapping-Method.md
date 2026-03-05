# Compound Structure Set Participates In Wrapping Method

Source: https://www.revitapidocs.com/2026/a0963e2b-4f8c-9117-a0cc-19da424e16d8.htm

---

| Compound Structure Set Participates In Wrapping Method |
| --- |

Assigns if a layer is included in wrapping at inserts and ends. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetParticipatesInWrapping(
	int layerIdx,
	bool participatesInWrapping
)
```

```
Public Sub SetParticipatesInWrapping ( 
	layerIdx As Integer,
	participatesInWrapping As Boolean
)
```

```
public:
void SetParticipatesInWrapping(
	int layerIdx, 
	bool participatesInWrapping
)
```

```
member SetParticipatesInWrapping : 
        layerIdx : int * 
        participatesInWrapping : bool -> unit 
```

#### Parameters

layerIdx Int32
:   Index of a layer in the CompoundStructure. The layer index is zero based. It counts from the exterior of wall and from the top of roofs, floors and ceilings.

participatesInWrapping Boolean
:   True if the specified layer will participate in wrapping at inserts and ends, false otherwise.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The wrapping of the layer is not valid. |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The layer index is out of range. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks This method applies only to interior and exterior shell layers. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[CompoundStructure Class](Compound-Structure-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
