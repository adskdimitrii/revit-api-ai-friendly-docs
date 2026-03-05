# Conductor Size Diameter Property

Source: https://www.revitapidocs.com/2026/27e36bdd-052b-2b37-a81a-1a2699e40b93.htm

---

| Conductor Size Diameter Property |
| --- |

The diameter of the conductor. 
**Namespace:** [Autodesk.Revit.DB.Electrical](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public double Diameter { get; set; }
```

```
Public Property Diameter As Double
	Get
	Set
```

```
public:
property double Diameter {
	double get ();
	void set (double value);
}
```

```
member Diameter : float with get, set
```

#### Property Value

Double ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The given value for diameter is not finite  \-or\-  When setting this property: The given value for diameter is not a number |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The given value for diameter must be non\-negative. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[ConductorSize Class](Conductor-Size-Class.md) [Autodesk.Revit.DB.Electrical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md)
