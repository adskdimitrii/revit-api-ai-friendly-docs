# Rebar Bend Data(Rebar Bar Type, Rebar Style, Bar Terminations Data) Constructor

Source: https://www.revitapidocs.com/2026/5f400204-97a0-5f92-54b7-932bf7431db5.htm

---

| Rebar Bend Data(Rebar Bar Type, Rebar Style, Bar Terminations Data) Constructor |
| --- |

Constructs a new RebarBendData using the bar type, style and termination's values. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public RebarBendData(
	RebarBarType barType,
	RebarStyle style,
	BarTerminationsData barTerminationsData
)
```

```
Public Sub New ( 
	barType As RebarBarType,
	style As RebarStyle,
	barTerminationsData As BarTerminationsData
)
```

```
public:
RebarBendData(
	RebarBarType^ barType, 
	RebarStyle style, 
	BarTerminationsData^ barTerminationsData
)
```

```
new : 
        barType : RebarBarType * 
        style : RebarStyle * 
        barTerminationsData : BarTerminationsData -> RebarBendData
```

#### Parameters

barType [RebarBarType](Rebar-Bar-Type-Class.md)
:   The RebarBarType.

style [RebarStyle](a9ac65a6-29e6-25e5-caca-502e21385f47.htm)
:   The style.

barTerminationsData [BarTerminationsData](Bar-Terminations-Data-Class.md)
:   The bar terminaions data.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarBendData Class](Rebar-Bend-Data-Class.md) [RebarBendData Overload](Rebar-Bend-Data-Constructor.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
