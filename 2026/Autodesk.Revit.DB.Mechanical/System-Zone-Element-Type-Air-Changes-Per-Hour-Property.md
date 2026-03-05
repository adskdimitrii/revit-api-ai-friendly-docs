# System Zone Element Type Air Changes Per Hour Property

Source: https://www.revitapidocs.com/2026/6c93d0e7-462a-c867-9313-2985b4bae1e6.htm

---

| System Zone Element Type Air Changes Per Hour Property |
| --- |

The air changes per hour. 
**Namespace:** [Autodesk.Revit.DB.Mechanical](../ungrouped/Autodesk.-Revit.-DB.-Mechanical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public double AirChangesPerHour { get; set; }
```

```
Public Property AirChangesPerHour As Double
	Get
	Set
```

```
public:
property double AirChangesPerHour {
	double get ();
	void set (double value);
}
```

```
member AirChangesPerHour : float with get, set
```

#### Property Value

Double ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The value should be between \[0\.0,10000]. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[SystemZoneElementType Class](System-Zone-Element-Type-Class.md) [Autodesk.Revit.DB.Mechanical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Mechanical-Namespace.md)
