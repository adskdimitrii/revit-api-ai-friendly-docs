# Rebar Shape Terminations Data Termination Orientation At Start Property

Source: https://www.revitapidocs.com/2026/321e6e08-2fb0-68e2-b89a-8151f152e859.htm

---

| Rebar Shape Terminations Data Termination Orientation At Start Property |
| --- |

Identifies the orientation of the termination (e.g. hook, crank) at start. 

The default value is Left. 

  
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public RebarTerminationOrientation TerminationOrientationAtStart { get; set; }
```

```
Public Property TerminationOrientationAtStart As RebarTerminationOrientation
	Get
	Set
```

```
public:
property RebarTerminationOrientation TerminationOrientationAtStart {
	RebarTerminationOrientation get ();
	void set (RebarTerminationOrientation value);
}
```

```
member TerminationOrientationAtStart : RebarTerminationOrientation with get, set
```

#### Property Value

[RebarTerminationOrientation](Rebar-Termination-Orientation-Enumeration.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarShapeTerminationsData Class](Rebar-Shape-Terminations-Data-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
