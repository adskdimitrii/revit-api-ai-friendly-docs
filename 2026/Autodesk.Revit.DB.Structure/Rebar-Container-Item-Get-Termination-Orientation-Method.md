# Rebar Container Item Get Termination Orientation Method

Source: https://www.revitapidocs.com/2026/9e334540-a122-5d54-2e67-08fb6aecd4a3.htm

---

| Rebar Container Item Get Termination Orientation Method |
| --- |

Gets the orientation of the hook plane at the start or at the end of the rebar with respect to the orientation of the first or the last curve and the plane normal. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public RebarTerminationOrientation GetTerminationOrientation(
	int end
)
```

```
Public Function GetTerminationOrientation ( 
	end As Integer
) As RebarTerminationOrientation
```

```
public:
RebarTerminationOrientation GetTerminationOrientation(
	int end
)
```

```
member GetTerminationOrientation : 
        end : int -> RebarTerminationOrientation 
```

#### Parameters

end Int32
:   0 for the start hook, 1 for the end hook.

#### Return Value

[RebarTerminationOrientation](Rebar-Termination-Orientation-Enumeration.md) 
Returns the orientation of the hook plane at the start or at the end of the rebar with respect to the orientation of the first or the last curve and the plane normal. 

Value \= Right: The hook is on your right as you stand at the end of the bar,
 with the bar behind you, taking the bar's normal as "up." 

Value \= Left: The hook is on your left as you stand at the end of the bar,
 with the bar behind you, taking the bar's normal as "up." 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | end must be 0 or 1\. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarContainerItem Class](Rebar-Container-Item-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
