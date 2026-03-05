# Rebar Container Item Set From Curves(Rebar Style, Rebar Bar Type, Rebar Hook Type, Rebar Hook Type, XYZ, IList Curve , Rebar Termination Orientation, Rebar Termination Orientation, Boolean, Boolean) Method

Source: https://www.revitapidocs.com/2026/8330d442-2219-f5e3-bb78-4c6e32b2c951.htm

---

| Rebar Container Item Set From Curves(Rebar Style, Rebar Bar Type, Rebar Hook Type, Rebar Hook Type, XYZ, IList Curve , Rebar Termination Orientation, Rebar Termination Orientation, Boolean, Boolean) Method |
| --- |

  
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetFromCurves(
	RebarStyle style,
	RebarBarType barType,
	RebarHookType startHook,
	RebarHookType endHook,
	XYZ norm,
	IList<Curve> curves,
	RebarTerminationOrientation startHookOrient,
	RebarTerminationOrientation endHookOrient,
	bool useExistingShapeIfPossible,
	bool createNewShape
)
```

```
Public Sub SetFromCurves ( 
	style As RebarStyle,
	barType As RebarBarType,
	startHook As RebarHookType,
	endHook As RebarHookType,
	norm As XYZ,
	curves As IList(Of Curve),
	startHookOrient As RebarTerminationOrientation,
	endHookOrient As RebarTerminationOrientation,
	useExistingShapeIfPossible As Boolean,
	createNewShape As Boolean
)
```

```
public:
void SetFromCurves(
	RebarStyle style, 
	RebarBarType^ barType, 
	RebarHookType^ startHook, 
	RebarHookType^ endHook, 
	XYZ^ norm, 
	IList<Curve^>^ curves, 
	RebarTerminationOrientation startHookOrient, 
	RebarTerminationOrientation endHookOrient, 
	bool useExistingShapeIfPossible, 
	bool createNewShape
)
```

```
member SetFromCurves : 
        style : RebarStyle * 
        barType : RebarBarType * 
        startHook : RebarHookType * 
        endHook : RebarHookType * 
        norm : XYZ * 
        curves : IList<Curve> * 
        startHookOrient : RebarTerminationOrientation * 
        endHookOrient : RebarTerminationOrientation * 
        useExistingShapeIfPossible : bool * 
        createNewShape : bool -> unit 
```

#### Parameters

style [RebarStyle](a9ac65a6-29e6-25e5-caca-502e21385f47.htm)
barType [RebarBarType](Rebar-Bar-Type-Class.md)
startHook [RebarHookType](Rebar-Hook-Type-Class.md)
endHook [RebarHookType](Rebar-Hook-Type-Class.md)
norm [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)
curves IList [Curve](../Autodesk.Revit.DB/Curve-Class.md)
startHookOrient [RebarTerminationOrientation](Rebar-Termination-Orientation-Enumeration.md)
endHookOrient [RebarTerminationOrientation](Rebar-Termination-Orientation-Enumeration.md)
useExistingShapeIfPossible Boolean
createNewShape Boolean

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarContainerItem Class](Rebar-Container-Item-Class.md) [SetFromCurves Overload](Rebar-Container-Item-Set-From-Curves-Method.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
