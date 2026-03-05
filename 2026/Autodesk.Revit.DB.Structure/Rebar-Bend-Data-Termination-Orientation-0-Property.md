# Rebar Bend Data Termination Orientation 0 Property

Source: https://www.revitapidocs.com/2026/fb7ea0ca-d147-b43c-5fb3-f620a05d4994.htm

---

| Rebar Bend Data Termination Orientation 0 Property |
| --- |

Identifies he orientation of the termination (e.g. hook, crank) at the start.
 The default value is RebarTerminationOrientation::Left. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public RebarTerminationOrientation TerminationOrientation0 { get; set; }
```

```
Public Property TerminationOrientation0 As RebarTerminationOrientation
	Get
	Set
```

```
public:
property RebarTerminationOrientation TerminationOrientation0 {
	RebarTerminationOrientation get ();
	void set (RebarTerminationOrientation value);
}
```

```
member TerminationOrientation0 : RebarTerminationOrientation with get, set
```

#### Property Value

[RebarTerminationOrientation](Rebar-Termination-Orientation-Enumeration.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarBendData Class](Rebar-Bend-Data-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
