# Compound Structure Reset Layer Priority Method

Source: https://www.revitapidocs.com/2026/8f5e9e2d-e1fa-2229-9717-dd2130651d03.htm

---

| Compound Structure Reset Layer Priority Method |
| --- |

Resets the priority of the specific layer to the default priority defined by its function. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void ResetLayerPriority(
	int layerIdx
)
```

```
Public Sub ResetLayerPriority ( 
	layerIdx As Integer
)
```

```
public:
void ResetLayerPriority(
	int layerIdx
)
```

```
member ResetLayerPriority : 
        layerIdx : int -> unit 
```

#### Parameters

layerIdx Int32
:   Index of a layer in the CompoundStructure. The layer index is zero based. It counts from the exterior of wall and from the top of roofs, floors and ceilings.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The layer index is out of range. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The default priorities definition:
 Structure: 1, Substrate: 2, Thermal/Air Layer: 3, Membrane Layer: 999, Finish 1: 4, Finish 2: 5\.
 In shell, a non\-membrane layer which is closer to the core should not have a lower priority. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[CompoundStructure Class](Compound-Structure-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
