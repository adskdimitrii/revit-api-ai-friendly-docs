# Piping System Type Fluid Temperature Property

Source: https://www.revitapidocs.com/2026/e84eb32b-5a1e-acf3-e765-d484d2d6eee4.htm

---

| Piping System Type Fluid Temperature Property |
| --- |

Fluid Temperature, in Kelvin. 
**Namespace:** [Autodesk.Revit.DB.Plumbing](cc553597-37c2-fcd9-6025-d904c129c80a.htm) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public double FluidTemperature { get; set; }
```

```
Public Property FluidTemperature As Double
	Get
	Set
```

```
public:
property double FluidTemperature {
	double get ();
	void set (double value);
}
```

```
member FluidTemperature : float with get, set
```

#### Property Value

Double ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The given value for fluidTemperature is not finite |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks Setter will choose the closest available temperature in settings. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[PipingSystemType Class](b0fe0b71-3b6c-85f0-8279-e93505e82529.htm) [Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.htm)
