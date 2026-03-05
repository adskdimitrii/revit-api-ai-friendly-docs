# Compound Structure Layer(Double, Material Function Assignment, Element Id) Constructor

Source: https://www.revitapidocs.com/2026/90c2ea06-4e80-c8c0-dbde-1b3f831c2de5.htm

---

| Compound Structure Layer(Double, Material Function Assignment, Element Id) Constructor |
| --- |

Creates a default compound structure layer based on the given width, function and material element id. The priority is initialized with 999\. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public CompoundStructureLayer(
	double width,
	MaterialFunctionAssignment function,
	ElementId materialId
)
```

```
Public Sub New ( 
	width As Double,
	function As MaterialFunctionAssignment,
	materialId As ElementId
)
```

```
public:
CompoundStructureLayer(
	double width, 
	MaterialFunctionAssignment function, 
	ElementId^ materialId
)
```

```
new : 
        width : float * 
        function : MaterialFunctionAssignment * 
        materialId : ElementId -> CompoundStructureLayer
```

#### Parameters

width Double
:   The width of the layer.

function [MaterialFunctionAssignment](Material-Function-Assignment-Enumeration.md)
:   The function of the layer.

materialId [ElementId](Element-Id-Class.md)
:   The material element id of the layer.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[CompoundStructureLayer Class](Compound-Structure-Layer-Class.md) [CompoundStructureLayer Overload](Compound-Structure-Layer-Constructor.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
