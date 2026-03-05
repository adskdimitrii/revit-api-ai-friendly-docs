# Zone Is Default Zone Property

Source: https://www.revitapidocs.com/2026/1c7ab253-c877-1483-341b-6e0ecec7a849.htm

---

| Zone Is Default Zone Property |
| --- |

**Note: This API is now obsolete.** 

Reports whether this zone is default or not. 
**Namespace:** [Autodesk.Revit.DB.Mechanical](../ungrouped/Autodesk.-Revit.-DB.-Mechanical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This property is deprecated in Revit 2026 and may be removed in a future version of Revit. Please use the GenericZone object and their properties instead.")]
public bool IsDefaultZone { get; set; }
```

```
<ObsoleteAttribute("This property is deprecated in Revit 2026 and may be removed in a future version of Revit. Please use the GenericZone object and their properties instead.")>
Public Property IsDefaultZone As Boolean
	Get
	Set
```

```
public:
[ObsoleteAttribute(L"This property is deprecated in Revit 2026 and may be removed in a future version of Revit. Please use the GenericZone object and their properties instead.")]
property bool IsDefaultZone {
	bool get ();
	void set (bool value);
}
```

```
[<ObsoleteAttribute("This property is deprecated in Revit 2026 and may be removed in a future version of Revit. Please use the GenericZone object and their properties instead.")>]
member IsDefaultZone : bool with get, set
```

#### Property Value

Boolean ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks This property can be used to set the current zone as the default zone. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Zone Class](Zone-Class.md) [Autodesk.Revit.DB.Mechanical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Mechanical-Namespace.md)
