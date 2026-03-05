# Rebar Container Item Set Hook Orientation Method

Source: https://www.revitapidocs.com/2026/3aea334b-d5ad-f2bc-d85d-31ceb5c2fa6b.htm

---

| Rebar Container Item Set Hook Orientation Method |
| --- |

**Note: This API is now obsolete.** 

Sets the orientation of the hook plane at the start or at the end of the rebar with respect to the orientation of the first or the last curve and the plane normal. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarContainerItem.SetTerminationOrientation(int end, RebarTerminationOrientation hookOrientation) instead.")]
public void SetHookOrientation(
	int end,
	RebarHookOrientation hookOrientation
)
```

```
<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarContainerItem.SetTerminationOrientation(int end, RebarTerminationOrientation hookOrientation) instead.")>
Public Sub SetHookOrientation ( 
	end As Integer,
	hookOrientation As RebarHookOrientation
)
```

```
public:
[ObsoleteAttribute(L"This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarContainerItem.SetTerminationOrientation(int end, RebarTerminationOrientation hookOrientation) instead.")]
void SetHookOrientation(
	int end, 
	RebarHookOrientation hookOrientation
)
```

```
[<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarContainerItem.SetTerminationOrientation(int end, RebarTerminationOrientation hookOrientation) instead.")>]
member SetHookOrientation : 
        end : int * 
        hookOrientation : RebarHookOrientation -> unit 
```

#### Parameters

end Int32
:   0 for the start hook, 1 for the end hook.

hookOrientation [RebarHookOrientation](Rebar-Hook-Orientation-Enumeration.md)
:   Only two values are permitted:
 Value \= Right: The hook is on your right as you stand at the end of the bar,
 with the bar behind you, taking the bar's normal as "up."
 Value \= Left: The hook is on your left as you stand at the end of the bar,
 with the bar behind you, taking the bar's normal as "up."

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | end must be 0 or 1\.  \-or\-  A value passed for an enumeration argument is not a member of that enumeration |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks If RebarShapeDefinesHooks property of ReinforcementSettings is true (non\-European shapes), setHookOrientation method does nothing. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarContainerItem Class](Rebar-Container-Item-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
