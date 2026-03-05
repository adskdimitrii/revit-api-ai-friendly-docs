# Rebar Shape Definition By Segments Add Constraint To Segment Method

Source: https://www.revitapidocs.com/2026/ffaca4d8-ddb4-c21e-7830-b5fffe314fc8.htm

---

| Rebar Shape Definition By Segments Add Constraint To Segment Method |
| --- |

Add a constraint that helps determine the length of a segment. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void AddConstraintToSegment(
	int iSegment,
	ElementId paramId,
	double constraintDirCoordX,
	double constraintDirCoordY,
	int signOfZCoordOfCrossProductOfConstraintDirBySegmentDir,
	bool measureToOutsideOfBend0,
	bool measureToOutsideOfBend1
)
```

```
Public Sub AddConstraintToSegment ( 
	iSegment As Integer,
	paramId As ElementId,
	constraintDirCoordX As Double,
	constraintDirCoordY As Double,
	signOfZCoordOfCrossProductOfConstraintDirBySegmentDir As Integer,
	measureToOutsideOfBend0 As Boolean,
	measureToOutsideOfBend1 As Boolean
)
```

```
public:
void AddConstraintToSegment(
	int iSegment, 
	ElementId^ paramId, 
	double constraintDirCoordX, 
	double constraintDirCoordY, 
	int signOfZCoordOfCrossProductOfConstraintDirBySegmentDir, 
	bool measureToOutsideOfBend0, 
	bool measureToOutsideOfBend1
)
```

```
member AddConstraintToSegment : 
        iSegment : int * 
        paramId : ElementId * 
        constraintDirCoordX : float * 
        constraintDirCoordY : float * 
        signOfZCoordOfCrossProductOfConstraintDirBySegmentDir : int * 
        measureToOutsideOfBend0 : bool * 
        measureToOutsideOfBend1 : bool -> unit 
```

#### Parameters

iSegment Int32
:   Index of the segment (0 to NumberOfSegments \- 1\).

paramId [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
:   Id of a parameter to drive the constraint.
 To obtain the id of a shared parameter,
 call RebarShape.GetElementIdForExternalDefinition().

constraintDirCoordX Double
:   The x\-coordinate of a 2D vector specifying the constraint direction.

constraintDirCoordY Double
:   The y\-coordinate of a 2D vector specifying the constraint direction.

signOfZCoordOfCrossProductOfConstraintDirBySegmentDir Int32
:   Legal values are 1 and \-1\. For a fixed\-direction segment, this value is ignored. For a variable\-direction segment, this value is combined with the constraint length (the nonnegative value associated with 'param') to determine the direction of the segment. For example, a segment whose direction vector lies in the upper\-right quadrant of the plane, and whose x\-axis projected length is A and whose y\-axis projected length is B, could be created by calling: AddConstraintToSegment(iSegment, paramA, 1\.0, 0\.0, 1, ...) AddConstraintToSegment(iSegment, paramB, 0\.0, 1\.0, \-1, ...)

measureToOutsideOfBend0 Boolean
:   Choose between two possibilities for the first reference of the length dimension. If false, the reference is at the point where the bend begins; equivalently, at the projection of the bend centerpoint onto the segment. If true, the reference is moved outward by a distance equal to the bend radius plus the bar diameter; if the bend is a right angle or greater, this is equivalent to putting the reference at the outer face of the bend.

measureToOutsideOfBend1 Boolean
:   Choose between two possibilities for the second reference of the length dimension.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | iSegment is not between 0 and NumberOfSegments.  \-or\-  paramId is not the id of a shared parameter in the current document,  or its unit type is not Reinforcement\_Length, Angle or Number.  \-or\-  The length of the vector (constraintDirCoordX, constraintDirCoordY) is too close to zero.  \-or\-  signOfZCoordOfCrossProductOfConstraintDirBySegmentDir is neither \-1 nor 1\. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The vector defined by (constraintDirCoordX, constraintDirCoordY) must have a positive dot product with the desired direction of the segment. This restriction, combined with the value of signOfZCoordOfCrossProductOfConstraintDirBySegmentDir, defines a quadrant of the plane that limits the variable\-angle segment. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarShapeDefinitionBySegments Class](7229fdba-1e8f-6cb7-e72e-0933e495ad62.htm) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
