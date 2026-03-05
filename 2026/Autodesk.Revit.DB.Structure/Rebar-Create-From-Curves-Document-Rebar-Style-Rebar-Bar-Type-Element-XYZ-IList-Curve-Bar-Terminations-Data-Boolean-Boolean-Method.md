# Rebar Create From Curves(Document, Rebar Style, Rebar Bar Type, Element, XYZ, IList Curve , Bar Terminations Data, Boolean, Boolean) Method

Source: https://www.revitapidocs.com/2026/46457aef-7ff3-e133-2ce1-cf143a66e65b.htm

---

| Rebar Create From Curves(Document, Rebar Style, Rebar Bar Type, Element, XYZ, IList Curve , Bar Terminations Data, Boolean, Boolean) Method |
| --- |

  
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static Rebar CreateFromCurves(
	Document doc,
	RebarStyle style,
	RebarBarType barType,
	Element host,
	XYZ norm,
	IList<Curve> curves,
	BarTerminationsData barTerminationsData,
	bool useExistingShapeIfPossible,
	bool createNewShape
)
```

```
Public Shared Function CreateFromCurves ( 
	doc As Document,
	style As RebarStyle,
	barType As RebarBarType,
	host As Element,
	norm As XYZ,
	curves As IList(Of Curve),
	barTerminationsData As BarTerminationsData,
	useExistingShapeIfPossible As Boolean,
	createNewShape As Boolean
) As Rebar
```

```
public:
static Rebar^ CreateFromCurves(
	Document^ doc, 
	RebarStyle style, 
	RebarBarType^ barType, 
	Element^ host, 
	XYZ^ norm, 
	IList<Curve^>^ curves, 
	BarTerminationsData^ barTerminationsData, 
	bool useExistingShapeIfPossible, 
	bool createNewShape
)
```

```
static member CreateFromCurves : 
        doc : Document * 
        style : RebarStyle * 
        barType : RebarBarType * 
        host : Element * 
        norm : XYZ * 
        curves : IList<Curve> * 
        barTerminationsData : BarTerminationsData * 
        useExistingShapeIfPossible : bool * 
        createNewShape : bool -> Rebar 
```

#### Parameters

doc [Document](../Autodesk.Revit.DB/Document-Class.md)
style [RebarStyle](a9ac65a6-29e6-25e5-caca-502e21385f47.htm)
barType [RebarBarType](Rebar-Bar-Type-Class.md)
host [Element](../Autodesk.Revit.DB/Element-Class.md)
norm [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)
curves IList [Curve](../Autodesk.Revit.DB/Curve-Class.md)
barTerminationsData [BarTerminationsData](Bar-Terminations-Data-Class.md)
useExistingShapeIfPossible Boolean
createNewShape Boolean

#### Return Value

[Rebar](Rebar-Class.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Rebar Class](Rebar-Class.md) [CreateFromCurves Overload](Rebar-Create-From-Curves-Method.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
