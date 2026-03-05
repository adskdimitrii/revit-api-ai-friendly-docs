# Rebar Shape Terminations Data Has Crank At Start Property

Source: https://www.revitapidocs.com/2026/53e2c8a9-4f1b-5f02-0dc8-2ae7c1ddd61b.htm

---

| Rebar Shape Terminations Data Has Crank At Start Property |
| --- |

Identifies if the rebar shape has crank at start.
 Setting this property to true, will set the HookAngleAtStart to 0 and EndTreatmentTypeIdAtStart to ElementId.InvalidElementId. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public bool HasCrankAtStart { get; set; }
```

```
Public Property HasCrankAtStart As Boolean
	Get
	Set
```

```
public:
property bool HasCrankAtStart {
	bool get ();
	void set (bool value);
}
```

```
member HasCrankAtStart : bool with get, set
```

#### Property Value

Boolean ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarShapeTerminationsData Class](Rebar-Shape-Terminations-Data-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
