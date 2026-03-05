# Rebar Set Termination Orientation Method

Source: https://www.revitapidocs.com/2026/11032d46-bb5a-e4cf-6c15-813e8f890311.htm

---

| Rebar Set Termination Orientation Method |
| --- |

Sets the orientation of the termination's (e.g. hook, crank) plane at the start or at the end of the rebar with respect to the orientation of the first or the last curve and the plane normal. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetTerminationOrientation(
	int end,
	RebarTerminationOrientation terminationOrientation
)
```

```
Public Sub SetTerminationOrientation ( 
	end As Integer,
	terminationOrientation As RebarTerminationOrientation
)
```

```
public:
void SetTerminationOrientation(
	int end, 
	RebarTerminationOrientation terminationOrientation
)
```

```
member SetTerminationOrientation : 
        end : int * 
        terminationOrientation : RebarTerminationOrientation -> unit 
```

#### Parameters

end Int32
:   0 for the start termination, 1 for the end termination.

terminationOrientation [RebarTerminationOrientation](Rebar-Termination-Orientation-Enumeration.md)
:   Only two values are permitted: 

Value \= Right: The termination is on your right as you stand at the end of the bar,
 with the bar behind you, taking the bar's normal as "up." 

Value \= Left: The termination is on your left as you stand at the end of the bar,
 with the bar behind you, taking the bar's normal as "up."

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | end must be 0 or 1\.  \-or\-  A value passed for an enumeration argument is not a member of that enumeration |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Rebar Class](Rebar-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
