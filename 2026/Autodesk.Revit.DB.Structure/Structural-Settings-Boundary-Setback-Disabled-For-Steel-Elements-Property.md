# Structural Settings Boundary Setback Disabled For Steel Elements Property

Source: https://www.revitapidocs.com/2026/e975b36b-0c0e-3925-6804-b72834a9ca3f.htm

---

| Structural Settings Boundary Setback Disabled For Steel Elements Property |
| --- |

Disallow shortening (setbacks) to joined element boundaries for beams and braces. If enabled, then beams and braces will have the setbacks set to 0 by default.
 Explicit setbacks to references will still be allowed. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public bool BoundarySetbackDisabledForSteelElements { get; set; }
```

```
Public Property BoundarySetbackDisabledForSteelElements As Boolean
	Get
	Set
```

```
public:
property bool BoundarySetbackDisabledForSteelElements {
	bool get ();
	void set (bool value);
}
```

```
member BoundarySetbackDisabledForSteelElements : bool with get, set
```

#### Property Value

Boolean ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[StructuralSettings Class](Structural-Settings-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
