# Zone Heating Set Point Property

Source: https://www.revitapidocs.com/2026/badb40e3-19a0-155b-38a0-573c3bcba79f.htm

---

| Zone Heating Set Point Property |
| --- |

**Note: This API is now obsolete.** 

Get or set the Heating Set Point of the Zone. 
**Namespace:** [Autodesk.Revit.DB.Mechanical](../ungrouped/Autodesk.-Revit.-DB.-Mechanical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This property is deprecated in Revit 2026 and may be removed in a future version of Revit. Please use the GenericZone and SystemZoneElementType objects instead.")]
public double HeatingSetPoint { get; set; }
```

```
<ObsoleteAttribute("This property is deprecated in Revit 2026 and may be removed in a future version of Revit. Please use the GenericZone and SystemZoneElementType objects instead.")>
Public Property HeatingSetPoint As Double
	Get
	Set
```

```
public:
[ObsoleteAttribute(L"This property is deprecated in Revit 2026 and may be removed in a future version of Revit. Please use the GenericZone and SystemZoneElementType objects instead.")]
property double HeatingSetPoint {
	double get ();
	void set (double value);
}
```

```
[<ObsoleteAttribute("This property is deprecated in Revit 2026 and may be removed in a future version of Revit. Please use the GenericZone and SystemZoneElementType objects instead.")>]
member HeatingSetPoint : float with get, set
```

#### Property Value

Double ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks This property is used to get or set the Heating Set Point of the Zone. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Zone Class](Zone-Class.md) [Autodesk.Revit.DB.Mechanical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Mechanical-Namespace.md)
