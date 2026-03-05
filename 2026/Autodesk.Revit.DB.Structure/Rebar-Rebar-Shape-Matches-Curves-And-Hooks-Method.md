# Rebar Rebar Shape Matches Curves And Hooks Method

Source: https://www.revitapidocs.com/2026/16036dad-204c-47fa-9ce7-090e964a70d5.htm

---

| Rebar Rebar Shape Matches Curves And Hooks Method |
| --- |

**Note: This API is now obsolete.** 

  
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarShape.RebarShapeMatchesCurvesAndTerminationsData(RebarShape rebarShape, RebarBarType barType, XYZ norm, IList<Curve> curves, BarTerminationsData barTerminationsData) instead.")]
public static bool RebarShapeMatchesCurvesAndHooks(
	RebarShape rebarShape,
	RebarBarType barType,
	XYZ norm,
	IList<Curve> curves,
	RebarHookType startHook,
	RebarHookType endHook,
	RebarHookOrientation startHookOrient,
	RebarHookOrientation endHookOrient
)
```

```
<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarShape.RebarShapeMatchesCurvesAndTerminationsData(RebarShape rebarShape, RebarBarType barType, XYZ norm, IList<Curve> curves, BarTerminationsData barTerminationsData) instead.")>
Public Shared Function RebarShapeMatchesCurvesAndHooks ( 
	rebarShape As RebarShape,
	barType As RebarBarType,
	norm As XYZ,
	curves As IList(Of Curve),
	startHook As RebarHookType,
	endHook As RebarHookType,
	startHookOrient As RebarHookOrientation,
	endHookOrient As RebarHookOrientation
) As Boolean
```

```
public:
[ObsoleteAttribute(L"This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarShape.RebarShapeMatchesCurvesAndTerminationsData(RebarShape rebarShape, RebarBarType barType, XYZ norm, IList<Curve> curves, BarTerminationsData barTerminationsData) instead.")]
static bool RebarShapeMatchesCurvesAndHooks(
	RebarShape^ rebarShape, 
	RebarBarType^ barType, 
	XYZ^ norm, 
	IList<Curve^>^ curves, 
	RebarHookType^ startHook, 
	RebarHookType^ endHook, 
	RebarHookOrientation startHookOrient, 
	RebarHookOrientation endHookOrient
)
```

```
[<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarShape.RebarShapeMatchesCurvesAndTerminationsData(RebarShape rebarShape, RebarBarType barType, XYZ norm, IList<Curve> curves, BarTerminationsData barTerminationsData) instead.")>]
static member RebarShapeMatchesCurvesAndHooks : 
        rebarShape : RebarShape * 
        barType : RebarBarType * 
        norm : XYZ * 
        curves : IList<Curve> * 
        startHook : RebarHookType * 
        endHook : RebarHookType * 
        startHookOrient : RebarHookOrientation * 
        endHookOrient : RebarHookOrientation -> bool 
```

#### Parameters

rebarShape [RebarShape](Rebar-Shape-Class.md)
barType [RebarBarType](Rebar-Bar-Type-Class.md)
norm [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)
curves IList [Curve](../Autodesk.Revit.DB/Curve-Class.md)
startHook [RebarHookType](Rebar-Hook-Type-Class.md)
endHook [RebarHookType](Rebar-Hook-Type-Class.md)
startHookOrient [RebarHookOrientation](Rebar-Hook-Orientation-Enumeration.md)
endHookOrient [RebarHookOrientation](Rebar-Hook-Orientation-Enumeration.md)

#### Return Value

Boolean ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Rebar Class](Rebar-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
