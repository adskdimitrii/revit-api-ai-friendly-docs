# Rebar Container Append Item From Curves(Rebar Style, Rebar Bar Type, Rebar Hook Type, Rebar Hook Type, XYZ, IList Curve , Rebar Hook Orientation, Rebar Hook Orientation, Boolean, Boolean) Method

Source: https://www.revitapidocs.com/2026/5e226c33-9073-1211-2ddb-8bd061b6ebf1.htm

---

| Rebar Container Append Item From Curves(Rebar Style, Rebar Bar Type, Rebar Hook Type, Rebar Hook Type, XYZ, IList Curve , Rebar Hook Orientation, Rebar Hook Orientation, Boolean, Boolean) Method |
| --- |

**Note: This API is now obsolete.** 

  
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarContainer.AppendItemFromCurves(RebarStyle style, RebarBarType barType, RebarHookType startHook, RebarHookType endHook, XYZ normal, IList<Curve> curves, RebarTerminationOrientation startHookOrient, RebarTerminationOrientation endHookOrient, bool useExistingShapeIfPossible, bool createNewShape) instead.")]
public RebarContainerItem AppendItemFromCurves(
	RebarStyle style,
	RebarBarType barType,
	RebarHookType startHook,
	RebarHookType endHook,
	XYZ normal,
	IList<Curve> curves,
	RebarHookOrientation startHookOrient,
	RebarHookOrientation endHookOrient,
	bool useExistingShapeIfPossible,
	bool createNewShape
)
```

```
<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarContainer.AppendItemFromCurves(RebarStyle style, RebarBarType barType, RebarHookType startHook, RebarHookType endHook, XYZ normal, IList<Curve> curves, RebarTerminationOrientation startHookOrient, RebarTerminationOrientation endHookOrient, bool useExistingShapeIfPossible, bool createNewShape) instead.")>
Public Function AppendItemFromCurves ( 
	style As RebarStyle,
	barType As RebarBarType,
	startHook As RebarHookType,
	endHook As RebarHookType,
	normal As XYZ,
	curves As IList(Of Curve),
	startHookOrient As RebarHookOrientation,
	endHookOrient As RebarHookOrientation,
	useExistingShapeIfPossible As Boolean,
	createNewShape As Boolean
) As RebarContainerItem
```

```
public:
[ObsoleteAttribute(L"This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarContainer.AppendItemFromCurves(RebarStyle style, RebarBarType barType, RebarHookType startHook, RebarHookType endHook, XYZ normal, IList<Curve> curves, RebarTerminationOrientation startHookOrient, RebarTerminationOrientation endHookOrient, bool useExistingShapeIfPossible, bool createNewShape) instead.")]
RebarContainerItem^ AppendItemFromCurves(
	RebarStyle style, 
	RebarBarType^ barType, 
	RebarHookType^ startHook, 
	RebarHookType^ endHook, 
	XYZ^ normal, 
	IList<Curve^>^ curves, 
	RebarHookOrientation startHookOrient, 
	RebarHookOrientation endHookOrient, 
	bool useExistingShapeIfPossible, 
	bool createNewShape
)
```

```
[<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarContainer.AppendItemFromCurves(RebarStyle style, RebarBarType barType, RebarHookType startHook, RebarHookType endHook, XYZ normal, IList<Curve> curves, RebarTerminationOrientation startHookOrient, RebarTerminationOrientation endHookOrient, bool useExistingShapeIfPossible, bool createNewShape) instead.")>]
member AppendItemFromCurves : 
        style : RebarStyle * 
        barType : RebarBarType * 
        startHook : RebarHookType * 
        endHook : RebarHookType * 
        normal : XYZ * 
        curves : IList<Curve> * 
        startHookOrient : RebarHookOrientation * 
        endHookOrient : RebarHookOrientation * 
        useExistingShapeIfPossible : bool * 
        createNewShape : bool -> RebarContainerItem 
```

#### Parameters

style [RebarStyle](a9ac65a6-29e6-25e5-caca-502e21385f47.htm)
barType [RebarBarType](Rebar-Bar-Type-Class.md)
startHook [RebarHookType](Rebar-Hook-Type-Class.md)
endHook [RebarHookType](Rebar-Hook-Type-Class.md)
normal [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)
curves IList [Curve](../Autodesk.Revit.DB/Curve-Class.md)
startHookOrient [RebarHookOrientation](Rebar-Hook-Orientation-Enumeration.md)
endHookOrient [RebarHookOrientation](Rebar-Hook-Orientation-Enumeration.md)
useExistingShapeIfPossible Boolean
createNewShape Boolean

#### Return Value

[RebarContainerItem](Rebar-Container-Item-Class.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarContainer Class](Rebar-Container-Class.md) [AppendItemFromCurves Overload](Rebar-Container-Append-Item-From-Curves-Method.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
