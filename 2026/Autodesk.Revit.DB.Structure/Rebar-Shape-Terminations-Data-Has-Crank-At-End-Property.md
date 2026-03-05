# Rebar Shape Terminations Data Has Crank At End Property

Source: https://www.revitapidocs.com/2026/dd9c6349-e723-7aef-6974-8ebb8114600b.htm

---

| Rebar Shape Terminations Data Has Crank At End Property |
| --- |

Identifies if the rebar shape has crank at end.
 Setting this property to true, will set the HookAngleAtEnd to 0 and EndTreatmentTypeIdAtEnd to ElementId.InvalidElementId. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public bool HasCrankAtEnd { get; set; }
```

```
Public Property HasCrankAtEnd As Boolean
	Get
	Set
```

```
public:
property bool HasCrankAtEnd {
	bool get ();
	void set (bool value);
}
```

```
member HasCrankAtEnd : bool with get, set
```

#### Property Value

Boolean ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarShapeTerminationsData Class](Rebar-Shape-Terminations-Data-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
