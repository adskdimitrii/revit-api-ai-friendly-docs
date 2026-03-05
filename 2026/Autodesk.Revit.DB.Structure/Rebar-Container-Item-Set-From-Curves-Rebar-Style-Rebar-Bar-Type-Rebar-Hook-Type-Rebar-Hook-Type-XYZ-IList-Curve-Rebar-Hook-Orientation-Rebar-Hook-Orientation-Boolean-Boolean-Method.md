# Rebar Container Item Set From Curves(Rebar Style, Rebar Bar Type, Rebar Hook Type, Rebar Hook Type, XYZ, IList Curve , Rebar Hook Orientation, Rebar Hook Orientation, Boolean, Boolean) Method

Source: https://www.revitapidocs.com/2026/c1c60114-a734-d73e-60db-8376e4110042.htm

---

| Rebar Container Item Set From Curves(Rebar Style, Rebar Bar Type, Rebar Hook Type, Rebar Hook Type, XYZ, IList Curve , Rebar Hook Orientation, Rebar Hook Orientation, Boolean, Boolean) Method |
| --- |

**Note: This API is now obsolete.** 

  
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarContainerItem.SetFromCurves(RebarStyle style, RebarBarType barType, RebarHookType startHook, RebarHookType endHook, XYZ norm, IList<Curve> curves, RebarTerminationOrientation startHookOrient, RebarTerminationOrientation endHookOrient, bool useExistingShapeIfPossible, bool createNewShape) instead.")]
public void SetFromCurves(
	RebarStyle style,
	RebarBarType barType,
	RebarHookType startHook,
	RebarHookType endHook,
	XYZ norm,
	IList<Curve> curves,
	RebarHookOrientation startHookOrient,
	RebarHookOrientation endHookOrient,
	bool useExistingShapeIfPossible,
	bool createNewShape
)
```

```
<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarContainerItem.SetFromCurves(RebarStyle style, RebarBarType barType, RebarHookType startHook, RebarHookType endHook, XYZ norm, IList<Curve> curves, RebarTerminationOrientation startHookOrient, RebarTerminationOrientation endHookOrient, bool useExistingShapeIfPossible, bool createNewShape) instead.")>
Public Sub SetFromCurves ( 
	style As RebarStyle,
	barType As RebarBarType,
	startHook As RebarHookType,
	endHook As RebarHookType,
	norm As XYZ,
	curves As IList(Of Curve),
	startHookOrient As RebarHookOrientation,
	endHookOrient As RebarHookOrientation,
	useExistingShapeIfPossible As Boolean,
	createNewShape As Boolean
)
```

```
public:
[ObsoleteAttribute(L"This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarContainerItem.SetFromCurves(RebarStyle style, RebarBarType barType, RebarHookType startHook, RebarHookType endHook, XYZ norm, IList<Curve> curves, RebarTerminationOrientation startHookOrient, RebarTerminationOrientation endHookOrient, bool useExistingShapeIfPossible, bool createNewShape) instead.")]
void SetFromCurves(
	RebarStyle style, 
	RebarBarType^ barType, 
	RebarHookType^ startHook, 
	RebarHookType^ endHook, 
	XYZ^ norm, 
	IList<Curve^>^ curves, 
	RebarHookOrientation startHookOrient, 
	RebarHookOrientation endHookOrient, 
	bool useExistingShapeIfPossible, 
	bool createNewShape
)
```

```
[<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarContainerItem.SetFromCurves(RebarStyle style, RebarBarType barType, RebarHookType startHook, RebarHookType endHook, XYZ norm, IList<Curve> curves, RebarTerminationOrientation startHookOrient, RebarTerminationOrientation endHookOrient, bool useExistingShapeIfPossible, bool createNewShape) instead.")>]
member SetFromCurves : 
        style : RebarStyle * 
        barType : RebarBarType * 
        startHook : RebarHookType * 
        endHook : RebarHookType * 
        norm : XYZ * 
        curves : IList<Curve> * 
        startHookOrient : RebarHookOrientation * 
        endHookOrient : RebarHookOrientation * 
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
startHookOrient [RebarHookOrientation](Rebar-Hook-Orientation-Enumeration.md)
endHookOrient [RebarHookOrientation](Rebar-Hook-Orientation-Enumeration.md)
useExistingShapeIfPossible Boolean
createNewShape Boolean

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarContainerItem Class](Rebar-Container-Item-Class.md) [SetFromCurves Overload](Rebar-Container-Item-Set-From-Curves-Method.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
