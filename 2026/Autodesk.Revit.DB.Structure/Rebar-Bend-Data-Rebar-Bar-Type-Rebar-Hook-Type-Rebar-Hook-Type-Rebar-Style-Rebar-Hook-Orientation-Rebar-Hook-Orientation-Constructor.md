# Rebar Bend Data(Rebar Bar Type, Rebar Hook Type, Rebar Hook Type, Rebar Style, Rebar Hook Orientation, Rebar Hook Orientation) Constructor

Source: https://www.revitapidocs.com/2026/16e0ceff-fb53-cee7-c49d-8bbd85151869.htm

---

| Rebar Bend Data(Rebar Bar Type, Rebar Hook Type, Rebar Hook Type, Rebar Style, Rebar Hook Orientation, Rebar Hook Orientation) Constructor |
| --- |

**Note: This API is now obsolete.** 

Constructs a new RebarBendData using the bar type, hook types, style and orientation values. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This constructor is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarBendData(RebarBarType barType, RebarStyle style, BarTerminationsData barTerminationsData);")]
public RebarBendData(
	RebarBarType barType,
	RebarHookType hookType0,
	RebarHookType hookType1,
	RebarStyle style,
	RebarHookOrientation terminationOrientation0,
	RebarHookOrientation terminationOrientation1
)
```

```
<ObsoleteAttribute("This constructor is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarBendData(RebarBarType barType, RebarStyle style, BarTerminationsData barTerminationsData);")>
Public Sub New ( 
	barType As RebarBarType,
	hookType0 As RebarHookType,
	hookType1 As RebarHookType,
	style As RebarStyle,
	terminationOrientation0 As RebarHookOrientation,
	terminationOrientation1 As RebarHookOrientation
)
```

```
public:
[ObsoleteAttribute(L"This constructor is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarBendData(RebarBarType barType, RebarStyle style, BarTerminationsData barTerminationsData);")]
RebarBendData(
	RebarBarType^ barType, 
	RebarHookType^ hookType0, 
	RebarHookType^ hookType1, 
	RebarStyle style, 
	RebarHookOrientation terminationOrientation0, 
	RebarHookOrientation terminationOrientation1
)
```

```
[<ObsoleteAttribute("This constructor is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarBendData(RebarBarType barType, RebarStyle style, BarTerminationsData barTerminationsData);")>]
new : 
        barType : RebarBarType * 
        hookType0 : RebarHookType * 
        hookType1 : RebarHookType * 
        style : RebarStyle * 
        terminationOrientation0 : RebarHookOrientation * 
        terminationOrientation1 : RebarHookOrientation -> RebarBendData
```

#### Parameters

barType [RebarBarType](Rebar-Bar-Type-Class.md)
:   The RebarBarType.

hookType0 [RebarHookType](Rebar-Hook-Type-Class.md)
:   The RebarHookType for the start. Can be .

hookType1 [RebarHookType](Rebar-Hook-Type-Class.md)
:   The RebarHookType for the end. Can be .

style [RebarStyle](a9ac65a6-29e6-25e5-caca-502e21385f47.htm)
:   The style.

terminationOrientation0 [RebarHookOrientation](Rebar-Hook-Orientation-Enumeration.md)
:   The termination orientation for the start.

terminationOrientation1 [RebarHookOrientation](Rebar-Hook-Orientation-Enumeration.md)
:   The termination orientation for the end.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarBendData Class](Rebar-Bend-Data-Class.md) [RebarBendData Overload](Rebar-Bend-Data-Constructor.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
