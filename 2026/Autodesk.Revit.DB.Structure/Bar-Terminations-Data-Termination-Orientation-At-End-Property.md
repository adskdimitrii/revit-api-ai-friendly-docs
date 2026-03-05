# Bar Terminations Data Termination Orientation At End Property

Source: https://www.revitapidocs.com/2026/fa6b10af-eb3b-4e5c-a04f-f4b6032f45a7.htm

---

| Bar Terminations Data Termination Orientation At End Property |
| --- |

Identifies the orientation of the termination's (e.g. hook, crank) plane at the end of the bar with respect to the orientation of the last curve and the plane normal. 

Only two values are permitted: 

Value \= Right: The termination is on your right as you stand at the end of the bar, with the bar behind you, taking the bar's normal as "up." 

Value \= Left: The termination is on your left as you stand at the end of the bar, with the bar behind you, taking the bar's normal as "up." 

The default value is Left. 

  
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public RebarTerminationOrientation TerminationOrientationAtEnd { get; set; }
```

```
Public Property TerminationOrientationAtEnd As RebarTerminationOrientation
	Get
	Set
```

```
public:
property RebarTerminationOrientation TerminationOrientationAtEnd {
	RebarTerminationOrientation get ();
	void set (RebarTerminationOrientation value);
}
```

```
member TerminationOrientationAtEnd : RebarTerminationOrientation with get, set
```

#### Property Value

[RebarTerminationOrientation](Rebar-Termination-Orientation-Enumeration.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[BarTerminationsData Class](Bar-Terminations-Data-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
