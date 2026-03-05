# Rebar Shape Definition By Segments Add Listening Dimension Bend To Bend Method

Source: https://www.revitapidocs.com/2026/4b140fb2-df81-856d-8188-6630c5be2006.htm

---

| Rebar Shape Definition By Segments Add Listening Dimension Bend To Bend Method |
| --- |

Specify a dimension between two bends, measured by a read\-only parameter. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void AddListeningDimensionBendToBend(
	ElementId paramId,
	double constraintDirCoordX,
	double constraintDirCoordY,
	int iSegment0,
	int iEnd0,
	int iSegment1,
	int iEnd1
)
```

```
Public Sub AddListeningDimensionBendToBend ( 
	paramId As ElementId,
	constraintDirCoordX As Double,
	constraintDirCoordY As Double,
	iSegment0 As Integer,
	iEnd0 As Integer,
	iSegment1 As Integer,
	iEnd1 As Integer
)
```

```
public:
void AddListeningDimensionBendToBend(
	ElementId^ paramId, 
	double constraintDirCoordX, 
	double constraintDirCoordY, 
	int iSegment0, 
	int iEnd0, 
	int iSegment1, 
	int iEnd1
)
```

```
member AddListeningDimensionBendToBend : 
        paramId : ElementId * 
        constraintDirCoordX : float * 
        constraintDirCoordY : float * 
        iSegment0 : int * 
        iEnd0 : int * 
        iSegment1 : int * 
        iEnd1 : int -> unit 
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

iEnd0 Int32
:   End (0 or 1\) of the first segment.

iSegment1 Int32
:   Index of the second segment (0 to NumberOfSegments \- 1\).

iEnd1 Int32
:   End (0 or 1\) of the second segment.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | paramId is not the id of a shared parameter in the current document,  or its unit type is not Reinforcement\_Length, Angle or Number.  \-or\-  The length of the vector (constraintDirCoordX, constraintDirCoordY) is too close to zero.  \-or\-  iSegment0 is not between 0 and NumberOfSegments.  \-or\-  iEnd0 is neither 0 nor 1\.  \-or\-  iSegment1 is not between 0 and NumberOfSegments.  \-or\-  iEnd1 is neither 0 nor 1\. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks Each reference is at the outside of the bend, perpendicular to the specified segment. So the overall length of a shape with 5 segments might be defined by calling this function with iSegment0\=0, iEnd0\=0, iSegment1\=4, iEnd1\=1\. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarShapeDefinitionBySegments Class](7229fdba-1e8f-6cb7-e72e-0933e495ad62.htm) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
