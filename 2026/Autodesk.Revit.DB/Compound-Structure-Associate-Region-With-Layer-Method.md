# Compound Structure Associate Region With Layer Method

Source: https://www.revitapidocs.com/2026/e0e669e0-97dd-5797-d75d-151fb3634af4.htm

---

| Compound Structure Associate Region With Layer Method |
| --- |

Associates a region with a layer. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void AssociateRegionWithLayer(
	int regionId,
	int layerIdx
)
```

```
Public Sub AssociateRegionWithLayer ( 
	regionId As Integer,
	layerIdx As Integer
)
```

```
public:
void AssociateRegionWithLayer(
	int regionId, 
	int layerIdx
)
```

```
member AssociateRegionWithLayer : 
        regionId : int * 
        layerIdx : int -> unit 
```

#### Parameters

regionId Int32
:   The id of a region.

layerIdx Int32
:   Index of a layer in the CompoundStructure. The layer index is zero based. It counts from the exterior of wall and from the top of roofs, floors and ceilings.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | It is not a valid region id. |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The layer index is out of range. |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This operation is valid only for vertically compound structures. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[CompoundStructure Class](Compound-Structure-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
