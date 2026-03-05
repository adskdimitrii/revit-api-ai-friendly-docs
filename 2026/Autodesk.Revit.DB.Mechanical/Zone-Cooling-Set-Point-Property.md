# Zone Cooling Set Point Property

Source: https://www.revitapidocs.com/2026/35ef2e5a-26b0-0531-26e6-33ec30bcce0b.htm

---

| Zone Cooling Set Point Property |
| --- |

**Note: This API is now obsolete.** 

Get or set the Cooling Set Point of the Zone. 
**Namespace:** [Autodesk.Revit.DB.Mechanical](../ungrouped/Autodesk.-Revit.-DB.-Mechanical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This property is deprecated in Revit 2026 and may be removed in a future version of Revit. Please use the GenericZone and SystemZoneElementType objects instead.")]
public double CoolingSetPoint { get; set; }
```

```
<ObsoleteAttribute("This property is deprecated in Revit 2026 and may be removed in a future version of Revit. Please use the GenericZone and SystemZoneElementType objects instead.")>
Public Property CoolingSetPoint As Double
	Get
	Set
```

```
public:
[ObsoleteAttribute(L"This property is deprecated in Revit 2026 and may be removed in a future version of Revit. Please use the GenericZone and SystemZoneElementType objects instead.")]
property double CoolingSetPoint {
	double get ();
	void set (double value);
}
```

```
[<ObsoleteAttribute("This property is deprecated in Revit 2026 and may be removed in a future version of Revit. Please use the GenericZone and SystemZoneElementType objects instead.")>]
member CoolingSetPoint : float with get, set
```

#### Property Value

Double ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks This property is used to get or set the Cooling Set Point of the Zone. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Zone Class](Zone-Class.md) [Autodesk.Revit.DB.Mechanical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Mechanical-Namespace.md)
