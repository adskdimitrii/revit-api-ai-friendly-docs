# Rebar Container Append Item From Curves And Shape(Rebar Shape, Rebar Bar Type, Rebar Hook Type, Rebar Hook Type, XYZ, IList Curve , Rebar Termination Orientation, Rebar Termination Orientation) Method

Source: https://www.revitapidocs.com/2026/02e34460-f53b-3cd1-71ba-74232d66080b.htm

---

| Rebar Container Append Item From Curves And Shape(Rebar Shape, Rebar Bar Type, Rebar Hook Type, Rebar Hook Type, XYZ, IList Curve , Rebar Termination Orientation, Rebar Termination Orientation) Method |
| --- |

  
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public RebarContainerItem AppendItemFromCurvesAndShape(
	RebarShape rebarShape,
	RebarBarType barType,
	RebarHookType startHook,
	RebarHookType endHook,
	XYZ normal,
	IList<Curve> curves,
	RebarTerminationOrientation startHookOrient,
	RebarTerminationOrientation endHookOrient
)
```

```
Public Function AppendItemFromCurvesAndShape ( 
	rebarShape As RebarShape,
	barType As RebarBarType,
	startHook As RebarHookType,
	endHook As RebarHookType,
	normal As XYZ,
	curves As IList(Of Curve),
	startHookOrient As RebarTerminationOrientation,
	endHookOrient As RebarTerminationOrientation
) As RebarContainerItem
```

```
public:
RebarContainerItem^ AppendItemFromCurvesAndShape(
	RebarShape^ rebarShape, 
	RebarBarType^ barType, 
	RebarHookType^ startHook, 
	RebarHookType^ endHook, 
	XYZ^ normal, 
	IList<Curve^>^ curves, 
	RebarTerminationOrientation startHookOrient, 
	RebarTerminationOrientation endHookOrient
)
```

```
member AppendItemFromCurvesAndShape : 
        rebarShape : RebarShape * 
        barType : RebarBarType * 
        startHook : RebarHookType * 
        endHook : RebarHookType * 
        normal : XYZ * 
        curves : IList<Curve> * 
        startHookOrient : RebarTerminationOrientation * 
        endHookOrient : RebarTerminationOrientation -> RebarContainerItem 
```

#### Parameters

rebarShape [RebarShape](Rebar-Shape-Class.md)
barType [RebarBarType](Rebar-Bar-Type-Class.md)
startHook [RebarHookType](Rebar-Hook-Type-Class.md)
endHook [RebarHookType](Rebar-Hook-Type-Class.md)
normal [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)
curves IList [Curve](../Autodesk.Revit.DB/Curve-Class.md)
startHookOrient [RebarTerminationOrientation](Rebar-Termination-Orientation-Enumeration.md)
endHookOrient [RebarTerminationOrientation](Rebar-Termination-Orientation-Enumeration.md)

#### Return Value

[RebarContainerItem](Rebar-Container-Item-Class.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarContainer Class](Rebar-Container-Class.md) [AppendItemFromCurvesAndShape Overload](Rebar-Container-Append-Item-From-Curves-And-Shape-Method.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
