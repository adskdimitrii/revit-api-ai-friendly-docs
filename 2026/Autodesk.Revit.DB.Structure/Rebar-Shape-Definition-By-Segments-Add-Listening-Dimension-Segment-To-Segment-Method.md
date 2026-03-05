# Rebar Shape Definition By Segments Add Listening Dimension Segment To Segment Method

Source: https://www.revitapidocs.com/2026/6a85387a-f0f5-ed76-6cf6-bc1f5f309977.htm

---

| Rebar Shape Definition By Segments Add Listening Dimension Segment To Segment Method |
| --- |

Specify a dimension perpendicular to two fixed\-direction segments, measured by a read\-only parameter. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void AddListeningDimensionSegmentToSegment(
	ElementId paramId,
	double constraintDirCoordX,
	double constraintDirCoordY,
	int iSegment0,
	int iSegment1
)
```

```
Public Sub AddListeningDimensionSegmentToSegment ( 
	paramId As ElementId,
	constraintDirCoordX As Double,
	constraintDirCoordY As Double,
	iSegment0 As Integer,
	iSegment1 As Integer
)
```

```
public:
void AddListeningDimensionSegmentToSegment(
	ElementId^ paramId, 
	double constraintDirCoordX, 
	double constraintDirCoordY, 
	int iSegment0, 
	int iSegment1
)
```

```
member AddListeningDimensionSegmentToSegment : 
        paramId : ElementId * 
        constraintDirCoordX : float * 
        constraintDirCoordY : float * 
        iSegment0 : int * 
        iSegment1 : int -> unit 
```

#### Parameters

paramId [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
:   Id of a parameter to report the length of the dimension. The parameter will be read\-only
 on Rebar instances.

constraintDirCoordX Double
:   The x\-coordinate of a 2D vector specifying the constraint direction.

constraintDirCoordY Double
:   The y\-coordinate of a 2D vector specifying the constraint direction.

iSegment0 Int32
:   Index of the first segment (0 to NumberOfSegments \- 1\).

iSegment1 Int32
:   Index of the second segment (0 to NumberOfSegments \- 1\).

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | paramId is not the id of a shared parameter in the current document,  or its unit type is not Reinforcement\_Length, Angle or Number.  \-or\-  The length of the vector (constraintDirCoordX, constraintDirCoordY) is too close to zero.  \-or\-  iSegment0 is not between 0 and NumberOfSegments.  \-or\-  iSegment1 is not between 0 and NumberOfSegments.  \-or\-  Edge iSegment0 has a variable angle; it must have a fixed angle perpendicular to (constraintDirCoordX, constraintDirCoordY).  \-or\-  Edge iSegment1 has a variable angle; it must have a fixed angle perpendicular to (constraintDirCoordX, constraintDirCoordY). |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks RebarShapeDefinitionBySegments supports driving (read\-write) dimensions only when they are associated with a single segment. Non\-driving dimensions can involve multiple segments. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarShapeDefinitionBySegments Class](7229fdba-1e8f-6cb7-e72e-0933e495ad62.htm) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
