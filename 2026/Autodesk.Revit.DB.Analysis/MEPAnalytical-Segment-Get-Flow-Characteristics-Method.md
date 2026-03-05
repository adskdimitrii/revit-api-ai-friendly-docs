# MEPAnalytical Segment Get Flow Characteristics Method

Source: https://www.revitapidocs.com/2026/b222de32-788b-c575-a42a-a28e1bbd1e47.htm

---

| MEPAnalytical Segment Get Flow Characteristics Method |
| --- |

Gets all flow characteristics of the segment. 
**Namespace:** [Autodesk.Revit.DB.Analysis](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public string GetFlowCharacteristics(
	Document doc
)
```

```
Public Function GetFlowCharacteristics ( 
	doc As Document
) As String
```

```
public:
String^ GetFlowCharacteristics(
	Document^ doc
)
```

```
member GetFlowCharacteristics : 
        doc : Document -> string 
```

#### Parameters

doc [Document](../Autodesk.Revit.DB/Document-Class.md)
:   The document of this segment.

#### Return Value

String 
All flow characteristics of the segment in one string, empty if all characteristics are undefined. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[MEPAnalyticalSegment Class](MEPAnalytical-Segment-Class.md) [Autodesk.Revit.DB.Analysis Namespace](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md)
