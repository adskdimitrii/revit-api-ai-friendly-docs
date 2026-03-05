# Rebar Coupler Error Enumeration

Source: https://www.revitapidocs.com/2026/36b8947f-6ee1-8f70-f2fc-ab52dd1afd90.htm

---

| Rebar Coupler Error Enumeration |
| --- |

Error states for the Rebar Coupler 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public enum RebarCouplerError
```

```
Public Enumeration RebarCouplerError
```

```
public enum class RebarCouplerError
```

```
type RebarCouplerError
```
![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Members 

| Member name | Value | Description |
| --- | --- | --- |
| ArcsHaveDifferentCenters | 16 | Cannot place rebar couplers on arcs with different centers. |
| ArcsHaveDifferentRadii | 15 | Cannot place rebar couplers on arcs with different radii. |
| ArcToStraightSegment | 17 | Cannot connect by coupler a straight segment with an arc segment. |
| BarSegementsAreNotParallel | 6 | The selected legs are not aligned. |
| BarSegmentsAreNotOnSameLine | 7 | The selected legs are not aligned. |
| BarSegmentSmallerThanEngagement | 13 | The selected leg is shorter than the bar engagement. |
| BarsNotTouching | 3 | The selected ends of the bars are too far apart. |
| BendingPlanesAreNotParallel | 18 | The bending planes of the connected bars are not parallel.  This will be returned when connecting two shape\-driven rebars whose bending planes are not parallel and the bar curves that need to be connected are not aligned. |
| CurvesOtherThanLine | 12 | Cannot place rebar couplers on circular legs. |
| DifferentLayout | 2 | The rebar sets have different numbers of bars. |
| InconsistentShape | 8 | One of the selected bars has an incorrect shape. |
| IncorrectEndTreatmentCoupler | 5 | The coupler cannot be placed at an end that already has a coupler. |
| IncorrectEndTreatmentCrank | 19 | The coupler cannot be placed at an end that already has a crank. |
| IncorrectEndTreatmentHook | 4 | The coupler cannot be placed at an end that already has a hook. |
| IncorrectInputData | 1 | Cannot place rebar coupler. |
| InvalidDiameter | 9 | The selected coupler type cannot be applied to the selected bar size(s). |
| ValidationSuccessfuly | 0 | Bars can be coupled |
| VaryingDistanceBetweenDistributionsBars | 14 | All the bars from the selected sets, which need to be connected, must be separated by the same distance. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
