# Rebar Create From Curves And Shape(Document, Rebar Shape, Rebar Bar Type, Rebar Hook Type, Rebar Hook Type, Element, XYZ, IList Curve , Rebar Hook Orientation, Rebar Hook Orientation, Double, Double, Element Id, Element Id) Method

Source: https://www.revitapidocs.com/2026/bba959de-0335-e395-61f9-ce45de268a52.htm

---

| Rebar Create From Curves And Shape(Document, Rebar Shape, Rebar Bar Type, Rebar Hook Type, Rebar Hook Type, Element, XYZ, IList Curve , Rebar Hook Orientation, Rebar Hook Orientation, Double, Double, Element Id, Element Id) Method |
| --- |

**Note: This API is now obsolete.** 

  
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use Rebar.CreateFromCurvesAndShape(Document doc, RebarShape rebarShape, RebarBarType barType, Element host, XYZ norm, IList<Curve> curves, BarTerminationsData barTerminationsData) instead.")]
public static Rebar CreateFromCurvesAndShape(
	Document doc,
	RebarShape rebarShape,
	RebarBarType barType,
	RebarHookType startHook,
	RebarHookType endHook,
	Element host,
	XYZ norm,
	IList<Curve> curves,
	RebarHookOrientation startHookOrient,
	RebarHookOrientation endHookOrient,
	double terminationRotationAngleAtStart,
	double terminationRotationAngleAtEnd,
	ElementId endTreatmentTypeIdAtStart,
	ElementId endTreatmentTypeIdAtEnd
)
```

```
<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use Rebar.CreateFromCurvesAndShape(Document doc, RebarShape rebarShape, RebarBarType barType, Element host, XYZ norm, IList<Curve> curves, BarTerminationsData barTerminationsData) instead.")>
Public Shared Function CreateFromCurvesAndShape ( 
	doc As Document,
	rebarShape As RebarShape,
	barType As RebarBarType,
	startHook As RebarHookType,
	endHook As RebarHookType,
	host As Element,
	norm As XYZ,
	curves As IList(Of Curve),
	startHookOrient As RebarHookOrientation,
	endHookOrient As RebarHookOrientation,
	terminationRotationAngleAtStart As Double,
	terminationRotationAngleAtEnd As Double,
	endTreatmentTypeIdAtStart As ElementId,
	endTreatmentTypeIdAtEnd As ElementId
) As Rebar
```

```
public:
[ObsoleteAttribute(L"This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use Rebar.CreateFromCurvesAndShape(Document doc, RebarShape rebarShape, RebarBarType barType, Element host, XYZ norm, IList<Curve> curves, BarTerminationsData barTerminationsData) instead.")]
static Rebar^ CreateFromCurvesAndShape(
	Document^ doc, 
	RebarShape^ rebarShape, 
	RebarBarType^ barType, 
	RebarHookType^ startHook, 
	RebarHookType^ endHook, 
	Element^ host, 
	XYZ^ norm, 
	IList<Curve^>^ curves, 
	RebarHookOrientation startHookOrient, 
	RebarHookOrientation endHookOrient, 
	double terminationRotationAngleAtStart, 
	double terminationRotationAngleAtEnd, 
	ElementId^ endTreatmentTypeIdAtStart, 
	ElementId^ endTreatmentTypeIdAtEnd
)
```

```
[<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use Rebar.CreateFromCurvesAndShape(Document doc, RebarShape rebarShape, RebarBarType barType, Element host, XYZ norm, IList<Curve> curves, BarTerminationsData barTerminationsData) instead.")>]
static member CreateFromCurvesAndShape : 
        doc : Document * 
        rebarShape : RebarShape * 
        barType : RebarBarType * 
        startHook : RebarHookType * 
        endHook : RebarHookType * 
        host : Element * 
        norm : XYZ * 
        curves : IList<Curve> * 
        startHookOrient : RebarHookOrientation * 
        endHookOrient : RebarHookOrientation * 
        terminationRotationAngleAtStart : float * 
        terminationRotationAngleAtEnd : float * 
        endTreatmentTypeIdAtStart : ElementId * 
        endTreatmentTypeIdAtEnd : ElementId -> Rebar 
```

#### Parameters

doc [Document](../Autodesk.Revit.DB/Document-Class.md)
rebarShape [RebarShape](Rebar-Shape-Class.md)
barType [RebarBarType](Rebar-Bar-Type-Class.md)
startHook [RebarHookType](Rebar-Hook-Type-Class.md)
endHook [RebarHookType](Rebar-Hook-Type-Class.md)
host [Element](../Autodesk.Revit.DB/Element-Class.md)
norm [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)
curves IList [Curve](../Autodesk.Revit.DB/Curve-Class.md)
startHookOrient [RebarHookOrientation](Rebar-Hook-Orientation-Enumeration.md)
endHookOrient [RebarHookOrientation](Rebar-Hook-Orientation-Enumeration.md)
terminationRotationAngleAtStart Double
terminationRotationAngleAtEnd Double
endTreatmentTypeIdAtStart [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
endTreatmentTypeIdAtEnd [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)

#### Return Value

[Rebar](Rebar-Class.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Rebar Class](Rebar-Class.md) [CreateFromCurvesAndShape Overload](Rebar-Create-From-Curves-And-Shape-Method.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
