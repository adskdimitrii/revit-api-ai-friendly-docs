# Compound Structure Can Layer Width Be Non Zero Method

Source: https://www.revitapidocs.com/2026/cae97272-2e0d-cee9-519d-9a983dd05de1.htm

---

| Compound Structure Can Layer Width Be Non Zero Method |
| --- |

Identifies if changing the width of an existing layer from zero to a positive value will create a rectangular region. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public bool CanLayerWidthBeNonZero(
	int layerIdx
)
```

```
Public Function CanLayerWidthBeNonZero ( 
	layerIdx As Integer
) As Boolean
```

```
public:
bool CanLayerWidthBeNonZero(
	int layerIdx
)
```

```
member CanLayerWidthBeNonZero : 
        layerIdx : int -> bool 
```

#### Parameters

layerIdx Int32
:   Index of a layer in the CompoundStructure. The layer index is zero based. It counts from the exterior of wall and from the top of roofs, floors and ceilings.

#### Return Value

Boolean ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks This is only allowed if there is a vertical line such that all regions to the left are assigned to layers with index \< layerIdx,
 and all regions to the right are assigned to layers with index \> layerIdx. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[CompoundStructure Class](Compound-Structure-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
