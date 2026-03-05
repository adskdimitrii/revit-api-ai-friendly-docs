# Bar Terminations Data Crank Type Id At Start Property

Source: https://www.revitapidocs.com/2026/8cbf6d7a-cb71-eec5-2836-8c4502cd6279.htm

---

| Bar Terminations Data Crank Type Id At Start Property |
| --- |

Identifies the crank type at the start of bar.
 Setting this property to a valid value, will set the HookTypeIdAtStart and EndTreatmentTypeIdAtStart to ElementId.InvalidElementId. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public ElementId CrankTypeIdAtStart { get; set; }
```

```
Public Property CrankTypeIdAtStart As ElementId
	Get
	Set
```

```
public:
property ElementId^ CrankTypeIdAtStart {
	ElementId^ get ();
	void set (ElementId^ value);
}
```

```
member CrankTypeIdAtStart : ElementId with get, set
```

#### Property Value

[ElementId](../Autodesk.Revit.DB/Element-Id-Class.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: crankTypeIdAtStart doesn't represent a crank type. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[BarTerminationsData Class](Bar-Terminations-Data-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
