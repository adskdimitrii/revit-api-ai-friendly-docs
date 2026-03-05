# Rebar Shape Definition By Segments Add Constraint Parallel To Segment Method

Source: https://www.revitapidocs.com/2026/c244128f-c910-c1f7-982d-dd01a5584557.htm

---

| Rebar Shape Definition By Segments Add Constraint Parallel To Segment Method |
| --- |

Constrain the length of a segment by parameterizing its length. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void AddConstraintParallelToSegment(
	int iSegment,
	ElementId paramId,
	bool measureToOutsideOfBend0,
	bool measureToOutsideOfBend1
)
```

```
Public Sub AddConstraintParallelToSegment ( 
	iSegment As Integer,
	paramId As ElementId,
	measureToOutsideOfBend0 As Boolean,
	measureToOutsideOfBend1 As Boolean
)
```

```
public:
void AddConstraintParallelToSegment(
	int iSegment, 
	ElementId^ paramId, 
	bool measureToOutsideOfBend0, 
	bool measureToOutsideOfBend1
)
```

```
member AddConstraintParallelToSegment : 
        iSegment : int * 
        paramId : ElementId * 
        measureToOutsideOfBend0 : bool * 
        measureToOutsideOfBend1 : bool -> unit 
```

#### Parameters

iSegment Int32
:   Index of the segment (0 to NumberOfSegments \- 1\).

paramId [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
:   Id of a parameter to drive the constraint. To obtain the id of a shared parameter,
 call RebarShape.GetElementIdForExternalDefinition().

measureToOutsideOfBend0 Boolean
:   Choose between two possibilities for the first reference of the length dimension. If false, the reference is at the point where the bend begins; equivalently, at the projection of the bend centerpoint onto the segment. If true, the reference is moved outward by a distance equal to the bend radius plus the bar diameter; if the bend is a right angle or greater, this is equivalent to putting the reference at the outer face of the bend.

measureToOutsideOfBend1 Boolean
:   Choose between two possibilities for the second reference of the length dimension.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | iSegment is not between 0 and NumberOfSegments.  \-or\-  paramId is not the id of a shared parameter in the current document,  or its unit type is not Reinforcement\_Length, Angle or Number. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarShapeDefinitionBySegments Class](7229fdba-1e8f-6cb7-e72e-0933e495ad62.htm) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
