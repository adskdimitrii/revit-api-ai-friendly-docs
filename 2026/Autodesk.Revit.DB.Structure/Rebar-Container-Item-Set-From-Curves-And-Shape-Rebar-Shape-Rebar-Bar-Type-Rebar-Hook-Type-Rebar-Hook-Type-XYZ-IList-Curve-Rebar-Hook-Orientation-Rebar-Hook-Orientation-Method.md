# Rebar Container Item Set From Curves And Shape(Rebar Shape, Rebar Bar Type, Rebar Hook Type, Rebar Hook Type, XYZ, IList Curve , Rebar Hook Orientation, Rebar Hook Orientation) Method

Source: https://www.revitapidocs.com/2026/1bf70fa9-9647-e168-c1bb-78bcdd7ba851.htm

---

| Rebar Container Item Set From Curves And Shape(Rebar Shape, Rebar Bar Type, Rebar Hook Type, Rebar Hook Type, XYZ, IList Curve , Rebar Hook Orientation, Rebar Hook Orientation) Method |
| --- |

**Note: This API is now obsolete.** 

  
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarContainerItem.SetFromCurvesAndShape(RebarShape rebarShape, RebarBarType barType, RebarHookType startHook, RebarHookType endHook, XYZ norm, IList<Curve> curves, RebarTerminationOrientation startHookOrient, RebarTerminationOrientation endHookOrient) instead.")]
public void SetFromCurvesAndShape(
	RebarShape rebarShape,
	RebarBarType barType,
	RebarHookType startHook,
	RebarHookType endHook,
	XYZ norm,
	IList<Curve> curves,
	RebarHookOrientation startHookOrient,
	RebarHookOrientation endHookOrient
)
```

```
<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarContainerItem.SetFromCurvesAndShape(RebarShape rebarShape, RebarBarType barType, RebarHookType startHook, RebarHookType endHook, XYZ norm, IList<Curve> curves, RebarTerminationOrientation startHookOrient, RebarTerminationOrientation endHookOrient) instead.")>
Public Sub SetFromCurvesAndShape ( 
	rebarShape As RebarShape,
	barType As RebarBarType,
	startHook As RebarHookType,
	endHook As RebarHookType,
	norm As XYZ,
	curves As IList(Of Curve),
	startHookOrient As RebarHookOrientation,
	endHookOrient As RebarHookOrientation
)
```

```
public:
[ObsoleteAttribute(L"This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarContainerItem.SetFromCurvesAndShape(RebarShape rebarShape, RebarBarType barType, RebarHookType startHook, RebarHookType endHook, XYZ norm, IList<Curve> curves, RebarTerminationOrientation startHookOrient, RebarTerminationOrientation endHookOrient) instead.")]
void SetFromCurvesAndShape(
	RebarShape^ rebarShape, 
	RebarBarType^ barType, 
	RebarHookType^ startHook, 
	RebarHookType^ endHook, 
	XYZ^ norm, 
	IList<Curve^>^ curves, 
	RebarHookOrientation startHookOrient, 
	RebarHookOrientation endHookOrient
)
```

```
[<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarContainerItem.SetFromCurvesAndShape(RebarShape rebarShape, RebarBarType barType, RebarHookType startHook, RebarHookType endHook, XYZ norm, IList<Curve> curves, RebarTerminationOrientation startHookOrient, RebarTerminationOrientation endHookOrient) instead.")>]
member SetFromCurvesAndShape : 
        rebarShape : RebarShape * 
        barType : RebarBarType * 
        startHook : RebarHookType * 
        endHook : RebarHookType * 
        norm : XYZ * 
        curves : IList<Curve> * 
        startHookOrient : RebarHookOrientation * 
        endHookOrient : RebarHookOrientation -> unit 
```

#### Parameters

rebarShape [RebarShape](Rebar-Shape-Class.md)
barType [RebarBarType](Rebar-Bar-Type-Class.md)
startHook [RebarHookType](Rebar-Hook-Type-Class.md)
endHook [RebarHookType](Rebar-Hook-Type-Class.md)
norm [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)
curves IList [Curve](../Autodesk.Revit.DB/Curve-Class.md)
startHookOrient [RebarHookOrientation](Rebar-Hook-Orientation-Enumeration.md)
endHookOrient [RebarHookOrientation](Rebar-Hook-Orientation-Enumeration.md)

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarContainerItem Class](Rebar-Container-Item-Class.md) [SetFromCurvesAndShape Overload](Rebar-Container-Item-Set-From-Curves-And-Shape-Method.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
