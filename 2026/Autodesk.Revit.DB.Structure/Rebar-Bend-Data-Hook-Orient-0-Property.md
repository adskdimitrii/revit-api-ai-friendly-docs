# Rebar Bend Data Hook Orient 0 Property

Source: https://www.revitapidocs.com/2026/53f6e950-f21f-a63c-a6cf-2420d37860e1.htm

---

| Rebar Bend Data Hook Orient 0 Property |
| --- |

**Note: This API is now obsolete.** 

Identifies the orientation of the termination (e.g. hook, crank) at the start.
 The default value is RebarTerminationOrientation::Left. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This property is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarBendData.TerminationOrientation0 instead.")]
public RebarHookOrientation HookOrient0 { get; set; }
```

```
<ObsoleteAttribute("This property is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarBendData.TerminationOrientation0 instead.")>
Public Property HookOrient0 As RebarHookOrientation
	Get
	Set
```

```
public:
[ObsoleteAttribute(L"This property is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarBendData.TerminationOrientation0 instead.")]
property RebarHookOrientation HookOrient0 {
	RebarHookOrientation get ();
	void set (RebarHookOrientation value);
}
```

```
[<ObsoleteAttribute("This property is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarBendData.TerminationOrientation0 instead.")>]
member HookOrient0 : RebarHookOrientation with get, set
```

#### Property Value

[RebarHookOrientation](Rebar-Hook-Orientation-Enumeration.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarBendData Class](Rebar-Bend-Data-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
