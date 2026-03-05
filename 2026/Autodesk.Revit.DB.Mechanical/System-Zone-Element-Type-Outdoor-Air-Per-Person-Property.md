# System Zone Element Type Outdoor Air Per Person Property

Source: https://www.revitapidocs.com/2026/f70bd0a8-1038-33a4-254c-ef8248cc4ea2.htm

---

| System Zone Element Type Outdoor Air Per Person Property |
| --- |

The outdoor air in unit cubic feet per second per person. 
**Namespace:** [Autodesk.Revit.DB.Mechanical](../ungrouped/Autodesk.-Revit.-DB.-Mechanical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public double OutdoorAirPerPerson { get; set; }
```

```
Public Property OutdoorAirPerPerson As Double
	Get
	Set
```

```
public:
property double OutdoorAirPerPerson {
	double get ();
	void set (double value);
}
```

```
member OutdoorAirPerPerson : float with get, set
```

#### Property Value

Double ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The value should be between \[0\.0,166\.66]. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[SystemZoneElementType Class](System-Zone-Element-Type-Class.md) [Autodesk.Revit.DB.Mechanical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Mechanical-Namespace.md)
