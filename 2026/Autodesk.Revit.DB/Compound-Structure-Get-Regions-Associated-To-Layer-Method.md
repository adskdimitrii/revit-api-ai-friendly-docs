# Compound Structure Get Regions Associated To Layer Method

Source: https://www.revitapidocs.com/2026/682ac400-fff2-f729-f529-c6b95c96c860.htm

---

| Compound Structure Get Regions Associated To Layer Method |
| --- |

Gets the set of region ids associated to a particular layer. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public IList<int> GetRegionsAssociatedToLayer(
	int layerIdx
)
```

```
Public Function GetRegionsAssociatedToLayer ( 
	layerIdx As Integer
) As IList(Of Integer)
```

```
public:
IList<int>^ GetRegionsAssociatedToLayer(
	int layerIdx
)
```

```
member GetRegionsAssociatedToLayer : 
        layerIdx : int -> IList<int> 
```

#### Parameters

layerIdx Int32
:   Index of a layer in the CompoundStructure. The layer index is zero based. It counts from the exterior of wall and from the top of roofs, floors and ceilings.

#### Return Value

IList Int32 
An array of region ids which are associated to the specified layer. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The layer index is out of range. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks Regions are associated to layers. In a vertically compound structure, more than one region may be associated to a
 single layer. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[CompoundStructure Class](Compound-Structure-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
