# Rebar Create From Curves(Document, Rebar Style, Rebar Bar Type, Rebar Hook Type, Rebar Hook Type, Element, XYZ, IList Curve , Rebar Hook Orientation, Rebar Hook Orientation, Boolean, Boolean) Method

Source: https://www.revitapidocs.com/2026/b020c9d5-6026-b9fa-7e23-f6a7ec2cede3.htm

---

| Rebar Create From Curves(Document, Rebar Style, Rebar Bar Type, Rebar Hook Type, Rebar Hook Type, Element, XYZ, IList Curve , Rebar Hook Orientation, Rebar Hook Orientation, Boolean, Boolean) Method |
| --- |

**Note: This API is now obsolete.** 

  
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use Rebar.CreateFromCurves(Document doc, RebarStyle style, RebarBarType barType, Element host, XYZ norm, IList<Curve> curves, BarTerminationsData barTerminationsData, bool useExistingShapeIfPossible, bool createNewShape) instead.")]
public static Rebar CreateFromCurves(
	Document doc,
	RebarStyle style,
	RebarBarType barType,
	RebarHookType startHook,
	RebarHookType endHook,
	Element host,
	XYZ norm,
	IList<Curve> curves,
	RebarHookOrientation startHookOrient,
	RebarHookOrientation endHookOrient,
	bool useExistingShapeIfPossible,
	bool createNewShape
)
```

```
<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use Rebar.CreateFromCurves(Document doc, RebarStyle style, RebarBarType barType, Element host, XYZ norm, IList<Curve> curves, BarTerminationsData barTerminationsData, bool useExistingShapeIfPossible, bool createNewShape) instead.")>
Public Shared Function CreateFromCurves ( 
	doc As Document,
	style As RebarStyle,
	barType As RebarBarType,
	startHook As RebarHookType,
	endHook As RebarHookType,
	host As Element,
	norm As XYZ,
	curves As IList(Of Curve),
	startHookOrient As RebarHookOrientation,
	endHookOrient As RebarHookOrientation,
	useExistingShapeIfPossible As Boolean,
	createNewShape As Boolean
) As Rebar
```

```
public:
[ObsoleteAttribute(L"This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use Rebar.CreateFromCurves(Document doc, RebarStyle style, RebarBarType barType, Element host, XYZ norm, IList<Curve> curves, BarTerminationsData barTerminationsData, bool useExistingShapeIfPossible, bool createNewShape) instead.")]
static Rebar^ CreateFromCurves(
	Document^ doc, 
	RebarStyle style, 
	RebarBarType^ barType, 
	RebarHookType^ startHook, 
	RebarHookType^ endHook, 
	Element^ host, 
	XYZ^ norm, 
	IList<Curve^>^ curves, 
	RebarHookOrientation startHookOrient, 
	RebarHookOrientation endHookOrient, 
	bool useExistingShapeIfPossible, 
	bool createNewShape
)
```

```
[<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use Rebar.CreateFromCurves(Document doc, RebarStyle style, RebarBarType barType, Element host, XYZ norm, IList<Curve> curves, BarTerminationsData barTerminationsData, bool useExistingShapeIfPossible, bool createNewShape) instead.")>]
static member CreateFromCurves : 
        doc : Document * 
        style : RebarStyle * 
        barType : RebarBarType * 
        startHook : RebarHookType * 
        endHook : RebarHookType * 
        host : Element * 
        norm : XYZ * 
        curves : IList<Curve> * 
        startHookOrient : RebarHookOrientation * 
        endHookOrient : RebarHookOrientation * 
        useExistingShapeIfPossible : bool * 
        createNewShape : bool -> Rebar 
```

#### Parameters

doc [Document](../Autodesk.Revit.DB/Document-Class.md)
style [RebarStyle](a9ac65a6-29e6-25e5-caca-502e21385f47.htm)
barType [RebarBarType](Rebar-Bar-Type-Class.md)
startHook [RebarHookType](Rebar-Hook-Type-Class.md)
endHook [RebarHookType](Rebar-Hook-Type-Class.md)
host [Element](../Autodesk.Revit.DB/Element-Class.md)
norm [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)
curves IList [Curve](../Autodesk.Revit.DB/Curve-Class.md)
startHookOrient [RebarHookOrientation](Rebar-Hook-Orientation-Enumeration.md)
endHookOrient [RebarHookOrientation](Rebar-Hook-Orientation-Enumeration.md)
useExistingShapeIfPossible Boolean
createNewShape Boolean

#### Return Value

[Rebar](Rebar-Class.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Rebar Class](Rebar-Class.md) [CreateFromCurves Overload](Rebar-Create-From-Curves-Method.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
