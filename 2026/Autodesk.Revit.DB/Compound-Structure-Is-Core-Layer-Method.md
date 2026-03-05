# Compound Structure Is Core Layer Method

Source: https://www.revitapidocs.com/2026/b71b0e57-fcdc-2b51-0418-7317ee135c3c.htm

---

| Compound Structure Is Core Layer Method |
| --- |

Checks if the specified layer is a core layer. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public bool IsCoreLayer(
	int layerIdx
)
```

```
Public Function IsCoreLayer ( 
	layerIdx As Integer
) As Boolean
```

```
public:
bool IsCoreLayer(
	int layerIdx
)
```

```
member IsCoreLayer : 
        layerIdx : int -> bool 
```

#### Parameters

layerIdx Int32
:   Index of a layer in the CompoundStructure. The layer index is zero based. It counts from the exterior of wall and from the top of roofs, floors and ceilings.

#### Return Value

Boolean 
Returns true if the layer is within the core layer boundary, false if it is in the interior or exterior shell layers. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks You can change the shell/core layer boundary using [SetNumberOfShellLayers(ShellLayerType, Int32\)](Compound-Structure-Set-Number-Of-Shell-Layers-Method.md) . ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[CompoundStructure Class](Compound-Structure-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
