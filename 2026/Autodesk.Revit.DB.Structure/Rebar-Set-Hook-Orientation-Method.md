# Rebar Set Hook Orientation Method

Source: https://www.revitapidocs.com/2026/d2bb944f-32dd-d6d0-142c-cba3dfd01e5f.htm

---

| Rebar Set Hook Orientation Method |
| --- |

**Note: This API is now obsolete.** 

Defines the orientation of the termination's plane at the start or at the end of the rebar with respect to the orientation of the first or the last curve and the plane normal.
 The orientation it's the same for both hook and crank. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use Rebar.SetTerminationOrientation instead.")]
public void SetHookOrientation(
	int end,
	RebarHookOrientation terminationOrientation
)
```

```
<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use Rebar.SetTerminationOrientation instead.")>
Public Sub SetHookOrientation ( 
	end As Integer,
	terminationOrientation As RebarHookOrientation
)
```

```
public:
[ObsoleteAttribute(L"This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use Rebar.SetTerminationOrientation instead.")]
void SetHookOrientation(
	int end, 
	RebarHookOrientation terminationOrientation
)
```

```
[<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use Rebar.SetTerminationOrientation instead.")>]
member SetHookOrientation : 
        end : int * 
        terminationOrientation : RebarHookOrientation -> unit 
```

#### Parameters

end Int32
:   0 for the start termination, 1 for the end termination.

terminationOrientation [RebarHookOrientation](Rebar-Hook-Orientation-Enumeration.md)
:   Only two values are permitted:
 Value \= Right: The termination is on your right as you stand at the end of the bar,
 with the bar behind you, taking the bar's normal as "up."
 Value \= Left: The termination is on your left as you stand at the end of the bar,
 with the bar behind you, taking the bar's normal as "up."

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | end must be 0 or 1\.  \-or\-  A value passed for an enumeration argument is not a member of that enumeration |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks If RebarShapeDefinesHooks property of ReinforcementSettings is true (non\-European shapes), SetTerminationOrientation method does nothing. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Rebar Class](Rebar-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
