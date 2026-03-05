# Rebar Shape Rebar Shape Matches Curves And Terminations Data Method

Source: https://www.revitapidocs.com/2026/3902cca7-5188-bfb2-6e25-859a8833fb22.htm

---

| Rebar Shape Rebar Shape Matches Curves And Terminations Data Method |
| --- |

  
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static bool RebarShapeMatchesCurvesAndTerminationsData(
	RebarShape rebarShape,
	RebarBarType barType,
	XYZ norm,
	IList<Curve> curves,
	RebarShapeTerminationsData rebarShapeTerminationsData
)
```

```
Public Shared Function RebarShapeMatchesCurvesAndTerminationsData ( 
	rebarShape As RebarShape,
	barType As RebarBarType,
	norm As XYZ,
	curves As IList(Of Curve),
	rebarShapeTerminationsData As RebarShapeTerminationsData
) As Boolean
```

```
public:
static bool RebarShapeMatchesCurvesAndTerminationsData(
	RebarShape^ rebarShape, 
	RebarBarType^ barType, 
	XYZ^ norm, 
	IList<Curve^>^ curves, 
	RebarShapeTerminationsData^ rebarShapeTerminationsData
)
```

```
static member RebarShapeMatchesCurvesAndTerminationsData : 
        rebarShape : RebarShape * 
        barType : RebarBarType * 
        norm : XYZ * 
        curves : IList<Curve> * 
        rebarShapeTerminationsData : RebarShapeTerminationsData -> bool 
```

#### Parameters

rebarShape [RebarShape](Rebar-Shape-Class.md)
barType [RebarBarType](Rebar-Bar-Type-Class.md)
norm [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)
curves IList [Curve](../Autodesk.Revit.DB/Curve-Class.md)
rebarShapeTerminationsData [RebarShapeTerminationsData](Rebar-Shape-Terminations-Data-Class.md)

#### Return Value

Boolean ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarShape Class](Rebar-Shape-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
