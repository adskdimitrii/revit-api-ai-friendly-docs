# Rebar Shape Definition By Segments Add Bend Variable Radius Method

Source: https://www.revitapidocs.com/2026/0a54d7c6-4951-e153-faba-b46dadb5c5c1.htm

---

| Rebar Shape Definition By Segments Add Bend Variable Radius Method |
| --- |

Specify a variable\-radius bend. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void AddBendVariableRadius(
	int vertexIndex,
	RebarShapeVertexTurn turn,
	RebarShapeBendAngle angle,
	ElementId paramId,
	bool measureIncludingBarThickness
)
```

```
Public Sub AddBendVariableRadius ( 
	vertexIndex As Integer,
	turn As RebarShapeVertexTurn,
	angle As RebarShapeBendAngle,
	paramId As ElementId,
	measureIncludingBarThickness As Boolean
)
```

```
public:
void AddBendVariableRadius(
	int vertexIndex, 
	RebarShapeVertexTurn turn, 
	RebarShapeBendAngle angle, 
	ElementId^ paramId, 
	bool measureIncludingBarThickness
)
```

```
member AddBendVariableRadius : 
        vertexIndex : int * 
        turn : RebarShapeVertexTurn * 
        angle : RebarShapeBendAngle * 
        paramId : ElementId * 
        measureIncludingBarThickness : bool -> unit 
```

#### Parameters

vertexIndex Int32
:   Index of the vertex (1 to NumberOfVertices \- 2\).

turn [RebarShapeVertexTurn](a59971ec-c31f-a05e-e2d7-65882e23a21f.htm)
:   Specify turn direction (RebarShapeVertexTurn::Left or RebarShapeVertexTurn::Right).

angle [RebarShapeBendAngle](176a9649-853e-f173-c108-d6722fcd5b61.htm)
:   Specify whether the bend is acute, obtuse, etc.

paramId [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
:   Id of a parameter driving the radius.

measureIncludingBarThickness Boolean
:   If true, the radius is measured to the outside of the
 bend; if false, it is measured to the inside.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | vertexIndex is not between 0 and NumberOfVertices.  \-or\-  paramId is not the id of a shared parameter in the current document,  or its unit type is not Reinforcement\_Length, Angle or Number. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks You must add a bend between each two segments. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarShapeDefinitionBySegments Class](7229fdba-1e8f-6cb7-e72e-0933e495ad62.htm) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
