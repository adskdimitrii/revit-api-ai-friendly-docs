# Extrusion Analyzer Create Method

Source: https://www.revitapidocs.com/2026/60f25f96-c3f8-8191-a0a9-d298fe5cd10f.htm

---

| Extrusion Analyzer Create Method |
| --- |

Creates an ExtrusionAnalyzer and computes and stores the Solid's shadow. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static ExtrusionAnalyzer Create(
	Solid solidGeometry,
	Plane plane,
	XYZ direction
)
```

```
Public Shared Function Create ( 
	solidGeometry As Solid,
	plane As Plane,
	direction As XYZ
) As ExtrusionAnalyzer
```

```
public:
static ExtrusionAnalyzer^ Create(
	Solid^ solidGeometry, 
	Plane^ plane, 
	XYZ^ direction
)
```

```
static member Create : 
        solidGeometry : Solid * 
        plane : Plane * 
        direction : XYZ -> ExtrusionAnalyzer 
```

#### Parameters

solidGeometry [Solid](7a3b5ac1-c66d-9f81-a11d-9bcd4e026295.htm)
:   The Solid to analyze.

plane [Plane](6a6ee978-f114-558d-3c69-00d289aa855f.htm)
:   The plane to use for the base plane for the extrusion.

direction [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)
:   The direction to use for the calculation for the extrusion.
 The direction must be transverse to the base plane.

#### Return Value

[ExtrusionAnalyzer](Extrusion-Analyzer-Class.md) 
The newly created ExtrusionAnalyzer object. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The input direction must be transverse to the input plane. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | A failure occurred in creating the ExtrusionAnalyzer or computing the Solid's shadow. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[ExtrusionAnalyzer Class](Extrusion-Analyzer-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
