# Rebar Shape Definition By Segments Set Segment As 180Degree Bend(Int 32, Element Id, Boolean) Method

Source: https://www.revitapidocs.com/2026/146fe862-c330-b686-bda5-2cc1a2422eb3.htm

---

| Rebar Shape Definition By Segments Set Segment As 180Degree Bend(Int 32, Element Id, Boolean) Method |
| --- |

Indicate that a segment is a "virtual" segment introduced to describe a 180\-degree bend. The radius of the bend will be driven by radiusParam. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetSegmentAs180DegreeBend(
	int iSegment,
	ElementId paramId,
	bool measureToOutsideOfBend
)
```

```
Public Sub SetSegmentAs180DegreeBend ( 
	iSegment As Integer,
	paramId As ElementId,
	measureToOutsideOfBend As Boolean
)
```

```
public:
void SetSegmentAs180DegreeBend(
	int iSegment, 
	ElementId^ paramId, 
	bool measureToOutsideOfBend
)
```

```
member SetSegmentAs180DegreeBend : 
        iSegment : int * 
        paramId : ElementId * 
        measureToOutsideOfBend : bool -> unit 
```

#### Parameters

iSegment Int32
:   Index of the segment (0 to NumberOfSegments \- 1\).

paramId [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
:   Id of a parameter to drive the radius.
 To obtain the id of a shared parameter,
 call RebarShape.GetElementIdForExternalDefinition().

measureToOutsideOfBend Boolean
:   Choose between two possibilities for the references of the radius dimension.
 If true, measure to the exterior face of the bar. If false, measure to the interior face.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | iSegment is not between 0 and NumberOfSegments.  \-or\-  paramId is not the id of a shared parameter in the current document,  or its unit type is not Reinforcement\_Length, Angle or Number. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarShapeDefinitionBySegments Class](7229fdba-1e8f-6cb7-e72e-0933e495ad62.htm) [SetSegmentAs180DegreeBend Overload](2144f300-4c4e-bda2-13ea-7ea4b5adf1c6.htm) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
