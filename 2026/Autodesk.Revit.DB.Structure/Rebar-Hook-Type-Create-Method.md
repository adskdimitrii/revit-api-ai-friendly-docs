# Rebar Hook Type Create Method

Source: https://www.revitapidocs.com/2026/e113d22a-0e59-6642-e45d-2538a0d24bff.htm

---

| Rebar Hook Type Create Method |
| --- |

Creates a new RebarHookType in a document. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static RebarHookType Create(
	Document doc,
	double angle,
	double multiplier
)
```

```
Public Shared Function Create ( 
	doc As Document,
	angle As Double,
	multiplier As Double
) As RebarHookType
```

```
public:
static RebarHookType^ Create(
	Document^ doc, 
	double angle, 
	double multiplier
)
```

```
static member Create : 
        doc : Document * 
        angle : float * 
        multiplier : float -> RebarHookType 
```

#### Parameters

doc [Document](../Autodesk.Revit.DB/Document-Class.md)
angle Double
:   Determine the hook angle in radians of new RebarHookType. Must be greater than 0\.0174532925 (1 degree) and no more than PI (180 degree).

multiplier Double
:   Determine the straight line multiplier of new RebarHookType.

#### Return Value

[RebarHookType](Rebar-Hook-Type-Class.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given value for angle is not a number  \-or\-  The given value for multiplier is not a number |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | angle must be greater than 0\.0174532925 (1 degree) and no more than PI (180 degree).  \-or\-  multiplier must be greater than 0 and no more than 99\. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarHookType Class](Rebar-Hook-Type-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
