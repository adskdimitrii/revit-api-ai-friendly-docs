# Compound Structure Get Layer Function Method

Source: https://www.revitapidocs.com/2026/7c681a04-b21d-99f2-76c1-d3415aa06576.htm

---

| Compound Structure Get Layer Function Method |
| --- |

Retrieves the function of the specified layer. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public MaterialFunctionAssignment GetLayerFunction(
	int layerIdx
)
```

```
Public Function GetLayerFunction ( 
	layerIdx As Integer
) As MaterialFunctionAssignment
```

```
public:
MaterialFunctionAssignment GetLayerFunction(
	int layerIdx
)
```

```
member GetLayerFunction : 
        layerIdx : int -> MaterialFunctionAssignment 
```

#### Parameters

layerIdx Int32
:   Index of a layer in the CompoundStructure. The layer index is zero based. It counts from the exterior of wall and from the top of roofs, floors and ceilings.

#### Return Value

[MaterialFunctionAssignment](Material-Function-Assignment-Enumeration.md) 
The function of the layer. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The layer index is out of range. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The function determines how this layer interacts with the layers of other elements to which it is joined. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[CompoundStructure Class](Compound-Structure-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
