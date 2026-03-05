# Rebar Set Bar Hidden Status Method

Source: https://www.revitapidocs.com/2026/9f58c248-58b9-47b9-4367-ead7f53695d6.htm

---

| Rebar Set Bar Hidden Status Method |
| --- |

Sets the bar in this rebar set to be hidden or unhidden in the given view. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetBarHiddenStatus(
	View view,
	int barIndex,
	bool hide
)
```

```
Public Sub SetBarHiddenStatus ( 
	view As View,
	barIndex As Integer,
	hide As Boolean
)
```

```
public:
void SetBarHiddenStatus(
	View^ view, 
	int barIndex, 
	bool hide
)
```

```
member SetBarHiddenStatus : 
        view : View * 
        barIndex : int * 
        hide : bool -> unit 
```

#### Parameters

view [View](../Autodesk.Revit.DB/View-Class.md)
:   The view.

barIndex Int32
:   The index of the bar from this set.

hide Boolean
:   True to hide this bar in the view, false to unhide the bar.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | This rebar cannot have a presentation mode applied for view, as the view is not valid for rebar presentation,  or the orientation of the view matches the normal direction of the rebar element. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | barIndex should be in range \[ 0, NumberOfBarPositions\-1 ] and the bar at barIndex should be included. |
| [InapplicableDataException](dc1a6d15-8923-a1fe-722a-4e976634a519.htm) | This rebar element represents a single bar (the layout rule is Single). |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks Individual bars of a rebar set can be hidden in a view only
 if the presentation mode is RebarPresentationMode.Select.
 If that is not the presentation mode assigned for this set in the view,
 this method will also change it. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Rebar Class](Rebar-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
