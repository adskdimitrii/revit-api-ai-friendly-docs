# MEPAnalytical Segment Get Flow Convergence Characteristic Method

Source: https://www.revitapidocs.com/2026/b340bcd8-2fe2-b3c0-a1ca-0182375b22c1.htm

---

| MEPAnalytical Segment Get Flow Convergence Characteristic Method |
| --- |

Gets the flow convergence characteristic of the segment. 
**Namespace:** [Autodesk.Revit.DB.Analysis](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public FlowConvergenceCharacteristic GetFlowConvergenceCharacteristic(
	Document doc,
	out FlowPositionCharacteristic outPosition
)
```

```
Public Function GetFlowConvergenceCharacteristic ( 
	doc As Document,
	<OutAttribute> ByRef outPosition As FlowPositionCharacteristic
) As FlowConvergenceCharacteristic
```

```
public:
FlowConvergenceCharacteristic GetFlowConvergenceCharacteristic(
	Document^ doc, 
	[OutAttribute] FlowPositionCharacteristic% outPosition
)
```

```
member GetFlowConvergenceCharacteristic : 
        doc : Document * 
        outPosition : FlowPositionCharacteristic byref -> FlowConvergenceCharacteristic 
```

#### Parameters

doc [Document](../Autodesk.Revit.DB/Document-Class.md)
:   The document of this segment.

outPosition [FlowPositionCharacteristic](Flow-Position-Characteristic-Enumeration.md)
:   The acquired flow position characteristic of the segment, undefined if the convergence characteristic is undefined.

#### Return Value

[FlowConvergenceCharacteristic](Flow-Convergence-Characteristic-Enumeration.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[MEPAnalyticalSegment Class](MEPAnalytical-Segment-Class.md) [Autodesk.Revit.DB.Analysis Namespace](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md)
