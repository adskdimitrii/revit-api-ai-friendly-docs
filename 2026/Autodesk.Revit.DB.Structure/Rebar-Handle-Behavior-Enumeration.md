# Rebar Handle Behavior Enumeration

Source: https://www.revitapidocs.com/2026/abd1f2f7-1fe1-14a0-4780-9e992324975f.htm

---

| Rebar Handle Behavior Enumeration |
| --- |

Different behaviors that can be applied to a RebarConstrainedHandle.
 Depending on the behavior, the RebarConstrainedHandle plane is situated in a different location
 All the data in constraints for a RebarConstrainedHandle with a specific behavior are relative to this plane. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public enum RebarHandleBehavior
```

```
Public Enumeration RebarHandleBehavior
```

```
public enum class RebarHandleBehavior
```

```
type RebarHandleBehavior
```
![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Members 

| Member name | Value | Description |
| --- | --- | --- |
| CrankAtEndOnBarSegment | 13 | The behavior can be set to an end of bar handle only if the bar has crank at end.  The plane of a RebarConstrainedHandle with behavior is situated at (crank length \+ crank angled length) distance from where the bar (with crank) ends. It's also the same as the default one. |
| CrankAtEndOnCrankEnd | 15 | The behavior can be set to an end of bar handle only if the bar has crank at end.  The plane of a RebarConstrainedHandle with behavior is situated exactly where the bar (with crank) ends. |
| CrankAtEndOnCrankSegment | 14 | The behavior can be set to an end of bar handle only if the bar has crank at end.  The plane of a RebarConstrainedHandle with behavior is situated at a crank length distance from where the bar (with crank) ends. |
| CrankAtStartOnBarSegment | 10 | The behavior can be set to a start of bar handle only if the bar has crank at start.  The plane of a RebarConstrainedHandle with behavior is situated at (crank length \+ crank angled length) distance from where the bar (with crank) ends. It's also the same as the default one. |
| CrankAtStartOnCrankEnd | 12 | The behavior can be set to a start of bar handle only if the bar has crank at start.  The plane of a RebarConstrainedHandle with behavior is situated exactly where the bar (with crank) ends. |
| CrankAtStartOnCrankSegment | 11 | The behavior can be set to a start of bar handle only if the bar has crank at start.  The plane of a RebarConstrainedHandle with behavior is situated at a crank length distance from where the bar (with crank) ends. |
| Default | 0 | Represents the default behavior of a RebarConstrainedHandle. |
| SpliceConnectedEndOnEnd1Position | 4 | The behavior can be set to a StartOfBar or EndOfBar RebarConstrainedHandle of a bar that is part of splice. On this RebarConstrainedHandle is a ToOtherRebar constraint whose target is the other bar involved in splice  The RebarConstrainedHandle's plane in the same position as the splice plane for End1\. It is located on the other bar's end that is involved in splice.  If a constraint for a handle with this behavior is set as preferred, it will be set a constraint for the RebarConstrainedHandle that represent the other bar's end that is involved in splice (all relevant data  are changed so that the offset is kept). |
| SpliceConnectedEndOnEnd2Position | 6 | The behavior can be set to a StartOfBar or EndOfBar RebarConstrainedHandle of a bar that is part of splice. On this RebarConstrainedHandle is a ToOtherRebar constraint whose target is the other bar involved in splice  The RebarConstrainedHandle's plane in the same position as the splice plane for End2\. It is located at a (lapLength \+ staggerLength) distance from the other bar's end that is involved in splice.  If a constraint for a handle with this behavior is set as preferred, it will be set a constraint for the RebarConstrainedHandle that represent the other bar's end that is involved in splice (all relevant data  are changed so that the offset is kept). |
| SpliceConnectedEndOnMiddlePosition | 5 | The behavior can be set to a StartOfBar or EndOfBar RebarConstrainedHandle of a bar that is part of splice. On this RebarConstrainedHandle is a ToOtherRebar constraint whose target is the other bar involved in splice  The RebarConstrainedHandle's plane in the same position as the splice plane for Middle. It is located at a (lapLength \+ staggerLength)/2 distance from the other bar's end that is involved in splice.  If a constraint for a handle with this behavior is set as preferred, it will be set a constraint for the RebarConstrainedHandle that represent the other bar's end that is involved in splice (all relevant data  are changed so that the offset is kept). |
| SpliceEdge | 9 | The behavior can be set to an edge segment that is connected to the other rebar of splice.  The plane of a RebarConstrainedHandle with behavior is the same as the default one.  If a constraint for a handle with this behavior is set as preferred, it will be set a constraint for the edge segment of the bar that is part of splice and don't have a ToOtherRebar constraint  to another bar in chain. |
| SpliceMainEndOnEnd1Position | 1 | The behavior can be set to a StartOfBar or EndOfBar RebarConstrainedHandle of a bar that is part of splice. On the connected bar there is a ToOtherRebar constraint whose target is the current rebar.  The RebarConstrainedHandle's plane in the same position as the splice plane for End1\. It goes through the bar's end. |
| SpliceMainEndOnEnd2Position | 3 | The behavior can be set to a StartOfBar or EndOfBar RebarConstrainedHandle of a bar that is part of splice. On the connected bar there is a ToOtherRebar constraint whose target is the current rebar.  The RebarConstrainedHandle's plane in the same position as the splice plane for End2\. It is located at a (lapLength \+ staggerLength)/2 distance from the RebarConstrainedHandle with the default behavior.  If a constraint for a handle with this behavior is set as preferred, it will be set a constraint for the RebarConstrainedHandle with default behaviour (all relevant data are changed so that the offset is kept). |
| SpliceMainEndOnMiddlePosition | 2 | The behavior can be set to a StartOfBar or EndOfBar RebarConstrainedHandle of a bar that is part of splice. On the connected bar there is a ToOtherRebar constraint whose target is the current rebar.  The RebarConstrainedHandle's plane in the same position as the splice plane for Middle. It is located at a (lapLength \+ staggerLength)/2 distance from the RebarConstrainedHandle with the default behavior.  If a constraint for a handle with this behavior is set as preferred, it will be set a constraint for the RebarConstrainedHandle with default behaviour (all relevant data are changed so that the offset is kept). |
| SpliceOutOfPlaneExtentOnSpliceSetExtent | 8 | The behavior can be set to a OutOfPlaneExtent RebarConstrainedHandle of a bar that is part of splice.  If we are looking at the extents of the entire set this RebarConstrainedHandle's plane is exactly on the set extents.  If a constraint for a handle with this behavior is set as preferred, it will be set a constraint for the OutOfPlaneExtent RebarConstrainedHandle of the first bar in splice chain (all relevant data  are changed so that the offset is kept). |
| SpliceRebarPlaneOnSpliceSetExtent | 7 | The behavior can be set to a RebarPlane RebarConstrainedHandle of a bar that is part of splice.  If we are looking at the extents of the entire set this RebarConstrainedHandle's plane is exactly on the set extents.  If a constraint for a handle with this behavior is set as preferred, it will be set a constraint for the RebarPlane RebarConstrainedHandle of the first bar in splice chain (all relevant data  are changed so that the offset is kept). |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
