# Rebar Create From Curves And Shape(Document, Rebar Shape, Rebar Bar Type, Element, XYZ, IList Curve , Bar Terminations Data) Method

Source: https://www.revitapidocs.com/2026/2ae9c77b-06e2-66c3-6efa-e01abf8115ab.htm

---

| Rebar Create From Curves And Shape(Document, Rebar Shape, Rebar Bar Type, Element, XYZ, IList Curve , Bar Terminations Data) Method |
| --- |

  
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static Rebar CreateFromCurvesAndShape(
	Document doc,
	RebarShape rebarShape,
	RebarBarType barType,
	Element host,
	XYZ norm,
	IList<Curve> curves,
	BarTerminationsData barTerminationsData
)
```

```
Public Shared Function CreateFromCurvesAndShape ( 
	doc As Document,
	rebarShape As RebarShape,
	barType As RebarBarType,
	host As Element,
	norm As XYZ,
	curves As IList(Of Curve),
	barTerminationsData As BarTerminationsData
) As Rebar
```

```
public:
static Rebar^ CreateFromCurvesAndShape(
	Document^ doc, 
	RebarShape^ rebarShape, 
	RebarBarType^ barType, 
	Element^ host, 
	XYZ^ norm, 
	IList<Curve^>^ curves, 
	BarTerminationsData^ barTerminationsData
)
```

```
static member CreateFromCurvesAndShape : 
        doc : Document * 
        rebarShape : RebarShape * 
        barType : RebarBarType * 
        host : Element * 
        norm : XYZ * 
        curves : IList<Curve> * 
        barTerminationsData : BarTerminationsData -> Rebar 
```

#### Parameters

doc [Document](../Autodesk.Revit.DB/Document-Class.md)
rebarShape [RebarShape](Rebar-Shape-Class.md)
barType [RebarBarType](Rebar-Bar-Type-Class.md)
host [Element](../Autodesk.Revit.DB/Element-Class.md)
norm [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)
curves IList [Curve](../Autodesk.Revit.DB/Curve-Class.md)
barTerminationsData [BarTerminationsData](Bar-Terminations-Data-Class.md)

#### Return Value

[Rebar](Rebar-Class.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Rebar Class](Rebar-Class.md) [CreateFromCurvesAndShape Overload](Rebar-Create-From-Curves-And-Shape-Method.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
