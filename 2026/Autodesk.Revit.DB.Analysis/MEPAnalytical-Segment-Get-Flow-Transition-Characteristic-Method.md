# MEPAnalytical Segment Get Flow Transition Characteristic Method

Source: https://www.revitapidocs.com/2026/4400a9dc-c405-dcd4-e1c8-814647b943e7.htm

---

| MEPAnalytical Segment Get Flow Transition Characteristic Method |
| --- |

Gets the flow transition characteristic of the segment. 
**Namespace:** [Autodesk.Revit.DB.Analysis](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public FlowTransitionCharacteristic GetFlowTransitionCharacteristic(
	Document doc
)
```

```
Public Function GetFlowTransitionCharacteristic ( 
	doc As Document
) As FlowTransitionCharacteristic
```

```
public:
FlowTransitionCharacteristic GetFlowTransitionCharacteristic(
	Document^ doc
)
```

```
member GetFlowTransitionCharacteristic : 
        doc : Document -> FlowTransitionCharacteristic 
```

#### Parameters

doc [Document](../Autodesk.Revit.DB/Document-Class.md)
:   The document of this segment.

#### Return Value

[FlowTransitionCharacteristic](Flow-Transition-Characteristic-Enumeration.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[MEPAnalyticalSegment Class](MEPAnalytical-Segment-Class.md) [Autodesk.Revit.DB.Analysis Namespace](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md)
