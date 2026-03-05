# Bar Terminations Data Crank Type Id At End Property

Source: https://www.revitapidocs.com/2026/8b7932b6-70cb-a8c0-08b0-84f496e82909.htm

---

| Bar Terminations Data Crank Type Id At End Property |
| --- |

Identifies the crank type at the end of bar.
 Setting this property to a valid value, will set the HookTypeIdAtEnd and EndTreatmentTypeIdAtEnd to ElementId.InvalidElementId. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public ElementId CrankTypeIdAtEnd { get; set; }
```

```
Public Property CrankTypeIdAtEnd As ElementId
	Get
	Set
```

```
public:
property ElementId^ CrankTypeIdAtEnd {
	ElementId^ get ();
	void set (ElementId^ value);
}
```

```
member CrankTypeIdAtEnd : ElementId with get, set
```

#### Property Value

[ElementId](../Autodesk.Revit.DB/Element-Id-Class.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: crankTypeIdAtEnd doesn't represent a crank type. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[BarTerminationsData Class](Bar-Terminations-Data-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
