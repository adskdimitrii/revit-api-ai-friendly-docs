# Compound Structure Set Layer Function Method

Source: https://www.revitapidocs.com/2026/afd19099-cc37-1cd3-80c8-e89df914e5e5.htm

---

| Compound Structure Set Layer Function Method |
| --- |

Sets the function of the specified layer. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetLayerFunction(
	int layerIdx,
	MaterialFunctionAssignment function
)
```

```
Public Sub SetLayerFunction ( 
	layerIdx As Integer,
	function As MaterialFunctionAssignment
)
```

```
public:
void SetLayerFunction(
	int layerIdx, 
	MaterialFunctionAssignment function
)
```

```
member SetLayerFunction : 
        layerIdx : int * 
        function : MaterialFunctionAssignment -> unit 
```

#### Parameters

layerIdx Int32
:   Index of a layer in the CompoundStructure. The layer index is zero based. It counts from the exterior of wall and from the top of roofs, floors and ceilings.

function [MaterialFunctionAssignment](Material-Function-Assignment-Enumeration.md)
:   The function of the layer.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The layer index is out of range.  \-or\-  A value passed for an enumeration argument is not a member of that enumeration |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[CompoundStructure Class](Compound-Structure-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
