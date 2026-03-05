# Rebar Shape Definition By Segments Remove Parameter From Segment Method

Source: https://www.revitapidocs.com/2026/07b27988-4b6c-9449-c2f1-16da13b042ca.htm

---

| Rebar Shape Definition By Segments Remove Parameter From Segment Method |
| --- |

Remove constraints from a segment. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void RemoveParameterFromSegment(
	int iSegment,
	ElementId paramId
)
```

```
Public Sub RemoveParameterFromSegment ( 
	iSegment As Integer,
	paramId As ElementId
)
```

```
public:
void RemoveParameterFromSegment(
	int iSegment, 
	ElementId^ paramId
)
```

```
member RemoveParameterFromSegment : 
        iSegment : int * 
        paramId : ElementId -> unit 
```

#### Parameters

iSegment Int32
:   Index of the segment (0 to NumberOfSegments \- 1\).

paramId [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
:   Id of a parameter driving one or more constraints.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | iSegment is not between 0 and NumberOfSegments.  \-or\-  paramId is not the id of a shared parameter in the current document,  or its unit type is not Reinforcement\_Length, Angle or Number. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks This reverses the effect of any AddConstraint and SetSegmentAs180DegreeBend operations involving the specified segment and parameter. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarShapeDefinitionBySegments Class](7229fdba-1e8f-6cb7-e72e-0933e495ad62.htm) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
