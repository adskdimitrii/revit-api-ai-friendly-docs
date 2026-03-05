# Rebar Shape Terminations Data End Treatment Type Id At Start Property

Source: https://www.revitapidocs.com/2026/f6460a5a-7981-0f65-86d3-fd1c1d41a49c.htm

---

| Rebar Shape Terminations Data End Treatment Type Id At Start Property |
| --- |

Identifies the end treatment type at the start of the rebar shape.
 Setting this property to a valid value, will set the HookAngleAtStart to 0 and HasCrankAtStart to false. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public ElementId EndTreatmentTypeIdAtStart { get; set; }
```

```
Public Property EndTreatmentTypeIdAtStart As ElementId
	Get
	Set
```

```
public:
property ElementId^ EndTreatmentTypeIdAtStart {
	ElementId^ get ();
	void set (ElementId^ value);
}
```

```
member EndTreatmentTypeIdAtStart : ElementId with get, set
```

#### Property Value

[ElementId](../Autodesk.Revit.DB/Element-Id-Class.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: endTreatmentTypeIdAtStart doesn't represent an end treatment type. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarShapeTerminationsData Class](Rebar-Shape-Terminations-Data-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
