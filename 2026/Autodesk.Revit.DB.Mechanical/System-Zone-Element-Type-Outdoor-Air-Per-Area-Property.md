# System Zone Element Type Outdoor Air Per Area Property

Source: https://www.revitapidocs.com/2026/5d770e66-4050-e38d-c269-9ec756b55c8e.htm

---

| System Zone Element Type Outdoor Air Per Area Property |
| --- |

The outdoor air per area in unit feet per second. 
**Namespace:** [Autodesk.Revit.DB.Mechanical](../ungrouped/Autodesk.-Revit.-DB.-Mechanical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public double OutdoorAirPerArea { get; set; }
```

```
Public Property OutdoorAirPerArea As Double
	Get
	Set
```

```
public:
property double OutdoorAirPerArea {
	double get ();
	void set (double value);
}
```

```
member OutdoorAirPerArea : float with get, set
```

#### Property Value

Double ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The value should be between \[0\.0,166\.66]. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[SystemZoneElementType Class](System-Zone-Element-Type-Class.md) [Autodesk.Revit.DB.Mechanical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Mechanical-Namespace.md)
