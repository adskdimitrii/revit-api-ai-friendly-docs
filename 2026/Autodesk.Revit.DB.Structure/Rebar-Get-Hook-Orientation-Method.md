# Rebar Get Hook Orientation Method

Source: https://www.revitapidocs.com/2026/0aabc992-1723-9f78-aff7-ef9760f8a64b.htm

---

| Rebar Get Hook Orientation Method |
| --- |

**Note: This API is now obsolete.** 

Returns the orientation of the termination's plane at the start or at the end of the rebar with respect to the orientation of the first or the last curve and the plane normal.
 The orientation it's the same for both hook and crank. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use Rebar.GetTerminationOrientation instead.")]
public RebarHookOrientation GetHookOrientation(
	int end
)
```

```
<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use Rebar.GetTerminationOrientation instead.")>
Public Function GetHookOrientation ( 
	end As Integer
) As RebarHookOrientation
```

```
public:
[ObsoleteAttribute(L"This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use Rebar.GetTerminationOrientation instead.")]
RebarHookOrientation GetHookOrientation(
	int end
)
```

```
[<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use Rebar.GetTerminationOrientation instead.")>]
member GetHookOrientation : 
        end : int -> RebarHookOrientation 
```

#### Parameters

end Int32
:   0 for the start termination, 1 for the end termination.

#### Return Value

[RebarHookOrientation](Rebar-Hook-Orientation-Enumeration.md) 
Value \= Right: The termination is on your right as you stand at the end of the bar,
 with the bar behind you, taking the bar's normal as "up."
 Value \= Left: The termination is on your left as you stand at the end of the bar,
 with the bar behind you, taking the bar's normal as "up." ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | end must be 0 or 1\. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Rebar Class](Rebar-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
