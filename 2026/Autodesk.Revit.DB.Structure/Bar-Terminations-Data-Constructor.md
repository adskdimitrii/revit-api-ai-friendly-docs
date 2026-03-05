# Bar Terminations Data Constructor

Source: https://www.revitapidocs.com/2026/30435fe5-ba56-431c-27f4-58d586d16bc9.htm

---

| Bar Terminations Data Constructor |
| --- |

Creates a new instance of BarTerminationData with the default values. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public BarTerminationsData(
	Document document
)
```

```
Public Sub New ( 
	document As Document
)
```

```
public:
BarTerminationsData(
	Document^ document
)
```

```
new : 
        document : Document -> BarTerminationsData
```

#### Parameters

document [Document](../Autodesk.Revit.DB/Document-Class.md)
:   The document containing the hook type ids, end treatment ids and crank type ids.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[BarTerminationsData Class](Bar-Terminations-Data-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
